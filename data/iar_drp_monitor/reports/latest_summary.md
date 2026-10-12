# IAR DRP Change Summary: 20261012T220816Z

## Source
- Current source file: `IA_INDVL_Feed_10_12_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_12_2026.xml.zip
- Retrieved at: 2026-10-12T22:08:16+00:00
- XML generated date: 2026-10-12
- XML files parsed from ZIP: 20
- SHA-256: `bdff53bc0d53d458db99b36b0d649f9db703d397f41af5f2b5cdbd19512e289b`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 441,527
- DRP occurrence rows parsed: 60,043
- Representatives with at least one DRP flag: 60,043

## Changes Since Previous Run
- Previous run: `20261009T193234Z`
- Total reported changes: 361
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 289
- drp_count_changed: 19
- representative_removed_from_feed: 17
- new_representative_with_drp: 15
- drp_category_added: 11
- drp_category_removed: 10

### Changed Categories
- current_employer: 289
- any_drp: 32
- drp_count: 19
- has_customer_complaint: 8
- has_bankrupt: 7
- has_judgment: 2
- has_civil_judgment: 2
- has_termination: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261012T220816Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261012T220816Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
