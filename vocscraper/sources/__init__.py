from .arctic_shift import ArcticShiftSource
from .reddit import RedditSource


def get_source(name: str):
    if name == "arctic":
        return ArcticShiftSource()
    if name == "reddit":
        return RedditSource()
    raise ValueError(f"Onbekende bron: {name} (kies arctic of reddit)")
