# BATCH-001 — Power Converter Candidate Staging

Date: 2026-08-12

This batch is a **candidate staging snapshot**, not formal research evidence.

## Scope

Independent discovery lanes were used for:

- CLLC / LLC resonant converters
- DAB / bidirectional converters
- Partial-power processing
- High-gain DC-DC
- GaN / SiC and high-power-density designs
- Soft switching (ZVS / ZCS)

Discovery sources included Sider Scholar, Firecrawl Research, Exa, Tavily, publisher pages, and institutional repositories.

## Gate applied

The formal research gate remains journal-first and evidence-first:

1. discovery result
2. DOI / canonical metadata check
3. journal / publication-type gate
4. legal or readable full-text resolution
5. hardware-prototype locator
6. numerical claim locator
7. comparison-boundary audit
8. only then comparison-ready / gap-ready

Search-tool output is never treated as evidence by itself.

## Files

- `candidates.csv` — journal candidates that survived the first metadata/prototype screen.
- `rejected.csv` — items deliberately excluded from the formal evidence set at this stage.
- `search_log.jsonl` — append-only provenance for the discovery lanes used in this batch.
- `evidence_audit.csv` — per-paper audit state, full-text source, experiment locator, numerical locator and evidence level.
- `evidence_claims.csv` — numerical claims that passed the BATCH-001 audit with explicit metric boundaries and locators.
- `unresolved.csv` — unresolved full-text or metric issues that block further promotion.
- `comparison_sets.csv` — instantiated comparison questions, gates, blocking reasons and targeted acquisition requirements under Power Converter Comparison Contract v0.1.
- `comparison_exclusions.csv` — direct comparisons explicitly prohibited because their metrics or boundaries are incompatible.

Reusable contract:
- `../../contracts/power_converter_comparison_contract_v0.1.md`

## Status semantics

- `L1_METADATA_VERIFIED`: DOI / canonical journal metadata is resolved, but the full-text evidence gate is not yet satisfied.
- `L2_PDF_VERIFIED`: a legal/readable full text is resolved but experimental evidence has not yet been located.
- `L3_EXPERIMENT_LOCATED`: hardware and experimental section/figure/table locators are established.
- `L4_NUMERICALLY_VERIFIED`: one or more numerical claims have explicit metric definitions, operating conditions and locators.
- `L5_COMPARISON_READY`: claims additionally satisfy an instantiated cross-paper comparison contract containing at least two independent papers.

No record becomes `comparison_ready` or `gap_ready` merely because it appears in this folder.

## Evidence Audit 2026-08-12

BATCH-001 contains 13 journal candidates. The first evidence audit resolved all three previously missing DOIs and produced the following conservative state:

- L4 NUMERICALLY_VERIFIED: 8 papers
- L3 EXPERIMENT_LOCATED: 3 papers
- L1 METADATA_VERIFIED: 2 papers
- L5 COMPARISON_READY: 0 papers

The two L1 records are retained because their DOI/publisher metadata is valid but a legal/readable public full text was not resolved. They are not rejected.

The audit also confirmed that a flat efficiency leaderboard would be invalid. In particular, full-power converter efficiency, partial-power system efficiency, calorimetric converter efficiency, and model-prediction accuracy are different metrics/boundaries.

## Comparison Contract Application 2026-08-12

Power Converter Comparison Contract v0.1 was applied to the existing 13-paper evidence pool.

Instantiated sets:

- `COMP-PP-001` — processed-power fraction versus total partial-power system efficiency.
- `COMP-DAB-001` — DAB modulation trade-off among RMS current, ZVS range and measured efficiency.
- `COMP-DCX-001` — high-power isolated DC-transformer efficiency/power-density trade-off.
- `COMP-HG-001` — non-isolated high-gain gain/stress/soft-switching/efficiency trade-off.
- `COMP-OBC-PPP-001` — variable-turns-ratio partial-power OBC soft-switching/system-efficiency trade-off.

Result:

- L5 promotions: **0**
- blocked comparison sets: **4**
- context-only sets: **1**

This is an expected evidence-first outcome. The existing papers are strong enough to define targeted acquisition requirements, but not yet strong enough to justify a direct cross-paper efficiency leaderboard.

The next evidence-acquisition targets are now bounded by the comparison contract rather than broad topical search. A missing comparator or missing field is an acquisition requirement, not a Research Gap.

## SSOT boundary

SQLite remains the canonical structured source of truth for the collector. This folder is a Git-versioned human-readable staging/audit snapshot for later ingestion. It must not become a parallel authoritative database.