# 51 — R7 Gain-Sharing Charge/RMS Break-Even Screen v1

Status date: 2026-08-20  
Role: `PRE-TOPOLOGY GAIN-SHARING / CHARGE-RMS / BREAK-EVEN SCREEN`  
Boundary: `12 Vdc / 2 kW / 360 Vdc working HV link / 50 kHz analytical screen`  
Evidence: `FIRST-PRINCIPLES / PARAMETRIC MODEL`  
PSIM/LTspice: `NOT EXECUTED`  
Hardware: `NOT EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Question

Before designing the positive/negative-half-cycle capacitor graph, test whether transferring part of the voltage-gain burden from the HFT to PM3 is physically worth pursuing.

Compared ideal gain shares:

```text
k=1 : HFT -> 360 V, no PM3
k=2 : HFT -> 180 V, PM3 -> 2x
k=3 : HFT -> 120 V, PM3 -> 3x
k=4 : HFT ->  90 V, PM3 -> 4x
k=6 : HFT ->  60 V, PM3 -> 6x
```

This is not yet a topology comparison. It is a burden screen.

---

## 2. Critical correction: lower secondary voltage is not automatically lower transformer loss/volume

At fixed power, an ideal re-optimized transformer has the first-order relation

```text
Ns proportional to Vsecondary
Acu proportional to Isecondary
Ns * Acu proportional to V * I approximately P
```

Therefore reducing secondary voltage while increasing secondary current does **not** by itself prove lower secondary copper-window demand.

Likewise the core still transfers approximately 2 kW, and primary volt-seconds are not reduced merely because a downstream capacitor network provides additional voltage gain.

Hence the topology-independent guaranteed magnetic saving from gain split is:

```text
NOT ESTABLISHED
```

Possible real savings remain geometry-specific:

```text
fewer secondary turns / layers
shorter mean turn length
lower proximity-effect Rac
lower leakage inductance
simpler insulation / creepage
better window utilization
possibly simpler rectifier/clamp integration
```

These must be quantified by a matched transformer redesign; they cannot be assumed from voltage ratio alone.

---

## 3. Output charge authority

At 360 V / 2 kW:

```text
Iout = 2000/360 = 5.556 A
```

At 50 kHz:

```text
Qout/cycle = Iout/fs = 111.1 uC/cycle
```

A PM3 flying-capacitor path must repeatedly move this load charge. Voltage gain does not remove the charge-transfer requirement.

For an ideal two-phase charge/stack process, if the charge state occupies fraction `delta` and the stack/output state occupies `1-delta`, the minimum piecewise-constant flying-capacitor RMS-current floor is

```text
Icap,rms,min = Iout / sqrt(delta*(1-delta))
```

Thus:

| delta | minimum per-cap RMS current |
|---:|---:|
| 0.50 | 11.11 A |
| 0.33 | 11.81 A |
| 0.25 | 12.83 A |
| 0.10 | 18.52 A |

This is an ideal lower-bound waveform model. Real diode/MOS commutation, leakage and finite charge intervals can raise RMS/peak current.

---

## 4. Hard-charge redistribution proxy

For a pure hard-recharged flying capacitor:

```text
Eredist per capacitor per cycle approximately 0.5*C*(DeltaV)^2
C approximately Qout/DeltaV
```

so

```text
Predist per capacitor approximately 0.5*Iout*DeltaV
```

For an ideal `k` stack with `k-1` flying capacitors and `DeltaV = ripple_fraction * (360/k)`:

| k | HFT rail | flying-cap proxy count | hard-charge proxy @1% ripple | @2% | @3% |
|---:|---:|---:|---:|---:|---:|
| 1 | 360 V | 0 | 0 W | 0 W | 0 W |
| 2 | 180 V | 1 | 5.00 W | 10.00 W | 15.00 W |
| 3 | 120 V | 2 | 6.67 W | 13.33 W | 20.00 W |
| 4 | 90 V | 3 | 7.50 W | 15.00 W | 22.50 W |
| 6 | 60 V | 5 | 8.33 W | 16.67 W | 25.00 W |

Status:

```text
HARD-CHARGE BRANCH PROXY
NOT A UNIVERSAL PM3 LOSS FLOOR
```

A resonant/soft-charge implementation can reduce this term, but that adds another physical mechanism and must be reclassified/audited rather than treated as free R7 behavior.

---

## 5. ESR sensitivity example

Using only a parameter example of `2 mOhm ESR per flying capacitor` and the best symmetric `delta=0.5` RMS floor (`11.11 A` per cap):

| k | cap-ESR proxy |
|---:|---:|
| 2 | 0.247 W |
| 3 | 0.494 W |
| 4 | 0.741 W |
| 6 | 1.235 W |

These numbers are not selected-component predictions; semiconductor path resistance, capacitor AC impedance, bus/contact resistance and switching losses are still absent.

The important result is scaling: each additional flying-cap path adds another full charge-transfer RMS path.

---

## 6. Resistance break-even sensitivity

For the same ideal charge/stack RMS floor, the maximum equivalent resistance **per flying-cap current path** that would consume a total 10-W conduction budget is:

### delta = 0.50

| k | flying paths | R each for total 10 W |
|---:|---:|---:|
| 2 | 1 | 81.0 mOhm |
| 3 | 2 | 40.5 mOhm |
| 4 | 3 | 27.0 mOhm |
| 6 | 5 | 16.2 mOhm |

### delta = 0.10

| k | flying paths | per-cap RMS | R each for total 10 W |
|---:|---:|---:|
| 2 | 1 | 18.52 A | 29.16 mOhm |
| 3 | 2 | 18.52 A | 14.58 mOhm |
| 4 | 3 | 18.52 A | 9.72 mOhm |
| 6 | 5 | 18.52 A | 5.83 mOhm |

Therefore a narrow charge window rapidly consumes the supposed advantage of moving PM3 to a higher-voltage domain.

---

## 7. What can and cannot be concluded before transformer geometry is known

### Established by this screen

```text
1. PM3 does avoid inserting its components into the 175-A source-series path.
2. PM3 nevertheless has a mandatory charge-transfer RMS burden.
3. More stack levels increase the number of full charge-transfer paths.
4. Hard charge can cost several to tens of watts even at small capacitor ripple.
5. Reducing HFT secondary voltage does not automatically reduce re-optimized copper-window demand at fixed 2-kW power.
```

### Not established

```text
transformer volume reduction
transformer copper-loss reduction
core-loss reduction
leakage reduction in watts
net efficiency improvement
system volume reduction
```

Those require actual winding/core geometry.

---

## 8. First priority decision

The gain-sharing sweep does **not** justify jumping to a 3x capacitor graph solely because 120 V is one-third of 360 V.

Current ordering for the next physical validation layer:

```text
k=2 / HFT 180 V
= PRIORITY A
Reason: smallest PM3 mechanism burden; only one flying-cap proxy path.

