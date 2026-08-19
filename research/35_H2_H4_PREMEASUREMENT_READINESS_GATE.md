# 35 — H2 / H4 Pre-Measurement Readiness Gate v1

Status date: 2026-08-20  
Role: `PRE-MEASUREMENT READINESS / PHYSICAL-GAP VALIDATION`  
Hardware execution status: `NOT EXECUTED`  
Energized-measurement authorization: `NOT GRANTED BY THIS FILE`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

This gate sits immediately after:

```text
research/34_H1_H2_H3_H4_EVIDENCE_ACQUISITION_WORKSHEET.md
```

and immediately before any energized H2 / H4 acquisition.

Its purpose is not to measure A0 and not to promote PG-2 or PG-4. It determines whether the real ASP-2000 A0, the actual laboratory measurement chain, the physical probe access and the predeclared materiality rule are sufficiently closed to permit a valid future measurement.

Current priority remains:

```text
H2 / PG-2 — commutation / dissipative-snubber materiality
H4 / PG-4 — source-side 2ω materiality
```

This file distinguishes:

```text
PROTOCOL READY
≠
LAB READY
≠
ENERGIZED HARDWARE AUTHORIZED
```

---

## 2. Governance boundary

This stage is a formal engineering-research readiness gate.

Hard rules:

```text
simulation / surrogate model ≠ hardware evidence
product-family specification ≠ physical-unit population verification
instrument availability by memory ≠ instrument rating verification
known schematic node ≠ confirmed safe physical probe access
```

No energized measurement is authorized until every mandatory item below is closed.

Unsafe, inaccessible or unverified measurements remain:

```text
OPEN
ACCESS_BLOCKED
UNSAFE
```

They must not be replaced by guessed values.

---

## 3. A0 product / physical-unit readiness

### 3.1 Product-family evidence found

Google Drive source:

```text
ASP standard spec 251023.pdf
Drive file ID: 1B3qSTDFgiv6_ExdLzDZ-WePQ9xpGbu9D
```

The family specification establishes:

```text
ASP-2000 rated output power = 2000 W
output-voltage options include 200 / 220 / 230 / 240 Vac
output frequency = 50 / 60 Hz
12 V nominal input family range = 10–17.2 Vdc
24 V nominal input family range = 20–34.4 Vdc
48 V nominal input family range = 40–68.8 Vdc
```

It also establishes input reverse-polarity protection at product-function level.

### 3.2 What the family specification does NOT establish

The Drive specification does not identify the exact physical A0 unit currently available for measurement.

Still required from the actual unit:

```text
physical unit ID / serial or unambiguous bench identifier
R52 linkage / revision confirmation
actual input-voltage population: 12 V / 24 V / 48 V
actual output-voltage setting / population
actual 50 / 60 Hz setting
actual fuse / populated-power-stage variant if relevant
condition / repair status / modifications if any
```

Therefore:

```text
ASP-2000 family 2 kW rating        = VERIFIED
12 V ASP family option             = VERIFIED
220 Vac ASP family option          = VERIFIED
physical A0 unit = 12 V population = OPEN
physical A0 unit = OP-A eligible   = OPEN
```

### 3.3 OP-A consequence

The project research anchor remains:

```text
Vin  = 12 V
Pout = 2 kW
Vout = 220 Vac / 1φ
```

But OP-A must not be applied to the physical unit until its actual 12 V / 2 kW / 220 Vac eligibility is verified.

---

## 4. Materiality predeclaration — rule established, numerical value NOT YET defensible

The project explicitly rejects arbitrary universal 5% / 10% materiality thresholds.

The 20 W LV-conduction budget remains a reference scale only; it is not automatically `T_mat`.

A valid numerical materiality threshold must satisfy all of the following before the first final H2/H4 interpretation:

```text
1. tied to the declared 12 V / 2 kW decision boundary
2. above the measurement / processing uncertainty floor
3. large enough to change architecture / thermal / mechanism-selection decisions
4. fixed before interpreting the final A0 H2/H4 result
5. applied identically to compared alternatives
6. not selected after seeing the measured result
```

### 4.1 PG-2 materiality rule

Decision quantity:

```text
B_PG2 = P_comm,avoidable
```

where the non-double-counted boundary is:

```text
P_comm,avoidable
= P_snubber
+ avoidable switching-transition dissipation
+ separately identifiable unrecovered leakage / Coss dissipation
```

