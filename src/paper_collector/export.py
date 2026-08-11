# -*- coding: utf-8 -*-

"""Derived human-readable exports from the SQLite source of truth."""

from __future__ import annotations

import csv
from pathlib import Path

from paper_collector.storage import load_papers

_CSV_FIELDS = (
    "id",
    "title",
    "doi",
    "venue",
    "publication_year",
    "landing_url",
    "pdf_url",
)


def export_papers_csv(database_path: Path, output_path: Path) -> int:
    """Export canonical papers to a regenerable UTF-8 CSV snapshot."""
    papers = load_papers(database_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=_CSV_FIELDS)
        writer.writeheader()
        for paper in papers:
            writer.writerow(
                {
                    "id": paper.id,
                    "title": paper.title,
                    "doi": paper.doi or "",
                    "venue": paper.venue or "",
                    "publication_year": paper.publication_year or "",
                    "landing_url": paper.landing_url or "",
                    "pdf_url": paper.pdf_url or "",
                }
            )
    return len(papers)
