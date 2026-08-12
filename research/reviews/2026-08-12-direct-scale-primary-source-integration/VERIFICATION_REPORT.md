# Verification Report

Date: 2026-08-12

## Scope verified

`SIX CORE PDF FULL EXTRACTION + DIRECT-SCALE PRIMARY-SOURCE INTEGRATION + FAMILY DEDUP + FRONTIER RE-RUN`

## Closed in this node

- Six newly supplied IEEE primary PDFs were fully boundary-screened and numerically audited to the extent supported by source text/figures.
- Two of the six newly supplied PDFs qualify as direct-scale under the frozen contract: Abbasi 2024 and Yao 2023.
- Two are retained as neighbor-scale context: Liao 2024 and Ding 2025.
- Two are retained as high-voltage/high-power context: Bhaskar 2026 and Omran 2025.
- IEEE document 11159317 / DOI `10.1109/TPEL.2025.3608899` full-text blocker is closed; the official primary PDF supports L5 bounded admission.
- Hasanpour 2023 and Hasanpour/Nouri 2025 primary IEEE PDFs are integrated with measured/theory boundaries preserved.
- Bounded L5 snapshot increases from 6 to **11** records.
- Independent L5 evidence-family count increases from 4 to **6** because Abbasi/Kashani/Rezaie and Yao/Guan add two independent direct-scale programs.
- Exploratory two-objective stress-pair screen is produced for internal evidence prioritization only.
- Broad keyword searching is stopped in favor of targeted saturation work.

## Verification of isolated GitHub execution

- Working branch: `research/direct-scale-primary-source-integration`.
- Base commit: `16287acdc0f8e7bdfc77287dec9281f83550e21f` (PR #15 head at node start).
- Before this verification report was added, branch comparison showed `ahead_by=10`, `behind_by=0`, with ten added review artifacts and no modifications/deletions to prior review files.
- This report is the eleventh append-only artifact in the node.
- No `main` branch modification occurred.
- No existing pull request was modified.
- No new pull request, merge, deployment, or publication was performed.

## Data-integrity checks

- No publisher PDF binary was committed to GitHub.
- Original `typed_frontier_v5.csv`, prior provenance, prior adjudication, and prior gate files are preserved; `v6`/`v2`/`v3` artifacts are append-only snapshots.
- Exact, approximate, upper-bound, theory-at-prototype, conflict, and unresolved semantics are preserved rather than flattened.
- Measured values are not relabeled from theory-derived values.
- Multi-switch records use maximum controlled-switch stress for comparison.
- Cross-scale records (300 V, 380 V/500 W, 650 V/500 W, 1 kV/500 W) are not ranked as direct 400 V / ~200 W peers.
- Efficiency remains a descriptor and is excluded from ranking.
- Paper count and independent-family count remain separate.
- Hasanpour-lineage papers are retained as topology evidence but do not receive duplicate independent-family credit.
- No independent-review credit is claimed; `independence_missing=true` remains explicit.

## Primary findings verified

### Abbasi 2024

At 20→400 V / 240 W / 50 kHz, the primary PDF reports measured S1=39.5 V, S2=102 V and diode values D1=36 V, D2=38 V, D3=174 V, D4=399 V, Do=269 V. Thus the measured stress pair used in the exploratory screen is approximately `(0.255, 0.9975)` for maximum controlled-switch and maximum diode stress normalized to Vout.

### Yao 2023

The primary PDF supports a 40→~400 V / 200 W / 500 kHz prototype with a planar three-winding coupled inductor, experimental switch ZVS, diode ZCS and 95.55% efficiency at 200 W. Exact measured maximum semiconductor voltage-stress scalars are not text-locked; prototype-equation values remain labeled `theory_at_prototype`.

### IEEE 11159317

The primary PDF closes the prior metadata-only status. The record is 25→400 V / 200 W / 50 kHz with measured switch stress approximately 50 V and maximum measured diode stress approximately 180 V, giving the bounded stress pair approximately `(0.125, 0.45)`.

## Improved but not closed

- Yao 2023: exact measured maximum switch/diode voltage-stress scalars remain unresolved.
- Hasanpour 2023: exact measured maximum diode stress remains unresolved; theoretical prototype value retained separately.
- Hasanpour/Nouri 2025: exact measured maximum diode scalar remains unresolved and a theory/measurement-boundary difference remains.
- Ding 2025: measured maximum stress across all diodes remains unresolved.
- Omran 2025: measured first-stage diode stress is available, but measured maximum across all eight VM diodes remains unresolved.
- Bhaskar 2026: measured maximum diode scalar remains unresolved and the source remains an accepted author version.

## Still blocked

- PC-CAND-0024 maximum measured diode-stress scalar.
- DOI `10.1155/etep/9317966` maximum measured diode-stress scalar.
- Independent source/packet interpretation of the expanded direct-scale evidence set.
- Formal search saturation / stopping rule: the latest six-PDF batch still added two independent direct-scale L5 families, so marginal yield remains positive.
- Formal all-objective Pareto declaration.
- Research Gap Candidate authorization.

## Exploratory frontier boundary

The two-objective stress-only screen may be used internally to guide evidence acquisition. It is **not** a formal all-objective Pareto frontier. In the measured-to-measured subset, PC-CAND-0027 (`~0.155`, `~0.275`) and IEEE11159317 (`~0.125`, `~0.45`) remain robust tradeoff candidates; several other direct records are stress-pair dominated on those two axes only. Component count, magnetic burden, input ripple, common ground, soft switching, power density, thermal burden, control complexity, and unresolved evidence can change all-objective ordering.

## Verification result

`PASS_FOR_REVIEW_ONLY_CONTINUATION`

This verifies the isolated research node only. It does not authorize merge to `main`, PR integration, formal Pareto-optimal labeling, or Research Gap declaration.
