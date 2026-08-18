# 低壓大電流 DC→AC — Current Research State

> 狀態日期：2026-08-19  
> 文件用途：只保存「現在研究走到哪裡」。詳細推理拆分到 `research/01_...11_...`。  
> Novelty：`NOT_ESTABLISHED`。搜尋不到完整匹配不得直接寫成 Research Gap。

## 1. Current phase

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

目前已不再泛搜「哪個拓撲效率最高」，而是驗證 extreme-low-voltage/high-current 條件下：

```text
哪些 current / energy components
真的穿越昂貴的 LV full-current path？

哪些結構改變能降低總 loss，
而不是只把 loss 搬到別處？
```

---

## 2. Research envelope

```text
Vin     = 12–24 Vdc
Pout    = 1–3 kW
Vout    = 220 Vac
Phase   = single phase / 1φ
Primary anchor = 12 V / 2 kW
```

12 V / 2 kW：

```text
I_in,ideal = 2000 / 12 ≈ 166.7 A
```

若以前級 95% 估算：

```text
I_in ≈ 175.4 A
```

若低壓 conduction budget 只允許 20 W：

```text
R_eq,max ≈ 0.65 mΩ
```

因此研究的核心不是單純 voltage gain，而是 hundred-ampere current path 的 RMS / resistance exposure。

---

## 3. Core research question

> **不是研究怎麼升壓，而是研究 12 V 的能量怎麼走，才最少變成熱。**

研究把能量 / 電流分成：

```text
average real power
2ω pulsating power
switching ripple
reactive / resonant / circulating energy
leakage / commutation energy
```

概念上：

```text
i_LV = I_avg
     + i_2ω
     + i_switching
     + i_circulating
     + i_reactive
     + i_commutation
```

必要平均功率電流無法在 X1 前消失；研究真正能改變的是哪些額外 RMS 分量也穿越最昂貴的低壓共同路徑。

---

## 4. Structural coordinates

```text
X1 = first major impedance / current-domain transformation
X2 = local 2ω / bidirectional buffer / recycling coordinate
X3 = complete AC synthesis coordinate
```

Important correction:

```text
X1 / X2 / X3 are functional coordinates,
not automatically three additional converter stages.
```

Current preferred ordering:

```text
extreme-LV full-current domain
↓
X1
↓
reduced-current domain
↓
[X2 if net-beneficial]
↓
X3
```

The reason is to avoid performing unnecessary RMS circulation or complete AC synthesis in the 12 V hundred-ampere domain.

---

## 5. Nine working main power-path families

```text
#01 Low-Frequency Transformer Inverter
#02 HFT + Rectifier + HV DC Bus + VSI
#03 Active-HFT / DAB + VSI
#04 Non-Isolated High-Gain DC/DC + VSI
#05 Bidirectional DC/DC + VSI
#06 Single-Stage Boost / Buck-Boost Inverter
#07 Z-Source / Quasi-Z-Source
#08 Switched-Capacitor / Multilevel Main Path
#09 Direct High-Frequency-Link DC–AC
```

Current first-pass family status:

```text
#01 = REFERENCE ONLY / POOR FIT for extreme-LV loss minimization
#02 = PRIMARY REAL-PRODUCT / EARLY-X1 BENCHMARK
#03 = PRIMARY ACTIVE-HFT / EARLY-X1 BENCHMARK
#04 = PRIMARY CURRENT-DISTRIBUTION / NON-ISOLATED BENCHMARK
#05 = KEEP AS ENERGY-ROUTING MECHANISM
#06 = HOLD / VERY HIGH CURRENT-STRESS RISK
#07 = HOLD / HIGH-RISK AT 12 V
#08 = HOLD / HIGH-RISK AT EXTREME LV
#09 = PRIMARY MODERN DIRECT-HFL BENCHMARK
```

`IPOS / modular / current sharing / matrix / capacitive isolation / active buffer / partial power / ZVS-ZCS` remain orthogonal design dimensions and do not automatically create a new numbered family.

---

## 6. Product reality check — ASP-2000 R52

The user-supplied ASP-2000 MAIN R52 Altium source has now been directly inspected at component/stage level.

Verified product-level structure includes:

```text
2 × PQ5050 HFT modules
4 × low-side switch banks
5 parallel LV MOS devices per bank
20 LV main MOS positions total
8 high-current input fuse positions
2 groups of low-voltage bulk capacitance
4 HV rectifier devices
HV DC-link / BUS capacitor region
separate post-bus HV AC-synthesis stage
```

