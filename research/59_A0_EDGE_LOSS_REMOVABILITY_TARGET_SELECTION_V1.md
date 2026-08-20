# 59 — A0 Edge-Loss Removability Target Selection v1

Status date: 2026-08-20  
Role: `A0 EDGE-LOSS AUDIT / REMOVABILITY RANKING / NEXT-TARGET SELECTION`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Canonical HV-link comparison point: `350 Vdc`  
Evidence status: `VERIFIED A0 GRAPH + MODELLED / MATCHED-TECHNOLOGY LOSS ANCHORS + OPEN-BUCKET AUDIT`  
Simulation status: `NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

File 58 ended generic partial-power synthesis and required a return to the real A0 baseline. This file ranks the actual A0 load-bearing edges by a stricter question:

> Which baseline edge is materially lossy, physically removable or mergeable, replaceable without recreating comparable VA/RMS stress, and still worth research after closest-prior-art density is considered?

This file does **not** assign a new converter topology.

The objective is target selection before graph synthesis.

---

## 2. A0 normalized edge map

```text
E1  12-V source / primary LV conduction exposure
 |
E2  primary switching / commutation / RC-snubber dissipation
 |
E3  HFT isolation + main voltage transformation
 |
E4  secondary full-wave rectification
 |
E5  HV-link / 2ω energy-buffer boundary
 |
E6  VSI / X3 AC-synthesis switching
 |
E7  output filtering / current shaping
 |
