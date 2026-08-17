# 01 — 研究範圍與問題定義

Status date: 2026-08-17
Novelty status: `NOT_ESTABLISHED`

## 1. 一般研究範圍

目前研究邊界固定為：

```text
Vin     = 12–24 Vdc
Pout    = 1–3 kW
Vout    = 220 Vac
Phase   = single phase / 1φ
Grid/f  = 以 60 Hz 為主要分析點，必要時保留 50 Hz 一般式
```

主要壓力錨點不是整個研究範圍，而是：

```text
12 V / 2 kW
```

理想平均輸入電流：

```text
I = P / V = 2000 / 12 ≈ 166.7 A
```

若以 95% 效率反推輸入電流：

```text
Iin ≈ 2000 / (12 × 0.95) ≈ 175.4 A
```

12 V / 3 kW 時理想電流約 250 A。這使研究進入 extreme-low-voltage / high-current regime，而不是一般 48 V 或數百伏 DC-link 的縮小版。

## 2. 研究不是什麼

本研究不以以下單一項目作為主題或新穎性：

- 再發明一般 Boost；
- 再發明 IPOS；
- 單純把 HFT 換成 capacitor；
- 單純加入 UPS / BESS 功能；
- 單純加入雙向 DC/DC；
- 單純加入 APD / PPB；
- 單純做 AI / MCU adaptive control；
- 單純追求最高效率數字；
- 因搜尋不到完整匹配就宣稱全球首創。

## 3. 核心物理問題

研究的核心不是「怎麼把 12 V 升到 220 Vac」；已有多種拓撲可以做到。

核心問題是：

> 在 12–24 V、1–3 kW 的單相 DC→AC 系統中，平均主功率、2 倍線頻脈動能量、反應能量、諧振／循環能量與換流能量，應該在哪裡完成第一次大倍率阻抗轉換、在哪裡循環、在哪裡暫存，才能讓低壓百安培路徑承受最少的不必要 RMS 電流，並使整機總損耗最低？

一句話工作表述：

> **不是研究怎麼升壓，而是研究 12 V 的能量怎麼走，才最少變成熱。**

## 4. 三個結構座標

研究使用三個位置變數描述架構：

```text
X1 = 第一次主要阻抗轉換位置
X2 = 2ω / reactive / recoverable energy 的 buffer / recycling 位置
X3 = AC waveform synthesis 位置
```

研究不預設 X1、X2、X3 必須分開，也不預設一定整合。要由損耗與應力驗證決定。

## 5. 主要最佳化目標

第一層：

```text
min I_LV,RMS
```

第二層：

```text
min I_circulating,RMS
```

最終目標：

```text
min P_loss,total
```

可用一般化目標函數表示：

```text
J = Σ(I_RMS,k² R_k)
  + ΣP_switching
  + ΣP_magnetic
  + ΣP_capacitor
  + P_auxiliary
```

任何新增支路或 Buffer 都必須滿足：

```text
P_saved > P_added
```

否則即使某一局部 ripple 下降，也不能視為系統改進。

## 6. 研究階段

目前階段：

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

目前尚未形成可正式主張的新拓撲，也尚未建立 novelty。
