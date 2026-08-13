# Targeted Stopping Test

Date: 2026-08-13

Broad keyword expansion remains stopped. The frozen boundary is nonisolated/unidirectional high-step-up hardware, Vin about 20-50 V, Vout about 380-400 V, and Pout about 150-300 W.

## Habibi and Jazi closure yield

Habibi DOI `10.1109/TPEL.2023.3344719` remains L4 because the exact measured clamp-switch scalar and measured maximum diode scalar remain unresolved.

Jazi DOI `10.1109/ACCESS.2025.3573936` is confirmed at 40 V -> 400 V / 200 W / 100 kHz with the structure and experimental features audited, but its auxiliary-switch operational-voltage scalar and maximum measured diode scalar remain unresolved. It remains L4 and receives no additional independent-family credit.

New L5 yield from these two closures: 0.

## Narrow stopping-check yield

A narrow different-author check surfaced a 2026 experimental record:

- Salehi / Varjani;
- DOI `10.1038/s41598-026-40326-8`;
- Scientific Reports 16, 9763 (2026).

The primary article confirms laboratory hardware at 24 V -> 400 V, two active switches and two diodes. It text-locks an experimentally shown active-switch voltage of 62 V, D1 reverse voltage of 200 V, D2 reverse voltage of 300 V, ZCS behavior, and measured efficiency of 96.6% at full load.

The exact rated/full-load output power in watts was not reproducibly text-locked in the current retrieval. Therefore this paper is registered only as `L3_EXPERIMENT_LOCATED / TARGETED_POWER_BOUNDARY_UNRESOLVED` and is not admitted to the direct-scale set.

## Marginal-yield and stopping decision

Confirmed new L5 records: 0.
Confirmed new independent L5 families: 0.
New different-author 24 V -> 400 V unresolved-power candidate: 1.

Marginal yield: `POSITIVE_UNRESOLVED`.

Stopping decision: `TARGETED_SEARCH_SATURATION_NOT_MET`.

The remaining stopping action is narrow: close the rated/full-load Pout of DOI `10.1038/s41598-026-40326-8`. If it is outside 150-300 W, demote it to context and rerun the stopping test. If it lies inside 150-300 W, complete its component and controlled-switch-vector audit. Do not return to broad keyword searching.