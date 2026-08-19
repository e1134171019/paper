# 24 — ASP-2000 A0 U5 Driver Variant and SavPP Gate

Status date: 2026-08-19  
Role: `A0 GATE-DRIVE ASSEMBLY-OPTION / ENABLE BOUNDARY CORRECTION`  
Evidence status: `DIRECT SCHDOC NET TRACE + R52 DESIGN FIELDS + OFFICIAL CANDIDATE PINOUT CROSS-CHECK`  
Production population status: `NOT YET BOM/PHYSICAL VERIFIED`  
Novelty relevance: `NONE — A0 timing/loss evidence governance`

## 1. Purpose

`research/23_ASP2000_A0_PRIMARY_SNUBBER_AND_GATE_DRIVER_BOUNDARY.md` identified U5 as an upstream dual-driver layer but intentionally left the exact populated device and signal direction open.

A deeper pinout and stuffing-path audit resolves the design intent more precisely:

> R52 is laid out to support a direct 0-ohm command-distribution path and a U5-buffered command-distribution path, while the U5 footprint itself is pin-compatible with both ADP3654 and 2EDN7524F across pins 2–7. The different function of pins 1/8 is deliberately accommodated by the Q73/SavPP network.

This note supersedes any wording that treats U5 as definitely populated in the production A0 unit or treats R212/R213 as definitely populated in the same assembly as U5.

---

## 2. U5 database/design fields — VERIFIED

The R52 SchDoc component record for U5 contains:

```text
Library reference = ADP3654
Comment           = 2EDN7524F

primary internal option:
MC-0802-0500-A
ADP3654ARDZ

second internal option:
MC-0802-1100-A
2EDN7524F
```

The R52 component export also identifies U5 with the `2EDN7524F` design comment.

Formal status:

```text
R52 design supports ADP3654 / 2EDN7524F compatible footprint = VERIFIED
R52 current design comment favors 2EDN7524F                  = VERIFIED_FROM_DESIGN_DATA
production-populated device                                  = OPEN
```

A separate Drive BOM containing ADP3654 belongs to another ADP product and is `CONTEXT_ONLY`; it cannot identify the ASP-2000 population.

---

## 3. Candidate pinout cross-check — IMPORTANT

Official ADP3654 pin functions:

```text
1 = NC
2 = INA
3 = PGND
4 = INB
5 = OUTB
6 = VDD
7 = OUTA
8 = NC
```

Official 2EDN7524F PG-DSO-8 pin functions:

```text
1 = ENA
2 = INA
3 = GND
4 = INB
5 = OUTB
6 = VDD
7 = OUTA
8 = ENB
```

Thus pins `2…7` are functionally aligned between the two candidate devices.

The only major footprint-function difference is:

```text
ADP3654 pin1/pin8 = NC
2EDN7524F pin1/pin8 = channel enables
```

This exactly explains why the R52 SchDoc symbol, inherited from the ADP3654 library, displays pin 1/8 as `NC` even though the design comment can be `2EDN7524F`.

---

## 4. Q73 / SavPP connection — VERIFIED

R52 direct net trace establishes:

```text
U5 pin 1
┐
├── common node → Q73 collector
┘
U5 pin 8

Q73 = DTC114EKAT146
      digital NPN transistor

Q73 base    → SavPP
Q73 emitter → B / SIG
```

Therefore, if the populated U5 is `2EDN7524F`:

```text
U5 pin1 = ENA
U5 pin8 = ENB

Q73 ON
→ ENA/ENB pulled to B/ground
→ both 2EDN channels forced low
```

The 2EDN7524F official datasheet states that low ENA/ENB forces the corresponding output low.

Conditional functional interpretation:

```text
SavPP → Q73 → common U5 enable pull-down
= STRONGLY_SUPPORTED FOR THE 2EDN7524F POPULATION OPTION
```

If U5 is ADP3654 instead:

```text
pin1/pin8 = NC
```

