# IAR DRP Change Summary: 20260511T164642Z

## Source
- Current source file: `IA_INDVL_Feed_05_11_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_11_2026.xml.zip
- Retrieved at: 2026-05-11T16:46:42+00:00
- XML generated date: 2026-05-11
- XML files parsed from ZIP: 20
- SHA-256: `4d20bbf54ed091de9525b3ed6c76220818a3afb87dd1129d1b54148d3a4235d2`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 432,957
- DRP occurrence rows parsed: 60,083
- Representatives with at least one DRP flag: 60,083

## Changes Since Previous Run
- Previous run: `20260508T155129Z`
- Total reported changes: 121
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 75
- representative_removed_from_feed: 11
- drp_count_changed: 11
- drp_category_added: 10
- drp_category_removed: 8
- new_representative_with_drp: 6

### Changed Categories
- current_employer: 75
- any_drp: 17
- drp_count: 11
- has_bankrupt: 7
- has_customer_complaint: 5
- has_reg_action: 4
- has_judgment: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260511T164642Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260511T164642Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
