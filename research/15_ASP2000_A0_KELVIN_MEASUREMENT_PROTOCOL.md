# 15 — ASP-2000 A0 Kelvin / Millivolt Measurement Protocol

Status date: 2026-08-19  
Role: `A0 EXECUTABLE MEASUREMENT PROTOCOL`  
Research phase: `PHYSICAL GAP VALIDATION`  
Hardware result status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark measurement gate`

## 1. 目的

把前一階段的：

```text
A0 net reconstruction
+ PCB geometry loss bounds
```

轉成可以直接在 ASP-2000 R52 實機執行的：

```text
電流 + mV 壓降 + 溫度
→ 分段等效 R
→ 分段 Watt loss
```

本文件的目標不是先量完整 inverter efficiency，而是先關閉：

```text
BAT+ / BAT−
→ low-voltage distribution
→ X1 前後附近
```

最昂貴的百安培電流路徑。

---

## 2. 量測方法原則

mΩ / sub-mΩ 路徑不可用普通二線電阻量測作為正式證據，因為量測線與接點電阻可能與 DUT 同量級。

正式方法使用：

```text
Kelvin / 4-wire concept
```

在實機有工作電流時，優先量：

```text
ΔV_segment
I_segment
Temperature
```

再計算：

```text
R_segment = ΔV_segment / I_segment
P_segment = I_segment × ΔV_segment
```

對具有明顯 switching ripple 的區段，若能同步取得波形，優先使用：

```text
P_segment = average[v(t) × i(t)]
```

不要把：

```text
Iavg × Vavg
```

誤當成所有高頻動態 loss 的完整結果。

---

## 3. 實機安全 / 接線邊界

ASP 低壓端雖為 12–24 V class，但可用電流為百安培等級，因此量測重點是避免探棒、sense wire 或金屬工具形成意外短路。

執行順序：

```text
1. Power OFF
2. 確認 DC-link / bus 已依現場程序進入安全狀態
3. 用 continuity / schematic 確認 probe node
4. 固定 sense leads / clips
5. 確認沒有可能碰觸鄰近 power node
6. 才 Power ON
7. 負載由低往高建立 operating point
8. 不在滿載狀態手持移動裸露 sense point
```

動態 mV 波形若使用 oscilloscope：

```text
use isolated / differential measurement
verify probe common-mode range
use the lowest practical attenuation / bandwidth limit for low-level mV work
```

不要把一般 earth-referenced single-ended scope ground clip 隨意跨接在不同 power nodes。

---

## 4. 已驗證的實體量測節點

### K0 — BAT+ source node

```text
BAT+ main connector power terminal
```

PcbDoc 已確認 BAT+ 經 Top/Bottom polygon、stitching vias 往 8 個 main fuse inputs 分配。

### K1-T1-IN — T1 fuse-bank BAT+ side

```text
BAT+ side of:
F2 / F3 / F5 / F6
```

精確 pad number 在上機前用 Power-OFF continuity 確認；不要只用左右方向猜 pad polarity。

### K1-T1-OUT — T1 fuse-bank output node

```text
opposite side of:
F2 / F3 / F5 / F6
→ local T1 feed node
```

### K2-T1 — T1 center tap

```text
T1 primary pin B / center-tap feed
```

### K1-T2-IN — T2 fuse-bank BAT+ side

```text
BAT+ side of:
F7 / F8 / F9 / F10
```

### K1-T2-OUT — T2 fuse-bank output node

```text
opposite side of:
F7 / F8 / F9 / F10
```

### KJ8-A / KJ8-B — T2 external-link boundary

PcbDoc 已確認同網路 `J8` 的兩個大型端點，中間不是普通 PCB polygon 連完整段。

```text
KJ8-A = fuse-bank / upstream side
KJ8-B = transformer / downstream side
```

實際 assembly 是 wire / jumper / copper strap / busbar 仍待實機確認。

### K2-T2 — T2 center tap

```text
T2 primary pin B / center-tap feed
```

### KB — main low-side return B

SchDoc 直接確認：

```text
Q39...Q65 source side = B
```

MOS symbol pin mapping：

```text
D = pin 2
S = pin 3
```

### KBAT− — battery-negative side of Q39...Q65

SchDoc connectivity：

```text
BAT− connector
→ Q39...Q65 drain side