so the same Q73 copper connection does not control the ADP3654 channels.

This is strong evidence that the board intentionally tolerates both device options rather than evidence of a schematic mistake.

Exact `SavPP` logic meaning at the control-board level remains open; do not expand the abbreviation or claim its firmware policy without upstream evidence.

---

## 5. Two command-distribution paths per logical side

### A logical command

Direct R52 trace gives:

```text
DR-A
├─ R21 = 47.5 Ω → DA1 local push-pull driver → DA1-G → 5 A-side MOS
│
├─ R213 = 0 Ω ─────────────────────────────→ DR-A2
│                                             ↓
│                                             R45 = 47.5 Ω
│                                             ↓
│                                             DA2 local push-pull driver
│                                             ↓
│                                             DA2-G → 5 A-side MOS
│
└─ R207 = 1 kΩ → U5 INB
                  ↓
               U5 OUTB
                  ↓
               R210 = 2.21 Ω
                  ↓
                DR-A2
```

### B/C logical command

```text
DR-B
├─ R43 = 47.5 Ω → DB1 local push-pull driver → DB1-G → 5 C-side MOS
│
├─ R212 = 0 Ω ─────────────────────────────→ DR-B2
│                                             ↓
│                                             R67 = 47.5 Ω
│                                             ↓
│                                             DB2 local push-pull driver
│                                             ↓
│                                             DB2-G → 5 C-side MOS
│
└─ R206 = 1 kΩ → U5 INA
                  ↓
               U5 OUTA
                  ↓
               R211 = 2.21 Ω
                  ↓
                DR-B2
```

U5 inputs also have 10 kΩ-class pull-downs to B, and U5 outputs have 47.5 kΩ-class pull-downs to B.

---

## 6. Assembly-option interpretation — STRONGLY SUPPORTED

The schematic contains both:

```text
0 Ω direct bypass path
and
active U5 buffered path
```

between the first and second local driver subgroups.

Treating a low-impedance push-pull U5 output and the 0 Ω bypass as blindly simultaneous, unconditional production paths would feed the buffered output back into the command/input net and does not form a sensible generic drive abstraction.

Therefore the safest current interpretation is:

```text
R212/R213 direct path
vs
U5 buffered path
= ASSEMBLY / STUFFING OPTIONS OR VARIANT-DEPENDENT PATHS
```

Evidence grade:

```text
STRONGLY_SUPPORTED_BY_TOPOLOGY
NOT YET POPULATION_VERIFIED
```

Do not claim the exact stuffing rule until one of the following is obtained:

```text
ASP-2000 R52 BOM / variant BOM
real assembled-board photograph readable at U5/R212/R213
continuity + component-presence inspection on production hardware
```

---

## 7. Correction to earlier 4-driver / 2-command statement

The broad functional conclusion survives:

```text
4 local push-pull driver subgroups
→ 2 logical A/C switch functions
```

But the stronger historical wording:

```text
R212/R213 = 0 Ω proves production DR-A=DR-A2 and DR-B=DR-B2
```

must be narrowed.

Current formal statement:

```text
R52 DESIGN offers two ways to distribute each logical command to subgroup 2:
1. direct 0 Ω bypass
2. U5 buffered path

production stuffing selection = OPEN
```

Therefore actual subgroup propagation mismatch cannot be derived from schematic connectivity alone.

---

## 8. Timing consequence

Exact A0 timing remains hardware evidence:

```text
fs        = OPEN
duty      = OPEN
dead time = OPEN
DA1↔DA2 propagation mismatch = OPEN
DB1↔DB2 propagation mismatch = OPEN
```

Official driver delays may only describe device capability.

For example, if 2EDN7524F is populated, its datasheet timing does **not** automatically equal product dead time because the system also contains:

```text
control-board timing
U5 path or bypass selection
47.5 Ω local base-drive resistors
local complementary transistor stage
individual 27.4 Ω MOS gate resistors
MOS gate charge / Miller behavior
PCB parasitic inductance
```

