# -*- coding: utf-8 -*-

"""Provider-neutral discovery connector interfaces."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from paper_collector.domain import PaperCandidate


@dataclass(frozen=True)
class DiscoveryPage:
    """One immutable page of discovery candidates and its resume cursor."""

    candidates: tuple[PaperCandidate, ...]
    next_cursor: str | None


class DiscoveryConnector(Protocol):
    """Interface implemented by academic discovery providers."""

    provider: str

    def fetch_page(self, query: str, cursor: str | None, page_size: int) -> DiscoveryPage:
        """Fetch one discovery page without persisting it."""
        ...
