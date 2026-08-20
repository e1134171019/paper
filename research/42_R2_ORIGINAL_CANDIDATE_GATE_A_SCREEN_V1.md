# 42 — R2 Independent Candidate Gate-A Screen v1

Status date: 2026-08-20  
Role: `R2 ORIGINAL-CANDIDATE GENERATION / IEEE GATE A / EARLY STOP CONTROL`  
Research boundary anchor: `12 Vdc / 2 kW / 220 Vac / 1φ`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

After File 41 reclassified the Wu-type active-clamp implementation as `R2-REF1`, this file starts independent R2 candidate generation from the **loss weakness**, not from copying a prior-art circuit and changing its values.

R2 remains:

```text
PM-1 magnetic transformation
+
PM-4 reactive-energy-assisted commutation
+
PM-7 AC synthesis
```

The candidate-generation question is now:

> Can PM-4 be implemented so that it does not create a large additional current-carrying path in the 12 V / hundred-ampere domain?

---

## 2. Weakness extracted from R2-REF1

R2-REF1 demonstrates a valid known solution:

```text
leakage energy
→ resonant transition
→ clamp capacitor
→ auxiliary switch path
→ energy returned to transformer / load
```

At the extreme-LV project boundary, the risk is not that this principle is wrong. The risk is that the auxiliary/clamp path may process enough current that:

```text
P_aux,cond
+ P_clamp-path,rms
+ P_circulation
+ P_added-interconnect
```

erases the removed:

```text
P_hard-switch
+ P_dissipative-snubber
+ P_unrecovered-leakage
```

Therefore the independent design target is:

```text
PM-4 should ideally exist only during commutation,
not as a sustained full-power auxiliary conduction path.
```

This target is a project design objective, not a novelty claim.

---

# 3. R2-C1 — branch-local modular active clamp

## 3.1 Concept

First independent attempt:

```text
12 V input
├─ local T1 push-pull module + local active clamp
└─ local T2 push-pull module + local active clamp

T1/T2 inputs in parallel
T1/T2 outputs in series
→ HV bus
```

The intent was to split commutation energy and current between two local transformer branches rather than one aggregated clamp path.

## 3.2 IEEE Gate-A result

This concept is **not worth deep simulation as a novelty path**.

Closest established directions include:

1. active-clamp / energy-recovery push-pull converters;
2. two-transformer current-fed isolated converters;
3. input-parallel/output-series modular DC/DC architectures.

Representative IEEE prior art includes:

- K. B. Park, G. W. Moon, M. J. Youn, "Two-Transformer Current-Fed Converter With a Simple Auxiliary Circuit for a Wide Duty Range," IEEE Transactions on Power Electronics, vol. 26, no. 7, 2011, DOI `10.1109/TPEL.2010.2094625`.
- B. Whitaker, D. Martin, E. Cilio, "Extending the operational limits of the push-pull converter with SiC devices and an active energy recovery clamp circuit," IEEE APEC 2015, DOI `10.1109/APEC.2015.7104628`.
- IEEE literature also contains input-parallel/output-series modular DC/DC control and architecture studies.

Formal Gate-A status:

```text
R2-C1
= CLOSE_PRIOR_ART
= STOP_AS_NOVELTY
= DO_NOT SPEND DEEP PSIM TIME
```

R2-C1 may remain only as a modular comparator idea if later useful.

This is an intentional early rejection and demonstrates the purpose of File 37.

---

# 4. R2-C2 — cross-commutation energy-shuttle concept

## 4.1 Design objective

R2-C2 changes the **commutation-energy route**, not merely the component values or number of active-clamp devices.

Working concept:

```text
Normal A power interval:
12 V → T1/T2 A-half primaries → Main-A → return

A→C transition:
outgoing A-side leakage / winding current
↓
short-duration bidirectional resonant shuttle path
↓
charge A-node effective Coss
+
discharge C-node effective Coss
↓
C body-diode conduction
↓
Main-C ZVS turn-on
↓
shuttle path OFF

Normal C power interval:
12 V → T1/T2 C-half primaries → Main-C → return
```

Then the reverse C→A transition is symmetric.

Critical intended distinction from R2-REF1:

```text
R2-REF1:
leakage energy → clamp storage → auxiliary path → transformer/load

R2-C2 target:
outgoing leakage energy → directly assists opposite-node commutation
→ no sustained clamp-energy-return interval in the normal power path
```

