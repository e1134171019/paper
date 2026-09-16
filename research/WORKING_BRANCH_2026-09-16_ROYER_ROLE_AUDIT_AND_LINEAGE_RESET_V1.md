# 2026-09-16 — Royer Role Audit and Lineage Reset v1

Status: `WORKING_BRANCH / ROLE_AUDIT / LINEAGE_RESET / PRE_MATH_REBASE`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Why this reset is needed

Recent Math-2/Math-3 work temporarily treated `W1` and `W2` as independent peer load-bearing power ports, influenced by SST/MAB/multiport literature. That interpretation is **not the canonical starting point of the original Royer-derived research path**.

The original host should remain a named self-oscillating push-pull lineage first, then improved descendants should donate concrete modifications.

Therefore:

```text
named host circuit
-> documented improved descendant
-> exact winding/switch role audit
-> extract one modification concept
-> transplant only after role compatibility is proven
```

Do not invent new winding roles merely because an SST/MAB architecture allows them.

---

## 2. Canonical Royer-role baseline

For the classical Royer / saturating self-oscillating push-pull family:

```text
Vin -> center tap of main primary

primary half P1 -> Q1
primary half P2 -> Q2

feedback winding F1/F2 -> drives Q1/Q2 gate/base network

secondary S -> output power transfer
```

Key distinction:

```text
P1 and P2 = two halves/sections of ONE center-tapped main primary,
            alternately energized through Q1/Q2.

They are both part of the main-power path,
but they are NOT automatically two independent SST/MAB peer ports.
```

A separate feedback winding does not directly “feed back into P1/P2.” It senses/couples transformer state and drives the switch-control terminals. By driving Q1/Q2 alternately, it indirectly selects which primary half conducts.

For MOSFET wording:

```text
feedback winding -> gate network of Q1/Q2
Q1/Q2 -> select P1/P2 current path
P1/P2 -> excite core / transfer power
```

---

## 3. Working notation reset

To avoid the previous ambiguity, stop using `W1/W2/W3` without role suffixes.

Use:

```text
P1 = main center-tapped primary, first half
P2 = main center-tapped primary, second half
F  = feedback / auxiliary drive winding
S  = output / secondary power winding
```

If the feedback winding itself is center-tapped, use:

```text
F1, F2
```

If a later improvement introduces an additional power-bearing winding, do NOT call it `F` merely because it is auxiliary. Give it a new role label such as:

```text
PAUX = auxiliary power winding
PCOMM = commutation-energy winding
PREG = correction / partial-power winding
```

but only after a documented lineage shows the role or the proposed modification explicitly creates it.

---

## 4. Literature-grounded named-circuit lineage

### L0 — Classical Royer oscillator / self-oscillating push-pull

Role pattern:

```text
center-tapped main primary P1/P2
+ two switches Q1/Q2
+ magnetic feedback winding F/F1/F2
+ optional output secondary S
```

The feedback winding provides positive feedback to the switch control terminals and sustains alternate conduction.

### L1 — Baxandall current-switching / resonant self-oscillating push-pull

Baxandall retains a center-tapped switched winding and a feedback winding, but adds/uses a tuned network and a source/current choke so the current is steered between switching devices while the resonant tank determines the waveform.

Transplantable concept:

```text
self-oscillation does not have to rely only on hard core saturation;
resonant/current-fed state can participate in the natural switching condition.
```

### L2 — Self-oscillating push-pull Class-E / Class-E-F descendants

Published work shows self-oscillating push-pull resonant converters that deliberately incorporate transistor parasitic capacitance into the resonant network to reduce gate-drive complexity and achieve soft-switching-style operation.

Transplantable concept:

```text
Coss / transistor parasitic capacitance can be part of the intended resonant state,
not only a parasitic to be overcome.
```

### L3 — 2023 self-oscillated feedback network for push-pull resonant converters

A modern IEEE TPEL paper demonstrates a self-oscillated feedback network expandable to push-pull resonant topologies, using coupled-inductor / virtual-ground behavior to maintain complementary symmetry and satisfy oscillation criteria.

Transplantable concept:

```text
self-oscillated feedback can be redesigned as a network-level function;
a dedicated classical Royer feedback winding is not the only possible realization.
```

Do not copy its VHF implementation directly into the 12-V/2-kW boundary.

### L4 — self-oscillation + outer tracking / regulation concept

Recent self-oscillating converter work in resonant/IPT systems separates a self-oscillating state from a power-injection/control state and uses a phase-tracking outer loop to follow parameter/load drift without replacing the inner oscillation mechanism.

Transplantable concept:

```text
inner natural oscillation
+
outer tracking / bounded correction
```

This supports the earlier “self-excited + externally coordinated” research direction, but implementation must be re-derived for the selected push-pull host.

---

## 5. Role-by-role audit before adding new functions

Every desired function must now be matched to a documented named circuit or documented improvement before synthesis.

### Function A — self-oscillating switch drive

Grounded donors:

```text
Royer / Jensen-style self-oscillating push-pull
Baxandall current-switching oscillator
modern self-oscillated push-pull resonant feedback network
```

Required audit:

```text
what physical variable creates positive feedback?
core saturation?
resonant voltage/current phase?
coupled-inductor state?
```

### Function B — external correction without replacing self-oscillation

Grounded concept donors:

```text
phase tracking / outer regulation around self-oscillation
current/flux balancing control in push-pull descendants
```

Required audit:

```text
what does the outer loop change?
threshold?
bias?
frequency pull?
power-injection interval?
flux balance?
```

### Function C — leakage energy use / soft switching

Grounded donors:

```text
self-oscillating Class-E/F push-pull
active-clamped current-fed push-pull
resonant push-pull descendants
```

Required audit:

```text
which inductance supplies commutation energy?
where does leakage energy go?
Coss/resonant capacitor/clamp?
```

### Function D — auxiliary winding carries power or changes role

Status:

```text
NOT YET GROUNDED FOR THE ORIGINAL ROYER HOST.
```

Classical Royer feedback winding is a drive/feedback winding, not automatically a main-power winding.

If the research wants:

```text
primary winding <-> auxiliary winding role switching
```

then a separate lineage search is mandatory before assuming it is legal/useful. Candidate donor families to inspect include:

```text
reconfigurable transformer / adjustable-turn converters
resonant converters with auxiliary winding turns
multiwinding / matrix-transformer descendants
push-pull converters with auxiliary winding used for soft switching/reset
```

But none of these should be relabeled as Royer until the actual power graph is reconciled.

### Function E — SST / MAB / multiport ideas

SST remains an architecture donor only:

```text
parallel low-voltage paths
series/stacked higher-voltage paths
shared magnetic infrastructure
reduced-switch multiport concepts
partial-power correction paths
```

It does NOT retroactively redefine P1/P2 as independent peer ports in the classical Royer host.

---

## 6. Correction to recent Math-2 / Math-3 interpretation

The modal mathematics itself can remain useful as an exploratory tool, but the assumption:

```text
W1 = independent peer power port
W2 = independent peer power port
```

must not be treated as canonical.

For the original Royer host, the correct first mapping is:

```text
P1/P2 = complementary halves of one center-tapped primary
F     = self-oscillation feedback/drive winding
S     = output winding
```

Only after a documented improvement adds a second independent power-primary path should a true peer-port modal model become the main line.

Therefore Math-2/Math-3 are retained as a conditional branch, not deleted, but the lineage role audit takes precedence before further Math-4 work.

---

## 7. Immediate next research action

Pause equal-resource `peer-port W1/W2` Math-4.

Instead create a **named-circuit + improved-circuit function matrix**:

```text
Row = one named host / descendant
Columns:
- P1/P2 role
- feedback winding role
- auxiliary winding role
- Q1/Q2 drive path
- oscillation trigger variable
- resonant/leakage path
- soft-switching mechanism
- external-control entry point
- whether auxiliary winding carries meaningful power
- whether winding role changes by state
- relevance to 12-V / 2-kW first conversion
```

Minimum first set:

```text
1. Classical Royer
2. Jensen self-oscillating push-pull
3. Baxandall current-switching oscillator
4. Self-oscillating push-pull Class-E/F
5. 2023 self-oscillated feedback network for push-pull resonant converters
6. Active-clamped / resonant current-fed push-pull descendants
7. one reconfigurable/auxiliary-winding power converter lineage
8. one SST/MAB/matrix-transformer architecture donor
```

Only after this matrix is built should we decide whether the proposed method is:

```text
Royer + resonant/leakage improvement
Royer + externally coordinated feedback improvement
Baxandall-derived current-fed self-oscillation improvement
or another named host with a better match to the 12-V/2-kW boundary.
```

---

## 8. Source anchors

- G. H. Royer, AIEE Transactions, 1955, pp. 322–327 (classic Royer lineage; cited by later patent literature).
- P. J. Baxandall, “Transistor Sine-Wave LC Oscillators,” 1959; current-switching oscillator with feedback winding and source choke.
- R.-L. Lin, F.-Y. Chen, “Self-oscillating push-pull class-E/F converters,” APCCAS 2004, DOI `10.1109/APCCAS.2004.1412961`.
- D. Kim, J. Chae, K.-B. Park, G.-W. Moon, “A Self-Oscillated Feedback Network for Push-Pull Resonant Power Converters,” IEEE TPEL, 2023, DOI `10.1109/TPEL.2023.3303649`.
- L. Chen et al., “Self-Oscillating Converter Based on Phase Tracking Closed Loop for a Dynamic IPT System,” Energies, 2024, vol. 17, 1814.
- Q. Wu et al., “Active-clamped ZVS current-fed push-pull isolated dc/dc converter for renewable energy conversion applications,” IET Power Electronics, 2018, DOI `10.1049/iet-pel.2017.0144`.

This file is a role reset / research-method correction, not a novelty claim.