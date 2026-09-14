# 2026-09-14 — Royer 原始構想補正與對話審讀進度 v1

Status: `WORKING_BRANCH / HISTORICAL_CONTEXT_ADDENDUM / PARTIAL_REVIEW`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Full conversation review: `INCOMPLETE`

## 1. 本次結論

早期構想以 Royer 的主功率、磁性回授與自激換相為起點，研究**同一磁性結構中的多組功率初級、共同回授與輸出繞組**，能否在 12 V 大電流入口改變功率分配方式，再探索外部參考修正與完整 220 Vac / 50 Hz 輸出功能。

後來 RH1 的「三個獨立 Royer Host，輸入並聯、輸出電壓貢獻串聯」是另一個比較架構。恢復 Royer 實體功率 Cell 是必要的脈絡修正，但不能僅憑這點宣稱三 Host 已完整還原原始共磁芯多初級構想。兩者須分別建立接線、磁性模型與總損耗帳。

本文件接續 2026-09-11 起草、2026-09-14 續作的更新，補充 [2026-09-10 脈絡整理](WORKING_BRANCH_2026-09-10_ROYER_X1_CONTEXT_AND_MAINLINE_RECONCILIATION_V1.md)，不覆蓋歷史版本，不把假說升級成可行性、新穎性或模擬通過結論。

## 2. 來源與審讀範圍

