# 2026-09-16 — First Multiwinding Combination Discovery Matrix v1

Status: `WORKING_BRANCH / COMBINATION_DISCOVERY / PRE_MATH / NO_PRUNING`  
Novelty: `NOT_ESTABLISHED`  
PSIM: `NOT_EXECUTED`  
Hardware: `NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`

## 1. Purpose

This file executes the next step after defining the multiwinding target functions `T1...T13` and the emergent-research-question workflow.

The goal is **not** to choose a topology. The goal is to combine the currently identified mechanism set `M1...M10` with named-topology / SST / multiwinding ideas and record what functions each combination appears capable of producing before any mathematical proof.

The research rule is:

```text
original target
-> combination
-> possible obtained function
-> unexpected function
-> new research question
-> mathematical validation
-> PSIM only after math closure
```

A combination is not rejected simply because it does not solve the original Royer-centered problem. If it reveals a different technically useful problem inside the same 12 V -> 220 Vac / 2 kW boundary, that problem is retained.

---

## 2. Mechanism vocabulary used here

```text
M1  Current-fed power entry
M2  Direct + stored-energy transfer
M3  Winding-factor / impedance-state gain
M4  Reconfigurable effective turns
M5  Common / differential magnetic modes
M6  Controllable leakage / integrated resonance
M7  Polyphase role rotation
M8  Secondary voltage stacking
M9  Bulk-power path + small regulating path
M10 Direct DC->AC magnetic / matrix states
```

Named donor families used as physical inspiration include:

```text
Royer / Baxandall / CFPP / Weinberg
Y-source / Trans-Z / A-source
Topology Morphing / SPARC / adjustable-turn converters
LLC / CLLC / resonant isolated families
DAB / TAB / QAB / MAB / multiwinding SST
Matrix Transformer / integrated magnetics
Voltage-multiplier / VMC / switched-capacitor hybrids
Matrix-type SST / direct HF-link isolated inverter
Hybrid SST / partial-power structures
```

No combination below is yet a legal circuit topology.

---

## 3. First broad combination batch

Legend:

- `Expected T`: functions we originally expect from `T1...T13`.
- `Emergent`: useful function that may appear even though it was not the original reason for the combination.
- `New RQ`: research question exposed by the combination.
- `Boundary`: whether the idea still fits the 12 V -> 220 Vac / 2 kW system study before detailed proof.

