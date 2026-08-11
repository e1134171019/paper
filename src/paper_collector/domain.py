# -*- coding: utf-8 -*-

"""Immutable domain objects for the paper collector."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class SearchJobStatus(Enum):
    """Persistent lifecycle states for a search job."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRY_PENDING = "retry_pending"


@dataclass(frozen=True)
class CanonicalPaper:
    """Canonical paper identity and bibliographic fields."""

    title: str
    title_key: str
    doi: str | None = None
    abstract: str | None = None
    venue: str | None = None
    publication_year: int | None = None
    landing_url: str | None = None
    pdf_url: str | None = None


@dataclass(frozen=True)
class PaperCandidate:
    """Immutable paper candidate returned by a discovery connector."""

    title: str
    provider: str
    source_record_id: str
    doi: str | None = None
    source_url: str | None = None
    abstract: str | None = None
    venue: str | None = None
    publication_year: int | None = None
    landing_url: str | None = None
    pdf_url: str | None = None

    def to_canonical(self) -> CanonicalPaper:
        """Pure function wrapper: convert this candidate to canonical form."""
        from paper_collector.canonical import canonicalize_candidate

        return canonicalize_candidate(self)