Predeclared threshold form:

```text
T_mat,PG2 = max(U_H2, T_arch,PG2)
```

where:

```text
U_H2
= conservative watt-equivalent uncertainty floor of the actual synchronized H2 measurement / integration chain

T_arch,PG2
= minimum avoidable commutation burden that is large enough to justify changing the X1 commutation mechanism under the 12 V / 2 kW project boundary
```

For a later PM-4 solution to survive, materiality alone is not enough. It must still pass:

```text
P_saved,commutation,low
>
P_added,PM4,high
```

including resonant / circulating RMS, extra magnetic loss, device loss, gate/control and support burden.

Current numerical status:

```text
U_H2 numerical value        = OPEN
T_arch,PG2 numerical value  = OPEN
T_mat,PG2 numerical value   = OPEN
```

Reason:

```text
actual voltage/current probes, bandwidth, deskew residual, range and integration uncertainty are not yet known;
a numerical threshold would therefore be invented rather than predeclared from a defensible measurement/decision basis.
```

### 4.2 PG-4 materiality rule

PG-4 must not use HV-link ripple amplitude alone as its materiality quantity.

Primary source-domain decision quantities are:

```text
I_2ω,source
ΔI_source,rms attributable to 2ω
ΔP_LV,2ω attributable to 2ω
```

Preferred loss-domain quantity where a defensible LV resistance/bound exists:

```text
ΔP_LV,2ω ≈ I_2ω,rms² · R_eq,LV
```

Predeclared threshold form:

```text
T_mat,PG4 = max(U_H4→loss, T_arch,PG4)
```

where:

```text
U_H4→loss
= conservative watt-equivalent uncertainty from source-current LF accuracy / zero drift / spectral extraction / R_eq,LV uncertainty

T_arch,PG4
= minimum source-domain 2ω loss / thermal burden large enough to justify adding or relocating a dedicated X2 energy path
```

Any later active X2 / PM-6 proposal must still satisfy:

```text
P_LV,saved,low
>
P_X2,added,high
```

Current numerical status:

```text
U_H4→loss numerical value   = OPEN
T_arch,PG4 numerical value  = OPEN
T_mat,PG4 numerical value   = OPEN
```

Reason:

```text
actual DC-current measurement accuracy / drift, source-domain resistance bound and minimum credible added X2 burden are not yet closed.
```

### 4.3 Surrogate-simulation boundary

Any prior A0 surrogate sensitivity sweep is classified only as:

```text
MODELLED / SCREENING
```

It may identify sensitive variables such as:

```text
fs
dead time
ΔV_AC
edge current
Cdc
2ω reflection ratio
```

but it must not be used to choose `T_mat` retrospectively from the simulated output and must not be promoted to A0 hardware evidence.

---

## 5. H2 laboratory-readiness inventory

Drive searches performed for the current lab context included:

```text
ASP-2000 + oscilloscope / probe
oscilloscope
current probe
isolated probe
differential probe
oscilloscope model
```

No usable record was found that ties an exact oscilloscope / differential probe / isolated probe / current probe model and rating to the present A0 H2 measurement chain.

Generic references to an oscilloscope in unrelated project material are not sufficient.

### 5.1 Required H2 chain

| H2 function | Minimum capability that must be verified | Current status |
|---|---|---|
| Oscilloscope | exact model, analog BW, sample rate, record length, input configuration | `OPEN` |
| A/B/C switched-node voltage | rated differential / isolated probe; differential + common-mode limits; BW; ratio | `OPEN` |
| Actual MOS VGS | safe Gate-to-own-Source probe method, sufficient edge/Miller BW | `OPEN` |
| R110 / R119 voltage | differential/isolated probe with adequate BW and safe floating-node rating | `OPEN` |
| T1/T2 or valid A/C current | current probe/transducer with adequate DC/AC peak range, BW and saturation margin | `OPEN` |
| V×I integration | verified channel synchronization and V/I deskew | `OPEN` |
| Current-probe preparation | zero / degauss procedure and residual-zero record | `OPEN` |
| Trigger / timebase | common timebase across required voltage/current channels | `OPEN` |

### 5.2 H2 parameter-specific readiness

The electrical measurement points are already defined by file 34:

```text
A = NetC62_1
C = NetC65_1
B = common source/return
representative MOS = Q3 / Q18 / Q11 / Q24
snubber resistors = R110 / R119
```

