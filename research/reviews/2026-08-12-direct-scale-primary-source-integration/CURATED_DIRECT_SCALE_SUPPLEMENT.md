# Curated Direct-Scale Evidence Supplement

Date: 2026-08-12
Purpose: neutral source packet for later independent interpretation.

This packet intentionally omits L5 decisions, independent-family labels, ranking, dominance, Pareto conclusions, and Research Gap conclusions.

## Source A — DOI 10.1109/OJPEL.2024.3432628

Title: Two-Switch Ultrahigh Step-Up DC–DC Converterer With Low Input Current Ripple and Low Switch Voltage Stress

Primary-source facts:
- experimental prototype: Vin=20 V, Vout=400 V, Pout=240 W, fs=50 kHz, D=0.458, n=1;
- measured switch voltages: S1=39.5 V, S2=102 V;
- measured diode voltages: D1=36 V, D2=38 V, D3=174 V, D4=399 V, Do=269 V;
- input-inductor current ripple reported as slightly higher than 30%;
- common ground explicitly stated;
- nominal efficiency 94.4% at 240 W / 20 V;
- power stage contains two controlled switches, five discrete diodes, five capacitors, one input inductor and one three-winding coupled inductor;
- no explicit ZVS/ZCS claim for the proposed hardware was located in the primary text used for this packet.

Locators: component-design section; Fig. 7 prototype; Fig. 8 experimental voltage/current and dynamic results; Fig. 9 efficiency.

## Source B — DOI 10.1109/TPEL.2023.3298683

Title: A Family of High Step-Up DC–DC Converters Based on Enhanced Boost Cells With Coupled Inductor

Primary-source facts:
- 200 W laboratory prototype;
- Vin=40 V and Vout≈400 V in the experimental waveform;
- nominal fs=500 kHz; duty commonly set around 0.5 for the reported prototype design;
- planar three-winding coupled inductor; selected turns structure 1:2:2;
- input current is continuous; RMS about 5.23 A;
- experimental switch waveform demonstrates ZVS turn-on;
- experimental diode waveforms demonstrate ZCS turn-off;
- efficiency reaches 95.55% at 200 W;
- exact measured maximum switch/diode voltage-stress scalars are not text-locked in the experimental prose;
- source equations at the nominal operating point imply Vsw≈80 V and diode stresses approximately 112 V / 288 V;
- power stage count used in this packet: one controlled switch, two discrete diodes, C1/C2/Co plus the explicit resonant switch capacitor, one input-inductor core and one three-winding coupled-inductor core.

Locators: Table II / Fig. 16; experimental Figs. 18–24.

## Source C — DOI 10.1109/OJPEL.2023.3275651

Title: A New Soft-Switched High Step-Up Trans-Inverse DC/DC Converter Based on Built-In Transformer

Primary-source facts:
- Vin=25 V, Vout=400 V, Pout=200 W;
- two controlled switches and active clamp;
- measured switch stresses about 50 V;
- both switches experimentally turn on under ZVS;
- theoretical maximum diode stress at the prototype design parameters is approximately 350 V;
- exact measured maximum diode-stress scalar is not text-locked;
- measured maximum efficiency about 95.8% at Pout=120 W;
- power stage: two switches, two discrete diodes, four capacitors, input inductor plus a three-winding built-in transformer.

Locators: prototype Table 5; Figs. 15–22.

## Source D — DOI 10.1109/TPEL.2025.3552015

Title: A New Active Clamp Quasi-Resonant High Step-Up DC/DC Converter Based on Built-In Transformer With Low Voltage Stress

Primary-source facts:
- Vin=25 V, Vout=400 V, Pout=200 W, fs=50 kHz;
- experimental duty waveform shows D≈0.51;
- measured S1/S2 maximum voltage about 50 V;
- both switches experimentally achieve ZVS turn-on;
- all four diodes exhibit low reverse-recovery behavior;
- theoretical diode stress at n=3.3 is approximately 173.7 V;
- exact measured maximum diode-stress scalar is not text-locked;
- conclusion contains a separate statement that maximum component stresses are below 40% of output voltage; this statement is retained separately rather than reconciled with the theoretical diode value;
- full-load efficiency about 96.3%; peak about 96.6% at 100 W;
- power stage: two controlled switches, four diodes, six capacitors, input inductor and a two-winding BIT.

Locators: Table V; Figs. 15–25.

## Source E — DOI 10.1109/TPEL.2025.3608899

Title: New Soft-Switched Three-Winding Built-In Transformer Step-Up DC/DC Converter With Low Voltage Stresses

Primary-source facts:
- Vin=25 V, Vout=400 V, Pout=200 W, fs=50 kHz;
- one controlled switch;
- measured switch stress approximately 50 V;
- measured D1–D4 stress approximately 180 V and clamp diode Dc approximately 50 V;
- switch ZCS turn-on is experimentally demonstrated;
- diodes exhibit low reverse-recovery operation;
- full-load efficiency approximately 96.6%;
- power stage: one controlled switch, five diodes, six capacitors, input inductor and three-winding built-in transformer.

Locators: Table IV; Figs. 12–20.

## Questions for independent reviewer

Without using prior adjudication or family labels:

1. Which facts above are directly measured, which are theoretical/recalculated, and which remain unresolved?
2. Are any source facts internally contradictory or boundary-mismatched?
3. At similar 20–40 V → 400 V / ~200–250 W conditions, what recurring engineering tradeoffs are supported by the evidence?
4. Does the evidence support a strict two-objective stress dominance statement for any pair when only measured-to-measured values are compared?
5. Which additional objective measurements are necessary before an all-objective Pareto claim could be defensible?
6. Do not infer a Research Gap unless the evidence independently supports it.
