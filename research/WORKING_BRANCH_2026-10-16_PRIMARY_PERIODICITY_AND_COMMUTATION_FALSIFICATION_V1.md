# 2026-10-16 — 一次側週期性、換流準入與反證 v1

Status：WORKING_BRANCH / HYPOTHESIS / REDUCED-MODEL-PERIOD-MAP / NOT-FULL-SYSTEM-CLOSURE

```text
Novelty = NOT_ESTABLISHED
PSIM = NOT_EXECUTED
Hardware = NOT_EXECUTED
Candidate #10 = HOLD / NOT_ASSIGNED
```

## 1. 口白摘要與本次邊界

「換相電流已經回到零」只表示一個關斷事件到達，電容偏壓、磁通與其他電流仍可能逐次漂移。
因此回零、回送能量、單次 ZVS、支路固定點及整機低損耗，是不同層級的命題。
PSH-1 未發現共用 Cc 必然短路的普遍反證，但兩臂電荷、磁通與負電流準入尚未全週閉合。
PSH-1L 必須另解 K0 與連續的 iLr；雙 aux OFF 的風險只能套用到真的指定此狀態的事件契約。
PSH-2 在外部強制 ±Vk 的理想支路模型有條件固定點，也有「每次回零卻偏壓漂移」的具體反例。
這些結果均不代表 12 V／2 kW 主橋 ZVS、效率、自激、完整啟動或 220 Vac 功能已成立。

共同錨點仍為 12 Vdc／2 kW／220 Vac、單相 50 Hz，目標是整機總損耗下降。
2000/12=166.67 A 只是理想平均輸入尺度；95% 仍是尺度假設，不是成果。
50 Hz 不是下文 HF 開關頻率，Vk 也不能直接代成 12 V。
本輪不新增候選、元件、BOM 或補救電路，不重做廣泛 prior-art 搜尋。
[現行主線 override](CURRENT_MAINLINE_OVERRIDE_2026-08-20.md) 所定 A0 M1–M4 採證、File65 門檻與帳本權限不變。
既有永久被動 LC Sketch A 的反證保留；本輪不重啟、不修復，也不以新映射回改其結論。

## 2. 節點權限與共通閉合要求

[10/10 原稿](WORKING_BRANCH_2026-10-10_PRIMARY_POWER_FUNCTION_REUSE_AND_LC_HYPOTHESES_V1.md) 第 5–13 節仍是接線權限，本檔只追加推導。
PSH-1 沿用 §6–9：P–WA–PA–LσA–A–QA–0；P–WB–PB–LσB–B–QB–0；WA 點在 P、WB 點在 PB。
QcA 為 D=K/S=A、body A→K；QcB 為 D=K/S=B、body B→K；Cc=K–P、Cin=P–0。
PSH-1L 只將兩 aux 的 D 改至 K0，再以 K0–Lr–K 接至原 Cc；其餘節點不變。
PSH-2 沿用 §10–11：Wp=A(dot)–B；理想 Wk=Uk+(dot)–K−，Uk+–Lσk–K+；Ck=K+–X。
Qk1 為 D=X/S=J，Qk2 為 D=K−/S=J，共 source J；兩管 ON 才連通 X–K−。
其 body 分別 J→X、J→K−，OFF 不形成雙向直流串通，但有限 Coss／浮動 J 的位移電流不能刪除。

固定線相位的 HF 篩查至少要求 x(Ts)=x(0)，涵蓋漏感電流、磁通、電容電荷、寄生與副邊狀態。
必要條件包括繞組伏秒、電容電荷與能量帳閉合，且每次事件在允許時間內合法到達。
全機還需 20 ms 有界重複與 100 Hz 功率緩衝；HF 支路零淨能量不能使這些要求消失。
必要積分成立不保證週期軌道存在、可達或穩定；指定週期初值也不是啟動證據。

## 3. PSH-1：KCL、body diode 與 nonlinear Qoss 準入

