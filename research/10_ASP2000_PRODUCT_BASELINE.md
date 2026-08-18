# 10 — ASP-2000 R52 Product Baseline

Status date: 2026-08-19  
Role: `A0 REAL-PRODUCT BENCHMARK`  
Evidence status: `DIRECT_SCHEMATIC_NET_RECONSTRUCTION / PCB-R NOT YET QUANTIFIED`  
Novelty relevance: `NONE — benchmark evidence only`

## 1. Purpose

This document records the product-level baseline derived from the user-supplied ASP-2000 MAIN R52 Altium source artifacts:

```text
PB-2200-0038-D_ASP-2000-MAIN-R52.SchDoc
PB-2200-0038-D_ASP-2000-MAIN-R52.PcbDoc
```

The raw company/product files are **not committed to this public repository**.

A0 exists to prevent unfair comparison. Any candidate must be compared with the real product structure rather than a simplified fictional single-transformer / single-switch path.

Detailed pin/net reconstruction and the first loss-budget gate are in:

```text
research/12_ASP2000_A0_POWER_PATH_AND_LOSS_BUDGET.md
```

---

## 2. Verified low-voltage power structure

### 2.1 Two PQ5050 HFT modules

```text
T1 = PQ5050
T2 = PQ5050
```

Both transformer primary symbols expose:

```text
pin 9 = A
pin 8 = B
pin 7 = C
```

with `B` used as the separately supplied center-tap node.

### 2.2 BAT+ is split into two four-fuse center-tap feeds

Direct net reconstruction establishes:

```text
BAT+
├─ F2 / F3 / F5 / F6 ─→ T1 pin B + local LV bulk
└─ F7 / F8 / F9 / F10 → T2 pin B + local LV bulk
```

Main fuse annotation:

```text
40 A / 32 V @12 V
20 A / 32 V @24 V
```

`F15 = 0603L020YR` is an auxiliary/sense-path polyfuse and is not a main high-current fuse.

`F1 = 2 A / 300 V` is also outside the main BAT+ four-fuse banks.

### 2.3 Local LV bulk exists at both transformer feeds

T1 feed includes visible capacitor positions:

```text
C2 C3 C4 C5 C6
+ C97 C98 C99 auxiliary/optional positions
```

T2 feed includes:

```text
C28 C29 C30 C31 C32
```

Main LV capacitor annotation includes:

```text
2700 uF / 25 V @12 V
1500 uF / 35 V @24 V
```

The annotation contains population shorthand that must not be converted into an exact assembly count without BOM/variant data.

### 2.4 T1/T2 primary ends share the switching nodes

Important correction to the earlier component-level abstraction:

```text
T1 A = T2 A = shared A-side switched drain net
T1 C = T2 C = shared C-side switched drain net
```

Therefore the four spatial groups of MOS positions are **not four electrically independent five-MOS converter branches**.

C-side shared node directly contains ten MOS positions:

```text
Q11 Q12 Q13 Q14 Q36
Q24 Q25 Q26 Q27 Q38
```

A-side shared node directly reconstructs nine expected connected positions:

```text
Q3 Q4 Q5 Q6 Q33
Q18 Q20 Q21 Q37
```

`Q19` is annotated as the same low-side MOS type but its drain appears isolated in the extracted SchDoc graph.

Status:

```text
20 low-side MOS positions annotated
19 expected power connections directly reconstructed
Q19 drain = SCHEMATIC_ANOMALY / VERIFY PCB-BOM-ASSEMBLY
```

### 2.5 Low-side MOS device variants

Schematic annotation:

```text
CSD18542KCS @12 V
CSD19533KCS @24 V
```

The product clearly uses heavy semiconductor paralleling, but exact current sharing and hot effective RDS(on) remain measurement/model quantities.

### 2.6 Operating-mode wording

The graph verifies:

```text
separately fed center-tapped primaries
+ shared A/C low-side switched nodes
```

This is consistent with push-pull-like operation.

However:

```text
exact gate timing / duty / dead time / modulation = NOT YET VERIFIED
```

So `push-pull-like` remains an inference rather than a fully verified operating-mode label.

---

## 3. Verified X1-to-HV connectivity

### 3.1 The two secondaries include a direct series junction

Direct reconstruction establishes:

```text
T1 pin 5 ── T2 pin 2
```

The outer secondary nodes feed two rectifier legs:

```text
T1 pin 2 → D1/D5 AC-side leg
T2 pin 5 → RL1 path → D2/D6 AC-side leg
```

The exact control/configuration purpose of `RL1` remains open.

### 3.2 HV rectifier bridge

Verified:

```text
D1 pin 2 → BUS+
D2 pin 2 → BUS+
D5 pin 1 → BUS-
D6 pin 1 → BUS-
```

Thus:

```text
D1/D5 = one rectifier leg
D2/D6 = the other rectifier leg
```

### 3.3 HV DC-link / energy node

Four capacitor positions are annotated:

```text
C8 C11 C89 C90
= 680 uF / 315 V
```

and are located in the `BUS+ / BUS-` HV energy-storage region.

