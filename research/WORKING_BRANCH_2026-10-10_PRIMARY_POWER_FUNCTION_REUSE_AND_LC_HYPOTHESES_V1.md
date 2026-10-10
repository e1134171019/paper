# 2026-10-10 — 一次側功率功能共用與 LC 假設 v1

Status：WORKING_BRANCH / NODE-CONTRACT / HYPOTHESIS / PRE-STATE-CLOSURE

```text
Novelty = NOT_ESTABLISHED
PSIM = NOT_EXECUTED
Hardware = NOT_EXECUTED
Candidate #10 = HOLD / NOT_ASSIGNED
```

## 1. 紀錄範圍與權限

本檔整理目前可見聊天與下列已讀、既有研究紀錄，不宣稱全部歷史對話及附件已審讀完成。
已讀 AGENTS.md、README.md、RESEARCH_STATE.md、09-18 整合收斂及兩份 09-26 S2 紀錄。
本次起草與交叉審查由內建代理執行；不是 OpenCode、Qwen 或本機 PSIM 的操作紀錄。
Wu Fig.1 接點沿用先前本對話的核對；Cho 僅作 closest 先例定位，本輪不宣稱重新審讀完整原論文。
本次只新增探索紀錄；沒有執行 PSIM、硬體、訓練、BOM 選型或參數最佳化。
正式 A0 M1–M4 量測主線保留，File65 仍留給有效量測後的正式 loss-ledger closure。
PSH-1、PSH-2、PSH-1L 是本檔命名，與既有 H1–H4 量測工作表不同。
本檔不重啟、不修復 09-26 的永久被動 LC Sketch A，也不更改其反證結論。

## 2. 固定研究邊界與尺度

| 項目 | 本檔契約 |
|---|---|
| 輸入 | 12 Vdc |
| 輸出 | 2 kW、220 Vac、單相、50 Hz |
| 理想平均輸入電流 | 2000 / 12 = 166.67 A |
| 95% 尺度假設 | 輸入平均電流 175.44 A、整機損耗 105.26 W |
| matched HV 比較點 | 350 V；須連同副邊、調變、濾波及功能契約一起匹配 |
| 336 V | 早期 screen 的比較值，不能當作目前量測或最後設計值 |

95% 只用於理解電流與損耗尺度，不是本候選的實測效率或已達成目標。
平均輸入電流不能直接替代每個 MOS bank、繞組、Cc/Ck 或 aux 支路的 RMS。
220 Vac 的正弦峰值約 311.13 V；220 / 12 不能直接當高頻變壓器匝比。
有效匝比還取決於 CT 半繞組或 full bridge、占空比、漏感占空損失與整流方式。
50 Hz 單相的 100 Hz 功率脈動及其緩衝位置仍未閉合，不能在一次側帳本消失。

## 3. 從聊天保留的研究問題

核心問題是主功率開關、繞組與磁性狀態能否兼任傳功、換相、復位或回收。
「多分支分流」「更多元件」「更少元件」均不能單獨證明總損耗下降。
ZVS 只是開通條件與局部損耗結果，不是整機低損耗或新穎性的證據。
多功率初級加耦合均衡仍可列入比較候選；目前撤回其優先排名。
Royer 保留實體 power host 的意義，不能只把磁性回授標籤貼到另一個功率級。
自激與 CT 是可研究維度，並非本次所有功率接線的硬約束；最佳方案尚未證明。
「同一磁件」需列入新增繞組、窗口、銅、漏感與核心負擔，不等於零新增成本。
本檔要求提出可反證的實際功率接線；只改閘極控制不能當作新的 power topology。

## 4. 已知來源與本案假設的分界

| 來源 | 可支持事項 | 本檔限制 |
|---|---|---|
| Wu 等，2008，DOI 10.1109/TIA.2007.912748 | CT 推挽、雙獨立主動箝位、漏感／Coss 換流與回收的已知基線 | 原型 40–60 V、1 kW、400 Vdc；不代表 12 V／2 kW 已驗證 |
| Cho 等，2000，DOI 10.1109/63.838097 | 變壓器輔助繞組參與 full-bridge 換相已有先例 | 不能據此稱 PSH-2 為原論文接線的復現或新穎 |
| TI SSZT951 官方文章 | 2 kW／48 V 例中，漏感及箝位關斷前電流決定 ZVS 範圍 | 是 current-fed full-bridge 案例，不能直接移植到本案 12 V |

