# 34 — H1 / H2 / H3 / H4 Evidence-Acquisition Worksheet v1

Status date: 2026-08-19  
Role: `EXECUTABLE A0 LAB EVIDENCE WORKSHEET / PHYSICAL-GAP VALIDATION`  
Hardware execution status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

This worksheet converts the minimum falsification plan into a lab-executable acquisition record for ASP-2000 R52 A0.

It does **not** authorize energized hardware operation by itself and it does **not** claim any measurement has already been taken.

The worksheet separates:

```text
A. A0-NOW hardware evidence
   = evidence that can be acquired from the real ASP A0 when the actual instrument/probe/access/safety conditions are approved

B. COMPARATOR / MODEL evidence
   = A1 / B / C2 / C3 / X2-P / X2-A evidence acquired later from matched literature, simulation, model, prototype or hardware
```

Current execution priority:

```text
Priority 1 — H2 / PG-2 hard materiality gate
Priority 1 — H4 / PG-4 hard materiality gate
Priority 2 — H1 / PG-1 pre-X1 conduction scale
Priority 3 — H3 / PG-3 total transformation burden
```

This is an information-efficiency order, not a statement that PG-2 or PG-4 is physically more important.

---

## 2. Hard safety and validity boundary

Before any energized capture:

```text
actual A0 input/output rating confirmed
instrument voltage/current/common-mode rating confirmed
probe category/rating confirmed
probe grounding/reference method confirmed
current-probe range and saturation margin confirmed
scope input configuration confirmed
load/source capability confirmed
thermal / ventilation condition confirmed
operator is qualified for the measurement boundary
```

Do not create a ground path from a normal earth-referenced oscilloscope lead into a floating/high-energy switching node.

Use appropriately rated differential / isolated voltage measurement for floating or high-common-mode nodes.

Stop or reconfigure if any of the following occurs:

```text
probe or instrument rating exceeded
unsafe ground/reference path exists
current probe saturates or degauss/zero is invalid
waveform clips or aliases
probe attachment materially changes ringing
V/I deskew is not verified for switching-energy integration
operating point cannot be repeated
thermal condition is not stable enough for the intended comparison
```

If a required measurement is unsafe or physically inaccessible:

```text
status = OPEN / ACCESS_BLOCKED
```

Do not replace it with an assumed value and call it measured evidence.

---

## 3. Evidence-status vocabulary

Use only the following acquisition statuses:

```text
READY
= measurement boundary and required access are identified; hardware measurement may proceed only after actual lab approval/readiness

CONDITIONAL
= valid only if stated access/instrument/rating condition is satisfied

OPEN
= required evidence is not yet available

ACCESS_BLOCKED
= physical/safety/access condition prevents current acquisition

INVALID
= capture exists but violates the required measurement boundary / synchronization / rating / metadata rule
```

Evidence class:

```text
MEASURED
BOUNDED
MODELLED
CONTEXT_ONLY
```

Decision state:

```text
PASS
FAIL
EVIDENCE_INSUFFICIENT
NOT_EVALUATED
```

No PASS/FAIL field is pre-populated in this v1 worksheet.

---

## 4. Pre-measurement declaration sheet — required for every operating point

Complete before interpreting any waveform or watt result.

| Field | Required entry |
|---|---|
| Run ID | TBD |
| Date / time | TBD |
| A0 hardware identity / revision | ASP-2000 R52 / physical unit ID TBD |
| Population / input-voltage variant | MUST VERIFY FROM ACTUAL UNIT |
| Vin | TBD |
| Vout | TBD |
| Pout real power | TBD |
| Load / PF | TBD |
| Output line frequency | 50 or 60 Hz — measured/declared |
| Ambient temperature | TBD |
| MOS / heatsink temperature | TBD |
| T1 temperature | TBD |
| T2 temperature | TBD |
| Time after thermal stabilization | TBD |
| DC source / battery source | TBD |
| Load instrument / load bank | TBD |
| Oscilloscope model / bandwidth | TBD |
| Scope sample rate / record length | TBD |
| Voltage probe type / ratio / bandwidth | TBD |
| Current probe type / range / bandwidth | TBD |
| Differential/common-mode rating | TBD |
| Probe deskew method / result | TBD |
| Current probe zero/degauss state | TBD |
| Raw file names | TBD |
| Operator | TBD |

