# 2026-09-10 — Royer/X1 研究脈絡、最近修正與工作主線 v1

Status: `WORKING_BRANCH / CONVERSATION_RECONCILIATION / ANALYTICAL_SCREEN`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. 結論與適用範圍

目前 Royer/X1 **探索工作主線**是：保留 Royer 為實體 Host Power Cell，從既有拓撲抽取功率／磁性／能量機制，在同一比較邊界下先算 RH1、RH5、RH6 的 P、V、I、RMS、gain 與總損耗，再決定哪些組合值得進入詳細換相設計。

Royer Host 在本研究的操作定義：

```text
主功率 MOS pair/banks
+ 中心抽頭初級與 HFT 功率傳輸
+ 磁性回授
+ 自激與自然換相
```

這是本研究採用的 Royer 類宿主定義，不把所有 Royer、resonant Royer 或 current-fed 變體視為相同電路。加入積木後，仍須確認回授、自激、磁通 reset 與主功率路徑是否成立。

**治理邊界：**本紀錄補充既有 2026-09-10 working branch，不取代 [2026-08-20 authoritative override](CURRENT_MAINLINE_OVERRIDE_2026-08-20.md)。正式 A0 證據主線仍是 File64 的 M1–M4 量測及後續帳本閉合；本輪沒有取得量測，也沒有證明任何 PG/CALG gate 通過。兩條線分開記錄，避免把「最近討論方向」誤寫成「正式證據已完成」。

## 2. 本次查核來源與命名決定

整理日期：2026-09-10。GitHub 查核基準 main commit：`e038f26321ad1f5180b45ba62be961f2fc0ee53f`。

