# 60 — E4+E6 Post-HFT Double-Processing Matched Loss Crossover v1

Status date: 2026-08-20  
Role: `POST-X1 SEMICONDUCTOR CROSSOVER / RECTIFIER+VSI VS DIRECT-HF-LINK REFERENCE`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Canonical post-X1 comparison point: `350 Vdc-class`  
Evidence status: `VERIFIED/LOCKED GRAPH CLASSES + CURRENT DEVICE-DATASHEET CONTRACT + FIRST-PRINCIPLES CROSSOVER + PRIOR-ART REFERENCE CHECK`  
Simulation status: `ANALYTICAL / PYTHON SWEEP COMPLETE; PSIM/LTspice NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

File59 separated the best known loss target from the best current topology-synthesis target:

```text
highest known/bounded loss bucket:
E2 primary commutation/snubber

selected synthesis crossover:
JOINT E4 + E6
secondary rectification + downstream VSI semiconductor processing
```

The purpose of File60 is not to propose a new direct-HF-link converter. The direct-HF-link / matrix-cycloconverter class is already established prior art and is used here only as a hard comparator.

The question is:

> At the same 12-V / 2-kW system boundary and matched modern 650-V semiconductor technology, does removing the standalone rectifier + VSI sequence create enough real loss headroom to pay for matrix/cycloconverter conduction, HF commutation, X2 relocation and transformer-current interaction?

No new graph may be promoted until this crossover is credible.

---

## 2. Two normalized post-X1 paths

### 2.1 Baseline post-X1 path

```text
HFT secondary
   |
E4 full-wave HV rectifier
   |
350-V-class HV link
   |
E5 passive 2ω energy storage / DC-link capacitor
   |
E6 full-bridge VSI
   |
output filter
   |
220 Vac / 50 Hz
```

The HFT / primary X1 path is not re-scored here except when the merged reference creates an interaction term that changes transformer RMS current.

### 2.2 Known merged reference

```text
HFT secondary / center-tapped HFT
   |
secondary bidirectional matrix / cycloconverter
   |
AC filter
   |
220 Vac / 50 Hz

+ separately identifiable X2 function
  using center-tap/common-mode state + Lbuf/Cbuf in the strongest known reference class
```

Reference class:

```text
G13-REF1 = isolated HF-link + secondary cycloconverter/matrix
G13-REF2 = Takaoka/Takahashi/Itoh center-tapped matrix converter with power decoupling
```

The reference is not Candidate #10.

---

## 3. Common electrical scales

At 2 kW:

```text
IHV,ideal = 2000/350 = 5.714 A
Iout,rms  = 2000/220 = 9.091 A
Iout,pk   = 12.856 A
Vac,pk    = 311.13 V
```

The 2ω energy requirement remains:

```text
E2ω,pk = P/(4πf) = 3.183 J
E2ω,pp = 6.366 J
```

This energy function exists in both paths. It may be implemented differently, but it cannot be removed.

---

## 4. Matched 650-V semiconductor technology contract

### 4.1 Rectifier floor

Retain the File47 matched rectifier reference:

```text
Infineon IDW10G65C5
650 V / 10 A SiC Schottky
VF,typ @25°C ≈ 1.5 V
VF,max @25°C ≈ 1.7 V
VF,typ @150°C ≈ 1.8 V
Qc,typ ≈ 15 nC
```

For the conservative baseline-low crossover, use the 25°C typical value rather than the hot value:

```text
Prect,low
≈ 2 × 1.5 V × 5.714 A
≈ 17.14 W
```

This is a matched-technology floor, not a measured A0 diode loss.

### 4.2 Current 650-V SiC MOSFET range

Current commercial 650-V SiC MOSFET examples span at least the following 25°C RDS(on) range:

```text
15 mΩ class
40 mΩ class
45 mΩ class
60 mΩ class
```

The crossover is therefore swept across this range instead of choosing one vendor as the proposed device.

This is a technology sensitivity contract, not procurement selection.

---

## 5. Conduction-only crossover

### 5.1 Baseline VSI conduction proxy

For a conventional full bridge with two MOSFET dies in the instantaneous load-current path:

```text
PVSI,cond ≈ 2 Rvsi Iout,rms²
```

### 5.2 Matrix/cycloconverter conduction proxy

A practical bidirectional AC switch cell may require two anti-series MOSFETs.

Two matrix cells are load-bearing during an active power-transfer state, giving a default four-die path:

```text
Pmatrix,cond ≈ 4 Rmatrix Iout,rms²
```

This is a conservative normalized implementation assumption. A true single-die reverse-blocking device or another lower-die-count realization would change the result and must be declared explicitly.

### 5.3 Matched-R result

If:

```text
Rvsi = Rmatrix = R
```

then the conduction-only saving from replacing rectifier + VSI by the matrix path is:

```text
ΔPcond
= Prect + 2 R Iout² - 4 R Iout²
= Prect - 2 R Iout²
```

The matrix conduction crossover occurs at:

```text
R < Prect / (2 Iout²)
  < 17.14 / (2 × 9.091²)
  < 0.1037 Ω
