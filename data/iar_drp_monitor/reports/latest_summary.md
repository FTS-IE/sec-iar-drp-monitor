# IAR DRP Change Summary: 20260626T162742Z

## Source
- Current source file: `IA_INDVL_Feed_06_26_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_26_2026.xml.zip
- Retrieved at: 2026-06-26T16:27:42+00:00
- XML generated date: 2026-06-26
- XML files parsed from ZIP: 20
- SHA-256: `c791343d98b8dfb2d317e3e2611bf01fe5cb198a94093d61bded234043c21687`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,268
- DRP occurrence rows parsed: 60,083
- Representatives with at least one DRP flag: 60,083

## Changes Since Previous Run
- Previous run: `20260625T163550Z`
- Total reported changes: 126
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 85
- representative_removed_from_feed: 17
- new_representative_with_drp: 14
- drp_count_changed: 4
- drp_category_added: 4
- drp_category_removed: 2

### Changed Categories
- current_employer: 85
- any_drp: 31
- drp_count: 4
- has_judgment: 2
- has_bankrupt: 1
- has_customer_complaint: 1
- has_criminal: 1
- has_investigation: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260626T162742Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260626T162742Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
