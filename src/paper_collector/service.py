# -*- coding: utf-8 -*-

"""Search orchestration across connectors, jobs, and SQLite persistence."""

from __future__ import annotations

from pathlib import Path

from paper_collector.artifacts import PdfAccessStatus, save_pdf_artifact
from paper_collector.connectors import DiscoveryConnector
from paper_collector.jobs import (
    SearchJob,
    create_search_job,
    load_search_job,
    mark_job_completed,
    mark_job_failure,
    mark_job_running,
    save_job_progress,
)
from paper_collector.storage import save_paper

_DEFAULT_PAGE_SIZE = 50


def _execute_search(
    database_path: Path,
    connector: DiscoveryConnector,
    job: SearchJob,
    *,
    max_results: int | None,
    page_size: int,
) -> SearchJob:
    """Run or resume one persistent search job until its current limit is reached."""
    if connector.provider != job.provider:
        raise ValueError(
            "Connector provider "
            f"{connector.provider!r} does not match job provider {job.provider!r}"
        )
    if page_size <= 0:
        raise ValueError("page_size must be positive")
    if max_results is not None and max_results <= 0:
        raise ValueError("max_results must be positive when provided")

    mark_job_running(database_path, job.id)
    current = load_search_job(database_path, job.id)
    cursor = current.cursor
    total_found = current.total_found
    total_stored = current.total_stored

    try:
        while max_results is None or total_found < max_results:
            remaining = (
                page_size
                if max_results is None
                else min(page_size, max_results - total_found)
            )
            page = connector.fetch_page(current.query, cursor, remaining)
            if not page.candidates:
                save_job_progress(
                    database_path,
                    current.id,
                    cursor=page.next_cursor,
                    total_found=total_found,
                    total_stored=total_stored,
                )
                break

            candidates = page.candidates[:remaining]
            for candidate in candidates:
                paper_id = save_paper(database_path, candidate.to_canonical(), candidate)
                if candidate.pdf_url is not None:
                    save_pdf_artifact(
                        database_path,
                        paper_id=paper_id,
                        url=candidate.pdf_url,
                        access_status=PdfAccessStatus.DISCOVERED,
                        source=candidate.provider,
                    )
            total_found += len(candidates)
            total_stored += len(candidates)
            cursor = page.next_cursor
            save_job_progress(
                database_path,
                current.id,
                cursor=cursor,
                total_found=total_found,
                total_stored=total_stored,
            )
            if cursor is None:
                break

        mark_job_completed(database_path, current.id)
    except Exception as error:
        mark_job_failure(database_path, current.id, str(error))
        raise

    return load_search_job(database_path, current.id)


def run_search(
    database_path: Path,
    connector: DiscoveryConnector,
    *,
    query: str,
    max_results: int | None = None,
    page_size: int = _DEFAULT_PAGE_SIZE,
) -> SearchJob:
    """Create a new persistent search job and execute it."""
    job = create_search_job(database_path, provider=connector.provider, query=query)
    return _execute_search(
        database_path,
        connector,
        job,
        max_results=max_results,
        page_size=page_size,
    )


def resume_search(
    database_path: Path,
    connector: DiscoveryConnector,
    job_id: str,
    *,
    max_results: int | None = None,
    page_size: int = _DEFAULT_PAGE_SIZE,
) -> SearchJob:
    """Resume an existing job from its persisted cursor and counters."""
    job = load_search_job(database_path, job_id)
    return _execute_search(
        database_path,
        connector,
        job,
        max_results=max_results,
        page_size=page_size,
    )