```

Therefore:

```text
RDS(on) crossover ≈ 104 mΩ per die @25°C proxy
```

Modern 15–60-mΩ 650-V SiC devices sit below this conduction-only threshold.

### 5.4 Sensitivity table

| matched 650-V MOSFET RDS(on) | baseline VSI conduction | 4-die matrix conduction | rectifier+VSI minus matrix conduction headroom |
|---:|---:|---:|---:|
| 15 mΩ | 2.48 W | 4.96 W | 14.66 W |
| 40 mΩ | 6.61 W | 13.22 W | 10.53 W |
| 45 mΩ | 7.44 W | 14.88 W | 9.70 W |
| 60 mΩ | 9.92 W | 19.83 W | 7.23 W |
| 100 mΩ | 16.53 W | 33.06 W | 0.61 W |

Interpretation:

> The known merged reference is not killed by conduction alone. With current SiC technology, removing the diode bridge can compensate for the additional matrix conducting dies.

But the available total-loss headroom is only of order 7–15 W for ordinary 15–60-mΩ device classes before switching, X2 and transformer interactions are counted.

---

## 6. Switching / commutation crossover budget

Let:

```text
ΔPdynamic
= Psw,matrix + Pcomm,matrix
- Psw,VSI
```

and let all other incremental merged-path costs be grouped as:

```text
Pinteraction
= ΔPtransformer
+ PLbuf
+ PCbuf,ESR
- PDC-link,ESR,baseline
+ Pfilter,delta
+ Pother
```

Then:

```text
ΔPtotal,post
= ΔPcond
- ΔPdynamic
- Pinteraction
```

The merged reference only beats the baseline when:

```text
ΔPtotal,post > 0
```

At a 50-kHz HF-link, the conduction-only headroom corresponds to the following maximum **total extra energy per HF cycle** if every remaining term were collapsed into one equivalent dynamic penalty:

| matched RDS(on) | conduction headroom | total extra budget per 50-kHz cycle |
|---:|---:|---:|
| 15 mΩ | 14.66 W | 293 µJ/cycle |
| 40 mΩ | 10.53 W | 211 µJ/cycle |
| 45 mΩ | 9.70 W | 194 µJ/cycle |
| 60 mΩ | 7.23 W | 145 µJ/cycle |

This is not a switching-energy measurement. It is the entire remaining loss budget available to matrix switching, commutation, X2 interaction and any extra magnetic/passive loss.

Known HF-link prior art demonstrates that this dynamic term can be structurally reduced:

```text
Takaoka/Takahashi/Itoh:
- matrix converter operated with PDM
- ZVS for matrix switches
- primary switches partially ZVS

