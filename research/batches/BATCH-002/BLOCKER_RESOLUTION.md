# BATCH-002 Targeted Blocker Resolution

Date: 2026-08-12
Status: targeted blocker-resolution complete
Scope: `COMP-HG-001` and `COMP-PP-001`
Contract: `research/contracts/power_converter_comparison_contract_v0.1.md`
Upstream audit: `research/batches/BATCH-002/NUMERICAL_AUDIT.md`

## Result

This pass resolves only the two comparison sets that were closest to L5 after the BATCH-002 numerical audit.

The result is intentionally asymmetric:

- `COMP-HG-001` reaches **L5_COMPARISON_READY in BOUNDED_TRADEOFF mode** for `PC-CAND-0024` and `PC-CAND-0027`.
- `COMP-PP-001` remains **NEAR_L5_BLOCKED**.

No `DIRECT_QUANTITATIVE` efficiency leaderboard is authorized by this pass.
No Research Gap claim is authorized by this pass.

## 1. First L5 set: COMP-HG-001

### Admitted records

| Candidate | Vin → Vout | Pout | fs | Full-load efficiency descriptor | Measured main-switch stress | Normalized stress | Soft switching |
|---|---|---:|---:|---:|---:|---:|---|
| `PC-CAND-0024` | 25 → 400 V | 200 W | 88 kHz | 96.4% | `<100 V` | `<0.25` | main-switch ZCS turn-on |
| `PC-CAND-0027` | 24 → 400 V | 200 W | 50 kHz | 94.53% | ~62 V | 0.155 | `No` per paper comparison table |

The two records are independent journal papers and are already `L4_NUMERICALLY_VERIFIED`.
Their electrical scales are sufficiently close for a bounded mechanism/trade-off comparison: nearly identical output voltage and output power, closely matched low-voltage input class, and a common normalization denominator `Vswitch / Vout`.

### Why L5 is permitted

The comparison contract allows `BOUNDED_TRADEOFF` when structured differences are retained rather than collapsed into a scalar ranking.

For this set:

1. `metric_gate`: pass for bounded descriptors — measured gain, measured/bounded normalized switch stress, verified soft-switching category, and full-load efficiency descriptors are separately typed.
2. `boundary_gate`: pass — both are non-isolated high-gain DC-DC power stages and stress uses the same measured output-voltage denominator.
3. `condition_gate`: pass with covariate — switching frequency differs (88 kHz vs 50 kHz) and remains explicit; it is not normalized away.
4. `measurement_gate`: pass with bound awareness — `PC-CAND-0024` is an upper bound `<100 V` / `<0.25`, not an invented exact scalar; `PC-CAND-0027` has an exact measured ~62 V / 0.155 value.
5. `auxiliary_gate`: pass only under the contract's no-ranking exception — auxiliary-loss inclusion is not matched, therefore efficiency is retained as a descriptor and **direct efficiency ranking is prohibited**.

### Authorized observations

The L5 set authorizes statements of this form:

- both papers are comparison-ready for a structured high-gain trade-off at approximately 200 W and 400 V output;
- `PC-CAND-0024` experimentally demonstrates main-switch ZCS turn-on at 88 kHz;
- `PC-CAND-0027` reports an exact measured main-switch stress of about 62 V, normalized to 0.155 of measured 400 V output, and its comparison table classifies the proposed topology as having no soft switching;
- `PC-CAND-0024` only establishes the measured stress bound `<100 V`, normalized `<0.25`;
- full-load efficiency descriptors may be carried alongside the comparison but not ranked as an apples-to-apples efficiency result because auxiliary-loss boundaries are not matched.

### Prohibited inferences

The following remain invalid:

- `PC-CAND-0024 is better because 96.4% > 94.53%`;
- `PC-CAND-0027 definitely has lower switch stress than PC-CAND-0024` — an upper bound `<0.25` does not establish the unknown exact value relative to 0.155;
- treating 88 kHz and 50 kHz as equivalent switching conditions;
- converting this two-paper trade-off into a general Research Gap claim;
- using `L5_COMPARISON_READY` as a synonym for `best topology`.

## 2. Partial Power remains blocked

`COMP-PP-001` does not receive an L5 promotion in this pass.

### Evidence already strong enough

`PC-CAND-0014` provides same-operating-point processed-power fraction and measured system efficiency for a 22-kW FB/PP S-PPC. The high-current points already locked are:

| Vin | Vout | Iout | Pconv/Pout | measured system efficiency |
|---:|---:|---:|---:|---:|
| 180 V | 220 V | 100 A | 18.18% | 97% |
| 222 V | 220 V | 99 A | 0.91% | 99% |
| 244 V | 220 V | 100 A | 10.91% | 97% |
| 255 V | 220 V | 100 A | 15.91% | 96% |

The separate `20%` value is a converter design/rating fraction (`4.4 kW / 22 kW`) and is not assigned to every efficiency point.

`PC-CAND-0015` independently provides a 15-kW HBPP system with reported `Kp = 0.08 / 0.06 / 0.06` at three battery-voltage operating points and measured system-efficiency curves above approximately 99%.

### Remaining hard gate

The current readable evidence does not provide a text-locked/tabulated **system-efficiency scalar at the exact same rows as each `Kp` value** for `PC-CAND-0015`.
Its peak system-efficiency statement must therefore not be paired automatically with one of the Table-3 `Kp` points.

The auxiliary/gate-drive power inclusion of the measured system-efficiency boundary also remains unresolved for this comparator.

An older 5-kW series-PPP flyback record (`PC-CAND-0004`) confirms that auxiliary-drive boundary can materially differ: its hardware uses isolated gate-drive supplies powered from an external +5-V source, while system efficiency is measured at the main dc-grid/battery terminals. Its reported 99.12% charging and 99.08% discharging peak values occur at 550 V / 2 A and must not be substituted for a rated/full-load point.

### Exact next action for COMP-PP-001

Before L5:

1. obtain a reproducible scalar extraction from `PC-CAND-0015` Figure 19/20 or a tabulated source that pairs `eta_system` with the same operating rows as `Kp = 0.08 / 0.06 / 0.06`;
2. record charge/discharge direction explicitly for each paired point;
3. resolve whether gate-drive/control auxiliary consumption is inside or outside the reported system-efficiency boundary;
4. only then normalize against `PC-CAND-0014` without mixing peak, full-load, or direction-specific values.

## 3. L5 count after this pass

`L5_COMPARISON_READY = 2 records`

Authorized set:

- `COMP-HG-001 / PC-CAND-0024`
- `COMP-HG-001 / PC-CAND-0027`

Authorization mode: `BOUNDED_TRADEOFF` only.

## 4. Research-gap guard

This result establishes the first comparison-ready pair; it does not establish a Research Gap.

A later gap-analysis stage must first add enough independent comparison-ready evidence to determine whether an observed trade-off is repeated, contradictory, scale-limited, condition-limited, or topology-family-specific.
