# Direct-Scale Component Recount Basis v1

Date: 2026-08-12
Status: FROZEN_FOR_THIS_REVIEW

## Purpose

Provide one common component-count basis for the direct-scale high-gain Pareto study. Author comparison tables remain preserved as source claims, but raw integers from incompatible counting conventions are not used directly for cross-paper dominance.

## Frozen basis: `SCHEMATIC_DISCRETE_POWER_STAGE_V1`

Count intentional physical components shown or explicitly named as part of the conversion power stage:

- `controlled_switches_total`: all externally controlled semiconductor switches, including main, auxiliary and active-clamp switches.
- `discrete_diodes_total`: all intentional discrete diodes in conversion, clamp, multiplier, snubber or output paths.
- `capacitors_total`: all intentional conversion, clamp, multiplier, resonant, snubber and output capacitors. Measurement-only or external bench decoupling is excluded.
- `magnetic_cores_total`: distinct physical magnetic cores, not equivalent-circuit leakage/magnetizing inductances.
- `windings_total`: physical windings on discrete inductors, coupled inductors or built-in transformers. A one-winding discrete input inductor counts as one winding.

Intrinsic MOSFET body diodes are not counted as separate discrete diodes unless the source explicitly treats a separately packaged diode as a component.

## Author-count preservation

When a paper reports a comparison-table count using a different convention, preserve both:

- `author_reported_count`
- `schematic_discrete_count`

A mismatch is `COUNT_BASIS_DIFFERENCE`, not a source contradiction, unless the paper claims both numbers under the same stated basis.

## Recount results

| record | controlled switches | discrete diodes | capacitors | magnetic cores | windings | basis note |
|---|---:|---:|---:|---:|---:|---|
| PC-CAND-0024 | 1 | 4 | 5 | 2 | 3 | one input-inductor winding + two-winding coupled inductor |
| PC-CAND-0027 | 1 | 8 | 8 | 1 | 2 | one two-winding coupled-inductor core |
| PC-CAND-0028 | 1 | 4 | 5 | 2 | 4 | one input-inductor winding + three-winding coupled inductor |
| PC-CAND-0030 | 2 | 4 | 5 | 1 | 2 | main + active-clamp switch; one two-winding coupled inductor |
| B004-CAND-0002 | 2 | 3 | 5 | 2 | 3 | Cc/C1/C2/C3/Co; one input inductor + two-winding coupled inductor |
| B004-CAND-0003 | 1 | 7 | 6 | 1 | 4 | author comparison table reports C=5, while detailed topology additionally names snubber capacitor Cs; unified basis counts Cs |

## Source-specific notes

### PC-CAND-0024 — DOI 10.1049/iet-pel.2015.0923
Publisher text/Table 2 reports proposed topology `S=1`, `D=4`, `CL+L=2+1`, `C=5`. Prototype parameters list one separate input-inductor core and one two-winding coupled-inductor core. This supports 2 physical cores and 3 total windings.

### PC-CAND-0027 — DOI 10.1038/s41598-024-78739-y
Primary full text states one switch, eight diodes, eight capacitors and one coupled-inductor core. The paper itself explains that the larger diode/capacitor network contributes to gain and lower switch stress.

### PC-CAND-0028 — DOI 10.1038/s41598-025-17301-w
Primary full text states one input inductor, one three-winding coupled inductor, one switch, four diodes and five capacitors. Therefore physical magnetic burden is 2 cores / 4 windings.

### PC-CAND-0030 — DOI 10.1049/iet-pel.2015.0870
BATCH-004 publisher-fulltext structural closure remains authoritative: one main + one active-clamp switch, four diodes, five capacitors, one coupled-inductor core with two windings.

### B004-CAND-0002 — DOI 10.1049/pel2.70039
Primary topology text names S1/S2, D1/D2/Do, Cc/C1/C2/C3/Co, one separate input inductor and one two-winding coupled inductor. No additional capacitor is promoted without an explicit source locator. This supersedes the weaker prior phrase `7 including snubber capacitors` for unified-count use.

### B004-CAND-0003 — DOI 10.1155/etep/9317966
Author comparison table reports `S=1, D=7, C=5, MC/W=1/4`. Detailed topology separately names snubber capacitor `Cs` in addition to C1, C2, CO1, CO2 and CO3. Under `SCHEMATIC_DISCRETE_POWER_STAGE_V1`, capacitor count is therefore 6; source table value 5 remains preserved as `author_reported_count`.

## Guardrail

No Pareto dominance claim may compare component-count integers unless all participating records use this same frozen basis.