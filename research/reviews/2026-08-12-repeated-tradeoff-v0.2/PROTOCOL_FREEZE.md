# Repeated Trade-off Pattern Audit v0.2 — Protocol Freeze

Date: 2026-08-12
Status: FROZEN_FOR_THIS_AUDIT
Parent evidence: BATCH-002, BATCH-003, Multi-Assistant Direction Audit

## Research question

For non-isolated high-step-up DC-DC hardware near the current comparison scale, what recurring design trade-offs link semiconductor voltage stress, soft-switching behavior, topology/magnetic complexity, source-current behavior, common-ground capability, switching frequency, and measured efficiency descriptors?

## Direct comparison scope

- Peer-reviewed journal article.
- Real hardware prototype.
- Non-isolated high-step-up DC-DC converter.
- Nominal output around 380–400 V.
- Prototype power approximately 150–300 W.
- Low-voltage input approximately 20–50 V.
- Exact/reproducible evidence locator for admitted metrics.
- Numeric claims cannot be admitted from abstract-only metadata.
- Current core L5 evidence families: PC-CAND-0024, PC-CAND-0027, PC-CAND-0028, PC-CAND-0030.

## Context / falsification scope

Counter-search may include approximately 15–50 V input, 150–360 W and 300–400 V output when needed to test whether a proposed pattern survives near-neighbor hardware evidence. Context records cannot silently become direct L5 members.

## Required normalized fields

Electrical: Vin, Vout, Pout, fs, duty cycle, turns ratio, voltage gain.

Complexity: main active switches, auxiliary switches, diodes, capacitors, magnetic-core count, winding count.

Stress: measured main-switch stress, normalized main-switch stress, maximum diode stress, stress type (exact / approximate / bound).

Source/application: continuous-input-current flag, input-current ripple, common-ground flag, isolation.

Switching: per-device ZVS/ZCS/hard-switching map, diode reverse-recovery behavior where explicitly measured.

Performance/quality: efficiency operating point and boundary, auxiliary-power inclusion, cooling/thermal condition, measurement instruments/method, uncertainty if reported, power-density volume boundary if used.

## Search sources

- Existing repository BATCH-001/002/003 and evidence locators.
- Publisher / institutional lawful full text.
- Scholar/OpenAlex metadata search.
- Exa source-grounded search/fetch.
- Firecrawl research corpus for adversarial/counter-search.
- Backward/forward citation snowballing when identifiers are available.

A miss in one engine is never evidence of absence.

## Stopping rule

A Research Gap Candidate is not authorized until all are true:

1. The direct comparison fields are sufficiently locked for every record used in the claim.
2. At least two independent extraction/review judgments exist for claim-critical records, with disagreements logged and adjudicated.
3. Backward and forward citation snowballing has been performed for the core evidence families.
4. Counter-search has been run using at least two substantially different query families.
5. Marginal-yield/saturation evidence is recorded; a single zero-result query is insufficient.
6. Study-quality gates pass or unresolved limitations are explicitly incorporated into the claim.
7. The proposed recurring pattern survives falsification attempts.

## Comparison policy

Current mode remains BOUNDED_TRADEOFF.

Efficiency is descriptor-only unless operating point, auxiliary/thermal boundary and measurement basis align. Interval or upper-bound stress evidence must remain interval-valued. No overall-best topology claim is permitted.

## Research-gap policy

This audit may authorize a `RECURRING_BOUNDARY_CANDIDATE`. It may create a `RESEARCH_GAP_CANDIDATE` only if the stopping rule is satisfied. Neither label is equivalent to an established research gap.