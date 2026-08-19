# 30 — Canonical L3 Physical-Mechanism Dictionary v1

Status date: 2026-08-19  
Role: `RESEARCH ONTOLOGY NORMALIZATION / PHYSICAL-GAP VALIDATION`  
Research object: `PM-R1...PM-R13 → CANONICAL L3 PHYSICAL MECHANISMS`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

本文件承接：

```text
research/28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md
research/29_NINE_FAMILY_X1_X2_X3_NORMALIZATION.md
```

將九類架構中抽出的 `PM-R1...PM-R13` raw items 去重、拆除支援功能、分離複合結構，建立可供後續 `PG × Physical Mechanism` 比較的正式 L3 dictionary。

本輪仍然：

```text
NOT topology synthesis
NOT Candidate #10 creation
NOT novelty claim
NOT PG compatibility execution
```

核心規則維持：

```text
Architecture ≠ Strategy ≠ Physical Mechanism ≠ Resulting Property
P_saved > P_added
```

---

## 2. L3 admission rule

一個項目只有在回答下列問題時，才可成為 canonical L3 mechanism：

> 實際靠哪一個可辨識的物理能量轉移、儲存、換流或波形合成過程完成此功能？

Admission gates：

```text
L3-G1 — independent of topology / product label
L3-G2 — describes a physical process, not only a system strategy
L3-G3 — identifiable from circuit graph and/or waveforms
L3-G4 — has separable loss / stress terms
L3-G5 — can recur across more than one architecture where physically applicable
L3-G6 — is not merely a resulting waveform/property
```

Therefore the following are NOT canonical L3 mechanisms by themselves：

```text
early X1
fan-out
interleaving
single-stage
remove HV bus
continuous-input current
lower ripple
high gain
DAB
LLC
switched-capacitor family label
```

They are strategies, architecture labels, properties, or implementation families until decomposed into a physical process.

---

## 3. Canonical mechanism classes

The v1 dictionary contains **7 canonical L3 mechanism classes**.

```text
PM-1 — Magnetic Flux-Linkage Transformation
PM-2 — Inductive Energy Transfer
PM-3 — Capacitive Charge-Transfer / Voltage-Stacking
PM-4 — Reactive-Energy-Assisted Commutation
PM-5 — Capacitive Field-Energy Buffering
PM-6 — Controlled Bidirectional Storage-Port Transfer
PM-7 — Semiconductor Switching-State AC Synthesis
```

Important：

```text
7 canonical mechanisms ≠ 7 topology families
```

A real converter may use several PM classes simultaneously.

---

## 4. PM-1 — Magnetic Flux-Linkage Transformation

### Physical definition

> 利用共享磁通耦合，在一次側與二次側之間傳遞主要功率，並以匝比建立不同電壓／電流域。

Physical basis：

```text
Faraday induction
mutual flux linkage
turns-ratio transformation
```

Typical coordinate：

```text
X1
```

Typical manifestations：

```text
line-frequency transformer
high-frequency transformer
isolated HF-link transformer
```

Raw sources：

```text
PM-R1 → KEEP / CANONICALIZED AS PM-1
```

Important boundary：

```text
transformer label ≠ PM-1 by itself
PM-1 is the flux-linkage / turns-ratio transfer process
```

Main loss signature：

```text
winding I²R / Rac
core hysteresis + eddy loss
leakage-related burden
magnetizing / reactive current where material
```

Families containing PM-1：

```text
#01
#02
#03
#09
#04 when a coupled-inductor cell includes transformer-like mutual-flux action
```

---

## 5. PM-2 — Inductive Energy Transfer

### Physical definition

> 利用電感磁場能量 `E_L = 1/2 L I²` 的建立、釋放或差動電壓驅動，完成主要功率傳遞或電壓轉換。

Canonical variants：

### PM-2A — switched accumulation / release

```text
inductor charges during one switching state
→ stored magnetic-field energy changes
→ energy is released / redirected during another state
```

Typical examples：

```text
boost
buck-boost
many high-gain inductor cells
```

### PM-2B — differential / phase-shift inductive transfer

```text
voltage difference across series/leakage inductance
→ controlled di/dt
→ active power transfer between switching bridges / ports
```

Typical examples：

```text
DAB leakage / external series-L power transfer
active-HFT phase-shift transfer
```

Raw sources：

```text
PM-R2 → PM-2A
PM-R6 → PM-2B
```

Decision：

```text
PM-R2 and PM-R6 are NOT two unrelated mechanism classes.
They are two transfer-law variants of the same inductive-field-energy mechanism class.
```

