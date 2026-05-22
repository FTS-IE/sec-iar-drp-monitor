# IAR DRP Change Summary: 20260522T163718Z

## Source
- Current source file: `IA_INDVL_Feed_05_22_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_22_2026.xml.zip
- Retrieved at: 2026-05-22T16:37:18+00:00
- XML generated date: 2026-05-22
- XML files parsed from ZIP: 20
- SHA-256: `fc4c6ebc3230453568bcb777d2b4aa023ad650ad274a8a476235a630500bb9d3`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,558
- DRP occurrence rows parsed: 60,120
- Representatives with at least one DRP flag: 60,120

## Changes Since Previous Run
- Previous run: `20260521T164903Z`
- Total reported changes: 150
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 93
- representative_removed_from_feed: 15
- new_representative_with_drp: 14
- drp_category_added: 13
- drp_count_changed: 11
- drp_category_removed: 4

### Changed Categories
- current_employer: 93
- any_drp: 29
- drp_count: 11
- has_customer_complaint: 8
- has_judgment: 6
- has_bankrupt: 2
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260522T163718Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260522T163718Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
