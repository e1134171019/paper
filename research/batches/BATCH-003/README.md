# BATCH-003 — High-Gain Comparison Expansion

Date: 2026-08-12
Status: comparison expansion audited
Parent set: `COMP-HG-001`
Contract: `research/contracts/power_converter_comparison_contract_v0.1.md`

## Purpose

Expand the first bounded L5 high-gain comparison set beyond two papers without relaxing the evidence contract.

The acquisition band remains non-isolated high-gain DC-DC hardware around:

- Vin: 20–40 V
- Vout: 380–400 V
- Pout: approximately 150–250 W
- measured semiconductor stress required for L5
- explicit soft-switching state required for L5
- efficiency operating point must be typed; unmatched auxiliary-loss boundaries prohibit a direct efficiency leaderboard

## Result

Four new journal papers were audited as `PC-CAND-0028` through `PC-CAND-0031`.

### New L5 promotions

- `PC-CAND-0028` — 25 V → 400 V, 250 W, 50 kHz, measured switch stress ≈55 V (0.1375 Vout), ZCS, measured full-load efficiency ≈96.4%.
- `PC-CAND-0030` — 40 V → 400 V, 200 W, 100 kHz, measured MOSFET stress <90 V (<0.225 Vout), ZVS, measured full-load efficiency 95.4%.

These join the existing L5 records `PC-CAND-0024` and `PC-CAND-0027`. `COMP-HG-001` therefore contains four L5 members from four distinct paper/author-group evidence families.

### L4/context holds

- `PC-CAND-0029` — 25 V → 400 V, 200 W, measured switch stress ≈50 V (0.125 Vout), ZCS, measured full-load efficiency 94.9%. Prototype switching frequency was not text-locked in this pass, so it remains L4/context and is not counted as an independent L5 expansion point.
- `PC-CAND-0031` — 40 V → 400 V, 200 W, 50 kHz, switch stress ≈100 V (0.25 Vout), ZVS, peak efficiency 97% at 80% load. Exact full-load efficiency was not text-locked, so it remains L4/context.

## Independence policy

Paper count is not treated as evidence-family count. Papers from the same or strongly overlapping author group are tagged with an `evidence_family` field. L5 expansion requires both paper-level reproducibility and adequate diversity of evidence families.

## Authorized comparison mode

`BOUNDED_TRADEOFF` only.

Authorized descriptors:

- Vin / Vout / measured gain
- Pout
- switching frequency when text-locked
- measured main-switch voltage stress or explicit upper bound
- normalized switch stress using measured Vout as denominator
- explicit ZVS / ZCS / No-soft-switching status
- efficiency only with its exact load condition

Prohibited:

- direct efficiency leaderboard across unmatched auxiliary-loss boundaries
- causal claim that soft switching alone caused an efficiency difference
- converting stress upper bounds into exact scalars
- overall-best-topology claims
- Research Gap claims

## Next formal node

`Repeated Trade-off Pattern Audit` on the four L5 members, with component-count / magnetic-count / active-switch-count normalization before any Research Gap candidate is considered.
