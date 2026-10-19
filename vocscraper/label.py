"""Label threads with Claude using the ThreadLabel schema (structured outputs)."""

from __future__ import annotations

import logging
import os
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import closing
from datetime import datetime, timezone

import anthropic

from . import db
from .schema import ThreadLabel

log = logging.getLogger(__name__)

DEFAULT_MODEL = os.environ.get("VOC_MODEL", "claude-opus-5-5")
# Bovengrens per thread, zodat megathreads met duizenden reacties de kosten niet opblazen.
# De best gewaardeerde reacties gaan eerst; het aantal weggelaten reacties staat in de prompt.
MAX_COMMENTS = 80
MAX_THREAD_CHARS = 60_000

SYSTEM = """Je bent een marktonderzoeker voor een Nederlands e-commercemerk dat koperen inlegzolen gaat \
verkopen. Je codeert Reddit-threads over voeten, voetklachten, schoenen en inlegzolen volgens een vast codeboek.

Regels:
- Citaten (quotes.text) zijn ALTIJD letterlijk en exact uit de bron overgenomen, inclusief spelfouten. \
Nooit samenvatten, vertalen of verbeteren in dat veld. nl_meaning is een getrouwe vertaling, geen reclametekst.
- Codeer alleen wat er staat. Verzin geen beroep, diagnose of situatie die niet genoemd wordt; gebruik dan null of een lege lijst.
- Scheid eigen ervaring (first_hand=true) van advies uit de tweede hand, diagnoses door vreemden en reclame van fabrikanten.
- Neem ook tegengeluiden en negatieve ervaringen mee: wat NIET werkt is net zo waardevol als wat wel werkt.
- Noteer elke vermelding van koper, magneten, acupressuur of reflexologie, ook sceptische, in 'copper'.
- Een Reddit-reactie bewijst geen klinische werking. Zet claims_risk op 'medical' bij aandoeningen of \
behandelclaims, 'material' bij materiaalclaims (koper, antibacterieel, geur), anders 'comfort_only'.
- medical_red_flag bij diabetes, neuropathie, gevoelloosheid, branden/tintelen, infectie, (stress)fracturen of ernstige zwelling.
- marketing_insight_nl is een hypothese voor ons merk, geen feit; beloof daarin nooit genezing of pijnvermindering.
- Is de thread niet over voeten/schoeisel/zolen (bijv. een toevallige zoekmatch), zet relevant=false en houd de rest minimaal."""


def _fmt_date(ts: int | None) -> str:
    return datetime.fromtimestamp(ts or 0, tz=timezone.utc).strftime("%Y-%m-%d")


def render_thread(conn: sqlite3.Connection, post: sqlite3.Row) -> str:
    comments = conn.execute(
        "SELECT * FROM comments WHERE post_id = ? ORDER BY score DESC", (post["id"],)
    ).fetchall()
    lines = [
        f"SUBREDDIT: r/{post['subreddit']}",
        f"DATUM: {_fmt_date(post['created_utc'])}  SCORE: {post['score']}  REACTIES: {post['num_comments']}",
        f"TITEL: {post['title']}",
        "POST (source_id=post):",
        (post["selftext"] or "").strip() or "(geen tekst)",
        "",
        "REACTIES (gesorteerd op score; source_id tussen haken; OP = vraagsteller):",
    ]
    used, size = 0, sum(len(x) for x in lines)
    for c in comments[:MAX_COMMENTS]:
        who = " OP" if c["author_hash"] and c["author_hash"] == post["author_hash"] else ""
        entry = f"[{c['id']}] (score {c['score']}, diepte {c['depth']}{who}) {c['body'].strip()}"
        if size + len(entry) > MAX_THREAD_CHARS:
            break
        lines.append(entry)
        used += 1
        size += len(entry)
    if used < len(comments):
        lines.append(f"({len(comments) - used} reacties met lagere score weggelaten)")
    return "\n".join(lines)


def label_post(client: anthropic.Anthropic, conn: sqlite3.Connection, post: sqlite3.Row, model: str) -> dict | None:
    thread = render_thread(conn, post)
    response = client.beta.messages.parse(
        model=model,
        max_tokens=16000,
        system=[{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": thread}],
        output_format=ThreadLabel,
        output_config={"effort": "low"},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )
    if response.stop_reason == "refusal":
        log.warning("post %s geweigerd door het model, overgeslagen", post["id"])
        return None
    if response.stop_reason == "max_tokens" or response.parsed_output is None:
        log.warning("post %s: geen geldige output (stop_reason=%s)", post["id"], response.stop_reason)
        return None
    return response.parsed_output.model_dump()


def pending_posts(conn: sqlite3.Connection, limit: int | None, relabel: bool = False) -> list[sqlite3.Row]:
    sql = """SELECT p.* FROM posts p
             LEFT JOIN labels l ON l.post_id = p.id
             WHERE (p.comments_fetched_at IS NOT NULL OR p.num_comments = 0)"""
    if not relabel:
        sql += " AND l.post_id IS NULL"
    sql += " ORDER BY p.num_comments DESC"
    if limit:
        sql += f" LIMIT {int(limit)}"
    return conn.execute(sql).fetchall()


def run(db_path: str, limit: int | None, model: str = DEFAULT_MODEL, workers: int = 4, relabel: bool = False) -> int:
    conn = db.connect(db_path)
    client = anthropic.Anthropic()
    posts = pending_posts(conn, limit, relabel)
    log.info("%d threads te labelen met %s", len(posts), model)
    done = 0
    def task(post: sqlite3.Row) -> dict | None:
        # Elke worker leest via een eigen verbinding; schrijven gebeurt hier op de hoofdthread.
        with closing(db.connect(db_path)) as reader:
            return label_post(client, reader, post, model)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(task, post): post for post in posts}
        for fut in as_completed(futures):
            post = futures[fut]
            try:
                label = fut.result()
            except anthropic.APIStatusError as exc:
                log.error("post %s: API-fout %s", post["id"], exc.status_code)
                continue
            except anthropic.APIConnectionError:
                log.error("post %s: verbindingsfout", post["id"])
                continue
            if label is None:
                continue
            db.save_label(conn, post["id"], model, label)
            conn.commit()
            done += 1
            if done % 25 == 0:
                log.info("%d/%d gelabeld", done, len(posts))
    return done
