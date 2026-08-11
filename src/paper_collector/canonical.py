# -*- coding: utf-8 -*-

"""Pure canonicalization and identity rules."""

from __future__ import annotations

import re
import unicodedata

from paper_collector.domain import CanonicalPaper, PaperCandidate

_DOI_PREFIX_PATTERN = re.compile(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", re.IGNORECASE)
_NON_WORD_PATTERN = re.compile(r"[^\w]+", re.UNICODE)
_WHITESPACE_PATTERN = re.compile(r"\s+")


def normalize_doi(raw_doi: str | None) -> str | None:
    """Pure function: normalize a DOI to a lowercase bare identifier."""
    if raw_doi is None:
        return None
    normalized = raw_doi.strip()
    normalized = _DOI_PREFIX_PATTERN.sub("", normalized).strip().lower()
    return normalized or None


def normalize_title(title: str) -> str:
    """Pure function: normalize a title for conservative identity matching."""
    normalized = unicodedata.normalize("NFKC", title).casefold()
    normalized = _NON_WORD_PATTERN.sub(" ", normalized)
    return _WHITESPACE_PATTERN.sub(" ", normalized).strip()


def canonicalize_candidate(candidate: PaperCandidate) -> CanonicalPaper:
    """Pure function: convert a discovery candidate to canonical paper fields."""
    title = candidate.title.strip()
    return CanonicalPaper(
        title=title,
        title_key=normalize_title(title),
        doi=normalize_doi(candidate.doi),
        abstract=candidate.abstract,
        venue=candidate.venue,
        publication_year=candidate.publication_year,
        landing_url=candidate.landing_url or candidate.source_url,
        pdf_url=candidate.pdf_url,
    )


def should_merge(left: CanonicalPaper, right: CanonicalPaper) -> bool:
    """Pure function: apply the v0.1 DOI-first deduplication contract."""
    if left.doi is not None and right.doi is not None:
        return left.doi == right.doi
    if left.doi is None and right.doi is None:
        return left.title_key == right.title_key
    return False
