# 28 — X1 / X2 / X3 與 Physical-Gap Definition v1

Status date: 2026-08-19  
Role: `RESEARCH-DEFINITION NORMALIZATION / PHYSICAL-GAP VALIDATION`  
Research object: `FUNCTIONAL COORDINATES + GAP PROMOTION RULES`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

本文件先處理研究語言與判定規則，不做 topology synthesis，也不開始新的 mechanism combination。

原因：目前 #01～#09、X1/X2/X3、MP-A...MP-F 與 PG-1...PG-4 已經形成工作框架，但存在不同抽象層級混用的風險。若不先正規化，後續 `PG × Mechanism compatibility` 可能把 strategy、physical mechanism、architecture、function、property 當成同一層級物件比較。

本文件建立：

```text
X1 / X2 / X3 operational definition
↓
coordinate-overlap rule
↓
architecture / strategy / mechanism / property separation
↓
Physical-Gap promotion gate
↓
A0 / #02 / #04 / #09 cross-test
↓
只有通過 Definition Gate 才進入 PG × Mechanism compatibility
```

核心規則不變：

```text
P_saved > P_added
```

但所有 `P_saved` / `P_added` 必須位於 matched comparison boundary 下。

---

## 2. X1 / X2 / X3 的共同原則

X1、X2、X3 是 **functional coordinates（功能座標）**，不是固定零件名稱，也不是強制串聯的三個實體級。

因此：

```text
X1 ≠ transformer
X2 ≠ capacitor
X3 ≠ H-bridge
```

而是：

```text
X1 = 第一次主要電壓 / 電流域轉換功能
X2 = 低頻脈動能量 / 雙向緩衝與路由功能
X3 = 最終單相 AC 波形合成功能
```

同一個 switching network 可以同時承擔兩個以上座標功能。

Formal overlap rule:

```text
X1, X2, X3 MAY OVERLAP PHYSICALLY
but MUST remain distinguishable by function and loss accounting.
```

禁止假設所有 architecture 都必須具有：

```text
X1 → X2 → X3
```

三個獨立串聯功率級。

---

## 3. X1 — First Major Voltage / Current-Domain Transformation Region

### 3.1 Formal definition

X1 定義為：

> 從低壓 DC source 沿主要功率路徑往後追蹤時，第一個使「大部分輸出功率」從 source-referenced extreme-LV / high-current domain 進入明顯較高電壓、較低主路徑電流之能量域的連續功率處理區域。

關鍵字是：

```text
first
majority of main-path power
voltage/current-domain transformation
continuous power-processing region
```

X1 是 **region**，不是單一節點。

### 3.2 X1 start boundary

X1 的起點定義為：

> 第一個主動或被動功率處理元件開始參與「建立新的電壓/電流域」的位置。

例如：

```text
#02 → LV switching / HFT excitation begins
#04 → first boost / coupled-inductor / multiplier processing cell begins
#09 → LV HF switching / HF-link excitation begins
```

單純：

```text
connector
fuse
busbar
reverse-polarity protection
local bulk capacitor
```

如果只承擔產品介面、分配、保護或去耦，而沒有建立新的主功率電壓/電流域，不視為 X1 本身。

這些元件的損耗仍可能屬於 `pre-X1 exposure`，但不能因位於 source 後方就自動稱為 X1。

### 3.3 X1 completion boundary

X1 的完成邊界定義為：

> 第一個可以證明主要輸出功率已經進入 reduced-current domain 的電氣邊界。

不以固定 topology 名稱判定，而記錄以下 normalized quantities：

```text
G_V,X1  = V_domain,after / V_source
ρ_I,X1  = I_rms,after / I_source,rms
P_X1    = main-path power transferred through X1
η_X1    = P_after / P_before under declared boundary
```

不在 v1 強制設定一個跨所有 topology 的固定 `G_V` 或 `ρ_I` 門檻；不同 architecture 的波形、AC/DC state 與分支數不同，硬設單一閾值會產生分類偏差。

但是每次宣稱「X1 已完成」時，必須能指出：

```text
1. X1 前的 source-domain current burden
2. X1 後的 voltage/current domain
3. majority power 確實已進入後者
4. 後續主功率路徑不再需要以 source-level full current 傳輸相同功率
```

### 3.4 Distributed-X1 rule

