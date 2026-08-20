# Current Mainline Override — 2026-08-20

Status: `AUTHORITATIVE CURRENT-MAINLINE OVERRIDE`

This file supersedes stale phase/header language in `research/RESEARCH_STATE.md` when determining the immediate research mainline. It does **not** erase the historical evidence, physical baseline, or governance content in `RESEARCH_STATE.md`.

## 1. Research boundary and governance

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

Evidence vocabulary:

```text
VERIFIED / MODELLED / HYPOTHESIS / OPEN / NOT_ESTABLISHED
```

Loss authority:

```text
ΔP_total = P_loss,baseline - P_loss,candidate
```

Preferred robust gate:

```text
P_loss,candidate,high < P_loss,baseline,low
```

Explicit current state:

```text
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty = NOT_ESTABLISHED
PSIM = NOT EXECUTED
LTspice = NOT EXECUTED
hardware = NOT EXECUTED
```

---

## 2. Generic topology-generation dimensions already closed

Files52–57 screened the representative X-coordinate overlap classes:

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

X1/X2/X3 remain mandatory functional coordinates.

File58 then closed generic partial-power processing as a novelty generator and introduced the minimum auxiliary-edge ledger:

```text
αP = active processed-power ratio
αS = apparent / VA / nonactive stress ratio
αI = RMS-current exposure ratio
αV = voltage-stress ratio
```

Hard conclusions retained:

```text
12→350-V series PPP: αP≈0.966 -> effectively full-power
full 2ω decoupling: |Pbuf|pk=Pout; Prms=Pout/sqrt(2)
post-X1 residual correction can be fractional, but generic PPP/master-slave/series-filter classes are prior-art rich
```

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

Current mixed-evidence anchors:

```text
E1 main MOS conduction proxy  ≈ 12.31 W  MODELLED / DATASHEET PROXY
E2 commutation bucket         ≈ 25.10 W  MODELLED / NOT MEASURED
E4 rectifier matched floor    ≈ 17.14 W  MATCHED-TECH MODEL
E3 HFT watts                  = OPEN
E5 HV-link/X2 watts           = OPEN
E6 VSI watts                  = OPEN
E7 filter watts               = OPEN
```

Two rankings remain distinct:

```text
strongest known LOSS TARGET
= E2 commutation/snubber

File59-selected SYNTHESIS-CROSSOVER TARGET
= JOINT E4 + E6
```

---

## 4. File60 — E4+E6 nominal matched-loss crossover

Authoritative artifact:

```text
research/60_E4_E6_POST_HFT_DOUBLE_PROCESSING_MATCHED_LOSS_CROSSOVER_V1.md
```

Compared paths:

```text
BASELINE:
HFT secondary
→ rectifier
→ HV-link / passive X2
→ VSI
→ AC

KNOWN MERGED REFERENCE:
HFT / center-tapped HFT
→ bidirectional matrix / cycloconverter
→ AC
+ center-tap/common-mode Lbuf/Cbuf X2 function
```

The merged graph is established prior art and is a hard comparator, not a proposed contribution.

File60 nominal 25°C conduction result:

```text
matrix four-die path survives if matched RDS(on) < ~104 mΩ/die
```

For 15–60-mΩ classes, nominal remaining conduction headroom was about:

```text
~7–15 W
```

before matrix switching/commutation, X2 and magnetic interaction.

File60 therefore classified:

```text
E4+E6 = CONDUCTION SURVIVOR / TOTAL-LOSS CROSSOVER_UNRESOLVED
```

---

## 5. File61 executed — thermal / dynamic / X2 / HFT uncertainty closure

Authoritative artifact:

```text
research/61_E4_E6_CROSSOVER_UNCERTAINTY_CLOSURE_V1.md
```

### 5.1 A0-specific evidence remains incomplete

The repository currently does not establish:

```text
actual populated A0 rectifier part number
actual A0 X3 semiconductor part number
actual A0 X3 switching frequency
actual A0 X3 switching watts
actual rectifier hot VF
actual A0 transformer DCR/Rac and secondary RMS waveform
actual A0 HV-link capacitor ESR/ripple watts
```

Those quantities remain `OPEN`.

### 5.2 Rectifier temperature

Matched SiC-diode sensitivity retained:

```text
VF,typ @25°C  ≈ 1.5 V -> ~17.14 W proxy
VF,typ @150°C ≈ 1.8 V -> ~20.57 W proxy
```

The preferred robust baseline-low comparison continues to use the 17.14-W floor until A0 hot evidence exists.

### 5.3 MOSFET hot RDS(on) collapses much of the nominal matrix margin

