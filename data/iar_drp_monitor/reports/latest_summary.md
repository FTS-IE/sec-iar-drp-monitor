# IAR DRP Change Summary: 20260622T181745Z

## Source
- Current source file: `IA_INDVL_Feed_06_22_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_22_2026.xml.zip
- Retrieved at: 2026-06-22T18:17:45+00:00
- XML generated date: 2026-06-22
- XML files parsed from ZIP: 20
- SHA-256: `38a875483bf4f57ebd64d6da5e2689d6b7b0262b0d39bdbd3a5e3538952c4090`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,974
- DRP occurrence rows parsed: 60,074
- Representatives with at least one DRP flag: 60,074

## Changes Since Previous Run
- Previous run: `20260619T164045Z`
- Total reported changes: 41
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 15
- drp_category_removed: 11
- drp_count_changed: 7
- representative_removed_from_feed: 4
- new_representative_with_drp: 4

### Changed Categories
- current_employer: 15
- has_bankrupt: 11
- any_drp: 8
- drp_count: 7

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260622T181745Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260622T181745Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
