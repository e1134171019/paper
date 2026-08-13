# Habibi Vector Closure

Date: 2026-08-13
DOI: `10.1109/TPEL.2023.3344719`
Record: `TSIR-HABIBI-2024`

## Source and boundary

Legal/readable primary-source route: Missouri University of Science and Technology Scholars' Mine author-hosted copy identifying the definitive IEEE DOI.

Direct-scale hardware boundary is confirmed:
- Vin = 20 V;
- Vout = 400 V;
- Pout = 200 W;
- fs = 50 kHz;
- three-winding coupled inductor prototype: n21 = 0.5, n31 = 2, Lm = 248 uH.

Primary locators: Sec. III-B and III-D, Eqs. (7)-(9); Sec. VI, Fig. 11, Table III, Fig. 12, Fig. 14.

## Common component-count basis

Under `SCHEMATIC_DISCRETE_POWER_STAGE_V1`:
- controlled switches = 2 (`S1`, active-clamp `Sc`);
- discrete diodes = 3 (`D1`, `D2`, `Do`);
- capacitors = 5 (`Cc`, `C1`, `C2`, `C3`, `Co`);
- magnetic structures / cores = 2 (input inductor + three-winding coupled inductor);
- total windings = 4 (input inductor winding + three coupled-inductor windings).

## Controlled-switch stress closure

Experimental text locks the main switch `S1` at almost 45 V. Therefore:

`measured S1 normalized stress ~= 45/400 = 0.1125`.

The recovered experimental prose describes `Sc` as similarly very low stress and confirms ZVS, but it does **not** text-lock an exact measured `Sc` scalar. Therefore the complete **measured** controlled-switch vector remains incomplete.

The paper's analytical model states:

`VS1 = VSc = VCc`

and Eq. (8) gives:

`VS1/Vo = VSc/Vo = (1-n21) / [1 + (1+n31-n21)(1+D)]`.

Using the prototype turns ratios and solving the ideal gain equation (7) for G = 20 gives recalculated `D ~= 0.52`. At that operating point:

- theoretical `VS1/Vo = VSc/Vo ~= 0.1042`;
- theoretical `VS1 = VSc ~= 41.7 V`.

These are retained as `theory_at_prototype / recalculated duty`, not measured values.

## Diode-stress closure

Eq. (9) gives the normalized theoretical diode stresses. With n21 = 0.5, n31 = 2 and recalculated D ~= 0.52:

- `D1 ~= 0.5208 Vout ~= 208.3 V`;
- `D2 ~= 0.625 Vout = 250 V`;
- `Do ~= 0.625 Vout = 250 V`.

Thus the theoretical maximum diode stress at the prototype point is `0.625 Vout`.

Fig. 12(g) contains experimental diode-voltage waveforms, but the recovered primary prose does not text-lock an exact maximum measured diode scalar. The theoretical vector is therefore **not** relabeled as measured.

## Soft switching / ripple / efficiency

- `S1`: ZVS turn-on experimentally verified.
- `Sc`: ZVS turn-on experimentally verified.
- diode reverse-recovery burden is reduced through leakage-inductance-controlled current fall rate.
- input-current ripple: qualitatively low; no measured scalar locked.
- measured rated-power efficiency: approximately 94%.

## Evidence decision

`L4_NUMERICALLY_VERIFIED / DIRECT_VECTOR_THEORY_CLOSED_MEASURED_VECTOR_INCOMPLETE`

No L5 promotion is authorized in this node because the exact measured `Sc` scalar and exact measured maximum diode scalar remain unresolved. Under the maximum-controlled-switch-vector policy, a measured `S1` value alone cannot be used as the record's measured maximum controlled-switch stress.

Potential independent family remains `HABIBI_RAHIMI_IMPEDANCE_ACTIVE_CLAMP`, but independent L5 family credit remains `NOT_YET_ELIGIBLE` until L5 admission.