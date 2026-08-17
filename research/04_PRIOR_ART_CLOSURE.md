# 04 — Prior-Art Closure Map

Status date: 2026-08-17
Novelty status: `NOT_ESTABLISHED`

## 1. 狀態定義

```text
CLOSED
= broad claim clearly has prior art.

PARTIALLY_CLOSED
= important adjacent/partial intersection exists; only narrower mechanism may remain.

OPEN_INTERSECTION
= current targeted search has not found a complete match.

NOT_ESTABLISHED
= novelty cannot yet be claimed.
```

搜尋不到完整匹配只代表下一輪搜尋與驗證需求，不能直接等同 Research Gap。

## 2. 已關閉的廣義主張

以下項目不得單獨當作 novelty：

```text
High-gain DC/DC
Input-parallel / output-series
Primary-parallel / secondary-series
Matrix transformer
Interleaving
Coupled-inductor high gain
Switched-capacitor high gain
Voltage multiplier
Quadratic / cubic gain
DAB / active isolated bridge
Single-stage boost inverter
Z-source / quasi-Z-source
High-frequency-link direct DC/AC
Bidirectional battery ↔ HV bus
UPS / BESS bidirectional conversion
APD / active power decoupling
PPB / power pulsation buffer
Series-connected / series-stacked buffer
Partial-power active buffer
Ripple port / ripple steering
HF-link integrated buffer
Transformer-integrated power decoupling
Capacitive power transfer / electric-field transfer
Capacitive galvanic isolation
kW-class capacitive conversion
High-conversion-ratio capacitively isolated conversion
```

## 3. Electric-field 研究線的 closure

### 3.1 kW electric-field / capacitive conversion

Status: `CLOSED`

已有 kW 級 capacitive-isolated / CPT / capacitor-transformer 類硬體工作，因此不得寫：

> electric-field power conversion has not been demonstrated at kW level.

### 3.2 Capacitively isolated inverter

Status: `CLOSED as broad concept`

2025 已追到 capacitively isolated inverter 研究，因此不得以「第一次把 capacitive isolation 用於 inverter」作為 broad claim。

目前追蹤的 inverter 工作是否為完整 hardware、其性能邊界與 isolation implementation，正式引用前仍需由 evidence pipeline 鎖定。

### 3.3 High conversion ratio + capacitive isolation

Status: `CLOSED as broad concept / active research`

MIT/Coday 等研究線已建立 capacitively-isolated hybrid switched-capacitor / high-conversion-ratio family，因此不能把「高轉換比 electric-field topology」本身視為空白。

### 3.4 Bidirectional capacitive power flow

Status: `PARTIALLY_CLOSED`

雙向 capacitive power transfer / capacitive converter 不是可安全宣稱的新概念。真正可能剩下的是特定 low-voltage extreme-current energy-routing mechanism，而不是 bidirectionality 本身。

## 4. 2ω / Buffer 研究線的 closure

以下 broad concepts 均視為 `CLOSED`：

```text
Active Power Decoupling
Power Pulsation Buffer
Series Energy Buffer
Series-Stacked Buffer
Multilevel Energy Buffer
Partial-Power Buffer
Ripple Port at DC / AC / HF link
Transformer-integrated decoupling
DAB + active energy buffer
Matrix converter + integrated buffer
```

因此：

```text
Electric-field + Buffer
```

本身不能作為 novelty sentence。

## 5. 西安 High-Frequency-Link 近鄰線

目前追蹤到 48 V→220 Vac single-phase high-frequency-link inverter，利用 differential AC output / AC-side decoupling 處理 double-line-frequency energy。

Status:

```text
48 V → 220 Vac + HFT + direct HFL AC synthesis + integrated APD
= CLOSED as a magnetic benchmark direction
```

這代表「讓 2ω 不必完整穿回低壓 source / HF stage」的思想已有強 prior art。

它對本研究的意義是建立 closest magnetic benchmark，而不是證明我們沒有空間。

正式數值與 2026 successor bibliographic metadata 必須再由 evidence pipeline 驗證後引用。

## 6. Extreme-low-voltage electric-field scale

目前 targeted search 所呈現的工作分布：

```text
12/24 V electric-field / CPT
→ 常見於低功率或數十瓦等級

kW electric-field / capacitive isolation
→ 常見於數百伏條件
```

目前尚未在 targeted search 中找到完整：

```text
12–24 V input
+ 1–3 kW
+ true capacitive/electric-field main conversion
+ single-phase 220 Vac output
```

但此狀態只能寫：

```text
OPEN_INTERSECTION
```

不能寫：

```text
FIRST / NEVER DONE / NOVEL
```

## 7. 目前最窄候選交集

```text
12–24 Vdc
+ 1–3 kW
+ 220 Vac / 1φ
+ electric-field / capacitive main power conversion
+ intentional bidirectional 2ω energy routing
+ explicit objective to minimize I_LV,RMS and total loss
```

Current status:

```text
OPEN_INTERSECTION
NOVELTY_NOT_ESTABLISHED
```

## 8. 候選 Gap 的較安全表述

目前較安全的研究問題不是：

> 沒有人做過電場逆變器。

而是：

> Existing capacitive-isolated and active-power-decoupled converters are largely demonstrated outside the extreme-low-voltage/high-current regime. The unresolved question is whether, at 12–24 V and kW-class single-phase operation, the first impedance-transformation boundary and the twice-line-frequency energy-routing boundary can be structurally coordinated to reduce low-side RMS-current exposure and total loss without introducing larger capacitive/resonant/circulating losses.

中文：

> 既有電容隔離與主動功率解耦研究多數並非針對 12–24 V、kW 級百安培條件；目前要驗證的是：第一次阻抗轉換位置與二倍線頻能量路由位置能否在此極低壓大電流區共同配置，使低壓側 RMS 電流與總 Loss 下降，同時避免新增更大的電容、諧振與循環損耗。

這仍是 research question，不是 novelty claim。

## 9. 下一輪 closure 必須回答

```text
1. 有沒有 12/24 V、≥1 kW 的 capacitively isolated hardware？
2. 有沒有 12/24 V→220 Vac 的 capacitive-isolated direct inverter hardware？
3. 有沒有同時將 2ω buffer 與 capacitive isolation 主路徑整合？
4. 有沒有明確以 battery/LV source I_RMS reduction 為 contribution？
5. 有沒有對 low-side conduction loss、capacitor RMS/ESR、circulating current 做完整 breakdown？
6. scale from 48/100/400 V to 12 V 時，作者是否明確指出 current/stress limitation？
```

只有完成這些 closest-prior-art closure 後，才進入正式 novelty wording。