k=3 / HFT 120 V
= PRIORITY B
Reason: stronger secondary-turn reduction, but two full charge-transfer paths and higher hard-charge burden.

k=4 / 90 V
= DEPRIORITIZE

k=6 / 60 V
= DEPRIORITIZE
```

`k=2` and `k=3` are not winners. They are the only cases retained for a geometry-specific magnetic crossover test.

---

## 9. Required next gate before PSIM

Do not yet synthesize a detailed positive/negative-half-cycle switching graph and do not run PSIM.

Next perform a matched transformer redesign at:

```text
T360 = HFT-only 360-V secondary reference
T180 = k=2 hybrid magnetic stage
T120 = k=3 hybrid magnetic stage
```

Use the same:

```text
12-V / 2-kW boundary
50-kHz class switching assumption
core/material family basis
Bpk limit
thermal/current-density basis
isolation contract
primary topology contract
```

For each derive/bound:

```text
Np / Ns
primary and secondary conductor area
turn length / layer count
window fill
DCR
Rac / skin-proximity multiplier
secondary leakage
winding capacitance proxy
core Bpk and core loss
insulation burden
magnetic physical volume
```

Then define the geometry-specific maximum benefit:

```text
Pmag_saved(k)
= Pmag(T360) - Pmag(T180 or T120)
```

and compare against candidate PM3 burden:

```text
Pmag_saved + Pother_removed
>
Pcap + Pcharge + Pswitch/diode + DeltaPsecondary_RMS + Pinteraction
```

Only if a positive crossover exists should a real half-cycle charge/stack graph be synthesized and passed to time-domain simulation.

---

## 10. Current formal status

```text
R7 gain-sharing hypothesis = CONDITIONAL / NOT PROVEN
k=2 = RETAIN FOR TRANSFORMER-GEOMETRY CROSSOVER
k=3 = RETAIN FOR TRANSFORMER-GEOMETRY CROSSOVER
k>=4 = DEPRIORITIZED AT THIS SCREEN
R7-C2 actual graph = NOT YET AUTHORIZED FOR PSIM
Candidate #10 = HOLD
Novelty = NOT_ESTABLISHED
```
