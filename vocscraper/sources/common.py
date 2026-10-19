"""Normalise raw Reddit-shaped JSON (official API and Arctic Shift share the field names)."""

from __future__ import annotations


def _strip_prefix(value: str | None) -> str | None:
    if value and len(value) > 3 and value[2] == "_":
        return value[3:]
    return value


def normalize_post(raw: dict, source: str) -> dict:
    data = raw.get("data", raw) if raw.get("kind") == "t3" else raw
    permalink = data.get("permalink") or ""
    return {
        "id": _strip_prefix(data.get("id") or data.get("name")),
        "subreddit": data.get("subreddit"),
        "title": data.get("title"),
        "selftext": data.get("selftext"),
        "author": data.get("author"),
        "created_utc": int(float(data.get("created_utc") or 0)),
        "score": data.get("score"),
        "num_comments": data.get("num_comments"),
        "permalink": f"https://www.reddit.com{permalink}" if permalink.startswith("/") else permalink,
        "url": data.get("url"),
        "source": source,
    }


def normalize_comment(data: dict, depth: int) -> dict:
    return {
        "id": _strip_prefix(data.get("id") or data.get("name")),
        "parent_id": data.get("parent_id"),
        "body": data.get("body"),
        "author": data.get("author"),
        "created_utc": int(float(data.get("created_utc") or 0)),
        "score": data.get("score"),
        "depth": data.get("depth", depth),
    }


def walk_comment_tree(nodes: list, depth: int = 0) -> list[dict]:
    """Flatten a Reddit comment tree. Accepts listing children ({kind, data}) or bare comment
    dicts, with replies either as a Listing or as a list. Skips 'more' stubs and removed bodies."""
    out: list[dict] = []
    for node in nodes or []:
        if not isinstance(node, dict):
            continue
        if node.get("kind") == "more":
            continue
        data = node.get("data", node) if "kind" in node else node
        if data.get("body") and data.get("body") not in ("[deleted]", "[removed]"):
            out.append(normalize_comment(data, depth))
        replies = data.get("replies") or node.get("children")
        if isinstance(replies, dict):
            replies = replies.get("data", {}).get("children", [])
        if isinstance(replies, list):
            out.extend(walk_comment_tree(replies, depth + 1))
    return out