令 A/B/K 為對 0 電壓，Vc=K−P；iA/iB 正向仍為繞組流向 A/B，v=P−PA=PB−P=N·dΦ/dt。
mA 是 A→0 的帶符號主管導電電流，cA 是 A→K 的帶符號 aux 導電電流，B 同理。
qmA=qoss,QA(A)、qcA=qoss,QcA(K−A)，均為 drain 端電荷，dq/dV=Coss(V)，不是常數 C 乘電壓。
```text
LσA·diA/dt = P−v−A−RA·iA
LσB·diB/dt = P+v−B−RB·iB
iA = mA+cA+dqmA/dt−dqcA/dt                    （B 鏡像）
cA+cB = Cc·dVc/dt+dqcA/dt+dqcB/dt
iA−iB = im+i's；線性區 v=Lm·dim/dt
```
i's 是抵銷副邊安匝的等效負載電流，必須由實際副邊狀態決定，不能任意另指定兩臂與 v。
body 的理想鉗位為 A,B≥0 及 A,B≤K；實際以各自 Vf、寄生及恢復電流修正。
T-A 的 QA/QcB ON 給 A≈0、B≈K=P+Vc；正 Vc 並未自動造成共用庫直通。
若 P=12、Vc=−24 V，指定 B=−12 V 立即被 QB body 打破；這反證任意初值合法，未反證正偏壓工作域。

雙 Qc ON、雙主 OFF 時 A=B≈P+Vc，漏感式化為 −v−Vc 與 v−Vc 的驅動差壓。
零漏感、零電阻且 Vc≠0 會同時要求 v=−Vc 與 v=+Vc，屬不相容極限。
有限漏感則承擔差壓；等 Lσ=L、R=0、固定 i's 時可有局部 v=0，且
```text
CΣ(Vc)·dVc/dt=iA+iB；d(iA+iB)/dt=−2Vc/L
CΣ=Cc+Coss,QA(P+Vc)+Coss,QB(P+Vc)>0
```
這給出 P+Vc>0 短區間的局部一致狀態，不是全週解；長重疊仍可能推高反向電流與 RMS。

QcA ON、QcB OFF、QB 未入場且 body 尚未接手時，由 B 節點積分：
```text
∫(−iB)dt = qmB(Bi)−qmB(Bf)+qcB(Kf−Bf)−qcB(Ki−Bi)
```
此處下標 i/f 是換流起終時刻，Ki 是共用 K 的起始電壓，不是 PSH-1L 的實體 K0 節點。
若 Bi=Ki、Bf≈0，必須放掉主 QB 的電荷並充入 aux QcB 的電荷；只算主管 Qoss 會低估需求。
寄生、diode 已導通區間與 gate 延遲須另納入；到達低壓後 iB<0 才能維持 QB body 接手，A 鏡像。
K 固定為正且整個死區 iB≥0 時，要求的搬移電荷為正而左式≤0，該次 ZVS 不可達。
能量足夠或某瞬間負電流均不替代此積分；∫(cA+cB)dt=0、磁通有界與兩臂準入仍待全週求解。

## 4. PSH-1L：K0 與 iLr 連續性

令 iLr 正向 K0→K，兩 aux 的電荷改為 qcA=qoss,QcA(K0−A)，B 同理。
```text
cA+cB=iLr+dqcA/dt+dqcB/dt；Cc·dVc/dt=iLr
K0−P=Vc+Lr·diLr/dt+Rr·iLr
```
雙 aux ON 時 A=B≈K0，兩漏感驅動式須以 K0−P 取代 Vc；不能把 K 的電壓當即時箝位值。
有限電壓下 iLr 連續；週期另要求 ∫iLr dt=0 及 ∫(K0−K−Rr·iLr)dt=0。
若另定 deadtime、啟動或故障情境讓兩 aux 均 OFF，A/B 暫近固定且 body 未導通時，有 d(qcA+qcB)/dt=−iLr。
此時正 iLr 拉低 K0、可能觸發 aux body，負 iLr 推高 K0，而 body A/B→K0 不能將上衝送回較低臂節點。
這是該雙 OFF 情境的續流／應力查核；原正常序列可由另一 aux 續接，不能宣稱其必然斷流。
是否實際出現此情境、Coss 能否接續及下一事件是否及時到達，均由尚待明定的契約決定。

