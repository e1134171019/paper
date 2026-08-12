# Habibi Vector Closure

Date: 2026-08-12
Record: `TSIR-HABIBI-2024`
DOI: `10.1109/TPEL.2023.3344719`

## Canonical source

Title: *An Impedance-Source-Based Soft-Switched High Step-Up DC-DC Converter With an Active Clamp*

Authors: Saeed Habibi, Ramin Rahimi, Mehdi Ferdowsi, Pourya Shamsi.

Primary-source route: legal/readable author-hosted IEEE paper at Missouri University of Science and Technology Scholars' Mine. The primary text identifies the same IEEE Transactions on Power Electronics article and DOI.

## Prototype boundary

- Vin = 20 V — reported experimental condition.
- Vout = 400 V — reported experimental condition.
- Pout = 200 W — reported rated experiment.
- fs = 50 kHz — reported experimental condition.
- coupled-inductor ratios: n21 = 0.5; n31 = 2.
- magnetizing inductance: 248 uH.
- exact experimental duty scalar: not text-locked in the recovered prose.

## Common component-count basis

`SCHEMATIC_DISCRETE_POWER_STAGE_V1`

- controlled switches = 2: S1 main + Sc active-clamp switch;
- discrete diodes = 3: D1, D2, Do;
- capacitors = 5: Cc, C1, C2, C3, Co;
- magnetic cores = 2: input inductor + one three-winding coupled inductor;
- total windings = 4: input-inductor winding + three coupled-inductor windings.

Intrinsic MOSFET body diodes are not counted as separate discrete diodes.

## Measured stress evidence

### Controlled switches

The experimental section text-locks the main-switch S1 stress as **almost 45 V** and experimentally demonstrates ZVS turn-on.

The clamp switch Sc is experimentally shown with a very low voltage stress and ZVS turn-on, but the recovered prose does **not** text-lock an exact Sc maximum voltage scalar.

Therefore:

- S1 measured stress ~= 45 V;
- Sc measured stress = unresolved exact scalar;
- measured maximum controlled-switch vector = unresolved.

The record must not use the S1 scalar alone as the maximum of a two-switch topology.

### Diodes

The experimental section provides diode voltage waveforms and states that their values agree closely with the steady-state analysis. No exact measured D1/D2/Do maximum voltage scalars were reproducibly text-locked in the recovered prose.

Therefore maximum measured diode stress remains `unresolved`.

## Recalculated/theoretical prototype vector

The paper gives the ideal gain relation:

`G = [1 + (1+n31-n21)(1+D)] / [(1-n21)(1-D)]`.

Using reported prototype values G = 400/20 = 20, n21 = 0.5 and n31 = 2 gives:

`D_recalculated = 0.52`.

This is a **recalculated** duty value, not a reported experimental duty scalar.

The paper gives both switch stresses as the clamp-capacitor voltage. At the recalculated prototype operating point:

- VS1(theory) = VSc(theory) ~= 41.67 V;
- normalized theoretical maximum controlled-switch stress ~= 41.67/400 = **0.1042**.

Using the paper's diode-stress equations at the same recalculated point:

- VD1(theory) ~= 208.33 V = 0.5208 Vout;
- VD2(theory) ~= 250 V = 0.625 Vout;
- VDo(theory) ~= 250 V = 0.625 Vout;
- normalized theoretical maximum diode stress = **0.625**.

These values are `theory_at_recalculated_prototype`. They are not converted into measured values.

## Other experimental evidence

- both controlled switches experimentally achieve ZVS turn-on;
- diode reverse-recovery loss is reported as minimized by controlled current fall rate;
- input-current ripple is qualitatively low; no measured ripple scalar is locked here;
- measured rated-power efficiency is approximately 94%.

## Admission decision

`evidence_level = L4_NUMERICALLY_VERIFIED`

`frontier_admission = CONTEXT_PENDING_MEASURED_VECTOR`

Reason: the theoretical/recalculated stress vector is now complete enough for bounded contextual comparison, but the exact **measured** Sc stress and maximum measured diode stress remain unresolved. The current node does not relax the controlled-switch-vector or measurement boundary merely because another L5 record uses theory-at-prototype evidence.

No L5 promotion is authorized in this node.

## Status

- theoretical stress vector: `CLOSED_WITH_RECALCULATED_DUTY`;
- measured controlled-switch vector: `INCOMPLETE`;
- measured maximum diode stress: `UNRESOLVED`;
- independent-family credit: `NOT_YET_ELIGIBLE`.
