# 47 — R2-REF2 Modern Matched Loss Contract and Crossover Screen v1

Status date: 2026-08-20  
Role: `MODERN MATCHED COMPONENT CONTRACT / LOSS-LOCATION CROSSOVER / PRE-SIMULATION SCREEN`  
Research boundary: `12 Vdc / 2 kW / 350 Vdc center HV-link / 220 Vac final target`  
Evidence status: `VERIFIED A0 GRAPH + CURRENT DATASHEET CONTRACT + MODELLED A0 COMMUTATION ANCHOR + FIRST-ORDER CROSSOVER ANALYSIS`  
Simulation status: `ANALYTICAL / PYTHON SWEEP COMPLETE; PSIM/LTspice NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

File 46 showed that scaling the Ryan 1998 reference from ~235 V / 1.8 kW toward 325–400 V / 2 kW does not, by itself, create a first-order copper-window or reactive-energy explosion.

This file removes another source of unfair comparison:

```text
1998 device technology
vs
modern A0 silicon
```

The topology comparison is therefore normalized to a common modern component technology contract before any detailed PSIM/LTspice comparison.

The primary question becomes:

> Where are the additional losses physically processed — in the 12-V / ~175-A domain or after X1 in the ~350-V / ~5.7-A domain — and how large can those added losses become before a soft-switching reference loses the modeled A0 commutation benefit?

---

## 2. Common matched boundary

Center point:

```text
Vin = 12 V
Pout = 2000 W
HV-link = 350 Vdc
eta reference current scale = 95%
fs = 50 kHz
```

Therefore:

```text
Iin,avg,95 = 2000/(12×0.95) = 175.44 A
I_HV,ideal = 2000/350 = 5.714 A
```

The final 220-Vac VSI is intentionally outside this X1 comparison because it is downstream/common and would not discriminate the R2 front-end mechanisms at this gate.

---

## 3. Matched modern low-voltage MOSFET contract

Use the real A0 main MOS technology as the common LV reference for A0, R2-REF1 and R2-REF2:

```text
TI CSD18542KCS
VDS = 60 V
RDS(on),max @ VGS=10 V = 4 mΩ
Qg,typ = 44 nC
```

Source: TI CSD18542KCS datasheet / product page, Rev. A.

All three paths are normalized to the A0 main-bank structure:

```text
10 MOS in parallel per logical A or C switch
20 main MOS total
```

Hence 25°C ideal-parallel logical resistance proxy:

```text
Rlogical = 4 mΩ / 10 = 0.400 mΩ
```

At the 175.44-A source-current scaling:

```text
Pmain,25C,proxy = Iin² × Rlogical
                 ≈ 12.31 W
```

This is a silicon floor proxy only; hot RDS(on), imbalance, busbar/PCB/contact resistance and AC effects remain open.

Gate-drive energy for the 20 common main MOS devices:

```text
Pgate ≈ N × Qg × Vg × fs
      = 20 × 44 nC × 10 V × 50 kHz
      ≈ 0.44 W
```

TI also provides an unencrypted PSpice model for this device. The same model should be used for later switching-cell comparison rather than assigning different Coss/Qg technology to each topology.

---

## 4. Common battery-interface rule

A0 contains seven parallel CSD18510KCS devices in the B-to-BAT- reverse-polarity/protection interface.

Current TI data:

```text
CSD18510KCS
VDS = 40 V
RDS(on),max @ 10 V = 1.7 mΩ
Qg,typ = 119 nC
```

This interface is held common and excluded from the differential R2 mechanism ranking at this stage.

Reason:

```text
common product protection overhead
!=
commutation-mechanism discriminator
```

If a later candidate removes or changes this product-level function, it must be brought back into the full loss ledger.

---

## 5. Common HV rectifier technology contract

For a modern matched rectifier floor, use a 650-V / 10-A SiC Schottky class rather than Ryan's 1998 diode technology.

Reference example:

```text
Infineon IDW10G65C5
650 V
10 A
VF ≈ 1.5 V product-page value
Qc ≈ 15 nC
```

This is a technology normalization reference, not a final procurement decision.

For a full bridge with two conducting diodes and `I_HV = 5.714 A`:

```text
Prect,base ≈ 2 × VF × I_HV
           ≈ 17.14 W
