# 46 — A0 vs R2-REF1 vs R2-REF2 Matched Theoretical Scaling Screen v1

Status date: 2026-08-20  
Role: `MATCHED THEORETICAL LOSS / SCALING SCREEN`  
Research boundary: `12 Vdc / 2 kW / 325–400 Vdc HV-link / 220 Vac final target`  
Evidence status: `MIXED: VERIFIED A0 GRAPH + DATASHEET BOUNDS + MODELLED A0 COMMUTATION PROXY + PUBLISHED PRIOR-ART PARAMETERS + FIRST-ORDER SIMILARITY SCALING`  
Simulation status: `ANALYTICAL / PYTHON SWEEP COMPLETE; PSIM NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

File 45 established that generic magnetizing-current-assisted ZVS push-pull is already prior art and promoted Ryan et al. 1998 to `R2-REF2`, a mandatory extreme-low-voltage / high-current comparator.

The immediate question is no longer:

```text
Can another ZVS push-pull topology be invented?
```

It is:

> Under one matched 12-V / 2-kW boundary, does the known Ryan-type resonant/ZVS route exhibit a structural loss penalty when its output is raised from the published ~235-V class to the project's 325–400-V HV-link class, and how does that compare with A0 and the active-clamp reference direction?

This file is a screening calculation, not a final loss budget and not a topology-novelty claim.

---

## 2. Compared structures and evidence roles

### A0 — ASP-2000 physical benchmark

Retained verified features from File 12:

```text
12-V battery domain
T1/T2 center-tapped primaries
common A logical MOS bank = 10 parallel CSD18542KCS
common C logical MOS bank = 10 parallel CSD18542KCS
T1/T2 secondaries series-connected
HV bridge rectification
HV link
```

Main-switch silicon bound:

```text
CSD18542KCS RDS(on),max @ 10 V = 4 mΩ
10-way ideal parallel per logical switch
Rlogical ≈ 0.400 mΩ
```

A0 physical transformer parameters and complete measured loss remain OPEN.

### R2-REF1 — active-clamp push-pull reference direction

Reference origin:

Tsai-Fu Wu et al., "An Active-Clamp Push–Pull Converter for Battery Sourcing Applications," IEEE Transactions on Industry Applications, 2008, DOI `10.1109/TIA.2007.912748`.

For this matched screen, Wu is used only as the known PM-4 active-clamp reference principle. The numerical current comparison uses the project's retained dual-HFT / series-secondary graph and a duty/RMS proxy; it is **not** claimed to reproduce Wu's complete original circuit.

### R2-REF2 — Ryan extreme-LV ZVS LCL push-pull

Reference:

M. J. Ryan, W. E. Brumsickle, D. M. Divan, R. D. Lorenz, "A New ZVS LCL-Resonant Push-Pull DC-DC Converter Topology," IEEE Transactions on Industry Applications, 1998, DOI `10.1109/28.720458`.

Published reference context recovered and locked in File 45 includes approximately:

```text
Vin ≈ 12 V
Iin ≈ 160 A
Vout ≈ 235 V
Pout ≈ 1.8 kW
measured efficiency ≈ 93% class
switching frequency ≈ 25 kHz
LCL resonance ≈ 50 kHz
external resonant L ≈ 27 µH
transformer leakage term used in model ≈ 18 µH
resonant C ≈ 1 µF
```

The exact component values above belong to Ryan's published prototype/model and are not candidate component selections for this project.

---

## 3. Matched 12-V current anchor

Project scaling anchor:

```text
Vin = 12 V
Pout = 2000 W
η reference = 95%
```

therefore:

```text
Iin,avg,95 = 2000 / (12 × 0.95)
           ≈ 175.44 A
