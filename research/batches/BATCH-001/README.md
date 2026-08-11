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

## Status semantics

- `metadata_verified`: title / journal / persistent identifier and a hardware indication were traceable from publisher or institutional sources; full-text evidence locators are still pending unless explicitly stated later.
- `doi_unresolved`: publisher journal record and prototype information were found, but DOI was not yet locked in this batch.

No record in this folder is `fulltext_verified`, `numerically_verified`, `comparison_ready`, or `gap_ready` merely because it appears here.

## SSOT boundary

SQLite remains the canonical structured source of truth for the collector. This folder is a Git-versioned human-readable staging snapshot for audit and later ingestion. It must not become a parallel authoritative database.