```

This base forward-drop term is approximately common to the compared full-bridge rectifier paths and therefore does not decide the topology ranking by itself.

What remains topology-dependent is:

```text
rectifier RMS waveform
junction-capacitance commutation
resonant current multiplier
reverse-voltage stress
thermal VF
```

---

## 6. A0 matched loss floor used for crossover

Common modeled terms at the center point:

```text
main MOS conduction proxy ≈ 12.31 W
gate drive proxy          ≈  0.44 W
HV bridge base proxy      ≈ 17.14 W
```

Previous A0 commutation surrogate:

```text
snubber    ≈  2.30 W
overlap    ≈ 21.05 W
dead-time  ≈  1.75 W
-------------------
commutation bucket ≈ 25.10 W
```

Status of `25.10 W`:

```text
MODELLED
NOT MEASURED
```

It is retained only as a crossover budget.

The differential question for R2 references is therefore:

```text
Can the reference remove a material part of ~25.1 W
while adding less than the removed watts elsewhere?
```

---

## 7. R2-REF1 — active-clamp low-voltage burden

At `D = 0.42`, the File-46 first-order duty/RMS proxy gives:

```text
Irms,main ≈ 191.42 A
Pmain,REF1 ≈ 14.66 W
```

Added main-MOS conduction versus A0 proxy:

```text
ΔPmain ≈ +2.35 W
```

Therefore the remaining A0 commutation-saving headroom is:

```text
25.10 - 2.35 = 22.75 W
```

before counting:

```text
Paux,cond
Paux,sw
Pclamp-cap/path
Pextra,circulation
Presidual,sw
```

### 7.1 Auxiliary-current break-even

Define:

```text
beta = Iaux,rms / Iin
```

If one auxiliary device has the same 4-mΩ reference RDS(on):

| beta | Iaux,rms | one 4-mΩ auxiliary conduction | max equivalent Raux allowed by 22.75-W headroom | minimum parallel 4-mΩ devices, conduction-only |
|---:|---:|---:|---:|---:|
| 0.20 | 35.09 A | 4.92 W | 18.48 mΩ | 1 |
| 0.30 | 52.63 A | 11.08 W | 8.21 mΩ | 1 |
| 0.40 | 70.18 A | 19.70 W | 4.62 mΩ | 1 |
| 0.50 | 87.72 A | 30.78 W | 2.96 mΩ | 2 |
| 0.75 | 131.58 A | 69.25 W | 1.31 mΩ | 4 |
| 1.00 | 175.44 A | 123.11 W | 0.739 mΩ | 6 |

Interpretation:

> R2-REF1 is extremely sensitive to how much RMS current the auxiliary/clamp path actually processes in the 12-V domain.

If the auxiliary path approaches full-source-current RMS, a single/few-device implementation cannot remain inside the present commutation-loss headroom even before auxiliary switching and clamp-capacitor losses are counted.

This does not reject R2-REF1. It defines the quantity that PSIM/LTspice must measure: `Iaux,rms`.

---

## 8. R2-REF2 — magnetizing-current burden

R2-REF2 does not require a sustained active-clamp return path. Its primary ZVS mechanism uses magnetizing-current commutation while the LCL network is downstream.

Define a first-order sensitivity:

```text
alpha = Im,rms / Iload,rms
```

and approximate:

```text
Pmain,REF2 ≈ Pmain,A0 × (1 + alpha²)
```

Then:

| alpha | added main-MOS conduction | remaining 25.1-W commutation headroom |
|---:|---:|---:|
| 0.10 | 0.12 W | 24.98 W |
| 0.20 | 0.49 W | 24.61 W |
| 0.30 | 1.11 W | 23.99 W |
| 0.40 | 1.97 W | 23.13 W |
| 0.50 | 3.08 W | 22.02 W |
| 0.75 | 6.93 W | 18.17 W |

This is not a waveform-accurate Ryan loss model. It establishes that a moderate magnetizing-current burden does not automatically consume the full A0 commutation bucket at full load.

The actual transformer copper/core penalty must be added later.

---

## 9. Main structural result — loss-location leverage

The most important result of this file is independent of exact component selection.

For a fixed allowable dissipation:

```text
P = I²R
```

At the 12-V source-current scale:

```text
I_LV = 175.44 A
```

The equivalent resistance that produces 25.1 W is only:

```text
R_LV,25.1W = 25.1 / 175.44²
            ≈ 0.815 mΩ
