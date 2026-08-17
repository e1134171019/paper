# 低壓大電流 DC→AC — Current Research State

> 狀態日期：2026-08-17  
> 文件用途：只保存「現在研究走到哪裡」。詳細推理拆分到 `research/01_...08_...`。  
> Novelty：`NOT_ESTABLISHED`。搜尋不到完整匹配不得直接寫成 Research Gap。

## 1. Current phase

```text
Literature Closure
        ↓
Physical Gap Validation   ← CURRENT
        ↓
Topology Synthesis
        ↓
Simulation Validation
        ↓
Hardware Validation
```

目前已經不是泛搜「哪個拓撲效率最高」，而是開始驗證 extreme-low-voltage/high-current 條件是否真的造成新的 loss/stress boundary。

## 2. Research envelope

```text
Vin     = 12–24 Vdc
Pout    = 1–3 kW
Vout    = 220 Vac
Phase   = single phase / 1φ
Primary anchor = 12 V / 2 kW
```

12 V / 2 kW 的理想平均電流：

```text
I = 2000 / 12 ≈ 166.7 A
```

這個 operating point 用來代表百安培低壓路徑的極端 `I²R` 壓力，不代表研究只限 12 V / 2 kW。

## 3. Core research question

> **不是研究怎麼升壓，而是研究 12 V 的能量怎麼走，才最少變成熱。**

研究把系統內能量分成：

```text
average real power
2ω pulsating power
reactive energy
switching / resonant / circulating energy
leakage / commutation energy
```

真正問題是：哪些非必要 RMS 電流穿越最昂貴的低壓共用路徑，以及第一次阻抗轉換與局部能量緩衝應該在哪裡發生。

使用三個結構座標：

```text
X1 = first major impedance transformation
X2 = local 2ω / bidirectional buffer / recycling point
X3 = AC synthesis point
```

## 4. Physical anchor

固定功率時：

```text
I ∝ 1/V
P_cond = I_RMS²R
```

因此相同功率與相同 R 下，48 V → 12 V：

```text
current × 4
conduction loss × 16
```

若完整單相 2ω power pulsation 直接反映到固定電壓 DC source，理想化模型：

```text
i_source(t) = I_avg [1 - cos(2ωt)]
I_RMS = sqrt(3/2) I_avg
```

同一 R 下，conduction loss 相對純平均 DC current 可增加到：

```text
1.5 × I_avg²R
```

這是目前要用 PLECS 驗證的機制假設，不代表所有現有 inverter 都必然具有完整此波形。

## 5. Topology map

目前使用九個主 power-path family：

```text
#01 Low-Frequency Transformer Inverter
#02 HFT + Rectifier + HV DC Bus + VSI
#03 Active-HFT / DAB + VSI
#04 Non-Isolated High-Gain DC/DC + VSI
#05 Bidirectional DC/DC + VSI
#06 Single-Stage Boost / Buck-Boost Inverter
#07 Z-Source / Quasi-Z-Source
#08 Switched-Capacitor / Multilevel Main Path
#09 Direct High-Frequency-Link DC–AC
```

`IPOS / modular / matrix / capacitive isolation / current sharing / active buffer / partial power` 視為正交設計維度，不自動增加新的 topology-family 編號。

西安交大的 48 V→220 Vac high-frequency-link + differential AC-side APD 研究屬 #09 的近期重要演進，不是第九類的歷史起點。

## 6. What prior art has already closed

以下 broad concepts 不能單獨當 novelty：

```text
High-gain conversion
IPOS / modular conversion
DAB / active isolated conversion
Direct high-frequency-link DC–AC
Bidirectional battery/HV-bus conversion
APD / PPB
partial-power / series-stacked buffer
HF-link ripple port / integrated buffer
CPT / capacitive isolation
kW-class capacitive conversion
capacitively isolated inverter
high-ratio capacitively isolated conversion
```

所以：

```text
Electric-field + Buffer
```

本身不是研究缺口。

## 7. Current open intersection

目前 targeted search 尚未找到完整匹配：