Hard rule:

```text
missing operating-point / probe / bandwidth / deskew metadata
→ waveform-derived switching loss cannot be benchmark-grade evidence
→ evidence class limited to CONTEXT_ONLY or EVIDENCE_INSUFFICIENT
```

---

## 5. Operating-point ladder

Do not jump directly to the research anchor without verifying the actual unit rating and measurement integrity.

### OP-0 — de-energized setup

Purpose:

```text
identify probe points
verify polarity/reference
configure current-probe direction
perform deskew/zero procedures
verify no unsafe ground path
```

No converter-loss conclusion is allowed from OP-0.

### OP-1 — controlled low-energy functional check

Purpose:

```text
confirm signal polarity
confirm channel scaling
confirm trigger / timing
confirm probes do not saturate or clip
confirm capture is physically plausible
```

Exact power is not prescribed here; it must remain within the actual unit and lab-approved safe setup.

### OP-A — research anchor

Target research condition:

```text
Vin = 12 V
Pout = 2 kW
Vout = 220 Vac / 1φ
```

Use OP-A only if the actual A0 unit/population is verified to support this operating point and all source/load/probe ratings are adequate.

Do **not** operate a 2 kW A0 beyond its verified product rating merely to cover the broader 1–3 kW research envelope.

### OP-R — repeat point

Repeat the same declared operating point after the full capture sequence to test repeatability / drift.

Record:

```text
ΔVin
ΔPout
Δtemperature
Δkey RMS / loss result
```

If repeatability is poor, do not promote a small difference into a Physical Gap result.

---

## 6. Raw-data naming and traceability

Recommended record identifier:

```text
A0_<YYYYMMDD>_<RunID>_<OP>_<H#>_<SignalID>
```

Example only:

```text
A0_20260819_R01_OPA_H2_VAB
```

For every processed scalar, retain a reference to:

```text
raw waveform file
processing method / script / scope math
probe scale
filter/bandwidth limit if applied
window used
uncertainty source
```

A scalar without source-waveform traceability is not sufficient for final verification.

---

# 7. H2 / PG-2 — commutation and dissipative-snubber hard gate

## 7.1 Objective

Determine whether the avoidable primary commutation burden is materially large enough to justify further PM-4 soft-commutation research.

Primary output:

```text
P_comm,avoidable
= P_snubber
+ avoidable P_switching,transition
+ separately identifiable unrecovered leakage/Coss dissipation
```

Do not count the same transition energy twice.

## 7.2 H2 acquisition table