Typical coordinate：

```text
X1
sometimes X2 active-buffer transfer implementation
```

Main loss signature：

```text
inductor copper/core
RMS / ripple / peak current
circulating current
switch conduction associated with energy-transfer states
commutation loss if not separately handled by PM-4
```

Families containing PM-2：

```text
#03
#04
#06
#07
#05 depending on bidirectional DC/DC implementation
```

---

## 6. PM-3 — Capacitive Charge-Transfer / Voltage-Stacking

### Physical definition

> 利用切換狀態改變電容之連接關係，使電荷在電容、source 與 load 之間重新分配，藉此建立 voltage lift、stacking 或 multiplication。

This is not the same as simply storing low-frequency energy in a DC-link capacitor.

Physical process：

```text
charge transfer
charge redistribution
series/parallel reconnection
voltage stacking / multiplication
```

Raw source：

```text
PM-R4 → KEEP / CANONICALIZED AS PM-3
```

Typical coordinate：

```text
X1
may overlap X3 in switched-capacitor / multilevel direct-AC architectures
```

Main loss signature：

```text
charge-redistribution loss
capacitor ESR / dielectric loss
large capacitor RMS current
switch conduction / switching
balancing / precharge burden
```

Families containing PM-3：

```text
#04 voltage-multiplier / voltage-lift variants
#08 switched-capacitor gain paths
```

Important boundary：

```text
PM-3 ≠ PM-5

PM-3 = intentional charge transfer / voltage building
PM-5 = energy storage / release for power pulsation buffering
```

---

## 7. PM-4 — Reactive-Energy-Assisted Commutation

### Physical definition

> 利用已儲存在 L/C 或 leakage / resonant network 中的反應性能量，主動塑造 switch transition，使開關在低電壓或低電流條件下換流，或降低需要耗散的 Coss / leakage / overlap energy。

Typical manifestations：

```text
ZVS
ZCS
resonant commutation
quasi-resonant transition
leakage-energy-assisted switching
```

Raw source：

```text
PM-R7 → KEEP / CANONICALIZED AS PM-4
```

Typical coordinate：

```text
overlay on X1 or X3 switching region
```

Important ontology rule：

```text
PM-4 is an overlay mechanism.
It does not define the main architecture by itself.
```

Example：

```text
PM-1 magnetic transformation + PM-4 ZVS commutation
PM-2 inductive transfer + PM-4 resonant transition
```

Main loss signature：

```text
resonant / circulating RMS
reactive component loss
residual hard-switching loss
Coss / Qg / gate-drive burden
control/dead-time sensitivity
```

Families containing PM-4：

```text
#02 selected resonant / soft-switched variants
#03 active-HFT / DAB variants
#09 selected resonant direct-HFL variants when actually implemented
```

---

## 8. PM-5 — Capacitive Field-Energy Buffering

### Physical definition

> 利用電容電場能量 `E_C = 1/2 C V²` 的可逆變化吸收與釋放低頻功率脈動，而不是利用切換電容做 voltage multiplication。

Raw source：

```text
PM-R8 passive capacitive 2ω buffering
→ generalized / canonicalized as PM-5
```

Typical coordinate：

```text
X2
```

Typical manifestations：

```text
HV DC-link bulk capacitor carrying 2ω energy swing
AC-side / differential passive buffer capacitor
```

Important boundary：

```text
having a capacitor ≠ PM-5
```

PM-5 exists only when the capacitor actually carries the declared energy swing.

Main loss signature：

```text
capacitor ESR
ripple-current heating
dielectric loss
voltage-ripple / stored-energy requirement
volume / lifetime burden
```

Families where PM-5 may appear：

```text
#02
#04
#05
#09
and any architecture containing an intentional 2ω storage capacitor
```

---

## 9. PM-6 — Controlled Bidirectional Storage-Port Transfer

### Physical definition

> 利用主動 switching network 在 main power path 與一個真正的 energy-storage port 之間控制雙向能量交換，使 storage port 能按指令吸收或釋放能量。

Raw source：

```text
PM-R9 → KEEP / CANONICALIZED AS PM-6
```

Typical coordinate：

```text
X2
sometimes overlapping X1 or X3 physically
```

Important boundary：

```text
bidirectional capability alone ≠ PM-6
```

There must be：

```text
actual storage port
+
controlled charge/discharge power exchange
```

A DAB that only transfers average power between two DC buses is not automatically X2 / PM-6.

Implementation may internally use：

