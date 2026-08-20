# 64 — A0 Minimum Measurement Pack: X3 / HFT / BUS v1

Status date: 2026-08-20  
Role: `A0-REAL MINIMUM PHYSICAL-EVIDENCE ACQUISITION CONTRACT`  
Research boundary: `12 Vdc / 2 kW / 220 Vac / 1φ / 50 Hz`  
Target hardware: `ASP-2000 R52 / 220-V output population`  
Evidence status: `MEASUREMENT CONTRACT READY / HARDWARE DATA NOT YET ACQUIRED`  
Simulation status: `PSIM NOT EXECUTED / LTspice NOT EXECUTED`  
Hardware status: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Purpose

File63 reduced the decision-dominant A0 unknowns to four quantities that can materially reverse the loss ranking:

```text
M1  physical HV-BUS operating voltage and ripple
M2  X3 carrier / modulation / dead time
M3  T1/T2 secondary-current RMS / peak / waveform
M4  de-energized T1/T2 winding DCR
```

File64 converts those unknowns into one minimum executable measurement pack.

The objective is not broad product characterization. The objective is to acquire only the data needed to decide whether the next research branch should be:

```text
A. E4+E6 modern matched crossover
B. E2 primary commutation
C. no new topology under the present boundary
```

This document does **not** claim any measurement has been performed.

---

## 2. Existing A0 design facts used by this contract

R52 design intent already establishes:

```text
E4 rectifier:
D1/D2/D5/D6 = KSU60D60N

E5 passive X2:
C8/C11/C89/C90 = 680 µF / 315 V
all four across BUS+ <-> BUS-
Cbus = 2720 µF schematic population

E6 / X3 @220-V:
8 × IRG7PH35UDPBF
4 H-bridge switch positions
2 IGBTs in parallel per position

left leg:
high = Q2 || Q31
low  = Q10 || Q35

right leg:
high = Q1 || Q32
low  = Q9 || Q34

HFT:
T1/T2 = PQ5050-class
secondaries in the common series power path ahead of the rectifier
```

File63 bounds but does not measure:

```text
244.36 V <= VBUS <= 315 V
Isec,rms >= 6.35 A
```

These are planning bounds only.

---

## 3. Governing safety / evidence rules

File64 inherits the measurement rules of:

```text
research/15_ASP2000_A0_KELVIN_MEASUREMENT_PROTOCOL.md
research/16_ASP2000_A0_DYNAMIC_SWITCHING_AND_HFT_MEASUREMENT_PROTOCOL.md
```

Hard rules:

```text
1. Power OFF before attaching or moving probes whenever practical.
2. Verify the HV link is in a safe discharged state before de-energized resistance work.
3. Do not connect an earth-referenced oscilloscope ground clip to arbitrary BUS, bridge-midpoint, high-side emitter, or transformer switching nodes.
4. Differential / isolated probes must be rated for the expected differential voltage, common-mode voltage, transient overshoot and measurement category of the actual setup.
5. Current probes must be zeroed/degaussed as applicable and must not saturate on the measured waveform.
6. A clipped, aliased, saturated, unsafe-grounded or unrepeatable capture is INVALID evidence.
7. Switching-energy integration is forbidden as benchmark evidence until voltage/current channel deskew is verified.
8. Do not exceed product, source, load, wiring, probe or laboratory limits merely to reach the 2-kW anchor.
```

If any required rating/reference is uncertain:

```text
STOP / RECONFIGURE / DO NOT ENERGIZE FOR THAT CAPTURE
```

---

## 4. Operating-point contract

Preferred minimum set:

```text
OP0 = no-load / idle reference
OP1 = approximately 25–50% rated load
OP2 = high-load point
OP3 = 12-V / 2-kW anchor only if explicitly permitted by the product/test setup
```

At every energized operating point record:

```text
Vin
Iin if available
Pout
Vout,rms
Iout,rms
load type
power factor if available
output frequency
ambient temperature
cooling/fan state
X3 heatsink temperature if available
T1/T2 temperature if available
time after load application / thermal stabilization state
```

Do not compare captures from different load/thermal states as if they were one operating point.

---

## 5. M1 — Physical HV BUS measurement

### 5.1 Quantity

Measure directly:

```text
V_BUS(t) = V(BUS+) - V(BUS-)
```

Use a properly rated differential/isolated measurement method.

Do not infer VBUS from:

```text
315-V capacitor rating
220-V output RMS
transformer turns assumptions
canonical 350-V modern-matched comparison coordinate
```

### 5.2 Required captures

Save two time scales at the same declared operating point.

#### M1-LF — line-cycle / 2ω window

Capture enough complete line cycles to extract:

```text
Vbus,avg
Vbus,min
Vbus,max
Vbus,pp,LF
100-Hz component at 50-Hz output
120-Hz component at 60-Hz output if that mode is used
```

Preferred analysis window:

```text
integer number of output cycles
```

#### M1-HF — switching-ripple / peak window

Capture a shorter high-bandwidth window to extract:

```text
Vbus,peak
Vbus,valley
HF ripple peak-to-peak
repetitive spike / ringing if present
```

The reported HF peak is probe-bandwidth dependent, so probe bandwidth and any bandwidth limit must be recorded.

### 5.3 Promotion rule

M1 becomes `MEASURED` only when:

```text
probe/reference rating documented
no clipping
same-point repeatability acceptable
operating point metadata complete
```

Otherwise:

```text
CONTEXT_ONLY / INVALID
```

---

## 6. M2 — X3 gate / carrier / modulation measurement

### 6.1 First capture: lowest-risk valid carrier evidence

Priority is to recover the real X3 PWM carrier before any switching-loss integration.

Preferred first measurement:

```text
one low-side X3 device gate-to-emitter waveform
for example Q10 or Q9
```

Measure the actual device quantity:

```text
VGE = V(gate) - V(the same device emitter)
```

A low-side position is preferred for the first carrier capture when it reduces common-mode probing burden, but the actual probe reference must still be verified from the PCB.

Extract:

```text
carrier frequency fs,X3
period
pulse-width distribution
fundamental-envelope relationship
turn-on / turn-off edge
VGE,on
VGE,off/min
ringing / overshoot
```

### 6.2 Dead-time capture

To measure one leg dead time, capture the high-side and low-side commands/gates of the **same leg**:

```text
left leg:  Q2/Q31 high vs Q10/Q35 low
or
right leg: Q1/Q32 high vs Q9/Q34 low
```

High-side gate must be measured relative to its own emitter with an appropriately rated isolated/differential method.

If that cannot be done safely with available instrumentation, use a proven isolated driver-command / logic-side timing point instead and classify it:

```text
DRIVER-COMMAND TIMING
!= DEVICE VGE TIMING
```

Extract:

```text
dead time / non-overlap
turn-on ordering
turn-off ordering
possible asymmetric dead time
```

### 6.3 Modulation classification

Use a long enough capture to determine whether the bridge behaves as:

```text
bipolar SPWM
unipolar SPWM
low-frequency polarity unfolding + PWM leg
other / unresolved
```

Do not classify modulation from a single isolated pulse.

### 6.4 Promotion rule

M2 closes when at least:

```text
fs,X3 = measured
one-leg timing/dead-time = measured or bounded
modulation class = measured / defensibly classified
```

If only a control-side signal is captured:

```text
carrier may be promoted if linkage is proven
actual device VGE remains OPEN
```

---

## 7. M3 — T1/T2 secondary-current waveform

### 7.1 Measurement boundary

The desired current is the actual series secondary / rectifier-input current, not an unrelated upstream bus current.

Preferred boundary:

```text
one accessible conductor in the T1/T2 series-secondary path immediately before the rectifier AC input
```

If T1 and T2 individual secondary leads are separately accessible, measure both to verify that the intended series-path current relationship is physically realized.

Identify the conductor using power-off continuity / schematic-PCB correlation before energizing.

Do not place a clamp around both outgoing and return conductors because magnetic cancellation can hide the actual current.

### 7.2 Required extracted quantities

Over an integer number of output line cycles calculate:

```text
Isec,rms
Isec,avg where meaningful
Isec,pk+
Isec,pk-
crest factor = max(|Isec|) / Isec,rms
rectifier charging conduction angle / pulse width if visible
HF ringing / commutation spikes
```

At the 2-kW anchor, File63 requires the sanity check:

```text
Isec,rms >= 6.35 A
```