| ID | Quantity | A0 measurement boundary / point | Instrument / probe class | Synchronization / bandwidth rule | Operating point | Calculation / output | Uncertainty / validity | Status |
|---|---|---|---|---|---|---|---|---|
| H2-00 | Probe deskew | voltage probe vs current probe path used for power integration | scope deskew fixture/method appropriate to actual probes | MUST be verified before V×I integration | OP-0 / OP-1 | deskew offset / residual | if unresolved → switching power INVALID | OPEN |
| H2-01 | DR-A / DR-B timing | control-drive region only | voltage probes appropriate to local logic reference | common timebase | OP-1 then OP-A | fs, period, relative timing | not a substitute for actual device VGS | OPEN |
| H2-02 | DA1-G / B | DA1 gate bus relative local B/source reference | isolated/differential or safe local probe | common timebase | OP-1 / OP-A | edge timing / ringing | reference must be local source/B, not arbitrary BAT- | OPEN |
| H2-03 | DA2-G / B | DA2 gate bus relative local B/source reference | same class as H2-02 | synchronized H2-02 | OP-1 / OP-A | DA1↔DA2 mismatch | — | OPEN |
| H2-04 | DB1-G / B | DB1 gate bus relative local B/source reference | same class | common timebase | OP-1 / OP-A | edge timing / ringing | — | OPEN |
| H2-05 | DB2-G / B | DB2 gate bus relative local B/source reference | same class | synchronized H2-04 | OP-1 / OP-A | DB1↔DB2 mismatch | — | OPEN |
| H2-06 | Representative actual VGS | Q3, Q18, Q11, Q24 Gate-to-own-Source | appropriately rated isolated/differential probing | high enough BW to resolve edges/Miller region | OP-1 / OP-A | VGS,on/off, plateau, overshoot, dead-time interpretation | do not infer product timing from driver datasheet alone | OPEN |
| H2-07 | V_A-B(t) | A = NetC62_1 to B | rated differential/isolated voltage probe | common timebase with current | OP-1 / OP-A | switched-node voltage, overshoot/ringing | unsafe earth reference → INVALID | OPEN |
| H2-08 | V_C-B(t) | C = NetC65_1 to B | rated differential/isolated voltage probe | common timebase with current | OP-1 / OP-A | switched-node voltage, overshoot/ringing | unsafe earth reference → INVALID | OPEN |
| H2-09 | I_T1(t) | actual T1 center-tap / winding-feed lead after local-bulk ambiguity if accessible | current probe with adequate peak/BW | common timebase with H2-07/08 | OP-1 / OP-A | Iavg, IRMS, peak, commutation spike | probe saturation → INVALID | OPEN |
| H2-10 | I_T2(t) | actual T2 center-tap / winding-feed lead after local-bulk ambiguity if accessible | same class | common timebase with H2-07/08 | OP-1 / OP-A | Iavg, IRMS, peak, imbalance | — | OPEN |
| H2-11 | v_R110(t) | directly across R110 if probe access/rating permit | differential/isolated voltage probe | bandwidth sufficient for snubber waveform | OP-A | `P_R110 = avg(v_R110²/100Ω)` | probe loading / BW recorded | OPEN |
| H2-12 | v_R119(t) | directly across R119 if probe access/rating permit | same class | common timebase preferred | OP-A | `P_R119 = avg(v_R119²/100Ω)` | — | OPEN |
| H2-13 | P_snubber | derived from H2-11/12 | processing | same acquisition basis | OP-A | `P_snubber=P_R110+P_R119` | R tolerance + waveform uncertainty | OPEN |
| H2-14 | A/C bank switching-region energy | A and C voltage with valid corresponding total-current boundary | synchronized voltage + current probes | deskew mandatory | OP-A | integrate transition windows / average region power | wrong-current or poor deskew → INVALID | OPEN |
| H2-15 | P_comm,avoidable bound | aggregate non-double-counted H2 result | analysis | matched boundary | OP-A | watts / bound | document unresolved terms | OPEN |

## 7.3 Current-boundary rule for H2

The real A0 power stage has:

```text
A logical switch = 10 parallel MOS
C logical switch = 10 parallel MOS
```

not four independent five-MOS power branches.

During stable conduction, first-order electrical boundaries are:

```text
i_A,total ≈ i_T1,A + i_T2,A

i_C,total ≈ i_T1,C + i_T2,C
```

During dead time / transition:

```text
Coss
body diode
leakage inductance
snubber
parasitic capacitance
ringing loops
```

may carry additional current. Therefore stable current summation must not be blindly applied to transition-energy integration.

If a trustworthy high-bandwidth A/C total-current reconstruction is not available:

```text
P_switching,transition = OPEN / BOUNDED ONLY
```

rather than forcing a false scalar.

## 7.4 H2 decision sheet

Predeclare before final interpretation:

```text
T_mat,PG2 = __________________ W
justification = ______________________________________
uncertainty floor = __________________ W
```

Calculated result:

```text
P_snubber              = __________ W / bound
P_switching,transition = __________ W / bound
P_comm,avoidable       = __________ W / bound
U_H2                    = __________ W
P_comm,avoidable,low   = __________ W
```

Decision:

```text
IF P_comm,avoidable,low <= T_mat,PG2
→ PG-2 = MATERIALITY_FAIL
→ PM-4 research direction CLOSED

ELSE
→ PG-2 may proceed to A1-S / PM-4 fair falsification
```

Final field:

```text
H2 decision = NOT_EVALUATED / PASS / FAIL / EVIDENCE_INSUFFICIENT
```

---

# 8. H4 / PG-4 — source-side 2ω hard gate

## 8.1 Objective