```text
12–24 Vdc
+ 1–3 kW
+ 220 Vac / 1φ
+ electric-field / capacitive main conversion
+ intentional bidirectional 2ω energy routing
+ explicit LV-RMS / total-loss minimization objective
```

狀態只能寫：

```text
OPEN_INTERSECTION
NOVELTY_NOT_ESTABLISHED
```

## 8. Current hypothesis

希望形成的能量路徑：

```text
Average Energy:
Source → Load

Pulsating 2ω Energy:
Local Buffer ↔ Load / reduced-current energy node
```

盡量避免：

```text
2ω energy ↔ 12 V source full-current path
```

若採 electric-field coupling，成立條件不是「拿掉 HFT」，而是：

```text
P_mag,saved
+ P_LV,RMS,saved
+ P_switching/rectifier,saved
>
P_cap
+ P_circulating
+ P_extra_switches
+ P_auxiliary
```

也就是所有改善都必須通過 Loss Migration 檢查。

## 9. Required benchmarks

```text
Benchmark A
#02 HFT + Rectifier + HV Bus + VSI
(ASP-class real-product baseline)

Benchmark B
#09 Direct High-Frequency-Link DC–AC
(Xi'an-type modern magnetic/HFL mechanism class)

Candidate C
Electric-field / energy-routing candidate
```

Candidate C 內部至少要做：

```text
Buffer OFF vs Buffer ON
```

## 10. Next validation gate

第一個主要模擬工具：

```text
PLECS
```

先不用完整 electric-field topology，而是建立：

```text
12–24 Vdc
→ idealized impedance transformation
→ HV / reduced-current energy node
→ single-phase inverter
→ 220 Vac
```

比較：

```text
Buffer OFF
vs
Buffer ON
```

必量：

```text
I_source,avg
I_source,RMS
I_source,2ω
I_buffer,RMS
P_saved from LV I²R
P_buffer,added
```

Go condition：

```text
P_saved > P_buffer,added
```

若這一關不成立，不能因為偏好 Electric-field 就繼續堆拓撲。

## 11. Detailed research documents

- [`01_SCOPE.md`](01_SCOPE.md) — 研究範圍、X1/X2/X3、最佳化目標。
- [`02_TOPOLOGY_TAXONOMY.md`](02_TOPOLOGY_TAXONOMY.md) — 九個主功率路徑家族與西安定位。
- [`03_LOSS_PHYSICS.md`](03_LOSS_PHYSICS.md) — `I²R`、RMS、2ω、Loss Migration 與 scaling。
- [`04_PRIOR_ART_CLOSURE.md`](04_PRIOR_ART_CLOSURE.md) — CLOSED / OPEN_INTERSECTION / novelty boundary。
- [`05_RESEARCH_HYPOTHESIS.md`](05_RESEARCH_HYPOTHESIS.md) — bidirectional 2ω routing 與 electric-field candidate hypothesis。
- [`06_VALIDATION_PLAN.md`](06_VALIDATION_PLAN.md) — PLECS → LTspice → Maxwell/Q3D → hardware。
- [`07_BENCHMARKS.md`](07_BENCHMARKS.md) — ASP、Direct HFL 與 candidate 的比較邊界。
- [`08_DECISION_LOG.md`](08_DECISION_LOG.md) — 保留／淘汰方向的理由與日期。

Evidence/acquisition layer remains under:

- [`batches/`](batches/)
- [`contracts/`](contracts/)

## 12. Current decision state

```text
Research target:
    low-voltage high-current DC → single-phase AC

General scale:
    12–24 V / 1–3 kW / 220 Vac

Primary anchor:
    12 V / 2 kW / ~166.7 A ideal

Current physical question:
    which energy/current components should cross the LV full-current domain?

Candidate mechanism:
    early impedance transformation
    + local bidirectional 2ω energy routing
    + possible electric-field main conversion

Novelty:
    NOT ESTABLISHED

Next action:
    PLECS mechanism validation before detailed topology synthesis
```
