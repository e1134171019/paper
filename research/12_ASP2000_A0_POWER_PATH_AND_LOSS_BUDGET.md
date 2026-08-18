# 12 — ASP-2000 A0 Power Path and Loss-Budget Gate

Status date: 2026-08-19  
Role: `A0 POWER-PATH / LOSS-LOCALIZATION GATE`  
Evidence status: `DIRECT_SCHEMATIC_NET_RECONSTRUCTION + DATASHEET BOUNDS`  
PCB resistance status: `NOT YET QUANTIFIED`  
Novelty relevance: `NONE — benchmark only`

## 1. Purpose

This document reconstructs the ASP-2000 R52 real-product power path far enough to support the first quantitative loss-localization gate.

Source artifacts:

```text
PB-2200-0038-D_ASP-2000-MAIN-R52.SchDoc
PB-2200-0038-D_ASP-2000-MAIN-R52.PcbDoc
```

The raw company/product files remain outside this public repository.

The central question is:

> Where is A0 loss actually concentrated from BAT+ to the first major impedance-transformation region X1?

Do not invent a new topology until this question has a bounded answer.

---

## 2. Directly reconstructed low-voltage power path

### 2.1 BAT+ splits into two separately fused transformer center-tap feeds

The schematic net reconstruction establishes:

```text
BAT+
├─ F2 / F3 / F5 / F6 ─→ T1 pin 8 = B
│                        + local LV bulk node
│
└─ F7 / F8 / F9 / F10 → T2 pin 8 = B
                         + local LV bulk node
```

Main-fuse annotation:

```text
40 A / 32 V @12 V
20 A / 32 V @24 V
```

`F15 = 0603L020YR` is on an auxiliary/sense path and is **not** part of the main 40 A fuse bank.

`F1 = 2 A / 300 V` is also not one of the main BAT+ current-sharing fuses.

### 2.2 Each PQ5050 primary is center-tapped at pin B

Both transformer symbols expose:

```text
pin 9 = A
pin 8 = B
pin 7 = C
```

with the separately fused BAT+ feeds connected to pin `B`.

The direct net reconstruction further establishes:

```text
T1 pin A ─┬─ T2 pin A
          └─ shared A-side low-MOS drain node

T1 pin C ─┬─ T2 pin C
          └─ shared C-side low-MOS drain node
```

Therefore the product is more accurately represented as two separately supplied center-tapped HFT primaries sharing the two switched primary-end nodes, not as four electrically independent five-MOS converter cells.

### 2.3 Low-side MOS connectivity

The schematic contains 20 low-side MOS positions annotated:

```text
CSD18542KCS @12 V
CSD19533KCS @24 V
```

C-side shared drain node has ten directly connected MOS positions:

```text
Q11 Q12 Q13 Q14 Q36
Q24 Q25 Q26 Q27 Q38
```

A-side shared drain node has nine directly reconstructed connected positions:

```text
Q3 Q4 Q5 Q6 Q33
Q18 Q20 Q21 Q37
```

`Q19` has the expected gate/source context but its drain appears isolated in the extracted SchDoc connectivity.

Status:

```text
Q19 drain = SCHEMATIC_ANOMALY / VERIFY PCB-BOM-ASSEMBLY
```

Therefore use:

```text
20 annotated low-side MOS positions
19 directly reconstructed expected power connections
```

until PCB/BOM/assembly evidence resolves Q19.

### 2.4 Operating-mode wording

The center-tapped primaries plus alternating A/C low-side switched nodes are consistent with a push-pull-like power stage.

Status:

```text
center-tapped primary structure = VERIFIED
A/C shared low-side switching nodes = VERIFIED
exact switching timing / modulation = NOT YET VERIFIED
exact operating-mode label = INFERENCE ONLY
```

Do not promote `push-pull` to fully verified until gate timing/control is traced or measured.

---

## 3. Directly reconstructed X1-to-HV path

### 3.1 T1/T2 secondaries are not two completely independent rectified outputs

Direct reconstruction establishes:

```text
T1 pin 5 ───────── T2 pin 2
```

as a common secondary-series junction.

The two outer secondary terminals feed the two rectifier AC legs:

```text
T1 pin 2 → D1/D5 AC-side leg
T2 pin 5 → RL1 path → D2/D6 AC-side leg
```

The relay `RL1` role is not yet assigned; its exact configuration/control function remains open.

### 3.2 High-voltage bridge rectification

Verified diode connectivity:

```text
D1 pin 2 → BUS+
D2 pin 2 → BUS+
D5 pin 1 → BUS-
D6 pin 1 → BUS-
```

with:

```text
D1/D5 = one rectifier leg
D2/D6 = other rectifier leg
```

This establishes a full high-voltage rectification boundary after the series/relay-configured transformer secondary path.

