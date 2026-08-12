# Targeted Stopping Round 3

Date: 2026-08-12

## Question

After closing the Li/He/Luo 2023 target, does a narrow different-program/direct-scale search still produce materially useful uncaptured journal hardware evidence?

## Search boundary

This node did not restart a broad high-gain-converter literature search.

Queries were limited to combinations near the active COMP-HG/direct-Pareto acquisition region:

- input approximately 20–40 V;
- output approximately 380–400 V;
- hardware approximately 100–500 W, with direct Pareto emphasis on 150–300 W;
- switching frequency approximately 50–100 kHz when available;
- different author/research programs;
- journal hardware evidence;
- 2025–2026 recency emphasis.

Known Habibi, Jazi, Khan, Tran, Hasanpour, Abbasi/Rezaie, Yao/Guan and already staged BATCH-004 candidates were treated as duplicates/context, not new yield.

## New yield 1 — Scientific Reports 2026

DOI: `10.1038/s41598-026-51505-y`

Title: *Inductor-capacitor gain cell-based non-isolated high step-up converter for DC microgrid*.

Publisher page states:

- open-access Scientific Reports article;
- published 10 June 2026;
- current page is explicitly labeled an unedited version;
- experimental `20 V -> 400 V / 200 W` prototype;
- `94.5%` full-load efficiency;
- maximum stress on the two switches stated as `10%` of output voltage;
- interleaved input stage / smooth ripple-free input current.

Exact DOI search in the repository returned no prior indexed record.

Decision:

`MATERIAL_DIRECT_SCALE_NEW_YIELD`.

It is not promoted in this node. The current unedited-version boundary, switching frequency, complete component counts, stress vector and exact evidence locators require a dedicated audit.

## New yield 2 — Journal of Engineering 2025

DOI: `10.1155/je/5145061`

Title: *A New ZVT Quadratic High Step-Up Nonisolated DC-DC Converter*.

Authors: Alireza Abdollahi, Majid Delshad, Ramtin Sadeghi.

The primary Wiley record/full-text search exposes:

- `20 V -> 400 V`;
- `200 W` hardware prototype;
- `50 kHz` switching frequency;
- main + auxiliary switching structure;
- ZVT / semiconductor soft-switching claims;
- stated full-load efficiency around `95%`.

Exact DOI search in the repository returned no prior indexed record.

Decision:

`MATERIAL_DIRECT_SCALE_NEW_YIELD`.

It requires complete common-schema extraction before any L4/L5/family credit.

## New yield 3 — Results in Engineering 2025 boundary record

DOI: `10.1016/j.rineng.2025.104050`

Title: *Single-switch ultra-high step-Up DC-DC converter for PV applications*.

Publisher search states an experimental `20 V -> 400 V / 100 W` prototype.

This is below the frozen 150–300 W direct Pareto power window but inside the broader COMP-HG 100–500 W acquisition scope.

Decision:

`BOUNDARY_NEW_YIELD`.

## Stopping decision

Round 3 marginal yield is not low.

At least two different-author direct-scale journal hardware programs inside the key 20→400 V / 200 W region were absent from the current repository evidence register, plus one relevant lower-power boundary program.

Therefore:

`TARGETED_MARGINAL_YIELD = POSITIVE`

`SEARCH_SATURATION = NOT_MET`

The discovery of these records is an evidence-acquisition requirement. It is not a Research Gap.

## Authorized acquisition priority after this node

1. `10.1038/s41598-026-51505-y` — final/edited-version status + full-vector audit;
2. `10.1155/je/5145061` — full-vector audit and family adjudication;
3. retain `10.1016/j.rineng.2025.104050` as boundary context unless power-window policy changes;
4. run another narrow stopping test only after the two direct-scale records are no longer uncaptured evidence.
