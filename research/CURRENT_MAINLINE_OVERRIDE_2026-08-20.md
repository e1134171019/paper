# Current Mainline Override — 2026-08-20

Status: `AUTHORITATIVE CURRENT-MAINLINE OVERRIDE`

This file supersedes stale phase/header language in `research/RESEARCH_STATE.md` when determining the immediate research mainline. It does **not** erase the historical evidence, physical baseline, or governance content in `RESEARCH_STATE.md`.

## 1. Research boundary

```text
Vin = 12–24 Vdc
Pout = 1–3 kW
anchor = 12 V / 2 kW
Vout = 220 Vac / 1φ / 50 Hz
canonical HV-link comparison point = 350 Vdc
```

Anchor scales:

```text
Iin,ideal = 166.7 A
Iin@95% reference ≈ 175.4 A
350-V / 2-kW current scale = 5.714 A
220-Vac / 2-kW output current = 9.09 Arms
```

Evidence governance remains:

```text
VERIFIED / MODELLED / HYPOTHESIS / OPEN / NOT_ESTABLISHED
```

No PSIM/LTspice/hardware result may be claimed unless actually executed.

Candidate #10 remains:

```text
HOLD / NOT_ASSIGNED
```

Novelty remains:

```text
NOT_ESTABLISHED
```

---

## 2. Closed generic synthesis dimensions

Files 52–57 screened the representative `X1/X2/X3` overlap classes:

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

File58 then screened edge-level partial-power processing and established:

```text
αP alone is insufficient
```

Every partial/corrective edge must also disclose:

```text
αS = apparent / VA / nonactive stress
αI = RMS-current exposure
αV = voltage stress
```

Hard File58 conclusions:

```text
12→350-V series PPP: αP≈0.966 -> effectively full-power
full 2ω decoupling: |Pbuf|pk=Pout; Prms=Pout/sqrt(2)
post-X1 residual correction can be fractional, but generic PPP/master-slave/series-filter families are prior-art rich
```

Therefore PPP is retained as an edge-accounting framework, not Candidate #10.

---

## 3. File59 executed — A0 edge-loss/removability ranking

Authoritative artifact:

```text
research/59_A0_EDGE_LOSS_REMOVABILITY_TARGET_SELECTION_V1.md
```

Normalized A0 edge map:

```text
E1  source / primary LV conduction exposure
E2  primary switching / commutation / RC-snubber dissipation
E3  HFT isolation + main transformation
E4  secondary rectification
E5  HV-link / 2ω energy buffer
E6  VSI / X3 AC synthesis
E7  output filtering / current shaping
```

Current loss anchors are intentionally mixed-evidence and must not be summed as a measured product total:

```text
E1 main MOS conduction proxy  ≈ 12.31 W  MODELLED / DATASHEET FLOOR
E2 commutation bucket         ≈ 25.10 W  MODELLED / NOT MEASURED
E4 rectifier matched floor    ≈ 17.14 W  MATCHED-TECH MODEL
E3 HFT watts                  = OPEN
E5 HV-link/X2 watts           = OPEN; 2ω energy is first-principles closed
E6 VSI watts                  = OPEN
E7 filter watts               = OPEN
```

At 2 kW / 50 Hz:

```text
E2ω,pk = 3.183 J
E2ω,pp = 6.366 J
```

---

## 4. File59 dual ranking

### 4.1 Present loss-removal materiality

```text
#1 E2 primary commutation/snubber       ~25.10 W MODELLED
#2 E4 secondary rectification           ~17.14 W matched floor
#3 E1 primary LV main conduction        ~12.31 W proxy
#4 E3 HFT                               OPEN
#5 E6 VSI                               OPEN
#6 E5 HV-link/X2 loss                   OPEN
#7 E7 filter                            OPEN
```

This ranking is about known/bounded watts only.

### 4.2 Topology-synthesis leverage

```text
#1 JOINT E4+E6 post-HFT semiconductor double-processing boundary
#2 E2 commutation fate, only if outside known active-clamp/resonant/Ryan classes
#3 E1 remains a hard strategy constraint: minimize, do not add source-domain edges
#4 E3 HOLD until actual transformer burden is quantified
#5 E5 mandatory-energy / reference-rich
#6 E7 HOLD
```

Critical distinction:

```text
E2 = strongest current LOSS TARGET
E4+E6 = strongest current SYNTHESIS-CROSSOVER TARGET
```

E2 is not promoted to the novelty mainline because Files41–48 already show dense soft-switching/active-clamp/resonant prior art.

---

## 5. Current selected target

Formal selected target:

```text
T_POST = JOINT E4 + E6
```

Meaning:

```text
HFT secondary
→ full-power secondary rectification
→ HV-link
→ full-power VSI AC synthesis
```

The physical question is:

> Does the A0-like post-HFT path pay two material semiconductor-processing boundaries, and can a merged path reduce their total loss after all matrix/bidirectional-switch, commutation, X2 and filtering interaction costs are counted?

This does **not** mean the known direct-HF-link/matrix converter is a new contribution. File53 already classified the generic graph as `SAME_GRAPH / NEAR_GRAPH` prior art.

The known G13 direct-HF-link family is now a hard comparator.

---

## 6. Mandatory next crossover

Do not synthesize Candidate #10 yet.

Immediate next formal artifact:

```text
research/60_E4_E6_POST_HFT_DOUBLE_PROCESSING_MATCHED_LOSS_CROSSOVER_V1.md
```

Required comparison:

```text
BASELINE:
HFT secondary
→ E4 rectifier
→ HV-link/X2
→ E6 VSI

KNOWN MERGED REFERENCE:
HFT secondary
→ direct-HF-link / matrix-cycloconverter
→ AC
+ explicit X2 function
```

Use matched technology and report at least:

```text
Pcond
Psw
Pcomm
PX2
Pfilter interaction
conducting die count
Irms
Vstress
switching frequency
```

Crossover authority:

```text
P_saved(E4+E6 baseline)
>
P_added(merged path + X2 + interaction)
```

If the known merged reference does not materially challenge A0 under a fair matched contract, stop searching for a more complex novelty graph in the same region.

If it does, future candidates must beat the **known merged reference**, not merely A0.

---

## 7. Explicit non-results

```text
PSIM = NOT EXECUTED
LTspice = NOT EXECUTED
hardware validation = NOT EXECUTED
new topology candidate = NOT ASSIGNED
Candidate #10 = HOLD / NOT_ASSIGNED
novelty = NOT_ESTABLISHED
```

R2/Ryan remains comparator-only.
R7 remains weak/deferred.
Generic X1/X2/X3 overlap remains closed as a novelty-generation method.
Generic PPP remains an edge-rating framework.

Immediate NEXT = File60 matched E4+E6 crossover.
