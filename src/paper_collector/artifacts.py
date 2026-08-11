# -*- coding: utf-8 -*-

"""PDF artifact metadata and local-file integrity helpers."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from paper_collector.storage import _connect

_HASH_CHUNK_SIZE = 1024 * 1024


class PdfAccessStatus(Enum):
    """Access state recorded for a candidate or local PDF artifact."""

    DISCOVERED = "discovered"
    OPEN_ACCESS = "open_access"
    LOCAL_FILE = "local_file"
    UNAVAILABLE = "unavailable"


@dataclass(frozen=True)
class PdfArtifact:
    """Immutable PDF artifact metadata loaded from SQLite."""

    id: int
    paper_id: int
    url: str
    access_status: PdfAccessStatus
    local_path: str | None
    sha256: str | None
    retrieved_at: str | None
    source: str


def calculate_sha256(file_path: Path) -> str:
    """Pure-value file operation: calculate SHA-256 for an approved local PDF file."""
    digest = hashlib.sha256()
    with file_path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(_HASH_CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def save_pdf_artifact(
    database_path: Path,
    *,
    paper_id: int,
    url: str,
    access_status: PdfAccessStatus,
    source: str,
    local_path: str | None = None,
    sha256: str | None = None,
    retrieved_at: str | None = None,
) -> None:
    """Persist or enrich PDF artifact metadata without downloading any content."""
    with _connect(database_path) as connection:
        connection.execute(
            """
            INSERT INTO pdf_artifacts (
                paper_id, url, access_status, local_path, sha256, retrieved_at, source
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(paper_id, url) DO UPDATE SET
                access_status = excluded.access_status,
                local_path = COALESCE(pdf_artifacts.local_path, excluded.local_path),
                sha256 = COALESCE(pdf_artifacts.sha256, excluded.sha256),
                retrieved_at = COALESCE(pdf_artifacts.retrieved_at, excluded.retrieved_at),
                source = excluded.source
            """,
            (
                paper_id,
                url,
                access_status.value,
                local_path,
                sha256,
                retrieved_at,
                source,
            ),
        )


def load_pdf_artifacts(database_path: Path, paper_id: int) -> list[PdfArtifact]:
    """Load PDF artifacts for one paper."""
    with _connect(database_path) as connection:
        rows = connection.execute(
            """
            SELECT id, paper_id, url, access_status, local_path, sha256, retrieved_at, source
            FROM pdf_artifacts
            WHERE paper_id = ?
            ORDER BY id
            """,
            (paper_id,),
        ).fetchall()
    return [
        PdfArtifact(
            id=int(row["id"]),
            paper_id=int(row["paper_id"]),
            url=str(row["url"]),
            access_status=PdfAccessStatus(str(row["access_status"])),
            local_path=None if row["local_path"] is None else str(row["local_path"]),
            sha256=None if row["sha256"] is None else str(row["sha256"]),
            retrieved_at=None if row["retrieved_at"] is None else str(row["retrieved_at"]),
            source=str(row["source"]),
        )
        for row in rows
    ]
