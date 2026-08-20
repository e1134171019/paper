# Current Mainline Override — 2026-08-20

Status: `AUTHORITATIVE CURRENT-MAINLINE OVERRIDE`

This file supersedes stale phase/header language in `research/RESEARCH_STATE.md` when determining the immediate research mainline. It does **not** erase the historical evidence, physical baseline, or governance content in `RESEARCH_STATE.md`.

## 1. Research boundary and evidence governance

```text
Vin = 12–24 Vdc
Pout = 1–3 kW
anchor = 12 V / 2 kW
Vout = 220 Vac / 1φ / 50 Hz
canonical post-X1 comparison point = 350 Vdc-class
```

Anchor scales:

```text
Iin,ideal = 166.7 A
Iin@95% reference ≈ 175.4 A
350-V / 2-kW current scale = 5.714 A
220-Vac / 2-kW output current = 9.09 Arms
```

Evidence vocabulary remains:

```text
VERIFIED / MODELLED / HYPOTHESIS / OPEN / NOT_ESTABLISHED
```

Total-loss authority remains:

```text
ΔP_total = P_loss,baseline - P_loss,candidate
```

Preferred robust gate:

```text
P_loss,candidate,high < P_loss,baseline,low
```

No PSIM/LTspice/hardware result may be claimed unless actually executed.

```text
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty = NOT_ESTABLISHED
```

---

## 2. Generic synthesis dimensions already closed

Files52–57 screened the representative X-coordinate partitions:

```text
O0   = X1 | X2 | X3
O13  = X1+X3 | X2
O23  = X1 | X2+X3
O12  = X1+X2 | X3
O123 = X1+X2+X3
```

Result:

```text
GENERIC X1/X2/X3 OVERLAP
= CLOSED AS A GENERIC NOVELTY GENERATOR
```

The coordinates remain mandatory analysis tools.

File58 then closed generic partial-power processing as a novelty generator and introduced the minimum auxiliary-edge ledger:

```text
αP = active processed-power ratio
αS = apparent / VA / nonactive stress ratio
αI = RMS-current exposure ratio
αV = voltage-stress ratio
```

Hard File58 results include:

```text
12→350-V series PPP: αP≈0.966 -> effectively full-power
full 2ω decoupling: |Pbuf|pk=Pout; Prms=Pout/sqrt(2)
post-X1 residual correction can be fractional, but generic PPP/master-slave/series-filter classes are prior-art rich
```

Therefore PPP remains an accounting framework, not Candidate #10.

---

## 3. File59 — A0 edge-loss / removability target selection

Authoritative artifact:

```text
research/59_A0_EDGE_LOSS_REMOVABILITY_TARGET_SELECTION_V1.md
```

A0 edge map:

```text
E1  source / primary LV conduction exposure
E2  primary switching / commutation / RC-snubber dissipation
E3  HFT isolation + main transformation
E4  secondary rectification
E5  HV-link / 2ω energy buffer
E6  VSI / X3 AC synthesis
E7  output filtering / current shaping
```

Current mixed-evidence loss anchors:

```text
E1 main MOS conduction proxy  ≈ 12.31 W  MODELLED / DATASHEET PROXY
E2 commutation bucket         ≈ 25.10 W  MODELLED / NOT MEASURED
E4 rectifier matched floor    ≈ 17.14 W  MATCHED-TECH MODEL
E3 HFT watts                  = OPEN
E5 HV-link/X2 watts           = OPEN; 2ω energy requirement closed
E6 VSI watts                  = OPEN
E7 filter watts               = OPEN
```

Two rankings remain deliberately separate:

```text
strongest known LOSS TARGET
= E2 commutation/snubber

strongest selected SYNTHESIS-CROSSOVER TARGET
= JOINT E4 + E6
```

E2 is retained as a loss/control comparator because active-clamp, resonant, magnetizing-current ZVS and Ryan-type soft-switching are already prior-art dense.

---

## 4. File60 executed — E4+E6 matched-loss crossover

Authoritative artifact:

```text
research/60_E4_E6_POST_HFT_DOUBLE_PROCESSING_MATCHED_LOSS_CROSSOVER_V1.md
```

Compared paths:

```text
BASELINE:
HFT secondary
→ E4 rectifier
→ HV-link / passive X2
→ E6 VSI
→ AC

KNOWN MERGED REFERENCE:
HFT / center-tapped HFT
→ bidirectional matrix / cycloconverter
→ AC
+ explicit center-tap/common-mode Lbuf/Cbuf X2 function
```

The merged graph is established prior art and is a hard comparator, not a proposed contribution.

### 4.1 Current matched-device contract

Conservative rectifier-low reference:

```text
Infineon IDW10G65C5-class SiC Schottky
VF,typ@25°C ≈ 1.5 V
Prect,low ≈ 17.14 W @5.714 A, two conducting diodes
```

Current commercial 650-V SiC MOSFET technology sensitivity:

```text
15 / 40 / 45 / 60 mΩ @25°C classes
```

### 4.2 Conduction-only result

For a normal VSI with two conducting MOSFET dies:

