"""Command line: python -m vocscraper <command> --help"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

from . import collect, db, export, label
from .config import import_keyword_xlsx, load_keywords, merge_keywords, save_keywords
from .sources import get_source

DEFAULT_DB = "data/reddit.db"


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="vocscraper", description="Reddit Voice-of-Customer scraper (koperen zolen)")
    parser.add_argument("--db", default=DEFAULT_DB, help=f"SQLite-bestand (standaard {DEFAULT_DB})")
    parser.add_argument("-v", "--verbose", action="store_true")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("import-keywords", help="Zoekwoorden uit een keyword-bank xlsx overnemen in config/keywords.csv")
    p.add_argument("xlsx", type=Path)
    p.add_argument("--language", required=True, choices=["en", "nl", "de"])
    p.add_argument("--sheet", help="Tabblad (standaard het eerste)")

    p = sub.add_parser("collect", help="Posts en reacties ophalen")
    p.add_argument("--source", choices=["arctic", "reddit"], default="arctic",
                   help="arctic = volledige historie (gratis archief); reddit = officiële API / nieuwe posts")
    p.add_argument("--groups", nargs="*", help="Alleen deze groepen uit subreddits.yaml")
    p.add_argument("--since", default="2015-01-01", help="Vanaf datum JJJJ-MM-DD (eerste run)")
    p.add_argument("--max-posts", type=int, help="Max posts per zoekopdracht (handig voor een proefrun)")
    p.add_argument("--sitewide", action="store_true", help="Ook alle zoekwoorden uit keywords.csv sitewide zoeken (alleen reddit)")
    p.add_argument("--keyword-langs", nargs="*", choices=["en", "nl", "de"])
    p.add_argument("--no-comments", action="store_true")
    p.add_argument("--comment-limit", type=int, help="Max aantal threads waarvan reacties opgehaald worden")

    p = sub.add_parser("comments", help="Alleen ontbrekende reacties ophalen")
    p.add_argument("--source", choices=["arctic", "reddit"], default="arctic")
    p.add_argument("--limit", type=int)

    p = sub.add_parser("label", help="Threads labelen met Claude")
    p.add_argument("--limit", type=int, help="Max aantal threads (begin klein!)")
    p.add_argument("--model", default=label.DEFAULT_MODEL)
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--relabel", action="store_true", help="Ook al gelabelde threads opnieuw doen")

    p = sub.add_parser("prepare-labels", help="Threads klaarzetten om in een Claude Code-sessie te labelen")
    p.add_argument("--limit", type=int, help="Max aantal threads")
    p.add_argument("--dir", default="data/labeling")

    p = sub.add_parser("import-labels", help="*.labels.json uit een Claude Code-sessie valideren en opslaan")
    p.add_argument("--dir", default="data/labeling")

    p = sub.add_parser("export", help="Excel-rapport maken")
    p.add_argument("--out", default="exports/reddit_voc.xlsx")
    p.add_argument("--include-irrelevant", action="store_true")

    sub.add_parser("stats", help="Korte telling van de database")

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    if args.command == "import-keywords":
        new = import_keyword_xlsx(args.xlsx, args.language, args.sheet)
        save_keywords(merge_keywords(load_keywords(), new))
        print(f"{len(new)} zoekwoorden ({args.language}) bijgewerkt in config/keywords.csv")
    elif args.command == "collect":
        collect.run(
            args.db, get_source(args.source), groups=args.groups, since=args.since, max_posts=args.max_posts,
            sitewide=args.sitewide, keyword_langs=args.keyword_langs, comments=not args.no_comments,
            comment_limit=args.comment_limit,
        )
    elif args.command == "comments":
        collect.fetch_missing_comments(db.connect(args.db), get_source(args.source), args.limit)
    elif args.command == "label":
        n = label.run(args.db, args.limit, args.model, args.workers, args.relabel)
        print(f"{n} threads gelabeld")
    elif args.command == "prepare-labels":
        paths = label.prepare(args.db, args.dir, args.limit)
        print(f"{len(paths)} batches klaargezet in {args.dir}")
        for path in paths:
            print(f"  {path}")
    elif args.command == "import-labels":
        saved, errors = label.import_labels(args.db, args.dir)
        print(f"{saved} labels opgeslagen")
        for err in errors:
            print(f"  FOUT {err}")
        if errors:
            raise SystemExit(1)
    elif args.command == "export":
        print(f"Geschreven: {export.build(args.db, args.out, args.include_irrelevant)}")
    elif args.command == "stats":
        conn = db.connect(args.db)
        for name, sql in [
            ("posts", "SELECT COUNT(*) FROM posts"),
            ("met reacties opgehaald", "SELECT COUNT(*) FROM posts WHERE comments_fetched_at IS NOT NULL"),
            ("reacties", "SELECT COUNT(*) FROM comments"),
            ("gelabeld", "SELECT COUNT(*) FROM labels"),
            ("relevant", "SELECT COUNT(*) FROM labels WHERE relevant = 1"),
            ("unieke schrijvers", "SELECT COUNT(DISTINCT author_hash) FROM (SELECT author_hash FROM posts UNION ALL SELECT author_hash FROM comments)"),
        ]:
            print(f"{name:>24}: {conn.execute(sql).fetchone()[0]}")