The symbols use four terminals; exact footprint-terminal semantics and series/parallel assembly must be checked before claiming an exact capacitor topology.

Safe conclusion:

```text
HV DC-link region = VERIFIED
exact capacitor assembly topology = NOT YET VERIFIED
```

### 3.4 X3 exists after the HV bus

A distinct high-voltage switching region is connected to the BUS and AC/output nets.

Relevant designators include:

```text
Q1 Q2 Q9 Q10
Q31 Q32 Q34 Q35
```

with variant annotations:

```text
NGTB50N65FL2W @110 V
IRG7PH35UDPBF @220 V
```

This remains the product reference for `X3`.

---

## 4. Revised A0 power-path abstraction

```text
BAT+
│
├─ 4× fuse bank → local bulk → T1 center tap B ─┐
│                                               │
└─ 4× fuse bank → local bulk → T2 center tap B ─┤
                                                │
T1/T2 A ends ─→ shared paralleled MOS node ─────┤
T1/T2 C ends ─→ shared paralleled MOS node ─────┤
                                                ↓
                                      common LV return
                                                │
                                     T1 + T2 HFT         ← X1
                                                ↓
                              series/collective secondary path
                                                ↓
                                    D1/D5 + D2/D6
                                                ↓
                                         BUS+ / BUS-
                                                ↓
                                      HV DC-link region  ← passive X2-capable node
                                                ↓
                                      HV inverter        ← X3
                                                ↓
                                             AC
```

Classification:

```text
A0 = #02 real-product magnetic HFT benchmark
```

---

## 5. X1 / X2 / X3 mapping

### X1

```text
low-side switched center-tapped T1/T2 magnetic transformation region
```

The MOS devices enable HF excitation; the major impedance/current-domain transformation is magnetic.

### X2 reference

```text
post-rectification HV DC-link / BUS region
```

Important:

```text
existing passive DC-link ≠ proposed active bidirectional 2ω buffer
```

### X3

```text
post-BUS high-voltage inverter / AC-synthesis region
```

A0 therefore already follows:

```text
X1 → HV/reduced-current energy node → X3
```

---

## 6. A0 loss map

Minimum decomposition:

```text
battery/source impedance
→ BAT+ common interconnect
→ 2 × four-fuse banks
→ local LV interconnect + bulk ESR/ripple
→ A/C MOS-bank conduction
→ MOS switching / Coss / gate / commutation
→ T1/T2 primary copper
→ T1/T2 core
→ T1/T2 secondary copper
→ leakage / clamp / snubber
→ D1/D2/D5/D6 rectifier
→ HV DC-link ESR/dielectric/ripple
→ HV inverter
→ output filter / terminal
```

The first formal quantitative gate is now `BAT+ → X1` loss localization; see `research/12_ASP2000_A0_POWER_PATH_AND_LOSS_BUDGET.md`.

---

## 7. Critical research consequences

The real A0 already contains:

```text
parallel low-side MOS
multiple HFT magnetic paths
separate fused current feeds
local LV energy support
collective/series secondary voltage formation
HV DC-link before X3
```

Therefore none of the following can be credited as candidate novelty or automatic loss advantage:

```text
parallel MOS
multiple current paths
multiple transformers
current sharing
early distribution
secondary voltage combination
HV bus before AC synthesis
```

A candidate must instead demonstrate a matched benefit in quantities such as:

```text
R_common before X1
I_common,RMS
MOS-bank I_RMS²R
switching / commutation loss
primary copper/core loss
leakage/clamp loss
rectifier loss
source 2ω RMS
P_total
```

under the rule:

```text
P_saved > P_added
```

---

## 8. Required magnetic comparison

### A0 — actual product

Use this reconstructed ASP-2000 structure for measurement-grounded loss localization.

### A1 — fair optimized magnetic architecture

A new candidate using N branches must also beat an HFT architecture allowed to use equivalent current-distribution freedom:

```text
12 V short bus
→ optimized distribution
→ switching + magnetic X1
→ collective HV formation / rectification
→ reduced-current node
→ X3
```

Do not compare a new modular candidate with an artificially monolithic HFT baseline.

---

## 9. What remains unverified

```text
Q19 intended/assembled drain connection
exact T1/T2 turns ratio
exact switching frequency / timing / duty
exact T1/T2 current balance
exact fuse current sharing
exact MOS current sharing
PCB copper Rdc/Rac
transformer winding Rac / core loss
leakage/clamp processed power
RL1 operating role
exact four-terminal HV capacitor implementation
source 100/120 Hz current
HV DC-link ripple
110 V / 220 V BOM population
stage efficiencies / thermal map
```

---

## 10. Formal status

```text
ASP A0 main power graph            = SUBSTANTIALLY RECONSTRUCTED
center-tap/fuse grouping           = VERIFIED
shared A/C switching nodes         = VERIFIED
secondary series/rectifier graph   = VERIFIED
A0 numerical BAT→X1 loss budget    = OPEN
PCB resistance extraction          = OPEN
A0 benchmark                       = ESTABLISHED
candidate superiority              = NOT ESTABLISHED
active X2 benefit                  = NOT ESTABLISHED
novelty                            = NOT ESTABLISHED
```
