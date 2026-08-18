# 13 — ASP-2000 A0 Numerical Loss Bounds

Status date: 2026-08-19  
Role: `A0 NUMERICAL-BOUND / LOSS-LOCALIZATION SUPPORT`  
Evidence status: `PCB STACK EXTRACTION + OFFICIAL MOSFET DATASHEET + PARAMETRIC MODEL`  
Measurement status: `NOT MEASURED`  
Novelty relevance: `NONE — benchmark only`

## 1. Purpose

This document converts the reconstructed ASP-2000 R52 A0 power path into the first numerical loss bounds without pretending that unmeasured quantities are known.

Evidence classes used here:

```text
VERIFIED
= directly extracted from the supplied SchDoc/PcbDoc or official device data

BOUND
= numerical upper/lower/scaling boundary from verified geometry/device data

PARAMETRIC
= equation evaluated versus an unknown variable such as fs or temperature multiplier

MEASUREMENT_NEEDED
= no defensible scalar value yet
```

The goal is not to rank the complete inverter yet. The goal is to determine which BAT→X1 loss buckets are already large enough to deserve priority measurement.

---

## 2. PCB copper stack boundary

Direct PcbDoc stack extraction shows the actual signal stack is:

```text
Top copper     = 1.4 mil
FR-4 dielectric
Bottom copper  = 1.4 mil
```

The active signal-layer set contains Top + Bottom; the plane-layer set is empty.

Using nominal copper resistivity at room temperature:

```text
rho_Cu ≈ 1.724e-8 ohm·m
copper thickness = 1.4 mil ≈ 35.56 um
```

single-layer sheet resistance:

```text
R_sheet = rho / t ≈ 0.485 mΩ/square
```

If Top and Bottom were ideally equal, perfectly paralleled copper of the same geometry:

```text
R_sheet,2layer,ideal ≈ 0.242 mΩ/square
```

This is a geometry-independent scaling relation. It is **not** the actual BAT+ path resistance because the real current distribution depends on polygon width, necks, vias, pads, solder reinforcement, terminals and current spreading.

---

## 3. Why one copper square matters at 12 V / 2 kW

Research anchor:

```text
Iin,ideal = 166.7 A
Iin@95% scaling reference ≈ 175.4 A
```

At 175.4 A, one single-layer 1.4-mil copper square would dissipate:

```text
P_per_square ≈ I² R_sheet
             ≈ 14.9 W / square
```

If the same geometry were perfectly shared by Top + Bottom:

```text
≈ 7.46 W / effective square
```

After ideal split into the two transformer center-tap feeds:

```text
I_feed,avg,ideal ≈ 87.7 A
```

per-square scaling becomes:

```text
single layer ≈ 3.73 W/square
ideal Top+Bottom ≈ 1.87 W/square
```

After ideal split into four fuse branches within one feed:

```text
I_fuse,avg,ideal ≈ 21.9 A
```

per-square copper scaling becomes:

```text
single layer ≈ 0.233 W/square
ideal Top+Bottom ≈ 0.117 W/square
```

Research implication:

> The first high-current common copper region can be comparable to semiconductor conduction loss even when its physical length is modest. Current splitting only becomes useful after the common full-current exposure is minimized.

---

## 4. Physical placement envelope from the PCB

PcbDoc component placement directly gives:

```text
BAT+ connector center ≈ (26375.98 mil, 9802.23 mil)
```

Straight-line center-to-center distances from BAT+ to the main fuse positions are approximately:

```text
F6  ≈ 35.95 mm
F5  ≈ 36.41 mm
F3  ≈ 37.81 mm
F2  ≈ 40.03 mm
F7  ≈ 40.69 mm
F8  ≈ 43.99 mm
F9  ≈ 47.79 mm
F10 ≈ 51.99 mm
```

These values are **placement distances only**, not copper-path lengths and not resistance estimates.

They show that the full-current region is physically nonzero before the two four-fuse banks are reached. Exact copper R still requires polygon/neck/via extraction or four-wire measurement.

---

## 5. 12 V MOS-bank conduction bound

The 12 V schematic population uses:

```text
CSD18542KCS
```

Official TI data:

```text
VDS = 60 V
RDS(on),max @ VGS=10 V = 4 mΩ
Qg,typ = 44 nC
```

Current reconstructed switching nodes:

```text
C-side = 10 directly connected MOS positions
A-side = 9 directly connected positions
Q19 drain connectivity = OPEN
```

Silicon-only parallel resistance at the datasheet 25°C/max boundary:

```text
10 devices → Req ≈ 0.400 mΩ
9 devices  → Req ≈ 0.444 mΩ
```

For the push-pull-like alternating A/C switching graph, use the simplified sensitivity model:

```text
P_MOS,cond ≈ 0.5 I_on² (R_A + R_C)
```

If the active switched-primary current is represented by the 175.4 A scaling current and A/C each conduct 50% of the cycle:

```text
9-device A + 10-device C
→ P_MOS,cond,25C-bound ≈ 13.0 W
```

If both nodes were ten devices:

```text
≈ 12.3 W
```

These are **not measured product losses**. The model omits magnetizing/ripple current, dead time, imbalance, package/PCB resistance and actual duty.

---

## 6. Hot-RDS(on) sensitivity — model only

Do not assume a temperature coefficient before locking the actual TI normalized-temperature curve and device junction temperature.

For planning only, define:

```text
kT = RDS(on,hot) / RDS(on,25C)
```

Using the current 9+10-device 13.0 W room-temperature bound:

```text
kT = 1.0 → ~13.0 W
kT = 1.5 → ~19.5 W
kT = 1.8 → ~23.4 W
kT = 2.0 → ~26.0 W
```

