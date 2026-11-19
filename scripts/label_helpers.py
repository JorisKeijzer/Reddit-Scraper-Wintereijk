"""Hulpfuncties om labels binnen een Claude Code-sessie te schrijven (zie LABELING.md).

Gebruik in een eigen script:

    from label_helpers import L, S, Q, CU, irrelevant, write_labels
    labels = {"abc123": L(problem_summary_nl="...", quotes=[Q("...", "post", "pain", "...")])}
    write_labels(labels, "data/labeling")

write_labels schrijft per klaargezette batch een <batch>.labels.json en controleert dat elke
thread in de batches een label heeft.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


def L(**kw):
    base = dict(
        relevant=True, language="en", thread_type="asking_help", problem_summary_nl="", regions=[], conditions=[],
        diagnosed_by_professional=None, occupation=None, situations=[], duration=None, previous_fixes=[],
        complaints_about_products=[], desired_outcomes_nl=[], solutions=[], brands_mentioned=[],
        copper={"mentioned": False, "sentiment": "not_mentioned", "summary_nl": ""}, price_mentions=[], quotes=[],
        emotional_intensity=2, medical_red_flag=False, claims_risk="comfort_only", marketing_insight_nl="",
    )
    base.update(kw)
    return base


def S(solution, category, verdict, reason, source_id, brand=None, first_hand=True):
    return dict(solution=solution, category=category, brand_or_product=brand, verdict=verdict,
                first_hand=first_hand, reason=reason, source_id=source_id)


def Q(text, source_id, kind, nl):
    return dict(text=text, source_id=source_id, kind=kind, nl_meaning=nl)


def CU(sentiment, summary_nl):
    return {"mentioned": True, "sentiment": sentiment, "summary_nl": summary_nl}


def irrelevant(summary, lang="en", note="Niet relevant."):
    return L(relevant=False, language=lang, thread_type="discussion", problem_summary_nl=summary,
             emotional_intensity=1, marketing_insight_nl=note)


def write_labels(labels: dict, directory: str = "data/labeling") -> None:
    missing = []
    for batch in sorted(Path(directory).glob("batch_*.md")):
        ids = re.findall(r"^=== THREAD (\S+) ===$", batch.read_text(encoding="utf-8"), flags=re.M)
        missing += [i for i in ids if i not in labels]
        items = [{"post_id": i, "label": labels[i]} for i in ids if i in labels]
        batch.with_name(batch.stem + ".labels.json").write_text(
            json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
        print(batch.name, len(items))
    if missing:
        raise SystemExit(f"Geen label voor: {', '.join(missing)}")
