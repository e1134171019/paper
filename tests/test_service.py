# -*- coding: utf-8 -*-

import sqlite3
from dataclasses import dataclass, field
from pathlib import Path

from paper_collector.connectors import DiscoveryPage
from paper_collector.domain import PaperCandidate, SearchJobStatus
from paper_collector.jobs import create_search_job, load_search_job, save_job_progress
from paper_collector.service import resume_search, run_search
from paper_collector.storage import initialize_database, load_papers


@dataclass
class FakeConnector:
    provider: str = "fake"
    seen_cursors: list[str | None] = field(default_factory=list)

    def fetch_page(self, query: str, cursor: str | None, page_size: int) -> DiscoveryPage:
        self.seen_cursors.append(cursor)
        if cursor is None:
            return DiscoveryPage(
                candidates=(
                    PaperCandidate(
                        title="Paper A",
                        doi="10.1/a",
                        provider=self.provider,
                        source_record_id="A",
                        pdf_url="https://example.test/A.pdf",
                    ),
                    PaperCandidate(
                        title="Paper B",
                        doi="10.1/b",
                        provider=self.provider,
                        source_record_id="B",
                    ),
                ),
                next_cursor="page-2",
            )
        if cursor == "page-2":
            return DiscoveryPage(
                candidates=(
                    PaperCandidate(
                        title="Paper B duplicate",
                        doi="10.1/b",
                        provider=self.provider,
                        source_record_id="B2",
                    ),
                    PaperCandidate(
                        title="Paper C",
                        doi="10.1/c",
                        provider=self.provider,
                        source_record_id="C",
                    ),
                ),
                next_cursor=None,
            )
        raise AssertionError(f"unexpected cursor: {cursor}")


def test_run_search_persists_two_pages_and_completes(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"
    initialize_database(database_path)
    connector = FakeConnector()

    job = run_search(
        database_path,
        connector,
        query="DAB",
        max_results=10,
        page_size=2,
    )

    assert connector.seen_cursors == [None, "page-2"]
    assert job.status is SearchJobStatus.COMPLETED
    assert len(load_papers(database_path)) == 3
    assert job.total_found == 4
    assert job.total_stored == 4
    with sqlite3.connect(database_path) as connection:
        artifact_count = connection.execute("SELECT COUNT(*) FROM pdf_artifacts").fetchone()[0]
    assert artifact_count == 1


def test_resume_search_begins_from_persisted_cursor(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"
    initialize_database(database_path)
    connector = FakeConnector()
    job = create_search_job(database_path, provider=connector.provider, query="CLLC")
    save_job_progress(
        database_path,
        job.id,
        cursor="page-2",
        total_found=2,
        total_stored=2,
    )

    resumed = resume_search(
        database_path,
        connector,
        job.id,
        max_results=10,
        page_size=2,
    )

    assert connector.seen_cursors == ["page-2"]
    assert resumed.status is SearchJobStatus.COMPLETED
    assert resumed.total_found == 4
    assert load_search_job(database_path, job.id).cursor is None