Q39...Q65 source side
→ B
```

因此整個 7-MOS bank 可以直接做：

```text
KBAT− ↔ KB
```

的總 mV drop 量測，不需要先假定每一顆 MOS 的均流。

---

## 5. 第一層：最低設備版本

最低需求：

```text
1 × I_source
+ isolated / differential / floating mV measurement
+ temperature record
```

即使沒有 I_T1 / I_T2，仍可先正式量：

### M5 — negative 7-MOS full-current bank

```text
KBAT− ↔ KB
```

因為整個 source current 都經過此串聯功能區：

```text
P_M5 ≈ I_source × ΔV_M5
R_M5 ≈ ΔV_M5 / I_source
```

這是目前最乾淨、最值得優先取得的 A0 實測 loss bucket 之一。

### Full-current connector / common-series element

如果某個區段明確位於分流前，且所有 source current 都經過：

```text
P = I_source × ΔV
```

即可直接取得該區段的工作點 loss。

---

## 6. 第二層：完整版本需要三個 current channels

Preferred current set：

```text
I_source
I_T1
I_T2
```

基本一致性檢查：

```text
I_source,avg ≈ I_T1,avg + I_T2,avg + I_aux,avg
```

若 auxiliary current 很小，可以先記錄 residual：

```text
I_residual = I_source - I_T1 - I_T2
```

不要強迫假設：

```text
I_T1 = I_T2 = 0.5 I_source
```

直到量測證明均流成立。

若 T1/T2 center-tap conductor 無法安全放入 DC/Hall current probe，則：

```text
T1/T2 branch-current split = OPEN
```

相關 local loss 只能暫列 estimate，不升級為 measured result。

---

## 7. M0 — BAT+ 多端 common-distribution loss

BAT+ polygon 是：

```text
one source
→ eight fuse-input sinks
```

因此不能用：

```text
WRONG:
P_BAT+ = I_source × one arbitrary fuse-input drop
```

正式式：

```text
P_BAT+dist = Σ I_Fk × (V_BAT+ - V_Fk,input)
```

若只有 T1/T2 feed current，而沒有 individual fuse current：

```text
ΔV_T1,in,avg = average(drop to F2,F3,F5,F6 BAT+ sides)
ΔV_T2,in,avg = average(drop to F7,F8,F9,F10 BAT+ sides)

P_BAT+dist ≈
    I_T1 × ΔV_T1,in,avg
  + I_T2 × ΔV_T2,in,avg
