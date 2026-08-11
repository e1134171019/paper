# Collector Core v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a tested Python 3.11+ collector core that searches OpenAlex/Crossref through a provider interface, deduplicates canonical papers, persists SQLite job/provenance state, resumes interrupted searches, and exports CSV snapshots.

**Architecture:** Pure canonicalization/deduplication is isolated from HTTP and SQLite side effects. Connectors return immutable candidates; a service orchestrates page fetching and transactional persistence. SQLite remains the SSOT, while CSV is derived output.

**Tech Stack:** Python 3.11+, sqlite3, httpx, pydantic, typer, pytest, ruff, mypy.

## Global Constraints

- Use UTF-8 and `# -*- coding: utf-8 -*-` at the top of Python files.
- All function parameters and return values have type annotations.
- Status values use Enum.
- Domain data uses `@dataclass(frozen=True)`.
- Pure business logic has no IO and is testable without mocks.
- Side-effect functions use verb-oriented names such as `fetch_`, `save_`, `load_`.
- SQLite is the only source of truth; CSV is derived.
- Do not bypass paywalls, CAPTCHAs, publisher access controls, or credentials.
- Do not deploy or publish a hosted service in v0.1.

---

### Task 1: Project baseline and canonical domain model

**Files:**
- Create: `pyproject.toml`
- Create: `.gitignore`
- Create: `README.md`
- Create: `src/paper_collector/__init__.py`
- Create: `src/paper_collector/domain.py`
- Create: `src/paper_collector/canonical.py`
- Create: `tests/test_canonical.py`

**Interfaces:**
- Produces: `PaperCandidate`, `CanonicalPaper`, `SearchJobStatus`, `normalize_doi()`, `normalize_title()`, `canonicalize_candidate()`, `should_merge()`.

- [ ] **Step 1: Write failing canonicalization tests**

```python
from paper_collector.canonical import normalize_doi, normalize_title, should_merge
from paper_collector.domain import CanonicalPaper


def test_normalize_doi_removes_url_prefix() -> None:
    assert normalize_doi("https://doi.org/10.1109/TPEL.2025.123") == "10.1109/tpel.2025.123"


def test_title_normalization_is_case_and_punctuation_insensitive() -> None:
    assert normalize_title("Dual-Active Bridge: A Study") == normalize_title("dual active bridge a study")


def test_should_merge_by_same_doi() -> None:
    left = CanonicalPaper(title="A", title_key="a", doi="10.1/x")
    right = CanonicalPaper(title="B", title_key="b", doi="10.1/x")
    assert should_merge(left, right) is True


def test_doi_record_does_not_merge_with_doi_less_record_by_title() -> None:
    left = CanonicalPaper(title="Same", title_key="same", doi="10.1/x")
    right = CanonicalPaper(title="Same", title_key="same", doi=None)
    assert should_merge(left, right) is False
```

- [ ] **Step 2: Run tests and verify RED**

Run: `pytest tests/test_canonical.py -v`
Expected: import/module failures because production modules do not exist.

- [ ] **Step 3: Implement immutable domain objects and minimal pure functions**

Implement:

```python
class SearchJobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRY_PENDING = "retry_pending"
```

and frozen dataclasses for candidates/canonical papers. `normalize_doi()` strips DOI URL/prefixes, trims whitespace, lowercases, and returns `None` for blank input. `normalize_title()` Unicode-normalizes, casefolds, replaces punctuation with spaces, collapses whitespace. `should_merge()` follows the design contract exactly.

- [ ] **Step 4: Run canonical tests and verify GREEN**

Run: `pytest tests/test_canonical.py -v`
Expected: all canonical tests pass.

- [ ] **Step 5: Run lint/type checks for Task 1**

Run: `ruff check src tests && mypy --strict src`
Expected: zero errors.

---

### Task 2: SQLite schema and paper/provenance persistence

**Files:**
- Create: `src/paper_collector/storage.py`
- Create: `tests/test_storage.py`

**Interfaces:**
- Consumes: `CanonicalPaper`, `PaperCandidate`.
- Produces: `initialize_database(path: Path)`, `save_paper(...) -> int`, `load_papers(...) -> list[StoredPaper]`, `StoredPaper`.

- [ ] **Step 1: Write failing storage tests**

Tests must prove:

```python
def test_initialize_database_is_idempotent(tmp_path: Path) -> None: ...
def test_same_doi_from_two_sources_creates_one_paper_two_sources(tmp_path: Path) -> None: ...
def test_doi_less_same_title_deduplicates(tmp_path: Path) -> None: ...
def test_doi_and_doi_less_same_title_remain_distinct(tmp_path: Path) -> None: ...
```

- [ ] **Step 2: Run storage tests and verify RED**

Run: `pytest tests/test_storage.py -v`
Expected: missing storage API failures.

- [ ] **Step 3: Implement minimal schema and transactional persistence**

Create tables:

```text
papers(id, title, title_key, doi, abstract, venue, publication_year, landing_url, pdf_url, created_at, updated_at)
paper_sources(id, paper_id, provider, source_record_id, source_url, created_at, UNIQUE(paper_id, provider, source_record_id))
search_jobs(...)
search_cursors(...)
pdf_artifacts(...)
```

Use a partial uniqueness strategy in application logic: query DOI first; only use `title_key` when incoming DOI is `None` and the stored candidate also has `doi IS NULL`.

