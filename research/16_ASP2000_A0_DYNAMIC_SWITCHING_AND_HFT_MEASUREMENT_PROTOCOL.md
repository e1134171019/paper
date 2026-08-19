# 16 — ASP-2000 A0 動態開關與 HFT 量測程序

Status date: 2026-08-19  
Role: `A0 DYNAMIC-LOSS MEASUREMENT GATE`  
Research phase: `PHYSICAL GAP VALIDATION`  
Hardware result status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark measurement gate`

## 1. 目的

前一階段已把低壓分配路徑拆成 Kelvin / mV-drop 量測。這一文件處理 Kelvin 無法關閉的動態損耗：

```text
Main MOS conduction + switching
T1/T2 primary RMS
switching frequency / duty / dead time
overshoot / ringing / commutation
HFT primary copper / core-related excitation
```

本文件已依 `research/17_ASP2000_A0_PRIMARY_SWITCH_CURRENT_BOUNDARY.md` 修正：

```text
四組 local gate drivers
!= 四個獨立 power branches
```

A0 實際是：

```text
2 個邏輯切換功能：A / C
每側 10 顆 MOS
4 組實體 driver subgroup
共同 Source/return = B
```

---

## 2. 已驗證的主功率切換結構

### A logical switch

Drain power node:

```text
NetC62_1
```

Connected MOS:

```text
DA1 subgroup:
Q3 Q4 Q5 Q6 Q33

DA2 subgroup:
Q18 Q19 Q20 Q21 Q37
```

All Source pads:

```text
→ B
```

Therefore:

```text
A logical switch = 10 parallel MOS
```

### C logical switch

Drain power node:

```text
NetC65_1
```

Connected MOS:

```text
DB1 subgroup:
Q11 Q12 Q13 Q14 Q36

DB2 subgroup:
Q24 Q25 Q26 Q27 Q38
```

All Source pads:

```text
→ B
```

Therefore:

```text
C logical switch = 10 parallel MOS
```

### Q19 correction

```text
Q19 Drain → NetC62_1
Q19 Source → B
```

Status:

```text
Q19 physical power connection = VERIFIED IN PCB
```

---

## 3. 四組實體 Gate driver、兩個邏輯命令

### DA1

```text
MOS: Q3 Q4 Q5 Q6 Q33
Gate bus: DA1-G
individual Rg: 27R4 each
local driver pair: Q7 / Q8
```

### DA2

```text
MOS: Q18 Q19 Q20 Q21 Q37
Gate bus: DA2-G
individual Rg: 27R4 each
local driver pair: Q17 / Q22
```

### DB1

```text
MOS: Q11 Q12 Q13 Q14 Q36
Gate bus: DB1-G
individual Rg: 27R4 each
local driver pair: Q15 / Q16
```

### DB2

```text
MOS: Q24 Q25 Q26 Q27 Q38
Gate bus: DB2-G
individual Rg: 27R4 each
local driver pair: Q23 / Q28
```

Upstream control:

```text
DR-A  ─ R213 = 0R ─ DR-A2
DR-B  ─ R212 = 0R ─ DR-B2
```

Therefore:

```text
A command → DA1 + DA2 drivers → 10 A-side MOS
C command → DB1 + DB2 drivers → 10 C-side MOS
```

Four drivers still require timing comparison because a common logic command does not guarantee identical local propagation/edge behavior.

---

## 4. Probe-reference correction

Do not use BAT- as the reference for main-MOS VGS.

Compiled physical source node is:

```text
B
```

Actual device quantity:

```text
VGS_device = V(Gate pin after individual 27.4 ohm Rg)
           - V(the same MOS Source pin / B-local point)