However electrical identification is not enough. Required bench confirmations are still:

```text
probe-tip access
safe local return / differential reference
creepage / clearance during attachment
mechanical probe retention
probe-loading acceptability
current-probe physical aperture / conductor access
```

Current H2 access status:

```text
A/B/C electrical node identity = VERIFIED_FROM_A0_STRUCTURE
physical safe probe access      = OPEN
MOS G/S safe access             = OPEN
R110/R119 safe access           = OPEN
T1/T2 current-path clamp access = OPEN
```

### 5.3 H2 readiness decision

```text
H2 protocol definition = READY_BY_PROTOCOL
H2 lab readiness        = OPEN
H2 energized acquisition = NOT_AUTHORIZED
```

Primary blockers:

```text
H2-B1 exact scope capability
H2-B2 exact floating/differential voltage-probe rating + BW
H2-B3 exact high-current / high-bandwidth current-probe capability
H2-B4 deskew / synchronization method
H2-B5 safe physical access to A/B/C, VGS and R110/R119
H2-B6 actual A0 physical-unit population / operating-point eligibility
H2-B7 numerical T_mat,PG2 freeze
```

---

## 6. H4 laboratory-readiness inventory

H4 has a different measurement problem from H2. It prioritizes correct DC + low-frequency fidelity and long line-cycle records rather than only switching-edge bandwidth.

### 6.1 Required H4 chain

| H4 function | Minimum capability that must be verified | Current status |
|---|---|---|
| Source current | DC-capable current probe/transducer; 175 A-class anchor headroom; verified 100/120 Hz accuracy; zero drift recorded | `OPEN` |
| Source voltage | appropriate isolated/differential DC measurement | `OPEN` |
| HV-link voltage | rated HV differential/isolated probe with margin above actual BUS+–BUS− and adequate LF accuracy | `OPEN` |
| Output voltage/current | rated output probes or power analyzer sufficient to establish Pout / PF / line frequency | `OPEN` |
| Long synchronized record | enough stable 50/60-Hz cycles to resolve 2f_line; adequate record length and LF fidelity | `OPEN` |
| Spectral extraction | coherent FFT or sinusoidal projection with recorded window / frequency convention | `READY_BY_METHOD` |
| Current zero / drift check | pre/post acquisition zero / offset verification | `OPEN` |

### 6.2 H4 physical access

Known electrical boundaries:

```text
source / battery input boundary
BUS+ / BUS− HV DC link
AC output
```

Still required:

```text
physical current-probe placement without bypassing local bulk ambiguity
safe BUS+ / BUS− attachment
safe output-power measurement arrangement
source/load capability at the declared operating point
```

Current H4 access status:

```text
source-current electrical boundary = DEFINED
physical current-sensor access      = OPEN
HV-link electrical boundary         = DEFINED
safe HV-link probe access           = OPEN
AC output boundary                  = DEFINED
rated output measurement chain      = OPEN
```

### 6.3 H4 readiness decision

```text
H4 protocol definition  = READY_BY_PROTOCOL
H4 lab readiness         = OPEN
H4 energized acquisition = NOT_AUTHORIZED
```

Primary blockers:

```text
H4-B1 exact DC-capable current-probe range / accuracy / drift
H4-B2 exact HV differential-probe rating
H4-B3 output P/PF measurement capability
H4-B4 long-record scope/analyzer capability
H4-B5 safe physical access
H4-B6 actual A0 physical-unit population / OP-A eligibility
H4-B7 defensible R_eq,LV / uncertainty basis for loss-domain interpretation
H4-B8 numerical T_mat,PG4 freeze
```

---

## 7. Mandatory calibration / validity record before future acquisition

For the exact instruments that will actually be used, the readiness record must include:

```text
instrument model
probe model
probe ratio
voltage rating
current rating
common-mode rating
bandwidth
sample rate / record length
calibration status when available
scope input impedance / termination
current-probe range
current-probe saturation margin
zero / degauss procedure
V/I deskew method and residual
```

For a known exact model, official manufacturer documentation may be used to verify specifications. Do not select arbitrary instruments from the web simply to fill this table.

---

## 8. Unsafe / invalid configurations — hard stop

The following remain prohibited:

```text
normal earth-referenced scope ground connected blindly to A / C / BUS+ / floating high-energy nodes
probe voltage or common-mode rating not verified
current probe operated near or beyond saturation without margin
switching-energy V×I integration without verified deskew
one current waveform mapped to the wrong electrical switch boundary
single short switching record used to infer 100/120-Hz source reflection
HV-link ripple used as proof of PG-4 without source-side 2ω evidence
unknown physical-unit input population driven at the 12 V / 2 kW anchor
```

Any such capture is:

```text
INVALID
```

for Physical-Gap verification.

---

## 9. Readiness-state summary

| Item | Status | Meaning |
|---|---|---|
| File-34 H2 acquisition definition | `READY_BY_PROTOCOL` | quantities / boundaries / validity rules are defined |
| File-34 H4 acquisition definition | `READY_BY_PROTOCOL` | quantities / boundaries / processing rules are defined |
| ASP-2000 family 2 kW / 12 V option | `VERIFIED_AT_PRODUCT_FAMILY_LEVEL` | family supports the research-class operating point |
| Physical A0 unit / input population | `OPEN` | must verify on actual unit |
| Exact H2 instrument chain | `OPEN` | model / ratings / BW / deskew unknown |
| Exact H4 instrument chain | `OPEN` | DC current / HV / output chain unknown |
| H2 physical probe access | `OPEN` | electrical nodes known, safe bench access unverified |
| H4 physical probe access | `OPEN` | electrical boundaries known, safe bench access unverified |
| `T_mat,PG2` derivation rule | `ESTABLISHED_V1` | non-arbitrary rule fixed |
| `T_mat,PG2` numerical value | `OPEN` | requires uncertainty + architecture relevance basis |
| `T_mat,PG4` derivation rule | `ESTABLISHED_V1` | source-loss-based rule fixed |
| `T_mat,PG4` numerical value | `OPEN` | requires measurement/loss uncertainty basis |
| Energized H2 acquisition | `NOT_AUTHORIZED` | readiness incomplete |
| Energized H4 acquisition | `NOT_AUTHORIZED` | readiness incomplete |

Overall gate result:

```text
H2/H4 PRE-MEASUREMENT READINESS GATE v1 = ESTABLISHED
LAB READINESS = OPEN
ENERGIZED ACQUISITION = BLOCKED_BY_READINESS, NOT EXECUTED
```

This is not a negative PG result. It is a measurement-readiness result.

Therefore:

```text
PG-2 = HYPOTHESIS / STRONG STRUCTURAL SIGNAL
PG-4 = HYPOTHESIS / NOT_ESTABLISHED
```

remain unchanged.

---

## 10. Exact conditions that unlock future H2 / H4 acquisition

Before requesting energized execution, close all of the following:

```text
R1 actual A0 physical unit identified
R2 actual 12 V / 2 kW / 220 Vac eligibility verified
R3 exact oscilloscope / analyzer model recorded
R4 exact voltage-probe models and ratings recorded
R5 exact current-probe / transducer models and ratings recorded
R6 H2 A/B/C + VGS + R110/R119 physical access confirmed or explicitly bounded
R7 H4 source-current + BUS+/BUS− + output access confirmed
R8 grounding / isolation diagram checked
R9 current zero/degauss and V/I deskew procedure defined
R10 OP-0 de-energized setup passes
R11 OP-1 controlled functional capture passes without clipping / saturation / unsafe reference
R12 numerical `T_mat,PG2` frozen before final H2 interpretation
R13 numerical `T_mat,PG4` frozen before final H4 interpretation
R14 user / lab approval for the exact energized scope obtained
```

Only after R1–R14 are satisfied may the project proceed to energized H2/H4 acquisition.

---

## 11. Next research action

The next action is not mechanism combination and not Candidate #10 synthesis.

It is:

```text
READINESS BLOCKER CLOSURE
↓
identify actual A0 physical unit / input population
↓
record exact available scope / voltage probes / current probes / analyzer
↓
verify official ratings for those exact models
↓
confirm physical probe access + grounding / isolation plan
↓
quantify H2 / H4 uncertainty floor
↓
freeze numerical T_mat,PG2 / T_mat,PG4
↓
OP-0 / OP-1 only under approved lab conditions
↓
then request explicit approval for energized OP-A H2 / H4 acquisition
```

Until then:

```text
Mechanism combination = NOT AUTHORIZED
Candidate #10          = HOLD / NOT_ASSIGNED
Novelty                = NOT_ESTABLISHED
```