| ID | Combination / donor idea | Expected T | Possible emergent function | New RQ exposed | Boundary |
|---|---|---|---|---|---|
| G01 | `M1+M4` Current-fed + reconfigurable turns | T1,T2,T3,T4,T6 | one connection state may also change leakage/current slope | Can one low-side state simultaneously set `Iin` behavior, `Neff` and `Zref` without putting reconfiguration switches in the full 175-A path? | YES |
| G02 | `M1+M6` Current-fed + controllable leakage/resonance | T1,T2,T7 | input inductor function and commutation inductance may partially merge | Can the current-fed energy path and ZVS energy path share one magnetic structure without excessive RMS current? | YES |
| G03 | `M1+M8` Current-fed + secondary stacking | T1,T2,T3,T9 | lower fixed transformer ratio may be sufficient | Is early current distribution + later low-current voltage stacking better than forcing the HFT alone to supply the full gain? | YES |
| G04 | `M1+M7` Current-fed + polyphase role rotation | T1,T2,T5,T10 | current-source input may keep aggregate source current continuous while one branch changes role | Can one branch temporarily leave transfer service without creating source-current or output-power discontinuity? | YES |
| G05 | `M2+M5` Direct/stored transfer + common/differential magnetic modes | T2,T5,T7 | common mode may carry direct power while differential mode stores/releases transient energy | Can direct transfer and flyback-like temporary energy transfer be separated by magnetic mode rather than separate magnetic components? | YES |
| G06 | `M2+M6` Direct/stored transfer + controllable leakage | T2,T7 | stored magnetic energy may become the commutation energy reservoir | Can leakage/magnetizing energy be intentionally sized to serve both delayed transfer and device capacitance commutation? | YES |
| G07 | `M2+M7` Direct/stored transfer + role rotation | T2,T5,T10 | only one phase at a time may operate in temporary-storage mode | Can a rotating storage branch reduce individual magnetic stress while maintaining total transfer? | YES |
| G08 | `M3+M4` Impedance-state gain + reconfigurable turns | T3,T4,T6 | winding factor and actual participating turns may become one structural gain variable | Is there a legal state law where coupled-impedance gain and `Neff` reconfiguration reinforce rather than duplicate each other? | YES |
| G09 | `M3+M5` Impedance-state gain + magnetic modes | T3,T4,T5 | gain may depend on which magnetic eigenmode is excited | Can a converter obtain different gain/reflected impedance by changing magnetic mode rather than only changing turns or duty? | CONDITIONAL |
| G10 | `M3+M8` Impedance-state gain + secondary stacking | T3,T4,T9 | transformer gain burden can be shared between magnetic coupling and electric-field stacking | What gain partition minimizes low-side current, turns ratio, capacitor stress and secondary RMS simultaneously? | YES |
| G11 | `M4+M5` Reconfigurable turns + common/differential modes | T4,T5,T6 | same state may change `Neff`, `Zref` and modal inductance | Can one `q` produce `q -> {Neff, Zref, Leff}` with useful power transfer in both states? | YES |
| G12 | `M4+M6` Reconfigurable turns + controllable leakage | T4,T6,T7 | same winding reconnection may set gain and commutation energy | Can `q -> {Neff, Zref, Lcomm}` be realized physically without unacceptable transient current during reconnection? | YES |
| G13 | `M4+M7` Reconfigurable turns + role rotation | T5,T6,T10 | gain transitions may be staggered across branches | Can discrete gain changes be time-staggered so aggregate output changes smoothly without all branches reconfiguring at once? | YES |
| G14 | `M4+M8` Reconfigurable turns + secondary stacking | T3,T4,T6,T9 | multiple low-ratio winding states may create several secondary voltage levels | Can a small number of winding sections replace an extreme fixed turns ratio and part of the downstream modulation burden? | YES |
| G15 | `M5+M6` Magnetic modes + controllable leakage/resonance | T5,T7,T8 | different eigenmodes may naturally present different inductances for transfer vs commutation | Can common mode be low-leakage for efficient transfer while differential mode is intentionally high-inductance for commutation? | YES |
| G16 | `M5+M7` Magnetic modes + polyphase role rotation | T5,T7,T10 | role rotation may excite different magnetic modes in time | Can `(T,T,K)` rotation be implemented as mode rotation rather than three independent transformers? | YES |
| G17 | `M5+M8` Magnetic modes + secondary stacking | T5,T8,T9 | different modal flux combinations may synthesize additive/subtractive secondary voltages | Can secondary voltage states be created by flux-mode combination without large circulating currents? | CONDITIONAL |
| G18 | `M6+M7` Controllable leakage + role rotation | T7,T10 | the branch entering K-role may temporarily expose a different `Lcomm` | Can only the commutating branch see large effective inductance while transfer branches remain tightly coupled? | YES |
| G19 | `M6+M8` Controllable leakage + voltage stacking | T7,T9 | leakage energy may be used during transitions between stacked-voltage states | Can secondary stack-state transitions be soft-commutated using intentionally shaped leakage? | YES |
| G20 | `M7+M8` Role rotation + secondary stacking | T9,T10 | branch phase and voltage contribution could be co-scheduled | Can phase-displaced branches build a stepped aggregate HV waveform before the final inverter stage? | YES |
| G21 | `M9 + multiwinding SST` Bulk path + small regulating port | T5,T11 | one lower-VA winding may correct a full-power transfer path | What minimum processed-power fraction is needed to regulate the 12-V-to-HV transfer without full-power PWM burden on every branch? | YES |
| G22 | `M10 + matrix-type SST` Direct HF-link / matrix states | T12 | useful AC voltage states may appear before a stiff HVDC bus | Can the W1/W2 magnetic stage reduce post-HFT rectifier/VSI processing while still closing single-phase `2omega` energy? | CONDITIONAL |
| G23 | `M4+M9` Reconfigurable turns + small regulating path | T6,T11 | coarse structural ratio + fine low-VA correction | Can structural gain provide coarse regulation while a fractional-power port supplies only fine correction? | YES |
| G24 | `M1+M5+M8` Current-fed + modal magnetics + secondary stacking | T1,T3,T5,T8,T9 | low-side split and high-side stack may be linked through one shared-core modal structure | Is matrix-transformer geometry a better primary research variable than converter branch count? | YES |
| G25 | `M1+M4+M6` Current-fed + reconfigurable turns + controllable leakage | T1,T3,T4,T6,T7 | one state may jointly change input-current slope, gain and commutation energy | Can a single multiwinding state law jointly control `Iin`, `Neff`, `Zref` and `Lcomm` with fewer added components than separate solutions? | YES |
| G26 | `M5+M7+M8` Magnetic modes + role rotation + voltage stacking | T5,T8,T9,T10 | rotating magnetic modes may also rotate secondary voltage contributions | Can a multi-limb / multiwinding structure synthesize gain states while one branch performs commutation support? | CONDITIONAL |
| G27 | `M3+M4+M8` Impedance gain + reconfigurable turns + stacking | T3,T4,T6,T9 | gain may be shared across three mechanisms, reducing stress on each | What gain allocation minimizes transformer ratio, switch stress and capacitor charge-transfer loss? | YES |
| G28 | `M1+M9` Current-fed bulk path + fractional regulator | T1,T2,T11 | nearly constant current-fed DCX-like transfer with small correction port | Can the raw 12-V high-current stage be kept near an efficient fixed operating point while regulation is moved to a lower-power path? | YES |

