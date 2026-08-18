# 10 — ASP-2000 R52 Product Baseline

Status date: 2026-08-19  
Role: `A0 REAL-PRODUCT BENCHMARK`  
Evidence status: `DIRECT_SCHEMATIC_EXTRACTION / PARTIAL_CONNECTIVITY_RECONSTRUCTION`  
Novelty relevance: `NONE — benchmark evidence only`

## 1. Purpose

This document records the product-level reality check derived from the user-supplied ASP-2000 MAIN R52 Altium source artifacts.

Source artifacts used in this analysis:

```text
PB-2200-0038-D_ASP-2000-MAIN-R52.SchDoc
PB-2200-0038-D_ASP-2000-MAIN-R52.PcbDoc
```

The raw product files are **not committed to this repository**. This document stores only the research-relevant structural abstraction and explicitly separates verified extraction from inference.

The purpose is to prevent an unfair comparison in which a new candidate is credited for current sharing or modularization that the real product already uses.

---

## 2. Verified product-level findings

The schematic source directly exposes the following power-stage structure.

### 2.1 Two high-frequency magnetic transformation modules

```text
T1 = PQ5050
T2 = PQ5050
```

Therefore the real product is not represented accurately by a single monolithic low-voltage transformer abstraction.

### 2.2 Low-voltage switching is already strongly paralleled

The 12 V / 24 V low-side power stage contains 20 main MOSFET positions annotated:

```text
CSD18542KCS @12V
CSD19533KCS @24V
```

They are arranged around the two HFT modules as four local switch banks of five parallel devices:

```text
T1 region:
Bank A1 = Q3, Q4, Q5, Q6, Q33
Bank B1 = Q11, Q12, Q13, Q14, Q36

T2 region:
Bank A2 = Q18, Q19, Q20, Q21, Q37
Bank B2 = Q24, Q25, Q26, Q27, Q38
```

Research interpretation:

```text
one HFT module
← two local low-side switching banks
← five parallel MOS devices per bank
```

Do not interpret this as proof of an exact push-pull/current-fed/full-bridge operating mode until full net connectivity and switching timing are independently reconstructed.

### 2.3 Input current distribution hardware is already present

Eight input fuse positions are grouped around the two low-voltage power sections:

```text
F2, F3, F5, F6
F7, F8, F9, F10
```

with schematic annotations:

```text
40 A / 32 V @12V
20 A / 32 V @24V
```

This is direct product evidence that the low-voltage source current is not treated as a single-device current path.

### 2.4 Low-voltage local energy storage is already substantial

Ten low-voltage bulk-capacitor positions are annotated for the voltage variants:

```text
2700 uF / 25 V @12V
1500 uF / 35 V @24V
```

The schematic notes show two groups of five capacitors associated with the low-voltage power regions.

This supports the engineering interpretation:

```text
battery / common LV path
→ local bulk energy support
→ paralleled switching banks
→ HFT
```

It does **not** prove that all switching-frequency current is fully localized; that requires waveform and impedance measurement.

### 2.5 High-voltage rectification stage is explicit

The schematic contains four KSU60D60N high-voltage rectifier devices:

```text
D1, D2
D5, D6
```

Their placement separates naturally into the T1 and T2 conversion regions.

Therefore the product-level front end is consistent with the working family:

```text
#02 HFT + Rectifier + HV DC Bus + VSI
```

### 2.6 High-voltage energy node / DC-link is explicit

The schematic contains:

```text
C8, C11, C89, C90
= 680 uF / 315 V
```

and power-net labels including:

```text
BUS+
BUS-
VBUS-class internal naming
```

Research interpretation:

```text
HFT
→ HV rectification
→ HV energy-storage / DC-link region
```

This region is the product-level physical reference for the research coordinate `X2`, but the existing passive DC-link must **not** be confused with an active bidirectional 2ω buffer.

### 2.7 A distinct high-voltage AC-synthesis stage exists

The schematic contains a separate high-voltage switching region with designators:

```text
Q1, Q2, Q9, Q10,
Q31, Q32, Q34, Q35
```

and alternative device annotations for 110 V / 220 V variants:

```text
NGTB50N65FL2W @110V
IRG7PH35UDPBF @220V
```

The same region is associated with AC/output labels such as:

```text
ACL
ACN
ACL1
ACN1
```

This is sufficient to classify a distinct post-DC-link AC-synthesis stage as the product reference for `X3`.

Exact population/parallelization under each 110 V / 220 V production variant remains `NOT YET VERIFIED` without the matching BOM/variant configuration.

---

## 3. Product power-path abstraction

The verified source evidence supports the following A0 abstraction:

```text
Battery / LV input
        ↓
input fuses / common LV distribution
        ↓
local LV bulk capacitors
        ↓
parallel low-side MOS banks
        ↓
T1 + T2 PQ5050 HFT modules          ← X1 region
        ↓
D1/D2 + D5/D6 HV rectification
        ↓
HV DC-link / BUS+/BUS-              ← passive X2-capable energy node
        ↓
high-voltage inverter stage         ← X3
        ↓
output filtering / AC terminals
        ↓
AC output
```

Classification:

```text
A0 = #02 real-product benchmark
```

---

## 4. X1 / X2 / X3 mapping

### X1 — first major impedance transformation

Product reference:

```text
low-side MOS switching banks
→ T1 / T2 PQ5050
```

The HFT modules are the first clearly identified major voltage/current-domain transformation.

### X2 — local energy-storage / 2ω placement coordinate

Product reference:

