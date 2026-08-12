# Verification Report — Khan + Tran Full-Vector / Stopping Round 2

Date: 2026-08-12
Branch: `research/khan-tran-full-vector-stopping-round-2`
Clean base SHA: `f1cd81cee9b617b5392798daa8e44fa0c0a35f0a`

## Research-state checks

PASS — evidence-level semantics preserved:

- Khan promoted only to bounded L4 partial; theoretical switch stress not relabeled measured;
- Khan maximum measured switch and diode stresses remain unresolved;
- Khan simulation load inconsistency is recorded rather than repaired;
- Tran remains L1 because complete full text is not legally readable under the current access state;
- Tran abstract values are not used to infer missing component/stress fields;
- Li/He/Luo 2023 is registered as a new stopping candidate only, not L5;
- L5 count remains 11 and independent-family count remains 6;
- independent review remains explicitly incomplete;
- formal Pareto and Research Gap remain unauthorized.

## Search/stopping checks

PASS — broad keyword search was not restarted.

PASS — Round 2 used targeted direct-scale/different-program acquisition logic.

FAIL_FOR_SATURATION — DOI `10.1007/s43236-022-00564-1` is a newly uncaptured 20 V -> 400 V / 200 W hardware program in the inspected project state.

Therefore:

`targeted_search_saturation = NOT_MET`.

## Source-policy checks

PASS — Khan legal/readable published full text resolved under CC BY.

PASS — Tran access restriction was respected; no subscription/login/paywall bypass was attempted.

PASS — no publisher PDF binary was committed.

PARTIAL TOOL FAILURE — Firecrawl returned insufficient credits and supplied no evidence.

PARTIAL VISUAL CHECK FAILURE — web PDF screenshot attempts for the Khan repository PDF returned cache-miss errors; those screenshots were not used as evidence. Text/full-document extraction and section/table/figure locators were available through the legal source path.

## Repository-integrity checks before this report

Clean-node comparison (`f1cd81c...` -> Round-2 branch) reported:

- status: `ahead`;
- ahead_by: `10`;
- behind_by: `0`;
- changed files: `10`;
- every changed-file status: `added`;
- modified inherited artifacts: `0`;
- deleted inherited artifacts: `0`.

The accidentally created old-branch file `INVALID` returned 404 on the clean Round-2 branch, confirming that it is not inherited here.

Comparison `main` -> Round-2 branch reported:

- main base SHA: `c88fe7254197082012494892b4141e1f39009bae`;
- branch status: `ahead`;
- behind_by: `0`.

No merge or branch update to `main` was performed in this node.

## Code/test boundary

This node adds research Markdown/CSV audit artifacts only. No Python/source-code file, schema, runtime behavior, or tests were modified; therefore no code test suite was required as evidence for this research-only change set.

## Current verdict

`PASS_FOR_REVIEW_ONLY_CONTINUATION`

The evidence package is internally consistent enough to continue the next targeted acquisition node, but it is not sufficient for formal Pareto or Research Gap authorization.
