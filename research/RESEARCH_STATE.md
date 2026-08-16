# 低壓大電流 DC↔AC 論文研究狀態

> 狀態日期：2026-08-16  
> 文件用途：保存目前研究推理、已排除方向、已知先行研究、候選缺口與下一步驗證計畫。  
> 注意：這是一份「研究工作記憶 / working state」，不是最終論文結論。任何「新穎性」都必須在完成 prior-art closure 後才能主張。

---

## 1. 研究核心

目前研究不是為了再發明一個一般性的 Boost、IPOS、CPT、BUS 或 UPS 架構，而是從低壓大電流條件出發，研究：

> 在 12 V、1–2 kW、約 100–200 A 的 DC→單相 AC 系統中，平均主功率、2 倍線頻脈動能量、反應能量、漏感 / 換流能量應該在哪裡完成阻抗轉換、在哪裡循環或暫存，才能使 12 V 低壓側的 RMS 電流暴露與全系統總 Loss 最低；並進一步判斷固定功率拓撲是否存在新的結構性解法。

研究層次目前定位在 **Topology Synthesis（功率級拓撲綜合）**，不是先做 MCU 動態選路徑，也不是先做 AI 控制。

---

## 2. 物理錨點：12 V / 2 kW

基本關係：

```text
P = V × I
I = P / V
P_loss = I_rms² × R
R = ρL / A
```

2 kW 時的理想電流：

```text
12 V  -> 166.7 A
48 V  -> 41.7 A
96 V  -> 20.8 A
192 V -> 10.4 A
```

同樣 1 mΩ 路徑電阻時：

```text
12 V / 166.7 A  -> 約 27.8 W
48 V / 41.7 A   -> 約 1.74 W
96 V / 20.8 A   -> 約 0.43 W
192 V / 10.4 A  -> 約 0.11 W
```

因此真正重要的不是「電流能不能消失」；12 V、2 kW 的來源端平均電流在物理上就是約 166.7 A。真正能被拓撲影響的是：

1. 166.7 A 在系統裡要存在多久、走多遠。
2. 哪些共享元件在第一次分流 / 阻抗轉換前仍承受全電流。
3. 除了平均主功率之外，額外的 ripple / circulating / reactive / commutation current 是否也穿過 12 V 側。
4. 第一次阻抗轉換點應該在哪裡。

---

## 3. ASP 產品基準架構

目前工作產品可作為實際 Benchmark。已知 ASP 系列為 12 V 輸入、約 700–3000 W 級，產品規格效率約 90–94%。

目前用於研究抽象的基準結構：

```text
12 V DC
  |
  | 低壓、大電流區
  v
MOS 高頻切換
  v
高頻磁性變壓器 HFT
  v
整流
  v
160–200 V DC Bus
  v
H-Bridge / SPWM
  v
LC Filter
  v
110 Vac
```

重要限制：

- 這是目前的系統抽象，不應在未讀完整原理圖前主張所有 ASP 機型都完全相同。
- ASP 的價值是作為真實低壓大電流產品 Benchmark，不是預設「傳統架構一定較差」。

---

## 4. 已知 8 類 DC→AC 拓撲族群

### A. 低頻變壓器式 inverter

```text
LV DC -> H-Bridge -> 50/60 Hz transformer -> AC
```

主要目的：簡單完成 DC/AC + 升壓 + 隔離。  
主要代價：低壓大電流存在時間長、低頻磁性體積與銅損大。

### B. 高頻磁隔離兩級式（ASP 類）

```text
LV DC -> HF switching -> HFT -> rectifier -> HV DC -> VSI -> AC
```

主要目的：更早完成阻抗轉換、縮小磁性體積。  
主要代價：LV MOS conduction、HFT copper/core、整流、第二級 inverter。

### C. 非隔離高增益 DC/DC + VSI

```text
LV DC -> Boost / Interleaved / Coupled-Inductor / SC / VM / Quadratic -> HV DC -> VSI -> AC
```

主要目的：不用傳統 HFT 完成高升壓。  
主要代價：高 Gain、極端 duty、inductor / MOS RMS current、circulating energy、元件數量。

### D. Single-Stage Boost / Buck-Boost Inverter

```text
LV DC -> single-stage boosting inverter -> AC
```

主要目的：把升壓與 AC 合成整合，減少完整轉換級。  
主要代價：RMS / peak current、器件 stress、2ω power、控制與換流複雜度。

### E. Z-Source / Quasi-Z-Source Inverter

```text
LV DC -> impedance network -> inverter -> AC
```

