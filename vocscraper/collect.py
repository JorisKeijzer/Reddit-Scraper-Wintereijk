"""Collect posts and comments into SQLite according to config/subreddits.yaml and keywords.csv."""

from __future__ import annotations

import logging
import sqlite3
import time
from dataclasses import dataclass
from datetime import datetime, timezone

from . import db
from .config import load_keywords, load_subreddits, subreddit_languages

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class Job:
    subreddit: str | None  # None = sitewide
    query: str | None  # None = hele subreddit
    lang: str


def build_jobs(cfg: dict, groups: list[str] | None, sitewide_keywords: list) -> list[Job]:
    jobs: list[Job] = []
    for name, group in cfg["groups"].items():
        if groups and name not in groups:
            continue
        terms = list(cfg["anchors"].get(group["lang"], []))
        if group.get("copper"):
            terms += cfg.get("copper_anchors", [])
        for sub in group["subs"]:
            if group["mode"] == "all":
                jobs.append(Job(sub, None, group["lang"]))
            else:
                jobs.extend(Job(sub, term, group["lang"]) for term in terms)
    jobs.extend(Job(None, kw.term, kw.language) for kw in sitewide_keywords)
    return jobs


def _since_ts(since: str | None) -> int | None:
    if not since:
        return None
    return int(datetime.strptime(since, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())


def is_excluded(post: dict, phrases: list[str]) -> bool:
    text = f"{post.get('title') or ''} {post.get('selftext') or ''}".lower()
    return any(p.lower() in text for p in phrases)


def run_job(
    conn: sqlite3.Connection, source, job: Job, since: int | None, max_posts: int | None, langs: dict,
    exclude: list[str] = (),
) -> int:
    sub_key, query_key = job.subreddit or "*", job.query or "*"
    after = db.get_newest(conn, source.name, sub_key, query_key) or since
    new, newest = 0, None
    for post in source.search_posts(job.subreddit, job.query, after, max_posts):
        if not post["id"] or not post["subreddit"]:
            continue
        newest = max(newest or 0, post["created_utc"])
        if job.query and is_excluded(post, exclude):
            continue
        post["lang_hint"] = langs.get(post["subreddit"].lower(), job.lang)
        new += db.upsert_post(conn, post, f"{sub_key}|{query_key}")
        if new and new % 100 == 0:
            conn.commit()
    db.log_query(conn, source.name, sub_key, query_key, newest)
    conn.commit()
    return new


def _last_run(conn: sqlite3.Connection, source_name: str, job: Job) -> int:
    row = conn.execute(
        "SELECT last_run FROM query_log WHERE source = ? AND subreddit = ? AND query = ?",
        (source_name, job.subreddit or "*", job.query or "*"),
    ).fetchone()
    return row["last_run"] if row and row["last_run"] else 0


def fetch_missing_comments(conn: sqlite3.Connection, source, limit: int | None = None, deadline: float | None = None) -> int:
    sql = "SELECT id FROM posts WHERE comments_fetched_at IS NULL AND num_comments > 0 ORDER BY num_comments DESC"
    if limit:
        sql += f" LIMIT {int(limit)}"
    ids = [r["id"] for r in conn.execute(sql)]
    log.info("reacties ophalen voor %d posts", len(ids))
    for n, post_id in enumerate(ids, start=1):
        if deadline and time.monotonic() > deadline:
            log.info("tijdbudget op na %d/%d threads met reacties", n - 1, len(ids))
            break
        try:
            db.replace_comments(conn, post_id, source.fetch_comments(post_id))
        except Exception:  # volgende run probeert deze post opnieuw
            log.exception("reacties van %s mislukt", post_id)
        if n % 50 == 0:
            conn.commit()
            log.info("%d/%d threads met reacties", n, len(ids))
    conn.commit()
    return len(ids)


def run(
    db_path: str,
    source,
    groups: list[str] | None = None,
    since: str | None = "2015-01-01",
    max_posts: int | None = None,
    sitewide: bool = False,
    keyword_langs: list[str] | None = None,
    comments: bool = True,
    comment_limit: int | None = None,
    time_budget_min: float | None = None,
) -> None:
    """With time_budget_min, stop starting new work once the budget is spent (the rest follows
    in the next run). Jobs that ran longest ago go first, so every job gets its turn."""
    deadline = time.monotonic() + time_budget_min * 60 if time_budget_min else None
    conn = db.connect(db_path)
    cfg = load_subreddits()
    langs = subreddit_languages(cfg)
    keywords = []
    if sitewide:
        if not source.supports_sitewide:
            raise SystemExit("Sitewide zoeken kan alleen met --source reddit")
        keywords = [k for k in load_keywords() if k.active and (not keyword_langs or k.language in keyword_langs)]
    jobs = sorted(build_jobs(cfg, groups, keywords), key=lambda j: _last_run(conn, source.name, j))
    log.info("%d zoekopdrachten via %s", len(jobs), source.name)
    total = 0
    # Ongeveer twee derde van het budget voor zoeken, de rest voor reacties.
    search_deadline = deadline - time_budget_min * 20 if deadline else None
    for n, job in enumerate(jobs, start=1):
        if search_deadline and time.monotonic() > search_deadline:
            log.info("tijdbudget voor zoeken op na %d/%d zoekopdrachten", n - 1, len(jobs))
            break
        try:
            added = run_job(conn, source, job, _since_ts(since), max_posts, langs, cfg.get("exclude_phrases", []))
        except Exception:  # één kapotte subreddit/zoekterm mag de run niet stoppen
            log.exception("zoekopdracht mislukt: %s", job)
            continue
        total += added
        log.info("[%d/%d] r/%s '%s': %d nieuw", n, len(jobs), job.subreddit or "*", job.query or "*", added)
    log.info("klaar: %d nieuwe posts", total)
    if comments:
        fetch_missing_comments(conn, source, comment_limit, deadline)