若升壓不是單一步驟，而是多個 cell / stage 累積完成，X1 可以是 distributed region。

例如：

```text
LV source
→ interleaved cell
→ coupled-inductor gain
→ multiplier cells
→ HV node
```

此時不可強迫把某一顆電感、某一顆 diode 或第一級 switch 單獨指定為 X1。

Formal rule:

```text
X1 may span multiple cells until the first sustained reduced-current domain is established.
```

### 3.5 X1 does not mean "earlier is always better"

`Earlier X1` 只是一種 strategy。

研究判定仍然是：

```text
saved pre-X1 conduction / RMS burden
>
added switching + magnetic + charge-transfer + circulating + control loss
```

因此：

```text
earlier voltage rise ≠ research gap
earlier X1 ≠ automatic improvement
```

---

## 4. Pre-X1 extreme-LV exposure — operational quantity for PG-1

PG-1 不再只使用模糊的 `exposure` 字眼。

v1 將 `pre-X1 extreme-LV exposure` 拆成至少四個可記錄量：

```text
E1 — I_source,rms / I_source,avg
E2 — Σ I_rms,k² · R_eff,k  for unavoidable source-domain conduction paths
E3 — semiconductor conduction loss while carrying source-domain current
E4 — source-domain current-bearing function count / path burden before X1 completion
```

其中核心損耗量為：

```text
P_preX1,cond
≈ Σ(I_rms,k² · R_eff,k)
 + Σ(P_semiconductor,cond,k)
```

實際比較時必須分離：

```text
intrinsic conversion path
product-interface protection
startup-only functions
packaging/interconnect engineering
```

避免把刪除保護、fuse、precharge 等產品功能誤算成 topology gain。

PG-1 的正式研究問題因此修正為：

> 在 matched product / converter contract 下，不同 X1 mechanism 完成第一次主要電壓/電流域轉換以前，需要付出多少 source-domain RMS / conduction burden；改變 X1 能否使總 `P_preX1,cond` 下降，而且新增損耗更小？

---

## 5. X2 — 2ω / Bidirectional Energy Buffer and Routing Coordinate

### 5.1 Formal definition

X2 定義為：

> 系統中專門吸收、釋放、重新路由或隔離單相 2ω pulsating energy，或提供等效雙向能量緩衝功能的功能座標。

X2 可以是：

```text
passive HV DC-link storage
active power-decoupling port
bidirectional buffer
AC-side / differential storage
HFL-integrated pulsating-energy routing
```

X2 不是「只要有 capacitor 就存在」。

只有當該元件 / 網路實際承擔 2ω 或等效低頻能量擺動時，才把它視為 X2 功能的一部分。

### 5.2 X2 observables

PG-4 / X2 至少記錄：

```text
P_2ω,source      = source-side 2ω power amplitude / equivalent scale
I_2ω,source      = source-current 100/120-Hz component
E_2ω,buffer      = energy swing handled by the buffer coordinate
ΔV_buffer,2ω     = buffer-node low-frequency ripple
P_X2,added       = active/passive buffer added loss
```

### 5.3 X2 overlap rule

X2 可以與 X1 或 X3 共用元件或 switching network。

例如：

```text
Direct HFL / differential AC decoupling
→ X2 + X3 may overlap
```

但 loss accounting 必須能區分：

```text
AC synthesis burden
vs
2ω energy-routing burden
```

### 5.4 X2 hard gate

Active X2 仍然不是預設答案。

```text
If passive / inherent architecture already suppresses LV-side 2ω sufficiently:
→ active X2 = REJECT / NOT JUSTIFIED
```

保留條件：

```text
P_LV,saved > P_X2,added
```

---

## 6. X3 — Complete AC-Synthesis Region

### 6.1 Formal definition

X3 定義為：

> 使主要功率最終取得要求之單相 AC polarity、fundamental amplitude / waveform control，並形成可供輸出濾波與負載使用之 AC 功率的功能區域。

典型 #02：

```text
HV DC-link
→ VSI / H-bridge + PWM
→ output filter
→ AC
```

其中 VSI / bridge 是 X3 核心；filter 為 output-conditioning boundary，需依比較 contract 一致納入或排除。

### 6.2 X3 may overlap X1

在 single-stage boost inverter、direct HFL、某些 switched-capacitor / multilevel architecture 中：

