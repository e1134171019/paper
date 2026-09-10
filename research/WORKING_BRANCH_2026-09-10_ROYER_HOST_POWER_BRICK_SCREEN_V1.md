# 2026-09-10 — Royer Host + Power-Brick Screening Working Branch v1

Status: `WORKING_BRANCH / ANALYTICAL_SCREEN / PSIM_NOT_EXECUTED / HARDWARE_NOT_EXECUTED`  
Candidate #10: `HOLD / NOT_ASSIGNED`  
Novelty: `NOT_ESTABLISHED`

> Governance note: this file does **not** replace `CURRENT_MAINLINE_OVERRIDE_2026-08-20.md`. The physical-measurement mainline remains authoritative unless explicitly superseded later. This file records the newer exploratory power-topology branch from the 2026-09-10 research discussion.

---

## 1. Research-route correction

The exploratory branch had temporarily over-separated Royer into only a timing/commutation primitive. That is useful for mechanism taxonomy, but it is incomplete as a physical circuit description.

For the present topology-synthesis work, restore:

```text
Royer Host Power Cell
=
main power MOS pair/banks
+ center-tapped primary
+ HFT power transfer
+ magnetic feedback / self-oscillation
+ natural commutation behavior
```

Therefore Royer is retained as a **physical host power cell**, while its magnetic-state self-oscillation remains separately falsifiable as a timing/commutation sub-mechanism.

The research question is no longer:

```text
Royer vs LLC vs DAB vs current-fed
```

because those items are not all on the same abstraction layer.

The new working procedure is:

```text
Royer Host
↓
add one or more power/magnetic/energy-transfer bricks
↓
compute P / V / I / RMS / gain / added loss for every brick
↓
retain only combinations with P_saved > P_added
↓
only then reopen detailed timing / commutation / PSIM
```

---

## 2. Fixed first-order screening boundary

```text
Vin = 12 Vdc
Pout = 2000 W
eta_target = 95 %
Pin,target = 2105.3 W
Iin,total = 175.44 A
HV screening anchor = 336 V
I_HV,out = 5.95 A
```

The 336-V node is only a screening anchor for X1 power accounting. It is not a hardware-verified bus value.

---

## 3. Power-brick library around the Royer Host

Current working bricks:

```text
PB-1 Early N-way split / multiple Royer power cells
PB-2 Primary-parallel / secondary-series magnetic combination
PB-3 Current-fed input / current-shaping brick
PB-4 Resonant / leakage / impedance-shaping brick
PB-5 Capacitive voltage-stacking / flying-cap / switched-cap brick
PB-6 Multi-primary / matrix / coupled magnetic structure
```

Important classification:

```text
Royer = Host power cell
Current-fed = power-path / energy-transfer brick
Resonant = commutation / impedance-shaping brick
Matrix transformer = magnetic-structure brick
Flying capacitor = capacitive gain / energy-transfer brick
```

These mechanisms can be combined; they are not mutually exclusive candidates.

---

## 4. RH0 — Single Royer Host reference

First-order reference:

```text
12 V
× ~175.44 A input
→ Royer self-oscillating push-pull power cell
→ HFT
→ ~336-V-class HF/HV node
```

If the HFT alone provides the full nominal voltage ratio, the first-order effective ratio is:

```text
336 / 12 ≈ 28
```

This is the reference host, not the preferred final topology.

---

## 5. RH1 — Three Royer power cells + series secondary contribution

This screening option is **not three transformers simply paralleled on both sides**.

The assumed first-order structure is:

```text
                    12 V source
                         |
          +--------------+--------------+
          |              |              |
      Royer Cell A   Royer Cell B   Royer Cell C
          |              |              |
        HFT-A            HFT-B          HFT-C
          |              |              |
          +------ secondary series -----+
                         |
                       336 V
```

Meaning:

```text
low-voltage inputs: parallel from the same 12-V source
high-voltage secondary contributions: series-added in this screening case
```

At equal sharing:

```text
Iin/cell ≈ 175.44 / 3 = 58.48 A
Pin/cell ≈ 2105.3 / 3 = 701.8 W
Pout/cell ≈ 2000 / 3 = 666.7 W
HV series current ≈ 5.95 A
secondary voltage contribution/cell ≈ 336 / 3 = 112 V
```

Thus the per-cell first-order effective voltage ratio becomes:

```text
112 / 12 ≈ 9.33
```

instead of about 28 for one cell doing all the voltage transformation.

This is useful as a power-distribution and magnetic-burden mechanism, but generic multi-cell/IPOS/series-secondary structure is prior art and is not a novelty claim by itself.

---

## 6. RH2 — RH1 + resonant brick

Add a resonant / leakage / impedance-shaping mechanism to the Royer host cells.

Potential benefit:

```text
soft commutation / ZVS assistance
+ impedance shaping
+ possible gain assistance
```

Primary risk is reactive RMS current.

If:

```text
I_rms,new = k * I_rms,base
```

then first-order resistive loss scales approximately as:

```text
P_I2R,new / P_I2R,base = k^2
```

Examples:

```text
k = 1.05 → +10.25 % I2R component
k = 1.10 → +21.0 %
k = 1.25 → +56.25 %
k = 1.50 → +125 %
```

Retention rule:

```text
saved switching / Coss / snubber loss
>
added resonant RMS + copper + ESR + core loss
```

Status: `KEEP_CONDITIONAL`.

---

## 7. RH3 — RH1 + current-fed brick

Add one current-fed/current-shaping input path per Royer cell:

```text
12 V
→ Lf_i / current-fed element
→ Royer Host Cell i
```

Each branch remains a full-power path:

```text
Icell ≈ 58.48 A
Pin,cell ≈ 701.8 W
```

First-order total choke copper loss for three equal cells is:

```text
P_Lf,Cu,total = 3 * Icell^2 * DCR_branch
```

At N=3:

```text
DCR = 0.10 mΩ / branch → ~1.03 W
DCR = 0.25 mΩ / branch → ~2.56 W
DCR = 0.50 mΩ / branch → ~5.13 W
DCR = 1.00 mΩ / branch → ~10.26 W
```

These numbers exclude core loss, ripple-current increase, clamp/commutation overhead and device stress.

Therefore current-fed is not a free gain brick. It survives only if the gain/current-shaping/commutation benefit exceeds its added full-current series-path penalty.

Status: `KEEP_CONDITIONAL`.

---

## 8. RH4 — RH1 + capacitive gain directly at the 12-V node

For a switched-cap / flying-cap brick transporting real power:

```text
Q_per_cycle ≈ P_processed / (f_s * V_step)
```

If a 12-V capacitive brick processed the full 2 kW at 50 kHz:

```text
Q_per_cycle ≈ 3.33 mC
I_charge-transfer,avg-equivalent ≈ 166.7 A
```

Therefore:

```text
pure capacitive voltage gain
≠ removal of the 12-V hundred-ampere condition
```

Actual capacitor RMS current can be much more pulsed than this average-equivalent value.

Status:

```text
RH4 at the immediate 12-V node = HOLD / HIGH_CURRENT_RISK
```

The capacitive brick remains usable later at a higher-voltage/lower-current node.

---

## 9. RH5 — Royer Host + current-fed + resonant + magnetic sharing

Current primary working combination:

```text
12 V
↓
early split into multiple Royer host cells
↓
current-fed / current-shaping brick per cell
↓
Royer main switching + magnetic self-oscillation retained
↓
resonant / leakage impedance shaping
↓
multi-primary and/or series-secondary magnetic power combination
↓
major step-up
```

Purpose:

```text
current distribution
+ reduced per-cell magnetic voltage ratio
+ possible gain sharing
+ soft commutation
```

Hard gate:

```text
full-current choke/core/clamp penalty
+ resonant reactive RMS penalty
+ magnetic copper/core penalty
<
removed switching / interconnect / transformation penalty
```

Status: `PRIMARY_POWER_BRICK_COMBINATION_TO_SCREEN`.

No novelty claim is authorized.

---

## 10. RH6 — Royer Host + resonant + capacitive gain after partial magnetic step-up

Alternative working combination:

```text
12 V
↓
Royer Host / resonant HFT performs the first voltage rise
↓
higher-V / lower-I intermediate node
↓
switched-cap / flying-cap voltage stacking
↓
336-V-class node
```

This is physically more plausible than forcing the capacitive gain brick to process the entire 2-kW power directly at 12 V.

Research objective:

```text
share voltage gain between magnetic and capacitive mechanisms
while moving charge-transfer processing out of the most expensive hundred-ampere domain
```

Status: `SECONDARY_POWER_BRICK_COMBINATION_TO_SCREEN`.

---

## 11. Current survivor board

```text
RH0 — single Royer Host reference
RH1 — 3-cell Royer + secondary-series magnetic contribution              KEEP
RH2 — RH1 + resonant                                                     KEEP_CONDITIONAL
RH3 — RH1 + current-fed                                                  KEEP_CONDITIONAL
RH4 — RH1 + capacitive gain directly at 12 V                             HOLD
RH5 — RH1 + current-fed + resonant + magnetic sharing                    PRIMARY SCREEN
RH6 — RH1 + resonant + post-step-up capacitive gain                      SECONDARY SCREEN
```

The number of cells is still a design variable. `N=3` is a screening point, not a locked architecture or novelty claim.

---

## 12. Next mandatory calculation gate

Do **not** return to detailed Royer gate timing yet.

Next compare RH1, RH5 and RH6 under one matched power/loss ledger.

For every electrical node / brick record:

```text
Vavg / Vrms
Iavg / Irms
P_real
P_reactive
voltage-gain contribution
main MOS conduction loss
switching / Coss / snubber loss
HFT copper / core loss
current-fed choke copper / core loss
resonant capacitor / inductor ESR/copper loss
flying-cap ESR / charge-redistribution loss
interconnect resistance loss
```

Decision rule:

```text
P_saved > P_added
```

and preferably under uncertainty:

```text
Delta P_total,low > 0
```

Only the surviving power-brick combination is allowed to proceed to exact switching-state design and PSIM.

---

## 13. Current formal status

```text
Royer Host physical role = RETAINED
Royer-only novelty = NOT_ESTABLISHED
RH1 / RH5 / RH6 = ANALYTICAL WORKING CANDIDATES
Candidate #10 = HOLD / NOT_ASSIGNED
PSIM = NOT EXECUTED
Hardware = NOT EXECUTED
Novelty = NOT_ESTABLISHED
```
