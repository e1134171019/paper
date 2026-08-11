# -*- coding: utf-8 -*-

"""OpenAlex discovery connector."""

from __future__ import annotations

from typing import Any

import httpx

from paper_collector.connectors import DiscoveryPage
from paper_collector.domain import PaperCandidate

_OPENALEX_WORKS_URL = "https://api.openalex.org/works"
_DEFAULT_TIMEOUT_SECONDS = 30.0


class OpenAlexConnector:
    """Fetch academic candidates from the OpenAlex Works API."""

    provider = "openalex"

    def __init__(self, client: httpx.Client | None = None) -> None:
        self._owns_client = client is None
        self._client = client or httpx.Client(timeout=_DEFAULT_TIMEOUT_SECONDS)

    def close(self) -> None:
        """Close the internally-created HTTP client."""
        if self._owns_client:
            self._client.close()

    def fetch_page(self, query: str, cursor: str | None, page_size: int) -> DiscoveryPage:
        """Fetch and map one OpenAlex cursor page."""
        response = self._client.get(
            _OPENALEX_WORKS_URL,
            params={
                "search": query,
                "per-page": page_size,
                "cursor": cursor or "*",
            },
        )
        response.raise_for_status()
        payload: dict[str, Any] = response.json()
        results = payload.get("results") or []
        candidates = tuple(self._map_work(work) for work in results if work.get("title"))
        meta = payload.get("meta") or {}
        next_cursor = meta.get("next_cursor")
        return DiscoveryPage(
            candidates=candidates,
            next_cursor=None if next_cursor is None else str(next_cursor),
        )

    def _map_work(self, work: dict[str, Any]) -> PaperCandidate:
        """Map one OpenAlex work response to a provider-neutral candidate."""
        raw_id = str(work.get("id") or "")
        source_record_id = raw_id.rsplit("/", 1)[-1] or raw_id
        primary_location = work.get("primary_location") or {}
        source = primary_location.get("source") or {}
        return PaperCandidate(
            title=str(work["title"]),
            provider=self.provider,
            source_record_id=source_record_id,
            doi=None if work.get("doi") is None else str(work["doi"]),
            source_url=raw_id or None,
            abstract=None,
            venue=None if source.get("display_name") is None else str(source["display_name"]),
            publication_year=(
                None if work.get("publication_year") is None else int(work["publication_year"])
            ),
            landing_url=(
                None
                if primary_location.get("landing_page_url") is None
                else str(primary_location["landing_page_url"])
            ),
            pdf_url=(
                None
                if primary_location.get("pdf_url") is None
                else str(primary_location["pdf_url"])
            ),
        )
