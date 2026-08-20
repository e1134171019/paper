# 40 — R2-G1 Dual-HFT Gain, ZVS Energy Scale, and P0 Model v1

Status date: 2026-08-20  
Role: `R2-G1 FIRST-PRINCIPLES DERIVATION / PRE-PSIM P0 MODEL`  
Boundary: `12 Vdc / 2 kW / 220 Vac / 1φ`  
Evidence class: `THEORETICAL / MODELLED PRECHECK / NOT PSIM-RUN / NOT MEASURED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

## 1. Scope

This file executes the immediate NEXT from File 39:

1. derive the actual first-order voltage relation for the A0-derived dual-HFT / series-secondary graph;
2. separate that relation from the Wu-2008 active-clamp reference gain equation;
3. derive a 12-V current-stress proxy;
4. derive the dual-HFT leakage-energy / ZVS condition;
5. lock a numerical P0 seed for PSIM Student.

No energized hardware work is authorized. No native PSIM file has been executed in the current tool environment.

---

## 2. Critical topology correction

Wu 2008 uses its own secondary filter/output structure and gives, for that reference topology:

```text
Vo/Vi = 2 n (D + D^2)
```

R2-G1 does **not** have that secondary graph.

R2-G1 preserves the verified A0 relationship:

```text
T1 secondary outer terminal
→ series junction
→ T2 secondary outer terminal
→ full-wave HV bridge
→ HV bulk capacitor
```

with:

```text
T1 pin 5 = T2 pin 2
D1/D5 = one bridge AC leg
D2/D6 = the other bridge AC leg
```

Therefore the Wu voltage-gain equation is not used as the R2-G1 system equation.

---

## 3. Dual-HFT ideal main-interval voltage relation

Define:

```text
n1 = Ns1 / Np1,half
n2 = Ns2 / Np2,half
```

During an A-side or C-side main power interval, each energized primary half is driven approximately by `Vin` in the ideal P0 model:

```text
|vp1| ≈ Vin
|vp2| ≈ Vin
```

Hence:

```text
|vs1| ≈ n1 Vin
|vs2| ≈ n2 Vin
```

Because the two secondaries are series-aiding in the retained system graph:

```text
|vs,series| ≈ (n1 + n2) Vin
```

After ideal bridge rectification:

```text
vrec,main ≈ (n1 + n2) Vin
```

With a sufficiently large HV bulk capacitor, the first-order cap-input bus target is therefore:

```text
Vdc,ideal ≈ (n1 + n2) Vin
```

or:

```text
n1 + n2 ≈ Vdc,target / Vin
```

For equal transformers:

```text
n1 = n2 = Vdc,target / (2 Vin)
```

This is the correct P0 static-ratio initialization for the retained A0-style series-secondary graph.

It is not yet a loaded-regulation equation. Later layers must include rectifier drop, winding drop, leakage duty loss, finite recharge time and HV-bulk ripple.

---

## 4. Numeric ratio targets at Vin = 12 V

| Vdc target | n1+n2 | n1=n2 if equal |
|---:|---:|---:|
| 325 V | 27.083 | 13.542 |
| 340 V | 28.333 | 14.167 |
| 350 V | 29.167 | 14.583 |
| 380 V | 31.667 | 15.833 |
| 400 V | 33.333 | 16.667 |

Center P0 seed:

```text
Vin = 12 V
Vdc,target = 350 V
n1 = n2 = 14.583333
```

These are ideal half-primary-to-secondary voltage ratios, not an authorized winding design.

The populated A0 transformer turns remain OPEN in File 21.

---

## 5. Active-clamp reset interval and why D is not the P0 static gain term

For the locked Wu-type PM-4 reference cell:

```text
Vclamp,ref = D/(1-D) Vin
VDS,ideal,ref = Vin/(1-D)
```

For `D < 0.5`:

```text
Vclamp,ref < Vin
```

If the reset/clamp voltage is reflected through the retained dual-HFT graph, the corresponding series-secondary reset magnitude is approximately:

```text
|vs,reset| ≈ (n1+n2) Vclamp,ref
```

which is below the main-interval secondary magnitude when `D<0.5`.

Therefore, in the ideal cap-input P0 model, the HV bulk peak is set primarily by the main interval:

```text
Vdc,peak ≈ (n1+n2) Vin
```

and not by `2 n (D+D²)`.

Duty remains critical because it changes:

```text
available power-transfer interval
RMS / peak current
clamp voltage
reset margin
commutation timing
recharge-current pulse shape
```

---

## 6. 12-V current-stress proxy versus duty

Reference average source current at 95% scaling:

```text
Iin,avg = 2000 / (12 × 0.95)
        = 175.44 A