```

With the A0 logical-switch resistance bound:

```text
Rlogical = 0.400 mΩ
```

and ideal 50/50 push-pull conduction, the main-switch conduction floor proxy is:

```text
Pmain,A0,25C-bound
≈ Iin² Rlogical
≈ 12.31 W
```

This is a silicon-conduction proxy only. It excludes hot RDS(on), imbalance, AC/interconnect resistance, switching, magnetics and rectifier loss.

---

## 4. A0 commutation-loss anchor used only as a modelled discriminator

The previous A0 surrogate at 50 kHz produced approximately:

```text
Psnubber proxy ≈ 2.30 W
Poverlap proxy ≈ 21.05 W
Pdeadtime proxy ≈ 1.75 W
--------------------------------
Pcomm,A0,surrogate ≈ 25.10 W
```

Status:

```text
MODELLED SURROGATE
NOT MEASURED
NOT A PUBLISHED A0 LOSS VALUE
```

This file uses 25.10 W only as a break-even reference:

```text
Any PM-4 solution must save enough of this commutation bucket
while adding less conduction / circulation / resonant-component loss.
```

---

## 5. R2-REF1 duty/RMS screen

Use the first-order proxy:

```text
main-power active fraction ≈ 2D
Iactive ≈ Iavg / (2D)
Irms ≈ Iavg / sqrt(2D)
Pmain ≈ Irms² Rlogical
```

Results:

| D | Irms proxy | Main MOS conduction | Added vs A0 | Remaining 25.1-W commutation-saving headroom |
|---:|---:|---:|---:|---:|
| 0.35 | 209.69 A | 17.59 W | +5.28 W | 19.82 W |
| 0.40 | 196.15 A | 15.39 W | +3.08 W | 22.02 W |
| 0.42 | 191.42 A | 14.66 W | +2.35 W | 22.75 W |
| 0.45 | 184.93 A | 13.68 W | +1.37 W | 23.73 W |
| 0.48 | 179.06 A | 12.82 W | +0.51 W | 24.59 W |

Interpretation:

```text
R2-REF1 can only beat the A0 commutation bucket if:

