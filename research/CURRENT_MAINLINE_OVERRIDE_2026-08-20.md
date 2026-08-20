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

Anchor current scales:

```text
Iin,ideal = 166.7 A
Iin@95% reference ≈ 175.4 A
350-V / 2-kW current scale = 5.714 A
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

## 2. Mainline change after Files 52–58

The generic topology-generation sequence has now been screened through three increasingly strict levels.

### 2.1 X1/X2/X3 overlap synthesis

Files 52–57 executed representative graphs for:

```text
O0   = X1 | X2 | X3
O13  = X1+X3 | X2
O23  = X1 | X2+X3
O12  = X1+X2 | X3
O123 = X1+X2+X3
```

Result:

```text
GENERIC X1/X2/X3 OVERLAP MATRIX
= CLOSED AS A GENERIC NOVELTY GENERATOR
```

The coordinates remain mandatory analysis tools, but merely choosing another overlap is no longer sufficient to generate a research candidate.

Representative obvious graphs were either already established prior art, physically weak, or incurred explicit interaction/RMS penalties.

### 2.2 Partial-power / edge-level reset

File 58 introduced:

```text
Paux = α Pout
```

but rejects the shortcut:

```text
small active Paux => small converter / low loss
```

Every future auxiliary edge must disclose at least:

```text
αP = active processed-power ratio
αS = apparent / VA / nonactive processing ratio
αI = RMS-current exposure ratio
αV = voltage-stress ratio
```

Key File-58 conclusions:

1. A direct series partial-power path from 12 V to 350 V is not meaningfully partial:

```text
αP ≈ 1 - 12/350 ≈ 0.966
```

so it still processes approximately 1.93 kW at the 2-kW anchor.

2. The mandatory isolation boundary prevents the HFT/X1 path from becoming a tiny-power auxiliary unless a separate majority-power isolated path exists.

3. Full single-phase 2ω decoupling is not a low-rated auxiliary simply because its signed average power is zero:

```text
|Pbuf|pk = Pout = 2 kW
Pbuf,rms = Pout/sqrt(2) ≈ 1.414 kW
```

Its preferred location is post-X1 because the current scale is lower, not because the energy-processing requirement disappears.

4. True partial-power opportunities require a majority path that already performs most of the required transformation and a corrective edge that only supplies a small residual ΔV / ΔI / waveform component.

5. Even then, active processed power alone is insufficient; a series correction edge may still carry full load current and therefore retain large VA/current stress.

Therefore:

```text
PARTIAL-POWER PROCESSING
= ANALYSIS / RATING DIMENSION
!= NOVELTY GENERATOR BY ITSELF
```

---

## 3. Current research position

The research is no longer at generic `Physical Gap Validation` alone.

Current phase is:

```text
A0 EDGE-LOSS / REMOVABILITY TARGET SELECTION
```

The next task is to return to the A0 baseline and rank actual loss-bearing / full-power edges by whether removing or relaxing them can create a defensible topology opportunity.

Normalized A0 edge map for the next audit:

```text
E1  source / primary LV conduction exposure
E2  primary switching / commutation / RC-snubber dissipation
E3  HFT main transformation edge
E4  secondary rectification edge
E5  HV-link / 2ω energy-buffer edge
E6  VSI / X3 switching edge
E7  output filtering / current-shaping edge
```

Product-interface items such as reverse-polarity protection, startup precharge, fuses and connectors remain separated from intrinsic topology loss unless they materially discriminate a topology-level physical gap.

---

## 4. Mandatory edge-removability audit

For each edge `Ei`, the next formal artifact must answer:

```text
1. What function is physically mandatory?
2. What loss bucket is VERIFIED / MODELLED / OPEN?
3. What watt scale is currently known or bounded?
4. Is the edge full-power, partial-power, reactive-only, or time-multiplexed?
5. Which X1/X2/X3 coordinate(s) does it implement?
6. Can the edge be REMOVED, REDUCED, or only RELOCATED?
7. What replacement edge is minimally required by conservation / isolation / 2ω physics?
8. What are αP, αS, αI, αV of that replacement?
9. Does the replacement operate in the 12-V/~175-A domain or after current reduction?
10. Which new interaction loss appears?
11. What is the closest prior-art graph?
12. Does total loss satisfy P_saved > P_added under a matched contract?
```

Loss-causality tags remain mandatory:

```text
REMOVED
REDUCED
RETAINED
RELOCATED
INTRINSIC_NEW
INTERACTION_NEW
SUPPORT_NEW
AUXILIARY_NEW
```

Total-loss authority remains:

```text
ΔP_total = P_loss,baseline - P_loss,candidate
```

Preferred robust gate:

```text
P_loss,candidate,high < P_loss,baseline,low
```

---

## 5. Current priority expectations before the audit

These are **not final rankings**; they are hypotheses to be falsified by the next edge audit.

### E1 — pre-X1 LV conduction

Status:

```text
HIGH PHYSICAL IMPORTANCE
```

Reason:

```text
~175 A source-domain current
+ every additional 0.1 mΩ ≈ 3.08 W
```

But a replacement must not simply add another series edge in the same current domain.

### E2 — primary commutation / dissipative snubber

Status:

```text
PROMISING REMOVABILITY TARGET / MATERIALITY NOT YET VERIFIED
```

A0 has a verified passive dissipative RC damping path; prior R2 work already showed soft-commutation/recovery is a mature region, so topology novelty cannot be assumed.

### E3 — HFT transformation

Status:

```text
MANDATORY ISOLATION / GAIN FUNCTION
TOTAL BURDEN OPEN
```

File51 rejected the shortcut that lower secondary voltage automatically yields large magnetic savings.

### E4 — secondary rectification

Status:

```text
POTENTIALLY REMOVABLE / MERGEABLE
```

but standard direct-HF-link and matrix/cycloconverter realizations are prior-art rich.

### E5 — HV-link / 2ω buffer

Status:

```text
ENERGY FUNCTION MANDATORY
PHYSICAL LOCATION OPTIMIZABLE
```

The required 2ω energy is not removable; only its storage/routing implementation and current domain can change.

### E6 — VSI / X3

Status:

```text
AC SYNTHESIS FUNCTION MANDATORY
STAGE BOUNDARY MAY BE MERGEABLE
```

but generic X1+X3 and X2+X3 integration is prior-art rich.

---

## 6. Explicit non-results

As of this override:

```text
PSIM = NOT EXECUTED
LTspice = NOT EXECUTED
hardware validation = NOT EXECUTED
new topology candidate = NOT ASSIGNED
Candidate #10 = HOLD / NOT_ASSIGNED
novelty = NOT_ESTABLISHED
```

R2/Ryan remains comparator-only.
R7 remains weak/deferred after the gain-sharing screen.
The generic X1/X2/X3 overlap matrix is closed as a novelty-generation method.
Generic PPP is retained as an edge-rating framework, not promoted as a topology candidate.

---

## 7. Immediate NEXT

Create the formal A0 edge-removability artifact, expected working title:

```text
research/59_A0_EDGE_LOSS_REMOVABILITY_TARGET_SELECTION_V1.md
```

The artifact must rank E1–E7 using matched evidence quality, watt materiality, physical removability, replacement lower bounds, current-domain location, and prior-art density.

Do not synthesize another converter graph before this target-selection gate identifies which A0 edge is actually worth attacking.