下列 ASCII 及節點表是聊天提出的假設契約，不是來源原圖。
Wu 的原圖保留兩個獨立 Ca/Cb；PSH-1 合併 K 節點及電容是本案探索改動。
原圖中 Q3/Q4 有短暫同時導通狀態；不能套用「所有 aux 重疊均禁止」的通則。
本檔只提供來源連結，不加入下載的出版商 PDF；來源完整 prior-art closure 尚未完成。

## 5. 共通非理想模型與器件記號

P 為輸入正端，0 為輸入回路負端；Cin 永久接 P–0。
QA/QB 及主橋符號均代表功率開關 bank，實體並聯數尚未指定。
所有 MOS 必須列入自己的 nonlinear Qoss/Coss、body diode、RDS(on)、封裝及接線寄生。
所有主功率繞組與輔助繞組都需有限漏感、DCR/Rac、Lm 與共享磁通模型。
磁件狀態不是電氣節點；理想變壓器與理想開關不足以驗證本研究。
Cc/Ck 位於鉗位或耦合支路，Cin 持續接 P–0；支路回流及 ESL 仍須顯式保留。
下述狀態先聲明合法通路及準入條件，尚未構成自激 gate/startup 實作。

## 6. PSH-1：CT 兩臂共用箝位庫

假設：把已知雙箝位的兩個電容上端合成 K，以一個 Cc 讓兩臂交替存取換流能量。
同一主磁件包含 WA/WB 及傳功副邊；WA 點在 P，WB 點在 PB。
定義 iA 正方向 PA→LσA→A，iB 正方向 PB→LσB→B，vCc = V(K)−V(P)。

```text
P—WA—PA—LσA—A—QA—0       WA dot = P
P—WB—PB—LσB—B—QB—0       WB dot = PB
QcA：D=K，S=A；body A→K
QcB：D=K，S=B；body B→K
QA：D=A，S=0；body 0→A
QB：D=B，S=0；body 0→B
Cc：K—P；Cin：P—0
Coss：每個 MOS 各自跨 D—S
```

兩半繞組的理想磁性部分滿足 V(P)−V(PA)=V(PB)−V(P)，漏感另行保留。
QcA/QcB 的 gate 均須以自己的 S 節點為參考，不能假設是共地驅動。

## 7. PSH-1：三主要狀態與鏡像

| 狀態 | 開關／准入 | 封閉電流路徑與能量意義 |
|---|---|---|
| T-A 傳功 | QA、QcB ON；QB、QcA OFF | P→WA→LσA→QA→0→輸入→P；Cc 可經 K→QcB→LσB→WB→P→Cc→K 釋能 |
| K-AB 收能 | QA OFF，QcB 暫留 ON；Coss 換充後 QcA body 導通才接手 | P→WA→LσA→A→QcA body→K→Cc→P；A 支路能量進共用庫 |
| T-B 準入 | QcA 保持 ON，QcB OFF；先確認 iB<0 且 Qoss 搬移完成，再開 QB | 0→QB body→B→LσB→WB→P→Cin→0；隨後 P→WB→LσB→QB→0→輸入→P 傳功 |

每個路徑箭頭代表該電流符號成立時的通路，不保證任意負載或初值都能取得此符號。
鏡像半週期交換 A/B、QA/QB、QcA/QcB，T-A 準入要求 iA<0。
收能階段允許兩個 Qc 短時重疊；兩主開關均 OFF，且保留有限 LσA/LσB。
禁止 QA 與 QcA、QB 與 QcB 的無死區直通；具體死區及故障狀態仍待定義。
負向支路電流是換流初始條件；不能由「電容共用」直接推得其必然存在。

## 8. PSH-1：待證的週期、磁通與損耗

