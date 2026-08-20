# 61 — E4+E6 Crossover Uncertainty Closure v1

Status date: 2026-08-20  
Role: `E4+E6 UNCERTAINTY ENVELOPE / THERMAL-DYNAMIC-X2-HFT CROSSOVER CLOSURE`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Canonical post-X1 comparison point: `350 Vdc-class`  
Evidence status: `A0 REPOSITORY AUDIT + CURRENT DATASHEET ENVELOPE + FIRST-PRINCIPLES RMS REFINEMENT + HARD-COMPARATOR LITERATURE PARAMETERS`  
Simulation status: `ANALYTICAL / REDUCED-ORDER ONLY; PSIM/LTspice NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

File60 showed that a known direct-HF-link matrix/cycloconverter reference survives the **conduction-only** crossover against the A0-like post-HFT path:

```text
HFT -> diode rectifier -> HV-link/X2 -> VSI
```

but only leaves about `7–15 W` of nominal conduction headroom for ordinary 15–60-mΩ / 650-V SiC device classes before switching, X2 and transformer interaction are counted.

File61 closes as much of that uncertainty as can be closed without inventing A0 measurements.

The objective is to decide whether `E4+E6` remains a defensible immediate topology-synthesis target or should be downgraded to a comparator/evidence branch.

---

## 2. Repository audit — what is still actually unknown in A0

The current A0 repository evidence verifies:

```text
D1,D2 -> BUS+
D5,D6 -> BUS-
HV DC-link -> HV inverter / X3 -> AC output
```

but the present formal research files do **not** establish:

```text
actual populated D1/D2/D5/D6 part number
actual populated X3 semiconductor part number
actual X3 switching frequency
actual X3 switching-energy bucket
actual rectifier junction temperature / hot VF
actual A0 transformer winding DCR/Rac
actual transformer secondary RMS waveform
actual HV-link capacitor ESR/ripple loss
```

Therefore none of those may be promoted to `VERIFIED A0 watts` in this file.

Status:

```text
A0 X3 DEVICE / fs = OPEN
A0 RECTIFIER DEVICE / HOT VF = OPEN
A0 HFT Cu/RMS = OPEN
A0 HV-LINK ESR = OPEN
```

This is a real evidence boundary, not a reason to substitute assumed values.

---

## 3. Rectifier thermal envelope

Retain the File47/File60 modern matched SiC Schottky reference:

```text
Infineon IDW10G65C5 class
650 V / 10 A
VF,typ @25°C, 10 A  ≈ 1.5 V
VF,max @25°C, 10 A  ≈ 1.7 V
VF,typ @150°C, 10 A ≈ 1.8 V
VF,max @150°C, 10 A ≈ 2.1 V
```

At the 350-V / 2-kW average-current scale:

```text
IHV = 5.714 A
```

constant-VF forward-drop proxies are:

```text
25°C typical:  Prect ≈ 2 × 1.5 × 5.714 = 17.14 W
150°C typical: Prect ≈ 2 × 1.8 × 5.714 = 20.57 W
```

These are matched-device proxies, not A0 measurements and not waveform-accurate diode models.

Important consequence:

> Heating the rectifier increases the baseline loss and therefore can make rectifier removal look more attractive; robust comparison must not rely on that favorable effect unless the baseline hot state is actually established.

For the preferred robust gate, keep:

```text
Prect,baseline,low = 17.14 W
```

until tighter A0 evidence exists.

---

## 4. MOSFET thermal envelope materially changes the matrix crossover

Current 650-V CoolSiC G2 examples establish that the 25°C `RDS(on)` label is not the hot operating resistance.

Useful thermal sensitivities:

```text
40-mΩ class: datasheet normalized RDS(on) is about 1.5× near 175°C
60-mΩ class: 60 mΩ @25°C -> about 98 mΩ @175°C (≈1.63× typical)
```

Therefore File60's 25°C conduction headroom is a nominal screen only.

### 4.1 Preferred robust conduction comparison

Use deliberately asymmetric uncertainty bounds:

```text
baseline low:
- rectifier at 1.5-V typical floor
- VSI MOSFET at 25°C nominal R

merged high:
- matrix MOSFET at hot multiplier kT
```

Then:

```text
Pbaseline,cond,low
= Prect,low + 2 R25 Iout,rms²

Pmerged,cond,high
= 4 (kT R25) Iout,rms²

