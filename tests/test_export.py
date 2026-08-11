# -*- coding: utf-8 -*-

import csv
from pathlib import Path

from paper_collector.domain import PaperCandidate
from paper_collector.export import export_papers_csv
from paper_collector.storage import initialize_database, save_paper


def test_export_papers_csv_is_derived_from_sqlite(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"
    output_path = tmp_path / "exports" / "papers.csv"
    initialize_database(database_path)
    candidate = PaperCandidate(
        title="DAB Converter",
        doi="10.1/dab",
        provider="openalex",
        source_record_id="W1",
        venue="IEEE TPEL",
        publication_year=2025,
    )
    save_paper(database_path, candidate.to_canonical(), candidate)

    exported_count = export_papers_csv(database_path, output_path)

    assert exported_count == 1
    with output_path.open("r", encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert rows[0]["title"] == "DAB Converter"
    assert rows[0]["doi"] == "10.1/dab"
    assert rows[0]["publication_year"] == "2025"
