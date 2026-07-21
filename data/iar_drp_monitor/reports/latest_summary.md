# IAR DRP Change Summary: 20260721T155244Z

## Source
- Current source file: `IA_INDVL_Feed_07_21_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_21_2026.xml.zip
- Retrieved at: 2026-07-21T15:52:44+00:00
- XML generated date: 2026-07-21
- XML files parsed from ZIP: 20
- SHA-256: `cada438daf291c83e1b67da4dff1ab7ceaa05dc5140313d462a4ba1b8783bf52`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 436,088
- DRP occurrence rows parsed: 60,038
- Representatives with at least one DRP flag: 60,038

## Changes Since Previous Run
- Previous run: `20260720T160114Z`
- Total reported changes: 234
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 162
- representative_removed_from_feed: 18
- new_representative_with_drp: 17
- drp_category_added: 15
- drp_count_changed: 15
- drp_category_removed: 7

### Changed Categories
- current_employer: 162
- any_drp: 35
- drp_count: 15
- has_reg_action: 10
- has_bankrupt: 4
- has_judgment: 4
- has_customer_complaint: 2
- has_criminal: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260721T155244Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260721T155244Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
