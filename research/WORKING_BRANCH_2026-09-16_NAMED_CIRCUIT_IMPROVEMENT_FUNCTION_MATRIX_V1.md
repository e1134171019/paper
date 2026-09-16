# 2026-09-16 — Named-Circuit Improvement Function Matrix v1

Status: `WORKING_BRANCH / LINEAGE_FUNCTION_MATRIX / PRE-SYNTHESIS`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Purpose

Reset the research method to:

```text
named circuit
-> documented improved circuit
-> exact winding / switch role comparison
-> extract one concrete improvement concept
-> only then transplant into the 12-V / 2-kW boundary
```

The matrix below is intentionally role-first. It prevents the recent mistake of assigning new meanings to `W1/W2/W3` before checking what the source circuit actually does.

Canonical notation for the Royer-derived host:

```text
P1 = first half of center-tapped main primary
P2 = second half of center-tapped main primary
F  = feedback / drive winding
S  = output secondary
Q1/Q2 = alternating main switches
```

If a later circuit introduces a genuinely different auxiliary power function, use a separate role label such as `PAUX`, `PCOMM`, or `PREG` rather than reusing `F`.

---

## 2. Function matrix

| Named circuit / descendant | Main power winding role | Feedback / auxiliary magnetic role | How Q1/Q2 or power switches are driven / commutated | Oscillation / timing origin | Leakage / resonance treatment | External-control entry | Does auxiliary winding carry main power? | Does winding role change by state? | What we may transplant into our boundary |
|---|---|---|---|---|---|---|---|---|---|
| Classical Royer self-oscillating push-pull | `P1/P2` are the two halves of one center-tapped main primary; they alternately carry the main input-power path | separate feedback winding couples transformer state back to transistor bases/gates; output secondary is separate | positive magnetic feedback makes Q1/Q2 alternate | classically core saturation / transformer state causes reversal | no deliberate leakage-energy function in the classical baseline | startup / bias can be added, but base oscillation is self-generated | `F`: NO, primarily drive/feedback | `P1/P2` alternate conduction, but `F` does not become a main-power winding | retain the host role structure and the fact that magnetic feedback controls the switch pair |
| Jensen self-oscillating push-pull | a separate linear main transformer carries useful power | a separate magnetic-saturation transformer performs the self-oscillation-frequency and drive function | saturation-transformer secondary drives the push-pull transistor bases; its primary is coupled to collector-side state | saturation of the dedicated drive transformer rather than forcing the main power transformer to saturate | not primarily a leakage-recovery topology | auxiliary start/protection networks possible | drive transformer: NO main-load power; main transformer remains the power transformer | magnetic roles are physically separated between two transformers rather than time-swapped | very important donor: separate `oscillation magnetics` from `power magnetics` instead of forcing one core/winding set to do both |
| Baxandall current-switching / LC self-oscillating family | center-tapped switched winding remains the main HF power path | feedback may be via tap or separate winding, while a source/current choke participates in current steering | transistor pair alternates through positive feedback and resonant/current-switching dynamics | LC resonance / current switching participates in timing; not only hard core saturation | resonant tank is intentional | regulation may act on supply/current path; self-oscillation remains intrinsic | feedback winding itself is not the main power path | main current alternates by state; feedback role remains feedback | donor for replacing hard-saturation timing with resonance/current-fed natural commutation |
| Self-oscillating push-pull Class-E/F (2004) | push-pull power devices/windings still carry main power | feedback/self-oscillation network supplies gate-driving behavior | self-oscillation is retained while Class-E / inverse-F waveform shaping is added | resonant-state conditions set the periodic behavior | transistor parasitic capacitance is deliberately incorporated into the resonant network | not the main contribution; self-oscillation is integral to the converter | no evidence that a classical feedback winding is promoted to full main-power winding | resonant states change device voltage/current waveform, not basic winding identity | donor for `self-oscillation + intentional Coss/resonant use` rather than treating Coss as only a burden |
| Self-oscillated feedback network for push-pull resonant power converters (Kim et al., IEEE TPEL 2023) | push-pull resonant power stage carries the useful power | self-oscillated feedback is implemented as a network using coupled-inductor / virtual-ground behavior rather than relying on only a conventional single-ended feedback form | feedback network maintains complementary symmetry and drives the push-pull pair | oscillation criteria of the resonant power oscillator / feedback network | resonance is part of the host power oscillator | conceptually compatible with outer supervision, but the paper focuses on self-oscillated feedback | feedback network is a drive function, not established as a 2-kW main-power auxiliary port | role is network-level feedback, not winding role-swapping | donor for redesigning the `feedback function` itself; proves self-oscillation need not equal classical Royer feedback winding implementation |
| Active-clamped current-fed push-pull (Wu et al., IET PE 2018) | current-fed push-pull main transformer path carries bulk power | clamp branch is an added power-processing/commutation path, not a traditional feedback winding | externally switched primary devices; not self-oscillating | fixed/controlled switching | transformer leakage is explicitly used in the ZVS condition; clamp suppresses spike and recovers/redirects energy | ordinary gate-control/modulation | clamp path processes transition energy, not the full output as an auxiliary transformer winding | leakage/clamp path changes role during switching intervals | donor for `how much leakage is useful`; paper explicitly shows trade-off: more Llk widens ZVS range but raises switch voltage stress |
| Push-pull forward with transformer auxiliary winding for ZCS (2004, discovery source) | main transformer windings remain the main power path | auxiliary transformer winding is used to create a soft-switching resonant path; reported resonant network is outside the main power loop | PWM controlled; auxiliary winding shapes ZCS transition | commanded switching, auxiliary resonance modifies transition | auxiliary winding/resonant network handles transition energy | full external PWM | auxiliary winding processes resonant/transition power, not identified as full main output power | auxiliary winding participates strongly only in the transition function | donor candidate for `auxiliary winding handles commutation without putting resonant current in raw main-power loop`; requires primary-source verification before formal adoption |
| Reconfigurable-secondary LLC (Queiroz & Costa, 2025) | primary power transformer role stays unchanged | additional/sectioned secondary winding plus one switch changes the active rectifier/turns configuration | externally controlled LLC, not self-oscillating | fixed switching frequency in the reported design | changing winding connection also changes the transformer/rectifier operating state; later detailed work shows leakage/resonant parameters can change with connection | secondary-side structural state selector | auxiliary secondary section does carry output power when inserted; this is a real power-winding role, unlike Royer `F` | YES: winding sections participate differently by mode | strong donor for our earlier idea `primary/auxiliary power winding state change`, but it must be transplanted as a reconfigurable-power-winding concept, not confused with Royer feedback |
| Matrix-transformer LLC (Huang, Ji, Lee, 2014) | multiple elemental transformer structures distribute real power | no classical feedback winding role; geometry/termination are co-designed | externally driven LLC | resonant converter control | leakage and AC resistance are reduced; flux cancellation and integrated secondary termination reduce winding/termination loss | normal LLC control | elemental windings are genuine main-power paths | connection/layout distributes current continuously rather than feedback-role swapping | donor for the physical reason multiwinding current distribution can help: termination, AC resistance, flux cancellation, not merely `I/N` arithmetic |
| Reduced-switch MAB for modular SST (Khani et al., 2025) | multiple transformer windings are genuine peer active power ports in MAB/SST architecture | no Royer-type feedback winding; bridges on multiple ports process real power | externally modulated active bridges, TCM used for soft switching | commanded bridge modulation | transformer/link current is shaped by TCM; soft-switching is modulation based | full external modulation | YES: every active port/winding is a power port | ports change power-transfer state through bridge modulation | architecture donor only: peer power ports and shared semiconductor legs are valid in SST/MAB, but this must NOT be retroactively mapped onto classical Royer `P1/P2/F` roles |