```text
voltage conversion
+
AC polarity/amplitude synthesis
```

可能由同一主 switching network 完成。

因此：

```text
X1 ≈ X3 physical overlap
```

是允許的。

這不表示兩個功能概念相同；只是 physical implementation 共用。

---

## 7. Research ontology normalization

後續不得再把不同抽象層級統稱為「mechanism」。

正式分成四層：

### L1 — Architecture / Main Circuit Graph

回答：

> 能量主路徑怎麼連？

例如：

```text
#02 HFT + Rectifier + HV DC Bus + VSI
#04 Non-Isolated High-Gain + VSI
#09 Direct HFL DC–AC
```

### L2 — Strategy

回答：

> 在哪裡、以什麼系統安排處理問題？

例如：

```text
early X1
stage integration
early fan-out
post-X1 buffering
```

### L3 — Physical Mechanism

回答：

> 實際靠哪個能量轉移 / 換流 / 儲能物理機制完成？

例如：

```text
transformer turns-ratio transformation
inductor energy transfer
coupled-inductor gain
capacitor charge transfer / stacking
resonant commutation
ZVS / ZCS
leakage-energy utilization
bidirectional buffer charge/discharge
```

### L4 — Resulting Property / Observable

回答：

> 最後得到什麼波形或應力特性？

例如：

```text
continuous input current
reduced source ripple
lower device voltage step
reduced dv/dt
reduced RMS current
```

Formal prohibition:

```text
Strategy ≠ Physical Mechanism
Architecture ≠ Physical Mechanism
Property ≠ Physical Mechanism
```

---

## 8. Reclassification of current MP-A...MP-F

MP-A...MP-F 保留作為 historical screening pools，但不再宣稱六者是同一 ontology level。

```text
MP-A Early X1
= Strategy pool

MP-B Soft commutation / leakage-energy utilization
= Physical-mechanism pool

MP-C Collective high-voltage building
= Mechanism-family / strategy hybrid pool
  → later must decompose into inductor / coupled-inductor / charge-transfer mechanisms

MP-D Direct / integrated AC synthesis
= Architecture / integration-strategy pool

MP-E Intentional 2ω energy routing
= Energy-routing function / physical-mechanism pool

MP-F Continuous-input / ripple-current shaping
= Resulting-property / control-strategy pool
```

因此下一輪不允許直接做：

```text
PG × {MP-A, MP-B, MP-C, MP-D, MP-E, MP-F}
```

而要先把每個 pool 中真正可比較的 `L3 Physical Mechanism` 拆出來。

---

## 9. Physical-Gap promotion gate

「看到損耗」不等於「研究缺口」。

正式狀態鏈：

```text
OBSERVATION
↓
TOPOLOGY-STRUCTURAL SIGNAL
↓
PHYSICAL-GAP HYPOTHESIS
↓
FAIR-FALSIFICATION TEST
↓
SURVIVES / REJECTED
↓
VERIFIED PHYSICAL GAP only if all gates pass
```

### G1 — measurable physical quantity

必須能用明確物理量描述，不得只靠形容詞。

例如：

```text
bad:  current is too large
better: P_preX1,cond / I_rms / R_eq
```

### G2 — abstraction survives A0

問題不能只存在於 ASP 的：

```text
PCB layout
specific fuse
specific connector
specific relay
specific driver stuffing
specific protection implementation
```

抽象掉產品細節後，仍必須是 main energy-path question。

### G3 — fair existing-method falsifier exists

每一個 PG 必須指定能反駁它的公平既有方法。

例如：

```text
PG-1 → optimized A1 magnetic X1 / alternative high-gain X1
PG-2 → resonant / soft-commutated A1 or active-HFT
PG-3 → fair optimized magnetic A1 vs nonmagnetic / alternative transformation mechanisms
PG-4 → passive HV-link + direct-HFL / AC-side decoupling benchmark
```

### G4 — matched comparison boundary

比較必須固定：

```text
Vin
Pout
Vout / AC requirement
load point
thermal condition
isolation requirement
protection / product functions
auxiliary-power boundary
semiconductor technology generation
measurement / estimation basis
```

否則 `P_saved` 與 `P_added` 不具可比性。

### G5 — materiality

物理問題必須足以改變研究決策。

