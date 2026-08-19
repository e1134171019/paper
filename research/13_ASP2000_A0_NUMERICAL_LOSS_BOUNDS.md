# 13 — ASP-2000 A0 Numerical Loss Bounds

Status date: 2026-08-19  
Role: `A0 NUMERICAL-BOUND / LOSS-LOCALIZATION SUPPORT`  
Evidence status: `PCB STACK + COMPILED PCB NETS + OFFICIAL DEVICE DATA + PARAMETRIC MODELS`  
Measurement status: `NOT HARDWARE-MEASURED`  
Novelty relevance: `NONE — benchmark only`

## 1. Purpose

This document converts the reconstructed ASP-2000 R52 A0 low-voltage path into numerical bounds without pretending that unmeasured quantities are known.

Evidence classes:

```text
VERIFIED
= directly extracted from SchDoc/PcbDoc or official device data

GEOMETRY_BOUND
= numerical result from reconstructed nominal PCB copper geometry

DATASHEET_BOUND
= device loss scale using official device data

PARAMETRIC
= sensitivity equation versus unknown operating quantity

MEASUREMENT_NEEDED
= no defensible hardware scalar yet
```

---

## 2. PCB copper stack boundary

PcbDoc stack:

```text
Top copper     = 1.4 mil ≈ 35.56 um
FR-4 dielectric
Bottom copper  = 1.4 mil ≈ 35.56 um
```

Using nominal room-temperature copper resistivity:

```text
R_sheet,1layer ≈ 0.485 mOhm/square
```

Ideal equal Top+Bottom parallel geometry:

```text
R_sheet,2layer,ideal ≈ 0.242 mOhm/square
```

This is not the actual BAT+ path resistance because current spreading, polygons, vias, contacts, solder reinforcement and assembly conductors matter.

---

## 3. Full-current copper scaling at 12 V / 2 kW

Anchor:

```text
Iin,ideal = 166.7 A
Iin@95% scaling ≈ 175.4 A
```

At 175.4 A:

```text
1 single-layer square ≈ 14.9 W
ideal Top+Bottom effective square ≈ 7.46 W
```

After ideal 50/50 split into T1/T2 feeds:

```text
I_feed ≈ 87.7 A
single-layer ≈ 3.73 W/square
ideal Top+Bottom ≈ 1.87 W/square
```

After ideal four-fuse split within one feed:

```text
I_fuse ≈ 21.9 A
single-layer ≈ 0.233 W/square
ideal Top+Bottom ≈ 0.117 W/square
```

Research implication:

> Loss is most expensive before the current is physically/electrically distributed. The value of fan-out depends on how quickly the full-current common exposure is terminated.

---

## 4. Positive distribution geometry bounds

Direct PCB primitive reconstruction identified:

```text
3 large BAT+ power pads
8 main fuse-input pads
16 BAT+ stitching vias
major Top/Bottom BAT+ polygons
```

A converged nominal-copper 2D sheet model gave:

```text
R_BAT+,common,geometry ≈ 0.249 mOhm
P @ 175.4 A ≈ 7.67 W
average modeled drop ≈ 43.7 mV
```

Post-fuse local PCB geometry models:

```text
T1 local PCB:
R ≈ 0.351 mOhm
P @ 87.7 A ideal share ≈ 2.70 W

T2 PCB excluding J8:
R ≈ 0.144 mOhm
P @ 87.7 A ideal share ≈ 1.10 W
```

Under ideal 50/50 T1/T2 sharing, partial positive PCB-only equivalent:

```text
R_eq,positive-PCB,partial ≈ 0.373 mOhm
P @ 175.4 A ≈ 11.5 W
```

This excludes connector/contact, fuse elements, J8 external link, hot-copper rise and assembly reinforcement.

Status:

```text
GEOMETRY_BOUND / NOT MEASURED
```

---

## 5. Main low-side MOS connectivity — corrected

Compiled PCB resolves the previous Q19 ambiguity.

### A logical switch

```text
Q3 Q4 Q5 Q6 Q33
Q18 Q19 Q20 Q21 Q37
```

All ten drains:

```text
→ NetC62_1
```

All ten sources:

```text
→ B
```

### C logical switch

```text
Q11 Q12 Q13 Q14 Q36
Q24 Q25 Q26 Q27 Q38
```

All ten drains:

```text
→ NetC65_1
```

All ten sources:

```text
→ B
```

Formal correction:

```text
A-side connected count = 10
C-side connected count = 10
Q19 drain connectivity = VERIFIED IN PCB
```

The previous 9+10 model is superseded.

---

## 6. Updated 12 V main-MOS conduction bound

12 V population:

```text
CSD18542KCS
VDS = 60 V
RDS(on),max @ VGS=10 V = 4 mOhm
Qg,typ = 44 nC
```

With ten devices per logical switch:

```text
R_A,eq,25C,max ≈ 4/10 = 0.400 mOhm
R_C,eq,25C,max ≈ 4/10 = 0.400 mOhm
```

Using the same simplified alternating 50%-per-side sensitivity model and 175.4 A current scale:

```text
P_mainMOS,cond
≈ 0.5 I^2 (R_A + R_C)
≈ 12.3 W
```

Status:

```text
DATASHEET_BOUND / NOT MEASURED
```

This is not a real product loss value. It excludes:

```text
hot RDS(on)
actual primary-current waveform
magnetizing/ripple current
subgroup mismatch
package/contact/copper resistance
dead time
Coss / commutation
switching overlap
```

---

## 7. Hot-RDS(on) sensitivity

Define only as a planning parameter:

```text
kT = RDS(on,hot) / RDS(on,25C)
```

Using the corrected 12.3 W bound:

```text
kT = 1.0 → ~12.3 W
kT = 1.5 → ~18.5 W
kT = 1.8 → ~22.1 W
kT = 2.0 → ~24.6 W
```

These are sensitivity scenarios, not datasheet claims about actual ASP junction temperature.

---

## 8. Gate-drive energy bound

Twenty annotated/connected 12 V main MOS devices:

```text
N = 20
Qg,typ = 44 nC
```

First-order gate-charge energy:

```text
P_gate ≈ N Qg VGS fs
```

At `VGS = 10 V`:

```text
P_gate ≈ 8.8e-6 × fs  [W, fs in Hz]
```

Examples:

```text
20 kHz  → ~0.176 W
50 kHz  → ~0.440 W
100 kHz → ~0.880 W
```

This excludes driver quiescent loss, Miller/overlap, Coss/Eoss, ringing and commutation.

Gate-charge energy alone is therefore unlikely to be the dominant tens-of-watts BAT→X1 term; total switching loss remains open.

---

## 9. Four drivers / two logical switching functions

Physical driver groups:

```text
DA1 + DA2 → A power node
DB1 + DB2 → C power node
```

Control trace:

```text
DR-A  ─ R213 = 0 ohm ─ DR-A2
DR-B  ─ R212 = 0 ohm ─ DR-B2
```

Therefore first-order switching-loss closure should target:

```text
A electrical switch region
C electrical switch region
```

not four fictitious independent converter branches.

The four physical drivers still must be compared dynamically for propagation/gate mismatch.

---

## 10. Negative-side full-current MOS bound

Verified physical region:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

Device annotation:

```text
CSD18510KCS
RDS(on),max @ VGS=10 V = 1.7 mOhm
```

Seven ideal parallel devices:

```text
R_eq,25C,max ≈ 1.7/7 ≈ 0.243 mOhm
```

At 175.4 A continuous-enhancement scaling:

```text
P ≈ 7.47 W
```

Status:

```text
DATASHEET_BOUND / NOT MEASURED
```

Preferred hardware closure is direct:

```text
P_negativeBank = I_source × ΔV(B↔BAT-)
```

with temperature recorded.

---

## 11. Switching loss remains OPEN

No defensible hardware switching-frequency scalar is yet measured.

Required:

```text
fs / duty / dead time
V_A-B(t)
V_C-B(t)
I_A,total(t)
I_C,total(t)
commutation / clamp behavior
channel deskew
```

System-level electrical boundary:

```text
p_A(t) = v_A-B(t) i_A,total(t)
p_C(t) = v_C-B(t) i_C,total(t)

P_switchRegion = average[p_A + p_C]
```

During stable conduction, transformer center-tap currents may support:

```text
i_A,total ≈ i_T1,A + i_T2,A

i_C,total ≈ i_T1,C + i_T2,C
```

During switching transitions/dead time, displacement/body-diode/leakage currents require synchronized high-bandwidth evidence.

---

## 12. Fuse and J8 losses remain hardware-measurement items

Fuse architecture:

```text
2 × 4 main fuses
```

No manufacturer resistance is locked strongly enough for benchmark loss.

Use:

```text
P_fuse = Σ I_fuse × ΔV_fuse
```

T2 contains a separate J8 high-current link boundary whose conductor/contact resistance remains open.

Use:

```text
P_J8 = I_T2 × ΔV_J8
```

---

## 13. Transformer loss remains OPEN

Known:

```text
2 × PQ5050
center-tapped primaries
shared A/C switched nodes
series/collective secondary formation
```

Still required:

```text
turns
conductor geometry
Rdc / Rac
core material
Ae / Ve
fs
volt-second / ΔB
primary/secondary RMS currents
temperature
```

Therefore:

```text
P_primary,Cu = OPEN
P_core       = OPEN
```

Do not infer magnetic loss from core size alone.

---

## 14. Current numerical picture

Current non-measured scales:

```text
BAT+ common PCB geometry model       ≈ 7.7 W
partial positive PCB geometry model  ≈ 11.5 W total
main 20-MOS conduction bound         ≈ 12.3 W @ 25C/max-RDS simplified model
negative 7-MOS bank bound            ≈ 7.5 W @ 25C/max-RDS simplified model
ideal gate-charge energy             < 1 W over 20–100 kHz example range
```

These numbers must **not** be summed into a claimed ASP measured total because they use different boundaries and evidence classes and omit several terms.

---

## 15. Measurement priority

```text
Priority 1 = actual positive distribution / fuse / J8 mV loss
Priority 2 = B↔BAT- seven-MOS bank mV loss
Priority 3 = A/C logical switch timing and hot conduction/switching
Priority 4 = T1/T2 current and primary copper/core
Priority 5 = source 100/120 Hz / HF ripple partition
```

The corrected finding remains:

> At 12 V / 2 kW, ordinary current-distribution resistance and heavily paralleled silicon are both first-order loss buckets. Neither can be treated as a minor layout detail.

---

## 16. Formal status

```text
Q19 anomaly                     = RESOLVED
A-side MOS count                = 10
C-side MOS count                = 10
main-MOS 25C bound              ≈ 12.3 W
positive PCB geometry bound     = ESTABLISHED / NOT MEASURED
negative series bank bound      = ESTABLISHED / NOT MEASURED
main switching loss             = OPEN
transformer loss                = OPEN
A0 dominant loss bucket         = NOT ESTABLISHED
candidate advantage             = NOT ESTABLISHED
novelty                         = NOT ESTABLISHED
```
