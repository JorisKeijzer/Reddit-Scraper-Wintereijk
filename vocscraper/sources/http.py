"""Polite HTTP client: fixed delay between requests, retries on 429/5xx."""

from __future__ import annotations

import logging
import time

import requests

log = logging.getLogger(__name__)

USER_AGENT = "python:wintereijk-voc-research:v0.1 (market research, read-only)"


class HttpClient:
    def __init__(self, min_interval: float = 1.0, max_retries: int = 4):
        self.session = requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT
        self.min_interval = min_interval
        self.max_retries = max_retries
        self._last = 0.0

    def get_json(self, url: str, params: dict | None = None, headers: dict | None = None) -> dict | list | None:
        """GET a JSON document. Returns None on 403/404 (private, banned or missing)."""
        for attempt in range(self.max_retries + 1):
            wait = self.min_interval - (time.monotonic() - self._last)
            if wait > 0:
                time.sleep(wait)
            self._last = time.monotonic()
            try:
                resp = self.session.get(url, params=params, headers=headers, timeout=60)
            except requests.RequestException as exc:
                log.warning("netwerkfout %s (%s), poging %d", url, exc, attempt + 1)
                time.sleep(2 ** (attempt + 1))
                continue
            if resp.status_code in (403, 404):
                log.warning("%s gaf %d, overgeslagen", resp.url, resp.status_code)
                return None
            if resp.status_code == 429 or resp.status_code >= 500:
                delay = float(resp.headers.get("Retry-After") or 2 ** (attempt + 2))
                log.warning("%s gaf %d, wacht %.0fs", resp.url, resp.status_code, delay)
                time.sleep(delay)
                continue
            if resp.status_code == 422:
                # Arctic Shift meldt overbelasting soms als 422 met {"error": ...}; de aanroeper probeert opnieuw.
                try:
                    return resp.json()
                except ValueError:
                    pass
            resp.raise_for_status()
            return resp.json()
        raise RuntimeError(f"Opgegeven na {self.max_retries + 1} pogingen: {url}")