Determine whether material single-phase twice-line-frequency power/current remains at the low-voltage source **after** the existing HV-link passive buffering is already doing its job.

Primary quantities:

```text
I_2ω,source
P_2ω,source
I_source,rms
HV-link ΔV_2ω
E_2ω,buffer
```

## 8.2 H4 acquisition table

| ID | Quantity | A0 measurement boundary / point | Instrument / probe class | Window / synchronization rule | Operating point | Calculation / output | Uncertainty / validity | Status |
|---|---|---|---|---|---|---|---|---|
| H4-01 | I_source(t) | source/battery input current at declared converter boundary | DC-capable current probe / current transducer with adequate accuracy at DC and 100/120 Hz | capture enough stable line cycles to resolve 2f_line and repeatability; target multi-cycle record, not one switching window | OP-A | Iavg, IRMS, spectrum / fitted 2f component | zero drift and gain accuracy recorded | OPEN |
| H4-02 | V_source(t) | declared input boundary | appropriate differential/isolated voltage measurement | synchronized H4-01 where input power decomposition is used | OP-A | Vavg / ripple context | — | OPEN |
| H4-03 | V_HVlink(t) | BUS+ to BUS- | appropriately rated HV differential/isolated probe | synchronized to H4-01 and line cycle | OP-A | Vavg, ΔV_2ω, phase | probe/common-mode rating mandatory | OPEN |
| H4-04 | Vout(t) | AC output | rated differential/isolated probe or power analyzer | synchronized output power context | OP-A | line frequency / waveform | — | OPEN |
| H4-05 | Iout(t) | AC output current | current probe / power analyzer | synchronized H4-04 | OP-A | Pout real power / PF | — | OPEN |
| H4-06 | I_2ω,source | derived H4-01 | FFT / sinusoidal fit / narrowband extraction with declared convention | same stable record | OP-A | RMS magnitude at `2 f_line` | processing window / leakage documented | OPEN |
| H4-07 | incremental source RMS from 2ω | derived | analysis | same record | OP-A | distinguish DC + low-frequency component + HF ripple | orthogonal-component assumption documented | OPEN |
| H4-08 | HV-link energy swing | H4-03 plus verified actual `C_eq,HV` when available | analysis | line-synchronous | OP-A | `E_C(t)=0.5 C_eq V_HVlink(t)^2` | if actual C_eq population/tolerance not verified → BOUNDED/OPEN | OPEN |
| H4-09 | incremental LV I²R impact | H4-06 + matched source-domain equivalent resistance/bound | analysis | same contract as PG-1 | OP-A | `ΔP_LV,2ω ≈ I_2ω,rms² R_eq,LV` where valid | do not use unknown R_eq as exact scalar | OPEN |

## 8.3 H4 processing convention

For this project, `I_2ω,source` must explicitly state whether it is:

```text
RMS magnitude of the 2f_line sinusoidal component
or
peak amplitude
```

Preferred reporting is RMS so that conduction impact can be compared directly with RMS-based loss accounting.

Use actual measured line frequency:

```text
50 Hz output → examine 100 Hz
60 Hz output → examine 120 Hz
```

Do not hard-code 100 Hz when the unit is running at 60 Hz, or vice versa.

## 8.4 Existing passive-buffer first falsifier

The ASP already has an HV DC-link. Therefore the first question is **not** whether an active buffer can be designed.

The first question is:

```text
After the existing passive HV link,
is source-side 2ω still material?
```

Predeclare:

```text
T_mat,PG4 = __________________ [W and/or declared source-RMS impact metric]
justification = ______________________________________
uncertainty floor = __________________
```

Result:

```text
I_2ω,source             = __________ Arms
P_2ω,source / impact    = __________ W / bound
ΔP_LV,2ω                = __________ W / bound
U_H4                     = __________
```

Decision:

```text
IF source-side 2ω burden is not material above T_mat,PG4
→ PG-4 = MATERIALITY_FAIL
→ active X2 CLOSED

ELSE
→ authorize later X2-P vs X2-A comparison
```

Final field:

```text
H4 decision = NOT_EVALUATED / PASS / FAIL / EVIDENCE_INSUFFICIENT
```

---

# 9. H1 / PG-1 — pre-X1 source-domain conduction scale

