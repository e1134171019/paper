# 07 — Benchmarks

Status date: 2026-08-19  
Purpose: define fair reference architectures before claiming improvement

## 1. Benchmark rule

Benchmark is not selected to make the candidate look better.

All comparisons must obey the declared boundary / operating-point / metric-definition contract and at minimum match or explicitly bound:

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
measurement basis
```

Unmatched peak efficiencies from different papers/products are not a ranking.

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

Direct net reconstruction of the user-supplied schematic now establishes a more specific structure than the earlier component-only abstraction:

```text
BAT+
├─ F2/F3/F5/F6 → local LV bulk → T1 center tap B
└─ F7/F8/F9/F10 → local LV bulk → T2 center tap B

T1 A = T2 A → shared paralleled low-MOS switching node
T1 C = T2 C → shared paralleled low-MOS switching node

T1/T2 HFT magnetic transformation                 ← X1
↓
T1/T2 secondary series/collective connection
↓
D1/D5 + D2/D6 HV rectifier bridge
↓
BUS+ / BUS- + HV DC-link                          ← passive X2-capable node
↓
post-bus HV inverter                              ← X3
↓
AC
```

Important correction:

```text
the visible four spatial groups of five MOS positions
are not four electrically independent converter branches.
```

The two transformer A ends share one switched drain node and the two C ends share the other.

Low-side MOS status:

```text
20 annotated positions total
19 expected power connections directly reconstructed
Q19 drain = schematic anomaly / requires PCB-BOM-assembly verification
```

A0 details and evidence boundary:

```text
research/10_ASP2000_PRODUCT_BASELINE.md
research/12_ASP2000_A0_POWER_PATH_AND_LOSS_BUDGET.md
```

A0 is used for real-product loss localization; it is not assumed inefficient.

### A1 — fair optimized magnetic benchmark

Any new architecture using early distribution / multicell must also beat a magnetic architecture allowed the same engineering freedom:

```text
12 V short / low-R bus
→ optimized current distribution
→ optimized switching + magnetic X1
→ collective HV formation / rectification
→ reduced-current node
→ X3
```

Forbidden comparison:

```text
new modular candidate
vs
artificially monolithic magnetic baseline
```

A1 answers:

> If the same layout, current-sharing and packaging improvements are applied to magnetic conversion, what candidate advantage remains?

### A-class loss map

```text
battery/source
→ common LV interconnect
→ fuse distribution
→ local LV bulk ESR/ripple
→ LV MOS conduction
→ LV MOS switching/Coss/gate/commutation
→ HFT primary copper/core
→ HFT secondary copper
→ leakage/clamp/snubber
→ HV rectifier
→ HV bus capacitor
→ HV inverter
→ output filter/interconnect
```

Required A0/A1 quantities:

```text
I_source,avg / RMS / 100-120Hz / HF
T1/T2 center-feed current
A-side / C-side switching-node current
fuse-path resistance/current
common LV Rdc/Rac
MOS conduction/switching loss
T1/T2 primary Rac + core loss
rectifier loss
HV DC-link ripple/capacitor RMS
HV inverter loss
```

If A0 already suppresses source 2ω strongly, active-X2 value must be reframed.

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

Relative to A0/A1 it avoids the complete conventional chain:

```text
HV rectifier → full HV DC bus → VSI
```

This is a required modern benchmark. A candidate that only improves on conventional two-stage conversion is insufficient.

Existing direct-HFL + AC-side power-decoupling prior art also means that keeping 2ω energy from fully returning to the LV source is not itself novel.

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

Required ablation:

```text
D0 — Buffer OFF
D1 — Buffer ON
```

Go condition:

```text
P_LV,saved > P_buffer,loss + P_extra,circulation
```

If electric-field conversion is used, it must similarly prove that removed magnetic/rectifier/LV loss exceeds capacitor/reactive/circulating/extra-switch loss.

---

## 6. Fair comparison matrix

```text
                    A0 ASP       A1 Opt HFT    B Direct HFL   C Non-iso HG   D Candidate
Vin                 matched      matched       matched         matched        matched
Pout                matched      matched       matched         matched        matched
Vout                matched      matched       matched         matched        matched
Isolation           explicit     explicit      explicit        explicit       explicit
I_common,RMS        measure/model model         model/report    model          measure/model
I_branch,RMS        measure/model model         model/report    model          measure/model
I_2ω                measure/model model         model/report    model          measure/model
I_circulating       measure/model model         model/report    model          measure/model
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

Core rule:

```text
P_saved > P_added
```