```text
PM-2 inductive transfer
PM-4 soft commutation
PM-5 capacitive storage
```

Therefore PM-6 describes the controlled storage-port energy-exchange process, while its internal converter physics must still be counted separately.

Main loss signature：

```text
extra switch conduction/switching
buffer inductor/capacitor loss
gate/control/sensing
circulating RMS
storage-port conversion loss
```

Families where PM-6 may appear：

```text
#05
#09 with active decoupling
#02/#04 if an active post-X1 buffer is added
```

---

## 10. PM-7 — Semiconductor Switching-State AC Synthesis

### Physical definition

> 利用可控半導體 switching states 選擇輸出端的 polarity、voltage level、source/link connection 或 amplitude-time state，形成要求的單相 AC 功率波形。

This canonical class merges three raw descriptions that represented different architectural realizations of the same physical synthesis principle.

Canonical variants：

### PM-7A — bridge polarity / amplitude synthesis

```text
two-level / full-bridge / half-bridge PWM state selection
```

Raw source：

```text
PM-R13 → PM-7A
```

### PM-7B — multilevel voltage-state synthesis

```text
selection among multiple available voltage states / levels
```

Raw source：

```text
PM-R12 → PM-7B
```

### PM-7C — bidirectional matrix / cycloconverter HF-link-to-AC synthesis

```text
bidirectional switch-state selection directly connects / commutates HF-link energy into the required AC polarity and waveform
```

Raw source：

```text
PM-R10 → PM-7C
```

Decision：

```text
PM-R10 / PM-R12 / PM-R13
= three implementation variants
NOT three independent same-level energy mechanisms
```

Typical coordinate：

```text
X3
```

It may physically overlap X1 in：

```text
#01
#06
#07
#08
#09
```

Main loss signature：

```text
switch conduction
switching / commutation loss
dead-time distortion
reverse-recovery / Coss where applicable
number of series devices in current path
circulating / balancing current for selected variants
```

---

## 11. Raw items demoted from independent canonical L3 status

### PM-R3 — coupled-inductor magnetic gain / energy transfer

Decision：

```text
NOT an independent primitive L3 class
```

Reason：

A coupled-inductor cell physically combines：

```text
PM-1 mutual-flux / turns-ratio action
+
PM-2 inductive field-energy storage / release
```

Its novelty or value must therefore be evaluated from the actual coupling / energy-transfer graph and loss terms, not from the label `coupled inductor`.

Status：

```text
PM-R3 → COMPOSITE(PM-1, PM-2)
```

### PM-R5 — impedance-network L/C exchange with shoot-through states

Decision：

```text
NOT an independent primitive L3 class
```

Reason：

Z/qZ impedance-network operation combines：

```text
PM-2 inductive field-energy transfer
+
capacitive field-energy storage
+
switching-state strategy using shoot-through / non-shoot-through intervals
```

When that capacitor participates in ordinary impedance-network state energy rather than 2ω buffering, it is not automatically X2 / PM-5 in the functional-coordinate sense.

Status：

```text
PM-R5 → COMPOSITE / ARCHITECTURE-CONDITIONED MECHANISM
```

### PM-R11 — semiconductor / synchronous rectification

Decision：

```text
SUPPORT PRIMITIVE
NOT admitted as independent physical-gap solution mechanism
```

Rectification is a real loss-bearing conversion function and must remain in loss accounting：

```text
diode Vf / recovery
or
synchronous-switch RDS(on) / switching / gate loss
```

But merely replacing rectification implementation does not create a separate research-direction mechanism unless it is part of a broader physical-gap solution.

Status：

```text
SP-1 = directional rectification / synchronous rectification support primitive
```

---

## 12. Raw-to-canonical mapping

```text
PM-R1  → PM-1
PM-R2  → PM-2A
PM-R3  → COMPOSITE(PM-1 + PM-2)
PM-R4  → PM-3
PM-R5  → COMPOSITE(PM-2 + capacitive field storage + shoot-through strategy)
PM-R6  → PM-2B
PM-R7  → PM-4
PM-R8  → PM-5
PM-R9  → PM-6
PM-R10 → PM-7C
PM-R11 → SP-1 support primitive
PM-R12 → PM-7B
PM-R13 → PM-7A
```

Therefore：

```text
13 raw entries
↓
7 canonical L3 mechanism classes
+ 1 support primitive
+ 2 explicit composite constructs
```

No information is discarded; ontology status is corrected.

---

## 13. Mechanism-function classes