## 9.1 Objective

Quantify or conservatively bound how much conduction/RMS loss is carried before X1 has moved majority main-path power into a sustained reduced-current domain.

Primary quantity:

```text
P_preX1,cond
≈ Σ(I_rms,k² R_eff,k)
 + Σ(P_semiconductor,cond,k)
```

Product-interface loss must remain separate unless Contract P is used on all compared architectures.

## 9.2 H1 acquisition table

| ID | Quantity | A0 measurement boundary / point | Instrument / probe class | Timing / thermal rule | Operating point | Calculation / output | Uncertainty / validity | Status |
|---|---|---|---|---|---|---|---|---|
| H1-01 | I_source avg/RMS | source input boundary | DC current probe / transducer | stable thermal condition | OP-A | Iavg / IRMS | zero/gain uncertainty | OPEN |
| H1-02 | M0 BAT+ common drops | BAT+ terminal → each fuse input as applicable | Kelvin/mV differential measurement | same current/load condition | OP-A | multi-terminal `P_BAT+=Σ I_k ΔV_k` where branch currents known | do not use one arbitrary fuse drop | OPEN |
| H1-03 | M1 fuse drops | each main fuse input → output | Kelvin/mV differential measurement | same condition | OP-A | `P=I ΔV` per branch | branch current required/bounded | OPEN |
| H1-04 | M2 T1 local feed drop | T1 fuse-output node → T1 center tap | Kelvin/mV differential measurement | thermal steady state | OP-A | R / P segment | boundary must exclude unrelated path | OPEN |
| H1-05 | M3 J8 drop | J8 left → J8 right external link | Kelvin/mV differential measurement | thermal steady state | OP-A | R_J8 / P_J8 | actual conductor/access required | OPEN |
| H1-06 | M4 T2 local feed drop | J8 right → T2 center tap | Kelvin/mV differential measurement | thermal steady state | OP-A | R / P segment | — | OPEN |
| H1-07 | M5 B↔BAT- bank drop | B to BAT- seven-MOS interface | Kelvin/mV differential measurement | record MOS temperature + 12VP | OP-A | `P_batteryInterface=I_source ΔV(B↔BAT-)` | classify separately under Contract C | OPEN |
| H1-08 | B-return copper | accessible B-return distribution segment | Kelvin/mV differential measurement | same load | OP-A | P / R | only if separable | OPEN |
| H1-09 | T1 RMS current | actual T1 center-tap/winding feed | current probe | same thermal/load condition | OP-A | IRMS | access conditional | OPEN |
| H1-10 | T2 RMS current | actual T2 center-tap/winding feed | current probe | same thermal/load condition | OP-A | IRMS | access conditional | OPEN |
| H1-11 | A-bank on-state VDS / equivalent | A-to-B during stable A conduction or valid hot R_eff boundary | Kelvin-grade low-voltage differential / synchronized waveform or bounded hot-RDS method | stable conduction window; avoid transition intervals | OP-A | conduction loss/bound | mV measurement noise may dominate; document method | OPEN |
| H1-12 | C-bank on-state VDS / equivalent | C-to-B during stable C conduction | same | stable conduction window | OP-A | conduction loss/bound | — | OPEN |
| H1-13 | MOS / heatsink temp | representative main MOS thermal location | calibrated temperature method | same stabilized run | OP-A | hot-condition context | sensor placement recorded | OPEN |
| H1-14 | P_preX1,cond,A0 | aggregate intrinsic source-domain terms | analysis | same contract | OP-A | W / conservative bound | unresolved terms retained in U_H1 | OPEN |

## 9.3 H1 loss-contract split

Maintain both when useful:

```text
Contract C — core converter
exclude battery-interface reverse-protection/sensing overhead equally from all sides

Contract P — product level
include matched protection/sensing/precharge functions on all compared sides
```

Do not let the candidate win by deleting A0 product functionality.

## 9.4 H1 decision sheet

Predeclare:

```text
T_mat,PG1 = __________________ W
justification = ______________________________________
uncertainty floor = __________________ W
```

Result:

```text
P_preX1,cond,A0 = __________ W / bound
U_H1             = __________ W
P_preX1,low      = __________ W
```

