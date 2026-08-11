# -*- coding: utf-8 -*-

"""Command-line interface for Collector Core v0.1."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from paper_collector.crossref import CrossrefConnector
from paper_collector.export import export_papers_csv
from paper_collector.jobs import list_search_jobs, load_search_job
from paper_collector.openalex import OpenAlexConnector
from paper_collector.service import resume_search, run_search
from paper_collector.storage import initialize_database

_DEFAULT_DATABASE = Path("data/research.sqlite")
_DEFAULT_EXPORT = Path("exports/papers.csv")
_DEFAULT_MAX_RESULTS = 100
_DEFAULT_PAGE_SIZE = 50

app = typer.Typer(no_args_is_help=True, help="Evidence-oriented academic paper collector.")

Connector = OpenAlexConnector | CrossrefConnector


def _create_connector(provider: str) -> Connector:
    """Create a registered discovery connector from a CLI provider name."""
    normalized = provider.strip().lower()
    if normalized == "openalex":
        return OpenAlexConnector()
    if normalized == "crossref":
        return CrossrefConnector()
    raise typer.BadParameter("provider must be one of: openalex, crossref")


@app.command("init-db")
def init_db_command(
    database: Annotated[
        Path, typer.Option("--database", help="SQLite database path.")
    ] = _DEFAULT_DATABASE,
) -> None:
    """Initialize the SQLite source of truth."""
    initialize_database(database)
    typer.echo(f"initialized: {database}")


@app.command("search")
def search_command(
    provider: Annotated[str, typer.Option("--provider", help="openalex or crossref")],
    query: Annotated[str, typer.Option("--query", help="Academic search query")],
    database: Annotated[Path, typer.Option("--database")] = _DEFAULT_DATABASE,
    max_results: Annotated[int, typer.Option("--max-results", min=1)] = _DEFAULT_MAX_RESULTS,
    page_size: Annotated[int, typer.Option("--page-size", min=1)] = _DEFAULT_PAGE_SIZE,
) -> None:
    """Start and persist a new academic search job."""
    initialize_database(database)
    connector = _create_connector(provider)
    try:
        job = run_search(
            database,
            connector,
            query=query,
            max_results=max_results,
            page_size=page_size,
        )
    finally:
        connector.close()
    typer.echo(
        f"job={job.id} status={job.status.value} found={job.total_found} stored={job.total_stored}"
    )


@app.command("jobs")
def jobs_command(
    database: Annotated[Path, typer.Option("--database")] = _DEFAULT_DATABASE,
) -> None:
    """List persisted search jobs."""
    initialize_database(database)
    for job in list_search_jobs(database):
        typer.echo(
            f"{job.id} {job.provider} {job.status.value} found={job.total_found} "
            f"stored={job.total_stored} cursor={job.cursor or '-'}"
        )


@app.command("resume")
def resume_command(
    job_id: Annotated[str, typer.Argument(help="Persistent search job ID")],
    database: Annotated[Path, typer.Option("--database")] = _DEFAULT_DATABASE,
    max_results: Annotated[int | None, typer.Option("--max-results", min=1)] = None,
    page_size: Annotated[int, typer.Option("--page-size", min=1)] = _DEFAULT_PAGE_SIZE,
) -> None:
    """Resume a search from its persisted provider cursor."""
    initialize_database(database)
    existing = load_search_job(database, job_id)
    connector = _create_connector(existing.provider)
    try:
        job = resume_search(
            database,
            connector,
            job_id,
            max_results=max_results,
            page_size=page_size,
        )
    finally:
        connector.close()
    typer.echo(
        f"job={job.id} status={job.status.value} found={job.total_found} stored={job.total_stored}"
    )


@app.command("export-csv")
def export_csv_command(
    database: Annotated[Path, typer.Option("--database")] = _DEFAULT_DATABASE,
    output: Annotated[Path, typer.Option("--output")] = _DEFAULT_EXPORT,
) -> None:
    """Regenerate a human-readable paper CSV from SQLite."""
    initialize_database(database)
    count = export_papers_csv(database, output)
    typer.echo(f"exported={count} output={output}")


if __name__ == "__main__":
    app()