Hrob,cond
= Pbaseline,cond,low - Pmerged,cond,high
```

At `Iout,rms = 9.091 A`:

| R25 per die | hot multiplier | baseline conduction low | merged conduction high | robust conduction headroom |
|---:|---:|---:|---:|---:|
| 15 mΩ | 1.50 | 19.62 W | 7.44 W | **12.18 W** |
| 40 mΩ | 1.50 | 23.75 W | 19.83 W | **3.92 W** |
| 40 mΩ | 1.63 | 23.75 W | 21.55 W | **2.20 W** |
| 60 mΩ | 1.50 | 27.06 W | 29.75 W | **−2.69 W** |
| 60 mΩ | 1.63 | 27.06 W | 32.33 W | **−5.27 W** |

Formal consequence:

```text
File60 nominal conduction SURVIVOR
!=
robust conduction survivor across the full 15–60-mΩ technology range
```

The merged path requires low-R / thermally controlled devices to retain a meaningful robust budget.

At the 40-mΩ class, only about `2–4 W` remain under the preferred baseline-low / candidate-hot conduction envelope before any matrix dynamic, buffer or transformer-interaction loss is counted.

---

## 5. Representative VSI hard-switching proxy — baseline remains OPEN, but scale is small enough to bound

A current 40-mΩ / 650-V CoolSiC G2 datasheet gives approximately:

```text
Etot = Eon + Eoff ≈ 46 µJ
at 400 V / 22.9 A / RG,ext=1.8 Ω
```

This is not the A0 X3 device.

As a deliberately crude linear-current sensitivity only:

```text
Etot(9.09 A) ≈ 46 µJ × 9.09/22.9 ≈ 18.3 µJ
```

For four hard-switched full-bridge devices:

```text
PVSI,sw,proxy ≈ 4 Etot fs
```

which gives:

| assumed VSI fs | matched-device hard-switch proxy |
|---:|---:|
| 10 kHz | ~0.73 W |
| 20 kHz | ~1.46 W |
| 50 kHz | ~3.65 W |
| 100 kHz | ~7.30 W |

This is **not** an A0 switching-loss claim.

It establishes only that a modern 650-V SiC VSI switching bucket at ~9-A current is plausibly of the same order as the remaining File60 headroom, not orders of magnitude larger.

Because the actual A0 X3 device and `fs` are still unknown:

```text
A0 VSI switching = OPEN
```

and the preferred robust baseline-low gate must not assume a large switching saving.

---

## 6. Known merged reference — dynamic-loss uncertainty is narrower than a hard-switch matrix assumption

The hard comparator remains the Takaoka/Takahashi/Itoh isolated single-phase matrix-converter family plus later soft-switching HF-link work.

Established reference behavior includes:

```text
matrix PDM synchronized to zero-voltage intervals
matrix-switch ZVS
partial primary-side ZVS
later HF-link modulation with DC-side ZVS / AC-side ZCS
no separate active APD switch stage in the center-tapped reference
```

Published reference conditions are not the project's matched 12-V/2-kW boundary, but they establish that a fair comparator must be soft-switched.

Reported reference-scale parameters include approximately:

```text
rated power               ~1 kW class
DC bus                    ~350–380 V class
full-bridge carrier       ~100 kHz
matrix-control carrier    ~10 kHz class
buffer inductor           mH class
buffer capacitor          hundreds-of-µF class
```

Therefore a deliberately hard-switched matrix is not an admissible `candidate-high` reference.

However, the literature does not provide a matched 12-V / 2-kW semiconductor-loss number that can be imported directly.

Status:

```text
Pmatrix,sw/comm = BOUNDED BY SOFT-SWITCHING MECHANISM / WATTS NOT CLOSED
```

---

## 7. Correction to File60 transformer-current sensitivity

File60 used the simple power/current scales:

```text
Imain ~ P/350 = 5.714 A
Ibuf,rms ~ P/(sqrt(2)×350) = 4.04 A
```

and therefore obtained `κ≈0.707`, `κ²≈0.5`.

That is useful as a power-domain proxy but it is not the best transformer-RMS proxy for a PDM direct-HF-link inverter.

### 7.1 Differential transformer-current RMS

For unity-PF output:

```text
vo = Vm sin(θ)
io = Ipk sin(θ)
```

and an HF-link square-wave magnitude `Vs`, the active pulse-density duty is approximately:

```text
d(θ) = m |sin(θ)|
m = Vm/Vs
```

If the transformer carries output current during active HF-link pulses, the differential RMS component obeys:

```text
IT,diff,rms²
≈ < d(θ) io²(θ) >
= m Ipk² < |sin(θ)|³ >

