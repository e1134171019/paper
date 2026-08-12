# Verification Report — Li/He/Luo 2023 / Stopping Round 3

Date: 2026-08-12
Branch: `research/li-he-luo-2023-full-vector-stopping-round-3`
Base SHA: `5f3ef9e860c2f88e3c55cb967e66780ba3d3aba2`

## 1. Governance verification

Refreshed before mutation:

- AI Work System global router;
- Research Evidence Pipeline v0.1 candidate method;
- Energy Conversion Evidence Schema v0.1;
- global resource registry and routing/reporting policy;
- repository `AGENTS.md`;
- frozen comparison/stress/Pareto policies.

The task stayed inside the approved research-only branch scope.

## 2. Target identity/source verification

DOI/title/authors/journal identity was cross-checked across the Journal of Power Electronics scholarly record and a public author-uploaded full-text article.

The readable complete text exposes the target sections, tables, equations and figure captions required for the audit.

The downloadable binary PDF endpoint itself could not be fetched in this runtime, so no screenshot-only measurement was claimed and no PDF binary was committed.

## 3. Li numerical verification

Prototype boundary locked:

- `Vin = 20 V`;
- `Vout = 400 V`;
- `Pout,rated = 200 W`;
- `fs = 50 kHz`.

Measured switch stress locked:

- `Vds = 117 V` at rated conditions;
- `117/400 = 0.2925` normalized measured controlled-switch stress.

Theoretical diode vector was recalculated from the paper's equations only after solving the gain equation for the declared prototype boundary. The maximum theory value is approximately 234.39 V / 0.5860 Vout.

The exact topology-wide measured diode peak remains unresolved and was not replaced by the theory value.

Efficiency semantics verified separately:

- maximum about 95.2% at 80 W;
- full-load 93.7% at 200 W.

No cross-paper efficiency ranking was produced.

## 4. Internal-conflict verification

The article separately reports `Io = 0.2 A` in a 20 V / 400 V design statement and `Pout = 200 W` as rated prototype power.

Arithmetic check:

`400 V * 0.2 A = 80 W`.

The conflict is real if those fields are interpreted as one operating point. The audit therefore records `INTERNAL_CURRENT_POWER_BOUNDARY_INCONSISTENCY` and excludes the current sentence from the full-load comparison definition.

No silent repair was performed.

## 5. L5/family verification

The frozen direct-scale protocol and `COMP-HG-001` comparison contract were reapplied.

Li passes bounded L5 admission because it provides a direct-scale primary journal hardware boundary plus a source-locked measured semiconductor-stress locator and explicit structural/operating fields.

Result:

`L5_COMPARISON_READY / BOUNDED_MEMBER`.

Family adjudication treats the recurring Li/He/Luo/Jiang topology-development line as a coherent program distinct from the six previously credited L5 programs.

Count after admission:

- bounded L5 records: `12`;
- independent L5 evidence families: `7`.

## 6. Stopping-rule verification

Round 3 was deliberately narrow and surfaced:

- `10.1038/s41598-026-51505-y` — materially new direct-scale 20->400 V / 200 W Scientific Reports program;
- `10.1155/je/5145061` — materially new direct-scale 20->400 V / 200 W / 50 kHz Journal of Engineering program;
- `10.1016/j.rineng.2025.104050` — lower-power 20->400 V / 100 W boundary program.

Exact DOI repository searches returned no indexed project records for the three targets during this node.

Therefore the stopping result is verified as:

`TARGETED_MARGINAL_YIELD = POSITIVE`

`SEARCH_SATURATION = NOT_MET`.

## 7. Independent-review verification

Two genuine external independent-review routes were attempted:

- Tavily Research: blocked by plan usage limit (`432`);
- Firecrawl Agent: blocked by insufficient credits.

Neither returned an independent review, so:

`independent_review = NOT_COMPLETE`

`independence_missing = true`.

## 8. Repository isolation verification

GitHub compare against the exact base SHA after the first eleven Round-3 artifacts reported:

- status: `ahead`;
- ahead_by: `11`;
- behind_by: `0`;
- changed files: `11`;
- all changed-file statuses: `added`;
- inherited files modified: `0`;
- inherited files deleted: `0`.

This verification report is the twelfth append-only artifact.

## 9. Gate result

- Li L5 promotion: `VERIFIED`;
- Li independent family credit: `VERIFIED`;
- targeted saturation: `NOT_MET`;
- independent review: `NOT_COMPLETE`;
- formal all-objective Pareto: `NOT_AUTHORIZED`;
- Research Gap Candidate: `NOT_AUTHORIZED`.

No merge to `main`, PR mutation, deployment, publication or downloaded publisher PDF commit was performed.
