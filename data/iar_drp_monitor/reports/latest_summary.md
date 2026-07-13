# IAR DRP Change Summary: 20260713T164316Z

## Source
- Current source file: `IA_INDVL_Feed_07_13_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_13_2026.xml.zip
- Retrieved at: 2026-07-13T16:43:16+00:00
- XML generated date: 2026-07-13
- XML files parsed from ZIP: 20
- SHA-256: `55dacb21fc9e794a73c4abf38a8e1575d0323ecadf9aadc111b4bd90b34615aa`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,732
- DRP occurrence rows parsed: 60,028
- Representatives with at least one DRP flag: 60,028

## Changes Since Previous Run
- Previous run: `20260710T163345Z`
- Total reported changes: 371
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 282
- drp_count_changed: 25
- representative_removed_from_feed: 24
- drp_category_added: 18
- drp_category_removed: 12
- new_representative_with_drp: 10

### Changed Categories
- current_employer: 282
- any_drp: 34
- drp_count: 25
- has_bankrupt: 11
- has_customer_complaint: 10
- has_judgment: 5
- has_reg_action: 3
- has_investigation: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260713T164316Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260713T164316Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
