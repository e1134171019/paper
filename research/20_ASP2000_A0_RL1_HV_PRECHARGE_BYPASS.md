# 20 — ASP-2000 A0 RL1 HV Precharge / Soft-Start Bypass

Status date: 2026-08-19  
Role: `A0 X1→HV STARTUP / PRECHARGE FUNCTION CLOSURE`  
Evidence status: `DIRECT SCHDOC CONNECTIVITY + COMPONENT VALUES + CONTROL-NET NAME`  
Hardware timing status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark/function-boundary evidence`

## 1. Purpose

Earlier A0 reconstruction established the secondary series path and placed `RL1` between the T2 outer secondary and the D2/D6 bridge leg, but left its operating role open.

This note closes that ambiguity far enough to classify the function without inventing the control-board timing/threshold.

Raw company Altium files remain outside the public repository.

---

## 2. RL1 component identity — VERIFIED

SchDoc hidden component data identifies `RL1` as:

```text
OZ-SS-112LM1
internal part text: RL-016A-240V-A
annotation: 240VAC / 16A / 12VDC
```

The SchDoc uses a multipart relay symbol:

```text
part 1 → coil pins 1 / 2
part 2 → power-contact pins 4 / 5
```

Therefore `RL1` is an electromechanical power relay, not a resistor, inductor, or magnetic conversion element.

---

## 3. Power-contact connectivity — VERIFIED

### RL1 contact pin 4 side

Direct wire-graph reconstruction gives:

```text
T2 pin 5
↓
RL1 pin 4
```

The same node also connects to one side of:

```text
R40 = 1 kΩ / 5 W
R41 = 1 kΩ / 5 W
```

### RL1 contact pin 5 side

The other contact side connects to the bridge AC node containing:

```text
D2 pin 1
D6 pin 2
```

The same node also connects to the opposite sides of `R40` and `R41`.

Therefore the physical secondary path is:

```text
T2 pin 5
│
├── RL1 power contact ───────────────────────┐
│                                            │
└── R40 1k/5W ─┐                             │
                ├── parallel resistor path ──┤
    R41 1k/5W ─┘                             │
                                             ↓
                                      D2 / D6 bridge AC node
```

The resistor equivalent is:

```text
R_precharge = 1 kΩ || 1 kΩ = 500 Ω
```

Thus the RL1 contact is an explicit bypass across a 500 Ω resistor-limited path.

---

## 4. Coil-control path — VERIFIED

RL1 coil pin 1 is wired to:

```text
12VP
```

RL1 coil pin 2 is driven through the local Q29/D9/R74/R78 network.

Relevant reconstructed parts:

```text
Q29 = 2SA1797
D9  = 1N4148-class flyback/clamp diode position
R74 = 10 kΩ
R78 = 1 kΩ
```

The Q29 control input is driven from the named net:

```text
RELAY_SS1
```

The same `RELAY_SS1` net is exported through:

```text
CN5A pin 3
```

Therefore the MAIN board receives a dedicated relay soft-start command from the control/interface side.

Exact active polarity, delay, bus-voltage threshold and fault logic remain open because the control-board receiver/source logic is not present in the currently available files.

---

## 5. Functional classification

The combined evidence is:

```text
T2 outer secondary
→ 500 Ω resistor-limited path
→ bridge AC terminal

power relay contact
→ directly bypasses the same 500 Ω path

relay control net
= RELAY_SS1
```

Formal decision:

```text
RL1 HV-secondary precharge / soft-start bypass function
= VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
```

The intended sequence is structurally:

```text
startup / relay not bypassing
→ secondary-to-bridge current passes through R40 || R41
→ HV DC-link charging/inrush is limited