All `G01...G28` remain `GENERATED / PRE_MATH / NOT_FALSIFIED`.

---

## 4. What changed relative to the original idea

The original multiwinding idea was dominated by this question:

```text
Can multiple windings / primaries distribute the 12-V high current early,
then transfer power through one shared magnetic structure?
```

The first combination batch expands that into several distinct possible research problems.

### 4.1 The problem may be `state-coupled gain + commutation`, not current split

`G11`, `G12`, and `G25` suggest a different target:

```text
q -> {Neff(q), Zref(q), Leff/Lcomm(q)}
```

If this can be closed mathematically, the important contribution may be a winding state that simultaneously changes power gain and commutation energy rather than simply splitting current.

### 4.2 The problem may be `modal magnetics`, not more windings

`G05`, `G15`, `G16`, `G17`, `G26` suggest that the important variable could be magnetic rank and modal inductance:

```text
Phi_common       -> bulk transfer
Phi_differential -> balancing / commutation / transient storage
```

In that case, merely adding more physical windings is not the research result. The residual problem becomes whether one magnetic structure can provide sufficiently independent useful modes.

### 4.3 The problem may be `gain partition`, not extreme turns ratio

`G03`, `G10`, `G14`, `G27` suggest splitting total gain among:

```text
magnetic turns ratio
+ winding-state gain
+ secondary voltage stacking
```

This may expose an optimum gain-allocation problem rather than a single new converter graph.

### 4.4 The problem may be `role continuity`, not interleaving

`G04`, `G07`, `G13`, `G16`, `G18`, `G20`, `G26` move the phase question from simple ripple cancellation to:

```text
which branch transfers?
which branch commutates?
which branch changes gain state?
```

The new research question becomes whether aggregate power can stay continuous while individual winding roles change.

### 4.5 The problem may be `fractional processing`, not full-power multifunctionality

`G21`, `G23`, and `G28` suggest that forcing every new function to process 2 kW may be unnecessary. A lower-VA port may perform regulation or correction while another path carries bulk power.

### 4.6 The problem may become `reduced-stage AC synthesis`

`G20`, `G22`, and `G26` can produce useful voltage-state information upstream of the conventional VSI. This does not prove that X3 can be removed. It exposes a separate question:

```text
Can post-HFT processing be reduced without worsening RMS current,
filtering, commutation, or 2omega energy handling?
```

---

## 5. Emergent problem registry from this batch

The broad batch creates the following additional research questions beyond ERQ-1...ERQ-10.

### ERQ-11 — Gain/commutation coupling versus reconfiguration transient

If winding reconfiguration changes both `Neff` and `Lcomm`, does the transition itself create current spikes, circulating energy, or dead intervals that erase the steady-state benefit?

### ERQ-12 — Magnetic rank requirement

What is the minimum independent magnetic modal rank required before `common-power + differential-commutation` is physically distinct rather than an equivalent leakage model of a conventional transformer?

### ERQ-13 — Gain allocation optimum

For the required 12-V to high-voltage transformation, how should gain be divided among transformer ratio, winding-state gain and secondary stacking to minimize total RMS current and loss?

### ERQ-14 — Transfer continuity during role rotation

When one branch enters a K / reset / storage state, what supplies its missing share of instantaneous power: remaining branches, stored energy, or output capacitance?

### ERQ-15 — Controllable leakage versus coupling quality

