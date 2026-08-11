# -*- coding: utf-8 -*-

from pathlib import Path

from paper_collector.domain import SearchJobStatus
from paper_collector.jobs import (
    create_search_job,
    load_search_job,
    mark_job_failure,
    mark_job_running,
    save_job_progress,
)
from paper_collector.storage import initialize_database


def test_job_progress_persists_cursor_and_counts(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"
    initialize_database(database_path)
    job = create_search_job(database_path, provider="openalex", query="DAB")

    mark_job_running(database_path, job.id)
    save_job_progress(
        database_path,
        job.id,
        cursor="cursor-2",
        total_found=50,
        total_stored=42,
    )

    loaded = load_search_job(database_path, job.id)
    assert loaded.status is SearchJobStatus.RUNNING
    assert loaded.cursor == "cursor-2"
    assert loaded.total_found == 50
    assert loaded.total_stored == 42


def test_resume_reads_persisted_cursor(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"
    initialize_database(database_path)
    job = create_search_job(database_path, provider="crossref", query="CLLC")
    save_job_progress(
        database_path,
        job.id,
        cursor="next-page",
        total_found=20,
        total_stored=18,
    )

    loaded = load_search_job(database_path, job.id)

    assert loaded.cursor == "next-page"


def test_failure_increments_retry_count_and_preserves_error(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"
    initialize_database(database_path)
    job = create_search_job(
        database_path,
        provider="openalex",
        query="soft switching",
        max_retries=2,
    )

    mark_job_failure(database_path, job.id, "timeout")
    first_failure = load_search_job(database_path, job.id)
    assert first_failure.retry_count == 1
    assert first_failure.status is SearchJobStatus.RETRY_PENDING
    assert first_failure.error == "timeout"

    mark_job_failure(database_path, job.id, "timeout again")
    final_failure = load_search_job(database_path, job.id)
    assert final_failure.retry_count == 2
    assert final_failure.status is SearchJobStatus.FAILED
    assert final_failure.error == "timeout again"
