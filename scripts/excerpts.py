"""Korte uittreksels van klaargezette threads, om snel te kunnen lezen tijdens het labelen.

    python scripts/excerpts.py [aantal_reacties] [overslaan,ids] > uittreksels.txt
"""

import pathlib
import re
import sys

ncom = int(sys.argv[1]) if len(sys.argv) > 1 else 10
skip = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else set()
for f in sorted(pathlib.Path("data/labeling").glob("batch_*.md")):
    for part in re.split(r"^=== THREAD ", f.read_text(encoding="utf-8"), flags=re.M)[1:]:
        pid = part.split(" ")[0]
        if pid in skip:
            continue
        lines = part.split("\n")
        start = next(i for i, l in enumerate(lines) if l.startswith("REACTIES ("))
        print("#####", pid)
        print("\n".join(l for l in lines[1:start] if l.strip())[:1500])
        for c in [l for l in lines[start + 1:] if l.startswith("[")][:ncom]:
            print(" ", c[:300])
