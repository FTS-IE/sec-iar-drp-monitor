# IAR DRP Change Summary: 20260716T154627Z

## Source
- Current source file: `IA_INDVL_Feed_07_16_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_16_2026.xml.zip
- Retrieved at: 2026-07-16T15:46:27+00:00
- XML generated date: 2026-07-16
- XML files parsed from ZIP: 20
- SHA-256: `3c074b44f4a1fd3ac77c547b8bb6962133334121cc87af1d70522a3a28ca70f3`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,912
- DRP occurrence rows parsed: 60,038
- Representatives with at least one DRP flag: 60,038

## Changes Since Previous Run
- Previous run: `20260715T154926Z`
- Total reported changes: 167
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 113
- representative_removed_from_feed: 19
- new_representative_with_drp: 13
- drp_category_added: 11
- drp_count_changed: 9
- drp_category_removed: 2

### Changed Categories
- current_employer: 113
- any_drp: 32
- drp_count: 9
- has_judgment: 4
- has_customer_complaint: 3
- has_termination: 3
- has_criminal: 1
- has_bankrupt: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260716T154627Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260716T154627Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