---

## 3. What this matrix corrects

### 3.1 Royer `P1/P2` are not MAB peer ports

They both carry main power, but in the classical host they are complementary halves of one center-tapped primary:

```text
Q1 ON -> P1 active
Q2 ON -> P2 active
```

That is different from:

```text
Port A independently transfers power
Port B independently transfers power
```

as in MAB/SST.

### 3.2 Classical feedback winding `F` is not automatically a power auxiliary winding

The correct signal chain is:

```text
transformer magnetic state
-> F induced voltage
-> Q1/Q2 control terminals
-> select P1 or P2 conduction
```

Therefore `F` affects P1/P2 indirectly through the switches.

### 3.3 An auxiliary winding CAN process power in other named lineages

The reconfigurable-LLC literature proves that an additional winding section can be inserted into a real output-power path and change effective turns ratio.

The ZCS auxiliary-winding push-pull literature indicates an auxiliary winding can also be dedicated to commutation / resonant energy without putting that resonant network directly in the main power loop.

Therefore the question is not:

```text
Can an auxiliary winding ever carry power?
```

It can.

The real question is:

```text
Which named lineage gives the exact auxiliary-winding role we want,
and can that role coexist with Royer/Jensen self-oscillation under our 12-V/2-kW boundary?
```

---

## 4. Immediate synthesis implications

The first synthesis should NOT start from `W1/W2/W3`.

It should start from one selected host and one selected documented modification.

### Path H1 — Royer host + resonant/soft-switching improvement

```text
Host:
P1/P2 + F + S + Q1/Q2

Import:
Class-E/F or active-clamp/resonant concept

Question:
Can leakage/Coss/resonant energy assist the natural Royer commutation without replacing F-driven self-oscillation?
```

