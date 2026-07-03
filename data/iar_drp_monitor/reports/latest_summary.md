# IAR DRP Change Summary: 20260703T160040Z

## Source
- Current source file: `IA_INDVL_Feed_07_03_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_03_2026.xml.zip
- Retrieved at: 2026-07-03T16:00:40+00:00
- XML generated date: 2026-07-03
- XML files parsed from ZIP: 20
- SHA-256: `1ce24085fef264468cbdc076ef3a0494f06b9e24a0ad4f88d5dc4c6aa6b31cf6`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,641
- DRP occurrence rows parsed: 60,059
- Representatives with at least one DRP flag: 60,059

## Changes Since Previous Run
- Previous run: `20260702T161617Z`
- Total reported changes: 140
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 108
- representative_removed_from_feed: 11
- new_representative_with_drp: 8
- drp_count_changed: 6
- drp_category_added: 4
- drp_category_removed: 3

### Changed Categories
- current_employer: 108
- any_drp: 19
- drp_count: 6
- has_judgment: 2
- has_criminal: 2
- has_termination: 1
- has_customer_complaint: 1
- has_bankrupt: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260703T160040Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260703T160040Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