- 來源：[電路設計靈感來源](https://chatgpt.com/c/6a9bd806-39cc-83e9-91ac-97cad613752c)。
- 本次連續審讀工作先前取得可存取對話分支的 22 頁、214 個 turn，游標已到最早頁。這是**分頁取得範圍**，不是逐字審讀完成證明。
- 部分閱讀輸出曾截斷；全文逐段審讀、缺段補讀與附件查核尚未完成。不得稱本文件為「全對話完整審計」。
- 當時工具列出 10 張可用圖片路徑；早期 PDF 與部分圖片只有附件標記。圖片尚未全部查核，附件清單也不代表全部原始附件已取得。
- 本補充依據已讀早期關鍵 turn、使用者提供的近期對話，以及重新取得的 repository 文件。未把缺失附件、生成圖片與歷史下載連結的內容當作已驗證事實。
- GitHub 查核基準：main commit `07aca67b9196bdf92d649871b2f41cc913a952ed`。本次更新流程已檢查 README、RESEARCH_STATE、2026-08-20 override、上一版脈絡紀錄與 research 命名；提交前再次確認 main。
- 沒有新增文獻查核、PSIM 執行或硬體量測。歷史助理文字中的「已執行」不單獨構成外部工具或測試證據。

沿用 `WORKING_BRANCH_日期_主題_V1.md`。File65 仍留給有效 M1–M4 量測後的 A0 loss-ledger closure。

## 3. 已讀關鍵轉折

序號為本次取得分支由舊到新的閱讀順序；turn ID 對應原對話。

| 位置 | 使用者主旨 | 保留的研究意圖 |
|---|---|---|
| Turn 12 — `66ae5eff-cd8f-4a40-8b61-1c7fabef9f04` | 多繞組／抽頭原本就是處理「電流怎麼扛」 | 功率分配是起點，不能縮成自激控制改良 |
| Turn 13 — `f8afed0b-9b32-48c9-8014-0512f6a4a5e9` | DC 進抽頭，MOS 形成 HF，希望结合升壓、50 Hz 與 220 V | 最終問題是 DC→AC，並非只完成 DC/DC |
| Turn 14 — `20f96bd0-b777-4cbd-8a99-664e98bed274` | 他激提供參考修正自激，加入 50 Hz 參數 | 外部修正疊加於自激功率 Cell；調變自由度待證 |
| Turn 15 — `61d96681-10b7-4d03-90dc-ac134f894a49` | 是否成立先看接線 | 逐狀態追電流，不能把繞組數直接當分流數 |
| Turn 16 — `d34a2feb-e11b-4034-9be2-18750f36e019` | 以 Royer 主、輔助、輸出繞組分工思考共磁芯限制 | 利用共用磁通，各初級不是自由 oscillator |
| Turn 17 — `422184df-3b8d-420d-96a2-88604b3145d2` | 成功驗證前先做數學理論 | 先定義圖與假設、守恆及磁性約束，再進模型／模擬 |

近期 turn 與 RH1/RH5/RH6 出處已列於上一版紀錄。尚未完整審讀的中段不能用來推定全部轉向原因；歷史助理的肯定也不代表使用者已接受定案。

## 4. 兩個研究對象分開建模

| 項目 | 原始共磁芯多初級構想 | 後期 RH1 多獨立 Host screen |
|---|---|---|
| 功率入口 | DC 分到多組初級／開關路徑 | DC 分到獨立 Cell |
| 磁性結構 | 同一磁芯／共用主磁通為起點 | 每 Cell 各自帶 HFT |
| 回授與振盪 | 共用磁性狀態作換相參考 | 同步與相位協調另行定義 |
| 功率合成 | 多初級共同向輸出繞組傳能 | 副邊電壓貢獻串聯 |
| 首要未解 | 合法狀態、差模／環流、均流、磁通平衡 | 精確串聯方式、頻率／相位、功率／電壓分享 |
| 結論地位 | 原始研究意圖，尚未驗證 | 比較架構，非已證明的等價實作 |

概念圖只表達角色，不是可直接模擬的接線圖：

```text
12 V → 多條 [功率初級 + 主 MOS] 路徑
                    │
               共用磁性結構
                ├─ F：回授／換相資訊
                └─ S：輸出功率
外部參考 → 修正自激條件
```

中心抽頭各半繞組、功能繞組與 PSIM winding sections 的計數必須分開。CT 兩半輪流導通，不等於兩條支路同時各承擔一半總電流。Gate driver 供電、訊號來源與 MOS Source 參考也須分別列出。

## 5. 已讀對話的約束與待證項

下列為脈絡補正，並非本輪新增的完整電路證明。

1. **Royer 保留完整功率角色。**主 MOS、CT HFT、磁性回授與自激換相共同構成此研究 Host；拆出 timing 做 prior-art 比較，不代表拿掉功率路徑。
2. **共用磁通不保證均流。**同主磁通模型的感應電壓按匝數／極性相關；端電壓還有漏感與電阻壓降。不能施加不相容的開關電壓，再假定電流自然等分。
3. **早分流不自動節省總損耗。**分叉前仍有總輸入電流；MOS 有效資源、銅材、磁件、熱條件與支援損耗須公平比較。
4. **自激不等於 ZVS。**換相機制與開通 VDS／電荷轉移條件分開驗證；ZVS 不能直接推出整機效率提升。
5. **50 Hz 包絡不等於負載端 50 Hz AC。**解調／極性換流、濾波、磁通復位與單相 2ω 能量去向仍須閉合。早期「初級 signed energy + LC」方向只能保留為未證假說。
6. **X1/X2/X3 是功能座標。**可研究物理重疊，但名稱重疊不是新穎性，也不能假定一顆 HFT 已完成全部 DC→AC 功能。
7. **數值尺度不是量測。**12 V / 2 kW 在理想、95% 假設、90% 假設下分別約 166.7、175.4、185.2 A。RH1 的 58.48 A/cell 是理想平均分配；336 V、112 V/cell、9.33 gain 不是確定匝比或 HF RMS。

搭配 [File28 功能定義](28_X1_X2_X3_AND_PHYSICAL_GAP_DEFINITION_V1.md)、[File33 組合損耗 gate](33_COMBINATION_LOSS_AUDIT_GATE.md) 及上一版的數值限制使用。HF 副邊直接串聯後整流與各自整流後 DC 串聯是不同電氣圖，不能共用未聲明的 RMS 結論。

## 6. 主線與待完成工作

**探索脈絡：**保留 Royer 實體 Host 與原始共磁芯多初級問題，將 RH1/RH5/RH6 作為已有 screen 對象；尚未選定最終實作，沒有新增 Candidate #10。

**正式證據主線：**[2026-08-20 override](CURRENT_MAINLINE_OVERRIDE_2026-08-20.md) 仍有效：File64 的 A0 M1–M4 量測與後續 matched ledger closure。本補充沒有證據可解除 gate 或宣稱量測完成。

下一步：

1. 完成全文逐段審讀、補讀截斷處與可存取附件查核，分別列出取得範圍、實讀範圍及缺失。
2. 追溯共磁芯構想到多 Host screen 的轉向，區分使用者決策、助理提案、否證結果與未決問題。
3. 為兩類對象分別建立端點、極性、回流路徑、合法狀態、磁性模型與均流條件；未閉合標記 OPEN。
4. 具體圖與波形足夠後，對齊 DC→AC 功能截面及資源，計算完整損耗。新增及交互作用損耗不可漏算，損耗轉移不能當移除。
5. 新穎性、數學可行性、PSIM 求解與硬體證據分別判定，不能互相替代。

## 7. 狀態

```text
Original shared-core multi-primary intent = RECOVERED_FROM_REVIEWED_TURNS
Equivalence to three independent hosts    = NOT_ESTABLISHED
Full conversation review                  = INCOMPLETE
Attachment review                         = INCOMPLETE
Current sharing / phase / exact graph     = OPEN
Matched total-loss advantage              = NOT_ESTABLISHED
Novelty                                   = NOT_ESTABLISHED
PSIM                                      = NOT_EXECUTED
Hardware                                  = NOT_EXECUTED
Candidate #10                             = HOLD / NOT_ASSIGNED
Formal A0 M1–M4 evidence mainline          = RETAINED
```

本次提交完成目前已核對內容的補充；完整歷史審讀仍是未完成工作。

