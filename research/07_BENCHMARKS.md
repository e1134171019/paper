# 07 — Benchmarks

Status date: 2026-08-19  
Purpose: define fair reference architectures before claiming improvement

## 1. Benchmark rule

Benchmark is not selected to make the candidate look better.

All comparisons must match or explicitly bound:

```text
Vin
Pout
Vout
power-flow direction
isolation requirement
load point
semiconductor technology class
switching-frequency scope
thermal boundary
auxiliary-loss policy
battery-interface protection/sensing functionality
measurement basis
```

Unmatched peak efficiencies from different papers/products are not a ranking.

Core rule:

```text
P_saved > P_added
```

Two comparison contracts are allowed:

```text
Contract P — product level
→ matched required battery-interface/protection/sensing functions and their loss counted

Contract C — core converter
→ battery-interface overhead excluded from A0/A1/candidate equally
```

Never delete A0 product functionality only on the candidate side and call the saved watts a topology gain.

---

## 2. Benchmark A — Magnetic HFT class

Working family:

```text
#02 High-Frequency Magnetic-Isolated Two-Stage
```

Generic path:

```text
LV DC
→ LV HF switching
→ HFT
→ HV rectification
→ HV DC bus
→ VSI
→ AC
```

### A0 — ASP-2000 R52 real-product baseline

Current SchDoc + compiled-PCB reconstruction establishes:

```text
BAT+
├─ F2/F3/F5/F6 → local LV bulk → T1 center tap
└─ F7/F8/F9/F10 → local LV bulk → T2 center tap

T1 A + T2 A → common A switched node → 10 parallel MOS → B
T1 C + T2 C → common C switched node → 10 parallel MOS → B

B
↓
7-MOS battery-interface protection/sensing bank
↓
BAT-

T1/T2 magnetic transformation                         ← X1
↓
secondary series / collective voltage formation
↓
D1/D5 + D2/D6 HV rectifier bridge
↓
BUS+ / BUS- + HV DC-link                              ← passive X2-capable node
↓
post-bus HV inverter                                  ← X3
↓
AC
```

Primary switches:

```text
A node = 10 connected main MOS
C node = 10 connected main MOS
common source/return = B
```

Q19 is verified in the compiled PCB; old `19 connected / Q19 OPEN` wording is superseded.

Gate structure:

```text
DA1 + DA2 → A power node
DB1 + DB2 → C power node

DR-A  ─ R213=0Ω ─ DR-A2
DR-B  ─ R212=0Ω ─ DR-B2
```

Thus:

```text
4 physical driver subgroups
2 logical switching functions
2 high-current switched nodes
```

Current variables:

```text
I_T1 / I_T2 = transformer feed currents
I_A,total / I_C,total = two electrical switch currents
I_DA1 / I_DA2 / I_DB1 / I_DB2 = local silicon-subgroup currents
```

Do not equate DA1/DA2 with T1/T2 currents.

#### A0 battery-interface function

Seven `CSD18510KCS` devices connect:

```text
Source → B
Drain  → BAT-
Gate   → common 12VP through individual 68.1Ω
Gate   → B through individual 47.5kΩ
```

No independent MAIN-board PWM/enable command was found for this bank.

Function status:

```text
low-side reverse-polarity / ideal-diode-style role = STRONGLY SUPPORTED
independent full-disconnect role = NOT SUPPORTED BY PRESENT CIRCUIT
```

U4 (`LM2904`) monitors `B` relative to `BAT-` and exports `BOCP` to CN4A pin 6:

```text
B↔BAT- voltage-drop sensing → BOCP = VERIFIED
BOCP over-current / abnormal-drop protection role = STRONGLY SUPPORTED
exact threshold / control response = OPEN
```

Therefore the seven-MOS loss is classified primarily as battery-interface protection/sensing overhead, not intrinsic magnetic-X1 loss.

A0 details:

```text
research/10_ASP2000_PRODUCT_BASELINE.md
research/12_ASP2000_A0_POWER_PATH_AND_LOSS_BUDGET.md
research/14_ASP2000_A0_DISTRIBUTION_AND_KELVIN_PLAN.md
research/16_ASP2000_A0_DYNAMIC_SWITCHING_AND_HFT_MEASUREMENT_PROTOCOL.md
research/17_ASP2000_A0_PRIMARY_SWITCH_CURRENT_BOUNDARY.md
research/18_ASP2000_A0_BATTERY_RETURN_PROTECTION_AND_BOCP.md
```

A0 is used for real-product loss localization; it is not assumed inefficient.

### A1 — fair optimized magnetic benchmark

A1 may use equivalent engineering freedom:

```text
12 V short / low-R bus
→ optimized current distribution
→ heavy parallel silicon
→ distributed local gate driving
→ optimized magnetic X1
→ collective HV formation / rectification
→ reduced-current node
→ X3
```

Under product-level Contract P, A1 must also provide matched required battery-interface functions, specifically as applicable:

```text
reverse-polarity / equivalent ideal-diode behavior
battery-return current/fault information equivalent to A0 requirement
fusing / fault isolation
```

Implementation does not need to copy A0. A lower-loss realization is allowed and should be counted as battery-interface engineering improvement.

Forbidden comparisons:

```text
candidate deletes battery protection/sensing
vs
A0/A1 carrying that product overhead
```

and:

```text
new modular candidate
vs
artificially monolithic / under-paralleled magnetic baseline
```

A1 answers:

