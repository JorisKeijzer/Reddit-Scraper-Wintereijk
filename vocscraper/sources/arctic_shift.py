"""Arctic Shift: free archive of Reddit history (https://github.com/ArthurHeitmann/arctic_shift).

Used for the initial bulk download: every post in a subreddit since a given date, optionally
filtered by a full-text query. Full-text search needs a subreddit, so sitewide keyword search
goes through the official API instead.
"""

from __future__ import annotations

import logging
from typing import Iterator

from .common import normalize_post, walk_comment_tree
from .http import HttpClient

log = logging.getLogger(__name__)

BASE = "https://arctic-shift.photon-reddit.com/api"
PAGE = 100


class ArcticShiftSource:
    name = "arctic_shift"
    supports_sitewide = False

    def __init__(self, http: HttpClient | None = None):
        self.http = http or HttpClient(min_interval=1.0)

    def search_posts(
        self, subreddit: str | None, query: str | None, after_utc: int | None, max_posts: int | None
    ) -> Iterator[dict]:
        if not subreddit:
            raise ValueError("Arctic Shift heeft een subreddit nodig")
        params = {"subreddit": subreddit, "limit": PAGE, "sort": "asc"}
        if query:
            params["query"] = query
        after = after_utc or 0
        seen = 0
        while True:
            params["after"] = after
            payload = self.http.get_json(f"{BASE}/posts/search", params=params)
            items = (payload or {}).get("data") or []
            if not items:
                return
            for raw in items:
                post = normalize_post(raw, self.name)
                yield post
                seen += 1
                if max_posts and seen >= max_posts:
                    return
            newest = max(int(float(i.get("created_utc") or 0)) for i in items)
            if len(items) < PAGE or newest <= after:
                return
            after = newest

    def fetch_comments(self, post_id: str) -> list[dict]:
        payload = self.http.get_json(f"{BASE}/comments/tree", params={"link_id": f"t3_{post_id}", "limit": 9999})
        return walk_comment_tree((payload or {}).get("data") or [])
