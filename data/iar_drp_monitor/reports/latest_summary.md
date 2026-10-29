# IAR DRP Change Summary: 20261029T193715Z

## Source
- Current source file: `IA_INDVL_Feed_10_29_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_29_2026.xml.zip
- Retrieved at: 2026-10-29T19:37:15+00:00
- XML generated date: 2026-10-29
- XML files parsed from ZIP: 20
- SHA-256: `c8e9b6074c3cab7a2e8d476ceb9c92c309a44b95eb50dc52d2e930650d5ff9eb`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 442,884
- DRP occurrence rows parsed: 60,097
- Representatives with at least one DRP flag: 60,097

## Changes Since Previous Run
- Previous run: `20261028T193300Z`
- Total reported changes: 152
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 96
- new_representative_with_drp: 18
- drp_count_changed: 12
- representative_removed_from_feed: 11
- drp_category_removed: 8
- drp_category_added: 7

### Changed Categories
- current_employer: 96
- any_drp: 29
- drp_count: 12
- has_judgment: 9
- has_reg_action: 2
- has_customer_complaint: 2
- has_criminal: 1
- has_bankrupt: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261029T193715Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261029T193715Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
