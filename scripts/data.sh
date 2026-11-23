#!/usr/bin/env bash
# De SQLite-database staat niet op de werkbranch maar als gzip op de branch
# 'voc-data'. Die branch heeft steeds maar één commit (force-push), zodat de git-historie niet
# elke dag een volledige kopie van de database erbij krijgt. De labels zelf staan ook als JSON
# in data/labeling/imported/ op de werkbranch.
# Omdat GitHub geen bestanden boven 100 MB accepteert, wordt de gzip in delen van 45 MB
# opgeslagen (reddit.db.gz.part-aa, -ab, ...). restore plakt ze weer aan elkaar en kan ook
# nog het oude enkele bestand reddit.db.gz lezen.
#
#   scripts/data.sh restore   haal data/reddit.db op van origin/voc-data
#   scripts/data.sh save      zet data/reddit.db op origin/voc-data
set -euo pipefail
cd "$(dirname "$0")/.."
DB=data/reddit.db
BRANCH=voc-data

case "${1:-}" in
  restore)
    if git fetch -q origin "$BRANCH" 2>/dev/null; then
      mkdir -p data
      parts=$(git ls-tree --name-only "origin/$BRANCH" | grep '^reddit\.db\.gz' | LC_ALL=C sort)
      for p in $parts; do git show "origin/$BRANCH:$p"; done | gunzip > "$DB"
      echo "database teruggezet: $(du -h "$DB" | cut -f1)"
    else
      echo "nog geen $BRANCH-branch; we beginnen met een lege database"
    fi
    ;;
  save)
    python3 -c "import sqlite3; c = sqlite3.connect('$DB'); c.execute('PRAGMA wal_checkpoint(TRUNCATE)'); c.close()"
    tmp=$(mktemp -d)
    gzip -9 -c "$DB" | split -b 45m - "$tmp/reddit.db.gz.part-"
    tree=$(for f in "$tmp"/reddit.db.gz.part-*; do
      printf '100644 blob %s\t%s\n' "$(git hash-object -w "$f")" "$(basename "$f")"
    done | git mktree)
    rm -rf "$tmp"
    commit=$(git commit-tree "$tree" -m "Database-snapshot $(date -u +%Y-%m-%dT%H:%MZ)")
    for delay in 0 2 4 8 16; do
      sleep "$delay"
      git push -q -f origin "$commit:refs/heads/$BRANCH" && { echo "database opgeslagen op $BRANCH"; exit 0; }
    done
    echo "opslaan mislukt" >&2
    exit 1
    ;;
  *)
    echo "gebruik: scripts/data.sh restore|save" >&2
    exit 2
    ;;
esac