normal power state / relay bypass active
→ RL1 contact shorts the resistor-limited path
→ normal secondary current reaches D2/D6 without the 500 Ω precharge resistance
```

Exact control timing and transition criterion remain:

```text
OPEN / CONTROL-BOARD EVIDENCE NEEDED
```

---

## 6. Scaling sanity check

The two precharge resistors provide approximately:

```text
500 Ω equivalent
10 W combined nominal continuous resistor rating
```

A purely continuous 10 W / 500 Ω scale corresponds to only:

```text
I ≈ sqrt(10/500) ≈ 0.14 A
```

This is orders of magnitude below the normal several-ampere-class HV-secondary current expected for a kW-class converter.

Therefore the resistor path cannot be the intended normal full-power path. Pulse/transient resistor capability may exceed the continuous rating, but the structural conclusion remains: the branch is a startup/precharge path that is bypassed for normal operation.

Status of this calculation:

```text
SCALING SUPPORT / NOT HARDWARE MEASUREMENT
```

---

## 7. Corrected X1→HV path

The A0 post-magnetic path should now be written:

```text
T1 secondary outer → D1 / D5 bridge leg

T1 pin 5 = T2 pin 2
        ↓
secondary series junction
        ↓
T2 pin 5
        ↓
[R40 || R41 = 500 Ω precharge path]
        ║
[RL1 soft-start bypass contact]
        ↓
D2 / D6 bridge AC node
        ↓
BUS+ / BUS-
        ↓
HV DC-link
        ↓
X3 inverter
```

This closes the former `RL1 role = OPEN` item.

---

## 8. Loss-accounting consequence

Do not classify R40/R41 startup dissipation as ordinary steady-state X1 conversion loss.

Use two distinct boundaries.

### Steady-state conversion loss

When the relay bypass is active, include as applicable:

```text
RL1 contact resistance / contact drop
secondary copper
bridge-diode loss
other normal conduction/commutation loss
```

The steady-state RL1 contact loss is still:

```text
MEASUREMENT_NEEDED
```

and should be obtained from contact millivolt drop if it is material and safely measurable.

### Startup / product-function energy

R40/R41 dissipated energy belongs to:

```text
HV DC-link precharge / inrush-management overhead
```

not to the steady-state magnetic-X1 efficiency number.

If startup energy/repetition is part of a product-level comparison, it must be compared under a matched startup contract.

---

## 9. Fair-comparison correction for A1 / candidates

Under product-level comparison, a candidate cannot delete HV-link precharge/inrush management only on the candidate side and call the removed hardware or startup energy a topology advantage.

Allowed contracts:

```text
Contract P — product level
→ match required DC-link precharge / inrush-management functionality

Contract C — steady-state core converter
→ exclude startup-only precharge energy from all compared architectures equally
```

A lower-loss / lower-cost / solid-state implementation is allowed, but the improvement must be classified correctly.

---

## 10. What remains open

```text
RELAY_SS1 active polarity
control-board condition that asserts RELAY_SS1
precharge delay / bus-voltage threshold
RL1 actual contact resistance at temperature
relay timing relative to X1 switching start
R40/R41 transient pulse energy / temperature
failure-mode behavior if RL1 does not bypass
```

These items do not block steady-state X1 topology classification, but they matter for product-level startup/protection validation.

---

## 11. Formal status

```text
RL1 identity                                = VERIFIED
RL1 coil supply 12VP                        = VERIFIED
RL1 command net RELAY_SS1                   = VERIFIED
RELAY_SS1 exported at CN5A pin 3            = VERIFIED
RL1 contact T2-pin5 side                    = VERIFIED
RL1 contact D2/D6 bridge-side               = VERIFIED
R40/R41 = 1k/5W each across same boundary   = VERIFIED
R40 || R41 equivalent = 500 Ω               = VERIFIED_FROM_VALUES
HV precharge / soft-start bypass role        = VERIFIED_AT_CONNECTIVITY_AND_NETNAME_LEVEL
exact control timing / threshold             = OPEN
steady-state relay-contact loss              = OPEN / MEASUREMENT_NEEDED
novelty relevance                            = NONE
```