```text
PVSI,cond ≈ 2 R Iout,rms²
```

For a matrix path using two bidirectional cells, each realized by two anti-series MOSFETs:

```text
Pmatrix,cond ≈ 4 R Iout,rms²
```

With matched `R`:

```text
ΔPcond = Prect - 2 R Iout²
```

Conduction crossover:

```text
RDS(on) < ~104 mΩ per die @25°C proxy
```

Current 15–60-mΩ SiC classes therefore survive the conduction-only gate.

Sensitivity:

| matched RDS(on) | VSI cond | 4-die matrix cond | remaining conduction headroom |
|---:|---:|---:|---:|
| 15 mΩ | 2.48 W | 4.96 W | 14.66 W |
| 40 mΩ | 6.61 W | 13.22 W | 10.53 W |
| 45 mΩ | 7.44 W | 14.88 W | 9.70 W |
| 60 mΩ | 9.92 W | 19.83 W | 7.23 W |

Formal result:

```text
CONDUCTION-ONLY GATE = SURVIVES
```

But the apparent saving is only roughly 7–15 W before matrix switching/commutation, X2 and magnetic interaction are counted.

### 4.3 Dynamic / X2 interaction gate

Known reference literature establishes feasible low-commutation operation:

```text
Takaoka/Takahashi/Itoh:
PDM + matrix ZVS + partial primary ZVS

Blinov et al.:
quasi-resonant HF-link commutation
DC-side ZVS
some AC switches fundamental-frequency
remaining AC-side transitions can achieve ZCS
```

This proves the known merged reference must be compared as a soft-switched reference.

It does **not** establish a matched total-loss win at this project's boundary.

The hidden decisive term is X2/common-mode current through the transformer environment.

At a simple 350-V scaling point:

```text
Ibuf,rms scale ≈ 2000/(sqrt(2)×350) ≈ 4.04 A
Imain scale    ≈ 2000/350 ≈ 5.714 A
κ ≈ 0.707
κ² ≈ 0.5
```

A first-order orthogonal-current sensitivity therefore gives:

```text
ΔPT,Cu ≈ 0.5 × PT,Cu,baseline
```

If that term alone consumes the conduction headroom, the allowable baseline transformer-copper scale is only:

```text
~29.3 W at 15 mΩ
~21.1 W at 40 mΩ
~19.4 W at 45 mΩ
~14.5 W at 60 mΩ
```

and those values leave zero budget for matrix switching, Lbuf or Cbuf ESR.

Therefore File60 forces E3 transformer copper/RMS back into the E4+E6 decision as an `INTERACTION_NEW` discriminator.

---

## 5. Formal File60 verdict

```text
E4+E6 MERGED REFERENCE
= PHYSICALLY PLAUSIBLE LOSS SURVIVOR
= CONDUCTION SURVIVOR
= SWITCHING/COMMUTATION PLAUSIBLE BUT NOT CLOSED
= X2/TRANSFORMER INTERACTION MATERIAL / UNRESOLVED
= NOT A ROBUST TOTAL-LOSS WINNER YET
= CROSSOVER_UNRESOLVED
```

This rejects the shortcut:

```text
remove rectifier + remove VSI stage
=> automatically large net saving
```

The actual remaining headroom is tight enough that a few watts of transformer/buffer/matrix interaction can reverse the ranking.

---

## 6. Current research phase

The current phase is now:

```text
E4+E6 CROSSOVER UNCERTAINTY CLOSURE
```

Do not synthesize a new graph before the hard comparator is quantitatively closed.

Minimum missing quantities:

### Baseline / A0-like

```text
A. actual/representative VSI device and conduction technology
B. VSI switching frequency and switching-loss bucket
C. actual rectifier waveform / hot VF
D. HV-link capacitor ripple/ESR loss
E. transformer secondary RMS and copper-loss scale
```

### Known merged reference

```text
F. matrix switch RMS and practical bidirectional die realization
G. soft-switched matrix commutation-loss bucket
H. referred buffer-current RMS κ
I. center-tapped transformer copper increment
J. Lbuf / Cbuf copper/core/ESR loss
```

Robust authority:

```text
Pmerged,high < Pbaseline,low
```

---

## 7. Immediate NEXT

Expected next artifact:

```text
research/61_E4_E6_CROSSOVER_UNCERTAINTY_CLOSURE_AND_MINIMUM_EVIDENCE_V1.md
```

The task is evidence closure / reduced-order comparator bounding, not new-topology generation.

Allowed:

```text
comparator-only analytical work
current datasheet normalization
reduced-order Python loss envelopes
actual A0 evidence acquisition where available
```

Still not authorized:

```text
PSIM as a proposed new topology
LTspice as a proposed new topology
Candidate #10 assignment
novelty claim
```

Explicit state:

```text
PSIM = NOT EXECUTED
LTspice = NOT EXECUTED
hardware = NOT EXECUTED
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty = NOT_ESTABLISHED
```

R2/Ryan remains comparator-only.
R7 remains weak/deferred.
Generic X1/X2/X3 overlap remains closed as a novelty-generation method.
Generic PPP remains an edge-rating framework.
