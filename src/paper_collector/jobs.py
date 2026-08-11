# -*- coding: utf-8 -*-

"""Persistent search-job lifecycle management."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4

from paper_collector.domain import SearchJobStatus
from paper_collector.storage import _connect


@dataclass(frozen=True)
class SearchJob:
    """Immutable persisted search-job snapshot."""

    id: str
    provider: str
    query: str
    status: SearchJobStatus
    cursor: str | None
    total_found: int
    total_stored: int
    retry_count: int
    max_retries: int
    error: str | None


def create_search_job(
    database_path: Path,
    *,
    provider: str,
    query: str,
    max_retries: int = 3,
) -> SearchJob:
    """Create and persist a pending search job."""
    job_id = str(uuid4())
    with _connect(database_path) as connection:
        connection.execute(
            """
            INSERT INTO search_jobs (
                id, provider, query, status, max_retries
            ) VALUES (?, ?, ?, ?, ?)
            """,
            (job_id, provider, query, SearchJobStatus.PENDING.value, max_retries),
        )
    return load_search_job(database_path, job_id)


def load_search_job(database_path: Path, job_id: str) -> SearchJob:
    """Load one persistent search job by ID."""
    with _connect(database_path) as connection:
        row = connection.execute(
            """
            SELECT id, provider, query, status, cursor, total_found, total_stored,
                   retry_count, max_retries, error
            FROM search_jobs
            WHERE id = ?
            """,
            (job_id,),
        ).fetchone()
    if row is None:
        raise KeyError(f"Unknown search job: {job_id}")
    return SearchJob(
        id=str(row["id"]),
        provider=str(row["provider"]),
        query=str(row["query"]),
        status=SearchJobStatus(str(row["status"])),
        cursor=None if row["cursor"] is None else str(row["cursor"]),
        total_found=int(row["total_found"]),
        total_stored=int(row["total_stored"]),
        retry_count=int(row["retry_count"]),
        max_retries=int(row["max_retries"]),
        error=None if row["error"] is None else str(row["error"]),
    )


def list_search_jobs(database_path: Path) -> list[SearchJob]:
    """Load all search jobs in creation order."""
    with _connect(database_path) as connection:
        rows = connection.execute("SELECT id FROM search_jobs ORDER BY created_at, id").fetchall()
    return [load_search_job(database_path, str(row["id"])) for row in rows]


def mark_job_running(database_path: Path, job_id: str) -> None:
    """Mark a job as actively running and clear its previous error."""
    with _connect(database_path) as connection:
        connection.execute(
            """
            UPDATE search_jobs
            SET status = ?, error = NULL, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (SearchJobStatus.RUNNING.value, job_id),
        )


def save_job_progress(
    database_path: Path,
    job_id: str,
    *,
    cursor: str | None,
    total_found: int,
    total_stored: int,
) -> None:
    """Persist resumable cursor and cumulative counters atomically."""
    with _connect(database_path) as connection:
        connection.execute(
            """
            UPDATE search_jobs
            SET cursor = ?, total_found = ?, total_stored = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (cursor, total_found, total_stored, job_id),
        )
        connection.execute(
            """
            INSERT INTO search_cursors (job_id, cursor, total_found, total_stored)
            VALUES (?, ?, ?, ?)
            """,
            (job_id, cursor, total_found, total_stored),
        )


def mark_job_completed(database_path: Path, job_id: str) -> None:
    """Mark a search job completed."""
    with _connect(database_path) as connection:
        connection.execute(
            """
            UPDATE search_jobs
            SET status = ?, error = NULL, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (SearchJobStatus.COMPLETED.value, job_id),
        )


def mark_job_failure(database_path: Path, job_id: str, error: str) -> None:
    """Persist a failure and transition to retry-pending or terminal failed."""
    current = load_search_job(database_path, job_id)
    retry_count = current.retry_count + 1
    next_status = (
        SearchJobStatus.RETRY_PENDING
        if retry_count < current.max_retries
        else SearchJobStatus.FAILED
    )
    with _connect(database_path) as connection:
        connection.execute(
            """
            UPDATE search_jobs
            SET status = ?, retry_count = ?, error = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (next_status.value, retry_count, error, job_id),
        )
