# Component Count Policy

Date: 2026-08-12

## Problem

Published comparison tables do not always count the same physical objects. A paper may report the number of power-path capacitors while omitting snubber capacitors, gate-drive parts or parasitic/resonant elements. Another paper may count every discrete capacitor in the schematic.

A raw integer such as `C=5` is therefore not automatically comparable across papers.

## Required fields

For each count, preserve:

- `component_class`
- `reported_count`
- `count_basis`
- `author_reported_or_recounted`
- `included_elements`
- `excluded_elements`
- `source_locator`
- `comparison_status`

## Allowed count bases

### author_reported_count
Use the paper's own comparison-table convention without reinterpretation.

### main_power_path_count
Count components explicitly identified as the converter's main power topology; snubber-only/measurement/gate-drive parts are excluded if the source convention excludes them.

### schematic_discrete_count
Count discrete components visible and text-identifiable in the full circuit, including auxiliary/snubber parts when they are physical devices.

### magnetic_core_count
Count physical cores, not inductance symbols. A multi-winding coupled inductor on one core remains one core but its winding burden is stored separately.

## Current examples

### 10.1155/etep/9317966
The paper's comparison table reports `S/D/C/MC/W = 1/7/5/1/4`. The circuit description also contains a snubber capacitor `Cs`. This is a counting-basis difference, not a source contradiction. The Pareto matrix therefore stores the author-reported `C=5` and prohibits comparing it against a schematic-discrete capacitor count from another paper until both are recounted under the same basis.

### 10.1049/pel2.70039
The main power path uses `Cc, C1, C2, C3, Co`; the experimental design also includes `Cs1, Cs2`. The typed matrix records `5 main-power; 7 including snubber capacitors` rather than selecting one integer without a basis.

## Comparison rule

A component-count dominance statement is allowed only when both records have the same `count_basis`, or when both have been independently recounted under an explicitly frozen common basis.

Until then, component count may be used as descriptive structural evidence but not as a Pareto dominance scalar.
