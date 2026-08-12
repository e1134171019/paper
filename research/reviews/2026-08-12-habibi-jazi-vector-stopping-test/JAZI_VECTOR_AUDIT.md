# Jazi 2025 Direct-Scale Vector Audit

Date: 2026-08-12
DOI: `10.1109/ACCESS.2025.3573936`
IEEE document: `11015738`

## Canonical identity

Title: *High Voltage Gain DC-DC Converter With Wide Range of Soft Switching and Continues Input Current for Renewable Energy Applications*

Authors: Hamed Moradmand Jazi; Behrouz Mohammadzadeh; Ramin Rahimzadeh Khorasani; Pericle Zanchetta; Ehsan Adib; Guillermo Velasco-Quesada; Herminio Martínez-García.

Venue: IEEE Access, vol. 13, pp. 94878-94892, 2025.

Date of publication: 26 May 2025.

Source route: IEEE Xplore open-access full text, with an additional open-access repository identity at UPCommons. The source is CC BY 4.0.

## Prototype boundary

- Vin = 40 V;
- Vout = 400 V;
- Pout = 200 W;
- fs = 100 kHz;
- coupled-inductor main turns ratio n = n2/n1 = 2;
- paper states a calculated duty of approximately 65% for the 40 V to 400 V design.

The approximately 0.65 duty is a **design/calculated** value. It is not relabeled as a directly measured oscilloscope scalar.

## Common component-count basis

`SCHEMATIC_DISCRETE_POWER_STAGE_V1`

From the proposed schematic and source description:

- controlled switches = 2: S1 main + SA auxiliary;
- discrete diodes = 4: DC, D1, D2, DO;
- capacitors = 6: CC, C1, C2, C3, CO, plus the explicit external snubber contribution to Cs1;
- magnetic cores = 2: Lin + coupled-inductor magnetic structure;
- total windings = 4: Lin plus the main/secondary/auxiliary coupled-inductor windings represented by the n and nA branches.

`Cs1` is defined by the paper as the parallel combination of MOSFET Coss and an external snubber capacitor. Only the explicit external discrete capacitor contribution is counted; intrinsic Coss is not counted as a separate discrete component.

## Experimental controlled-switch evidence

### S1 main switch

At full load, the paper text-locks:

- maximum VDS1 ~= **120 V**;
- normalized relative to 400 V output ~= **0.30**;
- S1 turns on under ZVS;
- the source also describes turn-off under a ZVS condition, while noting a slight current-voltage overlap associated with the snubber capacitor.

### SA auxiliary switch

The experiment reports:

- SA turns on under ZCS;
- SA turns off under ZVZCS;
- its voltage/current waveform is shown in Fig. 9(b).

However, the recovered full text does **not** text-lock an exact maximum VDSA scalar.

Therefore:

- measured S1 stress ~= 120 V;
- measured SA stress = unresolved exact scalar;
- measured maximum controlled-switch vector = unresolved.

The 120 V main-switch value is not used as the topology-wide maximum until the auxiliary-switch scalar is locked.

## Diode evidence

At full load, Fig. 9(d-g) shows DC, D1, D2 and DO voltage/current waveforms. The source states all four diodes have low voltage stress and turn off under ZCS.

The recovered text does not text-lock exact experimental peak-voltage scalars for all four diodes. Therefore:

`maximum measured diode stress = unresolved`.

## Theory/design stress boundary

The paper gives:

- `Vsw = Vo / [D(1+nK)+(3-D)]`;
- `VD1 = Vin/(1-D)`;
- `VSA = Vin/(1-D) + (nA/n1) * D*Vin/(1-D)`;
- `VDO = Vo - (1+D)Vin/(1-D)`;
- `VD2 = 2Vin/(1-D)`.

Using D ~= 0.65, Vin = 40 V, Vout = 400 V, n = 2 and K ~= 1 only as the paper's design-point idealization gives:

- Vsw(theory) ~= 93.0 V;
- VD1(theory) ~= 114.3 V;
- VDO(theory) ~= 211.4 V;
- VD2(theory) ~= 228.6 V.

The exact prototype `nA/n1` value was **not** recovered from the current paper's accessible table/text, so the auxiliary-switch theory scalar cannot be completed without assumption.

The measured main-switch value (~120 V) is materially above the idealized ~93 V design value. This is preserved as a `THEORY_MEASUREMENT_BOUNDARY_DIFFERENCE`; it is not reconciled by replacing one with the other.

No value from an older Jazi paper is imported to fill the missing nA/n1 field.

## Input current / grounding / soft switching

- shared/common ground between input and output: explicitly reported `YES`;
- input current: explicitly continuous;
- measured input-ripple scalar: unresolved;
- S1: ZVS experimental operation across tested power range;
- SA: ZCS turn-on and ZVZCS turn-off;
- DC/D1/D2/DO: ZCS turn-off;
- light-load experiment at 20% nominal load retains soft-switching behavior.

## Efficiency

Measured full-load efficiency ~= **96.5%** at the 200 W / 40 V to 400 V prototype.

Efficiency is retained as a descriptor only. No cross-paper efficiency ranking is authorized because auxiliary and measurement boundaries are not matched.

## Evidence-level decision

`evidence_level = L4_NUMERICALLY_VERIFIED`

`frontier_admission = CONTEXT_PENDING_COMPLETE_STRESS_VECTOR`

Reasons:

1. direct-scale hardware is verified;
2. main-switch stress is directly measured;
3. exact auxiliary-switch stress is unresolved;
4. exact maximum measured diode stress is unresolved;
5. auxiliary-switch theory also cannot be completed because nA/n1 is not text-locked in the accessible source.

No L5 promotion is authorized in this node.
