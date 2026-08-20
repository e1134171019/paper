# 39 — R2-G1 Reference-Locked Active-Clamp Mapping v1

Status date: 2026-08-20  
Role: `R2-G1 NODE/STATE MAPPING / IEEE GATE-B / PRE-PSIM BUILD CONTRACT`  
Research boundary anchor: `12 Vdc / 2 kW / 220 Vac / 1φ`  
Evidence class: `THEORETICAL / IEEE-PRIOR-ART-GROUNDED / NOT SIMULATED / NOT MEASURED`  
Topology-candidate authorization: `NOT GRANTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Locked IEEE reference cell

Primary reference for the PM-4 cell:

Tsai-Fu Wu, Jin-Chyuan Hung, Jeng-Tsuen Tsai, Cheng-Tao Tsai, and Yaow-Ming Chen, "An Active-Clamp Push–Pull Converter for Battery Sourcing Applications," IEEE Transactions on Industry Applications, vol. 44, no. 1, 2008, DOI `10.1109/TIA.2007.912748`.

The reference converter contains:

```text
Q1, Q2 = main push-pull switches
Q3, Q4 = auxiliary active-clamp switches
center-tapped transformer
Lk1, Lk2 = transformer leakage inductances
Cclamp1, Cclamp2 = clamp capacitors
Cr1..Cr4 = switch/snubber capacitances used in the resonant transitions
D5..D8 = secondary rectifiers
```

Reference switching relation:

```text
Q1 ↔ Q3 = complementary pair with dead time
Q2 ↔ Q4 = complementary pair with dead time
```

Reference physical function:

```text
leakage energy
+ switch capacitance
→ resonant transition
→ body-diode conduction
→ ZVS turn-on of main/auxiliary switch
→ leakage energy transferred into clamp capacitor
→ clamp capacitor later returns energy through auxiliary switch + transformer
```

Therefore the active-clamp subgraph is already established prior art and is not available as a novelty claim.

---

## 2. Reference half-cycle state sequence

The following is the reference-paper physical sequence for the Q1/Q3 side; the Q2/Q4 side is symmetric.

### S1 — pre-main-turn-on resonant transition

```text
Q3 OFF
opposite auxiliary path still conducting
Lk1 resonates with the relevant switch capacitances
VDS(Q1) falls toward zero
```

Admission condition is an energy condition of the form:

```text
0.5 Lk1 iLk1² >= capacitive transition energy
```

### S2 — Q1 ZVS turn-on

```text
VDS(Q1) ≈ 0
Q1 body diode conducts first
Q1 gate is then asserted
Q1 enters conduction under ZVS
```

### S3 — main power-transfer interval

```text
Vin
→ energized primary half
→ transformer
→ secondary rectifier
→ output
```

The opposite clamp capacitor can release previously stored energy through its auxiliary switch / leakage path / transformer.

### S4 — Q1 turn-off resonant transition

```text
Q1 OFF
Lk1 releases energy resonantly
main-switch capacitance charges
auxiliary-switch capacitance discharges
VDS(Q3) falls toward zero
```

### S5 — Q3 ZVS + leakage-energy recovery

```text
Q3 body diode conducts
Q3 gate is asserted under ZVS
Lk1 energy transfers into Cclamp1
Cclamp1 subsequently participates in transformer energy transfer / reset
```

Then the Q2/Q4 half-cycle repeats symmetrically.

This state sequence is the minimum behavior that the R2-G1 PSIM model must reproduce before nonideal loss comparison is allowed.

---

## 3. Mapping onto A0-derived R2-G1

A0 has two logical high-current switch nodes rather than four independent power branches:

```text
A = NetC62_1
C = NetC65_1
B = common source / return
```

with:

```text
A bank = 10 parallel main MOS positions
C bank = 10 parallel main MOS positions
```

and two transformer center-tap feeds:

```text
T1 CT → T1 A-half / C-half
T2 CT → T2 A-half / C-half
```

R2-G1 reference mapping:

| IEEE reference object | R2-G1 object |
|---|---|
| Q1 | logical A main MOS bank |
| Q2 | logical C main MOS bank |
| Q3 | Aux-A active-clamp switch bank |
| Q4 | Aux-C active-clamp switch bank |
| Lk1 | equivalent A-side commutation/leakage inductance of T1+T2 path |
| Lk2 | equivalent C-side commutation/leakage inductance of T1+T2 path |
| Cclamp1 | Cclamp-A |
| Cclamp2 | Cclamp-C |
| Cr1/Cr3 resonant capacitance pair | A main/aux effective capacitance set |
| Cr2/Cr4 resonant capacitance pair | C main/aux effective capacitance set |
| one reference transformer | two A0-derived HFTs with primary-side parallel energy sharing and secondary-series voltage addition |

Important:

```text
A0 T1/T2 parallel-primary + series-secondary structure
≠ literal Wu 2008 transformer graph
```

The Wu cell is used only to lock the PM-4 commutation principle and state sequence.

---

## 4. R2-G1 majority-power graph to build first

```text
VIN+
├─→ T1 center tap
└─→ T2 center tap

