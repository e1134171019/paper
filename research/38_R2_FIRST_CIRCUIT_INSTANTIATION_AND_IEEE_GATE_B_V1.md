# 38 — R2 First Circuit Instantiation + IEEE Gate-B Precheck v1

Status date: 2026-08-20  
Role: `R2 ACTUAL-GRAPH DEVELOPMENT / THEORETICAL COMPARATOR / IEEE PRIOR-ART GATE B`  
Research boundary anchor: `12 Vdc / 2 kW / 220 Vac / 1φ`  
Evidence class: `THEORETICAL / PRIOR-ART-GROUNDED / NOT SIMULATED / NOT MEASURED`  
Topology-candidate authorization: `NOT GRANTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

This file begins actual circuit composition for the first retained mechanism combination from File 36:

```text
R2 = PM-1 + PM-4 + PM-7
```

The purpose is **not** to claim a new topology. IEEE prior art already establishes active-clamped / resonant / ZVS push-pull isolated converters. R2 is therefore developed first as a strong, loss-fair magnetic comparator that changes the commutation mechanism while preserving the basic low-voltage magnetic energy path.

This file is subordinate to:

```text
research/37_IEEE_PRIOR_ART_GATE_AND_NOVELTY_CONTROL_V1.md
```

and opens IEEE Gate B for the actual graph.

---

## 2. Why the first R2 graph stays push-pull

A generic ZVS phase-shift full bridge is mature and must remain a comparator, but at the 12 V / ~175 A source-current scale it normally places two LV bridge devices in the instantaneous main conduction path.

For this project, every extra full-current LV series resistance is expensive:

```text
ΔP = I_rms² × ΔR
```

At the existing 95%-reference source-current scale:

```text
I_source ≈ 175.44 A
```

therefore an extra series path of:

```text
0.1 mΩ → ~3.08 W
0.5 mΩ → ~15.39 W
1.0 mΩ → ~30.78 W
```

For the first R2 comparator, preserve the push-pull property that only one logical main LV switch function carries each energized half-primary interval, then add PM-4 around commutation rather than replacing the entire LV bridge.

This is a theoretical architecture-selection reason, not yet a proof that push-pull beats PSFB.

---

## 3. R2-G1 system graph

Working identifier:

```text
R2-G1 = dual-HFT push-pull
      + active energy-recovery / ZVS clamp overlay
      + series secondary HV rectification
      + HV DC link
      + VSI AC synthesis
```

Majority-power graph:

```text
12 V source
  ↓
LV bulk / low-impedance distribution
  ↓
T1 + T2 center-tap feeds in parallel at input
  ↓
A/C push-pull primary switching
  ↓
PM-1 magnetic flux-linkage transformation
  ↓
T1/T2 secondary voltages connected in series
  ↓
HV rectifier
  ↓
HV DC link
  ↓
PM-7 HV VSI / full bridge
  ↓
LC output filter
  ↓
220 Vac / 1φ / 2 kW
```

PM-4 is an overlay on the A/C commutation region:

```text
transformer leakage inductance Llk
+ MOSFET output capacitance Coss
+ intentional resonant/snubber capacitance Cr where required
+ active clamp capacitor Cclamp
+ auxiliary clamp switch(es)
+ controlled dead time

→ resonant node transition
→ leakage-energy recovery instead of resistive dissipation
→ ZVS target for main/auxiliary switches
```

The exact auxiliary-switch / clamp-capacitor polarity and node orientation MUST be locked from the selected IEEE reference circuit before a SPICE/PSIM netlist is declared authoritative. This file does not invent a clamp orientation from memory.

---

## 4. A0-preserving electrical boundary

The first R2-G1 graph intentionally preserves the verified A0 high-current abstraction:

```text
T1 center feed ─→ T1 half-primary A ─┐
                                     ├→ common A switched node → main A MOS bank → B
T2 center feed ─→ T2 half-primary A ─┘

T1 center feed ─→ T1 half-primary C ─┐
                                     ├→ common C switched node → main C MOS bank → B
T2 center feed ─→ T2 half-primary C ─┘
```

Therefore:

```text
2 logical main LV switch functions
= A bank + C bank
```

The purpose of R2-G1 is to test:

```text
A0 dissipative commutation / RC damping
versus
R2-G1 recoverable / resonant commutation
```

without simultaneously adding PM-2 boost transfer or PM-3 voltage stacking.

---

## 5. Static voltage-ratio target

For 220 Vac:

```text
Vout,pk = 220 × sqrt(2) = 311.13 V
```

A practical HV-link target requires margin above this value. For theoretical screening only, evaluate:

| HV-link target | total effective 12V→HV factor | equal T1/T2 secondary contribution proxy |
|---:|---:|---:|
| 325 V | 27.08× | 13.54× per transformer |
| 340 V | 28.33× | 14.17× per transformer |
| 350 V | 29.17× | 14.58× per transformer |
| 380 V | 31.67× | 15.83× per transformer |
| 400 V | 33.33× | 16.67× per transformer |

The last column is **not yet a literal turns ratio**. It is only the equal-secondary voltage-contribution proxy for two series secondaries. Actual `Ns/Np_half` depends on applied primary waveform, duty, rectifier/capacitor behavior, regulation margin and losses.

The first simulation should therefore sweep HV-link target rather than prematurely freeze the transformer turns ratio.

---

## 6. PM-4 admission condition

A first-order energy condition for completing a ZVS-like capacitive transition is:

```text
0.5 L_comm I_comm² >= 0.5 C_eq V_sw²
```

or:

```text
I_comm,min >= V_sw × sqrt(C_eq / L_comm)
```

But R2-G1 is retained only if total loss improves:

```text
P_hard-switch + P_RC/snubber + P_unrecovered-leakage
>
P_aux-cond + P_aux-sw + P_clamp-cap + P_added-circulation
+ P_residual-switch + P_control-added
```

ZVS by itself is not success.

---

## 7. R2-G1 loss ledger

The simulation / theoretical ledger must separately report:

```text
P_mainMOS_cond
P_mainMOS_sw
P_auxMOS_cond
P_auxMOS_sw
P_transformer_primaryCu
P_transformer_secondaryCu
P_transformer_core
P_clamp_cap_ESR/dielectric
P_resonant_or_leakage_circulation
P_rectifier
P_HVlink
P_VSI_cond
P_VSI_sw
P_output_filter
P_gate/control_added
P_other
```

Causal tags against A0:

```text
A0 R110/R119 resistive damping
→ target tag = REMOVED or STRONGLY_REDUCED