兩 Qc 導通時 A=B≈P+vCc，理想半繞組的電壓約束由漏感電壓補足。
此處 v=V(P)−V(PA)=V(PB)−V(P)，iA/iB 方向沿用上一節。
忽略 R 與換充的瞬態簡式為 LσA·diA/dt=−v−vCc、LσB·diB/dt=v−vCc。
兩式相加為 −2vCc；漏感設為零會產生不相容約束，重疊過長可能累積過大反向電流與 RMS。
主 MOS 入場須同時驗證電流符號、可用時間內的 ∫i dt 與 nonlinear ΔQoss。
Eoss 能量足夠只是必要條件，還需閘極時刻、VDS、dv/dt 與 body recovery 合法。
共用 Cc 的整週期 ∫iCc dt=0、vCc 有界及磁通伏秒平衡均尚未證明。
K 節點完整 KCL 必須含兩個 aux Coss；通態近似才可寫 Cc·dvCc/dt=iQcA+iQcB。
原 Ca/Cb 的獨立偏壓被移除，原基線的個別偏壓／磁通校正論證不能沿用。
aux 可能承受反射傳功與復位電流，不能按「微小漏能」猜測其 RMS 或器件尺寸。
主要反證：iB 未反向、Cc 漂壓、偏磁、aux RMS 過大、漏感占空損失或反向恢復失控。
最終假設是共用庫可減少增量負擔；電容數減少本身不構成低損耗證明。

## 9. PSH-1L：共用庫前加入 Lr 的待驗變體

```text
QcA：D=K0，S=A；body A→K0
QcB：D=K0，S=B；body B→K0
K0—Lr—K；Cc：K—P
其餘 WA/WB、LσA/LσB、QA/QB、Cin 與 Coss 保留
```

PSH-1 本來已有 Lσ、Cc 與各管 Coss，不能說原來「只有 C」、加 L 才有換流。
Lr 的假設用途是限制共用庫電流斜率或提供可調換流尺度，是否淨有利仍未知。
關斷瞬間的電流先改充 Coss；Lr 電流不能瞬變，K0 的立即鉗位可能因此延遲。
VDS 過衝可增加，還須包含 Lr DCR、核心損耗、Cc ESR/ESL 與佈線 ESL。
原 PSH-1 狀態需重新寫 K0/K 的 KCL，不能複製同一個瞬間鉗位電壓。
定義 iLr 正方向 K0→K，則 V(K0)−V(P)=Lr·diLr/dt+vCc；此式尚忽略 Lr DCR。
Lr/Cc 的自然頻率不等於自激 gate 決策，也沒有解決啟動、偏磁或電容初值。
若新增 Lr 的 RMS／磁性損耗超過省下的切換損耗，就反證此變體。

## 10. PSH-2：非 CT 主橋加耦合換相繞組

假設：保留一套主功率磁件，用同磁芯 Wk 的短時電流脈衝協助主橋 Coss 搬移。
主繞組 Wp 為 A(dot)–B；其漏感與 Lm 保留，副邊仍是待定的反射負載邊界。
Wk 實體端口為 K+(dot)–K−，與 Wp 同點極性，保留有限 Lσk。
展開等效模型時可用理想 Wk 的 Uk+(dot)–K−，再接 Uk+–Lσk–K+。
定義 iK>0 為 K+→Ck→X→Qk1→J→Qk2→K−，vCk=V(K+)−V(X)。
Vk 是理想耦合繞組感應電壓的幅值；vk=V(Uk+)−V(K−)，與主 Wp 電壓同號。
pK=vk·iK；pK>0 表示理想耦合繞組向換相支路送能，pK<0 表示支路向磁件回送能量。

| 器件 | D／S 與 body diode |
|---|---|
| QAH | D=P、S=A；body A→P |
| QAL | D=A、S=0；body 0→A |
| QBH | D=P、S=B；body B→P |
| QBL | D=B、S=0；body 0→B |
| Qk1 | D=X、S=J；body J→X |
| Qk2 | D=K−、S=J；body J→K− |

Ck 接 K+–X；兩 N-MOS 採 common-source J 的背對背串接，ON 才連通 X–K−。
兩管 OFF 阻擋雙向通道，但各管 Coss 與浮動 J 的位移電流仍須納入。
Cin 接 P–0，各主橋與 aux MOS 的 Coss 均跨自己的 D–S。
Wp/Wk 的額外窗口、銅、耦合、絕緣與漏感成本必須入帳，未指派實體 BOM。

## 11. PSH-2：傳功尾段、換流與回收假設

| 狀態 | 接線行為 | 功率／電流路徑 |
|---|---|---|
| T+ | QAH、QBL ON，Qk1/Qk2 OFF | P→QAH→A→Wp→B→QBL→0→輸入→P |
| P+ 尾段 | 主正向對仍 ON，Qk1/Qk2 ON | Wk 的 K+→Ck→X→Qk1→J→Qk2→K−→Wk→K+ 建立 iK>0 的額外短脈衝 |
| K+→T− | 關正向主對，aux 暫保持；淨 Wp 電流須為 A→B | Coss 搬移令 A 下降、B 上升；完成後 0→QAL body→A→Wp→B→QBH body→P→Cin→0 |
| T− 回收尾 | VDS/Qoss 準入後開 QAL、QBH；保持 aux 至 iK 回零 | vk<0 且 iK>0 時 pK<0，支路向磁件回送能量；iK 回零才關 Qk1/Qk2 |

