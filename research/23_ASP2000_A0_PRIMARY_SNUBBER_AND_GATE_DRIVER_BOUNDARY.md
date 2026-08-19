# 23 — ASP-2000 A0 Primary Snubber and Gate-Driver Boundary

Status date: 2026-08-19  
Role: `A0 PRIMARY COMMUTATION / GATE-DRIVER EVIDENCE GATE`  
Evidence status: `DIRECT SCHDOC NET RECONSTRUCTION + R52 COMPONENT EXPORT + DEVICE-OPTION TRACE`  
Hardware waveform status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark loss localization`

## 1. Purpose

After correcting the R52 manufactured-copper bound, the next unresolved A0 loss region is no longer safely dominated by PCB copper. This note closes what can still be established from the R52 design files around the two primary switched nodes before hardware waveforms are available.

Questions:

```text
1. Is there an explicit primary commutation/clamp/snubber network across A/C?
2. Is that network dissipative or regenerative?
3. What upstream gate-driver layer exists before the four local MOS-driver subgroups?
4. Which quantities remain impossible to infer without waveforms or populated-BOM evidence?
```

Raw company Altium files remain outside this public repository.

---

## 2. Primary switched nodes — reference boundary

Current A0 electrical switch functions remain:

```text
A node
= T1 pin 9 + T2 pin 9
= drains of 10 A-side main MOS

C node
= T1 pin 7 + T2 pin 7
= drains of 10 C-side main MOS

common main-MOS source/return
= B
```

The A/C nodes are therefore the correct primary commutation-voltage boundary.

---

## 3. Explicit A↔C RC snubber network — VERIFIED

Direct SchDoc graph reconstruction identifies two symmetric series-RC branches connected directly between the two high-current primary switched nodes.

### Branch S-A

```text
A
↓
C62 = 103 / 1 kV
     = 10 nF class
↓
R110 = 100 Ω / 2512
↓
C
```

### Branch S-C

```text
A
↓
R119 = 100 Ω / 2512
[parallel tuning position R195 = NC]
↓
C65 = 103 / 1 kV
     = 10 nF class
↓
C
```

The physical order of R and C is reversed between the two branches, but each branch is electrically a 10 nF-class capacitor in series with a 100 Ω resistor across A↔C.

Formal status:

```text
A↔C branch 1: 10 nF + 100 Ω series RC = VERIFIED
A↔C branch 2: 10 nF + 100 Ω series RC = VERIFIED
R195 optional parallel tuning position       = VERIFIED / NC IN DESIGN DATA
```

Do not replace the physical two-branch structure with a single lumped equivalent in the formal power graph unless the approximation is explicitly labelled.

For small-signal intuition only, two identical series-RC branches in parallel would approach a nominal combined scale of approximately:

```text
C_total ≈ 20 nF
R_series,equivalent ≈ 50 Ω
```

but the actual branch currents and parasitic placement should be preserved for switching-loss work.

---

## 4. Functional classification — PASSIVE DISSIPATIVE COMMUTATION DAMPING

The verified A↔C branches contain only capacitor/resistor elements on the direct A/C path.

No diode, active switch, auxiliary winding, or explicit regenerative destination is present in these direct A↔C branches.

Therefore the formal classification is:

```text
explicit A↔C RC damping/snubber network
= VERIFIED

energy dissipation in R110/R119
= INTRINSIC DISSIPATIVE COMMUTATION LOSS BUCKET

