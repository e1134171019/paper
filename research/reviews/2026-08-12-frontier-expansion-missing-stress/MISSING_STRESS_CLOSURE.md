# Missing-Stress Closure

Date: 2026-08-12

## DOI 10.1155/etep/9317966
Status: `UNRESOLVED_RETAIN_L4`

Locked fields remain:
- 48 V → 400 V
- 200 W
- 100 kHz
- D = 0.52
- measured controlled-switch maximum ≈ 100 V
- main switch ZCS turn-on + ZVS turn-off
- diodes ZCS turn-off
- measured efficiency = 95.6% at 200 W

The publisher text associated with diode experimental waveforms does not supply a reproducible scalar for the maximum measured diode voltage. The waveform existence, analytical stress, and semiconductor voltage ratings are not substitutes for a measured peak. Therefore `max_diode_stress_v` remains `unresolved`.

## PC-CAND-0024 / DOI 10.1049/iet-pel.2015.0923
Status: `UNRESOLVED_RETAIN_BOUNDED_L5`

The experimental section locks:
- 25 V → 400 V
- 200 W
- 88 kHz
- measured switch stress < 100 V
- main switch ZCS turn-on
- diode natural/ZCS turn-off and low reverse-recovery behavior
- measured full-load efficiency = 96.4%

The experimental prose states that measured diode stresses agree with the derived equations, but does not state an exact measured maximum diode-voltage scalar. No theoretical value is promoted into the measured-stress field. `max_diode_stress_v` therefore remains `unresolved`.

## FEXP-CAND-0002 / DOI 10.1038/s41598-026-64796-y
Status: `UNRESOLVED_AND_OPERATING_POINT_CONFLICT`

The accepted-manuscript evidence includes a measured switch maximum around 54 V and diode waveform evidence, but the text does not provide a locked measured maximum diode scalar. The visual PDF screenshot route was attempted but was unavailable because the PDF screenshot cache failed; no value was estimated from a figure image.

In addition, the manuscript contains an output-power conflict: abstract/Table IV/full-load-efficiency context report 200 W while an experimental narrative reports a 250 W prototype. This record remains outside the formal frontier until the conflict is resolved by a stable publisher version or otherwise permanently typed for context only.

## Closure result
The requested missing-stress pass did not lawfully close either existing missing diode-stress scalar. This is preserved as a negative verification result rather than filled by inference.