Blinov/Korkh/Vinnikov/Galkin/Norrga:
- quasi-resonant commutation
- DC-side ZVS
- two AC-side switches can operate at fundamental frequency
- remaining AC-side switching can achieve ZCS
```

This establishes feasibility of low-commutation-loss operation.

It does NOT establish that the merged path beats the matched baseline total loss at the present 12-V / 2-kW boundary.

---

## 7. X2 / transformer interaction is the decisive hidden term

### 7.1 Baseline

The conventional HV-link capacitor performs the 2ω energy buffering after X1.

Its actual:

```text
capacitor ESR loss
ripple current
thermal burden
```

remain OPEN for A0.

No additional switching device is required solely to charge/discharge the stiff HV-link capacitor in the normalized baseline.

### 7.2 Strong merged reference

The strongest known G13-REF2 class uses:

```text
center-tapped HFT
+ common-mode bridge voltage
+ small Lbuf/Cbuf
+ no additional APD switching devices
```

The advantage is that X2 is integrated without an extra active switch stage.

The cost is that the buffer/common-mode current becomes part of the transformer / bridge current environment.

The prior-art description explicitly notes that buffer current overlaps transformer current and can help satisfy primary ZVS conditions.

Therefore X2 loss is not removed; it is partly relocated into:

```text
transformer RMS current
bridge RMS current
Lbuf copper/core loss
Cbuf ESR
common-mode commutation/control interaction
```

### 7.3 First-order transformer-RMS sensitivity

Use a topology-independent sensitivity variable:

```text
κ = Ibuf,rms,referred / Imain,rms,referred
```

If the buffer-current component is approximately orthogonal to the main transferred-current component, transformer copper exposure scales approximately as:

```text
Irms,new² / Irms,main² ≈ 1 + κ²
```

and:

```text
ΔPT,Cu ≈ κ² PT,Cu,baseline
```

For a simple high-voltage-domain scale:

```text
Ibuf,rms ≈ P/(sqrt(2) × 350)
          ≈ 4.04 A

Imain scale ≈ P/350
            ≈ 5.714 A