The seven canonical L3 mechanisms are on one ontology level, but they serve different physical functions：

```text
TRANSFORMATION / MAIN POWER TRANSFER
  PM-1 Magnetic Flux-Linkage Transformation
  PM-2 Inductive Energy Transfer
  PM-3 Capacitive Charge-Transfer / Voltage-Stacking

COMMUTATION
  PM-4 Reactive-Energy-Assisted Commutation

BUFFERING / ENERGY ROUTING
  PM-5 Capacitive Field-Energy Buffering
  PM-6 Controlled Bidirectional Storage-Port Transfer

AC SYNTHESIS
  PM-7 Semiconductor Switching-State AC Synthesis
```

This functional grouping does NOT reintroduce the old X1→X2→X3 mandatory-stage assumption.

A physical network may implement several classes at once.

---

## 14. Cross-family coverage after deduplication

```text
Family   Canonical L3 mechanisms commonly present / possible
--------------------------------------------------------------------------
#01      PM-1 + PM-7A
#02      PM-1 + [PM-4 variant] + PM-5 + PM-7A + SP-1
#03      PM-1 + PM-2B + [PM-4] + PM-7A
#04      PM-2A and/or PM-1+PM-2 coupled form and/or PM-3 + PM-7A + SP-1
#05      implementation-dependent PM-1/PM-2 + optional PM-5/PM-6 + PM-7A
#06      PM-2A + PM-7A
#07      composite PM-2 + capacitive field storage + PM-7A
#08      PM-3 + PM-7B, or PM-3 + downstream PM-7A
#09      PM-1 + PM-7C + optional PM-4 / PM-5 / PM-6
```

Square brackets / `optional` mean the family label does not guarantee the mechanism.

---

## 15. Loss-accounting rule for later compatibility screen

A mechanism may enter a PG compatibility comparison only with its own added-loss signature declared.

Minimum rule：

```text
ΔP_net = P_saved - P_added
```

where：

```text
P_saved and P_added
must use the same Vin / Vout / Pout / temperature / isolation / protection / auxiliary-loss boundary
```

For a strong mechanism claim, uncertainty must not be hidden.

Preferred conservative form：

```text
ΔP_net,min = P_saved,min - P_added,max
```

A mechanism does not pass merely because its topology label is known to be efficient in another operating regime.

---

## 16. What this changes from MP-A...MP-F

Historical pools remain useful as search / reasoning buckets, but they are no longer the objects directly crossed with PGs.

```text
MP-A Early X1
→ strategy; realized using PM-1 / PM-2 / PM-3 or composites

MP-B Soft commutation
→ primarily PM-4

MP-C Collective HV building
→ PM-1 / PM-2 / PM-3 depending actual energy path

MP-D Direct / integrated AC synthesis
→ architecture strategy using PM-7 variants

MP-E Intentional 2ω routing
→ PM-5 and/or PM-6

MP-F Continuous-input / ripple shaping
→ L4 property produced by implementation of PM-2 / composites / control
```

Formal consequence：

```text
PG × MP-A...MP-F = REJECTED
PG × canonical PM-1...PM-7 = NEXT SCREENING OBJECT
```

---

## 17. Decision state

```text
Raw L3 inventory PM-R1...PM-R13     = SUPERSEDED AS DIRECT SCREENING SET
Canonical L3 dictionary             = ESTABLISHED v1
Canonical L3 mechanism count        = 7
Support primitive SP-1              = ESTABLISHED
Coupled-inductor primitive status   = REJECTED / COMPOSITE(PM-1+PM-2)
Z/qZ impedance-network primitive    = REJECTED / COMPOSITE
PM-R10/R12/R13 independent status   = REJECTED / MERGED INTO PM-7 VARIANTS
MP-A...MP-F direct PG crossing      = REJECTED

PG-1                                = HYPOTHESIS
PG-2                                = HYPOTHESIS / STRONG SIGNAL
PG-3                                = OPEN
PG-4                                = HYPOTHESIS

Mechanism combination               = NOT YET EXECUTED
Candidate #10                       = HOLD / NOT_ASSIGNED
Novelty                             = NOT_ESTABLISHED
```

Next formal action：

```text
PG-1...PG-4 × PM-1...PM-7 compatibility screen
↓
for each pair classify:
DIRECT / CONDITIONAL / TRADE-OFF / IRRELEVANT / RISK
↓
attach required falsifier + added-loss terms
↓
reject mechanisms that merely relocate the loss
↓
only surviving pairs may proceed toward A1/B/C comparison
```