220 Vac load
```

The following product-interface items remain outside the intrinsic topology ranking unless a candidate changes their required function:

```text
reverse-polarity protection
fuses / connectors
startup precharge
BOCP sensing
```

---

## 3. Common anchor quantities

At the 12-V / 2-kW center point:

```text
Iin,ideal = 166.7 A
Iin@95% reference = 175.44 A
IHV,ideal @350 V = 5.714 A
Iout,rms @220 Vac = 9.09 A
```

Loss-location leverage remains extreme:

```text
P = I²R
```

At 175.44 A:

```text
0.1 mΩ -> ~3.08 W
```

The File-47 25.1-W crossover corresponds to only:

```text
0.815 mΩ @175.44 A
```

but about:

```text
0.769 Ω @5.714 A
```

for the same watt loss.

Therefore any replacement edge added after X1 has much larger resistance tolerance than a new source-domain edge, although switching, magnetic and reactive losses still require separate accounting.

---

## 4. Evidence classes used in this audit

This file separates three different quantities:

```text
A. known/bounded watt materiality
B. physical removability of the edge/function
C. novelty headroom after prior-art screening
```

These must not be conflated.

An edge may be the best loss-reduction target and still be a poor novelty target.

Ranking labels:

```text
LOSS TARGET:      A / B / C / HOLD
SYNTHESIS TARGET: A / B / C / STOP
EVIDENCE:         VERIFIED / MODELLED / BOUNDED / OPEN
```

No false numerical precision is assigned where the baseline watts are still open.

---

## 5. E1 — source / primary LV conduction exposure

### Function

Carry essentially all system power from the 12-V source into the first transformation region.

### Current evidence

Matched modern main-switch conduction proxy from File 47:

```text
10 × CSD18542KCS in parallel per logical switch
Rlogical,max,25C proxy = 0.4 mΩ
Pmain,25C,proxy ≈ 12.31 W
```

A0 manufacturing-geometry work also bounds a partial positive-side PCB path at approximately:

```text
≤ ~4.98 W
```

under the declared geometry assumptions, but this must not be blindly added to the MOS proxy as a measured total.

Status:

```text
MAIN MOS CONDUCTION = MODELLED / DATASHEET PROXY
PCB DISTRIBUTION = GEOMETRY BOUND / NOT MEASURED
```

### Removability

The **loss** may be reduced, but the **full-current source edge is not removable** while the source remains 12 V and supplies 2 kW.

Any candidate still obeys:

```text
Pin ≈ Pout + Ploss
```

so source current remains of order 167–175 A near full load.

### Replacement lower bound

A topology that adds another series device/path before current reduction immediately pays:

```text
ΔP ≈ I² ΔR
```

and therefore has only sub-milliohm tolerance.

### Decision

```text
LOSS TARGET = B
SYNTHESIS TARGET = C
```

Reason:

> E1 is physically important but not a deletable edge. The admissible topology strategy is to keep the source-domain path short/simple and complete X1 without adding another substantial 175-A branch. Pure RDS(on), copper, busbar or parallel-device optimization is product engineering unless it changes the majority-power graph.

---

## 6. E2 — primary commutation / RC-snubber dissipation

### Function

Safely commutate the LV primary switches and dispose/control leakage/Coss energy and switching overlap.

### Current evidence

A0 passive dissipative RC damping is physically verified at the graph level.

File-47 current analytical surrogate:

```text
Psnubber ≈ 2.30 W
Poverlap ≈ 21.05 W
Pdeadtime ≈ 1.75 W
----------------------
Pcomm,A0 ≈ 25.10 W
```

Status:

```text
MODELLED
NOT MEASURED
```

### Removability

The **commutation function is mandatory**, but the **dissipative fate is not**.

Possible fates include:

```text
REDUCED via ZVS/ZCS
RELOCATED into resonant/reactive paths
partially RECOVERED
```

### Replacement lower bound

This edge is attractive because the saved-loss budget is relatively large. However, any new auxiliary current in the 175-A domain is expensive. File47 showed that active-clamp/auxiliary RMS can consume the full 25.1-W budget quickly.

### Prior-art density

Files 41–48 already established:

```text
active clamp
magnetizing-current ZVS
LCL/resonant commutation
Ryan-type soft switching
```

as mature comparator regions.

### Decision

```text
LOSS TARGET = A
SYNTHESIS TARGET = C / PRIOR-ART-DENSE
```

Formal meaning:

> E2 is the strongest **known loss-saving target**, but not the strongest current novelty target. Any future E2 proposal must change the load-bearing energy path, not merely substitute another known ZVS/active-clamp implementation.

---

## 7. E3 — HFT isolation + main transformation

### Function

Provide galvanic isolation and transfer essentially the full 2-kW majority power into the high-voltage/reduced-current domain.

### Current evidence

Verified structural facts:

```text
T1/T2 = PQ5050 class
center-tapped primary connectivity
secondary series relationship
```

Still open for the actual A0 population:

```text
turns ratio
Lm / Lk
DCR / Rac
core material
core loss
winding loss
actual transformer watts
```

File51 also rejected the shortcut:

```text
lower secondary voltage => proportionally smaller/lower-loss transformer
```

because at fixed power the first-order `Ns × Acu` burden does not automatically collapse with voltage ratio.

### Removability

Under the current project isolation requirement, a full-power isolation edge is mandatory unless another isolation path carries the remainder.

File58 further established that the extreme 12→350-V ratio prevents a simple series partial-power reconnection from making the isolation transformer a tiny-power auxiliary.

### Decision

```text
LOSS TARGET = HOLD
SYNTHESIS TARGET = C
```

Reason:

> E3 cannot be ranked as the dominant A0 loss while its actual watts are OPEN, and its function is mandatory. Do not attack the transformer merely because the voltage ratio is large.

Required evidence before promotion:

```text
P_T,Cu
P_T,core
Rac/DCR
actual RMS currents
```

---

## 8. E4 — secondary rectification

### Function

Convert the bipolar HF transformer secondary power into a unipolar HV-link power flow.

### Current evidence

File47 modern matched rectifier technology floor used a 650-V / 10-A SiC Schottky class with approximately:

```text
VF ≈ 1.5 V
```

For two conducting diodes at 5.714 A:

```text
Prect,base ≈ 2 × 1.5 × 5.714
           ≈ 17.14 W
