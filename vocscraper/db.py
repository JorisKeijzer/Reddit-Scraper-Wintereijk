"""SQLite storage: posts, comments, labels and an incremental query log."""

from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import time
from pathlib import Path
from typing import Iterable

SCHEMA = """
CREATE TABLE IF NOT EXISTS posts (
    id            TEXT PRIMARY KEY,      -- reddit base36 id, zonder t3_
    subreddit     TEXT NOT NULL,
    title         TEXT,
    selftext      TEXT,
    author_hash   TEXT,                  -- gepseudonimiseerd, geen gebruikersnaam
    created_utc   INTEGER,
    score         INTEGER,
    num_comments  INTEGER,
    permalink     TEXT,
    url           TEXT,
    lang_hint     TEXT,                  -- taal van de subreddit uit config
    source        TEXT,                  -- arctic_shift / reddit_api / reddit_public
    first_query   TEXT,                  -- zoekopdracht waarmee de post gevonden werd
    fetched_at    INTEGER,
    comments_fetched_at INTEGER
);
CREATE TABLE IF NOT EXISTS post_matches (
    post_id TEXT NOT NULL,
    query   TEXT NOT NULL,
    PRIMARY KEY (post_id, query)
);
CREATE TABLE IF NOT EXISTS comments (
    id          TEXT PRIMARY KEY,
    post_id     TEXT NOT NULL,
    parent_id   TEXT,
    body        TEXT,
    author_hash TEXT,
    created_utc INTEGER,
    score       INTEGER,
    depth       INTEGER
);
CREATE INDEX IF NOT EXISTS comments_post ON comments(post_id);
CREATE TABLE IF NOT EXISTS labels (
    post_id     TEXT PRIMARY KEY,
    model       TEXT,
    labeled_at  INTEGER,
    relevant    INTEGER,
    data        TEXT                     -- ThreadLabel als JSON
);
CREATE TABLE IF NOT EXISTS query_log (
    source      TEXT NOT NULL,
    subreddit   TEXT NOT NULL,           -- '*' voor sitewide
    query       TEXT NOT NULL,           -- '*' voor hele subreddit
    last_run    INTEGER,
    newest_utc  INTEGER,
    PRIMARY KEY (source, subreddit, query)
);
"""

_SALT = os.environ.get("AUTHOR_HASH_SALT", "wintereijk-voc")


def hash_author(author: str | None) -> str | None:
    if not author or author in ("[deleted]", "AutoModerator"):
        return author
    return hashlib.sha256((_SALT + author).encode()).hexdigest()[:16]


def connect(path: str | Path) -> sqlite3.Connection:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path, timeout=60)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")  # verzamelen en labelen mogen tegelijk draaien
    conn.executescript(SCHEMA)
    return conn


def upsert_post(conn: sqlite3.Connection, post: dict, query: str) -> bool:
    """Insert or refresh a post. Returns True when the post is new."""
    exists = conn.execute("SELECT 1 FROM posts WHERE id = ?", (post["id"],)).fetchone()
    if exists:
        conn.execute(
            "UPDATE posts SET score = ?, num_comments = ? WHERE id = ?",
            (post.get("score"), post.get("num_comments"), post["id"]),
        )
    else:
        conn.execute(
            """INSERT INTO posts (id, subreddit, title, selftext, author_hash, created_utc,
                   score, num_comments, permalink, url, lang_hint, source, first_query, fetched_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                post["id"], post["subreddit"], post.get("title"), post.get("selftext"),
                hash_author(post.get("author")), post.get("created_utc"), post.get("score"),
                post.get("num_comments"), post.get("permalink"), post.get("url"),
                post.get("lang_hint"), post.get("source"), query, int(time.time()),
            ),
        )
    conn.execute("INSERT OR IGNORE INTO post_matches VALUES (?, ?)", (post["id"], query))
    return not exists


def replace_comments(conn: sqlite3.Connection, post_id: str, comments: Iterable[dict]) -> int:
    rows = [
        (
            c["id"], post_id, c.get("parent_id"), c.get("body"), hash_author(c.get("author")),
            c.get("created_utc"), c.get("score"), c.get("depth"),
        )
        for c in comments
    ]
    conn.executemany("INSERT OR REPLACE INTO comments VALUES (?, ?, ?, ?, ?, ?, ?, ?)", rows)
    conn.execute("UPDATE posts SET comments_fetched_at = ? WHERE id = ?", (int(time.time()), post_id))
    return len(rows)


def get_newest(conn: sqlite3.Connection, source: str, subreddit: str, query: str) -> int | None:
    row = conn.execute(
        "SELECT newest_utc FROM query_log WHERE source = ? AND subreddit = ? AND query = ?",
        (source, subreddit, query),
    ).fetchone()
    return row["newest_utc"] if row else None


def log_query(conn: sqlite3.Connection, source: str, subreddit: str, query: str, newest_utc: int | None) -> None:
    previous = get_newest(conn, source, subreddit, query)
    newest = max(filter(None, [previous, newest_utc]), default=None)
    conn.execute(
        "INSERT OR REPLACE INTO query_log VALUES (?, ?, ?, ?, ?)",
        (source, subreddit, query, int(time.time()), newest),
    )


def save_label(conn: sqlite3.Connection, post_id: str, model: str, label: dict) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO labels VALUES (?, ?, ?, ?, ?)",
        (post_id, model, int(time.time()), int(bool(label.get("relevant"))), json.dumps(label, ensure_ascii=False)),
    )
