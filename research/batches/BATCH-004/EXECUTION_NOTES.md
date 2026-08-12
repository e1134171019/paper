# BATCH-004 Execution Notes

Date: 2026-08-12

## Governance route

The formal execution refreshed and followed:

- `00｜GLOBAL｜AI 工作系統總綱`
- `Research Evidence Pipeline v0.1`
- `Energy Conversion Evidence Schema v0.1`
- `00-A｜全域工具與執行資源登錄表`
- `00-B｜全域工具路由與執行回報規範`

A governance-document mismatch was observed: `00-A` declares `registered_resource_count: 29`, while the visible mandatory-review summary index enumerates resources `01` through `28`. This batch does not invent a 29th entry. The mismatch is recorded as a governance-maintenance issue and is not treated as research evidence or as a blocker on individual paper verification.

## Tool route

- Google Drive: used to refresh project governance and research-method documents.
- GitHub: used as the repository source of truth and to create the isolated BATCH-004 branch/artifacts/PR.
- Sider Scholar/OpenAlex: used for scholarly discovery/mapping. Exact DOI lookup failed for some seeds, so it was not treated as complete citation-graph coverage.
- Firecrawl MCP: attempted for research search and returned HTTP 402; marked blocked for this pass.
- Public web primary/institutional/publisher sources: used as a fallback for current lawful full-text and source verification after Firecrawl/Sider limitations.
- Zotero: reviewed as relevant for bibliography management but not invoked because the repository remains the project evidence SSOT.

## Mutation boundary

All repository writes are isolated to `research/batch-004-coverage-closure`.

No merge to `research/repeated-tradeoff-audit-v0.2`, PR #9, `research/multi-assistant-direction-audit`, or `main` was performed.

No deployment, PDF redistribution, publisher-paywall bypass, or formal Research Gap publication was performed.

## Verification boundary

This batch is evidence-review data (CSV/Markdown), not a code change. The repository CI workflow is configured to run pull requests targeting `main`; the BATCH-004 review PR intentionally targets the v0.2 research branch and is not retargeted merely to obtain a CI badge.
