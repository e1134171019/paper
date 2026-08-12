# Independent Review Packet v3

Date: 2026-08-12
Role: neutral evidence packet for a future independent reviewer.

This packet intentionally omits L5 decisions, independent-family labels, ranking, formal Pareto labels and Research Gap conclusions.

## Existing direct-scale rows

The earlier neutral packet remains applicable for the established rows. The following updates/additions supersede only the matching entries.

### DOI 10.1109/TPEL.2023.3344719

- 20 V -> 400 V; 200 W; 50 kHz.
- two controlled switches; three discrete diodes; five capacitors; input inductor plus one three-winding coupled inductor.
- reported coupled-inductor ratios n21=0.5, n31=2.
- exact experimental duty scalar is unresolved in recovered prose.
- using the paper gain equation with reported prototype values gives recalculated D=0.52; this is not a measured duty.
- measured S1 stress is almost 45 V.
- exact measured Sc maximum voltage is unresolved.
- paper theory states both switches share clamp-capacitor voltage; at recalculated D=0.52, theoretical switch stress is ~41.67 V each (~0.1042 Vout).
- exact measured diode maximum is unresolved.
- paper equations at the same recalculated point imply D1~208.3 V and D2=Do~250 V; theoretical maximum ~0.625 Vout.
- both switches experimentally turn on under ZVS.
- rated-power measured efficiency is approximately 94%.
- input-current ripple is qualitatively low.

### DOI 10.1109/ACCESS.2025.3573936

- 40 V -> 400 V; 200 W; 100 kHz.
- two controlled switches S1/SA; four discrete diodes DC/D1/D2/DO.
- common count basis includes CC,C1,C2,C3,CO and the explicit external snubber contribution to Cs1; intrinsic Coss is not separately counted.
- input inductor plus a coupled-inductor magnetic structure.
- paper design uses n=n2/n1=2 and calculated duty approximately 0.65.
- measured S1 maximum voltage is approximately 120 V (~0.30 Vout).
- exact measured SA maximum voltage is unresolved.
- S1 experimentally operates under ZVS; SA turns on under ZCS and turns off under ZVZCS.
- all four diodes turn off under ZCS.
- exact measured maximum diode-voltage scalar is unresolved.
- ideal/design equations at D~0.65 imply main-switch ~93 V, D1~114.3 V, DO~211.4 V and D2~228.6 V; these are theory/design values and are not substituted for measured values.
- SA theoretical stress requires nA/n1, which was not text-locked in the accessible source.
- measured S1 ~120 V versus idealized ~93 V is retained as a theory/measurement boundary difference.
- continuous input current: yes.
- shared/common ground: yes.
- measured full-load efficiency approximately 96.5%.

## New stopping-test candidates not yet fully extracted

### DOI 10.3390/pr11041087

- published-version primary PDF is available under CC BY.
- different-author program: Rashid Ahmed Khan, Hwa-Dong Liu, Chang-Hua Lin, Shiue-Der Lu, Shih-Jen Yang, Adil Sarwar.
- experimental prototype operates from 20-40 V to 380 V at 150 W.
- reported experimental duty points include 0.54 at 20 V, 0.48 at 25 V, 0.44 at 30 V, 0.39 at 35 V and 0.35 at 40 V while targeting ~380 V output.
- reported efficiency varies approximately 90-96% across tested conditions.
- complete common-schema measured semiconductor-stress vector is not included in this packet yet.

### DOI 10.1088/2631-8695/ae8f9a

- IOP accepted manuscript record dated 23 July 2026.
- different-author program: Thai Anh Au Tran, Kim-Anh Nguyen, Xuân Khánh Hồ, Duong Thach Pham, Van Cong Tran.
- abstract states a 24 V -> 400 V / 200 W hardware prototype.
- topology abstract states two synchronously controlled switches, continuous input current, a three-winding coupled inductor, voltage-multiplier cell and passive clamp.
- measured efficiency stated in abstract: 95.7% full load; 96.7% peak at 40% load.
- complete switching frequency, component count and measured semiconductor-stress vectors are not yet extracted in this packet.

## Questions for independent reviewer

1. Classify every numerical stress as measured, upper-bound, theoretical/recalculated, conflict or unresolved.
2. Identify source-internal contradictions or theory/measurement boundary differences without reconciling them by assumption.
3. For approximately matched low-voltage to 380-400 V / ~150-250 W hardware, what burden redistributions are directly supported?
4. Identify strict measured-to-measured stress dominance only where the complete compared dimensions are measured.
5. Name the missing measurements required before an all-objective Pareto analysis is defensible.
6. Evaluate whether the evidence set is stable enough for a Research Gap; if not, identify the exact blockers.
