# Controlled-Switch Stress Vector Policy v1

Date: 2026-08-12

## Purpose
The direct-scale frontier previously carried a singular `main_switch_stress` field. That field is not sufficient when a topology contains more than one controlled semiconductor. A topology with one low-stress main MOSFET and one higher-stress auxiliary/synchronous MOSFET must not receive credit based only on the lower device.

## Frozen rule
For every topology, preserve the measured voltage-stress vector for all controlled switches in schematic identity order:

`controlled_switch_stress_vector_v = [VS1, VS2, ...]`

The scalar used for cross-topology semiconductor-stress screening is:

`max_controlled_switch_stress_v = max(vector)`

and, when the output-voltage boundary is compatible:

`normalized_max_controlled_switch_stress = max_controlled_switch_stress_v / Vout`

## Typed values
Each element and the derived maximum retain its evidence type:
- exact
- approx
- upper_bound
- range
- conflict
- unresolved

An upper bound must not be converted to an exact point. A conflict must not be averaged.

## Current impact
- Single-switch records are unchanged in substance because the vector has one member.
- PC-CAND-0030 is represented as `<90|<90`, not merely one `<90 V` main-switch value.
- DOI `10.1038/s41598-025-90093-1` is represented as `56|110 V`; its cross-topology maximum controlled-switch stress is therefore approximately 110 V, or 0.275 of the 400 V output.

## Guardrails
- Device voltage rating is not measured stress.
- Analytical stress is not substituted for measured stress in the measured frontier.
- Intrinsic MOSFET body diodes are not counted as separate controlled switches.
- Efficiency is not used to break stress ties unless its system/auxiliary/thermal measurement boundary is compatible.