- [ ] **Step 4: Run storage tests and verify GREEN**

Run: `pytest tests/test_storage.py -v`
Expected: all storage tests pass.

- [ ] **Step 5: Run all current checks**

Run: `pytest tests -v && ruff check src tests && mypy --strict src`
Expected: zero failures/errors.

---

### Task 3: Persistent search jobs and resume cursor

**Files:**
- Modify: `src/paper_collector/domain.py`
- Modify: `src/paper_collector/storage.py`
- Create: `src/paper_collector/jobs.py`
- Create: `tests/test_jobs.py`

**Interfaces:**
- Produces: `create_search_job()`, `mark_job_running()`, `save_job_progress()`, `mark_job_completed()`, `mark_job_failure()`, `load_search_job()`, `SearchJob`.

- [ ] **Step 1: Write failing job-state tests**

```python
def test_job_progress_persists_cursor_and_counts(tmp_path: Path) -> None: ...
def test_resume_reads_persisted_cursor(tmp_path: Path) -> None: ...
def test_failure_increments_retry_count_and_preserves_error(tmp_path: Path) -> None: ...
```

- [ ] **Step 2: Run job tests and verify RED**

Run: `pytest tests/test_jobs.py -v`
Expected: missing job APIs.

- [ ] **Step 3: Implement persistent job lifecycle**

`SearchJob` is frozen. Cursor storage is provider/query/job scoped. `mark_job_failure()` uses `RETRY_PENDING` while `retry_count < max_retries`, otherwise `FAILED`.

- [ ] **Step 4: Run job tests and verify GREEN**

Run: `pytest tests/test_jobs.py -v`
Expected: all job tests pass.

- [ ] **Step 5: Run regression checks**

Run: `pytest tests -v && ruff check src tests && mypy --strict src`
Expected: zero failures/errors.

---

### Task 4: Provider protocol, OpenAlex/Crossref connectors, search orchestration

**Files:**
- Create: `src/paper_collector/connectors.py`
- Create: `src/paper_collector/openalex.py`
- Create: `src/paper_collector/crossref.py`
- Create: `src/paper_collector/service.py`
- Create: `tests/test_service.py`
- Create: `tests/test_connectors.py`

**Interfaces:**
- `DiscoveryConnector` Protocol:

```python
class DiscoveryConnector(Protocol):
    provider: str
    def fetch_page(self, query: str, cursor: str | None, page_size: int) -> DiscoveryPage: ...
```

- `DiscoveryPage(candidates: tuple[PaperCandidate, ...], next_cursor: str | None)`.
- `run_search(...) -> SearchJob` and `resume_search(...) -> SearchJob`.

- [ ] **Step 1: Write failing orchestration tests with a deterministic fake connector**

Tests prove that two pages persist papers, progress cursor is saved after each page, and resume begins from the stored cursor rather than `None`.

- [ ] **Step 2: Run service tests and verify RED**

Run: `pytest tests/test_service.py -v`
Expected: missing connector/service APIs.

- [ ] **Step 3: Implement provider-neutral orchestration**

The service owns job state transitions and persistence. Connector implementations only transform remote responses to `PaperCandidate` values.

- [ ] **Step 4: Write connector parsing tests using `httpx.MockTransport`**

Cover one representative OpenAlex response and one Crossref response without live network access.

- [ ] **Step 5: Implement minimal OpenAlex and Crossref HTTP connectors**

Use injected `httpx.Client`. Apply explicit timeouts and `raise_for_status()`. OpenAlex uses cursor pagination; Crossref maps offset/cursor behavior behind the same protocol.

- [ ] **Step 6: Run Task 4 tests and verify GREEN**

Run: `pytest tests/test_service.py tests/test_connectors.py -v`
Expected: all pass.

- [ ] **Step 7: Run full checks**

Run: `pytest tests -v && ruff check src tests && mypy --strict src`
Expected: zero failures/errors.

---

### Task 5: CLI, CSV export, documentation, final verification

**Files:**
- Create: `src/paper_collector/export.py`
- Create: `src/paper_collector/cli.py`
- Create: `tests/test_export.py`
- Modify: `README.md`

**Interfaces:**
- `export_papers_csv(database_path: Path, output_path: Path) -> int`.
- CLI entrypoint `paper-collector`.

- [ ] **Step 1: Write failing CSV export test**

Test creates a SQLite DB, persists one paper, exports CSV, then verifies UTF-8 header and values.

- [ ] **Step 2: Run export test and verify RED**

Run: `pytest tests/test_export.py -v`
Expected: missing export API.

- [ ] **Step 3: Implement CSV export and CLI**

CLI commands:

```text
init-db
search
jobs
resume
export-csv
```

`search`/`resume` select only registered providers `openalex` or `crossref`.

- [ ] **Step 4: Run export and CLI smoke checks**

Run:

```bash
pytest tests/test_export.py -v
paper-collector --help
paper-collector init-db --database tests/output/smoke.sqlite
paper-collector export-csv --database tests/output/smoke.sqlite --output tests/output/papers.csv
```

Expected: commands exit 0 and files are created.

- [ ] **Step 5: Fresh final verification**

Run:

```bash
pytest tests -v
ruff check src tests
mypy --strict src
python -m compileall -q src
```

Expected: zero failures/errors.

- [ ] **Step 6: Review acceptance criteria and commit final implementation**

Confirm each design acceptance criterion against test/runtime evidence before opening a PR.
