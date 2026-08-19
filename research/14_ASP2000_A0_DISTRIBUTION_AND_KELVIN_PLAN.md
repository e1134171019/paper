# 14 — ASP-2000 A0 Distribution Resistance and Kelvin Measurement Gate

Status date: 2026-08-19  
Role: `A0 DISTRIBUTION-LOSS / MEASUREMENT GATE`  
Evidence status: `PCB PRIMITIVE RECONSTRUCTION + R52 MANUFACTURING SPEC + 2D SHEET MODEL + DEVICE/FUNCTION TRACE`  
Measurement status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark only`

## 1. Purpose

Quantify/bound the real high-current distribution and return losses surrounding ASP-2000 A0 before assigning loss to the magnetic X1 mechanism.

Key distinction:

```text
ordinary distribution / protection / sensing loss
!=
intrinsic X1 conversion loss
```

---

## 2. BAT+ distribution geometry — VERIFIED

PcbDoc identifies:

```text
3 large BAT+ connector pads
8 main fuse-input pads
16 BAT+ stitching vias
large Top/Bottom BAT+ polygons
```

Fuse grouping:

```text
T1: F2 F3 F5 F6
T2: F7 F8 F9 F10
```

### Copper-thickness evidence correction

Earlier geometry work used PcbDoc stack metadata:

```text
Top/Bottom ≈ 1.4 mil ≈35.56 µm
```

The R52 manufacturing specification tied to `PB-2200-0038-D_R52.RAR` explicitly requires:

```text
2-layer FR4
base copper = 2.0 oz
finished copper thickness >82 µm
```

Therefore:

```text
35.56 µm as-manufactured assumption = SUPERSEDED
≥82 µm finished copper = CURRENT MANUFACTURING BOUND
```

Using `82 µm` as a conservative minimum:

```text
R_sheet,1layer,max ≈0.210 mΩ/square
R_sheet,2layer,ideal,max ≈0.105 mΩ/square
```

---

## 3. Corrected positive-distribution geometry bounds

Rescaling the same reconstructed 2D current-spreading geometry to the minimum finished copper thickness gives:

```text
BAT+ common:
R_BAT+,common,geometry ≤~0.108 mΩ
P@175.4A ≤~3.32 W
average modeled drop ≤~18.9 mV

T1 local PCB:
R_T1local,PCB ≤~0.152 mΩ
P@87.7A ideal share ≤~1.17 W

T2 local PCB excluding J8:
R_T2local,PCB ≤~0.0624 mΩ
P@87.7A ideal share ≤~0.48 W
```

Two same-net `J8` power terminals remain separated by about 93 mm without an ordinary PCB polygon spanning the complete gap:

```text
external high-current link intent = STRONGLY_SUPPORTED
exact J8 conductor = OPEN
R_J8 = MEASUREMENT_NEEDED
```

Partial positive PCB-only input-referred model under ideal 50/50 T1/T2 sharing:

```text
R_eq,positive-PCB,partial ≤~0.162 mΩ
P@175.4A ≤~4.98 W
```

This excludes connector/contact, fuse elements, J8, hot copper and assembly reinforcement.

Status:

```text
MANUFACTURING_GEOMETRY_BOUND / NOT_MEASURED
```

Important correction:

```text
old partial positive PCB model ≈11.5 W
→ SUPERSEDED

current ≥82 µm manufacturing-bound model ≤~4.98 W
```

The PCB-only distribution remains material but is no longer justified as approximately equal to the full main-MOS conduction bucket.

---

## 4. B↔BAT- battery-interface bank

Seven parallel `CSD18510KCS` devices connect:

```text
B
↓
Q39 Q40 Q41 Q42 Q63 Q64 Q65
↓
BAT-
```

Verified:

```text
Source → B
Drain → BAT-
12VP → individual 68.1 Ω → Gate
Gate → individual 47.5 kΩ → B
```

Independent ASP product specification verifies input reverse-polarity protection. Hardware structure strongly supports Q39...Q65 as the low-side ideal-diode implementation.

U4 monitors the same B↔BAT- boundary and exports BOCP.

```text
B↔BAT- analog sensing → BOCP = VERIFIED
nominal BOCP gain ≈22.1 V/V = VERIFIED_FROM_MAIN_BOARD
exact control-board trip/response = OPEN / EVIDENCE_BLOCKED
```

---

## 5. Seven-MOS loss scale — NOT MEASURED

Using device max `RDS(on)=1.7mΩ @ VGS=10V` only as a boundary:

```text
7 ideal parallel → Req≈0.243mΩ
P@175.4A≈7.47W
```

Actual battery-interface loss:

```text
P_batteryInterface = I_source × ΔV(B↔BAT-)
```

with MOS temperature and `12VP` recorded.

---

## 6. Fair-comparison boundary

```text
Contract P — product level
→ preserve verified reverse-polarity protection and required current/fault information; count loss.

Contract C — core converter
→ exclude battery-interface overhead from A0/A1/candidate equally.
```

Do not delete required product functionality only on the candidate side and call the removed watts a topology gain.

---

## 7. Kelvin segmentation

```text
M0 BAT+ terminal → each fuse input
M1 each main fuse input → output
M2 T1 fuse-output node → T1 center tap
M3 J8 left → J8 right
M4 J8 right → T2 center tap
M5 B ↔ BAT- battery-interface bank
M6 B-return distribution if separately accessible
```

Preferred currents:

```text
I_source
I_T1
I_T2
```

Simple series segment:

```text
P_segment = I_segment × ΔV_segment
R_segment = ΔV_segment / I_segment
```

Multi-terminal BAT+:

```text
P_BAT+ = Σ I_k ΔV_k
```

not `I_source × one arbitrary fuse-input drop`.

---

## 8. Geometry-to-measurement diagnostic rule — UPDATED

Measured values should be compared with the **≥82 µm manufacturing-bound geometry**, not the old 35.56 µm PcbDoc model.

Example for T1 local path:

```text
current geometry-only bound:
R_T1local,PCB ≤~0.152 mΩ
```

If measured end-to-end resistance is materially higher, investigate:

```text
contacts / fuse terminals / necks
thermal rise
boundary includes non-PCB conductor
current crowding / via bottleneck
manufacturing deviation
```

If lower, investigate:

```text
actual copper thicker than 82 µm
solder reinforcement
parallel metal / bus structure
measurement boundary mismatch
```

---

## 9. Distribution-loss reconstruction

```text
P_distribution,meas =
    P_BAT+common
  + ΣP_fuse
  + P_T1local
  + P_J8
  + P_T2local
  + P_BreturnCopper
  + P_batteryInterface
```

Do not mix this with core/magnetic loss until the comparison boundary is explicit.

---

## 10. Gate logic

```text
A0 measured distribution + battery-interface loss
↓
A0 main switch + HFT dynamic loss
↓
separate product-interface overhead from intrinsic X1 loss
↓
A0 BAT→X1 Loss Budget v1
↓
A1 matched optimized magnetic benchmark
```

Current status:

```text
R52 finished copper = >82 µm / VERIFIED_FROM_MANUFACTURING_SPEC
old 35.56 µm geometry model = SUPERSEDED
BAT+ common geometry bound = ≤~0.108 mΩ / ≤~3.32 W
partial positive PCB geometry bound = ≤~0.162 mΩ / ≤~4.98 W
J8 resistance = OPEN
B↔BAT- measured loss = OPEN
A0 total BAT→X1 loss = OPEN
A1 = BLOCKED_UNTIL_A0_LOSS_LOCALIZATION
```
