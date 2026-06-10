# IAR DRP Change Summary: 20260610T173423Z

## Source
- Current source file: `IA_INDVL_Feed_06_10_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_10_2026.xml.zip
- Retrieved at: 2026-06-10T17:34:23+00:00
- XML generated date: 2026-06-10
- XML files parsed from ZIP: 20
- SHA-256: `7e768703d582b16b709a97d3fd15a62cbb6c95850e2a3f72bedc80333b57ff33`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,435
- DRP occurrence rows parsed: 60,076
- Representatives with at least one DRP flag: 60,076

## Changes Since Previous Run
- Previous run: `20260609T164656Z`
- Total reported changes: 178
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 100
- representative_removed_from_feed: 20
- drp_count_changed: 18
- new_representative_with_drp: 16
- drp_category_added: 14
- drp_category_removed: 10

### Changed Categories
- current_employer: 100
- any_drp: 36
- drp_count: 18
- has_bankrupt: 9
- has_criminal: 6
- has_customer_complaint: 6
- has_judgment: 2
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260610T173423Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260610T173423Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