```text
post-rectification HV DC-link / BUS region
```

Important distinction:

```text
existing passive DC-link ≠ proposed active bidirectional 2ω buffer
```

Whether an added active X2 produces net benefit remains a `HYPOTHESIS` and must pass Buffer OFF/ON loss comparison.

### X3 — AC synthesis

Product reference:

```text
post-BUS high-voltage inverter stage
```

Therefore the product already follows the structurally favorable ordering:

```text
X1 → HV energy node → X3
```

rather than synthesizing the complete low-frequency AC waveform in the 12 V hundred-ampere domain.

---

## 5. A0 loss map

The product benchmark must be decomposed at least as:

```text
Battery / source impedance
↓
Fuse + connector + common LV interconnect I²R
↓
LV bulk-capacitor ESR / ripple loss
↓
LV MOS-bank conduction
↓
LV MOS switching / Coss / gate-drive / commutation
↓
T1/T2 primary copper
↓
T1/T2 core
↓
T1/T2 secondary copper
↓
leakage / clamp / snubber / commutation
↓
D1/D2/D5/D6 rectifier conduction / recovery
↓
HV DC-link capacitor ESR / dielectric / ripple
↓
HV inverter conduction / switching
↓
output-filter copper / core / capacitor loss
↓
output interconnect / terminal
```

This is now the minimum real-product boundary for any claimed improvement.

---

## 6. Critical research correction caused by the product evidence

Previous candidate language emphasized:

```text
early distribute the hundred-ampere current
```

The real product proves that this principle already exists in A0.

Therefore the candidate **cannot** claim advantage merely because it uses:

```text
parallel MOS
multiple current paths
two or more power cells
early current sharing
modular HFT
```

A fair comparison must instead ask:

```text
Does the candidate reduce:
- common-path R_eq before X1?
- LV full-current physical exposure?
- MOS-bank I_RMS²R?
- HFT primary copper / magnetic loss?
- leakage / clamp / commutation loss?
- rectifier loss?
- 2ω component reflected to the LV source?

while keeping:
P_saved > P_added ?
```

---

## 7. Required matched magnetic benchmark

The magnetic baseline is now split into two levels.

### A0 — actual ASP-2000 R52 product abstraction

```text
real low-side parallel MOS banks
→ T1/T2 HFT
→ real rectifier stage
→ real HV DC-link
→ real HV inverter stage
```

Use A0 for measurement-grounded loss localization.

### A1 — optimized matched modular-HFT benchmark

A new candidate using N branches must also be compared against a fair magnetic architecture allowed to use the same current-distribution freedom:

```text
12 V short bus
→ N-way fan-out
→ N × [switching + HFT X1]
→ HV combine / rectification
→ HV node
→ X3
```

This prevents an invalid comparison of:

```text
new modular candidate
vs
artificially monolithic magnetic benchmark
```

---

## 8. Candidate architecture status after product reality check

Keep the current working architecture:

```text
12 V source
↓
very-short / very-low-R common path
↓
local bulk + HF decoupling
↓
early distributed branch power cells
↓
branch switching + X1
↓
reduced-current domain
↓
[X2 active 2ω buffer — optional / must prove benefit]
↓
X3
↓
220 Vac
```

Status by block:

```text
very-short common LV path      = KEEP / PHYSICAL REQUIREMENT
local decoupling               = KEEP / ENGINEERING REQUIREMENT
early current distribution     = KEEP AS HYPOTHESIS, not novelty
branch switching + X1          = CORE RESEARCH REGION
reduced-current node           = KEEP AS FUNCTIONAL CONCEPT
active X2 buffer               = OPTIONAL / NOT YET PROVEN
X3 after X1                    = KEEP / STRUCTURAL REQUIREMENT
```

The product evidence strengthens the need for a **matched** benchmark; it does not establish that the candidate is superior.

---

## 9. What remains unverified

Do not infer the following from the partial binary extraction:

```text
exact T1/T2 turns ratio
exact switching frequency
exact low-side modulation / bridge class
exact per-device current sharing
exact transformer primary / secondary RMS current
exact PCB copper Rdc/Rac
exact leakage inductance
exact clamp/snubber processed power
exact DC-link 100/120 Hz ripple
exact source 100/120 Hz current
exact 110 V / 220 V population variants
measured stage efficiencies
thermal distribution
```

These require source-net reconstruction, BOM/variant data, simulation, or hardware measurement.

---

## 10. Next A0 validation actions

Before claiming candidate benefit, obtain or model:

```text
1. I_source,avg / RMS / 2ω / HF ripple
2. each low-side MOS-bank current
3. T1 primary current
4. T2 primary current
5. R_common from battery/fuse/bus to switching banks
6. effective MOS-bank RDS(on) at operating temperature
7. T1/T2 copper + core loss
8. rectifier loss
9. HV DC-link ripple and capacitor RMS
10. HV inverter loss
```

The first candidate comparison should then use:

```text
A0 actual ASP product
A1 optimized matched modular HFT
B  non-isolated current-distribution / high-gain candidate
C  direct-HFL candidate
```

with identical declared comparison boundaries.

---

## 11. Formal status

```text
ASP-2000 R52 structural baseline = VERIFIED AT COMPONENT / STAGE LEVEL
full net-by-net reconstruction    = NOT YET COMPLETE
A0 benchmark                      = ESTABLISHED
candidate superiority             = NOT ESTABLISHED
active X2 benefit                 = NOT ESTABLISHED
novelty                           = NOT ESTABLISHED
```