explicit regenerative energy-recovery path in these A↔C branches
= NOT PRESENT IN THE VERIFIED BRANCH TOPOLOGY
```

Important limitation:

```text
NOT PRESENT IN THIS DIRECT RC BRANCH
≠
proof that every switching transient joule in the whole converter is dissipated only here.
```

Coss, body-diode current, transformer leakage, wiring inductance and other clamp/parasitic paths can still exchange energy during transitions.

---

## 5. Snubber loss must be measured or waveform-derived

The A↔C RC network creates a real A0 loss term:

```text
P_snubber = P_R110 + P_R119 [+ P_R195 if ever populated]
```

Preferred direct waveform calculation:

```text
P_R110 = average( v_R110(t)^2 / 100 Ω )
P_R119 = average( v_R119(t)^2 / 100 Ω )
```

or equivalently:

```text
P_R = average( i_branch(t)^2 R )
```

This avoids assuming a complete capacitor charge/discharge on every switching transition.

A parametric full-step sensitivity may be used only when clearly labelled:

```text
E_C,branch,transition ≈ 0.5 C (ΔV_C)^2
```

For two identical 10 nF branches, if both experience the same complete voltage step:

```text
E_twoBranches,transition ≈ 10 nF × (ΔV_C)^2
```

Total wattage still requires the actual capacitor-voltage step and actual transition rate:

```text
P ≈ E_transition × N_transitions_per_second
```

Do not substitute assumed `2×Vin`, assumed 24/48 V node swing, or guessed switching frequency as A0 evidence.

Formal status:

```text
snubber topology/values = VERIFIED
snubber actual watts     = OPEN / WAVEFORM_NEEDED
```

---

## 6. Research consequence after the manufactured-copper correction

The current non-measured scales are now qualitatively:

```text
positive PCB geometry bound     = material but reduced by >82 µm finished copper
main 20-MOS conduction          = first-order datasheet-scale bucket
battery-interface 7-MOS         = first-order product-interface bucket
A↔C RC snubber/commutation      = structurally verified / watts open
HFT copper/core/leakage          = open
```

Therefore an A1/candidate efficiency claim must not compare only:

```text
RDS(on)
+ transformer core size
```

It must also compare:

```text
P_snubber / P_commutation
```

under the same operating envelope.

A candidate that reduces leakage/overshoot enough to remove or shrink dissipative damping may gain real watts, but the saving is not established until:

```text
P_snubber,A0
>
P_snubber,candidate + any added recovery/control loss
```

---

## 7. U5 upstream dual gate-driver layer — DESIGN INTENT IDENTIFIED

The MAIN SchDoc contains:

```text
U5
Comment = 2EDN7524F
```

and alternative component fields also retain an ADP3654ARDZ option.

The R52 component export independently searches/identifies U5 under the `2EDN7524F` design comment.

Current evidence therefore supports:

```text
R52 design-intent U5 = 2EDN7524F
= SUPPORTED_BY_R52 DESIGN DATA

actual populated U5 production device
= NOT YET BOM/PHYSICAL VERIFIED
```

A Drive search for the internal `ADP3654ARDZ` part number finds it in a different ADP-series BOM. That cross-model BOM is not valid evidence that ASP-2000 R52 populates ADP3654.

Do not use cross-model BOM presence to override R52 design data.

---

## 8. U5 power/reference environment — VERIFIED FROM SCHDOC

U5 local supply/reference:

```text
VDD → 12VP
PGND/reference → SIG/B
```

Local decoupling includes:

```text
C105 = 104 class
C106 = 4.7 µF / 25 V
```

between the driver supply/reference region.

The same MAIN-board signal area contains the already established:

```text
DR-A / DR-A2
DR-B / DR-B2
```

with:

```text
R213 = 0 Ω linking DR-A ↔ DR-A2
R212 = 0 Ω linking DR-B ↔ DR-B2
```

and downstream four local BJT/MOS gate-buffer groups leading to the individual 27.4 Ω main-MOS gate resistors.

Thus the structural hierarchy is now:

```text
control/interface side
↓
U5 dual high-speed driver layer
↓
DR-A / DR-B command-drive region
↓
paired local driver subgroups
   DA1 + DA2
   DB1 + DB2
