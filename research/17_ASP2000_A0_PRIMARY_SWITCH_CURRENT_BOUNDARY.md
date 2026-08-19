# 17 — ASP-2000 A0 Primary Switch Current Boundary

Status date: 2026-08-19  
Role: `A0 PRIMARY-SWITCH / CURRENT-MAPPING CORRECTION`  
Evidence status: `COMPILED PCB NET RECONSTRUCTION + SCHDOC CONTROL TRACE`  
Hardware waveform status: `NOT YET MEASURED`  
Novelty relevance: `NONE — benchmark correction`

## 1. Purpose

This document resolves the remaining ambiguity between the four local gate-drive groups and the actual high-current power path of the ASP-2000 R52 low-voltage primary stage.

The key correction is:

```text
four local gate-driver groups
!=
four independent power branches
```

The compiled PCB establishes only two high-current switched primary-end nodes, A and C, with a common low-side return `B`.

---

## 2. Compiled PCB power nets — VERIFIED

### 2.1 Common source / return net

All twenty main low-voltage MOSFET source pads are on the same compiled PCB net:

```text
B
```

This includes:

```text
A-side groups:
Q3 Q4 Q5 Q6 Q33
Q18 Q19 Q20 Q21 Q37

C-side groups:
Q11 Q12 Q13 Q14 Q36
Q24 Q25 Q26 Q27 Q38
```

The low-side driver reference devices also return to `B` at PCB level:

```text
Q8  low-side driver reference → B
Q16 low-side driver reference → B
Q22 low-side driver reference → B
Q28 low-side driver reference → B
```

Therefore the schematic local labels:

```text
DA1-E
DB1-E
DA2-E
DB2-E
```

must not be treated as four electrically isolated high-current source returns in the physical loss model. They are local/hierarchical reference names whose compiled physical return is the common `B` net.

### 2.2 A-side switched node

The compiled PCB net:

```text
NetC62_1
```

contains:

```text
T1 primary pin 9 / A end
T2 primary pin 9 / A end

Q3 Q4 Q5 Q6 Q33 drains
Q18 Q19 Q20 Q21 Q37 drains
```

Therefore:

```text
A-side switch function
= 10 physically parallel MOS positions
```

### 2.3 C-side switched node

The compiled PCB net:

```text
NetC65_1
```

contains:

```text
T1 primary pin 7 / C end
T2 primary pin 7 / C end

Q11 Q12 Q13 Q14 Q36 drains
Q24 Q25 Q26 Q27 Q38 drains
```

Therefore:

```text
C-side switch function
= 10 physically parallel MOS positions
```

### 2.4 Separate center-tap supplies remain

The two transformer center taps remain separately supplied:

```text
T1 pin 8 center tap → NetC2_1 → T1 local bulk / fused feed
T2 pin 8 center tap → NetC28_1 → T2 local bulk / fused feed
```

Thus the accurate primary structure is:

```text
T1 center feed ─→ T1 half-primary A ─┐
                                     ├→ common A switched node → 10 MOS → B
T2 center feed ─→ T2 half-primary A ─┘

T1 center feed ─→ T1 half-primary C ─┐
                                     ├→ common C switched node → 10 MOS → B
T2 center feed ─→ T2 half-primary C ─┘
```

---

## 3. Q19 anomaly — RESOLVED AT PCB LEVEL

Earlier SchDoc-only graph extraction showed Q19 drain as apparently isolated.

The compiled PCB resolves the ambiguity:

```text
Q19 pad 2 / Drain → NetC62_1
```

which is the same A-side power net used by:

```text
Q3 Q4 Q5 Q6 Q33
Q18 Q20 Q21 Q37
T1 A
T2 A
```

Formal correction:

```text
Q19 physical drain connectivity = VERIFIED IN PCB
A-side connected MOS count      = 10
C-side connected MOS count      = 10
Total connected main LV MOS     = 20
```

The old `Q19 drain = OPEN` statement is superseded.

---

## 4. Four physical driver groups, two logical commands

The four local gate buses remain real:

```text
DA1-G → Q3 Q4 Q5 Q6 Q33
DA2-G → Q18 Q19 Q20 Q21 Q37

DB1-G → Q11 Q12 Q13 Q14 Q36
DB2-G → Q24 Q25 Q26 Q27 Q38
```

Each MOS has its own 27.4 ohm gate resistor.

However the upstream command nets are paired by zero-ohm links:

```text
DR-A  ── R213 = 0 ohm ── DR-A2
DR-B  ── R212 = 0 ohm ── DR-B2
```

Therefore the present compiled/control evidence supports:

```text
logical command A
→ two local driver stages
→ DA1-G + DA2-G
→ ten parallel A-side MOS

logical command B
→ two local driver stages
→ DB1-G + DB2-G
→ ten parallel C-side MOS
```

Interpretation:

```text
4 physical driver subgroups
2 logical switching functions
2 high-current switched power nodes
```

Exact timing symmetry between the two physical drivers under one logical command still requires waveform measurement.

---

## 5. Correct current mapping

### 5.1 Transformer currents

Define:

```text
i_T1(t) = current through the actual T1 center-tap lead / winding feed

i_T2(t) = current through the actual T2 center-tap lead / winding feed
```

These remain valid transformer-current measurements.

### 5.2 A/C total switch-node current

During a stable A-side conduction interval, neglecting small displacement/auxiliary terms:

```text
i_A,total(t) ≈ i_T1,A(t) + i_T2,A(t)
```

During a stable C-side conduction interval:

```text
i_C,total(t) ≈ i_T1,C(t) + i_T2,C(t)
```