### 3.3 HV DC-link and X3

The HV region contains four positions annotated:

```text
C8 C11 C89 C90
= 680 uF / 315 V
```

and explicit `BUS+ / BUS-` connectivity into the post-bus high-voltage inverter region.

The four-terminal capacitor symbols require footprint/BOM interpretation before claiming the exact internal series/parallel capacitor topology.

Safe status:

```text
HV DC-link capacitor region = VERIFIED
exact capacitor terminal/series-parallel implementation = NOT YET VERIFIED
```

The post-bus high-voltage switching stage remains the product reference for `X3`.

---

## 4. Revised A0 power-path graph

```text
BAT+
│
├─ 4× main fuse bank ─→ T1 center tap B + local LV bulk
│                         │
│                         ├─ T1 B→A half-primary ─┐
│                         └─ T1 B→C half-primary ─┤
│                                                │
└─ 4× main fuse bank ─→ T2 center tap B + local LV bulk
                          │                       │
                          ├─ T2 B→A half-primary ─┤
                          └─ T2 B→C half-primary ─┤
                                                  │
                         shared A-side MOS node ───┤
                         shared C-side MOS node ───┘
                                   ↓
                         common LV return

T1 + T2 magnetic transformation              ← X1 region
                                   ↓
T1 secondary outer ─┐
                    ├─ D1/D5 + D2/D6 rectifier
T1/T2 series link ──┤
T2 secondary outer ─┘
                                   ↓
                              BUS+ / BUS-
                                   ↓
                         HV DC-link region      ← passive X2-capable node
                                   ↓
                         HV inverter            ← X3
                                   ↓
                                AC output
```

Important research correction:

```text
A0 already contains:
- semiconductor paralleling
- two separately fused HFT center-tap feeds
- local LV bulk around each HFT feed
- shared switching nodes across the two HFT primaries
- series/collective secondary voltage formation
```

Therefore a candidate cannot claim benefit merely from `N branches`, `parallel MOS`, `multiple transformers`, or `voltage combining`.

---

## 5. Anchor-current references

Primary research anchor:

```text
Vin  = 12 V
Pout = 2 kW
```

Ideal source current:

```text
Iin,ideal = 2000 / 12 = 166.7 A
```

Using the existing research 95% front-end reference only as a scaling point:

```text
Iin@95% ≈ 175.4 A
```

If the two T1/T2 center-tap feeds shared average current perfectly:

```text
I_T1,avg,ideal-share ≈ 87.7 A
I_T2,avg,ideal-share ≈ 87.7 A
```

If the four main fuses in each feed shared perfectly:

```text
I_fuse,avg,ideal-share ≈ 21.9 A per fuse
```

Status:

```text
these are IDEAL EQUAL-SHARE REFERENCES ONLY
not measured RMS currents
```

Actual RMS/current sharing must be measured or reconstructed from switching waveforms.

---

## 6. MOSFET datasheet bounds for first-order modeling

### 12 V population — CSD18542KCS

Official TI product data:

```text
VDS = 60 V
RDS(on),max @ VGS=10 V = 4 mΩ
Qg,typ = 44 nC
```

### 24 V population — CSD19533KCS

Official TI product data:

```text
VDS = 100 V
RDS(on),max @ VGS=10 V = 10.5 mΩ
Qg,typ = 27 nC
```

These are datasheet boundaries, not measured ASP operating values.

At 12 V, if ten CSD18542KCS devices are truly connected in parallel on one active A/C switching node:

```text
R_eq,silicon,25C,max ≈ 4 mΩ / 10 = 0.40 mΩ
```

For the currently reconstructed nine-device A-side net:

```text
R_eq,silicon,25C,max ≈ 4 mΩ / 9 = 0.444 mΩ
```

At the 175.4 A scaling current, the corresponding active-state silicon-only `I²R` reference is approximately:

```text
10 devices: 175.4² × 0.00040 ≈ 12.3 W
9 devices:  175.4² × 0.000444 ≈ 13.7 W
```

Do **not** use these as actual stage losses because they omit:

```text
switching duty/current waveform
junction-temperature rise of RDS(on)
current mismatch
package/lead/contact resistance
PCB copper
source/common-return resistance
switching loss
Coss / gate / dead-time / commutation
```

They are only a lower-level feasibility bound showing that milliohm-scale silicon resistance remains material at the 12 V anchor.

---

## 7. A0 Battery-to-X1 loss equation

The first formal loss-localization boundary is:

```text
BAT+ → main fuse distribution → local LV node/bulk
→ T1/T2 primary halves → active A/C MOS bank → common LV return
```

Use:

```text
P_A0,BAT→X1 =
    P_common_upstream
  + P_fuse_banks
  + P_local_interconnect
  + P_bulk_ESR
  + P_MOS,cond
  + P_MOS,sw
  + P_primary,Cu
  + P_core
  + P_clamp/commutation_before_X1
```

