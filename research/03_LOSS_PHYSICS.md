# 03 — Loss Physics 與低壓縮放

Status date: 2026-08-17
Purpose: separate physical energy flow from irreversible loss

## 1. 基本關係

```text
P = V × I
I = P / V
P_cond = I_RMS² × R
P_R = V_RMS² / R
```

對低壓大電流 converter，不能只看平均電流；導通相關損耗由 `I_RMS²R` 決定。

## 2. 12 V 為何不是單純較低電壓

固定 2 kW：

```text
12 V → 166.7 A ideal
24 V → 83.3 A ideal
48 V → 41.7 A ideal
```

若固定等效電阻不變，從 48 V 降到 12 V：

```text
I × 4
P_cond × 16
```

因此在固定功率下：

```text
I ∝ 1 / V
P_cond ∝ 1 / V²    (R fixed)
```

這是目前研究最重要的 scaling anchor。

## 3. 可接受等效電阻預算

以 2 kW、95% 效率估算輸入電流，若低壓導通損失上限只允許輸出功率的 1%（20 W）：

```text
Vin   Iin@95%   Req,max for 20 W
48 V   43.9 A      ≈ 10.4 mΩ
24 V   87.7 A      ≈ 2.60 mΩ
12 V  175.4 A      ≈ 0.65 mΩ
```

12 V / 3 kW 若只允許 30 W conduction loss，理想 250 A 對應：

```text
Req,max ≈ 30 / 250² ≈ 0.48 mΩ
```

若以 95% 輸入電流估算，允許值會更低。

這說明 12 V/kW 級的 full-current path budget 極嚴格。

## 4. 電流分量分解

低壓側電流概念上可分為：

```text
i_LV = I_avg
     + i_2ω
     + i_switching
     + i_circulating
     + i_reactive
     + i_commutation
```

若各 AC 分量彼此正交或以頻域分解處理，可用：

```text
I_LV,RMS² = I_avg²
          + I_2ω,RMS²
          + I_switching,RMS²
          + I_circulating,RMS²
          + I_reactive,RMS²
          + I_commutation,RMS²
          + cross terms when not orthogonal
```

研究真正能改變的不是來源端必要的平均功率電流，而是哪些額外 RMS 分量也穿越最昂貴的低壓共用路徑。

## 5. 單相 2ω 功率脈動

對 unity-PF 單相輸出：

```text
p_out(t) = P_avg [1 - cos(2ωt)]
```

若 DC source 被迫直接提供完整瞬時功率，固定 source voltage 下可寫成理想化電流：

```text
i_source(t) = I_avg [1 - cos(2ωt)]
```

其 RMS：

```text
I_RMS = sqrt(3/2) × I_avg ≈ 1.225 I_avg
```

因此同一 R 下：

```text
P_cond = I_RMS²R = 1.5 I_avg²R
```

也就是相對純平均 DC current，完整 2ω 分量通過同一低壓電阻時，理想化 conduction loss 增加 50%。

注意：這是機制上限／比較模型，不代表所有實際 inverter 的 source current 都必然具有完整該波形；實際值必須由 DC-link capacitance、控制與 power-path dynamics 驗證。

## 6. 2ω Buffer 的能量式

定義：

```text
P_buf > 0 代表 Buffer 放電至 DC link / load
```

若 source 只提供平均功率：

```text
P_source ≈ P_avg
P_buf = P_out - P_source
      = -P_avg cos(2ωt)
```

因此：

- `P_buf < 0`：Buffer 充電；
- `P_buf > 0`：Buffer 放電。

能量關係：

```text
dE_buf / dt = -P_buf
```

2ω energy swing amplitude：

```text
ΔE_amp = P / (2ω)
```

peak-to-peak：

```text
ΔE_pp = P / ω
```

2 kW、60 Hz：

```text
ΔE_amp ≈ 2.65 J
ΔE_pp  ≈ 5.31 J
```

若以 capacitor 在 `Vmin` 到 `Vmax` 間承擔完整 peak-to-peak energy swing：

```text
C = 2 ΔE_pp / (Vmax² - Vmin²)
```

例如 360–440 V：

```text
C ≈ 166 µF
```

## 7. Loss 與能量流不可混為一談

### 7.1 不可逆耗散

```text
MOS RDS(on)
PCB / busbar / connector I²R
transformer / inductor copper loss
core loss
capacitor ESR / dielectric loss
diode conduction / reverse recovery
gate / auxiliary power
```

這些已變成熱，不能靠「雙向」直接回收。

### 7.2 可被回收但常被耗散的換流能量

```text
leakage inductance energy
MOS Coss energy
snubber / clamp energy
部分 commutation energy
```

可透過 active clamp、resonance、ZVS/ZCS 或 energy recycling 改變其去向。

### 7.3 本質不是 Loss 的往返能量

```text
2ω power pulsation
reactive load energy
resonant tank energy
buffer energy fluctuation
```

這些本身不是 loss；問題是其往返造成額外 RMS current，最後在 RDS(on)、銅與 ESR 中變成熱。

## 8. Loss Migration

本研究固定使用以下觀念：

> 拿掉一種損耗，通常不代表損耗消失；它可能遷移到另一個元件或電流分量。

典型例子：

```text
ZVS ↓ switching loss
    but may ↑ resonant/circulating RMS

APD ↓ 2ω current in main path
    but adds buffer conduction/switching loss

Electric-field isolation ↓ core/winding loss
    but may ↑ capacitor RMS/ESR, reactive VA, common-mode and balancing burden

Parallel MOSFET ↓ effective RDS(on)
    but ↑ gate drive, layout, sharing and parasitic complexity
```

因此評估必須使用：

```text
P_saved > P_added
```

而不是「某一個 loss bucket 下降」即判定成功。
