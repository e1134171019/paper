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

目標不是立刻得到完整 converter efficiency，而是建立可重複的 A0 動態量測資料，使：

```text
P_mainMOS,sw
P_mainMOS,cond
I_primary,RMS
switch timing
HFT volt-second stress
```

不再依賴猜測。

---

## 2. SchDoc 直接重建出的四組 Gate-drive architecture

主低壓 MOS 並不是 20 顆共用一條 gate net。直接 SchDoc net reconstruction 建立四組獨立 drive group。

### DA1 group

```text
Main MOS:
Q3 Q4 Q5 Q6 Q33

Driver-side gate bus:
DA1-G

Local source/reference:
DA1-E

Individual gate resistors:
R15 R12 R13 R14 R106
= 27R4 each

Gate-source pull-down:
R19 R16 R17 R18 R108
= 47K5 each

Local driver pair:
Q7  = KWC4672
Q8  = 2SA1797
```

### DB1 group

```text
Main MOS:
Q11 Q12 Q13 Q14 Q36

Gate bus:
DB1-G
Source/reference:
DB1-E

Gate resistors:
R30 R31 R32 R33 R113
= 27R4

Pull-down:
R36 R37 R38 R39 R116
= 47K5

Driver pair:
Q15 = KWC4672
Q16 = 2SA1797
```

### DA2 group

```text
Main MOS:
Q18 Q19 Q20 Q21 Q37

Gate bus:
DA2-G
Source/reference:
DA2-E

Gate resistors:
R46 R47 R48 R49 R117
= 27R4

Pull-down:
R55 R56 R57 R58 R118
= 47K5

Driver pair:
Q17 = KWC4672
Q22 = 2SA1797
```

`Q19 drain connectivity` remains `OPEN`; its gate/source context is present.

### DB2 group

```text
Main MOS:
Q24 Q25 Q26 Q27 Q38

Gate bus:
DB2-G
Source/reference:
DB2-E

Gate resistors:
R63 R64 R65 R66 R120
= 27R4

Pull-down:
R69 R70 R71 [plus remaining local pull-down position]
R121
= 47K5

Driver pair:
Q23 = KWC4672
Q28 = 2SA1797
```

Research consequence:

> Four drive groups must be checked independently before assuming symmetric timing/current sharing.

---

## 3. Important probe-reference rule

Do **not** define VGS as:

```text
Gate-to-BAT−
```

or:

```text
driver output-to-BAT−
```

The actual device quantity is:

```text
VGS_device = V(Gate pin after its individual 27.4 Ω resistor)
           - V(the same MOS Source pin)
```

For example:

```text
Q3 VGS  = Q3-G to Q3-S
Q11 VGS = Q11-G to Q11-S
Q18 VGS = Q18-G to Q18-S
Q24 VGS = Q24-G to Q24-S
```

Driver-bus waveform may be measured separately:

```text
DA1-G relative to DA1-E
DB1-G relative to DB1-E
DA2-G relative to DA2-E
DB2-G relative to DB2-E
```

This distinguishes:

```text
driver-command waveform
vs
actual device gate waveform after Rg/parasitics
```

---

## 4. Representative dynamic measurement set

Minimum representative devices:

```text
DA1 → Q3
DB1 → Q11
DA2 → Q18
DB2 → Q24
```

Reason:

```text
DA1/DA2 share the reconstructed A-side transformer switching node,
DB1/DB2 share the reconstructed C-side transformer switching node,
but their local source/reference and gate-drive groups are distinct.
```

Therefore one A-side device and one C-side device are not sufficient to prove all four groups are equivalent.

---

## 5. D0 — Gate timing only

First dynamic run should avoid immediate power-loss integration. Establish timing first.

For T1-side groups:

```text
CH1: DA1-G relative DA1-E
CH2: DB1-G relative DB1-E
```

For T2-side groups:

```text
CH1: DA2-G relative DA2-E
CH2: DB2-G relative DB2-E
```

Record:

```text
fs
period T
Ton
Toff
duty
DA↔DB non-overlap interval
turn-on delay difference
turn-off delay difference
ringing amplitude / frequency
```

For reproducible timing extraction, define the timing crossing consistently, e.g. 50% of each measured gate high-level amplitude. This is a timing definition only, not a claim about MOS conduction threshold.

Status after D0:

```text
exact switching frequency = MEASURED
exact duty              = MEASURED
exact dead/non-overlap   = MEASURED
four-group symmetry      = TESTABLE
```

---

## 6. D1 — Actual device VGS after gate resistor

For each representative device:

```text
Q3  Gate pin ↔ Source pin
Q11 Gate pin ↔ Source pin
Q18 Gate pin ↔ Source pin
Q24 Gate pin ↔ Source pin
```

Record:

```text
VGS,on plateau/high level
VGS,min during off state
turn-on edge
turn-off edge
Miller-region behavior
positive overshoot
negative undershoot
ringing
```

Purpose:

```text
verify whether the four nominally similar banks actually see similar drive
and whether gate-network parasitics can explain switching imbalance.
```

---

## 7. D2 — Device / bank VDS waveform

Representative VDS:

```text
Q3  D-S  → DA1 bank reference
Q11 D-S  → DB1 bank reference
Q18 D-S  → DA2 bank reference
Q24 D-S  → DB2 bank reference
```

Record:

```text
VDS,off
VDS,on
turn-on overlap interval
turn-off overlap interval
peak overshoot
ringing frequency
ringing decay
any repetitive avalanche-like excursion if observed
```

Do not use a ground-referenced oscilloscope probe across a floating switching node unless the measurement setup is explicitly safe for that reference. Use an appropriate differential/isolated measurement method within its common-mode and voltage ratings.

---

## 8. D3 — Current channels

Priority current channels remain:

```text
I_source
I_T1 center-feed
I_T2 center-feed
```

For dynamic switching-loss closure, ideal additional channels would be the individual DA1/DB1/DA2/DB2 bank currents. However current source/return connectivity is not yet reconstructed tightly enough to equate any one center-feed current directly with one MOS-bank current during all commutation intervals.

Therefore:

```text
I_T1 / I_T2
= valid transformer-feed measurements

I_DA1 / I_DB1 / I_DA2 / I_DB2
= separate bank-current quantities; do not infer without evidence
```

This prevents an invalid calculation such as:

```text
P_Q3bank = average[VDS_Q3 × I_T1]
```

unless the switching state and current mapping are explicitly verified.

---

## 9. D4 — Switching-loss integration hierarchy

### Level 1 — timing / stress only

If current-bandwidth evidence is not yet sufficient:

```text
report VGS/VDS/timing/overshoot only
P_sw = OPEN
```

### Level 2 — bank current available

For a bank where total bank current is measured synchronously:

```text
p_bank(t) = vDS,bank(t) × i_bank(t)
P_bank    = average[p_bank(t)]
```

This captures combined bank conduction + switching energy at the measured electrical boundary and does not require assuming equal current sharing between parallel MOS devices.

### Level 3 — per-device current available

Only if individual-device current sharing is itself under study:

```text
p_device(t) = vDS,device(t) × iD,device(t)
```

Per-device measurement is not required for the first A0 total-loss gate if bank-level power can be measured reliably.

---

## 10. D5 — T1/T2 primary-current characterization

Measure separately:

```text
I_T1(t)
I_T2(t)
```

Extract:

```text
Iavg
IRMS
peak current
current imbalance
magnetizing/ramp component if distinguishable
commutation spike
HF ringing
```

Current-sharing metric:

```text
k_share = I_T1,RMS / I_T2,RMS
```

Do not assume `k_share = 1` from topology symmetry.

Transformer copper-loss model remains:

```text
P_primary,Cu = I_primary,RMS² × R_primary,AC(f,T)
```

Actual `R_primary,AC` still requires measurement/extraction; DC winding resistance alone is insufficient at HF when skin/proximity effects are material.