鏡像從 T− 的尾段建立 iK<0，再搬移 B→低、A→高，進入 T+。
Wp 的耦合電流與實際副邊反射電流相加，決定 Coss 的淨搬移，不能只檢查 iK。
正向尾段若 vCk≈−Vk，而繞組感應電壓為 +Vk，差壓可刻意建立正向脈衝。
翻相後感應電壓為 −Vk，脈衝可減至零，Ck 偏壓轉向正值；此過程尚待積分驗證。
±Vk 的 Ck 初值只是對稱週期軌道假設，不是零能量啟動或穩定性證明。
此處確實增加短時電流與安匝；不能說只是搬已有負載電流、沒有額外電流。
回送磁件的能量可通往輸入或負載，份額需由完整副邊狀態與瞬時功率積分辨識。
iK 未回零即關斷 aux 會切斷漏感電流；不得用 avalanche 或 Coss 偶然吸收當正常閉合。
Wp/Wk 伏秒、Ck 電荷、浮動 J 與全週期初末狀態相等皆未證明。

## 12. 自激、gate 與啟動仍待實作

磁性回授可提供換相 request，VDS-ready/Qoss 準入可提供接手條件；兩者不是功率路徑。
PSH-1/PSH-2 的 gate 極性、延遲、鎖定、防直通與限頻網路尚未實現。
核心飽和不能自動保證 ZVS；磁通有界、啟動選邊、無載及故障復歸均需獨立設計。
主橋改成外部激勵也可以作 matched 對照，自激不享有預設優勢。
本檔兩個主假設都不是完整的 220 Vac converter；AC 合成、濾波與 2ω 緩衝仍開放。

## 13. 比較帳本及立即可反證的下一步

先比較已知雙獨立箝位、PSH-1、PSH-1L、PSH-2；不預先排序。
匹配 Vin/Pout/HV-domain、頻率範圍、半導體導通資源、銅/core 資源及產品功能。
功率帳包括主／aux 導通、切換、body recovery、gate、繞組／端接、core、ESR 與循環 RMS。
每一新增 L、C、繞組或開關都標記省下、保留、搬移與新產生的物理 watt 項。
局部回收閉合不等於損耗消失；PSH-1 的 aux 與 PSH-2 的額外脈衝都需單獨積分。
在固定 HF operating point 檢查 x(Ts)=x(0)；線週期再檢查 20 ms 的有界重複狀態。
下一步只先做各狀態 KCL／KVL、nonlinear Qoss、電流準入、電容與磁通週期性反證。
再建立同邊界比較帳，確認 P_saved>P_added 及總損耗不確定性；未通過便淘汰。
PSIM 是另行工作；本次沒有建立、修復或執行任何模型，不能更新執行狀態。
保留 Novelty NOT_ESTABLISHED、Hardware NOT_EXECUTED、Candidate #10 HOLD / NOT_ASSIGNED。

## 14. 可追溯來源

- [09-18 整合範圍與第一電路計畫](WORKING_BRANCH_2026-09-18_INTEGRATION_SCOPE_CONVERGENCE_AND_FIRST_CIRCUIT_PLAN_V1.md)
- [09-26 S2 first-circuit contract](WORKING_BRANCH_2026-09-26_S2_REFERENCE_FIRST_CIRCUIT_CONTRACT_V1.md)
- [09-26 Sketch A closure/falsification](WORKING_BRANCH_2026-09-26_S2_SKETCH_A_SYMBOLIC_CLOSURE_AND_FALSIFICATION_V1.md)
- [既有研究狀態](RESEARCH_STATE.md)；[正式 A0 主線 override](CURRENT_MAINLINE_OVERRIDE_2026-08-20.md)
- [Wu 2008 DOI](https://doi.org/10.1109/TIA.2007.912748)；[Cho 2000 DOI](https://doi.org/10.1109/63.838097)
- [TI 官方 SSZT951](https://www.ti.com/document-viewer/lit/html/SSZT951/GUID-69E9CB24-4059-4DA1-AF3C-582A1A711164)
