# Research Handoff

Use this file when starting a new AI session.

## Current task

Research a fixed power topology for `12 V low-voltage DC -> single-phase 110 Vac`, around `1-2 kW`, with total-loss minimization as the objective.

The key physical burden at 2 kW is approximately `166.7 A` at the 12 V source.

## Do not restart these ideas as novelty

Already known / prior art:

- IPOS and low-side current splitting / high-side voltage stacking.
- Primary-parallel / secondary-series magnetic structures.
- High-gain Boost / coupled-inductor / switched-capacitor / voltage-multiplier families.
- Single-stage boost inverters.
- Z-source / quasi-Z-source.
- HFL direct AC / matrix converters.
- CPT / capacitor-transformer concepts.
- Optimal intermediate voltage.
- Active power decoupling and 100/120 Hz energy buffering.
- Series-stacked and partial-power buffers.
- MEB voltage-modulating energy buffers.
- DAB with active energy buffers.
- Center-tapped transformer + LC power decoupling.
- Bidirectional battery / HV-bus / AC architectures.

## Current strongest candidate question

Not "can we add a buffer?" That is already known.

Instead ask:

> In a 12 V-class, kW-scale, 100-200 A DC-to-single-phase-AC converter, how should the first major impedance-transformation point and the local bidirectional energy-buffer point be positioned or integrated so that low-side RMS / conduction loss and total system loss are minimized?

## Required next search

Search specifically for papers combining:

`12V OR 24V`
+
`1kW OR 2kW`
+
`single-phase DC-AC inverter`
+
`current-fed / push-pull / full-bridge / DAB / matrix transformer`
+
`active power decoupling / ripple steering / energy buffer`
+
`primary-side RMS current / conduction loss / battery current ripple`
+
`integrated transformer / buffer placement`

## Evidence discipline

- Separate literature facts from engineering inference.
- Never say "nobody has done this" without closure evidence.
- Record closest prior art before drawing a new topology.
- If a new paper overlaps the candidate gap, update `PRIOR_ART_BOUNDARY.md` and `DECISION_LOG.md` first.