主要目的：利用 shoot-through 把 Boost 功能整合進 inverter。  
主要代價：L/C RMS、shoot-through current、circulating energy。

### F. Switched-Capacitor / Multilevel Inverter

```text
LV DC -> capacitor charge / series-parallel reconfiguration -> multilevel AC
```

主要目的：用電荷重組 / 多階電壓降低單一開關 stress、部分取代磁性升壓。  
主要代價：ESR、charge redistribution、switch count、balancing、capacitor RMS。

### G. High-Frequency-Link Direct AC

```text
LV DC -> HF bridge -> HFT -> bidirectional / matrix stage -> AC
```

主要目的：避免 `HF AC -> rectifier -> HV DC -> inverter -> AC` 的完整中間轉換。  
主要代價：雙向開關、commutation、高頻鏈 RMS、2ω energy handling。

### H. Modular / IPOS / Matrix / CPT 類

```text
LV DC
  -> parallel / distributed cells
  -> per-cell conversion
  -> high-side voltage stacking / series output
  -> AC or HV DC
```

主要目的：降低低壓側 current concentration、模組化、分散磁性 / 電場耦合。  
主要代價：cell count、driver、balancing、parasitics、auxiliary、circulating / CM / dielectric 等損失。

---

## 5. BUS / UPS / BESS 概念的正確定位

BUS 不是第 9 類新拓撲，也不是本論文要研究 UPS。

之所以引入 BUS 概念，是因為當研究 `Low-voltage DC -> AC` 時，需要追問：

> 如果系統內部允許某些能量雙向流動，那股反向能量到底從哪裡來、要去哪裡？

BUS / BESS 文獻已證明：

```text
Battery <-> bidirectional DC/DC <-> HV BUS <-> AC interface
```

以及 multi-port / UPS / storage / charge-discharge 都已成熟。因此：

- 「雙向 BUS」本身不是創新。
- 「DC↔AC」本身也不是創新。
- BUS 對本研究的價值是幫助建立 **內部能量流向** 的物理觀念。

研究仍以 DC→AC 為主，但可檢查某些內部支路是否必須具備局部雙向能量交換能力。

---

## 6. Loss 必須先按能量性質分類

不能把所有東西都叫做 Loss。

### 6.1 不可逆耗散（已變成熱，不能靠 BUS 回收）

```text
MOS RDS(on) conduction
PCB / busbar / connector I²R
Transformer / inductor copper loss
Core loss
Capacitor ESR
Dielectric loss
Diode conduction / reverse recovery
Gate / auxiliary power
```

這類只能靠降低 RMS current、R、磁通 / 頻率 stress、縮短路徑或改結構來減少。

### 6.2 原本可能被回收，但傳統電路可能把它耗散掉的能量

```text
Leakage inductance energy
MOS Coss energy
Snubber / clamp energy
部分 commutation energy
```

這類可用 active clamp、resonance、ZVS / ZCS、energy recycling 讓它在元件間交換，而不是每周期變成熱。

### 6.3 本質上不是 Loss，而是必須往返搬運的能量

```text
單相 2ω / 120 Hz power pulsation
Reactive load energy
Resonant tank energy
DC-link / buffer energy fluctuation
```

這類本身不是 Loss；真正的問題是它往返時增加 RMS current，最後在 RDS(on)、銅、ESR 中產生額外熱損失。

因此研究必須區分：

```text
I_real-power
I_ripple
I_circulating
I_reactive
I_commutation
```

導通損耗看的是 `I_rms² × R`，不是只看平均電流。

---

## 7. 目前形成的兩個核心研究問題

### Q1. 平均主功率：第一次阻抗轉換應該在哪裡？

原始問題：

```text
12 V / 2 kW
-> 約 166.7 A
-> 這個大電流應該走多遠？
-> 哪裡升壓才值得？
-> 升多少？
-> 新增 converter 的 Loss 是否小於被省下的 I²R？
```

簡化模型：

```text
P_total(Vint)
= (P/12)² * Rpre
+ (P/Vint)² * Rmid
+ (P/VHV)² * Rhigh
+ Pconv1
+ Pconv2
+ ...
```

這個問題不是預設 48 V、96 V 或某一拓撲一定最好，而是要由已知架構與 Loss matrix 推導。

### Q2. 非平均能量：應該在哪裡循環 / 暫存？

單相輸出有 2 倍線頻功率脈動。對純阻性負載：

```text
p_ac(t) = Pavg * [1 - cos(2ωt)]
```