```

For a first-order rectangular-current proxy in which the two main intervals together occupy `2D` of each switching cycle and carry most of the source power:

```text
Iactive,total ≈ Iin,avg / (2D)
```

For equal T1/T2 current sharing:

```text
Iactive,each-HFT ≈ Iin,avg / (4D)
```

and the pulsed-source RMS proxy is:

```text
Iin,rms,proxy ≈ Iin,avg / sqrt(2D)
```

Numerical center point at `D=0.42`:

```text
2D = 0.84
Iactive,total ≈ 208.86 A
Iactive,each-HFT ≈ 104.43 A
Iin,rms,proxy ≈ 191.42 A
```

This proxy excludes clamp-interval current and transformer magnetizing ripple, so it is not a final RMS result.

The important structural result is:

```text
lower D
→ higher current pulse amplitude / RMS burden
```

while higher D raises clamp voltage and reduces timing/reset margin.

---

## 7. Dual-HFT leakage-energy equation

For one A-side commutation, let the two transformer branches carry currents `i1` and `i2` with leakage inductances referred to the active half-primary `Lk1` and `Lk2`.

Available trapped inductive energy is:

```text
E_Lk,A = 0.5 Lk1 i1² + 0.5 Lk2 i2²
```

For identical transformers and equal sharing:

```text
Lk1 = Lk2 = Lk
 i1 = i2 = Icomm,total/2
```

thus:

```text
E_Lk,A = Lk × (Icomm,total/2)²
       = Lk Icomm,total² / 4
```

Equivalently, referred to the common A node:

```text
Lk,eq = Lk / 2
```

and:

```text
E_Lk,A = 0.5 Lk,eq Icomm,total²
```

The C side is symmetric.

This means two parallel HFT current paths halve the common-node leakage inductance for equal individual leakage values.

---

## 8. ZVS energy requirement for a MOS-bank transition

For P0 with a linear explicit commutation capacitance:

```text
E_C,req = 0.5 Ceq Vsw²
```

The dual-HFT ZVS energy condition is:

```text
0.5 Lk1 i1² + 0.5 Lk2 i2² + E_other
>=
0.5 Ceq Vsw²
```

For the equal dual-HFT case and ignoring `E_other`:

```text
Lk >= E_C,req / i_branch²
```

At the center seed:

```text
D = 0.42
Vsw,ref = 20.69 V
Ibranch,proxy = 104.43 A
```

linear-Ceq energy scale:

| Ceq total | Ecap | per-HFT Lk energy-equivalent floor |
|---:|---:|---:|
| 10 nF | 2.14 µJ | 0.196 nH |
| 25 nF | 5.35 µJ | 0.491 nH |
| 50 nF | 10.70 µJ | 0.981 nH |
| 100 nF | 21.40 µJ | 1.963 nH |

Interpretation:

```text
At full-load 12-V current scale,
energy sufficiency for ZVS may be easy to satisfy;
the larger risk can become excess trapped leakage energy / circulation.
```

This is a theoretical full-load inference, not yet an IEEE novelty claim and not a light-load conclusion.

For P1/P2, nonlinear MOS output-capacitance energy must replace the linear `0.5 C V²` approximation. The A0 main device CSD18542KCS has an official TI PSpice model available; that model is preferred over a single-point Coss value for later switching-cell validation.

---

## 9. Leakage-energy sensitivity — why PM-4 can matter at extreme current

Using the same `D=0.42` center current proxy and `fs=50 kHz`, if leakage energy were fully dissipated at every A and C commutation, the upper-bound scale would be:

| per-HFT Lk | fully dissipated leakage-energy power proxy |
|---:|---:|
| 1 nH | 1.09 W |
| 2 nH | 2.18 W |
| 5 nH | 5.45 W |
| 10 nH | 10.91 W |
| 20 nH | 21.81 W |
| 50 nH | 54.53 W |
| 100 nH | 109.05 W |
| 200 nH | 218.10 W |

This table is an **upper-bound sensitivity only**:

```text
P = 2 fs × [0.5 Lk i1² + 0.5 Lk i2²]
```

It must not be interpreted as actual R2-G1 loss because active clamp / resonant transfer can recover or relocate part of this energy.

The result establishes why leakage energy must be explicitly tracked at 12-V / hundred-ampere scale rather than treated as a small parasitic afterthought.

---

## 10. First P0 numerical build seed

### System

```text
Vin = 12 V
Pout target = 2 kW
Vdc target = 350 V
Rload,dc = Vdc²/P = 61.25 Ω
fs = 50 kHz
D = 0.42
n1 = n2 = 14.583333
Cdc initial numerical seed = 470 µF
```

`Cdc=470 µF` is a P0 numerical seed only, not an optimized inverter-link design.

### Transformer representation

Use two identical ideal multiwinding transformers:

```text
T1:
PA half winding = 1 pu turn
PC half winding = 1 pu turn
secondary = 14.583333 pu turns

