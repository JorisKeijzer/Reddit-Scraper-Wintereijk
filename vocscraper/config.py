"""Load subreddits.yaml and keywords.csv; import keyword banks from the research spreadsheets."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / "config"
KEYWORD_FIELDS = ["id", "language", "cluster", "term", "priority", "active"]


@dataclass
class Keyword:
    id: str
    language: str
    cluster: str
    term: str
    priority: str
    active: bool


def load_subreddits(path: Path = CONFIG_DIR / "subreddits.yaml") -> dict:
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def subreddit_languages(cfg: dict) -> dict[str, str]:
    return {sub.lower(): group["lang"] for group in cfg["groups"].values() for sub in group["subs"]}


def load_keywords(path: Path = CONFIG_DIR / "keywords.csv") -> list[Keyword]:
    if not path.exists():
        return []
    with open(path, encoding="utf-8", newline="") as fh:
        return [
            Keyword(
                id=row["id"], language=row["language"], cluster=row["cluster"], term=row["term"].strip(),
                priority=row["priority"], active=row["active"].strip().lower() in ("1", "true", "yes", "ja"),
            )
            for row in csv.DictReader(fh)
            if row["term"].strip()
        ]


def save_keywords(keywords: list[Keyword], path: Path = CONFIG_DIR / "keywords.csv") -> None:
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=KEYWORD_FIELDS)
        writer.writeheader()
        for kw in keywords:
            writer.writerow({**kw.__dict__, "active": "yes" if kw.active else "no"})


def import_keyword_xlsx(xlsx: Path, language: str, sheet: str | None = None) -> list[Keyword]:
    """Read a keyword bank sheet. Looks for a column whose header contains 'SEARCH TERM'
    (as in '01 - Copper Insoles - EN Keyword Bank.xlsx'); ID/cluster/priority are optional."""
    import openpyxl

    wb = openpyxl.load_workbook(xlsx, read_only=True, data_only=True)
    ws = wb[sheet] if sheet else wb.worksheets[0]
    rows = ws.iter_rows(values_only=True)
    header = [str(h or "").strip().lower() for h in next(rows)]

    def col(*names: str) -> int | None:
        for i, h in enumerate(header):
            if any(n in h for n in names):
                return i
        return None

    term_i = col("search term", "zoekterm", "suchbegriff", "keyword")
    if term_i is None:
        raise ValueError(f"Geen zoekterm-kolom gevonden in {xlsx} (headers: {header})")
    id_i, cluster_i, prio_i = col("id"), col("cluster"), col("priority", "prioriteit")

    out = []
    for n, row in enumerate(rows, start=1):
        term = row[term_i]
        if not term or not str(term).strip():
            continue
        out.append(
            Keyword(
                id=str(row[id_i]) if id_i is not None and row[id_i] else f"{language.upper()}-{n:03d}",
                language=language,
                cluster=str(row[cluster_i] or "") if cluster_i is not None else "",
                term=str(term).strip().rstrip("."),
                priority=str(row[prio_i] or "") if prio_i is not None else "",
                active=True,
            )
        )
    return out


def merge_keywords(existing: list[Keyword], new: list[Keyword]) -> list[Keyword]:
    """Replace keywords with the same (language, term); keep everything else."""
    key = lambda k: (k.language, k.term.lower())  # noqa: E731
    by_key = {key(k): k for k in existing}
    for kw in new:
        by_key[key(kw)] = kw
    return sorted(by_key.values(), key=lambda k: (k.language, k.id))
