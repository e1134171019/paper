# 14 — ASP-2000 A0 Distribution Resistance and Kelvin Measurement Gate

Status date: 2026-08-19  
Role: `A0 DISTRIBUTION-LOSS / MEASUREMENT GATE`  
Evidence status: `PCB PRIMITIVE RECONSTRUCTION + 2D SHEET MODEL + DATASHEET BOUND`  
Measurement status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark only`

## 1. Purpose

This document narrows the ASP-2000 R52 A0 loss-localization problem from a generic `BAT→X1` boundary to the actual high-current distribution and return paths that must be measured before A1 topology optimization.

Raw company/product files remain outside this public repository.

The current question is:

> How much irreversible loss is already spent simply moving the ~175 A-class source current from the battery terminals into and out of the existing magnetic power stage, before assigning loss to the main switching/HFT conversion mechanism itself?

This distinction matters because a candidate topology may not claim a topology advantage by silently removing protection, disconnect, current-distribution, or interconnect functions that A0 must retain.

---

## 2. Evidence classes

```text
VERIFIED
= directly reconstructed from supplied SchDoc/PcbDoc or official device data

GEOMETRY_MODEL
= nominal-copper 2D sheet-resistance result from reconstructed PCB primitives

DATASHEET_BOUND
= device-loss boundary using official maximum/typical device data

MEASUREMENT_NEEDED
= physical implementation or operating quantity cannot yet be reduced to a defensible scalar
```

No `GEOMETRY_MODEL` or `DATASHEET_BOUND` number in this file is an ASP measured loss.

---

## 3. BAT+ distribution geometry — VERIFIED

PcbDoc reconstruction identifies `BAT+` as one large multi-terminal current-distribution net rather than a narrow routed track.

Verified physical features include:

```text
3 large BAT+ connector power pads
8 main fuse input pads on BAT+
16 BAT+ stitching vias in the connector/distribution region
major BAT+ copper polygons on both Top and Bottom
```

The eight main fuse inputs are the same fuse groups already reconstructed from the schematic:

```text
T1 feed:
F2 F3 F5 F6

T2 feed:
F7 F8 F9 F10
```

The PCB stack extracted previously is:

```text
Top copper    ≈ 1.4 mil ≈ 35.56 um
Bottom copper ≈ 1.4 mil ≈ 35.56 um
```

Nominal room-temperature sheet resistance used for the geometry model:

```text
R_sheet,1layer ≈ 0.485 mΩ/square
```

---

## 4. BAT+ common-polygon 2D geometry model

A finite-difference 2D sheet-conductor model was solved on the reconstructed principal BAT+ Top/Bottom polygon geometry.

Model boundary:

```text
source terminals = the three large BAT+ connector pads
sink terminals   = the eight main fuse-input pads
current condition = equal current per fuse for the balanced reference case
Top + Bottom copper treated as parallel nominal sheet conductors
```

Grid convergence was checked down to approximately 3 mil.

Converged equal-current result:

```text
geometry factor ≈ 0.514 square
R_BAT+,common,geometry ≈ 0.249 mΩ
```

At the research scaling current:

```text
I_source ≈ 175.4 A
```

this corresponds to:

```text
P_BAT+,common,geometry ≈ 7.67 W
ΔV_average ≈ 43.7 mV
```

Status:

```text
GEOMETRY_MODEL / NOT MEASURED
```

The result excludes:

```text
connector contact resistance
fuse element resistance
solder-thickness reinforcement
copper-temperature rise
surface finish
current-crowding detail below model resolution
via-barrel resistance beyond idealized layer sharing
manufacturing tolerance
```

Therefore it is a loss-scale indicator, not a product efficiency datum.

### 4.1 Geometry-induced branch asymmetry

Under the same balanced current boundary, the model predicts different average copper drops toward the two fuse groups:

```text
closer T1 fuse group ≈ 32.9 mV
farther T2 fuse group ≈ 54.5 mV
model difference      ≈ 21.5 mV
```

Status:

```text
GEOMETRY_MODEL ONLY
```

Research implication:

> Even before fuse and transformer tolerances are included, distribution geometry can contribute to T1/T2 current-sharing error. Equal-share assumptions must therefore be checked by measurement rather than imposed on A0.

---

## 5. Post-fuse T1 local path — GEOMETRY_MODEL

The T1 fuse-output node and T1 center-tap node are connected primarily through the reconstructed local PCB copper region.

Equal-current four-fuse group model:

```text
I_T1,ideal-share ≈ 87.7 A
geometry factor  ≈ 0.724 square
R_T1local,PCB    ≈ 0.351 mΩ
```

Corresponding scaling loss/drop:

```text
P_T1local,PCB ≈ 2.70 W
ΔV_T1local    ≈ 30.8 mV
```

Status:

```text
GEOMETRY_MODEL / NOT MEASURED
```

This does not include the fuse elements themselves or transformer-winding resistance.

---

## 6. Post-fuse T2 path contains a non-PCB external-link region

The T2 fuse-output net is physically separated into a fuse-side PCB region and a T2-side PCB region.

PcbDoc contains two large multilayer pads both identified as `J8` on this same power net, with center-to-center spacing of approximately:

```text
93 mm
```

No ordinary reconstructed PCB copper polygon bridges the full gap between these two regions.

Safe interpretation:

```text
J8 external high-current link intent = STRONGLY SUPPORTED
exact conductor implementation       = OPEN
R_J8                                 = MEASUREMENT_NEEDED
```

Do not assume whether the physical link is a wire, jumper, copper strap, busbar, assembly conductor, or another production implementation without assembly/BOM evidence.

### 6.1 PCB-only portions excluding J8

The two PCB portions surrounding J8 give:

```text
fuse-output → left J8     ≈ 0.136 square
right J8 → T2 center tap ≈ 0.160 square
combined PCB-only        ≈ 0.296 square
```

Using the nominal Top/Bottom copper model:

```text
R_T2local,PCB,excludingJ8 ≈ 0.144 mΩ
```

At `I_T2≈87.7 A` ideal share:

```text
P_T2local,PCB,excludingJ8 ≈ 1.10 W
ΔV ≈ 12.6 mV
```

Actual T2 local loss must therefore be written:

```text
P_T2local = P_T2PCB + I_T2² R_J8 + contact losses
```

and cannot be closed numerically until J8 is measured or its physical conductor is identified.

---

## 7. Partial positive-path PCB loss bound

Under the ideal 50/50 T1/T2 current-share reference, combine only the currently modeled PCB copper:

```text
R_eq,BAT+ common      ≈ 0.249 mΩ
branch PCB contribution referred to input
  = (R_T1local + R_T2local,PCB)/4
  ≈ (0.351 + 0.144)/4
  ≈ 0.124 mΩ
