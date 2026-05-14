# IAR DRP Change Summary: 20260514T162012Z

## Source
- Current source file: `IA_INDVL_Feed_05_14_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_14_2026.xml.zip
- Retrieved at: 2026-05-14T16:20:12+00:00
- XML generated date: 2026-05-14
- XML files parsed from ZIP: 20
- SHA-256: `ccdfcb094890c5cc878ff73904fca7989380ea7b5fe32009076d7e0dc73e0141`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,187
- DRP occurrence rows parsed: 60,097
- Representatives with at least one DRP flag: 60,097

## Changes Since Previous Run
- Previous run: `20260513T163255Z`
- Total reported changes: 143
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 73
- drp_category_added: 20
- new_representative_with_drp: 16
- representative_removed_from_feed: 15
- drp_count_changed: 15
- drp_category_removed: 4

### Changed Categories
- current_employer: 73
- any_drp: 31
- drp_count: 15
- has_customer_complaint: 8
- has_judgment: 7
- has_bankrupt: 4
- has_reg_action: 3
- has_civil_judgment: 1
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260514T162012Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260514T162012Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