```

Status:

```text
MATCHED-TECHNOLOGY MODEL / NOT A0 MEASUREMENT
```

The actual A0 diode VF-temperature/waveform loss remains open.

### Removability

Unlike E3, the **standalone rectifier stage is physically mergeable/removable** if downstream switching states synthesize the required polarity directly.

File53 confirmed that a direct HF-link matrix/cycloconverter graph can remove the distinct rectifier edge at the architecture level.

### Interaction cost

Rectifier removal does not equal free loss removal. File53 showed the likely replacements:

```text
matrix bidirectional-switch conduction
HF commutation
leakage-current commutation burden
additional die count
X2 relocation / active-buffer requirement
```

### Prior-art density

Direct HFT + matrix/cycloconverter DC-AC conversion and its power-decoupling variants are established prior art.

### Decision

```text
LOSS TARGET = A-/B+
SYNTHESIS TARGET = B, BUT ONLY AS PART OF A JOINT E4+E6 CROSSOVER
```

Reason:

> E4 has a material matched loss floor and is genuinely mergeable, but the obvious replacement graph is already known. It becomes interesting only when evaluated together with E6 under one matched semiconductor/current/commutation contract.

---

## 9. E5 — HV-link / 2ω buffer

### Function

Maintain the energy balance between approximately constant source power and the pulsating single-phase output power.

At 2 kW / 50 Hz:

```text
E2ω,pk = P/(4πf) = 3.183 J
E2ω,pp = 6.366 J
```

### Current evidence

The energy requirement is first-principles closed.

The actual A0 capacitor ESR/ripple watts and thermal burden are still OPEN.

### Removability

The **2ω energy function is not removable**.

Only these aspects are mutable:

```text
storage medium
voltage swing
physical location
passive vs active routing
which current domain carries the oscillatory power
```

File53/54/55/56 showed that moving/merging X2 is a mature prior-art region and that full decoupling still has ±2-kW instantaneous power exchange.

### Decision

```text
LOSS TARGET = HOLD
SYNTHESIS TARGET = C
```

Reason:

> E5 is a mandatory energy-conservation function. Without measured/bounded A0 buffer loss, it should not be selected as a loss-removal target. Future work may optimize placement but must not claim the 2ω energy requirement has disappeared.

---

## 10. E6 — VSI / X3 AC synthesis

### Function

Generate the 220-V / 50-Hz AC voltage/current waveform from the HV power domain.

### Current evidence

A0 VSI conduction/switching watts are currently:

```text
OPEN
```

The function is mandatory; the standalone stage boundary is not necessarily mandatory.

### Removability

File53 proved the stage boundary can be merged with the HF-link secondary conversion so that a distinct rectifier + stiff HV-link + independent VSI sequence is not required.

But the replacement matrix/cycloconverter still carries full AC current and incurs its own conduction/switching/commutation burden.

### Prior-art density

Generic X1+X3 direct HF-link, matrix/cycloconverter and soft-switched variants are mature.

### Decision

```text
LOSS TARGET = HOLD pending matched VSI loss
SYNTHESIS TARGET = B when paired with E4
```

Reason:

> E6 alone cannot yet be ranked by watts. The meaningful question is whether deleting/merging **both E4 and E6** saves more total loss than a known direct-HF-link replacement adds.

---

## 11. E7 — output filtering / current shaping

### Function

Suppress switching-frequency harmonics and satisfy output voltage/current quality requirements.

### Current evidence

A0 output-filter copper/core/capacitor watts are currently:

```text
OPEN
```

### Removability

The exact filter may shrink if the upstream waveform becomes more sinusoidal/multilevel, but a current/EMI-quality function remains.

File58 showed that coarse-main + corrective waveform-processing families are already known and that a low active-power correction edge may still carry material VA stress.

### Decision

```text
LOSS TARGET = HOLD
SYNTHESIS TARGET = C
```

Do not target E7 before quantifying the upstream switching and filter trade-off.

---

## 12. Two different rankings are required

### 12.1 Ranking by present loss-removal materiality

Using only currently available evidence:

```text
#1 E2  primary commutation/snubber      ~25.10 W MODELLED
#2 E4  secondary rectification         ~17.14 W matched floor
#3 E1  primary LV main-switch conduction ~12.31 W proxy
#4 E3  HFT transformation              OPEN
#5 E6  VSI/X3                          OPEN
#6 E5  HV-link/X2 loss                 OPEN; energy requirement known
#7 E7  output filter                   OPEN
```

This is **not** a total A0 efficiency budget and must not be summed as measured product loss.

### 12.2 Ranking by topology-synthesis leverage

```text
#1 JOINT E4+E6 post-HFT semiconductor double-processing boundary
#2 E2 commutation fate, but only if a future mechanism is outside the known R2/active-clamp/resonant families
#3 E1 strategy constraint: minimize, do not add source-domain edges
#4 E3 HOLD until transformer loss is quantified
#5 E5 mandatory-energy function / reference-rich
#6 E7 HOLD
```

Why `E4+E6` is first for the next synthesis gate:

```text
- E4 already has a material ~17.14-W matched loss floor.
- E6 adds another full-power semiconductor stage whose watts are currently open.
- Both lie after current reduction, avoiding a new 175-A source-domain series edge.
- Their standalone stage boundaries are physically mergeable.
- The obvious direct-HF-link replacement is already prior art, so it can serve as a hard comparator rather than being mistaken for the contribution.
```

This ranking does **not** claim a new E4+E6 topology exists.

---

## 13. Selected next target — not Candidate #10

Formal target selection:

```text
PRIMARY NEXT LOSS-CROSSOVER TARGET:
T_POST = JOINT E4 + E6
         secondary rectification
         + downstream AC-synthesis semiconductor processing