```

Representative devices:

```text
Q3  = DA1
Q18 = DA2
Q11 = DB1
Q24 = DB2
```

The SchDoc labels:

```text
DA1-E / DA2-E / DB1-E / DB2-E
```

are local/hierarchical source-reference names, not four separate physical high-current returns. At PCB level the actual MOS sources and low-side driver references compile to `B`.

---

## 5. D0 — 先量四組 Gate timing

第一輪不要先做 switching-loss integration。

量測：

```text
DA1-G relative local B/source reference
DA2-G relative local B/source reference
DB1-G relative local B/source reference
DB2-G relative local B/source reference
```

Extract:

```text
fs
period
Ton / Toff
duty
A↔C non-overlap / dead time
DA1↔DA2 propagation mismatch
DB1↔DB2 propagation mismatch
turn-on / turn-off edge mismatch
ringing
```

Formal expected result:

```text
logical synchronization topology = VERIFIED
actual dynamic synchronization    = MEASURED AFTER D0
```

---

## 6. D1 — Actual VGS after Rg

Measure:

```text
Q3  G-S
Q18 G-S
Q11 G-S
Q24 G-S
```

Record:

```text
VGS,on plateau
VGS,min off
Miller behavior
turn-on / turn-off edge
overshoot / undershoot
ringing
```

Purpose:

```text
verify whether the two local drivers under one logical command actually deliver equivalent device drive
```

---

## 7. D2 — Power-node voltage

The first system-level switching-loss boundary should use the two real electrical switch nodes:

```text
V_A-B(t)
V_C-B(t)
```

where:

```text
A = NetC62_1
C = NetC65_1
B = common main-MOS source/return
```

Representative individual VDS such as Q3/Q18/Q11/Q24 may still be recorded to evaluate local parasitic mismatch, but they are not four independent power-stage voltages.

Record:

```text
Voff
Von
overlap interval
peak overshoot
ringing frequency / decay
repetitive avalanche-like stress if present
```

Use appropriately rated differential/isolated measurement equipment and do not create an unsafe ground reference.

---

## 8. D3 — 正確的 Current Boundary

Priority currents:

```text
I_source
I_T1(t) at actual transformer center-tap / winding-feed lead
I_T2(t) at actual transformer center-tap / winding-feed lead
```

The current probes should be placed so `I_T1/I_T2` represent transformer winding/feed current rather than only an upstream fuse/bulk current that can include capacitor-current ambiguity.

During stable A conduction:

```text
i_A,total ≈ i_T1,A + i_T2,A
```

During stable C conduction:

```text
i_C,total ≈ i_T1,C + i_T2,C
```

But:

```text
i_DA1 != i_T1 in general
i_DA2 != i_T2 in general
```

because DA1 and DA2 are parallel subgroups on the same A drain/source power nodes.

Likewise for DB1/DB2 on C.

Subgroup current sharing is a separate quantity:

```text
i_DA1 + i_DA2 = i_A,total
i_DB1 + i_DB2 = i_C,total
```

Do not assign transformer identity to driver subgroup current without evidence.

---

## 9. D4 — Switching-loss integration hierarchy

### Level 1 — timing/stress only

If current bandwidth / deskew are not sufficient:

```text
report timing + VGS + V_A-B / V_C-B stress
P_sw = OPEN
```

### Level 2 — two electrical switch regions

When synchronous current evidence is sufficient:

```text
p_A(t) = v_A-B(t) i_A,total(t)
p_C(t) = v_C-B(t) i_C,total(t)