因此平均功率與瞬時功率不相等。真正要問的是：

> 2ω、reactive、leakage、commutation 等非平均能量，應該留在高壓低電流側、HF link、transformer integration，還是穿回 12 V 側？

新的候選結構不應只是「再加一個 Buffer」，而應研究 **第一次阻抗轉換位置 X1** 與 **能量緩衝 / 回收位置 X2** 的相對配置與整合。

---

## 8. 已經被先行研究覆蓋，不可直接主張新穎性的項目

以下項目目前都應視為「已知」或「高度危險 prior art」：

- Input-Parallel / Output-Series (IPOS)。
- Primary-parallel / secondary-series magnetic conversion。
- Matrix transformer 用於 low-voltage high-current。
- Interleaved high-step-up。
- Coupled-inductor / switched-capacitor / voltage multiplier / quadratic / hybrid high-gain。
- Optimal intermediate voltage / variable DC-link voltage。
- Loss map / efficiency optimization。
- Physical PCB / busbar current path optimization。
- Single-stage boost inverter。
- Z-source / quasi-Z-source。
- High-frequency-link direct DC/AC。
- Bidirectional low-voltage battery ↔ HV bus。
- Single-stage bidirectional BESS inverter。
- Active Power Decoupling (APD)。
- Power Pulsation Buffer (PPB)。
- Partial-power active buffer。
- Series-stacked energy buffer。
- Multilevel Energy Buffer / Voltage Modulator (MEB)。
- Transformer-integrated power decoupling。
- DAB + active energy buffer。
- Matrix converter + center-tapped transformer + buffer。
- Ripple steering / current ripple suppression。
- CPT / Capacitor Transformer / electric-field power transfer。
- Magnetic-vs-capacitive mechanism comparison。

結論：

> 不能以「有 Buffer」、「雙向」、「IPOS」、「CPT」、「最佳中間電壓」、「低壓側分流」、「2ω decoupling」任何單一項目作為新穎性。

---

## 9. 關鍵先行研究清單

以下是目前最需要持續保留的 closest prior art。未列 DOI 的項目應在正式引用前再次確認出版資訊。

### 9.1 低壓高電流 / Primary-Parallel Secondary-Series

**Z. Ouyang et al.**, “Analysis and Design of Fully Integrated Planar Magnetics for Primary-Parallel Isolated Boost Converter,” IEEE Transactions on Industrial Electronics, 2013.  
DOI: `10.1109/TIE.2012.2186777`

重點：20–50 V -> 400 V、2 kW；primary-parallel / secondary-series；整合 planar magnetics；已直接證明「低壓分流 + 高壓疊壓」不是空白。

### 9.2 最佳中間電壓

**H. Zhang, S.-J. Park**, “Efficiency Optimization Method for Cascaded Two-Stage Boost Converter,” IEEE Access, 2022.  
DOI: `10.1109/ACCESS.2022.3175890`

重點：Optimal Intermediate Voltage Tracking (OIVT)；因此「找最佳 Vint」本身不是新穎性。

### 9.3 12 V / 400 V 多級 trade-off 近似案例

**L. Zhu et al.**, “Two-stage vs One-stage Design for A Bidirectional 400V/12V 6kW Auxiliary Power Module in Electric Vehicles,” IEEE ITEC, 2020.  
DOI: `10.1109/ITEC48692.2020.9161459`

重點：400 V / 12 V、低壓端數百安培；證明「增加級數一定更差」是不成立的，stage count 必須由 loss / density / operating range 決定。

### 9.4 CPT 高內部電壓 stress

**J. Lian et al.**, “Design of a Double-Sided LCLC-Compensated Capacitive Power Transfer System With Predesigned Coupler Plate Voltage Stresses,” IEEE JESTPE.  
DOI: `10.1109/JESTPE.2020.3030657`

重點：CPT 即使耦合良好，也可能因小耦合電容產生很高 plate voltage stress；不能只看「無磁芯」。

### 9.5 DAB DC/AC + ripple steering

**J. You et al.**, “An Active Power Decoupling Method for Single Phase DC/AC DAB Converters,” IEEE Access, 2019.  
DOI: `10.1109/ACCESS.2019.2893286`

重點：在 primary side 整合 ripple reduction，降低 DC source 的 2 倍線頻 ripple；已有「局部雙向 / ripple steering」思想。

### 9.6 Multilevel Energy Buffer / Voltage Modulator (MEB)

