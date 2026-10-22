# IAR DRP Change Summary: 20261022T183142Z

## Source
- Current source file: `IA_INDVL_Feed_10_22_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_22_2026.xml.zip
- Retrieved at: 2026-10-22T18:31:42+00:00
- XML generated date: 2026-10-22
- XML files parsed from ZIP: 19
- SHA-256: `e07b0150871383d944cef3ed3ccf38718aa781270aaa90110a8f0bbbfcb57016`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 420,205
- DRP occurrence rows parsed: 58,739
- Representatives with at least one DRP flag: 58,739

## Changes Since Previous Run
- Previous run: `20261021T183752Z`
- Total reported changes: 1,411
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- representative_removed_from_feed: 1,311
- current_employer_changed: 67
- new_representative_with_drp: 16
- drp_count_changed: 6
- drp_category_removed: 6
- drp_category_added: 5

### Changed Categories
- any_drp: 1,327
- current_employer: 67
- has_judgment: 11
- drp_count: 6

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261022T183142Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261022T183142Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