Current 650-V SiC thermal sensitivities support approximately:

```text
40-mΩ class: ~1.5× RDS(on) near 175°C
60-mΩ class: 60 mΩ -> ~98 mΩ near 175°C (~1.63×)
```

Preferred baseline-low / candidate-hot conduction envelope:

| R25 | hot multiplier | robust conduction headroom |
|---:|---:|---:|
| 15 mΩ | 1.50 | ~12.18 W |
| 40 mΩ | 1.50 | ~3.92 W |
| 40 mΩ | 1.63 | ~2.20 W |
| 60 mΩ | 1.50 | **−2.69 W** |
| 60 mΩ | 1.63 | **−5.27 W** |

Therefore:

```text
nominal conduction SURVIVOR
!=
robust conduction survivor across the full practical device envelope
```

### 5.4 File60 transformer-current proxy corrected

File60 used a simple 5.714-A main-current power scale.

For a direct-HF-link PDM path, a better first-order differential transformer RMS is:

```text
IT,diff,rms² ≈ m Ipk² <|sin|³>
<|sin|³> = 4/(3π)
m = Vm/Vs
```

At `Vm=311.13 V`, `Vs=350 V`, `Ipk=12.856 A`:

```text
IT,diff,rms ≈ 7.90 A
```

For effective buffer voltage `Vbuf≈200–350 V`:

```text
Ibuf,rms ≈ 7.07 ... 4.04 A
κ = Ibuf / 7.90 ≈ 0.895 ... 0.512
κ² ≈ 0.80 ... 0.26
```

Thus the first-order transformer copper interaction is not fixed at 50%:

```text
ΔPT,Cu / PT,Cu,affected
~ 0.26 ... 0.80
```

before waveform correlation / winding partition / Rac details.

### 5.5 Lbuf/Cbuf threshold accounting

For the buffer-current range:

```text
4.04 Arms -> ~61 mΩ equivalent series resistance causes 1 W
7.07 Arms -> ~20 mΩ equivalent series resistance causes 1 W
```

Inductor core loss remains separate.

The buffer cannot be assumed lossless, but multi-watt loss is component-design dependent rather than automatic.

### 5.6 Nominal vs robust result

At nominal 40-mΩ / 25°C conditions:

```text
Hcond,nom ≈ 10.53 W
```

so a total win remains possible if:

```text
ΔPdynamic + PLbuf/Cbuf + κ² PT,Cu,affected + Pother < 10.53 W
```

But under the preferred robust 40-mΩ baseline-low / candidate-hot envelope, only roughly `2–4 W` conduction margin remains before those terms are counted.

Formal File61 verdict:

```text
E4+E6 nominal loss status = CONDITIONAL_SURVIVOR
E4+E6 robust loss status  = NOT_ESTABLISHED
E4+E6 novelty status      = PRIOR-ART-RICH / NOT A CANDIDATE
E4+E6 topology-synthesis priority = DOWNGRADED FROM PRIMARY
```

---

## 6. Current research phase

The project is no longer authorized to generate another generic topology graph.

Current phase:

```text
A0 POST-X1 + HFT PARAMETER / EVIDENCE CLOSURE
```

The purpose is to determine whether the actual A0 baseline makes E4+E6 physically worth returning to, or whether E2 commutation becomes the stronger remaining research target.

---

## 7. Immediate NEXT

Expected next artifact:

```text
research/62_A0_POST_X1_AND_HFT_PARAMETER_CLOSURE_CONTRACT_V1.md
```

Required closure order:

```text
A. recover/identify actual A0 X3 semiconductor technology/part if possible
B. recover/identify actual X3 switching frequency/modulation if possible
C. recover actual A0 rectifier part or establish bounded hot-VF contract
D. close A0 transformer secondary RMS + DCR/Rac / copper-loss range
E. bound HV-link capacitor ESR/ripple loss
F. establish matched reduced-order A0 vs G13-REF2 comparator model contract
```

Only after A–F may the next mainline be selected among:

```text
E4+E6 returns as a loss-driven synthesis target
E2 commutation becomes the higher-value target
neither supports a new topology contribution under the present boundary
```

Allowed:

```text
comparator-only analytical / reduced-order model work
A0 evidence acquisition
matched current-datasheet normalization
```

Still not authorized:

```text
new-proposed-topology PSIM
new-proposed-topology LTspice
Candidate #10 assignment
novelty claim
```

R2/Ryan remains comparator-only.
R7 remains weak/deferred.
Generic X1/X2/X3 overlap remains closed as a novelty-generation method.
Generic PPP remains an edge-rating framework.