<|sin|³> = 4/(3π)
```

At:

```text
Vm = 311.13 V
Vs = 350 V
m  = 0.889
Ipk = 12.856 A
```

this gives:

```text
IT,diff,rms ≈ 7.90 A
```

This is a better first-order main-transformer current scale than 5.714 A for the direct HF-link PDM current path.

### 7.2 Buffer/common-mode current envelope

The buffer current depends on the actual buffer-capacitor voltage trajectory.

A simple power-current scale is:

```text
Ibuf,rms ≈ P/(sqrt(2) Vbuf,eff)
```

For `Vbuf,eff = 200...350 V`:

| Vbuf,eff | Ibuf,rms proxy | κ=Ibuf/7.90 | κ² |
|---:|---:|---:|---:|
| 200 V | 7.07 A | 0.895 | 0.801 |
| 250 V | 5.66 A | 0.716 | 0.513 |
| 300 V | 4.71 A | 0.597 | 0.356 |
| 350 V | 4.04 A | 0.512 | 0.262 |

Thus File60's `κ²≈0.5` remains a useful center sensitivity near a 250-V effective buffer voltage, but the admissible first-order interaction range is wider:

```text
ΔPT,Cu / PT,Cu,affected
~ 0.26 ... 0.80
```

before waveform-specific correlation, winding partition and AC-resistance effects.

Formal correction:

```text
TRANSFORMER COPPER INTERACTION
= MATERIAL
= NOT FIXED AT 50%
= STRONGLY BUFFER-VOLTAGE / CURRENT-PATH DEPENDENT
```

---

## 8. PQ50 context prevents an unsupported assumption that transformer copper must automatically kill the merged path

File27 records a separate real PQ50-class approval sheet:

```text
M1-PQ50-V108-A
secondary DCR samples ≈ 38.6 / 38.9 mΩ
```

This is `CONTEXT_ONLY`, not A0 evidence.

At the simple 5.714-A HV current scale:

```text
I²R ≈ 1.26 W per 38.7-mΩ secondary winding
```

and two such series windings would be of order:

```text
~2.53 W
```

before AC-resistance and waveform multipliers.

This does **not** establish A0 transformer copper loss.

It only prevents the opposite unsupported shortcut:

```text
PQ50 / high ratio => transformer Cu must already exceed 20 W
```

Actual A0 `PT,Cu` remains OPEN.

---

## 9. Lbuf/Cbuf loss should be judged by resistance/core thresholds, not guessed watts

For the X2 buffer current:

```text
P_R = Ibuf,rms² R_eq
```

Therefore the equivalent series resistance that produces **1 W** is:

| Ibuf,rms | R_eq for 1 W |
|---:|---:|
| 4.04 A | ~61 mΩ |
| 4.71 A | ~45 mΩ |
| 5.66 A | ~31 mΩ |
| 7.07 A | ~20 mΩ |

This `R_eq` may represent capacitor ESR, inductor DCR, winding AC resistance or their sum only for the appropriate current path.

Inductor core loss remains separate.

Thus an mH-class buffer at several amperes cannot be called lossless, but neither is a multi-watt penalty automatic.

Status:

```text
PLbuf/Cbuf = PARAMETRIC / COMPONENT DESIGN REQUIRED
```

---

## 10. Nominal total-loss crossover envelope

At the nominal 40-mΩ / 25°C matched-device point, File60 gives:

```text
Hcond,nom ≈ 10.53 W
```

The remaining condition is:

```text
Hcond,nom
>
ΔPdynamic
+ PLbuf/Cbuf
+ κ² PT,Cu,affected
+ Pother
```

Useful sensitivity examples:

### Case N1 — favorable buffer-voltage / low interaction

```text
κ² = 0.26
other incremental loss = 2 W
```

then the allowed affected-transformer copper baseline is:

```text
PT,Cu,affected < (10.53-2)/0.26 ≈ 32.8 W
```

### Case N2 — center sensitivity

```text
κ² = 0.50
other incremental loss = 3 W
```

then:

```text
PT,Cu,affected < (10.53-3)/0.50 ≈ 15.1 W
```

### Case N3 — low buffer voltage / stronger interaction

```text
κ² = 0.80
other incremental loss = 4 W
```

then:

```text
PT,Cu,affected < (10.53-4)/0.80 ≈ 8.2 W
```

Therefore the nominal crossover is **genuinely conditional**, not structurally dead and not structurally won.

---

## 11. Preferred robust gate fails to close for ordinary 40–60-mΩ classes

The project's preferred robust authority is:

```text
Pmerged,high < Pbaseline,low
```

Using only conduction uncertainty already shows:

```text
15-mΩ class, kT=1.5  -> ~12.18 W robust conduction headroom
40-mΩ class, kT=1.5  -> ~3.92 W
40-mΩ class, kT=1.63 -> ~2.20 W
60-mΩ class, kT=1.5  -> conduction robust FAIL
```

For the 40-mΩ class, if `κ²=0.5`, the transformer-copper interaction alone must satisfy approximately:

```text
PT,Cu,affected < 7.84 W   (kT=1.5, zero other loss)
PT,Cu,affected < 4.40 W   (kT=1.63, zero other loss)
```

and any dynamic/Lbuf/Cbuf loss tightens these limits further.

Thus:

```text
ROBUST E4+E6 WIN
= NOT ESTABLISHED
```

The result is strongly device-RDS(on), junction-temperature, buffer-voltage and transformer-current dependent.

---

## 12. File61 formal decision

### What survives

```text
1. Removing the standalone rectifier remains a real conduction opportunity.
2. A soft-switched direct-HF-link matrix reference is physically credible.
3. Post-X1 integration avoids adding a new 175-A source-domain edge.
4. Nominal matched loss can still favor the merged reference for low-R SiC and controlled X2 interaction.
```

### What does not survive as a strong mainline claim

```text
1. Stage-count reduction does not establish a robust total-loss win.
2. The nominal ~7–15-W File60 headroom is not robust across thermal/device envelopes.
3. The transformer-X2 interaction is not a fixed 50%; it spans a wide first-order range.
4. Actual A0 VSI / rectifier / transformer parameters remain missing.
5. The merged graph itself is mature prior art.
```

Formal classification:

```text
E4+E6 nominal loss status
= CONDITIONAL_SURVIVOR

