# 2026-09-26 — S2 Reference First-Circuit Contract v1

Status: `WORKING_BRANCH / REFERENCE-FALSIFICATION-BASELINE / PRE-SCHEMATIC`

```text
Novelty = NOT_ESTABLISHED
PSIM = NOT_EXECUTED
Hardware = NOT_EXECUTED
Candidate #10 = HOLD / NOT_ASSIGNED
```

## 1. Purpose and decision boundary

This record converts the S2 synthesis class into a bounded node/element contract without claiming a completed topology.

`S2_FIRST` means only:

> draw the first easily falsifiable external-commutation reference so that the transition-current path, residual-energy destination and added loss can be attacked explicitly.

It does **not** mean that S2 is preferred to S1, lower loss, lower risk, more novel or repository-mandated. The existing research requires one legal S1 graph and one legal S2 graph before ranking them.

The common system boundary remains:

```text
12 V DC -> 2 kW -> 220 Vac single phase
```

The selected v1 host is a **center-tapped resonant / magnetic-feedback self-oscillating push-pull power cell**. This is a `DESIGN_CHOICE` used to prevent classical core-saturation-triggered Royer behavior from being mixed with resonant/magnetic-feedback commutation in one undefined model. It is not an efficiency result.

## 2. Evidence labels

```text
VERIFIED         repository status or directly established repository fact
REPO_SUPPORTED   explicitly required or retained by the research records
DESIGN_CHOICE    a bounded choice introduced to make the next graph falsifiable
UNKNOWN          absent, open, unexecuted or not yet physically closed
```

`VERIFIED` in this record does not mean that the proposed electrical mechanism has been simulated or measured.

## 3. Host node contract

| Node | Role | Status |
|---|---|---|
| `NIN12` | 12-V source positive | `REPO_SUPPORTED` |
| `N0` | source return and common Q1/Q2 source node | `REPO_SUPPORTED` |
| `NCT` | center tap of the two primary halves | `REPO_SUPPORTED` |
| `ND1` | P1 outer end, Q1 drain and Coss1 high-side node | `DESIGN_CHOICE` name for a repository-required node |
| `ND2` | P2 outer end, Q2 drain and Coss2 high-side node | `DESIGN_CHOICE` name for a repository-required node |
| `NG1`, `NG2` | Q1/Q2 gate nodes | `REPO_SUPPORTED`; physical feedback connection `UNKNOWN` |
| `NSA`, `NSB` | secondary terminals | `DESIGN_CHOICE`; winding form, ratio and polarity `UNKNOWN` |
| `NHV+`, `NHV-` | reflected-load / rectified-output boundary | `DESIGN_CHOICE`; rectifier implementation `UNKNOWN` |

## 4. Host element contract

```text
Vin: NIN12 -> N0
NIN12 -> NCT
P1: NCT -> ND1
P2: NCT -> ND2
Q1: drain ND1, source N0, gate NG1
Q2: drain ND2, source N0, gate NG2
Coss1: ND1 -> N0
Coss2: ND2 -> N0
secondary S: NSA <-> NSB -> reflected load boundary
magnetic/resonant feedback: magnetic state -> NG1 / NG2
```

The first executable model must explicitly contain `Lm`, `Llk1`, `Llk2`, both nonlinear or operating-point-declared `Coss` terms, winding polarity, the feedback path and the secondary/reflected-load boundary. Values, saturation behavior, gate bias, startup assistance, turns ratio, dot polarity and frequency remain `UNKNOWN`.

## 5. S2 external-commutation sketches

Both sketches below are `DESIGN_CHOICE / HYPOTHESIS`. Neither is donor-confirmed, simulated, measured or eligible for Candidate #10.

### Sketch A — differential drain-to-drain LC reference

```text
ND1 -> Lcomm_ext -> NKA -> Cr_ext -> ND2
```

Why retain it first:

- it acts directly on the differential `ND1 <-> ND2` Coss transition;
- it does not place `Lcomm_ext` permanently in the full 12-V bulk-current path;
- it has fewer undefined coupling variables than an auxiliary-winding implementation;
- it is therefore easier to falsify.

Still `UNKNOWN`:

- whether `Cr_ext` is required;
- current direction and magnitude in each commutation interval;
- device/body-diode conduction and the legal return path;
- residual-energy destination;
- circulating RMS, VDS peak and component stress;
- startup, light-load, no-load and fault behavior;
- whether self-oscillation remains sustained.

### Sketch B — auxiliary commutation winding reference

```text
Wcomm + Lcomm_ext + symmetric steering/recovery network
```

This remains an S2 implementation family, but `Wcomm` polarity, turns ratio, coupling, steering devices, switching states and recovery destination are all `UNKNOWN`. It must not be confused with the Royer feedback winding. It is parked until those items are frozen in a separate node-level graph.

## 6. Four-state closure table

