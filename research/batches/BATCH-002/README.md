# BATCH-002 — Targeted Comparison Acquisition

Date: 2026-08-12

This batch is a **comparison-contract-driven acquisition snapshot**. It does not broaden the literature search indiscriminately and it does not promote records to `L5_COMPARISON_READY` by discovery alone.

## Upstream contract

- `research/contracts/power_converter_comparison_contract_v0.1.md`
- BATCH-001 `comparison_sets.csv`

## Acquisition objective

BATCH-002 searches specifically for evidence that can remove blockers in five comparison sets:

1. `COMP-PP-001` — processed-power fraction vs measured partial-power system efficiency.
2. `COMP-DAB-001` — DAB modulation trade-off among RMS current, ZVS range and measured efficiency under matched conditions.
3. `COMP-DCX-001` — high-power isolated DCX efficiency / power-density / switching-frequency trade-off.
4. `COMP-HG-001` — high-gain gain / normalized stress / soft-switching / efficiency trade-off.
5. `COMP-OBC-PPP-001` — OBC partial-power efficiency / processed-power fraction / ZCS-ZVS range over battery voltage.

## Files

- `candidates.csv` — journal candidates that meet the targeted-acquisition metadata gate.
- `target_map.csv` — how each candidate maps to a comparison-set blocker and what must be audited next.
- `rejected.csv` — search results deliberately excluded or held outside the formal evidence set.
- `search_log.jsonl` — append-only search provenance and query intent.

## Admission rules

A record enters `candidates.csv` only when:

- it is a journal article;
- DOI or equivalent persistent journal identifier is locked;
- a real hardware prototype is indicated by publisher/institutional/full-text evidence;
- it targets at least one comparison-set blocker;
- source and acquisition status are recorded.

`fulltext_ready` means a legal/readable publisher or institutional source was located for the next audit. It does **not** mean that every numerical claim is already verified.

`fulltext_unresolved` means metadata/prototype information is useful but the hard full-text gate remains unsatisfied.

## Important negative result

A relevant paper using HIL/simulation without a verified physical converter power-stage prototype is not admitted as formal hardware evidence. Conference papers and reviews remain outside the journal-first formal evidence pool even when technically useful.

## BATCH-002 acquisition result

This snapshot contains targeted journal candidates across Partial Power, DAB, DCX, High-Gain and OBC-PPC. The strongest immediate audit targets are:

- 22 kW FB/PP series partial-power converter with an explicit 20% processed-power design boundary;
- 1 kW DAB hardware papers focused on optimized phase-shift / ZVS / RMS-current behavior;
- 15 kW / 500 kHz CLLC/DCX evidence plus a same-constraint 10.9 kW DAB-vs-CLLC experimental comparison;
- multiple 200 W-class, approximately 20–30 V to 400 V high-gain prototypes, including quasi-resonant/ZCS designs.

No Research Gap is claimed. No BATCH-002 record is `L5_COMPARISON_READY` until the numerical and boundary audit is completed against the contract.

## SSOT boundary

SQLite remains the canonical structured SSOT. This batch is a Git-versioned research acquisition/audit artifact for later ingestion and must not become a parallel authoritative database.