Paux,cond
+ Paux,sw
+ Pclamp-cap/path
+ Pextra,circulation
+ residual switching
< remaining headroom
```

At D = 0.42, for example:

```text
remaining theoretical headroom ≈ 22.75 W
```

before magnetics/rectifier differences are considered.

This does not prove active clamp is better; it only quantifies how much added loss it can tolerate before losing the theoretical benefit relative to the current A0 surrogate.

---

## 6. R2-REF2 output-voltage scaling: first important result

Ryan reference:

```text
Vref = 235 V
Pref = 1.8 kW
Iout,ref = 1800 / 235 ≈ 7.66 A
Rload,ref = 235² / 1800 ≈ 30.68 Ω
```

Project targets at 2 kW:

| Vdc | HV current | Vdc/Vref | Rload | Rload/Rref |
|---:|---:|---:|---:|---:|
| 325 V | 6.154 A | 1.383× | 52.81 Ω | 1.721× |
| 340 V | 5.882 A | 1.447× | 57.80 Ω | 1.884× |
| 350 V | 5.714 A | 1.489× | 61.25 Ω | 1.996× |
| 380 V | 5.263 A | 1.617× | 72.20 Ω | 2.353× |
| 400 V | 5.000 A | 1.702× | 80.00 Ω | 2.608× |

At 350 V:

```text
required secondary-voltage / turns-ratio scale vs Ryan ≈ 1.489×
secondary current scale vs Ryan ≈ 0.746×
```

The immediate but incorrect shortcut would be:

```text
more turns → much more secondary copper loss
```

The first-order re-optimized copper-window relation does not support that shortcut.

---

## 7. Secondary copper-window similarity derivation

If primary flux conditions, material class and allowable current density are held comparable:

```text
Ns ∝ Vsecondary
Acu ∝ Isecondary
```

so a first-order winding-window copper demand proxy is:

```text
Ns × Acu ∝ V × I = P
```

Hence relative to Ryan:

```text
(Ns × Acu)target / (Ns × Acu)Ryan
≈ Ptarget / Pref
= 2000 / 1800
≈ 1.111×
```

This result is independent of choosing 325, 350 or 400 V because higher voltage is accompanied by lower secondary current at fixed power.

At 350 V explicitly:

```text
turns ratio scale = 1.489×
conductor-area scale at same J = 0.746×
product = 1.489 × 0.746 ≈ 1.111×
```

Therefore:

```text
235 V → 350 V
```

does **not** by itself imply a 49% increase in ideal re-optimized secondary copper-window burden.

The remaining real risks are second-order / physical-design effects:

```text
insulation thickness / creepage
winding layering
mean length per turn
skin / proximity effect
leakage inductance distribution
interwinding capacitance
rectifier voltage stress
layout / EMI
```

These remain OPEN and require magnetics-level modeling or hardware evidence.

---

## 8. LCL similarity scaling

For a first-order network similarity screen, keep:

```text
same normalized LCL impedance shape
same resonance-frequency ratio relative to switching frequency
```

Let the characteristic impedance scale with load resistance:

```text
Z0 ∝ Rload
```

For an LC pair:

```text
Z0 = sqrt(L/C)
ω0 = 1/sqrt(LC)
```

At fixed normalized resonance frequency:

```text
L ∝ Rload
C ∝ 1/Rload
```

Applying Ryan's approximate `27 µH / 18 µH / 1 µF` reference values gives the following **similarity values only**:

| Vdc | Lext proxy | Lleak-equivalent proxy | C proxy |
|---:|---:|---:|---:|
| 325 V | 46.48 µH | 30.98 µH | 0.581 µF |
| 340 V | 50.87 µH | 33.91 µH | 0.531 µF |
| 350 V | 53.90 µH | 35.93 µH | 0.501 µF |
| 380 V | 63.54 µH | 42.36 µH | 0.425 µF |
| 400 V | 70.40 µH | 46.94 µH | 0.384 µF |

These are **not component prescriptions**. They answer only whether a geometrically similar normalized LCL regime has a plausible scaling path.

---

## 9. Reactive-energy scaling result

Under the similarity relation above:

```text
Ctarget / Cref ∝ 1 / Rratio
Vtarget / Vref = voltage ratio
```

Therefore capacitor-energy scaling is:

```text
EC,target / EC,ref
≈ (Ctarget/Cref)(Vtarget/Vref)²
≈ Ptarget/Pref
≈ 1.111×
```

Likewise, for the inductive term:

```text
EL,target / EL,ref
≈ (Ltarget/Lref)(Itarget/Iref)²
≈ Ptarget/Pref
≈ 1.111×
```

The Python sweep returned the same ~1.111× factor throughout 325–400 V.

Important interpretation:

> If the Ryan LCL network is re-impedance-scaled while preserving the same normalized resonance, increasing the HV-link target from 235 V toward 325–400 V does not make stored reactive energy grow in proportion to voltage ratio. First-order stored energy tracks the ~11.1% power increase from 1.8 to 2.0 kW.

This substantially weakens the hypothesis that `higher required HV-link voltage alone` creates a structural R2-REF2 loss wall.

---

## 10. R2-REF2 magnetizing-current conduction penalty

A simple full-load sensitivity can be written as:

```text
Iprimary,rms² ≈ Iload,rms² + Im,rms²
```

Define:

```text
α = Im,rms / Iload,rms
```

then with the same logical-switch resistance:

```text
Pmain,REF2 ≈ Pmain,A0 × (1 + α²)
```

Sensitivity:

| α | Added main-MOS conduction vs A0 |
|---:|---:|
| 0.05 | ~0.03 W |
| 0.10 | ~0.12 W |
| 0.15 | ~0.28 W |
| 0.20 | ~0.49 W |
| 0.30 | ~1.11 W |
| 0.40 | ~1.97 W |

This is intentionally only a full-load RMS sensitivity. Actual Ryan-type magnetizing current, transformer current waveform and resonant current must be simulated/measured before using watt values in a publication.

The structural point is:

```text
modest magnetizing-current RMS does not automatically consume the entire ~25-W A0 commutation-loss proxy.
```

The likely larger REF2 penalties must therefore be sought in:

```text
transformer AC copper / leakage construction
LCL inductor copper + core
resonant capacitor ESR
secondary / rectifier RMS waveform
circulating / subresonant current
frequency-dependent magnetic loss
```

---

## 11. First matched ranking — NOT a final efficiency ranking

### A0

Strengths:

```text
simple known physical graph
no added resonant power component
main-switch conduction floor already relatively low through 10-way parallel silicon
```

Weakness:

```text
hard-switch / RC / leakage dissipation remains a modeled material bucket
```

Current status:

```text
physical benchmark
complete watts OPEN
```

### R2-REF1

Strength:

```text
known active recovery / ZVS route
can remove part of A0 hard-switch + snubber loss
```

Weakness at 12 V:

```text
narrower main power interval can increase RMS current
auxiliary/clamp path adds conduction and circulation
```

Current screen:

```text
possible net benefit
but only if all added REF1 losses stay below ~20–25 W headroom depending on D
```

### R2-REF2

Strengths:

```text
already demonstrated in extreme-LV / hundred-ampere prior art
main ZVS does not require a sustained active-clamp return path
first-order 235→325–400 V scaling does not show a voltage-driven reactive-energy or copper-window explosion
```

Weaknesses / open terms:

```text
resonant inductor / capacitor loss
magnetics AC loss
secondary RMS / rectifier stress
frequency and resonance optimization
implementation complexity
```

Current theoretical assessment:

```text
R2-REF2 = strongest known R2 comparator after this screen
```

This is not a statement that R2-REF2 is globally optimal.

---

## 12. Main falsification result from this screen

Pre-screen hypothesis:

```text
Ryan-type 235-V solution may become structurally unattractive
when forced toward 325–400 V at 12 V / 2 kW.
```

Current first-order result:

```text
NOT SUPPORTED by simple voltage-ratio scaling alone.
```

Specifically:

```text
secondary copper-window proxy ∝ power, not Vdc alone
normalized LCL reactive energy ∝ power, not Vdc alone
HV current falls as Vdc rises
```

Therefore the research must not manufacture a gap by assuming:

```text
higher output voltage → proportionally worse transformer/resonant loss
```

Any surviving R2 physical gap must come from second-order physical effects or matched total loss, not static voltage ratio by itself.

---

## 13. Decision

Formal decision after this analytical screen:

```text
A0                    = RETAIN physical benchmark
R2-REF1               = RETAIN active-clamp comparator
R2-REF2               = PROMOTE strongest R2 comparator
R2 new-topology search = PAUSE
```

Do not generate R2-C4 immediately.

Next useful execution is:

```text
R2-REF2 modern matched model
12 V / 2 kW / 350 V center point
↓
PSIM-level ideal waveform validation
↓
modern semiconductor + magnetic loss re-optimization
↓
compare against A0 and R2-REF1 under the same loss ledger
```

However, because Ryan already occupies the same extreme-LV current regime, a new R2 topology is justified only if the matched model exposes a surviving structural loss term that known R2 methods cannot remove without larger added loss.

Parallel research option:

```text
advance R6 / R7 / R8 IEEE-gated mechanism combinations
```

because R2 topology novelty risk is now high and its best known reference scales more plausibly than initially hypothesized.

---

## 14. Formal status

```text
Python matched scaling sweep              = COMPLETE
PSIM matched waveform/loss comparison     = NOT EXECUTED
A0 complete measured loss                 = OPEN
R2-REF1 matched total loss                = OPEN
R2-REF2 matched total loss                = OPEN
235→325–400V first-order scaling wall      = NOT FOUND
R2-REF2 priority as comparator             = HIGH
new R2 topology justification              = NOT ESTABLISHED
Candidate #10                              = HOLD
Novelty                                    = NOT_ESTABLISHED
```