```

At the 350-V side:

```text
I_HV = 5.714 A
```

If an added resonant network carries approximately the HV load current, the resistance giving the same 25.1-W loss is:

```text
R_HV,25.1W = 25.1 / 5.714²
            ≈ 0.769 Ω
```

That is approximately:

```text
0.769 Ω / 0.815 mΩ ≈ 943×
```

more resistance tolerance for the same watt loss.

### 9.1 Resonant-current multiplier sensitivity

Define:

```text
gamma = I_LCL,rms / I_HV
```

| gamma | I_LCL,rms | HV-side equivalent R causing 25.1 W | resistance tolerance vs 175-A LV path |
|---:|---:|---:|---:|
| 1.00 | 5.71 A | 0.769 Ω | 943× |
| 1.25 | 7.14 A | 0.492 Ω | 603× |
| 1.50 | 8.57 A | 0.342 Ω | 419× |
| 2.00 | 11.43 A | 0.192 Ω | 236× |
| 2.50 | 14.29 A | 0.123 Ω | 151× |
| 3.00 | 17.14 A | 0.0854 Ω | 105× |

Even if the LCL RMS current reaches `2×` the ideal HV output current, the same-watt resistance tolerance remains about `236×` larger than a 175-A low-voltage path.

This does **not** prove the LCL solution has low loss. Core loss, capacitor ESR, AC resistance and circulating reactive power still matter.

It does establish a strong topology-level structural advantage:

```text
putting added PM-4 passive processing after X1
is much less I²R-sensitive
than adding another substantial current path before X1.
```

---

## 10. Modern 350-V / 50-kHz R2-REF2 LCL similarity seed

Ryan reference approximately used:

```text
fs ≈ 25 kHz
fr ≈ 50 kHz
Lext ≈ 27 µH
Lleak/model term ≈ 18 µH
C ≈ 1 µF
Vout ≈ 235 V
Pout ≈ 1.8 kW
```

File 46 first scaled impedance from Ryan's load to the 350-V / 2-kW load.

For a matched modern switching-frequency center point:

```text
fs,target = 50 kHz
fr,target ≈ 100 kHz
```

Preserving the same normalized impedance and `fr/fs` ratio introduces an additional `25k/50k = 0.5` frequency scaling.

The resulting **similarity seed only** is:

```text
Lext ≈ 26.95 µH
Lleak-equivalent ≈ 17.97 µH
C ≈ 0.250 µF
```

These are not component prescriptions and must not be interpreted as a transformer leakage design requirement.

They are the starting values for an ideal P0 network sweep.

---

## 11. Matched crossover equations

### A0

Use the current surrogate only as reference:

```text
P_A0,diff ≈ Pcomm,A0 ≈ 25.1 W
```

### R2-REF1

At the D=0.42 center point:

```text
P_REF1,added
= 2.35 W main-RMS penalty
+ Paux,cond
+ Paux,sw
+ Pclamp
+ Pcirc
+ Presidual,sw
```

R2-REF1 theoretically beats the current A0 commutation surrogate only if:

```text
Paux,cond + Paux,sw + Pclamp + Pcirc + Presidual,sw
< 22.75 W
```

### R2-REF2

```text
P_REF2,added
= ΔPmag/main
+ ΔPtransformer,Cu
+ ΔPtransformer,core
+ PLCL,L
+ PLCL,C
+ ΔPrectifier,RMS
+ Presidual,sw
```

R2-REF2 theoretically beats the current A0 commutation surrogate only if:

```text
P_REF2,added < 25.1 W
```

At `alpha=0.2`, for example, the main-MOS magnetizing-current penalty proxy is only ~0.49 W, leaving ~24.61 W for all remaining added terms.

---

## 12. Current ranking after modern technology normalization

### A0

```text
status = physical benchmark
main LV conduction = low because of heavy MOS parallelization
commutation bucket = modeled material weakness
```

### R2-REF1

```text
status = viable known comparator
primary risk = added auxiliary RMS in the 12-V domain
critical observable = Iaux,rms
```

### R2-REF2

```text
status = strongest R2 comparator
primary advantage = no sustained active auxiliary low-voltage return path
added resonant hardware is mainly downstream of X1
critical observables = Im,rms, I_LCL,rms, LCL ESR/copper/core, rectifier RMS
```

Current theoretical preference for the **next simulation allocation**:

```text
R2-REF2 first
R2-REF1 second
A0 matched model as control
```

This is a simulation-priority decision, not a topology-optimality claim.

---

## 13. Falsification conditions for R2-REF2

R2-REF2 should be downgraded if the matched model shows any of the following:

```text
1. required Im,rms creates large primary/transformer copper burden;
2. LCL resonant current multiplier gamma is large enough that L/C loss exceeds the saved commutation watts;
3. the required secondary leakage/resonant construction causes unacceptable transformer AC loss or voltage stress;
4. rectifier RMS/commutation losses rise materially above the matched SiC bridge baseline;
5. total added REF2 watts >= A0 commutation watts removed;
6. the same result can be obtained more simply by A0 tuning without the LCL network.
```

The required robust condition remains:

```text
P_saved,low - P_added,high > 0
```

---

## 14. Next simulation contract

Do not yet build the final 220-Vac inverter.

Build three matched X1-to-HV-link P0/P1 models:

```text
A0-control
R2-REF1-active-clamp
R2-REF2-LCL-ZVS
```

Common:

```text
Vin = 12 V
Pout = 2 kW
HV link = 350 V
fs = 50 kHz
same CSD18542KCS main-switch model
same 650-V SiC rectifier technology class
same source/interconnect assumptions
same transformer copper/core accounting method
```

R2-REF2 initial ideal seed:

```text
fr ≈ 100 kHz
Lext ≈ 26.95 µH
Lleak-equivalent ≈ 17.97 µH
C ≈ 0.250 µF
```

Required exported observables:

```text
Iin,rms
I_A,rms / I_C,rms
Im,rms
VDS turn-on of main MOS
I_LCL,rms
LCL reactive power
rectifier Irms
transformer primary/secondary Irms
commutation energy per event
HV-link ripple
```

Required loss ledger:

```text
PmainMOS_cond
PmainMOS_sw
Pgate
Ptransformer_Cu
Ptransformer_core
Prectifier
PLCL_inductor_Cu
PLCL_inductor_core
PLCL_cap_ESR
Psnubber/clamp
Pcirculation
Pother
```

---

## 15. Formal conclusion

The modern matched screen does not establish a new topology.

It establishes a stronger physical selection result:

> At the 12-V / 2-kW boundary, a soft-switching strategy that introduces substantial additional RMS current before X1 is severely constrained by sub-milliohm loss budgets. A known Ryan-type route is structurally attractive because its added resonant passive network is processed largely after X1 in a much lower-current domain, while primary ZVS is obtained without a sustained active-clamp return path.

This makes `R2-REF2` the first R2 path that deserves matched simulation before any further R2 candidate generation.

Formal status:

```text
R2-REF2 simulation priority = FIRST
R2-REF1 simulation priority = SECOND
A0 = CONTROL
R2 new topology generation = PAUSED
Candidate #10 = HOLD
Novelty = NOT_ESTABLISHED
```