Decision sequence:

```text
IF P_preX1,low <= T_mat,PG1
→ PG-1 = MATERIALITY_FAIL

ELSE
→ compare against fair optimized A1 PM-1

IF A1 reduces the burden below materiality
→ PG-1 = FAIR_FALSIFIER_FAIL

ELSE
→ compare PM-2 C2 and PM-3 C3 under matched total-loss accounting
```

Final field:

```text
H1 decision = NOT_EVALUATED / PASS / FAIL / EVIDENCE_INSUFFICIENT
```

---

# 10. H3 / PG-3 — total transformation-burden evidence

## 10.1 Objective

Determine whether there is a material total transformation burden at the extreme voltage/current ratio and compare PM-1 / PM-2 / PM-3 symmetrically.

PG-3 is deliberately mechanism-neutral.

Do not begin from:

```text
"transformer is large"
```

Begin from:

```text
What total watts are required to move the same through-power
from the source-domain into a comparable reduced-current domain?
```

## 10.2 A0 / PM-1 acquisition table

| ID | Quantity | A0 measurement boundary / point | Instrument / method | Timing / sync rule | Operating point | Calculation / output | Uncertainty / validity | Status |
|---|---|---|---|---|---|---|---|---|
| H3-01 | I_T1(t) | actual T1 center-tap/winding feed | current probe | same run as relevant primary voltage if possible | OP-A | RMS / peak / waveform | — | OPEN |
| H3-02 | I_T2(t) | actual T2 center-tap/winding feed | current probe | same | OP-A | RMS / peak / imbalance | — | OPEN |
| H3-03 | T1 primary voltage | actual half-primary boundary | rated differential/isolated voltage probe | synchronized with current | OP-A | volt-second `∫Vdt` | winding boundary explicit | OPEN |
| H3-04 | T2 primary voltage | actual half-primary boundary | rated differential/isolated voltage probe | synchronized | OP-A | volt-second `∫Vdt` | — | OPEN |
| H3-05 | T1/T2 temperature | transformer body/core/winding-accessible thermal points | calibrated thermal method | after declared stabilization | OP-A | temperature rise/context | placement recorded | OPEN |
| H3-06 | Actual turns ratio | physical unit / approved A0 transformer evidence | measurement or direct approved data | de-energized where applicable | N/A | ratio | context-only other PQ50 sheets prohibited | OPEN |
| H3-07 | winding DCR | actual A0 transformer winding | appropriate low-resistance method | de-energized / temperature recorded | N/A | Rdc(T) | — | OPEN |
| H3-08 | winding Rac | actual A0 transformer / frequency-aware extraction | impedance/network/loss method appropriate to winding | declared frequency/temp | N/A/OP-A model | Rac(f,T) / bound | method required | OPEN |
| H3-09 | Lm / Lk | actual A0 transformer | appropriate impedance/LCR/network method | de-energized test conditions declared | N/A | Lm/Lk | test frequency/amplitude recorded | OPEN |
| H3-10 | core material / Ae / Ve | actual A0 transformer evidence | approved drawing/data or physical characterization | N/A | N/A | magnetic model inputs | do not infer from PQ5050 outline alone | OPEN |
| H3-11 | PM-1 transformation burden | declared X1 boundary | staged electrical/model/calorimetric closure | matched boundary | OP-A | `P_TR,PM1` / bound | unresolved core/copper terms explicit | OPEN |

If exact A0 transformer parameters cannot be established:

```text
report bounded PM-1 burden
or
H3 = EVIDENCE_INSUFFICIENT
```

Do not substitute `M1-PQ50-V108-A` or `M1-PQ50-V121-A` values as A0 numerical evidence without direct linkage.

## 10.3 H3 comparator evidence — later, not A0-now

| Comparator | Dominant PM | Required matched outputs | Must expose |
|---|---|---|---|
| A1 | PM-1 | P_TR, X1 completion boundary, M1-M7 | copper/core/leakage/magnetizing + switching/rectification support |
| C2 | PM-2 | P_TR, X1 completion boundary, M1-M7 | inductor copper/core, switch loss, ripple/peak/circulation |
| C3 | PM-3 | P_TR, X1 completion boundary, M1-M7 | capacitor ESR/RMS, charge redistribution, switch path, balancing/precharge |
| B | architecture-level Direct HFL | total matched architecture loss only after internal PM decomposition | actual X1/X2/X3 mechanisms; stage deletion alone not credited |

