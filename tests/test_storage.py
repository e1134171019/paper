# -*- coding: utf-8 -*-

import sqlite3
from pathlib import Path

from paper_collector.domain import PaperCandidate
from paper_collector.storage import initialize_database, load_papers, save_paper


def _candidate(*, title: str, doi: str | None, provider: str, record_id: str) -> PaperCandidate:
    return PaperCandidate(
        title=title,
        doi=doi,
        provider=provider,
        source_record_id=record_id,
        source_url=f"https://example.test/{record_id}",
    )


def test_initialize_database_is_idempotent(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"

    initialize_database(database_path)
    initialize_database(database_path)

    with sqlite3.connect(database_path) as connection:
        tables = {
            row[0]
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        }

    assert {"papers", "paper_sources", "search_jobs", "search_cursors", "pdf_artifacts"} <= tables


def test_same_doi_from_two_sources_creates_one_paper_two_sources(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"
    initialize_database(database_path)

    first = _candidate(title="DAB Paper", doi="10.1/ABC", provider="openalex", record_id="W1")
    second = _candidate(
        title="DAB Paper Extended",
        doi="https://doi.org/10.1/abc",
        provider="crossref",
        record_id="C1",
    )

    first_id = save_paper(database_path, first.to_canonical(), first)
    second_id = save_paper(database_path, second.to_canonical(), second)

    assert first_id == second_id
    assert len(load_papers(database_path)) == 1
    with sqlite3.connect(database_path) as connection:
        source_count = connection.execute(
            "SELECT COUNT(*) FROM paper_sources WHERE paper_id = ?", (first_id,)
        ).fetchone()[0]
    assert source_count == 2


def test_doi_less_same_title_deduplicates(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"
    initialize_database(database_path)

    first = _candidate(
        title="Dual-Active Bridge: A Study",
        doi=None,
        provider="openalex",
        record_id="W1",
    )
    second = _candidate(
        title="dual active bridge a study",
        doi=None,
        provider="crossref",
        record_id="C1",
    )

    first_id = save_paper(database_path, first.to_canonical(), first)
    second_id = save_paper(database_path, second.to_canonical(), second)

    assert first_id == second_id
    assert len(load_papers(database_path)) == 1


def test_doi_and_doi_less_same_title_remain_distinct(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"
    initialize_database(database_path)

    with_doi = _candidate(title="Same Paper", doi="10.1/x", provider="openalex", record_id="W1")
    without_doi = _candidate(title="Same Paper", doi=None, provider="crossref", record_id="C1")

    first_id = save_paper(database_path, with_doi.to_canonical(), with_doi)
    second_id = save_paper(database_path, without_doi.to_canonical(), without_doi)

    assert first_id != second_id
    assert len(load_papers(database_path)) == 2