## 5. PSH-2：受限理想支路的事件映射

沿用 iK>0：K+→Ck→X→Qk1→J→Qk2→K−；vCk=K+−X、vk=Uk+−K−、pK=vk·iK。
本節外部指定 vk=±V，V=Vk>0；L=Lσk>0、C=Ck>0、ω=1/√LC、Z=√(L/C)。
暫刪 R、所有 Coss 與浮動 J；ON 滿足 L·diK/dt=vk−vCk、C·dvCk/dt=iK，OFF 假設 iK=0、vCk 保持。
翻相是外部理想瞬時事件，iK/vCk 連續；真實主橋換充中的 vk 不能預設已完成此翻相。
每個脈衝從 iK=0 開始，源為 sV、s=±1，尾段定時 τ，α=ωτ，a=s·vCk,start/V、d=1−a。
取 d>0、0<α<π，才有期望 s 方向脈衝且尾段翻相前未先回零；其他初值不屬此事件分支。
令 x=ωt、u=s·vCk/V、j=sZiK/V；尾段及翻相後 y=ω(t−τ) 的解為：
```text
尾段：j=d sin x；u=1−d cos x                   （0≤x≤α）
b=d sinα；h=2−d cosα
回收：j=b cos y−h sin y；u=−1+h cos y+b sin y
β=atan2(b,h)∈(0,π)；D=√(b²+h²)=√(d²+4−4d cosα)
首次回零：iK,end=0；vCk,end=sV(D−1)
```
回收段 s·iK>0、pK<0；只在第一次回零 β/ω 時關斷。h<0 時回收電流先升再降，翻相時刻未必是峰值。
下一源符號變為 −s，因此 a'=1−D、d'=D，得到半週 F(d) 與全週 F∘F：
```text
F(d)=√(d²+4−4d cosα)；d[n+1]=F(d[n])
vCk[n]=(−1)^n s0 V(1−d[n])
0<α<π/2：d*=secα；β*=α
vCk,start=sV(1−secα)；vCk,end=sV(secα−1)
F'(d*)=−cos(2α)；λfull=cos²(2α)<1
```
這是固定定時、理想回零事件映射的局部穩定性；不含主橋、gate、自激或全機穩定性。
該 α 域內正 d 軌道收斂至唯一固定點；原先假設偏壓 −sV→+sV 只在 α=π/3 成立。
從零 Ck 偏壓 d0=1 可在這些外部事件已存在的前提下收斂，但不證明全機零能量啟動。
任意初值的 β 隨狀態改變；不能把固定 α 的定時關斷當成通用回零偵測。
α=π/2 時 d[n]²=d[0]²+4n；π/2<α<π 時 d 持續增加，無有限固定點。
取 α=π/2、vCk,start=−sV，即 d0=2：每次回零仍有幅值 V[2√(n+1)−1] 漂移。
第一半週終值已為 s(2√2−1)V≈s·1.828V，反證「回零便自行停在 ±V」。
此無界結論只適用 R=0；小正 R 仍可使單次 ±V 不閉合，但不能直接宣稱有阻尼後也必然無界。
α=0 無所需脈衝，α≥π 退出本事件分支；不能把上述失敗域擴大成全部 PSH-2 不可行。

## 6. 事件時間、電流與新增損耗