| Question | `qT1` | `qK12` | `qT2` | `qK21` |
|---|---|---|---|---|
| Conducting devices | Q1 main path; Q2 not in main transfer. Rectifier details `UNKNOWN`. | Q1-to-Q2 transition purpose `REPO_SUPPORTED`; exact MOS/body-diode/LC set `UNKNOWN`. | Q2 main path; Q1 not in main transfer. Rectifier details `UNKNOWN`. | Mirror transition purpose `REPO_SUPPORTED`; exact set `UNKNOWN`. |
| Source path | `NIN12 -> NCT -> P1/Llk1 -> ND1 -> Q1 -> N0` | Exact Vin/LC/Coss return path `UNKNOWN`. | `NIN12 -> NCT -> P2/Llk2 -> ND2 -> Q2 -> N0` | Mirror path `UNKNOWN`. |
| Load path | P1 through shared magnetic structure to secondary/reflected load | Load continuation during transition `UNKNOWN` | P2 through shared magnetic structure to secondary/reflected load | Load continuation during transition `UNKNOWN` |
| Return path | Main primary loop supported; secondary and parasitic returns `UNKNOWN` | Must be legal at all times; actual loop `UNKNOWN` | Mirror of qT1 | Actual loop `UNKNOWN` |
| Coss energy source | End-of-state `Lm/Llk/reflected-load` current is a possible source; share `UNKNOWN` | Must charge/discharge Coss1/Coss2; direction and shares `UNKNOWN` | Mirror of qT1 | Mirror of qK12 |
| Leakage-energy destination | Energy may be carried into the next transition; amount `UNKNOWN` | Must reach source, load, next state or a declared recovery element; destination `UNKNOWN` | Mirror of qT1 | Mirror of qK12 |
| Flux/reset | Full-cycle bounded flux is required | Reset function required; voltage and duration `UNKNOWN` | Full-cycle bounded flux is required | Reset function required; voltage and duration `UNKNOWN` |
| Transition condition | Outgoing Q1 must release and existing or deliberately created current must enter qK12 | Incoming Q2 turn-on requires both gate timing and actual VDS condition; threshold `UNKNOWN` | Mirror of qT1 | Mirror of qK12 |
| Failure modes | Flux walk, saturation, lost oscillation, excessive Ipk/Irms/VDS | incomplete Coss transition, illegal return, hard switching, overvoltage | Mirror of qT1 | Mirror of qK12 |
| Mandatory probes | VGS/VDS/IQ, primary/Im, secondary current, flux, output | both VGS/VDS, Icomm, flux and residual-energy destination | mirror of qT1 | mirror of qK12 |

This table exposes the missing definitions; it is not yet a closed state graph.

## 7. Stop conditions before PSIM

Do not promote either sketch to `PSIM_READY`, a candidate, a novelty claim or an efficiency claim until all of the following are explicit:

1. every switch, diode, winding, capacitor and inductor is connected to named nodes with declared polarity;
2. every qT/qK state has a closed source, load and return-current path;
3. Coss charge/discharge current and residual-energy destination are traceable;
4. full-cycle volt-second and flux balance are defined, including startup and abnormal states;
5. startup, no/light-load, load step, fault and fault-clear behavior have declared tests;
6. clamp/auxiliary DCR, ESR, core, recovery, gate and switching loss are included;
7. S1, S2 and an established external/clamp comparator share Vin, Pout, frequency range, semiconductor conduction resource and copper/core accounting;
8. system-level conclusions include the single-phase 2omega source-current and buffering obligation.

## 8. Decision

```text
Host = resonant / magnetic-feedback center-tapped self-oscillating push-pull
S2 role = REFERENCE / FALSIFICATION BOUND
rho_L = OPEN
Sketch A = FALSIFIABLE-FIRST / NOT CLOSED
Sketch B = PARKED / BLOCKED BY COUPLING AND RECOVERY UNKNOWNS
S1 versus S2 ranking = OPEN
```

The next legitimate action is to turn Sketch A into a fully named circuit graph and close `qT1 -> qK12 -> qT2 -> qK21` before assigning values or running PSIM.

## 9. Source records

- `research/WORKING_BRANCH_2026-09-17_SELF_OSCILLATION_DELTA_SYNTHESIS_V1.md` — S1/S2 roles, implementation families, state-graph requirement and open `rho_L`.
- `research/WORKING_BRANCH_2026-09-18_INTEGRATION_SCOPE_CONVERGENCE_AND_FIRST_CIRCUIT_PLAN_V1.md` — selected host family, minimum node skeleton, required nonideal elements, four-state questions, probes, matched comparison and formal statuses.
- `research/WORKING_BRANCH_2026-09-16_ROYER_ROLE_AUDIT_AND_LINEAGE_RESET_V1.md` — canonical center-tapped primary and feedback/auxiliary winding role separation.
- `research/WORKING_BRANCH_2026-09-16_MATH01_SELF_OSCILLATION_COMMUTATION_ENERGY_MODEL_V1.md` — commutation-energy necessary conditions and their proof limits.
- `research/WORKING_BRANCH_2026-09-16_MATH02_MULTIWINDING_FLUX_MODAL_BALANCE_V1.md` — flux/volt-second periodicity obligations.
- `research/WORKING_BRANCH_2026-09-16_MATH03_SELF_OSCILLATION_FREQUENCY_SENSITIVITY_V1.md` — startup, perturbation and bounded-return obligations.

