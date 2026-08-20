# Paper Collector

Evidence-oriented academic paper collection core for power-conversion research.

Collector Core v0.1 is intentionally small. It establishes the data pipeline that later powers the Research Explorer, full-text evidence extraction, and RAG layers.

## Research state

The current working memory for the low-voltage high-current DC↔AC loss/topology study is maintained in:

- [`research/RESEARCH_STATE.md`](research/RESEARCH_STATE.md)

Detailed reasoning is split into focused working documents:

- [`research/01_SCOPE.md`](research/01_SCOPE.md) — operating envelope and research question.
- [`research/02_TOPOLOGY_TAXONOMY.md`](research/02_TOPOLOGY_TAXONOMY.md) — current topology-family map.
- [`research/03_LOSS_PHYSICS.md`](research/03_LOSS_PHYSICS.md) — RMS, `I²R`, 2ω and loss migration.
- [`research/04_PRIOR_ART_CLOSURE.md`](research/04_PRIOR_ART_CLOSURE.md) — prior-art closure and novelty boundary.
- [`research/05_RESEARCH_HYPOTHESIS.md`](research/05_RESEARCH_HYPOTHESIS.md) — current energy-routing hypothesis.
- [`research/06_VALIDATION_PLAN.md`](research/06_VALIDATION_PLAN.md) — analytical, PLECS, LTspice, Maxwell/Q3D and hardware gates.
- [`research/07_BENCHMARKS.md`](research/07_BENCHMARKS.md) — benchmark architectures and comparison rules.
- [`research/08_DECISION_LOG.md`](research/08_DECISION_LOG.md) — dated research decisions.
- [`research/36_THEORETICAL_MECHANISM_COMBINATION_SCREEN_V1.md`](research/36_THEORETICAL_MECHANISM_COMBINATION_SCREEN_V1.md) — current pre-PG theoretical combination screen for R1–R9.
- [`research/37_IEEE_PRIOR_ART_GATE_AND_NOVELTY_CONTROL_V1.md`](research/37_IEEE_PRIOR_ART_GATE_AND_NOVELTY_CONTROL_V1.md) — mandatory IEEE Xplore Gate A/B/C before deep simulation, graph promotion, or contribution claims.

These documents are working research state, not final novelty claims. Candidate gaps remain provisional until closest-prior-art closure is complete. The current publication workflow treats IEEE Xplore as the primary prior-art corpus for research-effort control; an IEEE-only search pass is not a universal proof of novelty.

## What v0.1 does

- Searches OpenAlex and Crossref through a provider-neutral connector interface.
- Canonicalizes DOI and titles.
- Deduplicates DOI-first, with a conservative title fallback only when both records have no DOI.
- Stores papers, provenance, search jobs, cursors, and PDF artifact metadata in SQLite.
- Resumes interrupted searches from a persisted cursor.
- Records PDF URLs supplied by academic metadata providers without bypassing publisher access controls.
- Calculates SHA-256 for local PDF files obtained through an approved/legal route.
- Regenerates human-readable CSV from SQLite.

## What v0.1 does not do

- No paywall, CAPTCHA, or credential bypass.
- No automatic subscription-PDF downloading.
- No LLM evidence extraction yet.
- No GROBID/Docling parsing yet.
- No vector database/RAG yet.
- No web dashboard yet.

## Architecture

```text
OpenAlex / Crossref
        |
        v
DiscoveryConnector
        |
        v
Canonicalization
        |
        v
SQLite SSOT
  papers
  paper_sources
  search_jobs
  search_cursors
  pdf_artifacts
        |
        +--> CSV export
        +--> future GROBID / evidence extraction
        +--> future Research Explorer
```

## Setup

Python 3.11+ is required.

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## CLI

Initialize the local SQLite source of truth:

```bash
paper-collector init-db --database data/research.sqlite
```

Search OpenAlex:

```bash
paper-collector search \
  --provider openalex \
  --query "dual active bridge" \
  --max-results 100 \
  --database data/research.sqlite
```

Search Crossref:

```bash
paper-collector search \
  --provider crossref \
  --query "bidirectional CLLC resonant converter" \
  --max-results 100 \
  --database data/research.sqlite
```

Inspect jobs:

```bash
paper-collector jobs --database data/research.sqlite
```

Resume an interrupted job:

```bash
paper-collector resume <JOB_ID> --database data/research.sqlite
```

Generate a human-readable CSV snapshot:

```bash
paper-collector export-csv \
  --database data/research.sqlite \
  --output exports/papers.csv
```

## Data policy

SQLite is the source of truth. CSV is derived and may be regenerated at any time.

The local SQLite file and downloaded PDFs are ignored by Git because this repository is public and scientific PDFs may have license restrictions. Human-readable metadata exports can be committed deliberately after review.

## Development verification

```bash
pytest tests -v
ruff check src tests
mypy --strict src
python -m compileall -q src
```

See `docs/superpowers/specs/2026-08-12-collector-core-v0.1-design.md` for the approved design and `docs/superpowers/plans/2026-08-12-collector-core-v0.1.md` for the implementation plan.