leakage energy
→ target tag = RECOVERED / RELOCATED, not automatically REMOVED

auxiliary clamp switch conduction
→ INTRINSIC_NEW

clamp-cap ESR
→ INTRINSIC_NEW

extra resonant/circulating RMS
→ INTERACTION_NEW
```

The combination fails if local switching-loss reduction is outweighed by these new losses.

---

## 8. First parameter set to sweep — do not freeze parts yet

### System

```text
Vin = 12 V nominal
Pout = 2 kW
Vout = 220 Vac / 50 or 60 Hz
Vdc target sweep = 325 / 340 / 350 / 380 / 400 V
```

### X1 / switching

```text
fs = sweep, not fixed
main-bank R_eq(T) = parameter
Llk,eq = parameter
Lm = parameter
Coss,eq(V) = parameter
Cr,ext = parameter / zero allowed
Cclamp = parameter
aux-switch Rds(on)(T) = parameter
dead time = parameter
```

### Required outputs

```text
I_source,avg/rms
I_A,rms / I_C,rms
I_primary,rms / peak
V_A-B / V_C-B stress
main and auxiliary ZVS margin
transformer flux / volt-second balance
secondary RMS current
HV-link regulation / ripple
Pout / THD context
full loss ledger
```

---

## 9. IEEE Gate-B precheck

### Closest established IEEE prior art

1. Wu et al., **An Active-Clamp Push–Pull Converter for Battery Sourcing Applications**, IEEE Transactions on Industry Applications, 44(1), 196–204, 2008. DOI `10.1109/TIA.2007.912748`.
   - push-pull battery-source application
   - auxiliary switches + resonant/leakage inductance + clamp capacitors
   - leakage-energy recovery
   - main and auxiliary ZVS
   - 1 kW prototype

2. Whitaker et al., **Extending the operational limits of the push-pull converter with SiC devices and an active energy recovery clamp circuit**, IEEE APEC 2015.
   - push-pull + active energy-recovery clamp is independently established in IEEE prior art.

3. IEEE push-pull / HFL literature also establishes soft-switched push-pull and current-fed push-pull variants; current-fed variants belong closer to R6 because PM-2 becomes a main transfer mechanism.

### Preliminary Gate-B decision

```text
basic active-clamped push-pull cell
= SAME / KNOWN SUBGRAPH

A0-derived dual-HFT common-A/C primary structure
+ equal secondary-series voltage build
+ active clamp overlay
+ HV-link/VSI system boundary
= NEAR_GRAPH pending exact graph-to-graph closure
```

Therefore:

```text
R2-G1 topology novelty = NOT ESTABLISHED
R2-G1 may continue as comparator / loss-falsification vehicle
```

A future claim cannot be:

```text
"we invented active-clamped push-pull ZVS"
```

The only permissible research value at this stage is quantitative:

```text
Does this known PM-4 solution remain net-beneficial
at the project's extreme 12 V / 2 kW / ~175 A boundary
when every new conduction and interaction loss is counted?
```

---

## 10. Comparison branch retained

For fairness, R2 must eventually include at least two implementations:

```text
R2-G1 = push-pull + active energy-recovery/ZVS clamp
R2-G2 = ZVS phase-shift full bridge (PSFB)
```

Reason:

```text
R2-G1 minimizes LV series-device count
R2-G2 is a mature high-power soft-switching magnetic benchmark
```

A single chosen R2 implementation is not enough to conclude PM-1+PM-4 is good or bad.

---

## 11. Immediate NEXT

```text
1. Lock the exact IEEE R2-G1 clamp cell schematic/orientation.
2. Translate R2-G1 into an explicit node/branch netlist.
3. Run IEEE Gate B on that exact graph.
4. Build ideal-switch PSIM Student model first.
5. Add nonideal R_eq / Llk / Coss / clamp losses progressively.
6. Sweep fs × Llk × C_eq × deadtime × Vdc target.
7. Compare R2-G1 against A0-like hard-switched push-pull under the same transformer / semiconductor / cooling contract.
8. Only after the total-loss result, decide whether R2 survives as the strongest magnetic comparator.
```

No topology-candidate or novelty promotion is authorized by this file.
