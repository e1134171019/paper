# Collector Core v0.1 Design

## Goal
Build the first executable core of the paper evidence collection system for power-conversion research. The core must discover papers from multiple academic sources, canonicalize and deduplicate records, persist them in a single SQLite source of truth, resolve lawful PDF locations, preserve resumable job state, and export human-readable CSV snapshots.

## Scope
Collector Core v0.1 includes:

1. Academic discovery through a provider-neutral connector interface.
2. Initial connectors for OpenAlex and Crossref that do not require paid credentials.
3. Canonical paper records with DOI-first, normalized-title fallback deduplication.
4. SQLite persistence for papers, source provenance, search jobs, search cursors, and PDF artifacts.
5. Persistent job states so interrupted searches can resume from stored cursor/state.
6. Lawful PDF resolution metadata only; the core records URLs and access status but does not bypass paywalls or publisher restrictions.
7. SHA-256 support for local PDFs when a file is later downloaded by an approved workflow.
8. CSV exports generated from SQLite; CSV is never the source of truth.
9. CLI commands for database initialization, search, job inspection, and CSV export.
10. Automated tests for pure canonicalization/deduplication and SQLite persistence/job-resume behavior.

Out of scope for v0.1:

- SvelteKit Research Explorer UI.
- GROBID/Docling full-text parsing.
- LLM screening or evidence extraction.
- Vector database / PaperQA2 RAG.
- Automatic downloading of subscription-only PDFs.
- Deployment or hosted services.

## Architecture

```text
Academic sources
  ├─ OpenAlex
  └─ Crossref
        │
        ▼
Discovery Connector Protocol
        │
        ▼
Canonicalizer
  DOI normalization
  title normalization
  source provenance merge
        │
        ▼
SQLite SSOT
  papers
  paper_sources
  search_jobs
  search_cursors
  pdf_artifacts
        │
        ├─ CSV exporter
        └─ future parser / dashboard / RAG
```

The source interfaces are separated from canonicalization and storage. Replacing or adding a connector must not require changes to database consumers. Business rules are pure functions. HTTP, database, filesystem, and export functions are explicit side-effect boundaries.

## Domain model

### PaperCandidate
Immutable discovery result returned by connectors. It contains title, DOI, publication date/year, venue, URL, PDF URL if explicitly provided, source name, source record ID, and optional abstract.

### CanonicalPaper
Immutable canonical representation used for persistence. DOI is normalized to lowercase without `https://doi.org/` or `doi:` prefixes. If DOI is unavailable, a normalized title key is used for deduplication.

### SearchJob
Persistent job record with:

- id
- provider
- query
- status
- cursor
- total_found
- total_stored
- retry_count
- error
- created_at
- updated_at

Statuses use an enum, not free-form strings:

`PENDING`, `RUNNING`, `COMPLETED`, `FAILED`, `RETRY_PENDING`.

### PDFArtifact
Stores metadata about a lawful full-text candidate or local file:

- paper_id
- url
- access_status
- local_path nullable
- sha256 nullable
- retrieved_at nullable
- source

No PDF bytes are stored in SQLite.

## Deduplication contract

Deduplication priority:

1. Same normalized DOI => same paper.
2. If both records lack DOI, same normalized title => same paper.
3. If one record has DOI and the other does not, do not automatically merge solely on title in v0.1; keep both until later metadata enrichment resolves identity.

When duplicates are merged, source provenance is additive and richer non-empty metadata may fill missing canonical fields. Existing non-empty canonical values are not silently overwritten by a weaker source.

## Storage contract

SQLite is the only source of truth. CSV files are derived exports and may be deleted/recreated at any time.

Minimum tables:

- `papers`
- `paper_sources`
- `search_jobs`
- `search_cursors`
- `pdf_artifacts`

Database initialization must be idempotent.

## Search and resume flow

1. Create a persistent `PENDING` job.
2. Mark `RUNNING` before network work.
3. Connector fetches one page/batch and returns candidates plus next cursor.
4. Canonicalize candidates.
5. Upsert papers and provenance in one transaction.
6. Persist the next cursor and counters.
7. Continue until no next cursor or configured result limit is reached.
8. Mark `COMPLETED`.
9. On failure, store the exception summary, increment retry count, and set `RETRY_PENDING` or `FAILED` according to configured maximum retries.
10. Resume reads the latest stored cursor rather than restarting from the beginning.

## PDF policy

Collector Core v0.1 may store:

- publisher-provided open-access PDF URL,
- repository PDF URL,
- Unpaywall/OpenAlex open-access location supplied by a later connector,
- local file metadata for a PDF obtained through an approved/legal route.

The core must not implement paywall bypass, credential scraping, CAPTCHA bypass, or publisher access circumvention.

## CLI

Initial command surface:

```text
paper-collector init-db
paper-collector search --provider openalex --query "dual active bridge" --max-results 100
paper-collector jobs
paper-collector resume <job-id>
paper-collector export-csv --output exports/papers.csv
```

## Technology

- Python 3.11+
- stdlib `sqlite3` for v0.1 persistence to keep dependencies minimal
- `httpx` for HTTP
- `pydantic` for boundary validation/configuration
- `typer` for CLI
- `pytest` for tests
- `ruff` for lint/format
- `mypy --strict` for type validation

The external `findpapers` project remains a reference and potential later adapter, but v0.1 implements two small first-party connectors so the storage contract is under our control and tests do not depend on a third-party release branch.

## Error handling

- Network errors never corrupt stored papers; page persistence is transactional.
- Search jobs always retain failure state and error text.
- Unsupported provider names fail before a job starts.
- Invalid DOI strings normalize conservatively; empty/obviously unusable values become `None`.
- CSV export creates parent directories and writes UTF-8 with header.

## Testing contract

TDD is required for production behavior.

Minimum automated coverage:

1. DOI normalization.
2. Title normalization.
3. DOI-first deduplication.
4. Title fallback only when both DOI values are absent.
5. Database initialization idempotency.
6. Paper upsert preserves provenance.
7. Search job state transition and stored cursor.
8. Resume starts from persisted cursor.
9. CSV is generated from SQLite records.

HTTP connector tests use injected transports/fakes; core pure functions are tested without mocks.

## Acceptance criteria

Collector Core v0.1 is acceptable when:

- a fresh database can be initialized;
- at least one connector search can persist canonical papers;
- the same DOI from two providers produces one paper with two provenance rows;
- an interrupted job can be resumed from its persisted cursor;
- derived CSV can be regenerated from SQLite;
- tests, lint, and strict type checks pass in the verified runtime;
- no deployment, paywall bypass, or unapproved external mutation is performed.
