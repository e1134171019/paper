# -*- coding: utf-8 -*-

import hashlib
from pathlib import Path

from paper_collector.artifacts import (
    PdfAccessStatus,
    calculate_sha256,
    load_pdf_artifacts,
    save_pdf_artifact,
)
from paper_collector.domain import PaperCandidate
from paper_collector.storage import initialize_database, save_paper


def test_calculate_sha256_matches_file_bytes(tmp_path: Path) -> None:
    pdf_path = tmp_path / "paper.pdf"
    pdf_path.write_bytes(b"fake-pdf-bytes")

    assert calculate_sha256(pdf_path) == hashlib.sha256(b"fake-pdf-bytes").hexdigest()


def test_save_pdf_artifact_persists_open_access_url(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"
    initialize_database(database_path)
    candidate = PaperCandidate(
        title="Paper A",
        provider="openalex",
        source_record_id="W1",
        doi="10.1/a",
    )
    paper_id = save_paper(database_path, candidate.to_canonical(), candidate)

    save_pdf_artifact(
        database_path,
        paper_id=paper_id,
        url="https://example.test/paper.pdf",
        access_status=PdfAccessStatus.OPEN_ACCESS,
        source="openalex",
    )

    artifacts = load_pdf_artifacts(database_path, paper_id)
    assert len(artifacts) == 1
    assert artifacts[0].url == "https://example.test/paper.pdf"
    assert artifacts[0].access_status is PdfAccessStatus.OPEN_ACCESS
