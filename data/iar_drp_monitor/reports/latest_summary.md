# IAR DRP Change Summary: 20260526T173508Z

## Source
- Current source file: `IA_INDVL_Feed_05_26_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_26_2026.xml.zip
- Retrieved at: 2026-05-26T17:35:08+00:00
- XML generated date: 2026-05-26
- XML files parsed from ZIP: 20
- SHA-256: `1027da901d01e9ef97134f6a96522b9871bb5d4c4c6fe1afbf22e9a597121abe`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,586
- DRP occurrence rows parsed: 60,108
- Representatives with at least one DRP flag: 60,108

## Changes Since Previous Run
- Previous run: `20260525T163148Z`
- Total reported changes: 40
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 17
- drp_count_changed: 9
- drp_category_added: 5
- drp_category_removed: 4
- new_representative_with_drp: 3
- representative_removed_from_feed: 2

### Changed Categories
- current_employer: 17
- drp_count: 9
- has_customer_complaint: 6
- any_drp: 5
- has_bankrupt: 3

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260526T173508Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260526T173508Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
