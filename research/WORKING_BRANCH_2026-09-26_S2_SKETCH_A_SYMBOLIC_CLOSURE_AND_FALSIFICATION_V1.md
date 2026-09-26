# 2026-09-26 — S2 Sketch A Symbolic Closure and Falsification v1

Status: `WORKING_BRANCH / SYMBOLIC_EDGE_MODEL / NOT_TOPOLOGY_CLOSED`

```text
Novelty = NOT_ESTABLISHED
PSIM = NOT_EXECUTED
Hardware = NOT_EXECUTED
Candidate #10 = HOLD / NOT_ASSIGNED
```

## 1. Decision

Sketch A retains the resonant/magnetic-feedback center-tapped self-oscillating push-pull host and adds:

```text
ND1 -> Lcomm_ext -> NKA -> Cr_ext -> ND2
```

The graph now has complete named connectivity, but it does not yet have complete physical state closure.

The passive drain-to-drain series LC may be used as:

```text
single-edge commutation reachability model
full-cycle forced-circulation falsification model
```

It may not yet be used as evidence of self-starting, sustained self-oscillation, ZVS range, lower loss or a complete converter topology.

## 2. Named connectivity contract

```text
V_IN       NIN12 N0
NIN12      NCT
L_LK1      NCT NP1
P1_CORE    NP1 ND1 MAG
L_LK2      NCT NP2
P2_CORE    NP2 ND2 MAG
LM_CORE    MAG
S_CORE     NSA NSB MAG
Q1         ND1 NG1 N0
D_BODY1    N0 ND1
C_OSS1     ND1 N0
Q2         ND2 NG2 N0
D_BODY2    N0 ND2
C_OSS2     ND2 N0
L_COMM_EXT ND1 NKA
C_R_EXT    NKA ND2
F_CORE     NFA NFB MAG
B_FB       NFA NFB NG1 NG2 N0 [NIN12]
B_START    NIN12 N0 NG1 NG2
B_SECLOAD  NSA NSB NHV+ NHV-
```

`MAG` is a shared magnetic state, not an electrical node. Body-diode orientation is anode at `N0` and cathode at the corresponding drain. Winding dots, turns, equivalent leakage partition, feedback devices, startup network, secondary rectifier and component values remain `UNKNOWN`.

## 3. External-branch equations

Define:

\[
v_1=V(ND1),\qquad v_2=V(ND2),\qquad v_d=v_1-v_2
\]

\[
i_K>0:\ ND1\rightarrow L_{comm}\rightarrow C_r\rightarrow ND2
\]

\[
v_r=V(NKA)-V(ND2)
\]

Then:

\[
L_{comm}\frac{di_K}{dt}=v_d-v_r-R_Ki_K
\]

\[
C_r\frac{dv_r}{dt}=i_K
\]

The drain-node equations must use nonlinear device charge where available:

\[
\frac{dQ_{oss1}(v_1)}{dt}=i_1-i_{Q1}-i_K
\]

\[
\frac{dQ_{oss2}(v_2)}{dt}=i_2-i_{Q2}+i_K
\]

## 4. Required commutation directions

For `qK12`:

```text
v1: low -> high
v2: high -> low
iK must be negative: ND2 -> ND1
Q2 body diode or channel must legally receive the terminal current
```

For `qK21`:

```text
v2: low -> high
v1: high -> low
iK must be positive: ND1 -> ND2
Q1 body diode or channel must legally receive the terminal current
```

Energy availability is only a necessary condition:

\[
\frac12L_{comm}i_K^2+E_{lk,avail}+E_{m,avail}+E_{Cr,favorable}
\ge
\Delta E_{oss,net}+E_{par}+E_R+E_{dead}+E_{res,required}
\]

The correct charge must also move within the available dead time. Stored magnetic energy may be counted on the left side only after its actual qK current path is established.

## 5. Main falsification result

During a settled `qT1` interval:

\[
v_d\approx -V_H,\qquad i_K\rightarrow0,\qquad v_r\rightarrow -V_H
\]

During a settled `qT2` interval:

\[
v_d\approx +V_H,\qquad i_K\rightarrow0,\qquad v_r\rightarrow +V_H
\]

Therefore:

\[
v_d-v_r\rightarrow0
\]

The passive LC has no stored inductor current and no remaining voltage difference that independently initiates the next edge. It can assist after another mechanism releases the outgoing MOS, moves a drain node or establishes commutation current. It cannot by itself provide:

- first-switch selection;
- zero-energy startup;
- the gate decision law;
- alternating commutation-current polarity;
- compensation of DCR, ESR, gate and load losses;
- sustained self-oscillation across load.

At the same time, because the branch is permanently connected across `ND1-ND2`, it is driven by the full differential waveform during qT. It may therefore create full-cycle forced resonant current rather than a short commutation-only current.

## 6. Periodic conditions

A valid steady cycle requires:

\[
x(T_s)=x(0)
\]

including:

\[
i_K(T_s)=i_K(0),\qquad v_r(T_s)=v_r(0)
\]

\[
\int_0^{T_s} i_Kdt=0
\]

\[
\int_0^{T_s} v_mdt=0
\]

\[
\int_0^{T_s}(v_d-v_r-R_Ki_K)dt=0
\]

`Cr` charge balance does not prove primary flux balance. Half-cycle mismatch, qK volt-seconds, feedback delay, diode clamping and capacitor bias must be included explicitly.

## 7. First simulation contract

The first simulation, when executed, must be divided into two tests.

### Test E1 — single-edge reachability

Declare an initial `iK` with the required sign and an explicit `vCr` initial condition. Test whether Coss charge transfer completes before the incoming gate command. This is an edge test only and cannot establish self-starting or sustained oscillation.

### Test F1 — full-cycle falsification

Start from reasonable zero LC energy, bounded initial flux and an explicit startup/symmetry-breaking network. Sweep:

```text
switching frequency / LC natural frequency
Cr initial bias
component and half-cycle mismatch
no load / light load / rated mechanism load
startup / load step / fault clear
```

Mandatory outputs:

```text
vND1, vND2, iK, vCr
VGS1, VDS1, IQ1, VGS2, VDS2, IQ2
body-diode currents
primary, magnetizing and leakage currents
flux and per-cycle volt-second error
secondary/reflected-load current
per-element instantaneous power and cycle energy
```

## 8. Stop and branch rules

Stop the continuous passive Sketch A if:

- qT circulating RMS or its added loss is not below the switching loss it removes;
- operating frequency or tolerance crosses a high-Q series resonance;
- Cr bias destroys one commutation direction or component derating;
- the cycle closes only through avalanche or uncontrolled body-diode recovery;
- flux is not bounded under mismatch;
- startup depends on uncontrolled hard switching, saturation or accidental mismatch;
- light-load commutation requires excessive dedicated circulating current.

If the minimum repair is a controlled bidirectional element that connects the LC only during qK, reclassify the result as a gated commutation or active-clamp comparator. Do not continue calling it the simple passive Sketch A.

## 9. Current classification

```text
Named connectivity = COMPLETE
Physical qK closure = INCOMPLETE
Self-start = NOT_ESTABLISHED
Sustained self-oscillation = NOT_ESTABLISHED
ZVS = NOT_ESTABLISHED
Total-loss benefit = NOT_ESTABLISHED
PSIM readiness = EDGE-TEST CONTRACT ONLY
System 2omega obligation = DOWNSTREAM / OPEN
```

The next executable action is Test E1 followed by Test F1. No 2-kW optimization is authorized by this record.