---

## 11. D6 — Transformer voltage / volt-second capture

Measure the center-tap half-primary voltage waveforms with a measurement method appropriate to the switching node.

For each half-cycle, record:

```text
V_primary(t)
∫V_primary(t) dt  [volt-second]
```

The directly measurable volt-second integral is useful even before exact turns count/core area are known.

Once `N` and effective core area `Ae` are locked:

```text
ΔB = (1 / (N Ae)) ∫V_primary dt
```

Until then:

```text
volt-second stress = MEASURED
ΔB                 = OPEN
core loss          = OPEN / BOUNDED LATER
```

---

## 12. D7 — HFT loss closure strategy

Do not force a fake core-loss number before transformer construction data are available.

Use staged closure:

```text
Stage H1:
I_primary,RMS + winding Rdc/Rac
→ primary copper loss

Stage H2:
secondary current + winding Rdc/Rac
→ secondary copper loss

Stage H3:
measured volt-second + N + Ae + material/temperature
→ flux/core-loss model

or

Stage H3-alt:
calorimetric / residual electrical method
→ total transformer loss
```

Formal status:

```text
P_HFT,total = OPEN
until at least copper + core/residual evidence are available
```

---

## 13. Minimum waveform set for one operating point

At each declared operating point save at minimum:

```text
W0: I_source
W1: DA1-G vs DA1-E
W2: DB1-G vs DB1-E
W3: DA2-G vs DA2-E
W4: DB2-G vs DB2-E
W5: Q3 VGS
W6: Q11 VGS
W7: Q18 VGS
W8: Q24 VGS
W9: Q3 VDS
W10: Q11 VDS
W11: Q18 VDS
W12: Q24 VDS
W13: I_T1
W14: I_T2
W15: T1 primary voltage / volt-second
W16: T2 primary voltage / volt-second
```

Not all channels need to be captured simultaneously if the operating condition is repeatable; however waveforms used for instantaneous power integration must be synchronous and time-aligned.

---

## 14. Required operating-point metadata

Every dynamic capture must record:

```text
Vin
Pout
Vout
load type / PF
ambient temperature
MOS/heatsink temperature if available
T1 temperature
T2 temperature
probe type / bandwidth
current-probe type / bandwidth
scope bandwidth / sample rate
channel deskew status
capture time after thermal stabilization
```

Without this metadata, waveform-derived loss values are `CONTEXT_ONLY` rather than benchmark-grade evidence.

---

## 15. Dynamic measurement stop conditions

Stop/reconfigure the measurement rather than accepting the waveform if:

```text
probe common-mode or voltage rating is exceeded
measurement reference would create an unsafe ground path
current probe is saturated
channel time skew is large enough to corrupt v×i switching-energy integration
ringing changes materially when the probe is attached
waveform clips / aliases
operating point is not thermally repeatable
```

For switching-energy integration, probe deskew is mandatory because a small relative time shift between VDS and ID can create a large false switching-loss term.

---

## 16. Gate decision after dynamic data

The A0 dynamic gate closes only when we can separate at least:

```text
P_distribution,measured
P_negativeSeriesBank,measured
P_mainMOS,cond/sw or bounded bank power
P_primary,Cu
P_HFT,remaining/open
```

Then create:

```text
A0 BAT→X1 Loss Budget v1
```

Only after the largest credible loss buckets are known does A1 optimized magnetic synthesis proceed.

Current status:

```text
four drive groups / gate nets      = VERIFIED
individual 27.4 Ω gate resistors   = VERIFIED
local source-reference nets         = VERIFIED
exact fs/duty/dead time             = OPEN → D0
actual VGS/VDS stress               = OPEN → D1/D2
T1/T2 RMS current balance           = OPEN → D5
HFT volt-second                     = OPEN → D6
main MOS switching loss             = OPEN
HFT total loss                       = OPEN
A1                                  = BLOCKED
Candidate #10                        = NOT ASSIGNED
Novelty                              = NOT ESTABLISHED
```