```

Therefore:

```text
R_eq,positive-PCB,partial ≈ 0.373 mΩ
```

At `175.4 A`:

```text
P_positive-PCB,partial ≈ 11.5 W
```

Status:

```text
GEOMETRY_MODEL / PARTIAL
```

The missing positive-path terms are substantial:

```text
BAT+ connector/contact
8 fuse elements and fuse contacts
J8 external link + contacts
hot-copper correction
local assembly reinforcement
```

So `11.5 W` must not be treated as the complete positive-distribution loss.

---

## 8. Newly verified BAT− full-current series MOS bank

A critical return-path feature is now directly reconstructed.

The battery-negative connector net is not identical to the main low-side power-stage return net `B`.

Seven TO-220 MOSFET positions bridge these two nets:

```text
Q39 Q40 Q41 Q42 Q63 Q64 Q65
```

PCB pad connectivity verifies:

```text
Drain side  → BAT− net
Source side → B / main low-side return net
```

SchDoc part annotation identifies all seven as:

```text
CSD18510KCS
```

Official device data used for first-order bounding:

```text
40 V N-channel MOSFET
RDS(on),max @ VGS=10 V = 1.7 mΩ
Qg,typ = 119 nC
```

Exact product role is not yet assigned.

Status:

```text
negative-side full-current series MOS bank = VERIFIED
exact protection/disconnect/control role   = OPEN
```

### 8.1 Conduction bound

Seven ideal devices in parallel:

```text
R_eq,25C,max ≈ 1.7 mΩ / 7 ≈ 0.243 mΩ
```

At `I_source≈175.4 A`, if continuously enhanced:

```text
P_negative-series-MOS,25C-bound ≈ 7.47 W
```

Status:

```text
DATASHEET_BOUND / NOT MEASURED
```

It excludes hot `RDS(on)`, VGS variation, current-sharing error, package/contact/PCB resistance and any switching/transient operation.

Research implication:

> A0 contains a second hundred-ampere silicon loss region outside the main A/C switching bank. It must be included in the BAT→X1/system-boundary accounting before claiming that a candidate reduces low-voltage semiconductor loss.

---

## 9. Fair-comparison correction — protection functionality must be matched

A candidate must not obtain an apparent loss advantage by deleting an A0 battery-path function that is required for product protection, isolation/disconnect, reverse-current control, or safety.

Until the exact role of Q39/Q40/Q41/Q42/Q63/Q64/Q65 is verified, comparison policy is:

```text
A0 includes the negative-side series MOS bank loss.

A1 / candidate must either:
1. retain an equivalent required function and count its loss, or
2. explicitly declare the function out of the comparison boundary for BOTH sides.
```

Do not count:

```text
remove protection device → lower loss
```

as a topology improvement.

---

## 10. Revised A0 pre-X1 distribution-loss boundary

The low-voltage full-current accounting must now contain both positive and negative paths:

```text
BAT+
↓
BAT+ common copper / connector
↓
8-way fuse distribution
↓
Fuse elements
↓
T1 local PCB / T2 local PCB + J8
↓
T1/T2 center-tapped primary / main A-C switching stage
↓
B return net
↓
Q39/Q40/Q41/Q42/Q63/Q64/Q65 series bank
↓
BAT−
```

Before assigning HFT/core loss, define:

```text
P_distribution =
    P_BAT+common
  + P_fuses
  + P_T1local
  + P_T2localPCB
  + P_J8
  + P_negativeSeriesMOS
  + P_returnCopper
  + P_contacts
