# Li / He / Luo 2023 Full-Vector Audit

Date: 2026-08-12
DOI: `10.1007/s43236-022-00564-1`

## Canonical identity

- title: *Quadratic-type high step-up DC–DC converter with continuous input current integrating coupled inductor and voltage multiplier for renewable energy applications*;
- journal: Journal of Power Electronics;
- volume/issue/pages: 23(4), 555–567;
- authors: Fuwei Li, Jie He, Peng Luo, Haoyu Jiang, Mingxin Liu;
- publication year: 2023; online publication 2 December 2022;
- readable source: public author-uploaded full-text article record; DOI/bibliography cross-checked against Journal of Power Electronics/KCI metadata.

## Structural vector

Source locators: Section 1/2, Fig. 2–4, Table 1.

- direction: forward step-up;
- isolation: non-isolated;
- topology: quadratic boost + coupled inductor + voltage multiplier / shared passive clamp;
- controlled switches: `1`;
- discrete diodes: `6` (`D1`–`D6`);
- capacitors: `5` (`C1`, `C2`, `C3`, `C4`, `Co`);
- magnetic burden: `1 standalone input inductor + 1 two-winding coupled-inductor core`;
- magnetic cores total: `2`;
- winding count basis: `1 standalone winding + Np + Ns = 3`;
- author-reported component count: `14` under Table 1 basis;
- control: one switch / one control circuit;
- clamp: shares components with the second boost stage and voltage multiplier; no added controlled switch for the clamp;
- CCM operating modes: `4`;
- input current: continuous;
- common ground: yes; the paper states all Table 1 converters have common ground between load and source;
- verified target-paper soft switching: `NOT_REPORTED`.

`NOT_REPORTED` is not converted to `hard switching`.

## Prototype boundary

Source locator: Table 2 and Section 5.

- `Vin = 20 V`;
- `Vout = 400 V`;
- rated `Pout = 200 W`;
- `fs = 50 kHz`;
- power switch: `220N25NF`;
- `L1 = 29 uH`, core PQ3225;
- coupled inductor `Lm = 196 uH`, `Lk = 3 uH`, core PQ3535;
- turns ratio `Np:Ns = 14:14`, therefore `n = 1`;
- `C1, Co = 220 uF`;
- `C2, C3 = 22 uF`;
- `C4 = 47 uF`;
- `D1,D2 = MBR20100CT`;
- `D3 = MBR20300CT`;
- `D4,D5,D6 = MUR160`.

## Voltage-stress evidence

### Controlled switch

Source locator: Section 5.1, Fig. 10.

The article text explicitly reports the measured switch voltage under rated conditions:

`Vds_measured = 117 V`

At the declared `Vout = 400 V` boundary:

`normalized measured switch stress = 117 / 400 = 0.2925`.

Evidence type:

`recalculated_from_measured`.

Because this is a single-switch topology:

`controlled_switch_stress_vector_v = [117]`.

### Diodes

Source locator: Eqs. 16–20 and Figs. 11–14.

Theoretical reverse-voltage equations are explicitly given for all six diodes. At the prototype gain boundary `M = 400/20 = 20`, `n = 1`, Eq. 14 gives the physically valid duty ratio:

`D ≈ 0.5868956`.

Recalculated theory vector at that boundary:

- `VD1 ≈ 68.78 V`;
- `VD2 ≈ 48.41 V`;
- `VD3 ≈ 117.20 V`;
- `VD4 ≈ 234.39 V`;
- `VD5 ≈ 117.20 V`;
- `VD6 ≈ 234.39 V`.

Thus:

`theoretical max diode stress ≈ 234.39 V ≈ 0.5860 Vout`.

Evidence type:

`theory_at_recalculated_prototype`.

The article states the experimental diode currents and diode voltages agree with the theoretical analysis, and Figs. 11–14 contain the diode-voltage waveforms. However, the readable text/captions do not lock an exact measured peak scalar for every diode. The PDF binary endpoint could not be fetched for screenshot inspection in this environment.

Therefore:

`measured maximum diode stress = unresolved`.

The theory value is not substituted for the missing measured scalar.

## Efficiency boundary

Source locator: Section 5.2, Fig. 16–17.

- measured load range: `20–200 W`;
- maximum efficiency: `about 95.2% at 80 W`;
- full-load efficiency: `93.7% at 200 W`;
- diode losses: `42%` of the analyzed total losses at full load;
- switch losses: `15%`, the lowest reported category;
- the paper explicitly notes an `else` category representing losses not included in its loss analysis.

Consequences:

- peak and full-load efficiency are kept separate;
- no flat efficiency ranking is authorized;
- auxiliary/control/thermal measurement boundaries are not sufficiently harmonized across the frontier.

## Internal boundary inconsistency

Section 5 reports the design boundary:

`Vin = 20 V, Vout = 400 V, Io = 0.2 A, n = 1`.

Table 2 independently reports rated output power `Pout = 200 W` at `Vout = 400 V`.

These values do not simultaneously describe the same full-load power point because `400 V × 0.2 A = 80 W`.

Status:

`INTERNAL_CURRENT_POWER_BOUNDARY_INCONSISTENCY`.

This node does not silently replace `0.2 A` with a recalculated current. The inconsistency is isolated to that reported design/calculation sentence. The measured efficiency section separately defines the tested load sweep as 20–200 W and explicitly calls 200 W full load.

## Evidence-level adjudication

The record satisfies L4 because the prototype boundary and claim-critical numerical evidence have full-text locators.

It also satisfies the current direct-scale bounded-tradeoff L5 gate because:

1. it is a journal hardware prototype in the direct inclusion window;
2. `20 -> 400 V / 200 W / 50 kHz` is source-locked;
3. a measured semiconductor-stress locator exists (`Vds = 117 V` at rated conditions);
4. controlled-switch stress is typed and normalized to the same output boundary;
5. component/magnetic/input-current/common-ground fields are explicit;
6. peak and full-load efficiency semantics are separated;
7. the `Io = 0.2 A` inconsistency is excluded from comparison-defining full-load claims rather than repaired;
8. the comparison is `BOUNDED_TRADEOFF`, not an efficiency leaderboard.

Final target status:

`L5_COMPARISON_READY / BOUNDED_MEMBER`

Remaining target-specific limitations:

- exact topology-wide measured diode peak scalar unresolved;
- no verified target-paper ZVS/ZCS claim;
- auxiliary/cooling/thermal efficiency boundary unresolved;
- reported `Io = 0.2 A` design sentence conflicts with the rated 200 W / 400 V boundary.
