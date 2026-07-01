# IAR DRP Change Summary: 20260701T163909Z

## Source
- Current source file: `IA_INDVL_Feed_07_01_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_01_2026.xml.zip
- Retrieved at: 2026-07-01T16:39:09+00:00
- XML generated date: 2026-07-01
- XML files parsed from ZIP: 20
- SHA-256: `7ae86b7609764895d26d4ab7e0c10809fa518566f063a98954d9ba88ca7d59ee`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,478
- DRP occurrence rows parsed: 60,077
- Representatives with at least one DRP flag: 60,077

## Changes Since Previous Run
- Previous run: `20260630T163108Z`
- Total reported changes: 189
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 129
- drp_count_changed: 16
- drp_category_removed: 14
- representative_removed_from_feed: 12
- new_representative_with_drp: 12
- drp_category_added: 6

### Changed Categories
- current_employer: 129
- any_drp: 24
- drp_count: 16
- has_customer_complaint: 8
- has_bankrupt: 8
- has_judgment: 2
- has_termination: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260701T163909Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260701T163909Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