↓
individual 27.4 Ω gate resistors
↓
20 main MOS
```

However, the exact U5 input/output interpretation must remain conditional until the populated device option and symbol-pin mapping are reconciled.

---

## 9. U5 pin/function ambiguity — DO NOT OVERCLAIM

The SchDoc stores alternative device information for U5, and some symbol pins/net usage are not safe to interpret as one specific manufacturer's pin naming without first locking the populated option.

Therefore do **not** promote any of the following from schematic-name inference alone:

```text
exact U5 channel-A/channel-B polarity
exact enable behavior
exact propagation delay in the product
exact dead time generated by U5
exact DR-A/DR-B source-vs-feedback direction
```

Formal rule:

```text
manufacturer datasheet propagation delay
≠
measured ASP dead time
```

and:

```text
R52 component comment
≠
populated-BOM verification
```

---

## 10. Internal switching frequency / duty / dead time search result

Current Drive search covered terms including:

```text
ASP-2000 / ASP-2000W
ASP program identifiers
switching frequency
PWM
DR-A
ASP control-board terms
```

The available ASP standard specification exposes only the user-visible 50/60 Hz output-frequency specification, not the internal high-frequency X1 switching frequency.

The accessible model/program matrix contains ASP-2000 rows, but the program and transformer fields for those rows are blank in the current file.

Therefore:

```text
A0 internal fs       = OPEN
A0 duty              = OPEN
A0 dead time         = OPEN
A0 exact control law = OPEN
```

No lower-power ASP/VF/UK program identifier may be substituted across models.

---

## 11. Revised dynamic measurement sequence

The first dynamic capture should now include the snubber boundary explicitly.

### S0 — logical switch timing

```text
DR-A vs DR-B
→ fs / period / relative timing
```

Only after the actual U5 population/pin function is verified should internal U5 pins be used as a formal timing boundary.

### S1 — actual main-MOS VGS

At least one representative from each local driver subgroup:

```text
DA1 / DA2 / DB1 / DB2
```

measure Gate-to-own-Source.

### S2 — switched-node voltage

```text
V_A-B(t)
V_C-B(t)
V_A-C(t)
```

### S3 — snubber loss

Measure, if probe safety/bandwidth permits:

```text
v_R110(t)
v_R119(t)
```

then integrate resistor dissipation.

### S4 — transformer current

```text
I_T1(t)
I_T2(t)
```

### S5 — synchronized switching-region power

Use valid voltage/current boundaries and deskewed channels.

---

## 12. Revised A0 loss decomposition around X1

The intrinsic primary/X1 bucket must now include explicitly:

```text
P_A/C_MOS,cond
+ P_A/C_MOS,sw
+ P_gateDriver
+ P_primary,Cu
+ P_core
+ P_leakage/commutation
+ P_A↔C_RC_snubber
```

Do not hide `P_A↔C_RC_snubber` inside an undefined miscellaneous term after its physical network has been verified.

---

## 13. A1 / candidate benchmark rule

A fair optimized magnetic A1 receives permission to optimize:

```text
leakage inductance
commutation strategy
MOS technology/count
local driver distribution
gate resistance
snubber/clamp method
magnetic construction
```

but any claimed saving must close the full balance:

```text
P_saved,mainMOS
+ P_saved,snubber
+ P_saved,magnetic
>
P_added,newSwitching
+ P_added,recovery
+ P_added,driver/control
+ P_added,parasitics
```

This is consistent with the governing rule:

```text
P_saved > P_added
```

---

## 14. Formal status

```text
A/C high-current switched nodes                 = VERIFIED
A↔C RC branch C62+R110                          = VERIFIED
A↔C RC branch R119+C65                          = VERIFIED
C62/C65 nominal capacitance class               = 10 nF / 1 kV / VERIFIED_FROM_DESIGN_DATA
R110/R119                                      = 100 Ω / VERIFIED_FROM_DESIGN_DATA
R195                                           = OPTIONAL POSITION / NC IN DESIGN DATA
explicit RC network classification             = PASSIVE DISSIPATIVE SNUBBER / VERIFIED
actual snubber watts                           = OPEN / WAVEFORM_NEEDED
explicit regenerative element in direct RC path = NOT PRESENT IN VERIFIED BRANCH
U5 dual-driver layer                           = VERIFIED_IN_DESIGN
U5 R52 design comment                          = 2EDN7524F
U5 populated production P/N                    = OPEN / BOM_OR_PHYSICAL_CONFIRMATION_NEEDED
ADP3654 cross-model BOM evidence               = CONTEXT_ONLY / NOT A0
internal switching frequency                   = OPEN
actual duty                                    = OPEN
actual dead time                               = OPEN
A0 measured commutation loss                   = OPEN
A1                                             = BLOCKED_UNTIL_A0_LOSS_LOCALIZATION
Candidate #10                                  = NOT_ASSIGNED
Novelty                                        = NOT_ESTABLISHED
```