A result materially below the physical lower bound means the measurement boundary, scaling, operating point, or probe validity must be rechecked.

### 7.3 Current-probe validity

Record:

```text
probe model
range
bandwidth
zero/degauss state
DC capability or AC-only nature
observed saturation/clipping status
```

A probe that cannot reproduce the charging-pulse waveform cannot be used to claim benchmark-grade RMS/current stress.

---

## 8. M4 — De-energized transformer winding DCR

### 8.1 Mandatory precondition

This is a de-energized test.

Before connecting a resistance instrument:

```text
source disconnected according to lab procedure
unit unable to restart unexpectedly
HV link verified discharged by an approved method
winding terminals identified
parallel semiconductor/circuit paths evaluated
```

If the winding cannot be isolated sufficiently to prevent a parallel path from corrupting the result:

```text
DCR = MEASUREMENT_BOUNDARY_NOT_CLOSED
```

Do not publish the reading as transformer DCR.

### 8.2 Method

Preferred:

```text
Kelvin / four-wire milliohm measurement
```

Record at minimum:

```text
T1 secondary DCR
T2 secondary DCR
winding temperature
meter/test current
lead/contact arrangement
repeat readings
```

If primary half-windings are accessible without disturbing the assembly, also record:

```text
T1 primary-half DCR values
T2 primary-half DCR values
```

Current reversal / offset cancellation is preferred when supported by the instrument.

### 8.3 Copper-loss lower bound

Once M3 and M4 are valid:

```text
Psec,Cu,DC-lower
= Isec,rms² × (Rdc,T1,sec + Rdc,T2,sec)
```

This remains a lower bound because:

```text
Rac >= Rdc in the switching waveform
proximity/skin effect are not closed by DCR
hot winding resistance can exceed room-temperature DCR
```

### 8.4 Optional M4B — Rac / impedance follow-up

Only after the real switching-frequency spectrum is known from M2, an impedance/LCR measurement may characterize winding impedance near relevant frequencies.

Until the actual winding geometry and frequency-dependent loss are closed:

```text
HFT total copper loss = OPEN
```

---

## 9. M5 — Optional X3 switching-energy capture

M5 is **not part of the minimum gate** and is not authorized merely because File64 exists.

M5 becomes useful only after M1/M2 establish:

```text
actual VBUS
actual carrier
actual modulation/dead time
```

and suitable synchronized voltage/current measurement is available.

Target per switch region:

```text
Eon  = integral(vCE × iC dt) over valid turn-on interval
Eoff = integral(vCE × iC dt) over valid turn-off interval
```

Mandatory validity:

```text
voltage/current probe bandwidth adequate
current scaling valid
channel deskew verified
integration window documented
no clipping
no probe saturation
repeatable operating point
```

If those conditions are not met:

```text
report stress/timing only
Psw = OPEN
```

---

## 10. Minimum raw-data file set

Suggested naming:

```text
M1_BUS_LF_OPx.csv
M1_BUS_HF_OPx.csv
M2_X3_GATE_LOW_OPx.csv
M2_X3_LEG_TIMING_OPx.csv
M3_HFT_SECONDARY_CURRENT_OPx.csv
M4_HFT_DCR.csv
```

Optional screenshots may accompany the raw data, but screenshots alone are not preferred numerical evidence when CSV/waveform export is available.

Each waveform file should retain:

```text
time axis
raw channel values
probe attenuation/scaling
sample rate
scope bandwidth / bandwidth limit
channel labels
```

---

## 11. Minimum metadata schema

For every measurement batch record:

```text
measurement_batch_id
measurement_id
date_time
operator
unit_serial_or_asset_id
board_revision
output_variant
input_configuration
Vin_V
Iin_A
Pout_W
Vout_rms_V
Iout_rms_A
PF
output_frequency_Hz
load_type
ambient_C
X3_heatsink_C
T1_C
T2_C
cooling_state
thermal_state
scope_model
scope_sample_rate
scope_bandwidth
voltage_probe_model
voltage_probe_bandwidth
voltage_probe_ratio
current_probe_model
current_probe_bandwidth
current_probe_range
channel_deskew_ns
raw_file_name
notes
validity_status
```

Result fields:

```text
Vbus_avg_V
Vbus_min_V
Vbus_max_V
Vbus_pp_LF_V
Vbus_HF_pp_V
Vbus_peak_V
x3_fs_Hz
x3_deadtime_ns
x3_modulation_class
Isec_rms_A
Isec_peak_A
Isec_crest_factor
DCR_T1_sec_mOhm
DCR_T2_sec_mOhm
DCR_T1_primary_half_mOhm
DCR_T2_primary_half_mOhm
```

Use null/blank plus an evidence-status field for quantities not measured. Do not insert guessed values to make the table complete.

---

## 12. Evidence-validity codes

Use one of:

```text
VALID_MEASURED
VALID_BOUND
CONTEXT_ONLY
REPEAT_NEEDED
PROBE_LIMITED
SATURATED
CLIPPED
ALIASED
DESKEW_NOT_VALID
BOUNDARY_NOT_CLOSED
UNSAFE_TO_ACQUIRE
NOT_MEASURED
```

Only `VALID_MEASURED` values may be promoted into the A0-REAL benchmark ledger as measured scalars.

---

## 13. Stop / reject conditions

Reject or stop the measurement if any of the following applies:

```text
unknown scope-ground path on switching/HV node
probe differential/common-mode/transient rating not established
probe or channel clipping
current-probe saturation
current probe placed around cancelling conductors
winding DCR contaminated by an unclosed parallel path
incomplete operating-point metadata
waveform not repeatable
unexpected unit behavior / abnormal temperature / protection event
requested operating point exceeds approved setup limits
```

Do not continue simply to complete a row in the worksheet.

---

## 14. Minimum acquisition order

Recommended order:

```text
STEP 0  physical-unit / revision / output-variant confirmation

STEP 1  M4 de-energized DCR
        lowest-risk data first

STEP 2  M1 BUS measurement
        closes actual R52 post-X1 voltage

STEP 3  M2 low-side X3 gate / carrier
        closes the dominant E6 switching-frequency unknown

STEP 4  M2 one-leg high/low timing if safe instrumentation permits
        closes dead time / modulation detail

STEP 5  M3 secondary current
        closes HFT/rectifier RMS stress

STEP 6  stop and rebuild A0-REAL loss ledger

STEP 7  M5 switching-energy capture only if still decision-relevant
```

This order deliberately avoids beginning with the most difficult high-side switching-energy integration.

---

## 15. What File64 will close

A successful M1–M4 acquisition promotes:

```text
VBUS                  BOUNDED -> MEASURED
X3 carrier            OPEN -> MEASURED
X3 dead time/modulation OPEN -> MEASURED or BOUNDED
Isec,rms               LOWER-BOUND -> MEASURED
HFT secondary DCR      OPEN -> MEASURED
HFT DC-copper lower W  OPEN -> MEASURED/MODELLED FROM MEASURED INPUTS
```

It does **not** automatically close:

```text
HFT Rac/core loss
rectifier dynamic/recovery watts
full X3 switching watts
full product efficiency ledger
novelty
```

---

## 16. Immediate post-measurement artifact

After valid M1–M4 data exists, create:

```text
research/65_A0_REAL_LOSS_LEDGER_CLOSURE_V1.md
```

File65 must keep three ledgers separate:

```text
A0-REAL R52
A0-MODERN-MATCHED
G13-REF2 modern matched comparator
```

Decision gate after File65:

```text
A. E4+E6 returns only if a modern-matched structural loss advantage survives
B. E2 becomes mainline if primary commutation remains the strongest avoidable loss target
C. NO-NEW-TOPOLOGY if neither branch supports a robust advantage
```

No Candidate #10 assignment occurs before this gate.

---

## 17. Formal status

```text
File64 measurement contract = READY
M1 BUS                      = NOT MEASURED
M2 X3 carrier/dead time     = NOT MEASURED
M3 secondary current        = NOT MEASURED
M4 HFT DCR                  = NOT MEASURED
M5 X3 switching energy      = DEFERRED / CONDITIONAL

Candidate #10               = HOLD / NOT_ASSIGNED
Novelty                     = NOT_ESTABLISHED
PSIM                        = NOT EXECUTED
LTspice                     = NOT EXECUTED
Hardware                    = NOT EXECUTED
```