The auxiliary resonant branch is intended to conduct **only around dead time / transition**, not throughout the main power-transfer interval.

---

## 4.2 Functional graph boundary

R2-C2 preserves:

```text
T1/T2 center-tap magnetic X1
A/C main MOS banks
T1/T2 secondary series addition
HV rectifier
HV DC link
VSI
```

It changes only PM-4:

```text
A/C dissipative RC or stored-clamp return path
↓
short-duration cross-commutation resonant shuttle
```

Therefore this is still an R2 concept, not R6: no additional PM-2 boost stage is admitted.

---

## 4.3 First-order energy condition

The transition must satisfy:

```text
E_available,outgoing
>=
E_Coss,outgoing-charge
+ E_Coss,incoming-discharge
+ E_parasitic
+ E_margin
```

For nonlinear MOS output capacitance, final work must use:

```text
Eoss(V)
```

or integrated Qoss/Coss data rather than only `0.5 C V²`.

The intended gain relative to R2-REF1 is not more ZVS energy. It is:

```text
minimum commutation energy
+
minimum auxiliary RMS / conduction time
```

The central loss gate is:

```text
P_switching,saved + P_RC,saved
>
P_shuttle_cond + P_shuttle_sw + P_extra_circulation + P_added_parasitic
```

---

## 4.4 Initial IEEE Gate-A search

IEEE searches were run around:

```text
push-pull auxiliary resonant commutation
push-pull energy-recovery snubber
push-pull active energy recovery clamp
lossless snubber push-pull
auxiliary resonant commutated pole
cross-commutated / resonant ZVS push-pull
```

The search found established neighboring mechanisms:

- high-step-up push-pull series-resonant ZVS converters;
- active energy recovery clamp push-pull converters;
- passive/lossless snubbers for DC/DC converters;
- auxiliary resonant commutated pole (ARCP) inverters;
- ZVS full-bridge converters using controlled leakage inductance.

However, this first search did **not yet establish an IEEE paper with the exact complete R2-C2 graph** defined as:

```text
dual-HFT center-tap push-pull
+
common A/C main banks
+
transition-only cross-node commutation-energy shuttle
+
series secondary voltage addition
```

Formal status:

```text
R2-C2 Gate A
= POSSIBLY_DIFFERENTIATED_AT_GRAPH-CONCEPT_LEVEL

NOT:
= NOVEL
= CLEARED CANDIDATE
= READY FOR CLAIM
```

Prior-art risk remains HIGH because resonant snubber / ARCP / active-energy-recovery concepts are mature and may contain an equivalent state graph under different naming.

---

## 5. Hard Gate-A/B conditions before PSIM

Do NOT build a detailed loss model yet.

Next evidence required:

```text
A. draw the minimum R2-C2 node graph
B. enumerate A→C and C→A switching states
C. identify whether the auxiliary branch needs:
   - one bidirectional switch
   - two MOSFETs
   - one small Lr
   - one small Cr / DC-blocking capacitor
   - or can reuse controlled transformer leakage
D. prove there is no DC short / transformer flux-reset violation
E. search the exact state graph against IEEE
```

If an IEEE paper has the same graph/state sequence:

```text
R2-C2 → STOP_AS_NOVELTY / comparator only
```

If structurally different:

```text
R2-C2 → Gate B
```

Only after Gate B may PSIM P0 be authorized.

---

## 6. Current R2 board

| ID | Role | IEEE status | Action |
|---|---|---|---|
| R2-REF1 | Wu-type active-clamp push-pull | KNOWN PRIOR ART | benchmark only |
| R2-C1 | two local active-clamp modules / IPOS | CLOSE PRIOR ART | STOP as novelty |
| R2-C2 | transition-only cross-commutation energy shuttle | POSSIBLY DIFFERENTIATED | derive node/state graph + Gate B precheck |

No R2 item is currently authorized as Candidate #10.

---

## 7. Immediate NEXT

```text
R2-C2
↓
minimum electrical node graph
↓
state-by-state current path
↓
flux-reset / shoot-through check
↓
exact IEEE Gate A/B graph search
↓
ONLY IF SURVIVES:
PSIM P0
```

Hardware remains deferred.
