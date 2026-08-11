# -*- coding: utf-8 -*-

"""Crossref discovery connector."""

from __future__ import annotations

from typing import Any

import httpx

from paper_collector.connectors import DiscoveryPage
from paper_collector.domain import PaperCandidate

_CROSSREF_WORKS_URL = "https://api.crossref.org/works"
_DEFAULT_TIMEOUT_SECONDS = 30.0


class CrossrefConnector:
    """Fetch academic candidates from Crossref cursor pagination."""

    provider = "crossref"

    def __init__(self, client: httpx.Client | None = None) -> None:
        self._owns_client = client is None
        self._client = client or httpx.Client(timeout=_DEFAULT_TIMEOUT_SECONDS)

    def close(self) -> None:
        """Close the internally-created HTTP client."""
        if self._owns_client:
            self._client.close()

    def fetch_page(self, query: str, cursor: str | None, page_size: int) -> DiscoveryPage:
        """Fetch and map one Crossref cursor page."""
        response = self._client.get(
            _CROSSREF_WORKS_URL,
            params={
                "query.bibliographic": query,
                "rows": page_size,
                "cursor": cursor or "*",
            },
        )
        response.raise_for_status()
        payload: dict[str, Any] = response.json()
        message = payload.get("message") or {}
        items = message.get("items") or []
        candidates = tuple(self._map_item(item) for item in items if self._title(item))
        next_cursor = message.get("next-cursor")
        return DiscoveryPage(
            candidates=candidates,
            next_cursor=None if next_cursor is None else str(next_cursor),
        )

    @staticmethod
    def _title(item: dict[str, Any]) -> str | None:
        """Extract the first usable Crossref title."""
        titles = item.get("title") or []
        if not titles:
            return None
        title = str(titles[0]).strip()
        return title or None

    @staticmethod
    def _publication_year(item: dict[str, Any]) -> int | None:
        """Extract a publication year from Crossref date parts."""
        for key in ("published", "published-print", "published-online", "issued"):
            date_block = item.get(key) or {}
            date_parts = date_block.get("date-parts") or []
            if date_parts and date_parts[0]:
                return int(date_parts[0][0])
        return None

    @staticmethod
    def _pdf_url(item: dict[str, Any]) -> str | None:
        """Return an explicitly advertised PDF link, if Crossref supplies one."""
        for link in item.get("link") or []:
            content_type = str(link.get("content-type") or "").lower()
            if content_type == "application/pdf" and link.get("URL"):
                return str(link["URL"])
        return None

    def _map_item(self, item: dict[str, Any]) -> PaperCandidate:
        """Map one Crossref work to a provider-neutral candidate."""
        title = self._title(item)
        if title is None:
            raise ValueError("Crossref item has no usable title")
        doi = None if item.get("DOI") is None else str(item["DOI"])
        source_url = None if item.get("URL") is None else str(item["URL"])
        source_record_id = doi or source_url or title
        container_titles = item.get("container-title") or []
        venue = None if not container_titles else str(container_titles[0])
        return PaperCandidate(
            title=title,
            provider=self.provider,
            source_record_id=source_record_id,
            doi=doi,
            source_url=source_url,
            abstract=None if item.get("abstract") is None else str(item["abstract"]),
            venue=venue,
            publication_year=self._publication_year(item),
            landing_url=source_url,
            pdf_url=self._pdf_url(item),
        )