v1 不硬編碼固定 `5 W` 或 `10%` 全域門檻；每一 PG 必須在 comparison contract 內宣告 materiality criterion 與 uncertainty。

Formal rule:

```text
measurable ≠ material
material threshold must be declared before final promotion
```

### G6 — loss-shifting audit

若解法只是把一種損耗換成另一種同等或更大的損耗：

```text
PG solution claim = REJECT
```

必須滿足：

```text
P_saved > P_added
```

且新增：

```text
RMS
circulating current
commutation
magnetic burden
capacitor charge-transfer burden
control / gate-drive burden
```

都要進入同一 loss boundary。

### G7 — final promotion rule

只有以下全部成立才可稱：

```text
VERIFIED PHYSICAL GAP
```

條件：

```text
G1 measurable
G2 topology-relevant after product abstraction
G3 fair falsifier executed
G4 matched boundary satisfied
G5 materially significant
G6 survives loss-shifting audit
```

否則最多只能保持：

```text
HYPOTHESIS
SUPPORTED HYPOTHESIS
OPEN
```

---

## 10. Current PG status under the new gate

本文件不因重新定義而自動升級任何 PG。

### PG-1

```text
Status = HYPOTHESIS / TOPOLOGY-RELEVANT
```

現在已明確化主要量：

```text
P_preX1,cond
I_source,rms
source-domain semiconductor conduction
source-domain current-path burden
```

仍需：

```text
H1 evidence
fair A1 / alternative-X1 falsification
materiality criterion
```

### PG-2

```text
Status = HYPOTHESIS / STRONG STRUCTURAL SIGNAL
```

RC snubber 只證明存在 dissipative path，不證明 materiality。

仍需：

```text
P_snubber
P_switching / overlap
leakage/Coss significance
soft-commutated A1 falsifier
```

### PG-3

```text
Status = OPEN / NOT YET A GAP
```

而且比較量修正為：

```text
TOTAL TRANSFORMATION BURDEN
```

不是只比較：

```text
magnetic loss
```

對 alternative X1 必須對稱納入：

```text
inductor burden
capacitor RMS / ESR
charge redistribution
switch / diode loss
circulating energy
```

### PG-4

```text
Status = HYPOTHESIS / NOT_ESTABLISHED
```

正式 observables：

```text
P_2ω,source
I_2ω,source
E_2ω,buffer
ΔV_buffer,2ω
P_X2,added
```

Active X2 仍受 H4 hard gate。

---

## 11. Cross-test A — ASP-2000 A0 / #02

A0 verified path：

```text
BAT+
→ fuse/local bulk
→ A/C LV switching
→ T1/T2 PQ5050
→ secondary collective/series formation
→ HV rectifier
→ HV DC-link
→ HV inverter
→ AC
```

### X1 assignment

```text
X1 start
= A/C LV switching begins to excite T1/T2 primary

X1 core mechanism
= HFT magnetic impedance / voltage-ratio transformation

X1 completion boundary
= T1/T2 secondary high-voltage / reduced-current domain is established
```

因此：

```text
fuse / local bulk = pre-X1 support / product path
20 main LV MOS = X1 switching implementation
T1/T2 = X1 transformation core
HV rectifier = post-X1 conversion boundary
```

此定義與目前 A0 不衝突，而且比「X1 = transformer」更完整。

### X2 assignment

```text
HV DC-link
= passive X2-capable coordinate
```

但要等 H4 證明它實際承擔多少 2ω energy，不能只因存在大電容就自動宣稱 X2 effectiveness 已成立。

### X3 assignment

```text
HV inverter / VSI
= X3 core
```

Result：

```text
Definition cross-test = PASS
```

---

## 12. Cross-test B — #04 Non-Isolated High-Gain DC/DC + VSI

Representative path：

```text
LV source
→ switch / inductor / coupled-inductor / multiplier cells
→ HV DC node
→ VSI
→ AC
```

### X1 assignment

X1 不是一顆特定元件，而可能是 distributed region：

```text
first gain-processing cell
→ intermediate gain cells
→ first sustained HV / reduced-current node
```

機制可以不同：

```text
inductor energy transfer
coupled-inductor voltage gain
capacitor charge transfer / stacking
interleaved current processing
```

但 architecture 仍屬 #04。

### X2 assignment

若 HV node 具有足夠低頻 storage：

```text
passive X2-capable
```

若另有 active buffer：