κ ≈ 0.707
κ² ≈ 0.5
```

Thus a useful sensitivity point is:

```text
ΔPT,Cu ≈ 0.5 × PT,Cu,baseline
```

This is not a waveform-accurate G13-REF2 transformer model. It is a crossover proxy showing how quickly the apparent rectifier saving can be consumed by X2 current routed through the transformer.

If this 50%-extra-copper proxy alone consumes the entire conduction headroom, the corresponding maximum baseline transformer copper loss is:

| matched RDS(on) | conduction headroom | max PT,Cu,baseline if κ²=0.5 consumes all headroom |
|---:|---:|---:|
| 15 mΩ | 14.66 W | 29.33 W |
| 40 mΩ | 10.53 W | 21.06 W |
| 45 mΩ | 9.70 W | 19.41 W |
| 60 mΩ | 7.23 W | 14.45 W |

And these thresholds still leave **zero** budget for matrix switching, Lbuf, Cbuf ESR or any other interaction term.

Therefore actual A0 transformer copper/RMS data is now a first-order discriminator for the E4+E6 crossover even though File59 initially treated E3 as a separate edge.

---

## 8. Why stage-count reduction is not yet a loss proof

Baseline loss fate:

```text
E4 diode rectifier conduction   = potentially REMOVED
E6 standalone VSI boundary      = potentially MERGED
stiff HV-link boundary          = potentially REMOVED as a physical bus
2ω energy requirement           = RETAINED / RELOCATED
```

Merged-reference new/relocated terms:

```text
matrix multi-die conduction     = INTRINSIC_NEW relative to diode rectifier
HF matrix commutation           = INTERACTION_NEW
bidirectional-switch realization= SUPPORT_NEW / topology-dependent
center-tap/common-mode X2 current= RELOCATED
transformer RMS increment       = INTERACTION_NEW
Lbuf/Cbuf loss                  = INTRINSIC_NEW / SUPPORT_NEW
```

Therefore:

```text
rectifier removed != 17.14 W guaranteed net saving
stage removed     != function removed
DC-link removed   != 2ω energy removed
```

---

## 9. Prior-art hard-comparator status

The relevant reference region is firmly established.

### G13-REF2

Nagisa Takaoka, Hiroki Takahashi, Jun-ichi Itoh,
“Isolated Single-Phase Matrix Converter Using Center-Tapped Transformer for Power Decoupling Capability,”
IEEE Transactions on Industry Applications,
DOI `10.1109/TIA.2017.2774760`.

Published structure/behavior:

```text
full-bridge inverter
+ high-frequency center-tapped transformer
+ matrix converter
+ PDM / matrix ZVS
+ common-mode transformer voltage
+ small buffer capacitor/LC
+ no additional switches for power decoupling
```

The 1-kW prototype demonstrates power-decoupling and output-THD feasibility.

The paper does not provide the matched 12-V / 2-kW total-loss comparison required by this project; efficiency/volume closure therefore cannot be imported as evidence for our boundary.

### G13-REF3 soft-switching comparator

A. Blinov et al.,
“Soft-Switching Modulation Method for Full-Bridge DC-AC HF-Link Inverter,”
IECON 2019,
DOI `10.1109/IECON.2019.8927186`.

This establishes that the HF-link matrix/cycloconverter class has mature soft-switching techniques and cannot be compared using an artificially hard-switched matrix implementation.

Thus any future candidate must beat a **soft-switched known merged reference**, not merely the A0 rectifier+VSI baseline.

---

## 10. Formal crossover result

### Gate 1 — conduction-only

```text
RESULT = SURVIVES
```

Reason:

> With current 15–60-mΩ / 650-V SiC technology, the removed SiC-diode forward-drop bucket is large enough to pay for the extra matrix conducting dies in the normalized four-die path.

### Gate 2 — switching/commutation

```text
RESULT = PLAUSIBLE / NOT CLOSED
```

Reason:

> Known ZVS/ZCS/PDM methods can reduce the matrix dynamic penalty, but the matched watt value is not established at the present boundary.

### Gate 3 — X2 / transformer interaction

```text
RESULT = MATERIAL / UNRESOLVED
```

Reason:

> The merged power-decoupling reference routes buffer/common-mode current through the transformer environment. At the 350-V scaling point the buffer RMS-current scale is ~4.04 A versus ~5.71 A main-power current scale; a simple orthogonal-current proxy creates ~50% additional transformer-copper exposure.

### Total gate

```text
E4+E6 MERGED REFERENCE
= PHYSICALLY PLAUSIBLE LOSS SURVIVOR
= NOT YET A ROBUST TOTAL-LOSS WINNER
= CROSSOVER_UNRESOLVED
```

No Candidate #10 is assigned.

---

## 11. What this changes in the mainline

File59 selected `E4+E6` because it was a plausible double-processing boundary.

File60 narrows that statement:

```text
E4+E6 is still worth comparing,
but the possible net advantage is only a roughly 7–15-W conduction headroom
for ordinary current 15–60-mΩ device classes before dynamic/X2/magnetic interactions.
```

This is materially smaller than the naive assumption:

```text
remove rectifier (~17 W)
+ remove VSI
= large free saving
```

The merged reference must now be treated as a tightly budgeted crossover problem.

---

## 12. Immediate next evidence gate

Do not synthesize a new E4+E6 graph yet.

Immediate next task:

```text
E4+E6 CROSSOVER UNCERTAINTY CLOSURE
```

The minimum missing quantities are:

### Baseline / A0-like

```text
A. actual/representative VSI device technology and RDS(on)/VCE loss
B. VSI switching frequency and switching-energy bucket
C. actual rectifier current waveform / hot VF
D. HV-link capacitor ripple/ESR loss
E. A0 transformer secondary RMS and copper-loss scale
```

### Known merged reference

```text
F. normalized matrix-switch RMS current and practical bidirectional die realization
G. matrix switching/commutation energy under a soft-switched reference modulation
H. referred buffer-current RMS κ
I. center-tapped transformer copper increment
J. Lbuf / Cbuf ESR/core loss
```

Then apply:

```text
Pbaseline,low
= Prect,low
+ PVSI,cond,low
+ PVSI,sw,low
+ PX2,baseline,low

Pmerged,high
= Pmatrix,cond,high
+ Pmatrix,sw/comm,high
+ ΔPT,interaction,high
+ PLbuf/Cbuf,high
+ PX2,other,high
```

Robust survive only if:

```text
Pmerged,high < Pbaseline,low
```

Until then:

```text
PSIM AS A NEW PROPOSED TOPOLOGY = NOT AUTHORIZED
COMPARATOR-ONLY ANALYTICAL / REDUCED-ORDER WORK = AUTHORIZED
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty = NOT_ESTABLISHED
```