> If the same distribution, silicon-paralleling, driver-distribution, packaging and matched-product-function freedom is applied to magnetic conversion, what candidate loss advantage remains?

### A-class loss map

```text
battery/source
→ BAT+ connector / common copper
→ fuse distribution
→ local T1/T2 feed + J8
→ local LV bulk ESR/ripple
→ A/C 10-MOS logical switch conduction
→ A/C switching/Coss/gate/commutation
→ T1/T2 primary copper/core
→ secondary copper
→ leakage/clamp/snubber
→ B return copper
→ battery-interface protection/sensing overhead
→ HV rectifier
→ HV bus capacitor
→ HV inverter
→ output filter/interconnect
```

Required A0/A1 quantities:

```text
I_source,avg / RMS / 100-120Hz / HF
I_T1 / I_T2
I_A,total / I_C,total
subgroup-current mismatch if material
fuse/J8 path loss
common LV Rdc/Rac
A/C MOS conduction/switching loss
battery-interface loss or equal-boundary exclusion
T1/T2 primary Rac + core loss
rectifier loss
HV DC-link ripple/capacitor RMS
HV inverter loss
```

If A0/A1 already suppress source 2ω strongly, active-X2 value must be reframed.

---

## 3. Benchmark B — Direct High-Frequency-Link DC–AC

Working family:

```text
#09 Direct High-Frequency-Link DC–AC
```

Typical path:

```text
LV DC
→ HF bridge
→ HFT / HF link
→ bidirectional matrix / cycloconverter
→ AC
```

Relative to A0/A1 it may avoid:

```text
HV rectifier → full HV DC bus → VSI
```

This is a required modern benchmark. Existing direct-HFL + AC-side power-decoupling prior art means keeping 2ω energy from fully returning to the LV source is not itself novel.

Under Contract P, its battery-interface functions/loss must still be matched or bounded.

---

## 4. Benchmark C — Non-Isolated Current-Distribution / High-Gain

Working family:

```text
#04 Non-Isolated High-Gain DC/DC + VSI
```

Fair extreme-LV form:

```text
12 V short bus
→ N-way current distribution
→ N × [switching + high-gain / coupled-L X1]
→ collective HV combine
→ HV node
→ X3
```

Compare:

```text
common-path R_eq
branch IRMS
MOS conduction/switching
inductor/coupled-inductor copper/core
leakage/clamp
rectifier/diode loss
capacitor ESR/charge redistribution
internal circulation
matched battery-interface protection/sensing loss
```

Direct 12 V / 2 kW / ~400 V hardware intersection remains not directly established by the current evidence set.

---

## 5. Candidate D — Working loss-routing architecture

```text
12–24 Vdc
→ very-short common LV path
→ local bulk + HF decoupling
→ early distributed branch power cells
→ branch switching + candidate X1
→ reduced-current domain
→ [optional active X2]
→ X3
→ 220 Vac / 1φ
```

Status:

```text
working architecture = KEEP
candidate superiority = NOT ASSUMED
active X2 = OPTIONAL / MUST PASS ABLATION
```

Required X2 ablation:

```text
D0 — Buffer OFF
D1 — Buffer ON
```

Go condition:

```text
P_LV,saved > P_buffer,loss + P_extra,circulation
```

If electric-field conversion is used, removed magnetic/rectifier/LV loss must exceed capacitor/reactive/circulating/extra-switch loss under matched functionality.

---

## 6. Fair comparison matrix

```text
                    A0 ASP       A1 Opt HFT    B Direct HFL   C Non-iso HG   D Candidate
Vin                 matched      matched       matched         matched        matched
Pout                matched      matched       matched         matched        matched
Vout                matched      matched       matched         matched        matched
Isolation           explicit     explicit      explicit        explicit       explicit
Battery interface   documented   matched       matched/bound   matched/bound  matched
I_common,RMS        measure/model model         model/report    model          measure/model
I_branch,RMS        measure/model model         model/report    model          measure/model
I_2ω                measure/model model         model/report    model          measure/model
I_circulating       measure/model model         model/report    model          measure/model
P_distribution      decomposed   decomposed    decomposed      decomposed     decomposed
P_batt-interface    separated    matched/excl. matched/excl.   matched/excl.  matched/excl.
P_cond              decomposed   decomposed    decomposed      decomposed     decomposed
P_sw                decomposed   decomposed    decomposed      decomposed     decomposed
P_mag               decomposed   decomposed    decomposed      decomposed     N/A/remaining
P_cap               decomposed   decomposed    decomposed      decomposed     decomposed
P_rectifier         decomposed   decomposed    as applicable   decomposed     as applicable
P_buffer            if present   if present    if present      if present     decomposed
P_total             same bound   same bound    same bound      same bound     same bound
```

If boundaries cannot be matched, evidence is `CONTEXT_ONLY` or `BOUNDED_TRADEOFF`, not a scalar ranking.

---

## 7. Current benchmark gate

A proposed topology must eventually survive:

```text
Candidate
vs A0 actual ASP
vs A1 fair optimized magnetic HFT
vs Direct HFL
vs matched non-isolated high-gain when applicable
```

Current order:

```text
A0 measured static + dynamic loss localization
↓
separate battery-interface overhead from intrinsic X1 loss
↓
A0 BAT→X1 Loss Budget v1
↓
A1 matched optimized magnetic model
↓
X1 mechanism comparison
↓
X2 ablation
↓
Candidate synthesis only if a physical gap survives
```