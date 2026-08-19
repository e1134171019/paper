# 13 — ASP-2000 A0 Numerical Loss Bounds

Status date: 2026-08-19  
Role: `A0 NUMERICAL-BOUND / LOSS-LOCALIZATION SUPPORT`  
Evidence status: `R52 PCB MANUFACTURING SPEC + COMPILED PCB NETS + OFFICIAL DEVICE DATA + PARAMETRIC MODELS`  
Measurement status: `NOT HARDWARE-MEASURED`  
Novelty relevance: `NONE — benchmark only`

## 1. Purpose

This document converts the reconstructed ASP-2000 R52 A0 low-voltage path into numerical bounds without pretending that unmeasured quantities are known.

Evidence classes:

```text
VERIFIED
= directly extracted from product files / manufacturing documents or official device data

MANUFACTURING_GEOMETRY_BOUND
= PCB geometry model rescaled to the specified manufactured copper thickness

DATASHEET_BOUND
= device loss scale using official device data

PARAMETRIC
= sensitivity equation versus unknown operating quantity

MEASUREMENT_NEEDED
= no defensible hardware scalar yet
```

---

## 2. PCB copper-thickness correction — MANUFACTURING SPEC SUPERSEDES PcbDoc STACK METADATA

Earlier work used the PcbDoc stack metadata:

```text
Top copper ≈ 1.4 mil ≈ 35.56 µm
Bottom copper ≈ 1.4 mil ≈ 35.56 µm
```

That value is no longer the authoritative as-manufactured thickness for A0.

The R52 manufacturing specification tied to:

```text
PB-2200-0038-D_R52.RAR
```

explicitly requires:

```text
FR4
1.6 mm
2-layer PCB
base copper = 2.0 oz
finished copper thickness > 82 µm
```

Formal evidence decision:

```text
PcbDoc 35.56 µm stack value
= DESIGN_METADATA / SUPERSEDED_FOR_AS-BUILT_RESISTANCE_BOUND

R52 finished copper >82 µm
= AUTHORITATIVE MANUFACTURING MINIMUM FOR CURRENT GEOMETRY BOUND
```

Using room-temperature copper resistivity and `t = 82 µm` as the conservative minimum thickness:

```text
R_sheet,1layer,max ≈ 0.210 mΩ/square
R_sheet,2layer,ideal,max ≈ 0.105 mΩ/square
```

Because the specification says `>82 µm`, actual copper-only sheet resistance may be lower. Contacts, current crowding, vias, solder, joints and temperature remain separate effects.

---

## 3. Full-current copper scaling at 12 V / 2 kW — CORRECTED

Anchor:

```text
Iin,ideal = 166.7 A
Iin@95% scaling ≈ 175.4 A
```

At the 82 µm minimum-copper bound:

```text
1 single-layer square @175.4 A ≤ ~6.47 W
ideal Top+Bottom effective square ≤ ~3.23 W
```

After ideal 50/50 split into T1/T2 feeds (`~87.7 A`):

```text
single-layer square ≤ ~1.62 W
ideal Top+Bottom effective square ≤ ~0.81 W
```

After ideal four-fuse split within one feed (`~21.9 A`):

```text
single-layer square ≤ ~0.101 W
ideal Top+Bottom effective square ≤ ~0.050 W
```

Research implication remains qualitative but is weaker than the old 35.56 µm model:

> Common full-current copper is still worth minimizing, but the R52 manufacturing build uses much heavier copper than the PcbDoc metadata suggested. It is no longer defensible to claim that BAT+ PCB copper is automatically comparable to the entire main-MOS conduction bucket.

---

## 4. Positive-distribution geometry bounds — CORRECTED TO ≥82 µm FINISHED COPPER

Direct PCB primitive reconstruction identified:

```text
3 large BAT+ power pads
8 main fuse-input pads
16 BAT+ stitching vias
major Top/Bottom BAT+ polygons
```

The former 35.56 µm model values are superseded.

Because resistance scales approximately inversely with copper thickness for the same 2D geometry, rescaling the existing geometry solution from `35.56 µm` to the conservative `82 µm` minimum gives:

```text
BAT+ common:
R_BAT+,common,geometry ≤ ~0.108 mΩ
P @175.4 A ≤ ~3.32 W
average modeled drop ≤ ~18.9 mV

T1 local PCB:
R_T1local,PCB ≤ ~0.152 mΩ
P @87.7 A ideal share ≤ ~1.17 W

T2 PCB excluding J8:
R_T2local,PCB ≤ ~0.0624 mΩ
P @87.7 A ideal share ≤ ~0.48 W
```

Under ideal 50/50 T1/T2 sharing, the partial positive PCB-only input-referred equivalent becomes:

```text
R_eq,positive-PCB,partial ≤ ~0.162 mΩ
P @175.4 A ≤ ~4.98 W
```

This still excludes:

```text
BAT+ connector/contact
fuse elements and fuse contacts
J8 external link/contact
hot-copper rise
assembly-specific reinforcement / solder / bus conductors
```

Status:

```text
MANUFACTURING_GEOMETRY_BOUND / NOT MEASURED
```

These are conservative geometry-only values using the specified minimum finished copper thickness, not measured board resistance.

---

## 5. Main low-side MOS connectivity — RESOLVED

Compiled PCB establishes:

```text
A logical switch = 10 connected MOS → common source B
C logical switch = 10 connected MOS → common source B
Q19 drain connectivity = VERIFIED IN PCB
```

