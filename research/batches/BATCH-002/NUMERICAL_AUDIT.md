# BATCH-002 Numerical Audit + Comparison Contract Re-evaluation

Date: 2026-08-12
Status: audit complete; comparison re-evaluation complete
Contract: `research/contracts/power_converter_comparison_contract_v0.1.md`

## Result

This pass converts targeted acquisition records into explicit evidence states and re-runs the five comparison-set gates.

No record is promoted to `L5_COMPARISON_READY` in this pass.

This is intentional. The audit found several strong L4 candidates, but each comparison set still has at least one unresolved hard gate required by the comparison contract.

## Evidence promotions

Promoted to `L4_NUMERICALLY_VERIFIED`:

- `PC-CAND-0014` — 22-kW FB/PP series partial-power converter.
- `PC-CAND-0015` — 15-kW bidirectional HBPP partial-power system.
- `PC-CAND-0017` — 1.1-kW SUDPPC context paper; below primary COMP-PP power band.
- `PC-CAND-0023` — 195-W 20-V to 400-V hybrid quadrupler boost.
- `PC-CAND-0024` — 200-W 25-V to 400-V quasi-resonant high-step-up converter.
- `PC-CAND-0027` — 200-W 24-V to 400-V CISC high-step-up converter.

Held at `L3_EXPERIMENT_LOCATED`:

- `PC-CAND-0018` — exact eta/current curve points and switch-level ZVS remain to be extracted.
- `PC-CAND-0019` — exact DAB operating table and matched eta/RMS/ZVS points remain to be locked.
- `PC-CAND-0020` — OSTI confirms the experiment, but the accepted-manuscript retrieval timed out, so exact full-text locators and boundary definitions remain blocked.
- `PC-CAND-0021` — same-platform DAB-vs-CLLC experiment is strong, but exact efficiency curve points and final volume boundary remain pending.
- `PC-CAND-0022` — two-stage hardware is verified, but DCX-stage and total-system efficiency still require explicit separation at matched points.

Held below L3/L4:

- `PC-CAND-0016` — full experimental locators were not fully locked in this pass; retained as near-band evidence.
- `PC-CAND-0025` — legal/readable full text unresolved.
- `PC-CAND-0026` — legal/readable full text unresolved.

## Strongest new quantitative result: Partial Power

`PC-CAND-0014` provides a clean within-paper relation between processed-power fraction and measured system efficiency.

For the high-current operating points in Table 4:

| Vin | Vout | Iout | Recalculated Pconv/Pout | Measured system efficiency |
|---:|---:|---:|---:|---:|
| 180 V | 220 V | 100 A | 18.18% | 97% |
| 222 V | 220 V | 99 A | 0.91% | 99% |
| 244 V | 220 V | 100 A | 10.91% | 97% |
| 255 V | 220 V | 100 A | 15.91% | 96% |

The paper separately gives a design/rating value `Pconv/Ptotal = 1/5`. That 20% value is not assigned to all operating points.

`PC-CAND-0015` provides an independent 15-kW partial-power system with measured `Kp = 0.08 / 0.06 / 0.06` at three battery-voltage points and system efficiency above 99%, but exact system-efficiency scalars at those same Kp rows must still be extracted before L5.

## Strongest new quantitative result: High Gain

Two papers are now unusually close electrically:

| Candidate | Vin → Vout | Pout | fs | Full-load efficiency | Switch stress | Soft switching |
|---|---|---:|---:|---:|---:|---|
| `PC-CAND-0024` | 25 → 400 V | 200 W | 88 kHz | 96.4% | measured `<100 V`, normalized `<0.25` | main-switch ZCS turn-on |
| `PC-CAND-0027` | 24 → 400 V | 200 W | 50 kHz | 94.53% | measured ~62 V, normalized 0.155 | `No` per paper Table 1 |

This is sufficient to describe a bounded trade-off, but not sufficient for a flat leaderboard because:

1. `PC-CAND-0024` supplies only a measured stress upper bound, not an exact scalar.
2. Auxiliary-loss inclusion is not matched.
3. Switching frequency differs and must remain a covariate.

`PC-CAND-0023` is also L4 at 20 → 400 V / 195 W / 50 kHz, with ~97% peak efficiency and ~94.5% full-load efficiency, but its 100-V stress value is simulation-derived and is therefore not promoted as measured stress.

## Comparison-set re-evaluation

### COMP-HG-001

Status: `NEAR_L5_BLOCKED`

The set now has multiple independent L4 papers inside the electrical acquisition band. Remaining blockers are exact measured stress coverage and auxiliary-loss matching. No L5 promotion.

### COMP-PP-001

Status: `NEAR_L5_BLOCKED`

The 22-kW paper now provides same-point processed-power ratio + system-efficiency evidence. The 15-kW independent comparator still needs exact system-efficiency scalars at the reported Kp operating points and explicit auxiliary-loss treatment. No L5 promotion.

### COMP-DAB-001

Status: `BLOCKED`

The new 1-kW DAB papers strengthen hardware coverage, but target comparison metrics remain below L4 because exact eta/RMS/ZVS points have not been fully extracted.

### COMP-DCX-001

Status: `BLOCKED`

The 15-kW / 500-kHz CLLC paper is directly relevant, but exact accepted-manuscript locators and volume/auxiliary boundaries were not recovered in this pass. The 10.9-kW same-platform DAB-vs-CLLC paper is valuable context but operates below the declared 300–600-kHz direct-comparison band.

### COMP-OBC-PPP-001

Status: `BLOCKED_FULLTEXT`

The two primary OBC-PPC candidates still fail the legal/readable-fulltext hard gate.

## L5 count

`L5_COMPARISON_READY = 0`

This is a contract result, not a search failure and not a Research Gap.

## Exact next-stage targets

The next acquisition/extraction pass should be narrowly scoped to the remaining hard gates:

1. `COMP-HG-001`: obtain an exact measured switch-stress scalar on a comparator matched to `PC-CAND-0027`, and lock auxiliary-loss inclusion for the two full-load efficiency measurements.
2. `COMP-PP-001`: extract exact `PC-CAND-0015` system-efficiency values at the same rows as `Kp`, plus auxiliary-supply inclusion.
3. `COMP-DAB-001`: extract numeric eta/current points from `PC-CAND-0018` Figs. 24–26 and exact switch-level ZVS coverage; fully lock `PC-CAND-0019` prototype parameters.
4. `COMP-DCX-001`: resolve/retrieve `PC-CAND-0020` accepted manuscript and lock the converter-cell voltage, efficiency figure, power-density volume definition, and auxiliary-loss boundary.
5. `COMP-OBC-PPP-001`: resolve legal/readable full text before any numeric work.

No Research Gap claim is authorized by this audit.