# Paper Collector

Evidence-oriented academic paper collection core for power-conversion research.

Collector Core v0.1 is intentionally small. It establishes the data pipeline that later powers the Research Explorer, full-text evidence extraction, and RAG layers.

## Research state

The historical research state for the low-voltage high-current DC↔AC study is maintained in:

- [`research/RESEARCH_STATE.md`](research/RESEARCH_STATE.md)

The authoritative current-mainline override is:

- [`research/CURRENT_MAINLINE_OVERRIDE_2026-08-20.md`](research/CURRENT_MAINLINE_OVERRIDE_2026-08-20.md)

> Current 2026-08-20 mainline: File 59 executed the A0 `EDGE-LOSS / REMOVABILITY TARGET SELECTION`. Two rankings are now kept separate. By currently known/bounded watts, `E2 primary commutation/snubber` is the strongest loss target (`~25.10 W`, MODELLED / NOT MEASURED), followed by `E4 secondary rectification` (`~17.14 W` matched-technology floor) and `E1 primary LV main-switch conduction` (`~12.31 W` proxy). For topology-synthesis leverage, however, the selected next target is the **joint `E4+E6` post-HFT semiconductor double-processing boundary**: full-power secondary rectification followed by full-power VSI AC synthesis. `E2` is retained as a control/comparator because active-clamp, resonant and Ryan-type soft-switching regions are already prior-art dense. The generic direct-HF-link/matrix replacement of `E4+E6` is also established prior art and is therefore a hard comparator, not a proposed contribution. Immediate next is File 60: a matched semiconductor/current/commutation/X2 loss crossover between the A0-like `rectifier → HV-link/X2 → VSI` path and the known merged direct-HF-link reference. Candidate #10 remains `HOLD / NOT_ASSIGNED`; novelty remains `NOT_ESTABLISHED`; PSIM/LTspice/hardware are not executed.

Detailed reasoning is split into focused working documents:

