# -*- coding: utf-8 -*-

from paper_collector.canonical import normalize_doi, normalize_title, should_merge
from paper_collector.domain import CanonicalPaper, PaperCandidate


def test_normalize_doi_removes_url_prefix() -> None:
    assert normalize_doi("https://doi.org/10.1109/TPEL.2025.123") == "10.1109/tpel.2025.123"


def test_normalize_doi_returns_none_for_blank() -> None:
    assert normalize_doi("  ") is None


def test_title_normalization_is_case_and_punctuation_insensitive() -> None:
    assert normalize_title("Dual-Active Bridge: A Study") == normalize_title(
        "dual active bridge a study"
    )


def test_should_merge_by_same_doi() -> None:
    left = CanonicalPaper(title="A", title_key="a", doi="10.1/x")
    right = CanonicalPaper(title="B", title_key="b", doi="10.1/x")
    assert should_merge(left, right) is True


def test_should_merge_doi_less_records_by_normalized_title() -> None:
    left = CanonicalPaper(title="Same!", title_key="same", doi=None)
    right = CanonicalPaper(title="same", title_key="same", doi=None)
    assert should_merge(left, right) is True


def test_doi_record_does_not_merge_with_doi_less_record_by_title() -> None:
    left = CanonicalPaper(title="Same", title_key="same", doi="10.1/x")
    right = CanonicalPaper(title="Same", title_key="same", doi=None)
    assert should_merge(left, right) is False


def test_canonicalize_candidate_preserves_source_metadata() -> None:
    candidate = PaperCandidate(
        title="  Dual-Active Bridge: A Study  ",
        doi="DOI: 10.1/ABC",
        provider="openalex",
        source_record_id="W123",
        source_url="https://openalex.org/W123",
        publication_year=2025,
    )

    paper = candidate.to_canonical()

    assert paper.title == "Dual-Active Bridge: A Study"
    assert paper.title_key == "dual active bridge a study"
    assert paper.doi == "10.1/abc"
