# 26 — 九類主能量路徑 → 可抽取機制 → PG-1～PG-4 矩陣

Status date: 2026-08-19  
Role: `PHYSICAL-GAP VALIDATION / MECHANISM EXTRACTION`  
Research object: `X1 ENERGY-PATH MECHANISMS — NOT PRODUCT OPTIMIZATION`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

本文件回答目前正式研究問題：

> 九類既有主能量路徑中，哪些**物理機制**能處理 PG-1～PG-4，這些機制又新增什麼不可逆損耗？

本輪**不做 topology 拼接**。

正式順序：

```text
#01～#09 主能量路徑
↓
Mechanism Extraction
↓
PG-1～PG-4 對應
↓
Added-loss / trade-off audit
↓
Mechanism pool
↓
只有 surviving PG 才允許進入 mechanism combination
```

核心規則：

```text
P_saved > P_added
```

以及：

```text
組合多個既有機制
≠ 自動形成 Candidate #10
```

任何組合形成實際 circuit graph 後，必須重新分類回 #01～#09。

---

## 2. Physical-gap reference

```text
PG-1 — extreme-LV conduction / RMS exposure before X1
PG-2 — dissipative commutation / leakage / Coss energy handling
PG-3 — transformation-element burden at extreme conversion ratio
PG-4 — single-phase 2ω energy reflection into the LV source
```

評語標記：

```text
TARGET      = 此類具有直接可抽取的機制處理該 PG
POTENTIAL   = 有條件可能處理，必須量化新增 loss
TRADE-OFF   = 解一部分但容易用另一種 loss 交換
RISK        = 在 12–24 V / kW extreme-LV 條件下可能惡化該 PG
NO-INHERENT = 該 family 本身沒有直接解法
OPEN        = 現有證據不足
```

這些不是效率排名。

---

## 3. #01 Low-Frequency Transformer Inverter

### 主能量路徑

```text
LV DC
→ low-frequency switching / inverter
→ line-frequency transformer
→ AC
```

### 可抽取機制

```text
M01-A — 低 switching-frequency，降低每秒 switching events
M01-B — 單一步驟磁性隔離 / voltage ratio
```

### PG 對應

```text
PG-1 = RISK
PG-2 = POTENTIAL only through low switching frequency
PG-3 = RISK / dominant low-frequency magnetic burden
PG-4 = NO-INHERENT
```

### 新增代價

```text
large LF core / copper
large transformer VA / mass / volume
full power still crosses extreme-LV primary current path
no inherent 2ω energy-routing mechanism
```

### 決定

```text
REFERENCE_ONLY
NOT_IN_MECHANISM_COMBINATION_POOL
```

理由：降低 switching-event count 的優點伴隨很大的低頻磁性負擔；對本研究不是值得帶入新組合的主要機制。

---

## 4. #02 HFT + Rectifier + HV DC Bus + VSI

### 主能量路徑

```text
LV DC
→ LV HF switching
→ HFT                         ← X1
→ HV rectifier
→ HV DC link                  ← passive 2ω-capable energy node
→ VSI                         ← X3
→ AC
```

A0 ASP 屬此 family；A1 是公平最佳化版本。

### 可抽取機制

```text
M02-A — early magnetic impedance transformation
M02-B — transformer turns-ratio voltage lift
M02-C — resonant / soft-switched HFT implementation
M02-D — post-X1 HV energy storage / passive 2ω buffering
M02-E — AC synthesis after entering reduced-current domain
```

### PG 對應

```text
PG-1 = TARGET / but LV bridge conduction remains
PG-2 = POTENTIAL → TARGET when resonant/soft-commutation variant is used
PG-3 = TRADE-OFF / HFT copper-core-leakage burden remains
PG-4 = TARGET through post-X1 HV-link energy storage, effectiveness must be measured
```

### 新增代價

```text
LV bridge conduction + switching
HFT copper/core/leakage
rectifier loss
HV-link capacitor ESR/ripple
separate VSI loss
clamp/snubber if commutation is dissipative
```

### 決定

```text
KEEP AS PRIMARY MECHANISM DONOR + A1 FALSIFICATION BENCHMARK
```

特別是：

