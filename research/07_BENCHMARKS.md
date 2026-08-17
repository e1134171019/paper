# 07 — Benchmarks

Status date: 2026-08-17
Purpose: define fair reference architectures before claiming improvement

## 1. Benchmark 原則

Benchmark 不是「找一個比較差的舊電路來贏」。

任何比較必須遵守 `research/contracts/power_converter_comparison_contract_v0.1.md` 的 boundary / operating-point / metric-definition 規則。

至少固定：

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

不同 paper 的 peak efficiency 不得直接當排行榜。

## 2. Benchmark A — ASP / 傳統 HFT 兩級式

Working family:

```text
#02 High-Frequency Magnetic-Isolated Two-Stage
```

抽象功率路徑：

```text
12 Vdc
→ LV MOS HF switching
→ HFT
→ HV rectifier
→ HV DC bus
→ VSI / H-Bridge SPWM
→ LC filter
→ AC
```

目前已從 ASP-2000 類板件研究建立的主要 loss map：

```text
battery / fuse / connector
→ LV MOS conduction
→ LV MOS switching
→ HFT primary copper
→ HFT core
→ HFT secondary copper
→ leakage / clamp / snubber
→ HV rectifier
→ HV bus capacitor
→ HV inverter
→ output filter
→ interconnect / terminal
```

ASP 的研究用途：

```text
real product baseline
```

不是預設它一定效率差。

### A 類需要實測 / 建模的量

```text
source Iavg / IRMS
120 Hz component
HF ripple
HFT primary IRMS
LV path Rdc/Rac
MOS conduction/switching loss
transformer copper/core loss
rectifier loss
HV inverter loss
```

若實測發現 ASP 低壓 source 幾乎沒有 120 Hz 分量，則「2ω buffer 可大量降低 LV RMS」不能直接成立，必須重新定位主要 loss lever。

## 3. Benchmark B — 直接式高頻鏈 DC–AC

Working family:

```text
#09 Direct High-Frequency-Link DC–AC
```

典型路徑：

```text
LV DC
→ HF bridge
→ HFT / HF link
→ bidirectional matrix / cycloconverter stage
→ AC
```

相較 Benchmark A，省略完整：

```text
Rectifier → HV DC Bus → VSI
```

這是我們不能忽略的 modern benchmark，因為若候選 topology 只比傳統兩級式好，reviewer 仍可要求與 single-stage / direct-HFL 方法比較。

## 4. Xi'an line 的定位

目前追蹤的西安交大工作屬 Benchmark B 的重要近鄰：

```text
48 Vdc
→ HF inverter
→ HFT
→ differential cycloconverter / direct AC stage
→ 220 Vac
```

並在 AC side 利用 differential/common-mode capacitor-voltage freedom 做 double-line-frequency power decoupling。

研究含義：

```text
「讓 2ω 能量不必完整穿回 low-voltage / HF source path」
已存在 magnetic/HFT-based strong prior art.
```

因此我們未來若採 electric-field，不可把這個 energy-routing idea 本身當成新穎性。

正式數值、prototype 規格、DOI 與 2026 successor 狀態需由 evidence pipeline 再鎖定後引用。

## 5. Candidate C — Electric-Field / Energy-Routing Architecture

目前僅是 candidate：

```text
12–24 Vdc
→ LV current sharing / early transformation
→ capacitive/electric-field HF transfer
→ HV/reduced-current energy node
↔ bidirectional 2ω buffer
→ AC synthesis
→ 220 Vac
```

比較目標不是只有 efficiency：

```text
I_LV,RMS
I_2ω
I_circulating
number of full-current devices
R_eq seen before X1
switch stress
capacitor RMS / ESR loss
magnetic loss
buffer processed power
P_loss,total
power density estimate
isolation / common-mode / EMI burden
```

## 6. Candidate C 的必要消融實驗

```text
C0 — Buffer OFF
C1 — Buffer ON
```

若 C1 只降低 DC-link ripple、但：

```text
P_buffer,loss + P_extra_circulation > P_saved
```

則 C1 判定失敗。

若 electric-field 版本只移除 HFT core loss，但：

```text
P_cap + P_circulating + P_extra_switch > P_HFT,saved
```

則 electric-field 路線判定失敗或需要重構。

## 7. 公平比較矩陣

最終至少建立：

```text
                    A: HFT 2-stage   B: Direct HFL   C: Candidate
Vin                 matched          matched          matched
Pout                matched          matched          matched
Vout                matched          matched          matched
Isolation           explicit         explicit         explicit
Semiconductor       comparable       comparable       comparable
I_LV,RMS            measured/model   measured/model   measured/model
I_2ω                measured/model   measured/model   measured/model
I_circulating       reported/model   reported/model   measured/model
P_cond              decomposed       decomposed       decomposed
P_sw                decomposed       decomposed       decomposed
P_mag               decomposed       decomposed       N/A or remaining
P_cap               decomposed       decomposed       decomposed
P_buffer             if present       if present       decomposed
P_total              same boundary    same boundary    same boundary
```

若 boundary 無法匹配，該 paper 只能進 `CONTEXT_ONLY` 或 `BOUNDED_TRADEOFF`，不可做 direct scalar ranking。
