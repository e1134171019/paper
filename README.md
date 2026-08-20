# Paper Collector

Evidence-oriented academic paper collection core for power-conversion research.

Collector Core v0.1 is intentionally small. It establishes the data pipeline that later powers the Research Explorer, full-text evidence extraction, and RAG layers.

## Research state

The current working memory for the low-voltage high-current DC↔AC loss/topology study is maintained in:

- [`research/RESEARCH_STATE.md`](research/RESEARCH_STATE.md)

> Current 2026-08-20 exploratory override: File 52 supersedes the File-51 R7 geometry check as the immediate research mainline. The search now uses two orthogonal axes: physical mechanism set (`R1...R9`) and functional-coordinate placement/overlap (`X1/X2/X3`). R2/Ryan remains comparator-only; R7 is retained only as a weak/conditional deferred branch; R8 remains low-priority. `O13 = X1+X3 with X2 separately identifiable and preferably post-X1/reduced-current` is the PRIMARY graph-synthesis branch because it may remove rectifier/HV-bus/VSI stage boundaries without adding another ~175-A source-domain path. `O23 = X2+X3 after X1 completion` is SECONDARY. PSIM/LTspice remain unauthorized until actual graph closure, loss bounds, 2ω energy closure, and multi-assistant IEEE gates are passed.

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
- [`research/41_R2_REFERENCE_RECLASSIFICATION_AND_ORIGINALITY_BOUNDARY_V1.md`](research/41_R2_REFERENCE_RECLASSIFICATION_AND_ORIGINALITY_BOUNDARY_V1.md) — reclassifies the Wu-type active-clamp work as `R2-REF1 / IEEE_REFERENCE_COMPARATOR`; changed parameters alone are not a project topology contribution.
- [`research/42_R2_ORIGINAL_CANDIDATE_GATE_A_SCREEN_V1.md`](research/42_R2_ORIGINAL_CANDIDATE_GATE_A_SCREEN_V1.md) — first independent R2 candidate screen: `R2-C1` stopped at IEEE Gate A; `R2-C2` retained only as a possibly differentiated commutation-energy-routing concept pending graph/state verification.
- [`research/43_MULTI_ASSISTANT_IEEE_PRIOR_ART_VERIFICATION_PROTOCOL_V1.md`](research/43_MULTI_ASSISTANT_IEEE_PRIOR_ART_VERIFICATION_PROTOCOL_V1.md) — mandatory multi-assistant/multi-route verification for every IEEE Gate A/B/C; a single assistant/search route cannot complete a formal prior-art decision.
- [`research/44_R2_C2_MULTI_ASSISTANT_GATE_B_TRIAL_V1.md`](research/44_R2_C2_MULTI_ASSISTANT_GATE_B_TRIAL_V1.md) — first multi-assistant Gate-B trial; stops `R2-C2-v0` before PSIM because the transition-only active shuttle risks relocating hard-switching loss into its auxiliary switch and sits in a mature resonant-commutation prior-art region.
- [`research/45_R2_C3_MULTI_ASSISTANT_PRIOR_ART_AND_REF2_LOCK_V1.md`](research/45_R2_C3_MULTI_ASSISTANT_PRIOR_ART_AND_REF2_LOCK_V1.md) — stops auxiliary-free magnetizing-current ZVS as an R2 novelty path and locks Ryan et al. 1998 as `R2-REF2`, a mandatory extreme-LV/high-current IEEE comparator near the 12 V / 2 kW boundary.
- [`research/46_A0_REF1_REF2_MATCHED_THEORETICAL_SCALING_SCREEN_V1.md`](research/46_A0_REF1_REF2_MATCHED_THEORETICAL_SCALING_SCREEN_V1.md) — matched 12-V/2-kW scaling screen; finds no first-order 235→325–400-V copper-window/reactive-energy wall for the Ryan-type reference.
- [`research/47_R2_REF2_MODERN_MATCHED_LOSS_CONTRACT_AND_CROSSOVER_V1.md`](research/47_R2_REF2_MODERN_MATCHED_LOSS_CONTRACT_AND_CROSSOVER_V1.md) — normalizes A0/REF1/REF2 to modern matched silicon and quantifies the loss-location crossover; retained as comparator analysis, not the current topology-synthesis mainline.
- [`research/48_R2_REF2_REDUCED_ORDER_SURROGATE_SIMULATION_V1.md`](research/48_R2_REF2_REDUCED_ORDER_SURROGATE_SIMULATION_V1.md) — reduced-order pre-PSIM Ryan/REF2 surrogate; useful comparator evidence only after the mainline restoration.
- [`research/49_MAINLINE_RESTORE_R7_R8_MULTI_ASSISTANT_GATE_A_V1.md`](research/49_MAINLINE_RESTORE_R7_R8_MULTI_ASSISTANT_GATE_A_V1.md) — restores the original topology-synthesis intent, pauses Ryan deep-dive, runs multi-assistant Gate A on R7/R8, selects post-magnetic `R7` graph synthesis as the immediate NEXT, and deprioritizes R8 because its boost path remains in the ~175-A source domain.
- [`research/50_R7_C1A_C1B_ACTUAL_GRAPH_AND_MULTI_ASSISTANT_GATE_B_V1.md`](research/50_R7_C1A_C1B_ACTUAL_GRAPH_AND_MULTI_ASSISTANT_GATE_B_V1.md) — executes two concrete R7 graphs and Gate B: `R7-C1A` (post-rectifier active 3:1 series-parallel SC) is rejected as a cascade/composition of known subgraphs, while `R7-C1B` (HFT + voltage-doubler rectifier) is rejected as a known secondary primitive. The next R7 graph must integrate PM1 and PM3 at the secondary-state level.
- [`research/51_R7_GAIN_SHARING_CHARGE_RMS_BREAK_EVEN_SCREEN_V1.md`](research/51_R7_GAIN_SHARING_CHARGE_RMS_BREAK_EVEN_SCREEN_V1.md) — topology-independent 360/180/120/90/60-V gain-sharing sweep. Establishes the flying-cap charge/RMS burden, rejects the shortcut that lower HFT voltage automatically means lower transformer loss/volume, retains only `k=2` and `k=3` for a geometry-specific magnetic crossover, and blocks PSIM until that crossover is quantified.
- [`research/52_X1_X2_X3_NODE_OVERLAP_MATRIX_AND_MAINLINE_RESET_V1.md`](research/52_X1_X2_X3_NODE_OVERLAP_MATRIX_AND_MAINLINE_RESET_V1.md) — adds the missing coordinate-placement axis, quantifies the 2ω energy requirement, maps `X1|X2|X3`, `X1+X3|X2`, `X1|X2+X3`, `X1+X2|X3`, and `X1+X2+X3`, and promotes reduced-current `O13` overlap to the primary actual-graph search while deferring the weak R7 geometry branch.

These documents are working research state, not final novelty claims. Candidate gaps remain provisional until closest-prior-art closure is complete. The current publication workflow treats IEEE Xplore as the primary prior-art corpus for research-effort control; an IEEE-only search pass is not a universal proof of novelty. Formal IEEE Gate completion additionally requires the multi-assistant protocol in File 43.

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
