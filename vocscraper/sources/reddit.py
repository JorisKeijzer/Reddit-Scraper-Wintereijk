"""Official Reddit API (OAuth, app-only) with a fallback to the public .json pages.

With REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET set we use oauth.reddit.com (about 100 requests per
minute). Without them we use www.reddit.com/....json at a slow pace; fine for a trial, not for
scheduled runs. Reddit search returns at most a few hundred results per query, which is why
the bulk history comes from Arctic Shift and this source handles weekly updates and sitewide search.
"""

from __future__ import annotations

import logging
import os
import time
from typing import Iterator

import requests

from .common import normalize_post, walk_comment_tree
from .http import USER_AGENT, HttpClient

log = logging.getLogger(__name__)


class RedditSource:
    supports_sitewide = True

    def __init__(self, http: HttpClient | None = None):
        self.client_id = os.environ.get("REDDIT_CLIENT_ID")
        self.client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
        self.oauth = bool(self.client_id and self.client_secret)
        self.name = "reddit_api" if self.oauth else "reddit_public"
        self.http = http or HttpClient(min_interval=0.7 if self.oauth else 6.0)
        self._token: str | None = None
        self._token_expires = 0.0

    def _auth_headers(self) -> dict:
        if not self.oauth:
            return {}
        if not self._token or time.time() > self._token_expires - 60:
            resp = requests.post(
                "https://www.reddit.com/api/v1/access_token",
                auth=(self.client_id, self.client_secret),
                data={"grant_type": "client_credentials"},
                headers={"User-Agent": USER_AGENT},
                timeout=30,
            )
            resp.raise_for_status()
            body = resp.json()
            self._token = body["access_token"]
            self._token_expires = time.time() + body.get("expires_in", 3600)
        return {"Authorization": f"bearer {self._token}"}

    def _get(self, path: str, params: dict) -> dict | list | None:
        if self.oauth:
            url = f"https://oauth.reddit.com{path}"
        else:
            url = f"https://www.reddit.com{path}.json"
        return self.http.get_json(url, params={**params, "raw_json": 1}, headers=self._auth_headers())

    def search_posts(
        self, subreddit: str | None, query: str | None, after_utc: int | None, max_posts: int | None
    ) -> Iterator[dict]:
        """Newest first; stops at posts older than after_utc (incremental runs)."""
        if query:
            path = f"/r/{subreddit}/search" if subreddit else "/search"
            params = {"q": query, "sort": "new", "t": "all", "limit": 100, "type": "link"}
            if subreddit:
                params["restrict_sr"] = 1
        elif subreddit:
            path, params = f"/r/{subreddit}/new", {"limit": 100}
        else:
            raise ValueError("query of subreddit nodig")
        seen = 0
        after_token = None
        while True:
            if after_token:
                params["after"] = after_token
            payload = self._get(path, params)
            listing = (payload or {}).get("data") or {}
            children = listing.get("children") or []
            for child in children:
                post = normalize_post(child, self.name)
                if after_utc and post["created_utc"] <= after_utc:
                    return
                yield post
                seen += 1
                if max_posts and seen >= max_posts:
                    return
            after_token = listing.get("after")
            if not after_token or not children:
                return

    def fetch_comments(self, post_id: str) -> list[dict]:
        payload = self._get(f"/comments/{post_id}", {"limit": 500, "depth": 10, "sort": "top"})
        if not isinstance(payload, list) or len(payload) < 2:
            return []
        return walk_comment_tree(payload[1].get("data", {}).get("children", []))