A half-cycle:
VIN+
→ T1/T2 A half-primaries
→ common node A
→ A main MOS bank
→ B / VIN-

C half-cycle:
VIN+
→ T1/T2 C half-primaries
→ common node C
→ C main MOS bank
→ B / VIN-

T1 + T2 secondaries
→ series voltage addition
→ HV rectifier
→ Cdc
→ HV bus
```

Only after this DC/DC portion is stable:

```text
HV bus
→ PM-7 VSI full bridge
→ LC filter
→ 220 Vac
```

The first simulation must not add PM-2 boost or PM-3 voltage stacking.

---

## 5. PM-4 overlay for the first PSIM build

The first build contains:

```text
Main-A switch
Aux-A switch
Cclamp-A
Lcomm-A / leakage-A
Ceq-A

a symmetric Main-C / Aux-C path
```

where:

```text
Ceq-A/C initially = explicit ideal resonant capacitance
```

and only later becomes:

```text
nonlinear MOS Coss
+ any intentional external Cr
```

This staging avoids mixing topology/state debugging with nonlinear semiconductor modeling.

The exact physical orientation of auxiliary MOSFET and clamp capacitor must follow the locked IEEE reference schematic when the PSIM schematic is entered. No alternative clamp orientation may be invented and still be called R2-G1.

---

## 6. Reference analytical equations retained for screening

From Wu 2008, under its reference topology assumptions:

### Clamp voltage

```text
Vclamp = D/(1-D) × Vin
```

### Ideal main / auxiliary switch voltage stress

```text
VDS,ideal = Vin + Vclamp
           = Vin/(1-D)