**M. Chen, K. K. Afridi, D. J. Perreault**, “A Multilevel Energy Buffer and Voltage Modulator for Grid-Interfaced Micro-Inverters,” IEEE TPEL, 2015.

重點：27–38 V -> 230 Vac；Buffer 同時做 2ω energy buffering 與有效輸入電壓調變，降低 high-frequency DC/AC converter 的 conduction / magnetic loss。這與「用內部能量節點改善主轉換 Loss」高度接近。

### 9.7 Series-Connected Energy Buffer

**B. J. Pierquet, D. J. Perreault**, “A Single-Phase Photovoltaic Inverter Topology With a Series-Connected Energy Buffer,” IEEE TPEL, 2013.

重點：32 V-class low-voltage source、series-connected buffer、four-quadrant internal energy flow；證明「主功率 DC→AC + 內部雙向 buffer」已有直接前案。

### 9.8 Series-Stacked Energy Buffer (SSB)

**S. Qin et al.**, “A High Power Density Series-Stacked Energy Buffer for Power Pulsation Decoupling in Single-Phase Converters,” IEEE TPEL.

重點：2 kW，active converter 只處理部分功率，實驗效率 >98.9%；partial-power buffer 已成熟。

### 9.9 Isolated Single-Phase Matrix Converter + Transformer-Integrated Buffer

**N. Takaoka et al.**, “Isolated Single-Phase Matrix Converter Using Center-Tapped Transformer for Power Decoupling Capability,” IEEE Transactions on Industry Applications, 2018.

重點：bidirectional isolated DC↔single-phase AC、1 kW；center-tapped transformer + small LC buffer；不額外增加 power-decoupling switches；已直接整合 transformer、matrix AC conversion、buffer 與雙向。

### 9.10 Floating-Capacitor Integrated DAB (FCI-DAB)

題名：**“Floating Capacitor Integrated DAB for Single-Phase, Single-Stage PFC in Wireless Battery Charging Application”**

重點：active energy buffer 直接插在 high-frequency link；1.5 kW；報告 secondary-side RMS current 降低，對 secondary resistive conduction loss 有明顯改善。這是目前「Buffer placement in HF link」非常危險的 closest prior art。

---

## 10. BUS 啟發後真正剩下的問題

目前最值得追的不是「做雙向 BUS」，而是：

```text
X1 = 第一次高倍率阻抗轉換點
X2 = 2ω / reactive / recoverable energy buffer / recycling point
X3 = AC synthesis point
```

需要比較：

```text
Case A: X2 在 X1 前
12 V / 166 A <-> Buffer -> impedance conversion -> AC

Case B: X2 與 X1 整合
12 V -> [impedance conversion + energy buffering] -> AC

Case C: X2 在 X1 後
12 V -> impedance conversion -> HV buffer <-> AC
```

物理矛盾：

- Buffer 越靠近 12 V source，越可能抑制低壓側 ripple / RMS；但 Buffer 自己也要承受巨大電流。
- Buffer 越靠高壓側，Buffer 本身電流小、能量密度較好；但 12 V 高電流區的 conduction loss 已經先發生。
- 將 X1 + X2 整合可能降低元件 / 功率處理次數，但會增加 modulation、stress、circulating / commutation 的複雜度。

這個 **placement / integration trade-off** 是目前最需要做 prior-art closure 的位置。

---

## 11. 目前候選研究缺口（尚未證明首創）

目前較有希望的表述：

> 在 12 V-class、1–2 kW、100–200 A 的低壓電池 DC→單相 AC 系統中，將實際 source-side common-path resistance（battery / fuse / connector / busbar / PCB / MOS / primary winding）與 2 倍線頻 / reactive / commutation 能量流一併納入，研究第一次阻抗轉換點與局部雙向 energy-buffer / recycling point 的共同拓撲配置，並以降低 12 V 側 RMS current exposure 與總系統 Loss 為主要目標。

更具體的 candidate gap：

> **12 V / kW / 100–200 A 尺度下，是否存在把「高倍率第一次阻抗轉換」與「內部雙向 energy buffering / power decoupling」在同一 power structure 中整合，並明確以低壓側 RMS / conduction-loss reduction 為核心的固定拓撲？**

目前只能標記：

```text
STATUS = CANDIDATE GAP
NOVELTY = NOT YET ESTABLISHED
```

不能寫成「全球沒人做」。

---

## 12. 下一輪 prior-art closure 搜尋條件

優先鎖定以下交集，而不是再泛搜 APD / Boost：