The old 9+10 model is superseded.

---

## 6. 12 V main-MOS conduction bound

12 V population:

```text
CSD18542KCS
RDS(on),max @ VGS=10 V = 4 mΩ
Qg,typ = 44 nC
```

Ten devices per logical switch:

```text
R_A,eq,25C,max ≈ 0.400 mΩ
R_C,eq,25C,max ≈ 0.400 mΩ
```

Using the simplified alternating 50%-per-side sensitivity model and 175.4 A scale:

```text
P_mainMOS,cond,25C-bound ≈ 12.3 W
```

Status:

```text
DATASHEET_BOUND / NOT MEASURED
```

It excludes hot `RDS(on)`, real primary current waveform, mismatch, package/interconnect, dead time, Coss, commutation and switching overlap.

Hot-resistance sensitivity:

```text
kT = 1.0 → ~12.3 W
kT = 1.5 → ~18.5 W
kT = 1.8 → ~22.1 W
kT = 2.0 → ~24.6 W
```

These are sensitivity cases, not measured ASP losses.

---

## 7. Gate-drive energy bound

For 20 connected main MOS:

```text
P_gate ≈ N Qg VGS fs
≈ 8.8e-6 × fs  [W, fs in Hz, VGS=10 V]
```

Examples:

```text
20 kHz  → ~0.176 W
50 kHz  → ~0.440 W
100 kHz → ~0.880 W
```

Gate-charge energy alone is not the total switching loss.

---

## 8. Negative-side battery-interface MOS bound

Verified region:

```text
B
↓
7 × CSD18510KCS in parallel
↓
BAT-
```

Device max `RDS(on)=1.7 mΩ @ VGS=10 V` gives:

```text
R_eq,25C,max ≈ 0.243 mΩ
P @175.4 A ≈ 7.47 W
```

Status:

```text
DATASHEET_BOUND / NOT MEASURED
```

Preferred closure:

```text
P_negativeBank = I_source × ΔV(B↔BAT-)
```

with temperature and 12VP recorded.

---

## 9. Switching and transformer loss remain OPEN

Main switching requires synchronized:

```text
fs / duty / dead time
V_A-B(t), V_C-B(t)
I_A,total(t), I_C,total(t)
commutation/clamp behavior
deskew
```

Transformer numerical loss remains open because the current R52 evidence does not identify the populated transformer P/N, turns ratio, A0 Lm/Lk, winding DCR/Rac or core material.

The separate `M1-PQ50-V121-A` Drive test data belongs to another product variant and is `CONTEXT_ONLY`, not A0 input data.

---

## 10. Fuse / J8 / relay-contact items remain measurement gates

```text
P_fuse = Σ I_fuse × ΔV_fuse
P_J8   = I_T2 × ΔV_J8
P_RL1,steady = I_secondary × ΔV_RL1
```

RL1 is now classified as the HV precharge/soft-start bypass; R40/R41 startup dissipation is not ordinary steady-state X1 loss.

---

## 11. Corrected numerical picture

Current non-measured scales:

```text
BAT+ common PCB manufacturing-geometry bound    ≤ ~3.32 W
partial positive PCB manufacturing-geometry      ≤ ~4.98 W
main 20-MOS conduction datasheet bound           ≈ 12.3 W @25C simplified
negative 7-MOS battery-interface bound            ≈ 7.47 W @25C simplified
ideal gate-charge energy                          < 1 W over 20–100 kHz examples
```

Do not sum them into a claimed product total because evidence classes and boundaries differ.

Critical correction:

```text
OLD:
BAT+ common PCB ≈7.7 W
partial positive PCB ≈11.5 W
based on 35.56 µm PcbDoc stack metadata

CURRENT:
BAT+ common PCB ≤~3.32 W
partial positive PCB ≤~4.98 W
based on R52 manufactured copper ≥82 µm
```

Therefore the earlier statement that common PCB copper and the entire main-MOS conduction bucket are approximately equal is superseded.

---

## 12. Measurement priority

```text
Priority 1 = actual positive distribution / fuse / J8 mV loss
Priority 2 = B↔BAT- battery-interface mV loss
Priority 3 = A/C logical switch timing + hot conduction/switching
Priority 4 = T1/T2 current + correct-transformer magnetic parameters
Priority 5 = source 100/120 Hz / HF ripple partition
```

The heavy-copper correction reduces the expected PCB-only contribution, but it does not remove the need to measure contacts, fuses, J8 and hot current distribution.

---

## 13. Formal status

```text
R52 base copper                         = 2.0 oz / VERIFIED_FROM_MANUFACTURING_SPEC
R52 finished copper                    = >82 µm / VERIFIED_FROM_MANUFACTURING_SPEC
PcbDoc 35.56 µm as-built assumption    = SUPERSEDED
BAT+ common geometry bound             ≤~0.108 mΩ / ≤~3.32 W
partial positive PCB geometry bound    ≤~0.162 mΩ / ≤~4.98 W
main-MOS 25C conduction bound          ≈12.3 W / NOT_MEASURED
battery-interface 25C bound            ≈7.47 W / NOT_MEASURED
main switching loss                    = OPEN
A0 transformer numerical loss          = OPEN
A0 dominant loss bucket                = NOT_ESTABLISHED
candidate advantage                    = NOT_ESTABLISHED
novelty                                = NOT_ESTABLISHED
```
