# -*- coding: utf-8 -*-

"""SQLite persistence for canonical papers and provenance."""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

from paper_collector.domain import CanonicalPaper, PaperCandidate

_SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    title_key TEXT NOT NULL,
    doi TEXT,
    abstract TEXT,
    venue TEXT,
    publication_year INTEGER,
    landing_url TEXT,
    pdf_url TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX IF NOT EXISTS ux_papers_doi
ON papers(doi)
WHERE doi IS NOT NULL;

CREATE UNIQUE INDEX IF NOT EXISTS ux_papers_title_without_doi
ON papers(title_key)
WHERE doi IS NULL;

CREATE TABLE IF NOT EXISTS paper_sources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_id INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    provider TEXT NOT NULL,
    source_record_id TEXT NOT NULL,
    source_url TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(paper_id, provider, source_record_id)
);

CREATE TABLE IF NOT EXISTS search_jobs (
    id TEXT PRIMARY KEY,
    provider TEXT NOT NULL,
    query TEXT NOT NULL,
    status TEXT NOT NULL,
    cursor TEXT,
    total_found INTEGER NOT NULL DEFAULT 0,
    total_stored INTEGER NOT NULL DEFAULT 0,
    retry_count INTEGER NOT NULL DEFAULT 0,
    max_retries INTEGER NOT NULL DEFAULT 3,
    error TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS search_cursors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT NOT NULL REFERENCES search_jobs(id) ON DELETE CASCADE,
    cursor TEXT,
    total_found INTEGER NOT NULL DEFAULT 0,
    total_stored INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pdf_artifacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_id INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    url TEXT NOT NULL,
    access_status TEXT NOT NULL,
    local_path TEXT,
    sha256 TEXT,
    retrieved_at TEXT,
    source TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(paper_id, url)
);
"""


@dataclass(frozen=True)
class StoredPaper:
    """Immutable human-readable paper row loaded from SQLite."""

    id: int
    title: str
    title_key: str
    doi: str | None
    abstract: str | None
    venue: str | None
    publication_year: int | None
    landing_url: str | None
    pdf_url: str | None


def _connect(database_path: Path) -> sqlite3.Connection:
    """Open a configured SQLite connection."""
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_database(database_path: Path) -> None:
    """Create the SQLite schema if it does not already exist."""
    database_path.parent.mkdir(parents=True, exist_ok=True)
    with _connect(database_path) as connection:
        connection.executescript(_SCHEMA)


def _find_existing_paper_id(
    connection: sqlite3.Connection,
    paper: CanonicalPaper,
) -> int | None:
    """Find an existing paper using the v0.1 identity contract."""
    if paper.doi is not None:
        row = connection.execute(
            "SELECT id FROM papers WHERE doi = ?",
            (paper.doi,),
        ).fetchone()
    else:
        row = connection.execute(
            "SELECT id FROM papers WHERE doi IS NULL AND title_key = ?",
            (paper.title_key,),
        ).fetchone()
    return None if row is None else int(row["id"])


def _insert_paper(connection: sqlite3.Connection, paper: CanonicalPaper) -> int:
    """Insert one canonical paper and return its database ID."""
    cursor = connection.execute(
        """
        INSERT INTO papers (
            title, title_key, doi, abstract, venue, publication_year, landing_url, pdf_url
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            paper.title,
            paper.title_key,
            paper.doi,
            paper.abstract,
            paper.venue,
            paper.publication_year,
            paper.landing_url,
            paper.pdf_url,
        ),
    )
    if cursor.lastrowid is None:
        raise RuntimeError("SQLite did not return a paper ID")
    return int(cursor.lastrowid)


def _enrich_missing_fields(
    connection: sqlite3.Connection,
    paper_id: int,
    paper: CanonicalPaper,
) -> None:
    """Fill missing canonical metadata without replacing existing non-empty values."""
    connection.execute(
        """
        UPDATE papers
        SET
            abstract = COALESCE(abstract, ?),
            venue = COALESCE(venue, ?),
            publication_year = COALESCE(publication_year, ?),
            landing_url = COALESCE(landing_url, ?),
            pdf_url = COALESCE(pdf_url, ?),
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (
            paper.abstract,
            paper.venue,
            paper.publication_year,
            paper.landing_url,
            paper.pdf_url,
            paper_id,
        ),
    )


def save_paper(
    database_path: Path,
    paper: CanonicalPaper,
    source: PaperCandidate,
) -> int:
    """Persist one canonical paper and additive source provenance transactionally."""
    with _connect(database_path) as connection:
        paper_id = _find_existing_paper_id(connection, paper)
        if paper_id is None:
            paper_id = _insert_paper(connection, paper)
        else:
            _enrich_missing_fields(connection, paper_id, paper)
        connection.execute(
            """
            INSERT OR IGNORE INTO paper_sources (
                paper_id, provider, source_record_id, source_url
            ) VALUES (?, ?, ?, ?)
            """,
            (
                paper_id,
                source.provider,
                source.source_record_id,
                source.source_url,
            ),
        )
        return paper_id


def load_papers(database_path: Path) -> list[StoredPaper]:
    """Load canonical papers ordered by insertion ID."""
    with _connect(database_path) as connection:
        rows = connection.execute(
            """
            SELECT id, title, title_key, doi, abstract, venue, publication_year,
                   landing_url, pdf_url
            FROM papers
            ORDER BY id
            """
        ).fetchall()
    return [
        StoredPaper(
            id=int(row["id"]),
            title=str(row["title"]),
            title_key=str(row["title_key"]),
            doi=None if row["doi"] is None else str(row["doi"]),
            abstract=None if row["abstract"] is None else str(row["abstract"]),
            venue=None if row["venue"] is None else str(row["venue"]),
            publication_year=(
                None if row["publication_year"] is None else int(row["publication_year"])
            ),
            landing_url=None if row["landing_url"] is None else str(row["landing_url"]),
            pdf_url=None if row["pdf_url"] is None else str(row["pdf_url"]),
        )
        for row in rows
    ]