```text
soft switching / resonant HFT
```

必須先用來反證 PG-2，不能因 A0 有 RC snubber 就跳到新 topology。

Private industrial evidence note: a user-supplied PQ50-class approval sheet shows a real transfer-type HFT implementation using very-low-turn wide-foil primary windings, a higher-turn secondary, no intentional core gap, and nonzero measured leakage. This is structural context for PG-1/PG-2/PG-3, not A0 transformer numerical evidence.

---

## 5. #03 Active-HFT / DAB + VSI

### 主能量路徑

```text
LV active bridge
→ HFT + controlled leakage/series inductance
→ HV active bridge
→ HV node
→ VSI / AC stage
```

### 可抽取機制

```text
M03-A — phase-shift controlled power transfer
M03-B — transformer leakage / series inductance used as a controlled energy-transfer element
M03-C — ZVS / active soft commutation
M03-D — bidirectional power flow / active energy-routing authority
```

### PG 對應

```text
PG-1 = TRADE-OFF
       early X1 helps leave the LV domain,
       but circulating current can raise LV RMS/peak current

PG-2 = TARGET
       active phase-shift + leakage-mediated transfer can enable ZVS

PG-3 = TRADE-OFF
       HFT remains; added bridge and circulating-current burden appear

PG-4 = POTENTIAL
       bidirectional control is useful for energy routing,
       but 2ω decoupling is not inherent without storage/buffer placement
```

### 新增代價

```text
second active bridge
additional gate-drive/Coss
circulating/backflow power
RMS and peak current when voltage ratio is mismatched
soft-switching range limitation at light load / off-design points
```

### 決定

```text
KEEP MECHANISMS M03-B / M03-C / M03-D
DO NOT KEEP "DAB" AS AN UNQUESTIONED WINNER
```

DAB 的研究價值是：

```text
PG-2 improvement
vs
PG-1 circulating-current penalty
```

這是 mechanism trade-off，不是 topology ranking。

---

## 6. #04 Non-Isolated High-Gain DC/DC + VSI

### 主能量路徑

```text
LV DC
→ high-gain / coupled-inductor / multiplier / interleaved X1
→ HV DC node
→ VSI
→ AC
```

### 可抽取機制

```text
M04-A — interleaved / distributed low-side current processing
M04-B — coupled-inductor voltage gain
M04-C — voltage-multiplier / voltage-lift cells
M04-D — quadratic/cubic/cascaded gain
M04-E — continuous-input-current shaping in suitable variants
M04-F — high-gain X1 without galvanic-isolation HFT
```

### PG 對應

```text
PG-1 = POTENTIAL
       branch/interleaved current processing can reduce local current stress,
       but total LV RMS/I²R must be proven lower

PG-2 = TRADE-OFF
       HFT commutation may disappear,
       but coupled-inductor leakage, diode recovery and switch commutation remain

PG-3 = TARGET AS ALTERNATIVE MECHANISM
       replaces HFT burden with inductor/capacitor/diode burden rather than eliminating it

PG-4 = POTENTIAL
       an HV node can host 2ω storage; not inherently superior to #02
```

### 新增代價

```text
inductor / coupled-inductor copper and core
high duty ratio at extreme gain
leakage/clamp
rectifier/diode loss
capacitor ESR/dielectric loss
charge redistribution
internal circulating current
component voltage/current stress
```

### 決定

```text
KEEP M04-A / M04-C / M04-E / M04-F IN MECHANISM POOL
```

但：

```text
fan-out alone ≠ loss reduction
high gain alone ≠ PG-1 solution
```

---

## 7. #05 Bidirectional DC/DC + VSI

### 主能量路徑

此 family 在本研究中主要保留為**能量路由機制**，不是必然的獨立 X1 winner。

```text
source/battery
↕ bidirectional DC/DC
DC node / buffer
→ VSI
→ AC
```

### 可抽取機制

```text
M05-A — controlled bidirectional energy routing
M05-B — local buffer charge/discharge authority
M05-C — ripple-port / power-pulsation steering
```

### PG 對應

