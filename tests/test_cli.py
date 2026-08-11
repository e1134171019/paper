# -*- coding: utf-8 -*-

from pathlib import Path

from typer.testing import CliRunner

from paper_collector.cli import app

runner = CliRunner()


def test_cli_init_db_and_export_empty_csv(tmp_path: Path) -> None:
    database_path = tmp_path / "research.sqlite"
    output_path = tmp_path / "papers.csv"

    init_result = runner.invoke(app, ["init-db", "--database", str(database_path)])
    export_result = runner.invoke(
        app,
        [
            "export-csv",
            "--database",
            str(database_path),
            "--output",
            str(output_path),
        ],
    )

    assert init_result.exit_code == 0
    assert export_result.exit_code == 0
    assert database_path.exists()
    assert output_path.exists()