```

The currently available model already shows:

```text
positive PCB partial geometry loss  ≈ 11.5 W
negative series MOS 25C bound       ≈ 7.5 W
```

but these must remain separate evidence classes and must not be added into a claimed measured A0 total.

---

## 11. Kelvin measurement segmentation plan

The next A0 gate is a segmented millivolt-drop measurement rather than further scalar guessing from PCB geometry.

### M0 — BAT+ common distribution

Measure voltage drop from the BAT+ terminal reference to each of the eight fuse-input nodes under the same operating point.

Purpose:

```text
validate current-distribution model
identify T1/T2 feed asymmetry
bound BAT+ common copper/contact loss
```

### M1 — individual fuse drops

For:

```text
F2 F3 F5 F6 F7 F8 F9 F10
```

measure input-to-output millivolt drop and branch current.

Calculate:

```text
P_fuse,total = Σ I_fuse,k × ΔV_fuse,k
```

This is preferable to inferring hot fuse resistance from nominal current rating.

### M2 — T1 local path

Measure:

```text
T1 fuse-output local node → T1 center-tap B
```

with T1 group current.

### M3 — J8 external link

Measure directly across the two J8 power-link terminals:

```text
R_J8 = ΔV_J8 / I_T2
P_J8 = I_T2 × ΔV_J8
```

This closes the largest currently unknown positive-path physical implementation.

### M4 — T2 PCB local section

Measure:

```text
J8 T2-side terminal → T2 center-tap B
```

### M5 — BAT− to B series-MOS bank

Measure the total millivolt drop:

```text
BAT− terminal ↔ B main-return net
```

under source current.

Direct loss:

```text
P_negativeSeriesBank = I_source × ΔV_BAT−↔B
```

This automatically includes hot MOS conduction plus much of the associated connection/contact drop inside the selected measurement boundary.

### M6 — B-return distribution

If accessible, separately measure the drop from the main switching MOS source-return region to the selected `B` bank reference point.

Purpose:

```text
separate return copper from the Q39...Q65 silicon/function block
```

---

## 12. Required measurement channels

Minimum useful set:

```text
I_source
I_T1
I_T2

V_BAT+→F2in
V_BAT+→F3in
V_BAT+→F5in
V_BAT+→F6in
V_BAT+→F7in
V_BAT+→F8in
V_BAT+→F9in
V_BAT+→F10in

V_F2 ... V_F10
V_T1local
V_J8
V_T2local
V_BAT−↔B

relevant connector / fuse / MOS temperatures
```

Measurement principles:

```text
use Kelvin / four-wire sensing for mΩ-class DC-drop quantities
pre-place sense leads with power removed where practical
use appropriate isolated/differential instrumentation for dynamic measurements
record component temperature with the voltage-drop data
avoid interpreting oscilloscope ground-referenced measurements as floating power-node measurements
```

The exact test fixture belongs to the hardware-validation procedure and is not defined by this research note.

---

## 13. Measured loss reconstruction

For a steady operating point, prefer direct electrical loss reconstruction:

```text
P_segment = I_segment × ΔV_segment
```

rather than first converting every segment to resistance.

Then derive resistance when needed:

```text
R_segment = ΔV_segment / I_segment
```

The first measured distribution total becomes:

```text
P_distribution,meas =
    P_BAT+common
  + ΣP_fuse
  + P_T1local
  + P_J8
  + P_T2local
  + P_negativeSeriesBank
  + P_returnCopper
```

This result should be compared against the PCB geometry model as a sanity check, not forced to match it.

---

## 14. Gate logic

After measured distribution loss is available:

```text
A0 distribution loss
↓
add main A/C MOS conduction + switching
↓
add T1/T2 primary copper + core / commutation
↓
obtain credible BAT→X1 loss budget
↓
build A1 matched magnetic benchmark
```

Decision questions:

```text
Q1 — Is the dominant A0 pre-X1 loss ordinary distribution/protection resistance?

Q2 — Can A1 remove most of that loss without changing X1 physics?

Q3 — After fair A1 optimization, is there still a material magnetic/X1 loss mechanism worth replacing?
```

Only Q3 can justify advancing toward a different X1 mechanism.

---

## 15. Formal status

```text
BAT+ multi-terminal distribution geometry = VERIFIED
BAT+ common 2D resistance model           = GEOMETRY_MODEL
T1 local PCB resistance model             = GEOMETRY_MODEL
T2 PCB portions excluding J8              = GEOMETRY_MODEL
J8 external-link physical resistance      = MEASUREMENT_NEEDED
negative-side 7-MOS full-current bank      = VERIFIED
negative-side bank exact function          = OPEN
negative-side bank conduction value        = DATASHEET_BOUND
BAT− / B return-copper resistance           = OPEN
A0 measured distribution loss              = OPEN
A1 matched model                            = BLOCKED UNTIL A0 LOSS BOUNDS / MEASUREMENT
Candidate superiority                      = NOT_ESTABLISHED
Novelty                                    = NOT_ESTABLISHED
```

Next gate:

```text
Segmented Kelvin / millivolt-drop measurement of the actual A0 low-voltage distribution path.
```
