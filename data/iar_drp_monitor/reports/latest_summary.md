# IAR DRP Change Summary: 20260623T164054Z

## Source
- Current source file: `IA_INDVL_Feed_06_23_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_23_2026.xml.zip
- Retrieved at: 2026-06-23T16:40:54+00:00
- XML generated date: 2026-06-23
- XML files parsed from ZIP: 20
- SHA-256: `9a5bdb54f77cfc32367e7f1179afa8c543f99d8c9a250bb2034248718ce6ca6c`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,065
- DRP occurrence rows parsed: 60,073
- Representatives with at least one DRP flag: 60,073

## Changes Since Previous Run
- Previous run: `20260622T181745Z`
- Total reported changes: 166
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 112
- new_representative_with_drp: 16
- representative_removed_from_feed: 13
- drp_count_changed: 10
- drp_category_removed: 10
- drp_category_added: 5

### Changed Categories
- current_employer: 112
- any_drp: 29
- drp_count: 10
- has_bankrupt: 6
- has_judgment: 4
- has_customer_complaint: 3
- has_reg_action: 1
- has_investigation: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260623T164054Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260623T164054Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