All three primary transformation mechanisms must terminate at a comparable reduced-current / voltage-domain boundary.

## 10.4 H3 decision sheet

Predeclare:

```text
T_mat,PG3 = __________________ W / declared transformation-burden metric
justification = ______________________________________
uncertainty floor = __________________
```

Results:

```text
P_TR,PM1 = __________ W / bound
P_TR,PM2 = __________ W / bound
P_TR,PM3 = __________ W / bound
```

Decision:

```text
boundary mismatch
→ EVIDENCE_INSUFFICIENT

no material difference above uncertainty / T_mat,PG3
→ MATERIALITY_FAIL

optimized PM-1 not materially worse than alternatives
→ reject claim that magnetic transformation itself is the gap

one alternative has robust lower total transformation burden
→ PG-3 survives mechanism-level falsification
```

Final field:

```text
H3 decision = NOT_EVALUATED / PASS / FAIL / EVIDENCE_INSUFFICIENT
```

---

# 11. Comparator / model evidence worksheet — later phase

The following is intentionally separated from A0-now measurement.

| Comparator role | Activation condition | Evidence source allowed | Required quantities | Current status |
|---|---|---|---|---|
| A1 PM-1 magnetic | H1/H3 comparison requires fair PM-1 falsifier | matched paper/model/PLECS/prototype/hardware | P_preX1, P_TR, M1-M7, full support loss | NOT YET ACQUIRED |
| A1-S PM-1 commutation-optimized | H2 materiality survives | matched paper/model/prototype/hardware | P_comm, added resonant/driver/circulation loss | NOT YET ACQUIRED |
| C2 PM-2 | PG-1/PG-3 survives to alternative comparison | matched paper/model/prototype/hardware | full PM-2 transformation ledger | NOT YET ACQUIRED |
| C3 PM-3 | PG-1/PG-3 survives to alternative comparison | matched paper/model/prototype/hardware | full PM-3 transformation ledger | NOT YET ACQUIRED |
| X2-P PM-5 | H4 survives | matched passive-buffer model/hardware | passive buffer loss/energy/volume/ripple | CLOSED UNTIL H4 |
| X2-A PM-6 | H4 survives | matched active-buffer model/hardware | saved LV loss + full active-buffer added loss | CLOSED UNTIL H4 |
| B Direct HFL | architecture integration comparison becomes relevant | matched paper/model/prototype/hardware | decomposed PMs + full total-loss boundary | NOT YET ACQUIRED |

No literature efficiency number may be directly ranked unless it passes the existing comparison contract.

---

# 12. Uncertainty worksheet

Every H1-H4 scalar should list the dominant uncertainty contributors.

## 12.1 Typical entries

```text
voltage-probe gain / offset
current-probe gain / offset / zero drift
scope ADC / noise / bandwidth
probe bandwidth / loading
V/I timing skew
resistor tolerance / temperature
current-path allocation uncertainty
thermal drift / run-to-run drift
filter/window/FFT processing choice
model parameter range
```

For independent uncertainty sources, an RSS form may be used when justified:

```text
U_total = sqrt(U1² + U2² + ...)
```

If independence is not defensible, use a conservative bounded combination instead of forcing RSS.

For H2 switching energy, timing skew deserves its own explicit uncertainty entry because a small V/I offset can create a large false switching-energy result.

For H4 low-frequency extraction, record the analysis window and spectral leakage / fit residual.

---

# 13. Repeatability gate

At least one key operating point used for a PG decision must be repeated after the acquisition sequence.

Compare:

```text
I_source,rms
Pout
key temperatures
H2 P_snubber / P_comm bound where applicable
H4 I_2ω,source
H1 P_preX1 bound
```

If the between-run spread is comparable to the claimed architecture-relevant saving:

```text
result = EVIDENCE_INSUFFICIENT
```

until the repeatability problem is resolved or incorporated into uncertainty.

---

# 14. Lab execution order v1