E4+E6 robust loss status
= NOT_ESTABLISHED

E4+E6 novelty status
= PRIOR-ART-RICH / NOT A CANDIDATE

E4+E6 immediate topology-synthesis priority
= DOWNGRADE FROM PRIMARY
```

This is not a rejection of direct HF-link technology. It is a rejection of using the generic `rectifier+VSI removal` argument as the next novelty generator before hard evidence closes the crossover.

---

## 13. Mainline consequence — stop generic graph synthesis and close discriminating evidence

No new Candidate #10 graph is authorized after File61.

The next formal task is an evidence/model closure contract, not another topology permutation.

Immediate next working title:

```text
research/62_A0_POST_X1_AND_HFT_PARAMETER_CLOSURE_CONTRACT_V1.md
```

Required closure order:

```text
A. identify actual A0 X3 semiconductor technology / part if recoverable
B. identify actual X3 switching frequency / modulation if recoverable
C. identify actual A0 rectifier part or establish a bounded hot-VF contract
D. close A0 transformer secondary RMS + DCR/Rac / copper-loss range
E. bound HV-link capacitor ESR/ripple loss
F. build a matched reduced-order A0 vs G13-REF2 comparator model
```

Only after A–F may the project decide whether:

```text
E4+E6 returns as a real loss-driven synthesis target
or
E2 commutation becomes the higher-value remaining physical target
or
neither supports a new topology contribution under the present boundary
```

Comparator-only simulation/model work is admissible.

New-proposed-topology PSIM remains unauthorized.

---

## 14. Explicit non-results

```text
A0 X3 loss = NOT MEASURED / NOT IDENTIFIED
A0 rectifier hot loss = NOT MEASURED
A0 transformer Cu loss = NOT MEASURED
G13-REF2 matched 2-kW efficiency = NOT ESTABLISHED
PSIM = NOT EXECUTED
LTspice = NOT EXECUTED
hardware = NOT EXECUTED
Candidate #10 = HOLD / NOT_ASSIGNED
Novelty = NOT_ESTABLISHED
```