How much intentional leakage is useful for ZVS/resonance before it produces unacceptable reactive RMS current, regulation error, or copper/core penalty?

### ERQ-16 — Structural current sharing versus copper duplication

Can matrix/multiwinding geometry reduce termination and local hot-spot loss under equal copper volume, or is the apparent sharing simply duplicated conductor area?

### ERQ-17 — Secondary stacking transition loss

Does secondary voltage stacking reduce turns ratio enough to compensate capacitor ESR, charge redistribution, diode/switch stress and state-transition loss?

### ERQ-18 — Fractional processed-power ratio

For partial-power variants, what is the processed-power fraction `alpha = P_processed / P_out`, and does the correction path stay low-VA over the complete input/load range?

### ERQ-19 — X1/X3 overlap versus 2omega relocation

If direct HF-link voltage states reduce rectifier/VSI stages, where does the unavoidable single-phase double-line-frequency energy ripple move?

### ERQ-20 — Magnetic integration as the actual novelty locus

If the electrical converter graph reduces to known CFPP, DAB/MAB, LLC, Y-source, or matrix-converter families, can the residual research problem still reside in a demonstrably different integrated magnetic state space?

---

## 6. Minimum state variables required before mathematics

Every G-candidate must now be converted into an explicit state graph. At minimum define:

```text
q                structural state
s_j(q)           semiconductor connection state
r_W1(q), r_W2(q) winding roles
Neff(q)          effective participating turns
Zref(q)          reflected impedance
Lmatrix(q)       winding/mode inductance matrix
Lcomm(q)         effective commutation path inductance
Phi_mode,j(q)    independent magnetic-mode fluxes
I_W1, I_W2       winding currents
Iin              source current
Vsec,k(q)        secondary section voltages
Ppath,k(q)       instantaneous power paths
Wstored(q)       explicit stored energy, if any
phi_k            branch phase schedule where used
```

No mathematics should be performed from mechanism names alone.

---

## 7. Coverage set for the next state-graph step — not a ranking

To avoid writing 28 full circuit graphs at once, the next step should use a **coverage set**, not a best/worst ranking. The following nine combinations span the main newly exposed physics:

```text
G01  current-fed + reconfigurable turns
G03  current-fed + secondary stacking
G05  direct/stored transfer + magnetic modes
G11  reconfigurable turns + magnetic modes
G15  magnetic modes + controllable leakage
G16  magnetic modes + role rotation
G21  bulk path + small regulating port
G22  direct HF-link / matrix states
G25  current-fed + reconfigurable turns + controllable leakage
```

Reason for using these nine: together they cover input-current behavior, gain, impedance transformation, magnetic mode, leakage/commutation, phase-role reassignment, partial-power processing and possible X1/X3 overlap. They are not declared superior to the other G-candidates.

---

## 8. Next execution rule

For each coverage-set combination, write the smallest legal circuit/state description before solving equations:

```text
1. terminals and winding polarity
2. q1 / q2 / ... switch states
3. W1/W2 role in every state
4. source-current path
5. output-current path
6. flux/reset path
7. stored-energy path, if any
8. secondary combination path
9. expected Neff/Zref/Lcomm state changes
10. newly exposed research question
```

Then apply the mathematical gates already defined:

```text
MG1 state legality / power continuity
MG2 volt-second and flux balance
MG3 ampere-turn / sharing consistency
MG4 gain and reflected impedance
MG5 winding/switch RMS and peak stress
MG6 commutation / resonance energy
MG7 energy conservation
MG8 first loss ledger
MG9 single-phase boundary closure
```

Only combinations with sufficient mathematical closure proceed to PSIM.

---

## 9. Current conclusion

This batch does not identify a final topology. It changes the research space from one narrow question — `how to split the 12-V high current with a multiwinding transformer` — into a controlled set of physically distinct questions:

```text
current distribution
state-dependent gain
reflected impedance
magnetic modal rank
controllable leakage
role rotation
secondary voltage stacking
partial-power regulation
direct HF-link contribution
```

The central synthesis question for the next stage is therefore:

> Can a legal W1/W2 state graph make one physical multiwinding magnetic structure control more than one of `current path`, `Neff`, `Zref`, `Lcomm`, `power role`, or `secondary voltage state`, while keeping flux, RMS current, energy conservation and loss physically closed?

That question is now ready to be attacked mathematically candidate by candidate, beginning with explicit state graphs rather than topology names.