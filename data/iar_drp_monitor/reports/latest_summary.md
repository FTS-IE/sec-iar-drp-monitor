# IAR DRP Change Summary: 20261009T193234Z

## Source
- Current source file: `IA_INDVL_Feed_10_09_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_09_2026.xml.zip
- Retrieved at: 2026-10-09T19:32:34+00:00
- XML generated date: 2026-10-09
- XML files parsed from ZIP: 20
- SHA-256: `558df2b0c2b02e4faced5d847475f82ebf9440cc11cde6e083f9fe47cde0d178`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 441,460
- DRP occurrence rows parsed: 60,042
- Representatives with at least one DRP flag: 60,042

## Changes Since Previous Run
- Previous run: `20261008T195746Z`
- Total reported changes: 151
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 80
- drp_category_added: 22
- drp_count_changed: 17
- representative_removed_from_feed: 14
- new_representative_with_drp: 13
- drp_category_removed: 5

### Changed Categories
- current_employer: 80
- any_drp: 27
- drp_count: 17
- has_customer_complaint: 10
- has_bankrupt: 7
- has_judgment: 6
- has_criminal: 2
- has_termination: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261009T193234Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261009T193234Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
