# 15 — ASP-2000 A0 Kelvin / Millivolt Measurement Protocol

Status date: 2026-08-19  
Role: `A0 EXECUTABLE MEASUREMENT PROTOCOL`  
Research phase: `PHYSICAL GAP VALIDATION`  
Hardware result status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark measurement gate`

## 1. Purpose

Convert the reconstructed A0 high-current path into direct hardware evidence:

```text
current + segment mV drop + temperature
→ effective R
→ segment W loss
```

This protocol closes BAT+/BAT− distribution and nearby X1 boundaries before assigning loss to the magnetic conversion mechanism.

---

## 2. Measurement rule

For mΩ/sub-mΩ paths use Kelvin / four-wire concepts. Prefer loaded working-point measurements:

```text
R_segment = ΔV_segment / I_segment
P_segment = I_segment × ΔV_segment
```

For switching/ripple-dominated regions, use synchronized:

```text
P = average[v(t)i(t)]
```

Do not use ordinary two-wire resistance or `Iavg×Vavg` as the complete dynamic-loss result.

---

## 3. Safety boundary

The input voltage is low but the available current is hundred-ampere class.

```text
Power OFF
→ verify DC-link safe state
→ identify/secure sense points
→ verify no exposed lead can bridge power nodes
→ Power ON
→ raise load progressively
```

Use isolated/differential/floating methods where required. Do not connect an earth-referenced scope ground clip across arbitrary power nodes.

---

## 4. Measurement nodes

```text
K0       = BAT+ main connector
K1-T1-IN = BAT+ side of F2/F3/F5/F6
K1-T1-OUT= output side of T1 fuse bank
K2-T1    = T1 center tap
K1-T2-IN = BAT+ side of F7/F8/F9/F10
K1-T2-OUT= output side of T2 fuse bank
KJ8-A/B  = two sides of external J8 high-current boundary
K2-T2    = T2 center tap
KB       = main low-side return B
KBAT−    = battery-negative side of Q39...Q65
```

Verify exact pad polarity with power-off continuity before energizing.

---

## 5. Minimum current set

Preferred:

```text
I_source
I_T1
I_T2
```

Consistency check:

```text
I_source,avg ≈ I_T1,avg + I_T2,avg + I_aux,avg
```

Do not force 50/50 transformer current sharing before measurement proves it.

---

## 6. M0 — BAT+ multi-terminal distribution

BAT+ is one source feeding eight fuse-input sinks. Correct total:

```text
P_BAT+dist = Σ I_Fk × (V_BAT+ - V_Fk,input)
```

If only T1/T2 branch currents are available:

```text
P_BAT+dist ≈
I_T1 × average(drop to T1 fuse inputs)
+
I_T2 × average(drop to T2 fuse inputs)
```

Only if T1/T2 currents are unavailable may an equal-share estimate be used, labelled:

```text
EQUAL-SHARE ESTIMATE / NOT MEASURED DISTRIBUTION LOSS
```

---

## 7. M1 — Fuse banks

```text
T1: F2 // F3 // F5 // F6
T2: F7 // F8 // F9 // F10
```

Bank loss:

```text
P_FUSE,T1 = I_T1 × ΔV_FUSE,T1
P_FUSE,T2 = I_T2 × ΔV_FUSE,T2
```

Individual fuse mV is used for sharing/contact/thermal anomaly screening. Without individual fuse current, do not promote assumed per-fuse W to measured evidence.

---

## 8. M2 — T1 local feed — MANUFACTURING-BOUND CORRECTION

Measure:

```text
K1-T1-OUT → K2-T1
```

With I_T1:

```text
R_T1local = ΔV_T1local / I_T1
P_T1local = I_T1 × ΔV_T1local
```

Important correction: the former geometry comparison `~0.351 mΩ` used the PcbDoc `35.56 µm` stack metadata and is superseded.

The R52 manufacturing specification requires:

```text
base copper = 2 oz
finished copper >82 µm
```

The corrected same-geometry conservative bound is:

```text
R_T1local,PCB ≤~0.152 mΩ
```

Use this current bound when comparing hardware data.

Measured value materially above it may indicate contacts/necks/hot copper/current crowding/non-PCB conductors or boundary mismatch. A lower value may reflect copper thicker than 82 µm, solder/metal reinforcement or parallel paths.

---

## 9. M3/M4 — T2 and J8

Measure separately:

```text
M3a: K1-T2-OUT → KJ8-A
M3b: KJ8-A → KJ8-B
M4 : KJ8-B → K2-T2
```

Key unknown:

```text
R_J8 = ΔV_J8 / I_T2
P_J8 = I_T2 × ΔV_J8
```

Corrected geometry-only T2 PCB bound excluding J8:

```text
R_T2local,PCB ≤~0.0624 mΩ
```

Do not substitute guessed wire/strap dimensions for measured J8 mV.

---

## 10. M5 — B ↔ BAT− battery-interface bank

Seven parallel CSD18510KCS devices occupy this full-current boundary.

Measure:

```text
KBAT− ↔ KB
```

Calculate:

```text
R_M5 = ΔV_M5 / I_source
P_M5 = I_source × ΔV_M5
```

Record simultaneously/repeatably:

```text
I_source
ΔV_M5
12VP
V_BOCP relative B/SIG
MOS-bank temperature
ambient/cooling state
```

The 25°C datasheet scale remains:

```text
Req≈0.243 mΩ
P@175.4A≈7.47 W
```

but is not measured loss.

BOCP is only a product sense-chain cross-check. The MAIN-board nominal analog relation is:

```text
V_BOCP - V_B ≈22.1 × ΔV_M5
```

Exact control-board trip threshold remains open.

---

## 11. M6 — B-return distribution

If a clean boundary exists between main MOS source region and B:

```text
P_Breturn ≈ I_source × ΔV_Breturn
```

If the physical current boundary cannot be closed, keep:

```text
MEASUREMENT_BOUNDARY_NOT_CLOSED
```

---

## 12. Main A/C switching MOS are a separate dynamic gate

Do not close the two high-frequency logical switch regions with DC Kelvin alone.

Required:

```text
V_A-B(t), V_C-B(t)
I_A,total(t), I_C,total(t)
VGS(t)
fs / duty / dead time
temperature
deskew
```

and:

```text
p_A(t)=v_A-B(t)i_A,total(t)
p_C(t)=v_C-B(t)i_C,total(t)
```

---

## 13. Operating-point matrix

Use only product/test conditions approved for the hardware:

```text
OP0 = idle/no-load reference
OP1 = low load
OP2 = mid load
OP3 = high load
OP4 = 12 V / 2 kW anchor only if setup/product limits permit
```

At each point record steady state, thermal condition and measurement uncertainty.

---

## 14. Current geometry references — DO NOT USE OLD 35.56 µm VALUES

Current R52 manufacturing-bound references using minimum finished copper `82 µm`:

```text
BAT+ common PCB       ≤~0.108 mΩ / ≤~3.32 W @175.4A
T1 local PCB          ≤~0.152 mΩ / ≤~1.17 W @87.7A
T2 PCB excl. J8       ≤~0.0624mΩ / ≤~0.48 W @87.7A
partial positive PCB  ≤~0.162 mΩ / ≤~4.98 W @175.4A
```

Old values based on 35.56 µm PcbDoc stack metadata are superseded.

---

## 15. Evidence promotion rule

```text
GEOMETRY/MANUFACTURING BOUND
→ useful planning bound

MEASURED current + mV + temperature
→ benchmark-grade static-loss evidence

synchronous v×i waveform
→ dynamic switch-region evidence
```

Do not mix evidence classes into a single claimed measured total.

---

## 16. Immediate hardware sequence

```text
M5 B↔BAT− load sweep
↓
M1 fuse-bank drops
↓
M3 J8
↓
M2/M4 local feeds
↓
M0 BAT+ distribution
↓
M6 return copper if boundary is clean
↓
D0–D7 dynamic switch/HFT gate
```

Formal status:

```text
Kelvin protocol = READY
R52 copper manufacturing correction = APPLIED
hardware measurements = OPEN
A0 BAT→X1 measured loss = OPEN
A1 = BLOCKED UNTIL A0 LOSS LOCALIZATION
```
