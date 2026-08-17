# 06 — Validation Plan

Status date: 2026-08-17
Current gate: `G0/G1 preparation`

## 1. 驗證原則

不要一開始就畫完整「新拓撲」並用複雜元件模型硬跑。

先驗證研究假設，再逐步增加物理細節：

```text
Analytical scaling
→ system-level mechanism
→ switching-cell physics
→ field/parasitic extraction
→ back-annotated system loss
→ hardware
```

每一階段都可以淘汰錯誤假設。

## 2. G0 — Analytical Scaling

目標：證明 48 V → 24 V → 12 V 時，哪些 loss/stress 以什麼比例變化。

固定至少比較：

```text
Pout = 1 / 2 / 3 kW
Vin  = 12 / 18 / 24 / 48 V
Vout = 220 Vac
fout = 60 Hz
```

輸出：

```text
Iavg
required R_eq budget
I²R sensitivity
2ω energy swing
candidate capacitor-energy requirement
full-current component count
```

優先建立 scaling law，而不是只列數字。

## 3. G1 — PLECS 系統級驗證

第一個主要模擬工具：

```text
PLECS
```

原因：先驗證 topology / energy-routing / RMS / loss mechanism，而非先研究單顆 semiconductor transient。

### 3.1 最小模型

先使用 idealized impedance transformation：

```text
12–24 Vdc
   ↓
Ideal / controlled impedance-transformation block
   ↓
HV energy node
   ↓
single-phase inverter
   ↓
220 Vac
```

比較：

```text
Case 0 — Buffer OFF
Case 1 — HV-side bidirectional 2ω Buffer ON
```

### 3.2 第一輪必看量

```text
I_source,avg
I_source,RMS
I_source,2ω
I_link,RMS
I_buffer,RMS
P_buffer processed
DC-link ripple
P_cond with declared R_eq
```

核心判定：

```text
ΔP_saved
= (I_RMS,OFF² - I_RMS,ON²) × R_LV
```

再比較：

```text
ΔP_saved > P_buffer,loss ?
```

若否，該 placement 不值得繼續。

### 3.3 第二輪 PLECS

將 ideal transformation 逐步替換為：

```text
A. conventional HFT benchmark
B. direct HFL benchmark
C. candidate capacitive/electric-field cell
```

所有方案盡量鎖定：

```text
Vin / Pout / Vout
semiconductor generation
thermal constraint
copper budget
switching-frequency range
passive-volume boundary
auxiliary-loss accounting
```

## 4. G2 — LTspice switching-cell 驗證

第二個工具：

```text
LTspice
```

用途：從完整系統抽出單一 switching cell，加入詳細 semiconductor / parasitic behavior。

重點觀察：

```text
VDS / IDS
VGS
Coss / Qoss behavior
body diode
reverse recovery
dead time
ZVS / ZCS boundary
resonant current
commutation current
voltage overshoot
```

不要用 LTspice 當第一個完整 60 Hz + hundreds-kHz 全系統 loss simulator。

## 5. G3 — Ansys Maxwell / Q3D

第三階段：

```text
Maxwell electrostatic / field model
Q3D parasitic extraction
```

Electric-field candidate 必須由幾何結構得到實際：

```text
coupling capacitance
capacitance matrix
parasitic capacitance
E-field distribution
dielectric stress
common-mode paths
```

Q3D / interconnect extraction：

```text
R(f)
L(f)
C
G
busbar / PCB / connector parasitics
```

## 6. G4 — Back-Annotation

將 LTspice / Maxwell / Q3D 得到的真實參數回填 PLECS：

```text
RDS(on,T)
ESR(f,T)
DCR / AC resistance
parasitic L/C
switching-energy maps
coupling capacitance
common-mode capacitance
```

再做完整：

```text
P_semiconductor
P_switching
P_magnetic
P_capacitor
P_busbar/PCB
P_buffer
P_auxiliary
P_total
```

## 7. G5 — Hardware Prototype

硬體不只量輸入輸出效率。

至少量：

```text
source Iavg / IRMS
source 120 Hz component
HF switching ripple
main-link RMS current
buffer current / voltage
capacitive-link current
switch stress
thermal map
efficiency curve
loss breakdown or calorimetric/cross-checked estimate
common-mode / EMI indicators
isolation stress
```

## 8. Benchmark / Ablation 結構

正式論文不一定寫「對照組」，但至少需要：

```text
Benchmark A:
Conventional HFT + Rectifier + HV Bus + VSI

Benchmark B:
Direct HFT High-Frequency-Link DC–AC / Xi'an-type mechanism class

Candidate C:
Electric-field / energy-routing candidate
```

以及候選內部：

```text
Ablation 1: Buffer OFF
Ablation 2: Buffer ON
```

## 9. 第一個 Go / No-Go Gate

在投入 Electric-field geometry 之前，必須先得到：

```text
1. Buffer ON 確實降低 LV-side RMS current；
2. 對指定 R_LV，省下的 I²R 可量化；
3. Buffer added loss 的合理上限低於 saved loss；
4. 改善在 12–24 V / 1–3 kW 範圍內不是只有單一點成立。
```

若 G1 不成立：

```text
STOP / REFRAME
```

不要為了既定 Electric-field 構想繼續堆疊複雜度。
