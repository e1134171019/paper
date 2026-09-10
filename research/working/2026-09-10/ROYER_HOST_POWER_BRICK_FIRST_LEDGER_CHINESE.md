# Royer Host + 功率積木：第一輪功率帳本

狀態：**FIRST-ORDER POWER SCREEN / 非 PSIM / 非實機 / Novelty 未建立**

> Governance note：本文件是 2026-09-10 對話中的 working-branch 分析，不覆寫 `main` 目前由 File64 鎖定的 physical-measurement mainline。Candidate #10 仍為 `HOLD / NOT_ASSIGNED`。

## 1. 研究方法修正

本輪恢復原本的研究宿主：

```text
Royer Host Power Cell
= 主功率 MOS
+ center-tapped primary
+ HFT
+ magnetic feedback / self-oscillation
```

Royer 不再只被當成 timing 插件。

其他拓撲被拆成 **Power Bricks** 加到 Royer Host 周圍：

```text
Royer Host
├─ Early Split / Multi-cell
├─ Multi-primary / series-secondary magnetic
├─ Current-fed
├─ Resonant / impedance shaping
└─ Capacitive voltage stacking
```

本輪只問：**每一塊到底處理多少功率、電流與電壓；是否值得留到下一輪。**

## 2. 固定功率邊界

```text
Vin = 12 V
Pout = 2000 W
eta_target = 95 %
Pin_target ≈ 2105.3 W
Iin,total ≈ 175.44 A
HV screening node = 336 V
I_HV,out ≈ 5.952 A
```

336 V 只是本輪 X1 高壓節點 screening anchor，不代表最終硬體已定版。

## 3. Royer Host 本身

單一 Royer Host 若全部功率都走同一低壓 Cell：

```text
12 V × ~175.4 A → ~2.105 kW input throughput
```

若假設 HFT secondary 直接建立 336-V 級 HF/HV node，忽略 resonant gain 等修正，effective voltage ratio 的一階量級約：

```text
336 / 12 ≈ 28
```

這是 RH0 reference。

## 4. 第一個 Power Brick：3-way Royer split + secondary series

不是把 Royer 拿掉，而是把一顆 Host 複製成 3 個 power cells：

```text
                    12 V
                     │
          ┌──────────┼──────────┐
          │          │          │
      Royer-A    Royer-B    Royer-C
          │          │          │
        HFT-A      HFT-B      HFT-C
          │          │          │
          └──── secondary series ───→ 336 V
```

在 equal sharing 下：

```text
Iin/cell ≈ 58.48 A
Pin/cell ≈ 701.8 W
Pout/cell ≈ 666.7 W
```

series secondary 的總電流相同：

```text
I_HV ≈ 5.952 A
```

每顆 transformer 只需要貢獻約：

```text
336 / 3 = 112 V
```

所以每 Cell 一階 effective magnetic ratio：

```text
112 / 12 ≈ 9.33
```

相較單 Cell 的約 28，這個積木真正改變的是「每個磁性 Cell 所需的電壓轉換份額」與低壓實體電流分布。

但：**3-cell / IPOS / series-secondary 本身不是新穎性。**

## 5. Current-fed Brick：它是 full-power series brick

若每 Cell 前加入 current-fed choke：

```text
12 V source → Lf_i → Royer primary cell
```

那 `Lf_i` 不是小訊號元件。每個 `Lf_i` 都要承受約：

```text
58.5 A
~702 W input throughput
```

第一階只算 DCR：

```text
P_Lf,Cu,total = N × Icell² × DCRbranch
```

N=3 時：

- DCR = 0.10 mΩ/branch → 約 1.03 W
- DCR = 0.25 mΩ/branch → 約 2.56 W
- DCR = 0.50 mΩ/branch → 約 5.13 W
- DCR = 1.00 mΩ/branch → 約 10.26 W

這還沒有算 core loss、ripple RMS、clamp、switch stress。

因此 current-fed 不是「免費 gain」。下一輪只有在它節省的 switching/magnetic/turns-ratio burden > 這些新增損耗時才保留。

## 6. Resonant Brick：主要敵人是 reactive RMS

若 resonant current RMS 相對原本主路徑變成：

```text
I_rms,new = k × I_rms,base
```

所有純電阻型 loss 約乘：

```text
k²
```

例如：

- k=1.05 → I²R +10.25%
- k=1.10 → I²R +21%
- k=1.25 → I²R +56.25%
- k=1.50 → I²R +125%

所以 LLC/LCL/resonant brick 只有在：

```text
saved switching/Coss/snubber loss
>
added reactive RMS + resonant copper/ESR/core loss
```

時才值得留。

## 7. Capacitive Gain Brick：在 12-V 端的功率帳很嚴苛

對 switched-cap / flying-cap，若某 capacitor brick 以電壓步階 `Vstep`、頻率 `fs` 搬運 `Pcap`：

```text
Q_per_cycle ≈ Pcap / (fs × Vstep)
```

如果它在 12-V 級節點處理完整 2 kW，fs=50 kHz：

```text
Q/cycle ≈ 3.333 mC
equivalent average charge-transfer current ≈ 166.7 A
```

純電容不會讓 12-V / 2-kW 的百安培物理條件消失。若 3-way split，等效平均仍約 55.6 A/cell，而實際 capacitor current 還可能更脈衝化，所以 RMS 更高。

因此 Flying-Cap / Charge-Pump brick 比較有希望放在「已經做過第一次電壓提升」之後，而不是直接放在最前面的 12-V 百安培節點。

## 8. 第一輪候選收斂

### RH0 — Royer Host only
保留作 reference。

### RH1 — 3-cell Royer + series secondary
保留。每 Cell 約 58.5 A；magnetic voltage share 約 112 V/cell；effective ratio 約 9.33。

### RH2 — RH1 + Resonant
保留，條件式。先用 `k²` 檢查 reactive RMS 代價。

### RH3 — RH1 + Current-fed
保留，條件式。Current-fed choke 是 full-power / full-current brick。

### RH4 — RH1 + Capacitive gain at 12 V
降級 / HOLD。百安培 charge-transfer risk 太直接。

### RH5 — RH1 + Current-fed + Resonant
列為**主功率積木組合候選**。

### RH6 — RH1 + Resonant + Capacitive gain after partial step-up
列為**第二功率積木組合候選**。關鍵是把 capacitive gain 移到較高 V / 較低 I 的位置。

## 9. 下一 Gate

暫時不要再深入 Royer exact gate sequence，也不要直接進 PSIM。

下一輪只做：

```text
RH1 vs RH5 vs RH6
→ matched power/loss ledger
```

每組至少填：

```text
Node
Vin/Vout
Iavg/Irms
P_real
P_reactive
effective gain
MOS conduction
switching/Coss
magnetic copper/core
choke loss
capacitor ESR/redistribution
added interconnect
```

然後才決定哪一組值得形成正式 X1 候選。