```

Thus for `Vin=12 V` and `D<0.5`, the reference-cell ideal switch stress remains below `24 V` before parasitic/transient margin.

### Reference voltage-transfer relation

```text
Vo/Vin = 2 n (D + D²)
```

where `n` is the reference-paper secondary/primary turns ratio.

Hard warning:

```text
This equation is NOT the final R2-G1 dual-HFT system equation.
```

The A0-derived dual-HFT parallel-primary / series-secondary graph requires its own derivation after the PSIM ideal graph is locked.

The equation is retained only as a reference mapping / initialization proxy.

---

## 7. 12 V analytical seed from the IEEE reference equation

For theoretical screening only:

```text
Vin = 12 V
Vdc,target = 350 V
```

Using the reference equation:

```text
D = 0.40 → n_eff,reference ≈ 26.04
D = 0.42 → n_eff,reference ≈ 24.45
D = 0.45 → n_eff,reference ≈ 22.35
D = 0.48 → n_eff,reference ≈ 20.53
```

If two identical series-secondary HFTs shared the voltage equally under the same first-order scaling, the per-transformer proxy would be approximately:

```text
D = 0.40 → ~13.02
D = 0.42 → ~12.23
D = 0.45 → ~11.17
D = 0.48 → ~10.26
```

These are NOT authorized winding ratios.

At the same duty values, the reference ideal switch stresses are:

```text
D = 0.40 → 20.00 V
D = 0.42 → 20.69 V
D = 0.45 → 21.82 V
D = 0.48 → 23.08 V
```

The immediate theoretical trade-off is therefore:

```text
higher D
→ lower required magnetic ratio proxy
→ higher clamp voltage / smaller reset margin
```

The first PSIM sweep must therefore include duty rather than freezing it.

---

## 8. First PSIM Student build contract

### Stage P0 — topology/state debug

Use only ideal elements:

```text
Vin = 12 V
ideal main switches
ideal auxiliary switches
ideal body diodes where PSIM device model requires them
ideal transformers
explicit Lcomm
explicit Cr
large ideal Cclamp
ideal HV rectifier
Cdc + resistive DC load
```

Initial sweep:

```text
fs = 30 / 50 / 80 kHz
D  = 0.40 / 0.42 / 0.45 / 0.48
Vdc target region = 325–400 V
```

P0 pass conditions:

```text
correct A/C alternating flux
no transformer DC-bias accumulation in the ideal symmetric case
correct main/aux dead-time ordering
body-diode-before-gate ZVS sequence reproduced
clamp capacitor reaches periodic steady state
HV bus reaches stable target range
no impossible shoot-through path
```

### Stage P1 — commutation physics

Add:

```text
T1/T2 leakage inductance
MOS Coss-equivalent capacitance
finite dead time
finite clamp-cap ESR
```

Observe:

```text
VDS_main_A/C
VDS_aux_A/C
Icomm_A/C
Cclamp voltage
transformer primary current
HV bus
```

### Stage P2 — conduction-loss layer

Add:

```text
main MOS RDS(on)
aux MOS RDS(on)
primary winding Rdc/Rac proxy
secondary winding resistance
rectifier loss
bus/interconnect equivalent resistance
```

Then report the first full DC/DC loss ledger.

### Stage P3 — AC synthesis

Only after P0–P2 are stable:

```text
HV bus
→ full-bridge VSI
→ LC filter
→ 220 Vac / 2 kW load
```

---

## 9. Mandatory Gate-B comparison result

### Same as IEEE prior art

```text
push-pull main function
active-clamp auxiliary switch pair
leakage-energy resonant transition
body-diode-assisted ZVS
clamp-cap energy recovery
main/aux complementary timing with dead time
```

Status:

```text
SAME_SUBGRAPH / KNOWN PRIOR ART
```

### Different system-level context currently retained

```text
dual HFT primary current sharing
common A/C logical MOS banks
series secondary voltage addition
12 V / 2 kW extreme-LV current boundary
HV bus followed by 220 Vac VSI
A0-matched loss comparison
```

Status:

```text
NEAR_SYSTEM_GRAPH
NOT SUFFICIENT FOR NOVELTY
```

Research value remains:

```text
Does a known active-clamp push-pull PM-4 cell still produce net total-loss benefit
when scaled into a 12 V / ~175 A dual-HFT inverter front end?
```

---

## 10. Hard stop conditions before deeper simulation

Stop R2-G1 as a preferred path if any of the following becomes robustly true:

```text
1. required auxiliary/clamp RMS current erases switching-loss savings
2. required leakage/commutation inductance causes unacceptable duty loss / current stress
3. 12 V-domain added series resistance produces larger I²R loss than the removed RC/switching loss
4. transformer/reset requirements force a magnetic burden worse than the matched hard-switched comparator
5. IEEE Gate B identifies the entire dual-HFT graph + same claimed 12 V loss result as established prior art
```

If stopped, R2-G1 remains a comparator and does not invalidate the broader PM-screening method.

---

## 11. Immediate NEXT

```text
1. Build P0 ideal DC/DC schematic in PSIM Student
2. verify the 10-state full-cycle main/aux sequence
3. derive the actual dual-HFT R2-G1 voltage-transfer equation from that graph
4. sweep D / fs / effective turns ratio
5. only after P0 passes, add Llk + Coss + dead time
6. perform first R2-G1 vs hard-switching matched LOSS comparison
```

Hardware validation remains deferred by current user-authorized research order.
