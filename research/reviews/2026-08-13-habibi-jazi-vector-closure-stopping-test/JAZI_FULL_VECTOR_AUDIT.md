# Jazi Full Vector Audit

Date: 2026-08-13
DOI: `10.1109/ACCESS.2025.3573936`
IEEE document: `11015738`

## Canonical identity and legal full text

Title: `High Voltage Gain DC-DC Converter With Wide Range of Soft Switching and Continues Input Current for Renewable Energy Applications`

Authors: Hamed Moradmand Jazi, Behrouz Mohammadzadeh, Ramin Rahimzadeh Khorasani, Pericle Zanchetta, Ehsan Adib, Guillermo Velasco-Quesada, Herminio Martínez-García.

Publication: IEEE Access, vol. 13, 2025, pp. 94878-94892. The legal/readable primary route used in this node is the Universitat Politècnica de Catalunya UPCommons open-access copy; the repository declares open access / Creative Commons Attribution 4.0 and identifies the IEEE DOI.

Primary locators used: Fig. 1; Eqs. (31)-(36); Table 1; Table 2; Fig. 8; Fig. 9; Table 3; Table 4; Fig. 15; Sec. IV.A-IV.D; Conclusion.

## Prototype boundary

Confirmed direct-scale laboratory prototype:
- Vin = 40 V;
- Vout = 400 V;
- Pout = 200 W;
- fs = 100 kHz;
- coupled-inductor turns ratio `n = 2`;
- calculated prototype duty approximately 0.65.

## Topology and common component-count basis

The schematic text explicitly defines:
- main switch `S1`;
- auxiliary switch `SA`;
- input inductor `Lin`;
- a coupled magnetic element with primary, secondary and auxiliary winding ratios (`n` and `nA`);
- clamp diode `DC`;
- multiplier diodes `D1`, `D2`;
- output diode `DO`;
- capacitors `CC`, `C1`, `C2`, `C3`, `CO`;
- external snubber capacitor `Cs1` across the main switch in addition to intrinsic `Coss`.

Under `SCHEMATIC_DISCRETE_POWER_STAGE_V1`:
- controlled switches = 2;
- discrete diodes = 4;
- discrete capacitors = 6 (`CC`, `C1`, `C2`, `C3`, `CO`, external `Cs1`);
- magnetic structures / cores = 2 (`Lin` + coupled magnetic element);
- total windings = 4 (one `Lin` winding + three coupled-magnetic windings).

If an author comparison table excludes the external snubber capacitor from its component total, that is a count-basis difference, not a contradiction.

## Semiconductor stress

### Measured main switch

Experimental Fig. 9(a) text-locks maximum main-switch voltage at approximately 120 V:

`S1 measured normalized stress ~= 120/400 = 0.30`.

The paper states that `S1` operates under ZVS at full load and also demonstrates soft switching at 20% nominal load.

### Auxiliary switch

Fig. 9(b) experimentally verifies:
- turn-on under ZCS;
- turn-off under ZVZCS.

However, the recovered primary text does not text-lock an exact maximum operational voltage scalar for `SA`. The 250 V device rating of FDA69N25 is **not** substituted for operational stress.

Therefore the complete measured controlled-switch vector is unresolved and the record cannot use `0.30` as its measured maximum controlled-switch stress.

### Theoretical semiconductor stresses

The recovered design equations are preserved as theory:
- Eq. (32): main-switch stress;
- Eq. (33): `D1`;
- Eq. (34): auxiliary switch `SA`;
- Eq. (35): `DO`;
- Eq. (36): `D2`.

Using Vin = 40 V, Vout = 400 V, n = 2, K ~= 1 and D ~= 0.65:
- theoretical S1 ~= 93.0 V ~= 0.2326 Vout;
- theoretical D1 ~= 114.3 V ~= 0.2857 Vout;
- theoretical DO ~= 211.4 V ~= 0.5286 Vout;
- theoretical D2 ~= 228.6 V ~= 0.5714 Vout.

An exact `nA` value needed to resolve Eq. (34) for `SA` was not reproducibly locked in the recovered text, and an exact formula/scalar for clamp diode `DC` was not recovered. Therefore neither the complete theoretical controlled-switch maximum nor complete theoretical diode maximum is promoted to a scalar record field.

The paper qualitatively states that all four diodes have low stress and Fig. 9(d)-(g) shows their experimental voltage/current waveforms, but an exact maximum **measured** diode scalar is not text-locked in the recovered prose.

## Soft switching, input behavior and efficiency

Experimentally supported:
- S1: ZVS;
- SA: ZCS turn-on and ZVZCS turn-off;
- all four diodes turn off under ZCS;
- continuous input current;
- shared/common ground between input and output;
- soft-switching operation persists at 20% nominal load;
- measured full-load efficiency = 96.5%.

Efficiency remains descriptor-only and is excluded from ranking.

## Evidence decision

`L4_NUMERICALLY_VERIFIED / DIRECT_FULL_STRUCTURE_AUDITED_SWITCH_VECTOR_INCOMPLETE`

No L5 promotion is authorized in this node. Although the electrical boundary, structure and many experimental properties are direct-scale and well supported, the maximum-controlled-switch comparison field is incomplete because the exact auxiliary-switch voltage stress is unresolved. The exact measured maximum diode stress is also unresolved.

No theory or device-rating value is substituted for either missing measured vector.