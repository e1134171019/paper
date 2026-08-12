# Execution Notes — Direct-Scale Frontier Numeric Closure + Independent Review

Date: 2026-08-12

## Governance

Formal route refreshed from Google Drive:

- `00｜GLOBAL｜AI 工作系統總綱`
- `Research Evidence Pipeline v0.1`
- `Energy Conversion Evidence Schema v0.1`
- `00-A｜全域工具與執行資源登錄表`
- `00-B｜全域工具路由與執行回報規範`

The 29-resource registry is operationally interpreted as 28 numbered summary resources plus the later `Registry Amendment｜Exa｜2026-08-09`. The missing numbered `29.` entry remains a registry-index maintenance issue but does not mean Exa is absent from the registered set.

## Tool route

Actually used:

- Google Drive — governance / research-method SSOT refresh.
- GitHub — repository SSOT, parent PR readback, isolated branch and evidence artifacts.
- Sider Scholar/OpenAlex — direct-scale discovery and marginal-yield check.
- Exa — primary/publisher full-text discovery and source-grounded component/prototype checks.
- Tavily — Wiley primary-page extraction when direct Exa fetch failed.
- Firecrawl — independent-agent attempt and direct scrape attempt.

Relevant but not invoked:

- Zotero — reference management is relevant but repository remains project evidence SSOT.

Blocked/unavailable for the intended role:

- Hybrid MCP Gateway — appropriate as an independent reviewer in the registry, but no callable interface is exposed in this conversation.
- Firecrawl direct Wiley scrape — insufficient credits.
- Exa direct Wiley live fetch — livecrawl timeout.

All other registered resources were reviewed as not materially relevant to this evidence-review stage.

## Mutation boundary

All writes in this stage are isolated to:

`research/direct-scale-frontier-numeric-independent-review`

Base:

`research/direct-scale-pareto-frontier-closure`

No historical BATCH/review file was overwritten.

No merge to PR #11's base, earlier research branches or `main` was performed.

No deployment, PDF redistribution or Research Gap publication was performed.

## CI boundary

The repository workflow triggers pull-request CI only for PRs targeting `main`. This review chain intentionally does not target `main`; it must not be retargeted merely to obtain a CI badge. Evidence verification is therefore based on source readback, branch diff and PR diff rather than claiming a non-existent CI run.