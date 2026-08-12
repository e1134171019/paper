# Curated Evidence Packets

Date: 2026-08-12
Review role: neutral source-derived packet for independent interpretation

Do not infer missing values. Do not rank efficiency. Preserve all value types.

---

## Packet A — PC-CAND-0024

- DOI: `10.1049/iet-pel.2015.0923`
- Title: Single-switch high step-up converter based on coupled inductor and switched capacitor techniques with quasi-resonant operation
- Prototype: Vin 25 V; Vout 400 V; Pout 200 W; fs 88 kHz
- Common count basis: 1 controlled switch; 4 discrete diodes; 5 capacitors; 2 magnetic cores; 3 windings
- Controlled-switch voltage stress: `<100 V`, type `upper_bound`; normalized `<0.25` relative to 400 V output
- Maximum measured diode-voltage stress: `unresolved`
- Soft switching: main switch ZCS at turn-on; relevant diode low-reverse-recovery / natural-turn-off context
- Efficiency descriptor: measured full-load 96.4%; auxiliary-loss boundary not matched for cross-paper ranking
- Input current: continuous low-ripple qualitative description
- Common ground: unresolved
- Locators: Experimental results; Fig. 10(a) for switch waveform/stress/ZCS; Fig. 12 for measured efficiency

## Packet B — PC-CAND-0027

- DOI: `10.1038/s41598-024-78739-y`
- Title: A single switch high step-up DC-DC converter derived from coupled inductor and switched capacitor
- Prototype: Vin 24 V; Vout 400 V; Pout 200 W; fs 50 kHz; D = 0.60; CCM
- Common count basis: 1 controlled switch; 8 discrete diodes; 8 capacitors; 1 magnetic core; 2 windings
- Controlled-switch voltage stress: approximately 62 V; normalized approximately 0.155
- Maximum measured diode-voltage stress: approximately 110 V; normalized approximately 0.275
- Soft switching: paper comparison classification = No
- Efficiency descriptor: measured 94.53% at full load; separate peak 95.89% at 60 W
- Common ground: No
- Input-current behavior: unresolved in the current packet
- Locators: Experimental results; Fig. 12 switch stress; Fig. 15 efficiency; Table 1 soft-switch classification; Table 2 operating conditions

## Packet C — PC-CAND-0028

- DOI: `10.1038/s41598-025-17301-w`
- Title: A novel soft-switched trans-inverse ultra-high-gain DC/DC converter with low switch voltage stress
- Prototype: Vin 25 V; Vout 400 V; Pout 250 W; fs 50 kHz; D = 0.55
- Common count basis: 1 controlled switch; 4 discrete diodes; 5 capacitors; 2 magnetic cores; 4 windings
- Controlled-switch voltage stress: approximately 55 V; normalized approximately 0.1375
- Maximum measured diode-voltage stress: approximately 240 V; normalized approximately 0.60
- Soft switching: main switch ZCS at turn-on; all circuit diodes low reverse recovery
- Efficiency descriptor: measured 96.4% at full load
- Input current: continuous low-ripple; design target around 25% ripple
- Common ground: unresolved
- Locators: Experimental section / prototype table; Fig. 13(a) switch waveform; Figs. 13(b)-14 diode waveforms; Fig. 19 measured efficiency

## Packet D — PC-CAND-0030

- DOI: `10.1049/iet-pel.2015.0870`
- Title: Soft-switched non-isolated high step-up DC-DC converter with reduced voltage stress
- Prototype: Vin 40 V; Vout 400 V; Pout 200 W; fs 100 kHz; D approximately 0.5
- Common count basis: 2 controlled switches; 4 discrete diodes; 5 capacitors; 1 magnetic core; 2 windings
- Controlled-switch voltage stress vector: main `<90 V`, clamp `<90 V`; type `upper_bound`; normalized maximum `<0.225`
- Maximum measured diode-voltage stress: approximately 200 V; normalized approximately 0.50
- Soft switching: main and active-clamp switches ZVS at turn-on
- Efficiency descriptor: measured 95.4% at full load
- Input current: reduced/low-ripple qualitative claim
- Common ground: unresolved
- Locators: Experimental results; Fig. 7(a-b) switch waveforms; diode waveform results; Fig. 8 measured efficiency; topology/design section for structural counts

## Packet E — FEXP-CAND-0001

- DOI: `10.1038/s41598-025-90093-1`
- Title: A new ultra-high voltage gain DC/DC converter based on coupled-inductor
- Prototype: Vin 25 V; Vout 400 V; Pout 200 W; fs 50 kHz; D approximately 0.51
- Common count basis: 2 controlled switches; 5 discrete diodes; 5 capacitors; 2 magnetic cores; 3 windings
- Controlled-switch voltage stress vector: S1 approximately 56 V; S2 approximately 110 V; normalized maximum approximately 0.275
- Maximum measured diode-voltage stress: approximately 235 V; normalized approximately 0.5875
- Soft switching: S2 ZCS turn-on; D2/D3/D4/Do ZCS turn-off; experimental soft-switch state of S1 unresolved
- Efficiency descriptor: measured 95.9% full load; separate peak 96.2% at 160 W
- Input current: continuous low-ripple
- Common ground: Yes
- Locators: experimental-results section / Figs. 10-11; efficiency section; circuit schematic description

## Packet F — PC-CAND-0029

- DOI: `10.1038/s41598-026-47061-0`
- Title: A new soft-switched trans-inverse quasi-Z source DC-DC converter with low switch voltage stress
- Prototype: Vin 25 V; Vout 400 V; Pout 200 W; fs 50 kHz; D = 0.30
- Common count basis: 1 controlled switch; 4 discrete diodes; 5 capacitors; 2 magnetic cores; 4 windings
- Controlled-switch voltage stress: approximately 50 V; normalized approximately 0.125
- Measured diode-voltage stresses: D1 approximately 50 V; D2 approximately 180 V; D3 approximately 300 V; Do approximately 300 V; normalized maximum approximately 0.75
- Soft switching: main switch ZCS turn-on; diodes reported with low reverse-recovery behavior
- Efficiency descriptor: measured 94.9% at full load
- Input current: low-ripple / quasi-Z-source continuous-input behavior
- Common ground: Yes
- Locators: version-of-record PDF Table 4, p.17 for 200 W / 25 V / 400 V / 50 kHz prototype; experimental section p.18 / switch and diode waveform figures for approximately 50 V and 50/180/300/300 V stresses; measured-efficiency figure for 94.9% full-load value
- Visual verification note: PDF page screenshots were attempted but source-cache retrieval failed; packet uses publisher PDF parsed text, not visual inference