These relations are the correct first-order current boundary for the two electrical switch functions.

### 5.3 DA1/DA2 are not T1/T2 currents

Because DA1 and DA2 drains are on the same A power net and all sources are on `B`:

```text
i_DA1 + i_DA2 = i_A,total
```

but generally:

```text
i_DA1 != i_T1

i_DA2 != i_T2
```

Likewise:

```text
i_DB1 + i_DB2 = i_C,total
```

but generally:

```text
i_DB1 != i_T1

i_DB2 != i_T2
```

Subgroup current division depends on:

```text
hot RDS(on)
gate timing mismatch
gate-drive impedance
source/drain copper resistance
package/contact parasitics
common-source inductance
thermal mismatch
```

A useful parametric form is:

```text
i_DA1 = alpha_A i_A,total

i_DA2 = (1-alpha_A) i_A,total
```

with `alpha_A` measured/modelled rather than assumed to be 0.5.

The same applies to the B-side driver subgroups.

---

## 6. Commutation caveat

The simple current-sum relation must not be blindly applied through dead time and switching transitions.

During commutation, additional current may flow through:

```text
MOS Coss / displacement current
body-diode paths
transformer leakage inductance
clamp/snubber networks
parasitic capacitance
ringing loops
```

Therefore:

```text
stable conduction interval
→ center-tap-current sum is a strong first-order switch-current boundary

switching transition / dead time
→ synchronous high-bandwidth current + voltage evidence required
```

---

## 7. Revised switching-loss measurement boundary

The first A0 switching-loss target should no longer be four fictional independent power banks.

Use two electrical switch functions:

```text
A switch region:
V_A-B(t)
I_A,total(t)

C switch region:
V_C-B(t)
I_C,total(t)
```

System-level instantaneous absorbed power boundary:

```text
p_A(t) = v_A-B(t) i_A,total(t)

p_C(t) = v_C-B(t) i_C,total(t)
```

Then:

```text
P_primarySwitchRegion
= average[p_A(t) + p_C(t)]
```

The probe points must be defined tightly enough that the voltage boundary does not unintentionally include large unrelated bus/contact loss.

Device-level power can be studied later if subgroup/current-sharing behavior itself becomes a research target.

---

## 8. Revised waveform plan

### Timing verification

Still measure all four driver outputs:

```text
DA1-G / B
DA2-G / B
DB1-G / B
DB2-G / B
```

Purpose:

```text
verify the two local drivers under logical A switch together
verify the two local drivers under logical B switch together
quantify propagation / turn-on / turn-off mismatch
```

### Device VGS verification

Representative devices remain useful:

```text
Q3  = DA1 representative
Q18 = DA2 representative
Q11 = DB1 representative
Q24 = DB2 representative
```

Measure each actual Gate-to-Source pin voltage.

### Power-node VDS

For first system-level switching-region loss closure, prioritize:

```text
V_A-B
V_C-B
```

rather than pretending Q3/Q18 or Q11/Q24 are four independent power branches.

### Transformer current

Place current probes on the actual transformer center-tap leads if physically accessible, after local bulk/fuse junction ambiguity, so the measured current is winding/feed current rather than only upstream source current.

---

## 9. Updated conduction bound

For the 12 V population:

```text
CSD18542KCS
RDS(on),max @ VGS=10 V = 4 mOhm
```

With ten connected devices on each logical switched node:

```text
R_A,eq,25C,max ≈ 0.4 mOhm
R_C,eq,25C,max ≈ 0.4 mOhm
```

Under the same simplified 175.4 A / 50%-per-side sensitivity model used previously:

```text
P_mainMOS,cond,25C-bound
≈ 0.5 I^2 (R_A + R_C)
≈ 12.3 W
```

Status:

```text
DATASHEET BOUND / NOT MEASURED
```

The previous 9+10-device / ~13 W bound is superseded.

---

## 10. Research consequence

The real A0 architecture is now more tightly defined:

```text
BAT+
→ two separately fused/local-bulk center-tap feeds
→ T1 + T2 center-tapped primaries
→ two common switched primary-end nodes
   A = 10 MOS
   C = 10 MOS
→ common B return
→ seven-device BAT- series/protection bank
→ BAT-
```

This means ASP already uses:

```text
10-way silicon paralleling per logical switch
split local gate driving
common-source high-current return
two magnetic center-feed paths
shared primary-end switching nodes
```

A candidate cannot claim a structural advantage merely by replacing four imagined 5-MOS branches with a more integrated switch bank; the fair A1 magnetic baseline must preserve equivalent silicon-paralleling and drive-distribution freedom.

---

## 11. Formal status

```text
Q19 drain connectivity                 = VERIFIED IN PCB
A-side main MOS connected count        = 10
C-side main MOS connected count        = 10
all main MOS sources → B               = VERIFIED
DA1/DA2 physical power node            = SAME A NODE
DB1/DB2 physical power node            = SAME C NODE
DR-A ↔ DR-A2 via 0R                    = VERIFIED
DR-B ↔ DR-B2 via 0R                    = VERIFIED
4 local driver groups                  = VERIFIED
2 logical switching functions          = VERIFIED AT CONTROL-CONNECTIVITY LEVEL
exact dynamic synchronization          = NOT YET MEASURED
subgroup current sharing                = NOT YET MEASURED
A/C switching loss                      = OPEN
A0 total BAT→X1 loss                    = OPEN
A1                                      = BLOCKED UNTIL A0 LOSS LOCALIZATION
Candidate #10                           = NOT ASSIGNED
Novelty                                 = NOT ESTABLISHED
```