```text
explicit X2
```

### X3 assignment

```text
VSI = X3
```

Result：

```text
Distributed-X1 rule required
Definition cross-test = PASS
```

---

## 13. Cross-test C — #09 Direct High-Frequency-Link DC–AC

Representative path：

```text
LV source
→ HF switching
→ HFT / HF link
→ matrix / cycloconverter / direct AC stage
→ AC
```

### X1 assignment

```text
X1 start
= LV HF switching

X1 core
= HFT / HF-link voltage-current-domain transformation

X1 completion
= reduced-current HF secondary / link domain
```

### X3 assignment

```text
direct matrix / cycloconverter / AC synthesis region
= X3
```

X1 與 X3 可以相鄰甚至部分共用 switching / commutation resources，不要求完整 HV DC bus。

### X2 assignment

只有當 architecture 有：

```text
AC-side decoupling
differential-output storage
intentional HFL pulsating-energy routing
```

時才宣稱明確 X2。

「沒有 full HV DC-link」本身不是 X2 solution。

Result：

```text
Coordinate-overlap rule required
Definition cross-test = PASS
```

---

## 14. Definition Gate result

v1 定義已通過三個 materially different architecture 的初步交叉測試：

```text
A0 / #02 magnetic HFT path      = PASS
#04 distributed high-gain path  = PASS
#09 direct HFL path              = PASS
```

因此後續可以保留：

```text
X1 / X2 / X3 as functional coordinates
```

但不再把它們視為固定三個實體 stages。

---

## 15. Research-sequence correction

原流程：

```text
Nine-family mechanism extraction
↓
PG × Mechanism compatibility
```

修正為：

```text
Nine-family mechanism extraction                  ✅ v1
↓
X1 / X2 / X3 + Physical-Gap Definition Gate       ✅ v1
↓
Normalize #01–#09 into common X1/X2/X3 template   ← NEXT
↓
Decompose MP pools into ontology-consistent L3 mechanisms
↓
PG × Physical-Mechanism compatibility screen
↓
retain 2–3 physically defensible paths
↓
reclassify against #01–#09
↓
H1–H4 / A1-B-C falsification where required
↓
Topology synthesis only for surviving verified gap
```

因此原本 `PG × Mechanism compatibility = NEXT` 暫時被 Definition Gate 插入一步，不是取消。

---

## 16. Candidate #10 / novelty boundary

本文件再次鎖定：

```text
new taxonomy slot ≠ novelty
new circuit graph ≠ automatically research novelty
existing family ≠ no novelty
```

必須分開：

```text
family classification
circuit-graph difference
physical-mechanism difference
measured / validated research contribution
```

Candidate #10 只有在：

```text
1. verified physical gap survives
2. solution path cannot be reasonably represented by #01–#09
```

時才允許討論。

目前：

```text
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty       = NOT_ESTABLISHED
```

---

## 17. Formal decision state

```text
X1 definition                         = ESTABLISHED v1 / FUNCTIONAL REGION
X2 definition                         = ESTABLISHED v1 / ENERGY-ROUTING COORDINATE
X3 definition                         = ESTABLISHED v1 / AC-SYNTHESIS REGION
X1/X2/X3 physical overlap             = ALLOWED
fixed three-stage interpretation      = REJECTED

pre-X1 exposure wording               = REFINED TO OPERATIONAL LOSS QUANTITIES
MP-A...MP-F same-level ontology        = REJECTED
MP-A...MP-F historical screening use  = KEEP / RECLASSIFICATION REQUIRED

Physical-Gap promotion gate           = ESTABLISHED v1
PG-1                                  = HYPOTHESIS / TOPOLOGY-RELEVANT
PG-2                                  = HYPOTHESIS / STRONG STRUCTURAL SIGNAL
PG-3                                  = OPEN / NOT YET A GAP
PG-4                                  = HYPOTHESIS / NOT_ESTABLISHED

A0/#02 definition cross-test          = PASS
#04 definition cross-test             = PASS
#09 definition cross-test             = PASS

PG × Physical-Mechanism compatibility = DEFERRED ONE STEP
next action                           = NORMALIZE #01–#09 INTO COMMON X1/X2/X3 TEMPLATE
Candidate #10                         = HOLD / NOT_ASSIGNED
Novelty                               = NOT_ESTABLISHED
```