These multiplier cases are **sensitivity scenarios, not datasheet claims**.

This already shows why junction temperature and current sharing must be measured or thermally modeled before comparing candidates.

---

## 7. Gate-drive loss is parameterizable even though fs is unknown

For the 12 V population:

```text
N = 20 annotated MOS positions
Qg,typ = 44 nC/device
```

A first-order gate-drive energy model is:

```text
P_gate ≈ N Qg VGS fs
```

At `VGS = 10 V`:

```text
P_gate ≈ 8.8e-6 × fs  [W, fs in Hz]
```

Sensitivity:

```text
20 kHz  → ~0.176 W
50 kHz  → ~0.440 W
100 kHz → ~0.880 W
```

This only represents ideal gate-charge energy. It does not include driver quiescent loss, overlap loss, Coss/Eoss, Miller transition, ringing or commutation loss.

Therefore gate-drive energy alone is unlikely to explain a tens-of-watts BAT→X1 loss bucket unless switching frequency or drive conditions are unusual; total switching loss remains open.

---

## 8. MOS switching loss remains OPEN

The supplied main-board SchDoc/PcbDoc does not expose a defensible switching-frequency scalar.

Required before numerical switching-loss calculation:

```text
fs
VDS waveform
ID waveform
turn-on / turn-off transition time or energy
Coss/Eoss operating voltage
commutation / clamp behavior
dead time
ringing / avalanche status
```

Use only parametric form for now:

```text
P_sw ≈ Σ(Eon + Eoff + Eoss + Ecommutation) fs
```

or, as a rough overlap model only when waveform evidence supports it:

```text
P_overlap ≈ 0.5 VDS ID (tr + tf) fs
```

Status:

```text
P_MOS,sw = MEASUREMENT_NEEDED / MODEL_NEEDED
```

---

## 9. Fuse loss remains OPEN

The schematic proves the architecture and rating annotation:

```text
2 banks × 4 fuses
40 A / 32 V @12 V
20 A / 32 V @24 V
```

but does not expose a manufacturer part number or cold/hot resistance sufficient for a defensible scalar loss.

Required:

```text
R_fuse,cold
R_fuse,hot
or measured Vdrop at operating current
```

Then:

```text
P_fuse,total = Σ I_fuse,RMS² R_fuse(T)
```

Because each fuse branch sees only part of the source current, fuse loss cannot be estimated by applying the full 175 A to one element.

---

## 10. Transformer primary copper/core loss remains OPEN

The source confirms:

```text
T1 = PQ5050
T2 = PQ5050
center-tapped primaries
shared A/C switching nodes
series/collective secondary formation
```

But `PQ5050` identifies the magnetic form factor, not the actual loss model.

Still required:

```text
primary turns
secondary turns
wire/foil geometry
Rdc
Rac at fs
core material
Ae / le / Ve
fs
flux swing ΔB
primary RMS waveform
temperature
```

Therefore:

```text
P_primary,Cu = OPEN
P_core       = OPEN
```

Do not infer a magnetic loss merely from core size.

---

## 11. Current first-order ranking

At this stage the only defensible numerical comparisons are order-of-magnitude bounds:

```text
12 V MOS silicon conduction:
~13 W at the current 25°C/max-RDS simplified 9+10-device bound

1 full-current copper square, one 1.4-mil layer:
~14.9 W/square

1 full-current copper square, ideal Top+Bottom parallel:
~7.46 W/effective-square

MOS ideal gate-charge energy:
sub-watt across 20–100 kHz in the simple 10 V model
```

This does **not** establish the dominant loss bucket.

It does establish a measurement priority:

```text
Priority 1 = actual common-path / distribution resistance
Priority 2 = hot MOS conduction + current sharing
Priority 3 = MOS switching / commutation
Priority 4 = T1/T2 primary copper + core
Priority 5 = fuse hot resistance / Vdrop
```

Fuse and magnetic losses may move upward once measured.

---

## 12. Main research consequence

The strongest new conclusion is not that MOS loss dominates.

It is:

> At the 12 V / 2 kW anchor, ordinary PCB copper geometry before current splitting can consume the same order of watts as the entire heavily paralleled low-side MOS silicon. Therefore `R_common` is a first-class topology/packaging variable, not a layout afterthought.

This strengthens the retained structural rule:

```text
full-current common region
→ minimize physical/electrical exposure
→ split current
→ enter X1 quickly
```

but it still does not prove that the working candidate is superior to A0/A1.

---

## 13. Next measurement gate

The minimum measurement set needed to turn the present bounds into an actual A0 loss budget is:

```text
M1. source current waveform
    Iavg / IRMS / 100-120Hz / HF

M2. T1 and T2 center-tap currents

M3. BAT+ connector → each fuse-bank input Kelvin Vdrop

M4. each fuse Vdrop under load

M5. fuse output → T1/T2 center-tap Vdrop

M6. MOS bank VDS(on) / current / case or junction-temperature proxy

M7. switching frequency and gate timing

M8. T1/T2 primary current waveform and winding resistance
```

With these, the next formal table can become:

```text
A0 @ 12 V / 2 kW
common copper     = xx W
fuses             = xx W
MOS conduction    = xx W
MOS switching     = xx W
primary copper    = xx W
core              = xx W
commutation/clamp = xx W
-----------------------
BAT→X1 total      = xx W
```

Until then:

```text
A0 dominant loss bucket = NOT ESTABLISHED
candidate advantage     = NOT ESTABLISHED
novelty                 = NOT ESTABLISHED
```
