# 07 — Benchmarks

Status date: 2026-08-19  
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

---

## 2. Benchmark A — Magnetic HFT class

Working family:

```text
#02 High-Frequency Magnetic-Isolated Two-Stage
```

抽象功率路徑：

```text
LV DC
→ LV MOS HF switching
→ HFT
→ HV rectifier
→ HV DC bus
→ VSI / H-Bridge SPWM
→ LC filter
→ AC
```

A 類現在必須分成兩層，避免把新 modular candidate 跟人工簡化的單體磁性基準比較。

### A0 — ASP-2000 R52 real-product baseline

Direct schematic extraction from the user-supplied ASP-2000 MAIN R52 source establishes:

```text
2 × PQ5050 HFT modules
4 × low-side MOS banks
5 parallel LV MOS devices per bank
20 LV main MOS positions total
8 high-current input fuse positions
2 groups of low-voltage bulk capacitance
4 HV rectifier devices
4 × 680 uF / 315 V HV capacitor positions
separate post-bus HV AC-synthesis stage
```

Research abstraction:

```text
Battery / LV input
→ fuse / LV distribution
→ local LV bulk
→ paralleled LV switch banks
→ T1 / T2 HFT                         ← X1
→ HV rectification
→ HV DC-link / BUS                    ← passive X2-capable node
→ HV inverter                         ← X3
→ output filter
→ AC
```

Detailed evidence boundary is recorded in:

```text
research/10_ASP2000_PRODUCT_BASELINE.md
```

A0 的用途：

```text
measurement-grounded real product baseline
```

不是預設它一定效率差。

### A1 — fair optimized modular-HFT baseline

任何候選若使用 early fan-out / multicell，都必須允許 magnetic benchmark 使用同樣的 current-distribution freedom：

```text
12 V short bus
→ N-way fan-out
→ N × [switching + HFT X1]
→ HV combine / rectification
→ reduced-current energy node
→ X3
→ AC
```

因此禁止以下不公平比較：

```text
new modular candidate
vs
artificially monolithic HFT benchmark
```

A1 主要用於回答：

```text
如果只把現有 magnetic X1 做到同樣好的 current distribution / packaging，
候選機制還剩多少真正的 loss advantage？
```

### A 類 loss map

至少拆解：

```text
battery / fuse / connector
→ common LV interconnect I²R
→ LV bulk ESR / ripple
→ LV MOS conduction
→ LV MOS switching / Coss / gate
→ HFT primary copper
→ HFT core
→ HFT secondary copper
→ leakage / clamp / snubber / commutation
→ HV rectifier
→ HV bus capacitor
→ HV inverter
→ output filter
→ interconnect / terminal
```

### A 類需要實測 / 建模的量

```text
source Iavg / IRMS
100/120 Hz component
HF ripple
per-bank current
T1 primary IRMS
T2 primary IRMS
LV path Rdc/Rac
MOS conduction/switching loss
transformer copper/core loss
rectifier loss
HV DC-link ripple / capacitor RMS
HV inverter loss
```

若實測發現 ASP 低壓 source 幾乎沒有 100/120 Hz 分量，則「2ω buffer 可大量降低 LV RMS」不能直接成立，必須重新定位主要 loss lever。

---

## 3. Benchmark B — Direct High-Frequency-Link DC–AC

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

相較 A0/A1，省略完整：

```text
Rectifier → HV DC Bus → VSI
```

這是不能忽略的 modern benchmark。若候選 topology 只比傳統兩級式好，reviewer 仍可要求與 direct-HFL 方法比較。

### Xi'an line 的定位

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

因此未來若採 electric-field，不可把這個 energy-routing idea 本身當成新穎性。

正式數值、prototype 規格、DOI 與 successor 狀態仍需由 evidence pipeline 鎖定後引用。

---

## 4. Benchmark C — Non-Isolated Current-Distribution / High-Gain class

Working family:

```text
#04 Non-Isolated High-Gain DC/DC + VSI
```

對目前 extreme-LV 問題，公平版本不是單一 175 A high-gain cell，而是允許：

```text
12 V short bus
→ N-way current distribution
→ N × [switching + high-gain / coupled-L X1]
→ HV collective combine
→ HV energy node
→ X3
```

主要比較量：

```text
common-path R_eq
branch IRMS
MOS conduction / switching
inductor / coupled-inductor copper + core
leakage / clamp
rectifier / diode loss
capacitor ESR / charge redistribution
internal circulating current
```

Direct 12 V / 2 kW / ~400 V non-isolated high-gain hardware remains `OPEN_INTERSECTION / NOT DIRECT-SCALE VERIFIED` unless separately locked by evidence.

---

## 5. Candidate D — Working loss-routing architecture

Current working architecture is preserved as a hypothesis:

```text
12–24 Vdc
→ very-short common LV path
→ local bulk + HF decoupling
→ early distributed branch power cells
→ branch switching + candidate X1
→ reduced-current energy node
→ [optional active X2 2ω buffer]
→ X3
→ 220 Vac / 1φ
```

Detailed block-by-block added-loss audit is recorded in:

```text
research/11_WORKING_ARCHITECTURE_LOSS_AUDIT.md
```

Candidate D is **not** assumed superior.

### Required ablations

```text
D0 — active X2 Buffer OFF
D1 — active X2 Buffer ON
```

If D1 only lowers source/DC-link ripple but:

```text
P_buffer,loss + P_extra_circulation > P_LV,saved
```

then active X2 fails and must be removed or restructured.

If an electric-field version only removes HFT loss but:

```text
P_cap + P_circulating + P_extra_switch > P_HFT,saved
```

then the electric-field route fails or must be restructured.

---

## 6. Fair comparison matrix

Final comparison must at minimum include:

```text
                    A0: ASP real   A1: modular HFT   B: Direct HFL   C: Non-iso HG   D: Candidate
Vin                 matched        matched           matched         matched         matched
Pout                matched        matched           matched         matched         matched
Vout                matched        matched           matched         matched         matched
Isolation           explicit       explicit          explicit        explicit        explicit
Semiconductor       documented     comparable        comparable      comparable      comparable
I_common,RMS        measured/model model              model           model           measured/model
I_branch,RMS        measured/model model              model           model           measured/model
I_2ω                measured/model model              reported/model  model           measured/model
I_circulating       measured/model model              reported/model  model           measured/model
P_cond              decomposed     decomposed         decomposed      decomposed      decomposed
P_sw                decomposed     decomposed         decomposed      decomposed      decomposed
P_mag               decomposed     decomposed         decomposed      decomposed      N/A or remaining
P_cap               decomposed     decomposed         decomposed      decomposed      decomposed
P_rectifier         decomposed     decomposed         as applicable   decomposed      as applicable
P_buffer            if present     if present         if present      if present      decomposed
P_total             same boundary  same boundary      same boundary   same boundary   same boundary
```

若 boundary 無法匹配，該 paper / product datum 只能進：

```text
CONTEXT_ONLY
或
BOUNDED_TRADEOFF
```

不可做 direct scalar ranking。

---

## 7. Current benchmark rule

A proposed candidate must no longer pass only this test:

```text
Candidate < old generic #02 loss
```

It must eventually survive:

```text
Candidate
vs A0 actual ASP
vs A1 fair optimized magnetic benchmark
vs Direct HFL
vs matched non-isolated high-gain benchmark when applicable
```

Core rule remains:

```text
P_saved > P_added
```