P_primarySwitchRegion
= average[p_A + p_C]
```

This is the preferred first A0 bank-level electrical boundary.

### Level 3 — driver subgroup current sharing

Only if DA1/DA2 or DB1/DB2 current imbalance becomes important:

```text
i_DA1 = alpha_A i_A,total
i_DA2 = (1-alpha_A) i_A,total
```

Measure/model `alpha_A` rather than assuming 0.5.

### Level 4 — per-device current

Only if individual MOS current sharing itself becomes a target.

---

## 10. Commutation warning

The stable-conduction current-sum model is not automatically valid during dead time and transition edges because current may flow through:

```text
Coss / displacement paths
body diodes
leakage inductance
clamp / snubber networks
parasitic capacitance
ringing loops
```

For switching-energy integration:

```text
voltage and current channels must be synchronous
probe bandwidth must be adequate
channel deskew is mandatory
```

A small V/I time offset can produce a large false switching-energy result.

---

## 11. D5 — T1/T2 primary-current characterization

Measure separately:

```text
I_T1(t)
I_T2(t)
```

Extract:

```text
Iavg
IRMS
peak
T1/T2 imbalance
current ramp / magnetizing component if distinguishable
commutation spike
HF ringing
```

Current-sharing metric:

```text
k_share = I_T1,RMS / I_T2,RMS
```

Do not assume `k_share = 1`.

Primary copper-loss model:

```text
P_primary,Cu = Σ I_primary,RMS^2 R_primary,AC(f,T)
```

Actual `R_primary,AC` still requires measurement/extraction.

---

## 12. D6 — Primary voltage / volt-second

Capture center-tap half-primary voltage waveforms.

For each relevant interval:

```text
∫ V_primary(t) dt
```

Once `N` and `Ae` are locked:

```text
DeltaB = (1 / (N Ae)) ∫V_primary dt
```

Until then:

```text
volt-second stress = MEASURABLE
DeltaB             = OPEN
core loss          = OPEN
```

---

## 13. D7 — HFT loss closure

Use staged closure:

```text
H1:
I_primary,RMS + Rdc/Rac
→ primary copper loss

H2:
secondary current + Rdc/Rac
→ secondary copper loss

H3:
volt-second + N + Ae + material + temperature
→ core-loss model

or H3-alt:
calorimetric / residual electrical method
→ total transformer loss
```

Do not force a core-loss scalar from `PQ5050` form factor alone.

---

## 14. Minimum waveform set

At a declared operating point save at minimum:

```text
W0  I_source
W1  DA1-G / local B reference
W2  DA2-G / local B reference
W3  DB1-G / local B reference
W4  DB2-G / local B reference
W5  Q3 VGS
W6  Q18 VGS
W7  Q11 VGS
W8  Q24 VGS
W9  V_A-B
W10 V_C-B
W11 I_T1
W12 I_T2
W13 T1 primary voltage / volt-second
W14 T2 primary voltage / volt-second
```

Optional local-parasitic set:

```text
Q3 / Q18 individual VDS
Q11 / Q24 individual VDS
```

Waveforms used for instantaneous power integration must be time-aligned.

---

## 15. Required metadata

Every dynamic capture must record:

```text
Vin
Pout
Vout
load / PF
ambient temperature
MOS/heatsink temperature
T1/T2 temperature
probe type / bandwidth
current-probe type / bandwidth
scope bandwidth / sample rate
channel deskew
capture time after thermal stabilization
```

Without this metadata, waveform-derived loss is `CONTEXT_ONLY` rather than benchmark-grade evidence.

---

## 16. Stop conditions

Stop/reconfigure rather than accepting the waveform if:

```text
probe rating/common-mode exceeded
unsafe ground path exists
current probe saturates
V/I skew corrupts integration
probe attachment materially changes ringing
waveform clips / aliases
operating point is not repeatable
```

---

## 17. Gate decision

The A0 dynamic gate closes only when we can separate at least:

```text
P_distribution,measured
P_negativeSeriesBank,measured
P_A/C_switchRegion or credible bound
P_primary,Cu
P_HFT,remaining/open
```

Then create:

```text
A0 BAT→X1 Loss Budget v1
```

Current status:

```text
A/C power nodes                    = VERIFIED
10 MOS per logical switch          = VERIFIED
Q19 connectivity                   = VERIFIED
4 local drivers / 2 logical cmds   = VERIFIED AT CONNECTIVITY LEVEL
actual driver timing mismatch      = OPEN → D0
actual VGS/V_A-B/V_C-B             = OPEN → D1/D2
T1/T2 RMS current                  = OPEN → D5
A/C switching-region loss          = OPEN
HFT total loss                     = OPEN
A1                                 = BLOCKED
Candidate #10                      = NOT ASSIGNED
Novelty                            = NOT ESTABLISHED
```
