# 48 — R2-REF2 Reduced-Order Surrogate Simulation v1

Status date: 2026-08-20  
Role: `R2-REF2 REDUCED-ORDER SURROGATE / PRE-PSIM PHYSICS SCREEN`  
Boundary: `12 Vdc / 2 kW / 350 Vdc HV-link / fs = 50 kHz`  
Evidence class: `PUBLISHED PRIOR-ART TOPOLOGY CONTEXT + PROJECT-MATCHED REDUCED-ORDER PYTHON MODEL`  
PSIM: `NOT EXECUTED`  
LTspice: `NOT EXECUTED`  
Hardware: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

This file executes the first numerical surrogate requested after File 47.

It does **not** claim a complete Ryan-1998 switching simulation. The exact four-mode rectifier/tank equations and nonlinear semiconductor models are not yet implemented. Instead, two reduced-order submodels are executed to test whether R2-REF2 has an immediate physical dead-end before spending PSIM/LTspice effort:

1. primary magnetizing-current-assisted MOS-bank commutation;
2. LCL natural-mode / loss-crossover behavior around the matched 350-V operating point.

Ryan et al. 1998 remains prior art and comparator only.

---

## 2. Published prior-art anchors retained

Ryan et al., IEEE Transactions on Industry Applications, 1998, DOI `10.1109/28.720458`, reports an LCL-resonant push-pull converter in which:

```text
primary switches operate with ZVS
via transformer magnetizing-current commutation
+
MOSFET drain-source capacitance
```

and the secondary-side LCL network uses transformer leakage plus an added resonant capacitor/inductor. Published reference context includes approximately:

```text
Vin = 12 V
Iin ≈ 160 A
Vout ≈ 235 V
Pout ≈ 1.8 kW
fs ≈ 25 kHz
LCL resonance ≈ 50 kHz
transformer leakage term ≈ 18 µH
external resonant L ≈ 27 µH
resonant C ≈ 1 µF
```

The paper explicitly notes that switching is most efficient when it occurs near a minimum of the transformer-current oscillation, reducing trapped primary-leakage energy.

---

## 3. Matched project seed

From File 47, the modern matched boundary is:

```text
Vin = 12 V
Pout = 2 kW
Vdc = 350 V
fs = 50 kHz
Iin @95% reference = 175.44 A
I_HV = 5.714 A
```

Matched low-voltage silicon proxy:

```text
10 × CSD18542KCS per logical main switch bank
Rlogical,25C,max proxy ≈ 0.400 mΩ
```

A0 modelled commutation-loss discriminator retained only for break-even screening:

```text
Pcomm,A0,surrogate ≈ 25.10 W
```

Status of the 25.10-W value remains:

```text
MODELLED / NOT MEASURED
```

---

## 4. Reduced primary commutation model

For one push-pull transition, use two equal logical-switch-bank output-capacitance proxies:

```text
A bank node: 0 → 2Vin
C bank node: 2Vin → 0
```

With a first-order constant commutating current `Icomm`, each bank capacitance `Cbank` is charged/discharged with:

```text
tcomm ≈ (2 Vin) Cbank / Icomm
```

This is a charge-transfer timing model, not a nonlinear Eoss semiconductor model.

Center numerical example:

```text
Vin = 12 V
2Vin = 24 V
Cbank = 50 nF per logical bank
Icomm = 20 A
```

therefore:

```text
tcomm ≈ 24 × 50 nF / 20 A
      ≈ 60 ns
```

Interpretation:

```text
If the incoming main MOS bank is gated after its node has fallen to ~0 V,
a ~20-A commutating-current scale is sufficient to complete the idealized
50-nF-bank transition within ~60 ns.
```

This is not yet proof of robust ZVS because real Coss is nonlinear and the actual magnetizing/leakage current trajectory is not constant.

---

## 5. Primary ZVS timing sweep

The required idealized commutating current is:

```text
Icomm,min = 2 Vin Cbank / tdead
```

Examples:

| Cbank per logical bank | dead time | required Icomm |
|---:|---:|---:|
| 25 nF | 40 ns | 15 A |
| 25 nF | 80 ns | 7.5 A |
| 50 nF | 40 ns | 30 A |
| 50 nF | 60 ns | 20 A |
| 50 nF | 80 ns | 15 A |
| 100 nF | 60 ns | 40 A |
| 100 nF | 120 ns | 20 A |

For a rough triangular magnetizing-current waveform with `Im,rms ≈ Ipk/sqrt(3)`, even the 20-A peak example corresponds to only about 11.5 A RMS. Against a 0.400-mΩ logical-switch resistance, the additional MOS conduction term is small relative to the present 25.1-W commutation discriminator.

This supports, but does not prove, the File-47 hypothesis that REF2 can obtain useful commutation current without requiring a sustained hundred-ampere auxiliary path.

---

## 6. LCL natural-mode surrogate