with:

```text
P_common_upstream = I_source,RMS² R_common

P_fuse_banks = Σ I_fuse,k,RMS² R_fuse,k(T)

P_MOS,cond = Σ I_MOS,k,RMS² RDS(on),k(Tj,VGS)

P_MOS,sw ≈ Σ [Eon + Eoff + Eoss + commutation terms] fs

P_primary,Cu = Σ I_primary,RMS² R_primary,AC(f,T)
```

Core loss requires the actual frequency, flux swing and core/material data; it is not yet numerically bounded from the present source file.

---

## 8. Current loss-budget table

| Region | Current variable | Loss model | Current evidence | Status |
|---|---|---|---|---|
| BAT+/upstream common path | `I_source,RMS` | `I²R` | topology known | `R NOT YET QUANTIFIED` |
| 2 × four-fuse banks | `I_fuse,k,RMS` | `ΣI²R_fuse` | exact main fuse grouping reconstructed | `R_fuse / RMS NEEDED` |
| local T1/T2 LV nodes | local pulse/RMS | copper + capacitor ESR | local capacitor association reconstructed | `ESR / PCB R NEEDED` |
| A/C MOS switching node | `I_MOS,RMS` | conduction + switching | MOS connectivity reconstructed; Q19 anomaly | `WAVEFORM / TEMP NEEDED` |
| T1/T2 primary halves | `I_primary,RMS` | `I²Rac + core` | exact center-tap/A/C connectivity reconstructed | `Rac / f / ΔB NEEDED` |
| X1→rectifier | secondary RMS | copper + diode/commutation | secondary series/rectifier graph reconstructed | `WAVEFORM NEEDED` |
| HV DC-link | capacitor ripple | ESR/dielectric | BUS region verified | `CAP FOOTPRINT / RIPPLE NEEDED` |
| X3 | HV inverter current | cond + sw | post-bus stage verified | later gate |

This table intentionally leaves unknown quantities blank rather than guessing them.

---

## 9. What can and cannot be concluded now

### VERIFIED

```text
- two separately fused T1/T2 center-tap supplies
- four main fuses per center-tap feed
- local bulk capacitor regions at each feed
- T1/T2 A primary ends share one switching net
- T1/T2 C primary ends share one switching net
- low-side MOS devices are heavily paralleled on those shared nodes
- T1/T2 secondaries contain a direct series junction
- D1/D5 and D2/D6 form the two HV rectifier legs to BUS+/BUS-
- post-bus X3 exists
```

### HYPOTHESIS / INFERENCE

```text
- push-pull-like operation from the center-tapped primary graph
- equal T1/T2 current sharing
- equal fuse sharing
```

### NOT YET ESTABLISHED

```text
- dominant A0 loss bucket
- actual MOS RMS/current sharing
- exact fs / duty / dead time
- PCB common-path resistance
- T1/T2 Rac/core loss
- source 100/120 Hz ripple
- active X2 value
- candidate superiority
- novelty
```

---

## 10. Required Gate-1 measurements / extraction

Priority order:

```text
G1.1 source current:
     Iavg, IRMS, 100/120 Hz, HF ripple

G1.2 split current:
     T1 center-feed current
     T2 center-feed current

G1.3 fuse-bank loss:
     voltage drop / resistance of each main fuse path under load

G1.4 LV common-path resistance:
     BAT+ connector → fuse bank → local node
     MOS source/common-return path

G1.5 primary current / magnetic loss:
     T1/T2 primary current waveform
     winding Rdc/Rac
     fs / flux swing / temperature

G1.6 MOS loss:
     VGS, VDS, current waveform, switching timing, device temperature
```

For PCB/interconnect resistance, use measurement and/or Q3D/field extraction rather than estimating from schematic geometry.

---

## 11. Gate decision

Do not proceed from product inspection directly to a new topology claim.

Next decision rule:

```text
Locate the largest credible BAT→X1 loss buckets in A0.
Then ask whether A1 optimized magnetic architecture can remove them.
Only the loss that survives A1 becomes a legitimate reason to replace the X1 mechanism.
```

Sequence:

```text
A0 actual product loss localization
↓
A1 matched optimized HFT
↓
X1 mechanism comparison
↓
X2 Buffer OFF/ON
↓
Candidate topology synthesis only if a physical gap survives
```

Current status:

```text
A0 topology graph              = SUBSTANTIALLY RECONSTRUCTED
A0 numerical loss budget       = OPEN
PCB R extraction               = OPEN
Q19 connectivity anomaly       = OPEN
A1 matched model               = NEXT AFTER A0 LOSS BOUNDS
Candidate superiority          = NOT ESTABLISHED
Novelty                        = NOT ESTABLISHED
```