令 Th 為相鄰翻相時間，兩次尾段要不重疊，須 α+β<ωTh；固定點為 2α<ωTh，Ts=2Th。
若沒及時回零、vk 未維持到 β 或下一次尾段已開始，前述映射不適用。
令 g(z)=z/2−sin(2z)/4，每脈衝的電荷與電流平方積分為：
```text
Qpulse=sCV(d+D−2)
S2=∫iK²dt=(V/Z)²[d²g(α)+D²g(β)]/ω
尾段峰值=(V/Z)d sin(min(α,π/2))
回收峰值=(V/Z)b （h≥0）；(V/Z)D （h<0）；Ipk 取兩段較大值
固定點：Ipk=(V/Z)tanα
Irms²=2S2/Ts=2(V/Z)²[α−sin(2α)/2]/(ωTs cos²α)
Ein,tail=CV²(secα−1)；Ereturn=−Ein,tail；ΔEfull=0
```
每全週兩脈衝處理 2Ein,tail；理想零淨能量仍有循環電流，α 接近 π/2 時偏壓／峰值急增。
一階新增導通代價為 RΣ·Irms²，RΣ 包含 Wk／漏感銅阻、Ck ESR 與兩 MOS 通道。
若兩管每全週各開通兩次，gate 代價約 4QgVg/Ts；另計 Coss、磁芯、恢復與驅動實耗。
反射到 Wp 的電流乘 Nk/Np；主橋總 RMS 必須保留與負載電流的交叉項。
加入損耗後須重求固定點；理想 ΔE=0 不代表能量回到輸入的份額或總 loss 降低。

## 7. 獨立數值查核與 provenance

三個內建代理分別完成 PSH-1／1L 節點查核、PSH-2 解析映射與獨立 red-team 交叉查核；本檔綜合其推導。
root 另以歸一化 V=L=C=1、di/dt=e−v、dv/dt=i 的 RK4 積分查核，而非僅把解析式再代入一次。
[數值紀錄](WORKING_BRANCH_2026-10-16_PRIMARY_PERIODICITY_NUMERIC_CHECK_V1.json) 保存步長 0.0005、八個端值案例與三組有限差分。
八案例涵蓋 α=0.3、π/3、1.5、π/2，vstart=0 或 −1；與解析端值最大絕對差 8.23×10⁻⁸。
全週 multiplier 的解析／有限差分交叉檢查如下，角度均為 rad：

| α | d* | λfull 解析 | λfull 有限差分 |
|---|---:|---:|---:|
| 0.3 | 1.0467516015 | 0.6811788772 | 0.6811788771 |
| π/3 | 2.0000000000 | 0.2500000000 | 0.2499999998 |
| 1.5 | 14.1368329030 | 0.9800851433 | 0.9800851419 |

α=1.5 從零偏壓迭代 200 半週仍為 d=13.4096205370，未到固定點；有限次迭代不替代週期證明。
RK4 與有限差分只查核受限支路算式，未包含主橋、副邊、Coss／J、器件、啟動或線週期。
這是數值計算，不是 PSIM、硬體或全機模擬；四項執行／候選狀態不因此升級。
本機 OpenCode 1.18.32／ollama/qwen2.5:14b 另有兩次嘗試；首輪無結果，次輪輸出未通過查核，不列理論結論佐證。

## 8. 當前決策與唯一下一步

PSH-1、PSH-1L、PSH-2 全數維持 HYPOTHESIS；本輪未找到可一概判死三者的拓撲矛盾，也未建立效率排名。
支路固定點不等於主橋完成 Coss 換充；反向電流準入不等於達成該電流的機制。
節省項必須大於新增主／aux、磁性、ESR、gate 與循環損耗，且在匹配資源和不確定性下仍成立。
本探索分支下一步唯一 action：先明定含副邊反射電流與主橋 nonlinear Coss 的 PSH-2 事件契約。
契約須定義主橋 OFF→diode-ready→gate 接手、實際 vk(t)、iK 回零關斷及完整狀態向量，才可判定映射能否保留。
這只是採證順序，不是效率排名或 Candidate #10 指派；正式 A0 M1–M4 主線與 File65 門檻保持不變。