Likewise ADP3654 timing cannot be substituted unless its population is established.

---

## 9. Correct measurement hierarchy

Before using U5 pins as a benchmark timing boundary:

### G-V0 — population inspection

Record:

```text
U5 populated? yes/no
U5 top marking / P/N
R212 populated? yes/no
R213 populated? yes/no
```

This single inspection determines which design path is actually active.

### G-V1 — external command timing

Measure:

```text
DR-A
DR-B
```

relative to B/SIG.

### G-V2 — subgroup-drive timing

Measure:

```text
DR-A2
DR-B2
```

then compare:

```text
DR-A → DR-A2 delay
DR-B → DR-B2 delay
```

### G-V3 — actual MOS gate timing

Representative actual Gate-to-own-Source measurements:

```text
DA1-G
DA2-G
DB1-G
DB2-G
```

Only G-V3 closes the actual four-subgroup switching synchronization seen by the power MOSFETs.

### G-V4 — SavPP / enable check

If U5 is confirmed as 2EDN7524F:

```text
SavPP
U5 ENA/ENB node
OUTA/OUTB
```

may be correlated to verify shutdown behavior.

Do not perform this inference for an ADP3654 population, where pins 1/8 are NC.

---

## 10. Loss-accounting consequence

The driver architecture creates three different possible loss categories:

```text
P_U5        — only if active/populated in the selected assembly
P_localBJT  — four local push-pull stages
P_gateR     — twenty individual 27.4 Ω gate resistors
```

Gate-charge energy ultimately scales with actual switching frequency and gate charge, but distribution of dissipation between U5/local transistors/gate resistors depends on the active stuffing path and waveform.

Therefore:

```text
P_gateDriver,A0 = OPEN
```

and should not be represented only by the simple `N Qg Vgs fs` gate-charge energy equation once detailed device-level loss allocation is required.

---

## 11. Fair A1/candidate requirement

A1 and any candidate are allowed to improve the gate-drive distribution, but must compare actual complete effects:

```text
propagation mismatch
switching overlap
commutation/snubber energy
MOS transition loss
driver dissipation
EMI/ringing consequences
```

A lower driver-part count is not automatically a lower-loss solution if it increases power-device switching loss.

---

## 12. Formal status

```text
U5 dual-compatible footprint                  = VERIFIED
U5 pins2–7 ADP3654/2EDN functional alignment = VERIFIED_FROM_OFFICIAL_PINOUTS
U5 pin1/8 candidate difference                = VERIFIED_FROM_OFFICIAL_PINOUTS
Q73 = DTC114EKAT146                           = VERIFIED_FROM_R52 DESIGN DATA
Q73 collector → U5 pins1+8                   = VERIFIED
Q73 base → SavPP                              = VERIFIED
Q73 emitter → B/SIG                           = VERIFIED
2EDN option common enable pull-down via Q73   = STRONGLY_SUPPORTED / CONDITIONAL_ON_2EDN_POPULATION
ADP option pin1/8 unaffected because NC       = VERIFIED_DEVICE_BEHAVIOR
R212/R213 direct 0 Ω distribution path        = VERIFIED_IN_DESIGN
U5 buffered distribution path                 = VERIFIED_IN_DESIGN
direct vs buffered production stuffing        = OPEN / BOM_OR_PHYSICAL_INSPECTION_NEEDED
4 local driver subgroups                      = VERIFIED_IN_DESIGN
2 logical A/C command functions               = VERIFIED_AT_FUNCTIONAL_TOPOLOGY_LEVEL
exact production propagation path             = OPEN
internal fs / duty / dead time                 = OPEN
actual gate-driver loss                        = OPEN
A1                                             = BLOCKED_UNTIL_A0_LOSS_LOCALIZATION
Candidate #10                                  = NOT_ASSIGNED
Novelty                                        = NOT_ESTABLISHED
```
