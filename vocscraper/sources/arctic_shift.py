"""Arctic Shift: free archive of Reddit history (https://github.com/ArthurHeitmann/arctic_shift).

Used for the initial bulk download: every post in a subreddit since a given date, optionally
filtered by a full-text query. Full-text search needs a subreddit, so sitewide keyword search
goes through the official API instead.
"""

from __future__ import annotations

import logging
import time
from typing import Iterator

from .common import normalize_post, walk_comment_tree
from .http import HttpClient

log = logging.getLogger(__name__)

BASE = "https://arctic-shift.photon-reddit.com/api"
PAGE = 100


class ArcticShiftSource:
    name = "arctic_shift"
    supports_sitewide = False

    def __init__(self, http: HttpClient | None = None, retry_delays: tuple[int, ...] = (5, 15, 30)):
        self.http = http or HttpClient(min_interval=2.0)
        self.retry_delays = retry_delays

    def _search(self, params: dict) -> list[dict]:
        """Full-text search often answers 'Timeout. Maybe slow down a bit'; retry with pauses."""
        for delay in (0, *self.retry_delays):
            if delay:
                time.sleep(delay)
            payload = self.http.get_json(f"{BASE}/posts/search", params=params) or {}
            if not payload.get("error"):
                return payload.get("data") or []
            log.debug("arctic shift: %s (%s)", payload["error"], params)
        raise RuntimeError(f"Arctic Shift blijft time-outs geven: {params}")

    def search_posts(
        self, subreddit: str | None, query: str | None, after_utc: int | None, max_posts: int | None
    ) -> Iterator[dict]:
        """Without a query: every post in the subreddit. With a query: separate passes over the
        title and the selftext (the combined 'query' parameter times out on large subreddits).
        If a pass keeps failing, the other pass still runs and the job is reported as failed
        afterwards, so the next run tries it again."""
        if not subreddit:
            raise ValueError("Arctic Shift heeft een subreddit nodig")
        failed = []
        for field in ("title", "selftext") if query else (None,):
            params = {"subreddit": subreddit, "limit": PAGE, "sort": "asc"}
            if field:
                params[field] = query
            after, seen = after_utc or 0, 0
            try:
                while True:
                    params["after"] = after
                    items = self._search(dict(params))
                    for raw in items:
                        yield normalize_post(raw, self.name)
                        seen += 1
                        if max_posts and seen >= max_posts:
                            break
                    if not items or len(items) < PAGE or (max_posts and seen >= max_posts):
                        break
                    newest = max(int(float(i.get("created_utc") or 0)) for i in items)
                    if newest <= after:
                        break
                    after = newest
            except RuntimeError as exc:
                log.warning("r/%s '%s' via %s mislukt: %s", subreddit, query, field, exc)
                failed.append(field)
        if failed:
            raise RuntimeError(f"r/{subreddit} '{query}': {', '.join(map(str, failed))} mislukt, volgende run opnieuw")

    def fetch_comments(self, post_id: str) -> list[dict]:
        for delay in (0, *self.retry_delays):
            if delay:
                time.sleep(delay)
            payload = self.http.get_json(f"{BASE}/comments/tree", params={"link_id": f"t3_{post_id}", "limit": 9999}) or {}
            if not payload.get("error"):
                return walk_comment_tree(payload.get("data") or [])
        raise RuntimeError(f"Arctic Shift blijft time-outs geven voor reacties van {post_id}")