- 原對話：[電路設計靈感來源](https://chatgpt.com/c/6a9bd806-39cc-83e9-91ac-97cad613752c)。本輪讀取最近 20 個 turn，包含控制／功率拆解、三 Cell、換相修正，以及最後恢復 Royer Host 的討論。這是有界對話查核，不宣稱完整讀完所有更早歷史或附件。
- 最新工作紀錄：[Royer Host Power-Brick Screen v1](WORKING_BRANCH_2026-09-10_ROYER_HOST_POWER_BRICK_SCREEN_V1.md) 與 [Decision v1](WORKING_BRANCH_2026-09-10_ROYER_HOST_POWER_BRICK_DECISION_V1.json)。
- [README](../README.md)、[RESEARCH_STATE](RESEARCH_STATE.md)、[2026-08-20 override](CURRENT_MAINLINE_OVERRIDE_2026-08-20.md)：目前索引、歷史狀態與正式主線的權限關係。
- [File26](26_NINE_FAMILY_MECHANISM_EXTRACTION_MATRIX.md)：九類拓撲的機制抽取方法。
- [File28](28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md)：X1/X2/X3 與 physical-gap 定義。
- [File33](33_COMBINATION_LOSS_AUDIT_GATE.md)：組合損耗、交互作用、損耗轉移與 matched total-loss gate。
- [File45](45_R2_C3_MULTI_ASSISTANT_PRIOR_ART_AND_REF2_LOCK_V1.md)：R2-C3 停止新穎性主張、Ryan 1998 鎖為 R2-REF2 的既有研究結果。

現有 numbered research 為 01–64；override 已將 File65 留給取得有效 M1–M4 後的 A0-REAL loss-ledger closure。因此沿用 `WORKING_BRANCH_日期_主題_V1.md` 命名，不佔用 65、不覆蓋原 screen/decision，也不改寫舊研究的歷史結論。

對話中「已執行 Gate」「檔案已整理」等文字，只按對話陳述處理。沒有可核對的工具紀錄、模型、波形或附件內容，就不升級成實際驗證。本輪沒有新增文獻搜尋或重跑 File43 多路審查；File45 的 prior-art 結果以既有研究來源引用，不冒充本輪獨立重驗。

## 3. 脈絡：為什麼從 Royer 控制討論回到功率拓撲

| 階段 | 研究意圖／結果 | 目前如何保留 |
|---|---|---|
| Royer 起點 | DC 經主 MOS 交替切換、HFT 交變激磁與升壓；磁性狀態參與換相 | 保留完整自激功率 Cell |
| 外部修正層 | 探索自然換相加外部 phase/duty/ZVS admission 修正 | 是待驗證控制選項，不代表取代 Royer 功率級 |
| 機制拆解 | 分開 power-path、magnetic、commutation、timing，避免把不同抽象層當互斥候選 | 分類方法保留 |
| 過度抽象化 | 對話曾把 Royer 說成「不是完整功率拓撲／只負責何時切」 | 這種實體電路描述已被最近使用者糾正，不再沿用 |
| 換相研究分支 | current-fed、overlap、clamp、Coss、cross-cell magnetic shuttle 的可行性討論 | 保留限制和反例，詳細設計延後 |
| 最近主線修正 | 使用者要求「開始用積木算功率」，並指出 Royer 功率部分被拿掉 | 恢復 Royer Host，先 RH1/RH5/RH6 同邊界帳本 |

可追溯的關鍵對話 turn：

- `bbb2197c-e56c-4422-a31d-e5d57230f7dd`：已說明 Royer 是功率級加自激換相，成熟機制可整合到同一 switching cell。
- `55ba9469-3fb4-4c40-a764-03180af82f2c`：修正 BOTH_OFF 過度否定，將已知 local ZVS 與 cross-cell 假說拆開。
- `50a4d008-0a42-4573-8f29-e8e41dd7db15`：使用者要求回到積木功率計算。
- `fb9df356-2409-452c-9b0b-7c250fd761c9`：明確恢復 Royer Host Power Cell。
- `f3a96410-22f3-4456-825f-340c60d020f9`：RH1/RH5/RH6 一階 screening。
- `abb2bca7-a5c7-4915-8b2f-0927f7b81991`：最後追問三個 Royer 變壓器是否並聯；已有 repository screen/decision 提供串並聯澄清。

核心不是再增加更多 topology 名稱，而是讓成熟積木在 Royer Host 上有清楚的功率路徑、必要功能與新增損耗。Royer 的磁性自激仍可單獨做 falsification；「可拆出 timing 子機制」不代表實際主 MOS/HFT 可以從宿主消失。

## 4. X1 與比較問題保持一致

依 File28：

- X1：第一次主要電壓／電流域轉換區域，涵蓋開始主功率處理到大部分功率持續进入較低電流域。
- X2：單相 2ω 能量緩衝／路由功能。
- X3：最終單相 AC 波形合成功能。

這些是功能座標，可物理重疊，並非三個必須獨立串聯的零件。產生 HF alternating excitation 是目前 HFT 宿主的必要功能，但不是完整的 220 Vac 輸出，也不是 Royer 獨有的新穎性。

比較要回答「百安培能量經過哪些元件、在哪裡轉換電流域、總損耗是否降低」。早分流、三 Cell、matrix magnetics、ZVS、電容疊壓都不能單獨代表 verified physical gap 或 Candidate #10。

## 5. 三 Cell 的正確讀法與未閉合處

RH1 的一階假設是：

```text
共用 12-V DC source
  ├─ Royer Host A → HFT A ┐
  ├─ Royer Host B → HFT B ├─ 副邊電壓貢獻串聯相加 → HV boundary
  └─ Royer Host C → HFT C ┘
```

並聯的是三個 Host 的低壓 DC 輸入；不是把三個變壓器一次側 switching nodes 與二次側都直接並接。N=3 是計算點，尚非固定最佳架構；也不等於已建立單一共磁芯 matrix transformer。

**這張圖仍是 block-level screen。**必須再區分：

1. HF 副邊繞組直接串聯後共同整流：必須定義瞬時極性、頻率、相位與整流／負載狀態，才能計算有效相加電壓。三顆獨立自激不會因共用 DC source 就自動同相，也不會自動固定 120°。
2. 各副邊獨立整流後 DC 串聯：這是另一個需要明列的電氣圖；要計入各整流器、儲能、均壓、啟動與故障支援損耗。

兩種圖不可共用一套未聲明的 RMS／loss 結論；也不能把 interleaving 效益直接套到同相副邊串聯假設。均流、相位協調與電壓分享目前都未驗證。

## 6. 已有一階功率帳：數字成立的條件

沿用 screen 的計算假設：Vin=12 V、Pout=2000 W、eta_target=0.95、N=3、HV screening anchor=336 V。

| 量 | 重算尺度 | 證據／限制 |
|---|---:|---|
| 理想輸入電流 Pout/Vin | 166.67 A | 不含損耗 |
| Pin=Pout/eta_target | 2105.26 W | 95% 是目標假設，不是量測效率 |
| 輸入平均電流 Pin/Vin | 175.44 A | 尚非 source RMS |
| 每 Cell 平均輸入電流 | 58.48 A | 理想等分，非每顆 MOS RMS/peak |
| 每 Cell 輸入 throughput | 701.75 W | 非 choke 本身耗散功率 |
| 每 Cell 輸出貢獻 | 666.67 W | 理想等功率 |
| HV 功率電流尺度 2000/336 | 5.95 A | DC/equivalent scale，非已知 HF 繞組 RMS |
| 每 Cell 電壓貢獻 336/3 | 112 V | 相加與等分假設 |
| 每 Cell 有效 gain 112/12 | 9.33 | 非已確定 Ns/Np |
| 單 Cell 全部 gain 336/12 | 28 | 同上，仍需波形與整流模型 |

336 V 只屬此 exploratory screen；不能取代 override 的 350-V-class MODERN-MATCHED 條件，也不是 A0 R52 的實測 BUS。A0 既有 244.36–315 V 是不同邊界的 bound，不能混入此表當同一硬體結果。

若 2 kW 指最終 AC 輸出，則實際 X1/HV 需再供應後級損耗；5.95 A 只是忽略後級損耗的尺度。後續必須分清系統效率與 X1 效率、每個 P 的量測截面。

### 積木代價的有效結論

- Current-fed：3 × (58.48 A)^2 × DCR，在每支路 DCR=0.10/0.25/0.50/1.00 mΩ 時，總 DC 銅損尺度約 1.03/2.56/5.13/10.26 W。實際應用每支路 Irms，不可忽略 ripple、core、clamp 與其他串聯路徑。
- Resonant：在電阻不變時，Irms 放大 k 倍使該 I²R 項放大 k²。k=1.10 為 +21%；k=1.25 為 +56.25%。這不是整機損耗百分比。
- Capacitive gain：以 12 V、50 kHz、完整 2 kW 能量搬運尺度估算 Q≈P/(fV)=3.33 mC/cycle，等效平均電流 166.67 A。這不是每顆 flying capacitor 的已確定電荷／RMS；仍需具體 switching states、搬運比例與電壓階差。
- 後移電容積木至較高電壓節點可能降低相同功率的平均電流，但不自動證明較低 ESR、charge-redistribution 或總損耗。
- 分三支路不自動降低總 loss：共用 source path 仍承受總電流，器件／銅材資源、磁性與驅動數量也要公平比較。

## 7. 換相分支保留的修正，不作當前主線

| 舊敘述／方向 | 現在保留的判定 |
|---|---|
| current-fed 的 BOTH_OFF 必然開路 | 過度絕對；須看 Coss、diode、channel、clamp 等實際有限時間路徑與 stress |
| BOTH_ON overlap 可以續流，所以有 ZVS | 續流不等於 incoming MOS 的 VDS 已降到零 |
| 純磁耦合可取代本地電流迴路 | 不成立；磁耦合不能免除本地電氣路徑 |
| local magnetizing/leakage current + Coss/body diode ZVS | File45 已列為 known prior art/comparator，不能重新包裝成新穎性 |
| inter-cell differential mode 能降低 local magnetizing current | 仍是未驗證假說；需區分非零可控的跨 Cell 能量與已知 local ZVS |
| Royer 自然換相即代表更高效率 | 未成立；需同功率網路的 forced/hybrid comparator |

對話中的 P3/P3R/C3R2、X1-C1/C2/C3 等為探索分支標籤，不是 Candidate #10 編號，也不等同 repository 的 R2-C3。詳細 coupled-inductance、E_cross 與 gate sequence 研究延後；必要的基本電氣可行性仍須在功率篩選時檢查，不能用「先算功率」掩蓋斷路或磁通不平衡。

本紀錄不採用簡單相加兩個 Eoss 就宣稱 ZVS 已閉合：實際能量／電荷平衡、非線性 Coss、極性、時間窗口與回收路徑仍需由具體圖推導。

## 8. 正確 survivor board 與下一步

| ID | 意義 | 目前狀態 |
|---|---|---|
| RH0 | 單 Royer Host | reference |
| RH1 | 多 Host，輸入並聯／副邊貢獻串聯 | 基本比較架構；KEEP 僅指保留作分析 |
| RH2 | RH1 + resonant | KEEP_CONDITIONAL |
| RH3 | RH1 + current-fed | KEEP_CONDITIONAL |
| RH4 | 直接 12-V capacitive gain | HOLD / HIGH_CURRENT_RISK |
| RH5 | Royer Host + current-fed + resonant + magnetic sharing | PRIMARY SCREEN；非已證明最佳 |
| RH6 | Royer Host + resonant + 第一次升壓後 capacitive gain | SECONDARY SCREEN |

下一輪應完成同一份 RH1/RH5/RH6 matched ledger：

1. 聲明輸入、輸出截面、AC/DC/HF 波形、隔離／保護、負載、熱條件、器件世代與 N；336 V screen 和其他 bus 比較必須先正規化。
2. 為每個組合指定足以計算的實際連接圖、回流路徑與基本狀態；尚未定義者記 GRAPH_UNRESOLVED。
3. 每個節點列 Vavg/Vrms、Iavg/Irms/Ipeak、P_real、gain、處理功率比例。非正弦網路須聲明 reactive/apparent power 定義，不能把 reactive VA 當耗散 W。
4. 合計 MOS conduction、switching/recovery/Coss、HFT copper/core、choke、resonant L/C、capacitor ESR/redistribution、rectifier、interconnect、gate/control/support 損耗。circulating current 導致的同一銅損只計一次。
5. 依 File33 另外加 REMOVED/REDUCED/RELOCATED/INTERACTION_NEW 等因果標籤，不與物理瓦數重複相加；未知 material loss 記 LOSS_LEDGER_INCOMPLETE。
6. 對每個相同功率網路，保留 Royer 與 forced/hybrid 控制的公平鏡像比較；並使用既有成熟 active-clamp／R2-REF2 作對照，不只打敗弱 baseline。
7. 用 ΔP_total=P_loss,baseline−P_loss,candidate 判斷，優先要求 P_loss,candidate,high < P_loss,baseline,low；材料門檻與不確定度必須明列。通過前不宣稱總損耗優勢。
8. 只有功率與必要證據 gate 存活後，才展開詳細換相時序、精確 prior-art 差異及 PSIM 驗證。這裡只記錄後續順序，本輪未執行。

## 9. 最終狀態

```text
Royer physical Host                     = RETAINED
Current exploratory focus               = RH1 / RH5 / RH6 matched power-loss accounting
N=3                                     = SCREENING_POINT / NOT_LOCKED
Exact secondary / rectifier graph       = OPEN
Current sharing / phase coordination    = NOT_VERIFIED
Matched total-loss advantage            = NOT_ESTABLISHED
Formal A0 measurement mainline          = RETAINED / M1–M4 NOT_ACQUIRED_THIS_RUN
Candidate #10                           = HOLD / NOT_ASSIGNED
Novelty                                 = NOT_ESTABLISHED
PSIM                                    = NOT_EXECUTED
Hardware                                = NOT_EXECUTED
```

本次成果是研究脈絡、修正與索引的可追溯整理；不是新拓撲定案、量測報告、模擬報告或新穎性證明。