```text
PG-1 = RISK / extra LV active stage can add conduction
PG-2 = OPEN / implementation-dependent
PG-3 = OPEN / depends on isolated or nonisolated realization
PG-4 = TARGET if used as intentional 2ω routing/buffer port
```

### 新增代價

```text
extra active power-processing stage
buffer switch conduction/switching
gate drive
buffer inductor/capacitor loss
extra circulating RMS
control and sensing
```

### 決定

```text
CONDITIONAL MECHANISM DONOR FOR PG-4 ONLY
```

若 PG-4 被 passive HV link 或 direct-HFL decoupling 解掉：

```text
M05-A/B/C → DO NOT ADD
```

---

## 8. #06 Single-Stage Boost / Buck-Boost Inverter

### 主能量路徑

```text
LV DC
→ boost/buck-boost energy processing
→ direct AC synthesis
```

升壓與 AC polarity/amplitude synthesis 被整合在同一主路徑。

### 可抽取機制

```text
M06-A — stage integration
M06-B — direct boost-to-AC synthesis
M06-C — remove separate full HV-bus→VSI conversion boundary where architecture permits
```

### PG 對應

```text
PG-1 = RISK at 12 V / kW extreme gain
       low-side switches/inductors may retain large RMS current and high duty burden

PG-2 = POTENTIAL / fewer conversion boundaries but not inherently soft-switched

PG-3 = TRADE-OFF
       removes HFT but substitutes boost-inductor and switch stress

PG-4 = TRADE-OFF
       direct single-stage operation does not automatically provide 2ω decoupling
```

### 新增代價

```text
large boost ratio / duty burden
inductor RMS and core/copper
switch voltage-current stress
high-frequency ripple
single-phase pulsating-power management still required
```

### 決定

```text
KEEP M06-A / M06-B AS STAGE-INTEGRATION MECHANISMS
HOLD FAMILY AS PRIMARY 12-V X1 CANDIDATE
```

---

## 9. #07 Z-Source / Quasi-Z-Source

### 主能量路徑

```text
LV source
→ impedance network L/C
→ shoot-through-enabled inverter
→ AC
```

### 可抽取機制

```text
M07-A — shoot-through boost within inverter bridge
M07-B — impedance-network energy shaping
M07-C — continuous-input-current behavior in suitable quasi-Z-source variants
```

### PG 對應

```text
PG-1 = TRADE-OFF / RISK
       continuous-input-current variants may reduce source ripple,
       but boost/shoot-through operation creates inductor and internal RMS burden

PG-2 = NO-INHERENT
       shoot-through boost is not itself a soft-switching solution

PG-3 = TRADE-OFF
       replaces transformer with L/C impedance-network burden

PG-4 = POTENTIAL only with intentional decoupling design; not inherent
```

### 新增代價

```text
impedance-network inductors/capacitors
shoot-through current
capacitor voltage stress
inductor RMS/core/copper
extra internal circulating/reactive energy
control range constraints at extreme boost
```

### 決定

```text
KEEP M07-C AS A CURRENT-SHAPING REFERENCE
M07-A/B = HOLD UNTIL EXTREME-LV LOSS BENEFIT IS PROVEN
```

---

## 10. #08 Switched-Capacitor / Multilevel Main Path

### 主能量路徑

```text
LV source
→ switched-capacitor / charge-transfer / stacking cells
→ multilevel / boosted voltage synthesis
→ AC or HV node
```

### 可抽取機制

```text
M08-A — collective capacitor voltage stacking
M08-B — switched-capacitor voltage multiplication
M08-C — multilevel AC synthesis / lower per-device voltage steps
M08-D — magnetic-light / magnetic-free voltage-gain mechanism
```

### PG 對應

```text
PG-1 = POTENTIAL / TRADE-OFF
       voltage can be built collectively,
       but low-side charge pulses and capacitor/switch RMS may remain high

PG-2 = POTENTIAL
       multilevel voltage steps may reduce dv/dt/device switching stress,
       but charge redistribution introduces a different irreversible loss

PG-3 = TARGET AS ALTERNATIVE MECHANISM
       replaces part/all magnetic transformation burden with capacitor charge-transfer burden

PG-4 = POTENTIAL
       capacitors store energy, but ordinary SC gain cells are not automatically 2ω buffers
```