```

如果連 I_T1 / I_T2 都沒有，才允許 temporary equal-share estimate：

```text
P_BAT+dist,estimate ≈
I_source × average(all eight fuse-input drops)
```

狀態必須寫：

```text
EQUAL-SHARE ESTIMATE
not measured distribution loss
```

這是對前一階段 geometry model 的必要實測修正。

---

## 8. M1 — Fuse-bank loss

### T1 fuse bank

```text
F2 // F3 // F5 // F6
```

四顆 fuse 為平行支路時，若量 common input node 到 common output node 的工作壓降：

```text
P_FUSE,T1 = I_T1 × ΔV_FUSE,T1
```

不需要知道每顆 fuse 電流即可得到整個 fuse bank 的 total loss。

### T2 fuse bank

```text
F7 // F8 // F9 // F10
```

```text
P_FUSE,T2 = I_T2 × ΔV_FUSE,T2
```

### individual fuse mV

另量 8 顆 fuse 各自 end-to-end mV：

```text
F2 F3 F5 F6
F7 F8 F9 F10
```

用途主要是：

```text
current-sharing / contact / thermal anomaly screening
```

沒有 individual branch current 時，不要把：

```text
P_Fk = assumed current × measured drop
```

升級成正式 per-fuse loss。

---

## 9. M2 — T1 local feed

量測：

```text
K1-T1-OUT → K2-T1
```

有 I_T1 時：

```text
R_T1local = ΔV_T1local / I_T1
P_T1local = I_T1 × ΔV_T1local
```

與前一階段 2D geometry model：

```text
R_T1local,PCB ≈ 0.351 mΩ
```

比較。

如果實測顯著高於 geometry model，優先檢查：

```text
contact / neck / thermal rise / actual current spreading / assembly details
```

如果實測顯著低於 geometry model，優先檢查：

```text
solder reinforcement / extra conductor / model boundary mismatch
```

---

## 10. M3 + M4 — T2 / J8 boundary

分開量：

```text
M3a: K1-T2-OUT → KJ8-A
M3b: KJ8-A → KJ8-B
M4 : KJ8-B → K2-T2
```

其中最重要：

```text
R_J8 = ΔV_J8 / I_T2
P_J8 = I_T2 × ΔV_J8
```

這會直接解掉目前 geometry model 最大的 assembly unknown。

不要用猜測 wire gauge / copper strap size 代替實機 mV。

---

## 11. M5 — BAT− ↔ B seven-MOS bank

量：

```text
KBAT− → KB
```

計算：

```text
R_negBank = ΔV_negBank / I_source
P_negBank = I_source × ΔV_negBank
```

目前 datasheet boundary：

```text
7 × CSD18510KCS ideal parallel
R_eq,25C,max ≈ 0.243 mΩ
P @ 175.4 A ≈ 7.47 W
```

實測若高於此值，不代表錯誤；需要同時看：

```text
junction/case temperature
VGS
current sharing
PCB / package / contact contribution
```

如果此區實測為重要 loss bucket，後續比較 A1 / Candidate 時必須先判斷：

```text
產品必要功能 loss
or
X1/topology intrinsic loss
```

不能直接把整桶都算成新 topology 可節省的 loss。

---

## 12. M6 — B return distribution

如果能找到 main A/C switching MOS source plane 與 `B` reference node 之間可安全分離的 sense points：

```text
main MOS source-region → B
```

則量：

```text
ΔV_Breturn
```

若此段確定承受完整 source-return current：

```text
P_Breturn ≈ I_source × ΔV_Breturn
```

若 current spreads through multiple asynchronous/local paths and boundary 不清楚，維持：

```text
MEASUREMENT_BOUNDARY_NOT_CLOSED
```

不要硬套 single-path I×V。

---

## 13. Main A/C switching MOS 不在本輪用 DC Kelvin 關閉

主 switching nodes：

```text
A-side paralleled MOS
C-side paralleled MOS
```

承受高頻脈衝電流。

這些不能只量一個 DC mV 後直接寫：

```text
P_mainMOS = I_source × Vdrop
```

正式需要：

```text
VDS(t)
ID(t)
VGS(t)
fs
Tdevice
```

以及：

```text
P_cond/sw ≈ average[vDS(t) × iD(t)]
```

或使用經驗證的 device-loss model。

因此：

```text
Distribution Kelvin Gate
≠ Main MOS switching-loss Gate
```

兩者分開。

---

## 14. 建議 operating-point matrix

所有 operating points 必須在產品額定與現場核准條件內。

建議使用同一 Vin 與同一 cooling condition，依產品允許逐步提高負載：

```text
OP0 = no-load / idle reference
OP1 = low-load reference
OP2 = mid-load reference
OP3 = high-load reference
OP4 = 12 V / 2 kW anchor if product/test setup permits
```

每一點至少記錄：

```text
Vin at BAT connector
Vout
Pout
I_source,avg
I_T1,avg if available
I_T2,avg if available
ΔV M0...M6
ambient temperature
Fuse temperatures
Q39...Q65 temperature
main low-side MOS temperature
T1/T2 temperature
run / stabilization condition
```

不要跨 operating point 使用不同未記錄 cooling 狀態。

---

## 15. mV 尺度參考

在 175.4 A：

```text
0.05 mΩ → 8.77 mV → 1.54 W
0.10 mΩ → 17.54 mV → 3.08 W
0.20 mΩ → 35.08 mV → 6.15 W
0.25 mΩ → 43.85 mV → 7.69 W
0.40 mΩ → 70.16 mV → 12.31 W
0.65 mΩ → 114.01 mV → 20.00 W
1.00 mΩ → 175.4 mV → 30.77 W
```

在 87.7 A，電壓尺度約為上述一半；功率約為四分之一（在相同 R 下）。

因此正式量測最好具有穩定的 sub-mV to mV resolution，而不是用幾十 mV 精度的粗略讀值判斷 sub-mΩ loss。

---

## 16. 量測品質檢查

每個點至少做：

```text
repeat reading
polarity sanity check
current stability check
temperature record
sense-point photo / identifier
```

低阻結果若要跨時間比較，sense points 必須保持相同。

如果量到：

```text
negative R
large sign reversal
mV jump unrelated to current
large result change after touching probe
```

先判定：

```text
MEASUREMENT INVALID / REPEAT
```

而不是直接寫入 loss table。

Dynamic oscilloscope measurement 另檢查：

```text
probe common-mode range
bandwidth / noise
channel offset / zero
clipping
synchronization with current waveform
```

---

## 17. 第一份正式實測資料表格式

| OP | Segment | Current used | ΔV | R_eq | P_loss | Temp | Evidence |
|---|---|---:|---:|---:|---:|---:|---|
| OPx | BAT+ distribution | `I_T1/I_T2 weighted` |  |  |  |  | MEASURED |
| OPx | T1 fuse bank | `I_T1` |  |  |  |  | MEASURED |
| OPx | T1 local feed | `I_T1` |  |  |  |  | MEASURED |
| OPx | T2 fuse bank | `I_T2` |  |  |  |  | MEASURED |
| OPx | J8 external link | `I_T2` |  |  |  |  | MEASURED |
| OPx | T2 local feed | `I_T2` |  |  |  |  | MEASURED |
| OPx | BAT−↔B 7-MOS bank | `I_source` |  |  |  |  | MEASURED |
| OPx | B return copper | boundary-specific |  |  |  |  | MEASURED/OPEN |

另外保留：

```text
Geometry Bound
Datasheet Bound
Measured
```

三欄並列，不能覆蓋原始 bound。

---

## 18. Loss classification after measurement

量完後，不直接把所有 A0 loss 都當成 topology opportunity。

分三類：

### A — Product-required functional loss

例如若確認為必要：

```text
Fuse
battery disconnect / reverse protection
connector / safety function
```

公平 benchmark 必須匹配功能。

### B — Packaging / distribution loss

```text
common PCB copper
J8
contacts
current-spreading path
```

這些可以被 A1 layout/current-distribution optimization 攻擊，但不自動構成新 topology。

### C — X1 intrinsic conversion loss

```text
main switching MOS
primary copper
core
leakage / clamp / commutation
rectification associated with X1
```

只有：

```text
A1 已合理最佳化後仍然存在的重大 C 類 loss
```

才是換掉 X1 physical mechanism 的強理由。

---

## 19. Gate-out condition

本 Gate 完成條件：

```text
1. M0/M1/M2/M3/M4/M5 至少取得主要 working point 的可信 mV
2. I_source 已量
3. I_T1/I_T2 已量，或明確標記 branch split OPEN
4. 溫度已記錄
5. geometry/datasheet/measured 三類 evidence 分開
6. product-required vs packaging vs X1-intrinsic loss 已分類
```

Gate output：

```text
A0 measured distribution-loss table
↓
A0 BAT→X1 loss budget v1
↓
A1 optimized magnetic target specification
```

如果沒有實測資料：

```text
A1 remains BLOCKED
```

---

## 20. Current status

```text
Kelvin measurement method        = DEFINED
probe-node map                   = DEFINED AT DESIGNATOR/NET LEVEL
multi-terminal BAT+ loss formula = CORRECTED / DEFINED
M5 negative-bank measurement     = READY
T1/T2 branch-current measurement = REQUIRED FOR FULL CLOSURE
hardware data                    = NOT YET ACQUIRED
A0 measured loss budget          = OPEN
A1 synthesis                     = BLOCKED
Candidate #10                    = NOT ASSIGNED
Novelty                          = NOT_ESTABLISHED
```
