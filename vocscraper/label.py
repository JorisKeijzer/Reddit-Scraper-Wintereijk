"""Label threads with Claude using the ThreadLabel schema (structured outputs)."""

from __future__ import annotations

import json
import logging
import os
import re
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path

import anthropic
from pydantic import ValidationError

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


def render_thread(conn: sqlite3.Connection, post: sqlite3.Row, max_chars: int = MAX_THREAD_CHARS) -> str:
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
        if size + len(entry) > max_chars:
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


# --- Labelen binnen een Claude Code-sessie (geen API-sleutel nodig) -------------------------
#
# prepare() schrijft batchbestanden met instructies + threads; de Claude Code-sessie leest een
# batch en schrijft <batch>.labels.json; import_labels() valideert die tegen ThreadLabel en
# slaat ze op. Zie LABELING.md.

SESSION_MODEL = "claude-code-session"
SESSION_THREAD_CHARS = 20_000
BATCH_CHARS = 60_000


def _batch_header(name: str, post_ids: list[str]) -> str:
    return f"""# Label-batch {name}

## Instructies
{SYSTEM}

## Opdracht
Label elke thread hieronder volgens het schema `ThreadLabel` in `vocscraper/schema.py`.
Schrijf het resultaat naar `{name}.labels.json` in dezelfde map, als JSON-lijst:
`[{{"post_id": "...", "label": {{...ThreadLabel...}}}}, ...]`, één item per thread
({len(post_ids)} threads: {", ".join(post_ids)}).
Importeer daarna met: `python -m vocscraper import-labels`

"""


def prepare(db_path: str, out_dir: str, limit: int | None, batch_chars: int = BATCH_CHARS) -> list[Path]:
    """Write pending threads into batch files of roughly batch_chars characters."""
    conn = db.connect(db_path)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    # Threads die al in een nog niet geïmporteerde batch staan niet opnieuw klaarzetten.
    queued = set()
    for f in out.glob("batch_*.md"):
        queued.update(re.findall(r"^=== THREAD (\S+) ===$", f.read_text(encoding="utf-8"), flags=re.M))
    posts = [p for p in pending_posts(conn, None) if p["id"] not in queued][: limit or None]
    existing = sorted(out.glob("batch_*.md")) + sorted((out / "imported").glob("batch_*.md"))
    next_no = max((int(re.search(r"\d+", f.stem).group()) for f in existing), default=0) + 1

    written, current, size = [], [], 0

    def flush():
        nonlocal current, size, next_no
        if not current:
            return
        name = f"batch_{next_no:04d}"
        body = "".join(text for _, text in current)
        path = out / f"{name}.md"
        path.write_text(_batch_header(name, [pid for pid, _ in current]) + body, encoding="utf-8")
        written.append(path)
        current, size, next_no = [], 0, next_no + 1

    for post in posts:
        text = f"=== THREAD {post['id']} ===\n{render_thread(conn, post, SESSION_THREAD_CHARS)}\n\n"
        if current and size + len(text) > batch_chars:
            flush()
        current.append((post["id"], text))
        size += len(text)
    flush()
    return written


def import_labels(db_path: str, in_dir: str) -> tuple[int, list[str]]:
    """Validate and store every *.labels.json in in_dir; move imported batches to imported/."""
    conn = db.connect(db_path)
    src = Path(in_dir)
    done_dir = src / "imported"
    done_dir.mkdir(parents=True, exist_ok=True)
    saved, errors = 0, []
    for f in sorted(src.glob("*.labels.json")):
        try:
            items = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{f.name}: geen geldige JSON ({exc})")
            continue
        ok = True
        for item in items:
            post_id = item.get("post_id")
            if not conn.execute("SELECT 1 FROM posts WHERE id = ?", (post_id,)).fetchone():
                errors.append(f"{f.name}: onbekende post_id {post_id}")
                ok = False
                continue
            try:
                label = ThreadLabel.model_validate(item.get("label")).model_dump()
            except ValidationError as exc:
                errors.append(f"{f.name} / {post_id}: {exc.error_count()} schemafouten, bijv. {exc.errors()[0]['loc']}: {exc.errors()[0]['msg']}")
                ok = False
                continue
            db.save_label(conn, post_id, SESSION_MODEL, label)
            saved += 1
        conn.commit()
        if ok:
            f.rename(done_dir / f.name)
            batch = f.with_name(f.name.replace(".labels.json", ".md"))
            if batch.exists():
                batch.rename(done_dir / batch.name)
    return saved, errors


def pending_posts(conn: sqlite3.Connection, limit: int | None, relabel: bool = False) -> list[sqlite3.Row]:
    sql = """SELECT p.* FROM posts p
             LEFT JOIN labels l ON l.post_id = p.id
             WHERE (p.comments_fetched_at IS NOT NULL OR p.num_comments = 0)"""
    if not relabel:
        sql += " AND l.post_id IS NULL"
    # Voorrang: eerst threads over koper/magneten, dan threads met reacties (meeste eerst);
    # threads zonder reacties komen achteraan.
    sql += """ ORDER BY
        (lower(p.title || ' ' || coalesce(p.selftext, '')) LIKE '%copper%'
         OR lower(p.title || ' ' || coalesce(p.selftext, '')) LIKE '%koper%'
         OR lower(p.title || ' ' || coalesce(p.selftext, '')) LIKE '%kupfer%'
         OR lower(p.title || ' ' || coalesce(p.selftext, '')) LIKE '%magnetic insole%') DESC,
        (p.num_comments > 0) DESC,
        p.num_comments DESC"""
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