### 新增代價

```text
capacitor ESR/dielectric loss
charge-redistribution loss
balancing current
large capacitor RMS
additional switches / gate drive
startup/precharge/balancing complexity
possible high pulsed source current
```

### 決定

```text
KEEP M08-A / M08-C / M08-D IN MECHANISM POOL
```

但必須以：

```text
P_charge-redistribution + P_cap,RMS + P_switch
```

對抗被移除的 magnetic/rectifier/stage loss。

---

## 11. #09 Direct High-Frequency-Link DC–AC

### 主能量路徑

```text
LV DC
→ HF switching
→ HFT / HF link                   ← X1
→ matrix / cycloconverter / direct AC stage
→ AC
```

可不建立完整：

```text
HV rectifier → full HV DC bus → VSI
```

### 可抽取機制

```text
M09-A — direct HF-link-to-AC synthesis
M09-B — removal/integration of separate rectifier + full DC-link + VSI stages
M09-C — AC-side / differential-output 2ω power decoupling
M09-D — place pulsating-energy routing after HFT rather than through LV source
```

### PG 對應

```text
PG-1 = POTENTIAL
       early HFT still leaves the extreme-LV domain early,
       but LV HF bridge current does not disappear

PG-2 = TRADE-OFF
       removed stages can save loss,
       but bidirectional/matrix commutation becomes a first-order problem

PG-3 = TRADE-OFF
       HFT remains; stage count may decrease

PG-4 = TARGET
       direct-HFL + AC-side/integrated decoupling is a strong existing mechanism
       for preventing all 2ω energy from returning through the LV source path
```

### 新增代價

```text
bidirectional switch conduction
matrix/cycloconverter commutation
HF circulating current
control complexity
AC-side buffer/passive components if used
loss of a large passive HV-link energy reservoir if omitted
```

### 決定

```text
KEEP M09-A / M09-C / M09-D IN MECHANISM POOL
```

PG-4 必須先用 #09 existing prior art 反證；不能把「讓 2ω 不回 LV source」當成新概念。

---

## 12. Nine-family PG matrix — v1

```text
Family   PG-1 extreme-LV        PG-2 commutation        PG-3 transform burden      PG-4 2ω routing
------------------------------------------------------------------------------------------------------
#01      RISK                   POTENTIAL(low fs)       RISK                      NO-INHERENT
#02      TARGET/TRADE-OFF       POTENTIAL→TARGET*       TRADE-OFF                 TARGET
#03      TRADE-OFF              TARGET                  TRADE-OFF                 POTENTIAL
#04      POTENTIAL              TRADE-OFF               TARGET-ALTERNATIVE        POTENTIAL
#05      RISK/NEUTRAL           OPEN                    OPEN                      TARGET
#06      RISK                   POTENTIAL               TRADE-OFF                 TRADE-OFF
#07      TRADE-OFF/RISK         NO-INHERENT             TRADE-OFF                 POTENTIAL
#08      POTENTIAL/TRADE-OFF    POTENTIAL               TARGET-ALTERNATIVE        POTENTIAL
#09      POTENTIAL              TRADE-OFF               TRADE-OFF                 TARGET
```

`* #02` 只有在 resonant / active-clamp / soft-commutation implementation 下才可把 PG-2 升成 `TARGET`；A0 的 dissipative RC damping 不代表整個 #02 family 必然如此。

---

## 13. Mechanism pool — 第一輪保留

九類拆解後，目前只允許以下機制進入後續 combination screen。

### MP-A — Early X1 / leave extreme-LV domain early

來源：

```text
#02 #03 #04 #09
```

作用：

```text
PG-1
```

注意：

```text
"earlier voltage rise" = strategy
not novelty
```

### MP-B — Soft commutation / leakage-energy utilization

來源：

```text
#02 resonant/soft-switched variants
#03 DAB/active-HFT
```

作用：

```text
PG-2
```

必要 trade-off：

```text
saved switching/snubber energy
vs
added resonant/circulating RMS + gate/control loss
```

### MP-C — Collective high-voltage building

來源：

```text
#04 high-gain / multiplier
#08 switched-capacitor / multilevel
```

