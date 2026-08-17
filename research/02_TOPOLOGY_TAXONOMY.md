# 02 — 低壓 DC→AC 拓撲分類

Status date: 2026-08-17
Classification type: working research taxonomy

## 1. 分類原則

這份分類不是宣稱全世界只能分成九種，而是本研究用來比較「主功率路徑」的工作分類。

判定一個主家族的核心是：

> 能量從低壓 DC 到單相 AC 的主要 power path 是否不同？

以下特徵原則上視為正交設計維度，不因單獨出現就自動變成新的編號家族：

- IPOS / ISOP；
- modular / multicell；
- current sharing；
- matrix connection；
- capacitive isolation / CPT / electric-field coupling；
- active power decoupling；
- partial-power processing；
- bidirectional buffer；
- ZVS / ZCS modulation。

## 2. 九個主功率路徑家族

### #01 低頻變壓器式逆變器

```text
LV DC → H-Bridge → 50/60 Hz Transformer → AC
```

優點：結構直觀，可同時升壓與隔離。

主要代價：低壓大電流存在時間長；低頻磁性體積與銅損大。

### #02 高頻磁隔離兩級式

```text
LV DC → HF Switching → HFT → Rectifier → HV DC Bus → VSI → AC
```

中文：

```text
低壓直流
→ 高頻切換
→ 高頻變壓器
→ 整流器
→ 高壓直流母線
→ 電壓源型逆變器
→ 交流輸出
```

ASP 類產品屬於本研究的主要實際 Benchmark。

### #03 Active-HFT / DAB + VSI

```text
LV DC ↔ active isolated HF stage / DAB ↔ HV DC Bus → VSI → AC
```

與 #02 的差別是高頻隔離級本身採 active bridge / bidirectional power-transfer mechanism，而不只是單向 HF switching + diode rectification。

### #04 非隔離高增益 DC/DC + VSI

```text
LV DC → high-gain DC/DC → HV DC Bus → VSI → AC
```

可包含：

```text
Boost
Interleaved Boost
Coupled-Inductor
Voltage Multiplier
Switched-Capacitor Hybrid
Quadratic / Cubic
其他 high-gain cells
```

主要風險是高 gain 下的 duty、RMS、switch stress、passive stress 與 circulation。

### #05 雙向 DC/DC + VSI

```text
Battery / LV DC ↔ Bidirectional DC/DC ↔ HV DC Bus ↔ VSI ↔ AC
```

常見於 UPS / PCS / BESS。這個家族本身已成熟；「雙向」不是本研究的新穎性來源。

### #06 單級升降壓逆變器

```text
LV DC → Single-Stage Boost / Buck-Boost Inverter → AC
```

升壓與 AC 合成在同一主要功率級內完成。

主要代價：器件 RMS / peak current、2ω energy handling、控制與換流複雜度。

### #07 Z-Source / Quasi-Z-Source Inverter

```text
LV DC → Impedance Network → Inverter → AC
```

利用 shoot-through / impedance-network dynamics 將升壓功能整合到 inverter。

### #08 Switched-Capacitor / Multilevel 主路徑

```text
LV DC → capacitor charge/reconfiguration/stacking → multilevel or boosted AC
```

主要代價：charge redistribution、ESR、switch count、balancing、capacitor RMS。

### #09 直接式高頻鏈 DC–AC

```text
LV DC → HF Bridge → HF Link → Bidirectional / Matrix / Cycloconverter Stage → AC
```

關鍵特徵是避免完整：

```text
HF AC → Rectifier → HV DC Bus → VSI → AC
```

而由高頻鏈後端直接合成低頻 AC。

## 3. 西安研究的定位

目前追蹤的西安交大 48 V→220 Vac single-phase high-frequency-link inverter + differential AC-side active power decoupling，應歸入：

```text
#09 Direct High-Frequency-Link DC–AC
```

它是 #09 的重要近期演進，不應寫成「2025/2026 才發明第九類」。

其研究價值在於：

```text
48 V DC
→ HF bridge
→ HFT
→ differential cycloconverter / direct AC stage
→ 220 Vac
```

並利用 AC-side differential/common-mode freedom 處理 double-line-frequency energy。

正式論文引用前，出版資訊與數值需重新通過 evidence pipeline 驗證。

## 4. Electric-field 應如何分類

Electric-field / capacitive isolation 不應自動稱為第十類。

例如：

```text
12 V → capacitively isolated DC/DC → HV DC Bus → VSI → AC
```

從主功率路徑看，可能仍是 #02 / #03 的 capacitive-isolation variant。

而：

```text
12 V → capacitive HF link → direct AC synthesis → AC
```

可能是 #09 的 electric-field variant。

只有當未來候選電路真正改變平均功率與 2ω 能量的結構路徑，形成不同於上述家族的 power structure，才有理由討論新的主家族。

因此目前狀態：

```text
Candidate #10 = NOT ASSIGNED
```

不得因使用 electric field + buffer 就提前編成新家族。