```

Control target:

```text
T_COMM = E2 commutation/snubber
```

`T_COMM` remains the highest known modeled loss bucket, but mature soft-switching prior art makes it a comparator/control rather than the immediate novelty-search target.

`T_POST` is selected because it tests whether the baseline pays two material full-power semiconductor-processing boundaries after X1 and whether a merged replacement can **actually** reduce total loss once matrix/bidirectional switching and X2 interaction are included.

---

## 14. Mandatory crossover before any new graph

Do not synthesize Candidate #10 yet.

The next formal artifact must execute a matched loss/stress crossover between:

```text
BASELINE POST-X1:
HFT secondary
→ E4 rectifier
→ HV link / X2
→ E6 VSI

REFERENCE MERGED PATH:
HFT secondary
→ known direct-HF-link / matrix-cycloconverter reference
→ AC
+ explicit X2 implementation
```

Both sides must use matched technology and report at least:

```text
Pcond
Psw
Pcomm
PX2
Pfilter interaction
semiconductor die count in conducting path
Irms per device/path
Vstress
switching frequency
```

The crossover authority is:

```text
P_saved(E4+E6 baseline)
>
P_added(matrix/direct-HF-link + X2 + interaction)
```

If the known merged reference cannot beat or materially challenge A0 under a fair matched loss contract, there is no physical reason to invent a more complex novelty graph in the same region.

If it does beat A0, then any future candidate must beat the **known merged reference**, not merely the A0 baseline.

---

## 15. Immediate next

Expected working title:

```text
research/60_E4_E6_POST_HFT_DOUBLE_PROCESSING_MATCHED_LOSS_CROSSOVER_V1.md
```

Required first step:

```text
quantify a matched A0 rectifier + VSI semiconductor floor
vs
G13-REF1 / G13-REF2 direct-HF-link semiconductor + X2 floor
```

Do not authorize PSIM until the analytical/device-level crossover identifies a plausible positive loss budget.

Candidate #10 remains `HOLD / NOT_ASSIGNED`.
Novelty remains `NOT_ESTABLISHED`.
PSIM/LTspice/hardware remain `NOT EXECUTED`.