作用：

```text
PG-1 / PG-3
```

必要 trade-off：

```text
removed magnetic / low-side exposure
vs
inductor/diode/capacitor/charge-redistribution loss
```

### MP-D — Direct / integrated AC synthesis

來源：

```text
#06
#08
#09
```

作用：

```text
stage-count / post-X1 loss reduction
PG-4 placement options
```

必要 trade-off：

```text
removed rectifier/DC-link/VSI loss
vs
boost/multilevel/matrix commutation burden
```

### MP-E — Intentional 2ω energy routing

來源：

```text
#02 passive HV-link storage
#05 bidirectional buffer/ripple port
#09 AC-side / HFL-integrated decoupling
```

作用：

```text
PG-4
```

Gate：

```text
ONLY IF PG-4 SURVIVES H4 MEASUREMENT / FAIR BENCHMARK
```

### MP-F — Continuous-input / ripple-current shaping

來源：

```text
#04 selected interleaved/high-gain variants
#07 selected qZ-source variants
```

作用：

```text
PG-1 source RMS/ripple component
```

必要 trade-off：

```text
reduced source ripple
vs
added inductor/circulating current and magnetic loss
```

---

## 14. Mechanisms NOT admitted to combination pool yet

```text
#01 low-frequency transformer itself
more MOS in parallel
fan-out by itself
interleaving by itself
active X2 before PG-4 survives
remove HV DC bus by itself
DAB label by itself
LLC label by itself
switched-capacitor label by itself
high-gain label by itself
```

Reason:

```text
technique name ≠ physical-gap solution
```

---

## 15. Combination rules — next-stage gate

只有在 mechanism matrix 完成後，才允許開始組合；每一個組合必須通過：

```text
C1 — 每個機制對應明確 surviving PG
C2 — 兩個機制不能只重複解同一件事卻疊加 loss
C3 — circuit graph 必須物理相容
C4 — quantify new circulating/RMS/commutation burden
C5 — P_saved > P_added
C6 — 完成後重新分類 #01～#09
C7 — 若可合理歸回既有 family → 不叫 Candidate #10
C8 — 只有 existing families 無法合理描述且 gap survives → 才討論 #10
```

---

## 16. Evidence notes used for this v1

Prior-art closure already records that the following broad concepts are not novel by themselves:

```text
DAB / active isolated bridge
single-stage boost inverter
Z/qZ-source
switched-capacitor high gain
high-frequency-link direct DC/AC
bidirectional battery↔HV bus
active power decoupling / PPB
```

External literature cross-check used in this pass confirms the mechanism-level trade-offs represented above:

```text
- DAB: leakage/series inductance + phase shift can control power and enable soft switching;
  voltage-ratio mismatch can increase circulating power, RMS and peak current.

- Resonant/LLC: soft switching is a mature HFT mechanism, but resonant/circulating current remains a design trade-off.

- Non-isolated high-gain: coupled-inductor, voltage-multiplier, switched-inductor/capacitor and quadratic mechanisms are established gain mechanisms.

- Single-stage boost inverter, Z/qZ-source, switched-capacitor multilevel and direct-HFL + active-power-decoupling are established prior-art directions.
```

Formal bibliography locking remains under the evidence pipeline; this document uses them to classify mechanisms, not to claim numerical superiority.

---

## 17. Decision

Current research position:

```text
Nine-family taxonomy                = KEEP
Mechanism extraction               = COMPLETE v1
Mechanism pool MP-A...MP-F          = ESTABLISHED FOR SCREENING
PG-1                                = HYPOTHESIS
PG-2                                = HYPOTHESIS / STRONG SIGNAL
PG-3                                = OPEN
PG-4                                = HYPOTHESIS
Mechanism combination               = NEXT, BUT ONLY AGAINST SURVIVING PGs
Candidate #10                       = HOLD / NOT_ASSIGNED
Novelty                             = NOT_ESTABLISHED
```

Next formal action:

```text
PG × Mechanism pair compatibility screen
↓
reject redundant / loss-stacking pairs
↓
retain only 2–3 mechanism combinations with a defensible physical reason
↓
reclassify each combination against #01–#09
```