Research abstraction:

```text
Battery / LV input
→ fuse / LV current distribution
→ local LV bulk
→ parallel low-side MOS banks
→ T1 / T2 HFT                       ← X1
→ HV rectification
→ HV DC-link / BUS                  ← passive X2-capable node
→ HV inverter                       ← X3
→ AC
```

Status:

```text
ASP-2000 R52 = A0 REAL-PRODUCT BENCHMARK
```

Detailed evidence boundary:

```text
research/10_ASP2000_PRODUCT_BASELINE.md
```

Important consequence:

```text
parallel MOS
multiple HFT paths
current sharing
early distribution
```

are already present in the real product and cannot be treated as candidate novelty or automatic efficiency advantage.

---

## 7. Current working architecture — retained

The current candidate framework is kept:

```text
12 V source
↓
very-short / very-low-R common LV path
↓
local bulk + HF decoupling
↓
early distributed branch power cells
↓
branch switching + X1
↓
reduced-current domain
↓
[X2 active 2ω buffer — optional / must prove benefit]
↓
X3
↓
220 Vac / 1φ
```

Status by block:

```text
very-short common LV path      = KEEP / PHYSICAL REQUIREMENT
local decoupling               = KEEP / ENGINEERING REQUIREMENT
early current distribution     = KEEP AS HYPOTHESIS
branch switching + X1          = CORE RESEARCH REGION
reduced-current node           = KEEP AS FUNCTIONAL CONCEPT
active X2 buffer               = OPTIONAL / NOT YET PROVEN
X3 after X1                    = KEEP / STRUCTURAL REQUIREMENT
```

Detailed loss audit:

```text
research/11_WORKING_ARCHITECTURE_LOSS_AUDIT.md
```

---

## 8. Critical corrections after loss audit

### 8.1 Early fan-out is not automatically loss-saving

Splitting:

```text
175 A → N lower-current branches
```

does not by itself guarantee lower total copper loss if total conductor cross-section is unchanged.

Added branch penalties include:

```text
more interconnect
current-sharing error
more gate-drive power
more Coss / Qoss / Qg
parasitic-inductance mismatch
possible branch circulation
EMI / control burden
```

Therefore N is an optimization variable.

### 8.2 Active X2 is not mandatory

Post-X1 placement is physically attractive because the same pulsating power can be processed at lower current, but active buffering adds:

```text
switch conduction / switching
inductor copper / core
capacitor ESR / dielectric
buffer RMS
control / auxiliary
extra commutation / circulation
```

Required gate:

```text
Buffer OFF vs Buffer ON
P_LV,saved > P_X2,added
```

If the existing passive HV DC-link already suppresses source 2ω sufficiently, active X2 must be removed or restructured.

---

## 9. Physical anchor for 2ω hypothesis

For unity-PF single-phase output:

```text
p_out(t) = P_avg [1 - cos(2ωt)]
```

If the source were forced to supply the complete pulsation at fixed voltage:

```text
I_RMS = sqrt(3/2) I_avg ≈ 1.225 I_avg
```

so the same LV resistance would see up to:

```text
1.5 × I_avg²R
```

relative to pure average DC current.

This remains a mechanism upper-bound / comparison model, **not** a claim that ASP necessarily exhibits the complete waveform.

For 2 kW / 60 Hz:

```text
ΔE_amp ≈ 2.65 J
ΔE_pp  ≈ 5.31 J
```

The actual source 100/120 Hz current must be measured or modeled from the real A0 dynamics.

---

## 10. Prior-art / novelty boundary

Broad concepts already closed as standalone novelty include:

```text
High-gain conversion
IPOS / modular conversion
parallel current sharing
DAB / active isolated conversion
Direct HFL DC–AC
Bidirectional battery/HV-bus conversion
APD / PPB
partial-power / series-stacked buffer
HF-link ripple port / integrated buffer
CPT / capacitive isolation
kW-class capacitive conversion
capacitively isolated inverter
high-ratio capacitively isolated conversion
```

Therefore:

```text
Electric-field + Buffer
```

is not itself a research gap.

Current narrow intersection remains:

```text
OPEN_INTERSECTION
NOVELTY_NOT_ESTABLISHED
```

until a materially different power/energy path is demonstrated and prior-art closure survives.

---

## 11. Required benchmark stack

Current matched benchmark set:

```text
A0 — actual ASP-2000 R52 product abstraction
A1 — optimized matched modular-HFT benchmark
B  — Direct High-Frequency-Link DC–AC
C  — non-isolated current-distribution / high-gain
D  — working candidate architecture
```

A1 is required because a new N-branch candidate may not be compared against an artificially monolithic magnetic baseline.

Benchmark details:

```text
research/07_BENCHMARKS.md
```

---

## 12. Current validation gate

First system-level tool remains:

```text
PLECS
```

But the first model should now be grounded in A0/A1 rather than a generic converter only.

Required mechanism questions:

```text
Q1 — Where is A0 loss concentrated from battery to X1?

Q2 — Does early current distribution reduce total declared R_eq / I²R
     versus A0 and a fair A1 magnetic benchmark?

Q3 — Which X1 class gives the lowest matched total loss:
     magnetic HFT, non-isolated high-gain, or Direct HFL?

Q4 — Does active post-X1 2ω buffering produce positive net saved loss
     versus the passive DC-link baseline?
```

Required measurements / model outputs:

```text
I_source,avg
I_source,RMS
I_source,2ω
I_source,HF
per-bank / per-branch IRMS
T1/T2 primary IRMS for A0
R_common
P_MOS,cond
P_MOS,sw
P_magnetic
P_rectifier
P_cap
P_circulating
P_buffer
P_total
```

Go condition for every structural addition:

```text
P_saved > P_added
```

---

## 13. What remains unverified in A0

Do not infer yet:

```text
exact T1/T2 turns ratio
exact switching frequency
exact low-side modulation / bridge class
exact device current sharing
exact PCB copper Rdc/Rac
exact leakage / clamp processed power
exact DC-link 100/120 Hz ripple
exact source 100/120 Hz current
exact 110 V / 220 V BOM population variants
measured stage efficiency
thermal distribution
```

These require full net reconstruction, BOM/variant data, simulation, or hardware measurement.

---

## 14. Detailed research documents

- [`01_SCOPE.md`](01_SCOPE.md) — scope, X1/X2/X3, optimization objective.
- [`02_TOPOLOGY_TAXONOMY.md`](02_TOPOLOGY_TAXONOMY.md) — nine main power-path families.
- [`03_LOSS_PHYSICS.md`](03_LOSS_PHYSICS.md) — I²R, RMS, 2ω, Loss Migration.
- [`04_PRIOR_ART_CLOSURE.md`](04_PRIOR_ART_CLOSURE.md) — CLOSED / OPEN_INTERSECTION / novelty boundary.
- [`05_RESEARCH_HYPOTHESIS.md`](05_RESEARCH_HYPOTHESIS.md) — energy-routing hypothesis.
- [`06_VALIDATION_PLAN.md`](06_VALIDATION_PLAN.md) — PLECS → LTspice → Maxwell/Q3D → hardware.
- [`07_BENCHMARKS.md`](07_BENCHMARKS.md) — A0/A1, Direct HFL, high-gain, candidate comparison.
- [`08_DECISION_LOG.md`](08_DECISION_LOG.md) — retained / rejected decisions.
- [`09_CANDIDATE10_SYNTHESIS_BOUNDARY.md`](09_CANDIDATE10_SYNTHESIS_BOUNDARY.md) — fixed candidate front-end / Block ⑥ boundary.
- [`10_ASP2000_PRODUCT_BASELINE.md`](10_ASP2000_PRODUCT_BASELINE.md) — real ASP-2000 R52 product baseline.
- [`11_WORKING_ARCHITECTURE_LOSS_AUDIT.md`](11_WORKING_ARCHITECTURE_LOSS_AUDIT.md) — block-by-block added-loss audit.

Evidence/acquisition layer remains under:

- [`batches/`](batches/)
- [`contracts/`](contracts/)

---

## 15. Current decision state

```text
Research target:
    low-voltage high-current DC → single-phase AC

General scale:
    12–24 V / 1–3 kW / 220 Vac

Primary anchor:
    12 V / 2 kW / 166.7 A ideal

A0 real-product benchmark:
    ASP-2000 R52

Working architecture:
    KEEP

Core research region:
    branch switching + X1

Early fan-out benefit:
    NOT YET PROVEN

Active X2 benefit:
    NOT YET PROVEN

Candidate #10:
    NOT ASSIGNED

Novelty:
    NOT ESTABLISHED

Next action:
    A0 loss localization + matched A0/A1/X1 mechanism modeling before detailed topology invention
```