T2: same
```

The A/C half-primary winding polarities must be opposite with respect to core flux so alternating A/C switching produces symmetric bipolar core excitation.

Secondary connection:

```text
T1 secondary terminal-2
→ series junction
→ T2 secondary terminal-1
```

Outer secondary terminals feed the two AC inputs of an ideal full bridge.

### Main switching nodes

```text
VIN+ → T1 CT
VIN+ → T2 CT

T1/T2 A halves → common node A → Main-A → B
T1/T2 C halves → common node C → Main-C → B

B → VIN-
```

### PM-4 seed sweep

Do not freeze one leakage value.

Use:

```text
Lcomm per HFT = 1 / 2 / 5 / 10 / 20 / 50 nH
Ceq per logical commutation = 25 / 50 / 100 nF
```

For equal parallel HFTs:

```text
Lcomm,common-node = Lcomm_each / 2
```

Quarter-resonant timing estimate:

```text
tq ≈ (π/2) sqrt(Lcomm,eq Ceq)
```

For `Ceq=50 nF`:

```text
Lk(each)=5 nH  → tq≈17.6 ns
10 nH          → tq≈24.8 ns
20 nH          → tq≈35.1 ns
50 nH          → tq≈55.5 ns
```

Therefore initial dead-time sweep:

```text
20 / 30 / 40 / 60 / 80 ns
```

is more defensible than choosing one arbitrary value.

---

## 11. P0 measurements that must be exported

```text
V_A-B
V_C-B
VDS_MainA
VDS_MainC
VDS_AuxA
VDS_AuxC
I_T1_primary
I_T2_primary
I_A_total
I_C_total
V_CclampA
V_CclampC
V_secondary_T1
V_secondary_T2
V_secondary_series
V_rectified
V_HVbus
I_HVbus
transformer volt-second integral per full cycle
```

P0 is PASS only if:

```text
A/C flux is symmetric
no DC flux accumulation appears in ideal symmetric case
T1/T2 current sharing is symmetric
series-secondary voltage adds rather than cancels
HV bus settles near the target implied by n1+n2
main/aux state ordering is physically valid
no shoot-through path appears
Cclamp reaches periodic steady state
```

---

## 12. P0 analytical precheck result

At the center point:

```text
Vin = 12 V
D = 0.42
fs = 50 kHz
n1+n2 = 29.1667
```

main-interval series secondary magnitude:

```text
|vs,main| ≈ 29.1667 × 12
          ≈ 350 V
```

Wu-reference clamp voltage:

```text
Vclamp,ref ≈ 8.69 V
```

so a first-order reflected reset magnitude would be:

```text
|vs,reset| ≈ 29.1667 × 8.69
           ≈ 253.4 V
```

Because the HV bulk is near 350 V, an ideal bridge/bulk combination would not normally be recharged by the lower reset pulse; the 350-V main pulses dominate the cap-input bus peak.

Status:

```text
P0_ANALYTICAL_GAIN_PRECHECK = PASS
PSIM_P0_EXECUTION = NOT_EXECUTED
```

---

## 13. Main research consequence from this step

The first R2-G1 question is now sharper:

```text
The required voltage ratio is not the first obstacle.
Two series secondaries can reach the 325–400 V class with a defined magnetic ratio.

The critical PM-4 question becomes:
Can leakage energy be made just large enough for robust commutation across load,
without creating a 12-V-domain circulation / duty-loss / copper-loss penalty that exceeds the recovered switching/snubber loss?
```

At full-load extreme-LV current, the design may be in an `energy-surplus` rather than `energy-starved` ZVS regime. This must be checked across load and with nonlinear Coss before any contribution claim.

---

## 14. Next execution gate

```text
1. Enter this exact P0 graph into PSIM Student.
2. Run center point: 12 V / 350 V / 50 kHz / D=0.42 / n1=n2=14.5833.
3. Verify waveform pass conditions.
4. Sweep D = 0.35 / 0.40 / 0.42 / 0.45 / 0.48.
5. Sweep Lcomm × Ceq × dead time.
6. Only after P0 passes, replace linear Ceq with actual device Coss/Eoss behavior and add RDS(on)/winding loss.
7. Compare hard-switched R1/A0-like model vs R2-G1 under the same turns ratio, bus target, load and thermal assumptions.
```

IEEE Gate B remains open. R2-G1 remains a comparator, not a topology novelty claim.
