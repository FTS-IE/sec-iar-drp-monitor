# IAR DRP Change Summary: 20260908T175553Z

## Source
- Current source file: `IA_INDVL_Feed_09_08_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_08_2026.xml.zip
- Retrieved at: 2026-09-08T17:55:53+00:00
- XML generated date: 2026-09-08
- XML files parsed from ZIP: 20
- SHA-256: `997abde436cb288c8d9daaf4d8d07a8d5da37fee2da14090c15be9c5cf593ed0`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,159
- DRP occurrence rows parsed: 60,002
- Representatives with at least one DRP flag: 60,002

## Changes Since Previous Run
- Previous run: `20260907T184335Z`
- Total reported changes: 15
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 9
- representative_removed_from_feed: 4
- drp_count_changed: 1
- drp_category_removed: 1

### Changed Categories
- current_employer: 9
- any_drp: 4
- drp_count: 1
- has_bankrupt: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260908T175553Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260908T175553Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