The File-47 matched similarity seed at 350 V / 50 kHz is:

```text
Lleak,eq ≈ 17.97 µH
Lext      ≈ 26.95 µH
Cres      ≈ 0.250 µF
```

For the L-C-L natural mode:

```text
ω0² = (Lleak + Lext) / (Lleak Lext Cres)
```

therefore:

```text
f0 ≈ 96.94 kHz
f0 / fs ≈ 1.94
```

This is close to the Ryan design pattern in which the resonant frequency is about twice the switching frequency.

A reduced small-signal natural-ring simulation around the DC operating point was executed with a 20-V capacitor perturbation. It produced the expected ~97-kHz oscillation between the leakage branch, resonant capacitor, and external inductor.

This confirms that the File-47 scaled seed preserves the intended normalized LCL resonance. It does **not** reproduce the complete four rectifier modes, diode commutation, output regulation, or transformer-current waveform of Ryan's converter.

---

## 7. Loss-crossover model

Define:

```text
α = Im,rms / Iin
γ = I_LCL,rms / I_HV
R_LCL,eq = total equivalent dissipative series resistance
           of the added resonant path at the matched operating point
```

Reduced added loss is screened as:

```text
Padded,REF2
≈ (α Iin)² Rlogical
 + (γ I_HV)² R_LCL,eq
```

Break-even against the current A0 commutation surrogate requires:

```text
Padded,REF2 < 25.10 W
```

or:

```text
R_LCL,eq,max
=
[25.10 - (α Iin)²Rlogical]
/
(γ I_HV)²
```

Representative limits:

```text
If γ = 1.0:
R_LCL,eq,max ≈ 0.7–0.8 Ω over the tested α range.

If γ = 2.0:
R_LCL,eq,max ≈ 0.17–0.19 Ω.

If γ = 3.0:
R_LCL,eq,max ≈ 0.075–0.085 Ω.
```

Thus the decisive REF2 unknown is not merely whether an LCL exists, but how much RMS resonant current it creates.

---

## 8. Center-case numerical screen

One deliberately moderate, non-authoritative point was evaluated:

```text
α = 0.15
Im,rms ≈ 26.3 A
γ = 2.0
I_LCL,rms ≈ 11.43 A
R_LCL,eq = 0.10 Ω
```

Result:

```text
Pmag-added ≈ 0.28 W
PLCL-added ≈ 13.06 W
Padded,total ≈ 13.34 W
```

Against:

```text
Pcomm,A0,surrogate = 25.10 W
```

remaining theoretical headroom is:

```text
25.10 - 13.34
≈ 11.76 W
```

Formal reduced-order result:

```text
CENTER SURROGATE = PASS
```

Meaning only:

```text
The reduced model does not expose an immediate loss contradiction.
```

It does **not** mean:

```text
R2-REF2 efficiency is proven
Ryan is optimal
PSIM has passed
hardware is validated
```

---

## 9. What would make REF2 fail

The reduced crossover becomes unfavorable if one or more of the following is large:

```text
I_LCL,rms / I_HV substantially above ~2–3×
LCL inductor copper/core loss
resonant capacitor ESR/dielectric loss
transformer AC copper/leakage loss
primary-leakage avalanche loss
nonlinear Coss commutation deficit
rectifier RMS/reverse-recovery loss
hot RDS(on) / current-sharing degradation
```

The Ryan paper itself emphasizes that excessive resonance depth raises conduction loss and that frequency tuning is important because primary-leakage avalanche loss changes strongly with switch-current at commutation.

---

## 10. Decision after first surrogate

Current result:

```text
R2-REF2 reduced primary commutation = PLAUSIBLE
R2-REF2 scaled LCL resonance         = PLAUSIBLE
R2-REF2 center loss crossover       = PASS_AT_SCREEN_POINT
FULL SWITCHED CONVERTER             = NOT YET SIMULATED
```

Therefore REF2 is **not rejected** at this stage.

The next authorized modeling layer should implement the actual four-mode Ryan rectifier/LCL state machine or an equivalent switched-circuit model, then replace:

```text
constant Icomm
linear Cbank
lumped R_LCL,eq
```

with:

```text
nonlinear MOS Coss/Eoss
actual magnetizing-current waveform
actual rectifier conduction intervals
actual LCL RMS current
primary-leakage avalanche term
```

Only after that should a PSIM/LTspice total-loss comparison against A0 be treated as meaningful.

---

## 11. Formal status

```text
R2-REF2 PRIOR ART ROLE             = RETAINED COMPARATOR
REDUCED-ORDER SURROGATE            = EXECUTED
CENTER SCREEN                      = PASS
PSIM                               = NOT EXECUTED
LTSPICE                            = NOT EXECUTED
HARDWARE                           = NOT EXECUTED
TOPOLOGY NOVELTY                   = NOT CLAIMED
CANDIDATE #10                      = HOLD
```