### Path H2 — Jensen host + power/oscillation magnetic separation

```text
Host:
main linear power transformer
+
separate saturation/drive transformer

Import:
modern resonant/self-oscillated feedback improvement

Question:
Can the oscillation magnetic element be redesigned so main 2-kW transformer avoids saturation-driven timing?
```

### Path H3 — Royer/Jensen host + auxiliary commutation winding

```text
Host self-oscillation remains recognizable
+
PCOMM auxiliary winding / resonant branch
```

Question:

```text
Can PCOMM handle only transition energy while P1/P2 remain the bulk-power path?
```

This is closer to the user's original `main winding + auxiliary winding` concept than the recent peer-port model.

### Path H4 — self-oscillating host + reconfigurable power winding

```text
Royer/Jensen self-oscillation mechanism
+
separate PAUX power winding state inspired by reconfigurable-transformer literature
```

Possible future state:

```text
q1 -> only base power winding participates
q2 -> base + PAUX participate
```

which may alter:

```text
Neff(q)
Zref(q)
Lcomm(q)
```

But this is **not yet a circuit**. It requires a legal state graph proving that the reconfiguration switch is not placed in a catastrophically lossy raw-12-V path.

### Path H5 — SST/MAB remains system architecture donor

After a valid self-oscillating cell is obtained, SST ideas may tell us how multiple cells are combined:

```text
low-voltage parallel
higher-voltage series/stacked
shared switch legs
shared HF link
partial-power correction
```

Do not use SST to redefine the inner Royer winding roles before that cell exists.

---

## 5. Current best interpretation of the user's original idea

The original intent is better represented as:

```text
main center-tapped power winding P1/P2
+
feedback / self-oscillation magnetic function F
+
possible additional auxiliary power or commutation winding PAUX / PCOMM
+
external correction of the self-oscillating behavior
```

NOT:

```text
W1 = independent power port
W2 = independent power port
W3 = self-feedback port
```

The exact choice between `F`, `PCOMM` and `PAUX` should now be decided from documented named-circuit descendants rather than by naming first.

---

## 6. Evidence / source anchors

### Strong / primary or institutional sources

- Royer structure evidence: later Royer oscillator patents explicitly show a center-tapped primary split into `P1/P2`, feedback winding, and alternating switches; original lineage traces to G. H. Royer, AIEE 1955.
- P. J. Baxandall, “Transistor Sine-Wave LC Oscillators,” Proc. IEE, 1959; later RRE lecture reproduces/derives the oscillator principles.
- R.-L. Lin, F.-Y. Chen, “Self-oscillating push-pull class-E/F converters,” APCCAS 2004, DOI `10.1109/APCCAS.2004.1412961`.
- D. Kim, J. Chae, K. B. Park, G. W. Moon, “A Self-Oscillated Feedback Network for Push-Pull Resonant Power Converters,” IEEE TPEL, 2023, DOI `10.1109/TPEL.2023.3303649`.
- Q. Wu et al., “Active-clamped ZVS current-fed push–pull isolated dc/dc converter for renewable energy conversion applications,” IET Power Electronics, 2018, DOI `10.1049/iet-pel.2017.0144`.
- S. S. Queiroz, L. F. Costa, “LLC Resonant Converter With Reconfigurable Secondary-Side for Output Voltage Regulation,” IEEE TCAS-II, 2025, DOI `10.1109/TCSII.2025.3625415`.
- D. Huang, S. Ji, F. C. Lee, “LLC Resonant Converter With Matrix Transformer,” IEEE TPEL, 2014, DOI `10.1109/TPEL.2013.2292676`.
- S. Khani, S. H. Hosseini, M. Sabahi, “Reduced switch multiple active bridge DC-DC converter for modular solid-state transformers,” Scientific Reports, 2025, DOI `10.1038/s41598-025-23427-8`.

### Discovery-only / needs primary-source recheck before formal Delta adoption

- “ZCS push-pull forward PWM converter using transformer auxiliary winding,” 2004. Current accessible evidence is abstract/index level; retain only as a donor lead until primary full paper or stronger bibliographic source is verified.

---

## 7. Next execution

The next step is to select **two host paths only**, not combine all rows.

Recommended comparison set for the next gate:

```text
Host-A = Royer single-transformer host
Host-B = Jensen separated-oscillation / main-power-transformer host
```

For each host, build three modification trials on paper only:

```text
M-A: resonant / Coss / leakage-assisted commutation
M-B: auxiliary commutation winding PCOMM
M-C: externally bounded self-oscillation
```

Then compare:

```text
which host keeps the self-oscillation concept most intact,
which host keeps the 2-kW power transformer out of saturation-driven timing,
and where a future PAUX reconfigurable winding can be inserted with the least raw-12-V penalty.
```

Only after this host comparison should mathematical verification resume.