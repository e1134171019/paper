# 05 — Current Research Hypothesis

Status date: 2026-08-17
Status: `HYPOTHESIS / NOT YET PROVEN`

## 1. 問題起點

單相 DC→AC 系統同時存在：

```text
平均主功率
2ω 脈動功率
反應能量
高頻諧振 / 循環能量
漏感 / Coss / commutation 能量
```

在 12 V、kW 級條件下，任何額外 RMS current 若穿越 full-current low-voltage path，都可能因 `I²R` 被放大。

因此假設不是「把所有能量都做雙向」，而是先決定不同能量分量應該在哪個區域流動。

## 2. 第一層能量路由假設

希望達成：

```text
Average Energy:
Source → Load

Pulsating 2ω Energy:
Buffer ↔ Load / HV energy node
```

盡量避免：

```text
Pulsating 2ω Energy ↔ 12 V source
```

目標結果：

```text
I_LV,2ω ↓
→ I_LV,RMS ↓
→ P_LV,cond ↓
```

但只有在：

```text
P_LV,saved > P_buffer,added
```

時才算成功。

## 3. UPS 式雙向補償的正確定位

這裡的「UPS 式」只指能量交換邏輯，不是 UPS backup-time 功能，也不是 AI adaptive control。

工作名稱：

```text
Bidirectional Energy Buffer
或
Bidirectional Power-Decoupling Port
```

定義 `P_buf > 0` 為 Buffer 放電至 DC link / load：

```text
P_buf = P_out - P_source
```

若 source 近似只提供平均功率：

```text
P_buf = -P_avg cos(2ωt)
```

所以 Buffer 以 100/120 Hz 持續充放電，處理的是 Joule-scale pulsating energy，而非長時間備援能量。

## 4. X1 / X2 / X3 假設

```text
X1 = first major impedance transformation
X2 = 2ω / local bidirectional energy buffer
X3 = AC synthesis
```

三個可能 placement：

```text
Case A: X2 before X1
LV source ↔ Buffer → impedance transformation → AC

Case B: X1 and X2 integrated
LV source → [transformation + buffering structure] → AC

Case C: X2 after X1
LV source → impedance transformation → HV node ↔ Buffer → AC
```

目前工程直覺偏向 Case C 或 B，而不是把完整 Buffer 放在 12 V 百安培側；但這只是 hypothesis，必須由公平 loss model 驗證。

## 5. Electric-field 的角色

Electric-field / capacitive isolation 目前只是 candidate mechanism，不是已成立的研究缺口。

原始動機：

```text
HFT magnetic core/winding/leakage losses
        ↓
是否可用 electric-field coupling 改變 loss structure？
```

但已確認：

```text
Removing magnetics ≠ removing loss
```

可能產生的新增代價：

```text
coupling-capacitor RMS current
ESR / dielectric loss
resonant/reactive VA
circulating current
common-mode current
mismatch / balancing
extra switching devices
precharge / protection complexity
EMI / isolation stress
```

因此 Electric-field 必須通過：

```text
P_mag,saved
+ P_LV,RMS,saved
+ P_switching,saved
+ P_rectifier,saved
>
P_cap
+ P_circulating
+ P_extra_switches
+ P_control/auxiliary
```

## 6. Candidate architecture — 僅為工作假設

```text
12–24 Vdc
   ↓
LV current sharing / multicell
   ↓
Early impedance transformation
   ↓
Capacitive / electric-field HF power transfer
   ↓
HV / reduced-current energy node
   ├────────↔ Bidirectional 2ω Buffer
   ↓
AC synthesis
   ↓
220 Vac / 1φ
```

更積極的候選是三埠 electric-field network：

```text
Port A = 12–24 V source
Port B = main HV/AC power path
Port C = energy buffer
```

並讓 main-power transfer 與 compensation path 共享部分 switching / coupling / resonant structure。

但目前：

```text
three-port electric-field architecture = HYPOTHESIS
novelty = NOT ESTABLISHED
```

## 7. 不能接受的假成功

以下都不能單獨證明研究成立：

```text
Buffer voltage ripple ↓
某一 MOS loss ↓
HFT removed
component count ↓
peak efficiency ↑ at one point
2ω source ripple ↓
```

真正成功條件至少要同時觀察：

```text
I_LV,RMS
I_2ω
I_circulating
component RMS/stress
P_loss,total
thermal / isolation / EMI feasibility
```

## 8. 目前一句話假設

> **在 12–24 V、kW 級單相逆變器中，若能在低壓百安培 full-current path 之後盡早完成有效阻抗轉換，並使二倍線頻脈動能量在高壓／較低電流的局部能量節點與 Buffer 間循環，而不是穿回低壓來源，則有機會降低低壓 RMS conduction loss；Electric-field coupling 是否能成為此結構的一部分，必須以新增 circulation/capacitor loss 小於被省下的 magnetic/LV loss 為成立條件。**