- [`research/01_SCOPE.md`](research/01_SCOPE.md) — operating envelope and research question.
- [`research/02_TOPOLOGY_TAXONOMY.md`](research/02_TOPOLOGY_TAXONOMY.md) — current topology-family map.
- [`research/03_LOSS_PHYSICS.md`](research/03_LOSS_PHYSICS.md) — RMS, `I²R`, 2ω and loss migration.
- [`research/04_PRIOR_ART_CLOSURE.md`](research/04_PRIOR_ART_CLOSURE.md) — prior-art closure and novelty boundary.
- [`research/05_RESEARCH_HYPOTHESIS.md`](research/05_RESEARCH_HYPOTHESIS.md) — current energy-routing hypothesis.
- [`research/06_VALIDATION_PLAN.md`](research/06_VALIDATION_PLAN.md) — analytical, PLECS, LTspice, Maxwell/Q3D and hardware gates.
- [`research/07_BENCHMARKS.md`](research/07_BENCHMARKS.md) — benchmark architectures and comparison rules.
- [`research/08_DECISION_LOG.md`](research/08_DECISION_LOG.md) — dated research decisions.
- [`research/28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md`](research/28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md) — authoritative X1/X2/X3 coordinate definition.
- [`research/33_COMBINATION_LOSS_AUDIT_GATE.md`](research/33_COMBINATION_LOSS_AUDIT_GATE.md) — mandatory total-loss and loss-relocation gate.
- [`research/36_THEORETICAL_MECHANISM_COMBINATION_SCREEN_V1.md`](research/36_THEORETICAL_MECHANISM_COMBINATION_SCREEN_V1.md) — theoretical R1–R9 mechanism-combination screen.
- [`research/37_IEEE_PRIOR_ART_GATE_AND_NOVELTY_CONTROL_V1.md`](research/37_IEEE_PRIOR_ART_GATE_AND_NOVELTY_CONTROL_V1.md) — mandatory IEEE prior-art gates.
- [`research/43_MULTI_ASSISTANT_IEEE_PRIOR_ART_VERIFICATION_PROTOCOL_V1.md`](research/43_MULTI_ASSISTANT_IEEE_PRIOR_ART_VERIFICATION_PROTOCOL_V1.md) — multi-route/multi-assistant verification protocol.
- [`research/47_R2_REF2_MODERN_MATCHED_LOSS_CONTRACT_AND_CROSSOVER_V1.md`](research/47_R2_REF2_MODERN_MATCHED_LOSS_CONTRACT_AND_CROSSOVER_V1.md) — current A0 commutation and modern-device loss anchors.
- [`research/49_MAINLINE_RESTORE_R7_R8_MULTI_ASSISTANT_GATE_A_V1.md`](research/49_MAINLINE_RESTORE_R7_R8_MULTI_ASSISTANT_GATE_A_V1.md) — restored topology-synthesis mainline and R7/R8 Gate A.
- [`research/50_R7_C1A_C1B_ACTUAL_GRAPH_AND_MULTI_ASSISTANT_GATE_B_V1.md`](research/50_R7_C1A_C1B_ACTUAL_GRAPH_AND_MULTI_ASSISTANT_GATE_B_V1.md) — stops obvious R7 cascade/doubler graphs.
- [`research/51_R7_GAIN_SHARING_CHARGE_RMS_BREAK_EVEN_SCREEN_V1.md`](research/51_R7_GAIN_SHARING_CHARGE_RMS_BREAK_EVEN_SCREEN_V1.md) — gain-sharing/charge-RMS screen; R7 becomes weak/deferred.
- [`research/52_X1_X2_X3_NODE_OVERLAP_MATRIX_AND_MAINLINE_RESET_V1.md`](research/52_X1_X2_X3_NODE_OVERLAP_MATRIX_AND_MAINLINE_RESET_V1.md) — coordinate-placement/overlap matrix.
- [`research/53_G13_A_ACTUAL_GRAPH_STATE_CLOSURE_AND_MULTI_ROUTE_GATE_A_V1.md`](research/53_G13_A_ACTUAL_GRAPH_STATE_CLOSURE_AND_MULTI_ROUTE_GATE_A_V1.md) — direct HF-link/matrix actual graph and Gate A; retained as comparator.
- [`research/54_G23_A_X2_X3_SHARED_STORAGE_SYNTHESIS_AND_GATE_A_V1.md`](research/54_G23_A_X2_X3_SHARED_STORAGE_SYNTHESIS_AND_GATE_A_V1.md) — split-link/flying-cap X2+X3 screen.
- [`research/55_G23_B_DIFFERENTIAL_STORAGE_COMMON_MODE_DECOUPLING_GATE_A_V1.md`](research/55_G23_B_DIFFERENTIAL_STORAGE_COMMON_MODE_DECOUPLING_GATE_A_V1.md) — differential/common-mode APD screen.
- [`research/56_G12_A_X1_X2_SHARED_FRONT_END_POWER_DECOUPLING_GATE_A_V1.md`](research/56_G12_A_X1_X2_SHARED_FRONT_END_POWER_DECOUPLING_GATE_A_V1.md) — X1+X2 front-end buffering screen.
- [`research/57_G123_A_TRIPLE_OVERLAP_STATE_FALSIFICATION_AND_GATE_A_V1.md`](research/57_G123_A_TRIPLE_OVERLAP_STATE_FALSIFICATION_AND_GATE_A_V1.md) — closes generic X1/X2/X3 overlap as a novelty generator.
- [`research/58_EDGE_LEVEL_PARTIAL_POWER_SYNTHESIS_RESET_V1.md`](research/58_EDGE_LEVEL_PARTIAL_POWER_SYNTHESIS_RESET_V1.md) — introduces `αP/αS/αI/αV` partial-power accounting and closes generic PPP as a novelty generator.
- [`research/59_A0_EDGE_LOSS_REMOVABILITY_TARGET_SELECTION_V1.md`](research/59_A0_EDGE_LOSS_REMOVABILITY_TARGET_SELECTION_V1.md) — ranks E1–E7 and selects joint `E4+E6` as the immediate matched-loss crossover target while retaining E2 as the strongest known loss bucket/control target.

These documents are working research state, not final novelty claims. Candidate gaps remain provisional until closest-prior-art closure is complete. IEEE Xplore is the primary prior-art corpus for research-effort control, but an IEEE-only search pass is not a universal proof of novelty. Formal Gate completion additionally requires the multi-assistant protocol in File 43.

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