```text
12V OR 24V low-voltage source
+
kW single-phase inverter
+
100A / high-current / current-fed
+
high-frequency transformer / matrix transformer / DAB / current-fed push-pull
+
integrated energy buffer / power decoupling / ripple steering
+
low-side RMS current reduction / battery ripple reduction / conduction-loss reduction
```

替代術語：

```text
power pulsation buffer
active energy buffer
series energy buffer
series-stacked buffer
third-port energy buffering
ripple port
ripple steering
energy recycling
integrated power decoupling
transformer-integrated decoupling
common-mode buffer
floating capacitor integrated DAB
partial power processing
differential power processing
minimum power processing
current-fed isolated inverter
low-voltage battery inverter
auxiliary power module 12V/48V
```

搜索時應特別看：

1. Buffer 放在哪一側（LV、HF link、HV、AC）。
2. Buffer 是否穿過主功率電流。
3. 是否減少 battery / LV source `I_rms`。
4. 是否只降低 2ω ripple，還是也降低 HFT primary RMS / conduction loss。
5. 是否為 12–24 V、kW、100 A 級，而不是 30–60 V、百瓦級。
6. 是否雙向只是系統功能，還是局部 energy recycling 的核心。
7. 是否有完整 loss breakdown，而非只報效率。

---

## 13. 模擬 / 實驗應先做的最小驗證

在畫新拓撲前，先建立統一 Loss 基準。

### 13.1 先量 / 建模 ASP 低壓大電流路徑

```text
Battery terminal
-> Fuse
-> Connector
-> Wire / Busbar
-> PCB copper
-> MOS group
-> HFT primary
```

需要得到：

```text
Rdc
Rac
Irms
P_loss
physical length
shared vs split path
```

### 13.2 把 12 V source current 分成有效與額外分量

不要只量 Iavg，至少要看：

```text
Iavg
Irms
120 Hz component
HF switching ripple
circulating / magnetizing component
```

研究重點：

```text
I_rms² - I_avg²
```

代表額外非平均電流對 conduction loss 的貢獻。

### 13.3 先做三個 placement benchmark

```text
S0: 現有 HFT + HV DC-link buffer
S1: LV-side / pre-transform buffer
S2: HF-link integrated buffer
S3: HV-side active buffer
```

所有方案使用相同：

```text
Vin
Pout
Vout
semiconductor technology
thermal constraint
copper budget
magnetic / capacitor volume budget
```

輸出至少比較：

```text
source Irms
HFT primary Irms
MOS conduction loss
switching loss
magnetic loss
buffer loss
PCB / busbar loss
2ω ripple magnitude
total efficiency
power density estimate
```

---

## 14. 研究方法上的固定原則

1. **先列 Known Architecture，再找 Gap。** 不從「想做什麼」反推新穎性。
2. **拓撲固定後才談控制。** MCU / DSP / AI 不是目前的新穎性來源。
3. **不能只看最高效率。** 必須做 loss decomposition。
4. **不把可逆能量搬運直接叫 Loss。** 要區分 energy flow 與 dissipation。
5. **不把拿掉 HFT 自動視為進步。** 需看整體 RMS / switching / passive / isolation / stress。
6. **不把多相 / 多 cell 自動視為降 Loss。** 固定總 silicon / copper / volume 後重新比較。
7. **BUS 只是一個能量流概念來源。** 本論文不是 UPS / BESS 功能研究。
8. **任何 novelty statement 前都要做 closest-prior-art closure。**

---

## 15. 當前一句話研究主線

> **從既有低壓 DC→AC 拓撲的 Loss 與能量流矩陣出發，研究 12 V / kW 百安培系統中「第一次阻抗轉換」與「局部雙向能量緩衝 / 回收」應如何在固定功率級結構中配置或整合，目標是降低 12 V 側 RMS 電流暴露與全系統總 Loss，而不是再堆疊一個已知高升壓單元。**

---

## 16. 目前決策狀態

```text
Research target:
    low-voltage high-current DC -> single-phase AC loss reduction

Primary scale:
    12 V, 1–2 kW, ~100–200 A

Topology focus:
    fixed power topology synthesis

Not the focus:
    UPS system design
    general bidirectional BUS
    AI / MCU dynamic path selection
    novelty-by-component-count

Strongest current candidate:
    joint placement / integration of
    first impedance transformation
    + local bidirectional energy buffering / recycling

Novelty status:
    NOT YET ESTABLISHED

Next action:
    close prior art on 12/24 V + kW + high-current + HFT/DAB/current-fed
    + integrated energy buffer + low-side RMS/conduction-loss reduction
```