Recommended acquisition order after actual hardware-readiness approval:

```text
L0 — OP-0 de-energized point identification / probe ratings / current-probe direction
↓
L1 — probe zero + deskew + OP-1 low-energy waveform sanity check
↓
L2 — H2 timing / switched-node / snubber capture
↓
L3 — H4 line-cycle source-current + HV-link capture
↓
L4 — H1 Kelvin / hot-conduction / temperature capture
↓
L5 — H3 transformer current / volt-second / thermal evidence
↓
L6 — OP-R repeat capture
↓
L7 — uncertainty + materiality decision
```

Reason:

```text
H2/H4 can close entire research branches earliest
H1 establishes the central extreme-LV conduction scale
H3 is parameter-heavy and should not delay hard-gate evidence
```

---

# 15. Decision summary sheet

Fill only after evidence acquisition and predeclared thresholds are locked.

| PG | Main acquired burden | Threshold | Lower bound / robust quantity | Materiality | Fair falsifier status | Net-benefit status | Final state |
|---|---:|---:|---:|---|---|---|---|
| PG-1 | TBD | T_mat,PG1 = TBD | TBD | NOT_EVALUATED | A1 TBD | C2/C3 TBD | HYPOTHESIS |
| PG-2 | TBD | T_mat,PG2 = TBD | TBD | NOT_EVALUATED | A1-S/PM-4 TBD | TBD | HYPOTHESIS |
| PG-3 | TBD | T_mat,PG3 = TBD | TBD | NOT_EVALUATED | A1/C2/C3 TBD | TBD | OPEN |
| PG-4 | TBD | T_mat,PG4 = TBD | TBD | NOT_EVALUATED | existing PM-5 first | X2-P/X2-A CLOSED | HYPOTHESIS |

No row may be upgraded to `VERIFIED PHYSICAL GAP` from this worksheet alone. Formal G1-G6 promotion gates still apply.

---

# 16. Handoff into future Combination Loss Audit

If and only if a PG survives its evidence/falsification gate:

```text
surviving PG
↓
select minimum necessary mechanism set
↓
define actual electrical graph
↓
research/33_COMBINATION_LOSS_AUDIT_GATE.md
↓
CALG-0...CALG-12
↓
matched total-loss advantage
```

The H1-H4 worksheet does not authorize mechanism stacking.

A candidate that later emerges must carry forward:

```text
measured/bounded A0 loss term it claims to remove
uncertainty
comparison contract
M1-M7 baseline
```

so that a claimed saving is not detached from the evidence that originally established the PG.

---

# 17. Formal status after worksheet creation

```text
Executable H1/H2/H3/H4 worksheet      = ESTABLISHED v1
A0 hardware measurements              = NOT EXECUTED
H2 acquisition definition             = READY_BY_PROTOCOL / HARD-GATE PRIORITY
H4 acquisition definition             = READY_BY_PROTOCOL / HARD-GATE PRIORITY
H1 acquisition definition             = READY_BY_PROTOCOL
H3 acquisition definition             = READY_BY_PROTOCOL / PARAMETER-DEPENDENT
T_mat,PG1...PG4 numerical values       = OPEN / MUST BE PREDECLARED BEFORE INTERPRETATION
instrument/probe actual capability     = OPEN / LAB READINESS NEEDED
hardware rating/access approval        = OPEN / LAB READINESS NEEDED
comparator evidence A1/B/C2/C3         = NOT YET ACQUIRED
X2-P/X2-A                              = CLOSED UNTIL H4 SURVIVES
mechanism combination                  = NOT EXECUTED
Combination Loss Audit execution       = NOT AUTHORIZED BEFORE PG SURVIVAL
Candidate #10                          = HOLD / NOT_ASSIGNED
Novelty                                = NOT_ESTABLISHED
```

Next valid action:

```text
H2/H4 PRE-MEASUREMENT READINESS GATE
↓
predeclare T_mat,PG2 and T_mat,PG4
confirm actual A0 unit rating / population
confirm available probe/instrument ratings and bandwidth
confirm physical access to A/B/C, R110/R119, source current and HV-link
confirm deskew / current-probe zero procedure
↓
ONLY THEN execute energized H2/H4 hardware acquisition
```
