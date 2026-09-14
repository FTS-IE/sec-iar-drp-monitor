# IAR DRP Change Summary: 20260914T192110Z

## Source
- Current source file: `IA_INDVL_Feed_09_14_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_14_2026.xml.zip
- Retrieved at: 2026-09-14T19:21:10+00:00
- XML generated date: 2026-09-14
- XML files parsed from ZIP: 20
- SHA-256: `cbe428568b7c3b80268bd0d58f3791773c0a623e7fb4b606d56d0d101fd622ea`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,425
- DRP occurrence rows parsed: 59,984
- Representatives with at least one DRP flag: 59,984

## Changes Since Previous Run
- Previous run: `20260911T174504Z`
- Total reported changes: 176
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 112
- representative_removed_from_feed: 19
- drp_count_changed: 15
- drp_category_added: 12
- drp_category_removed: 10
- new_representative_with_drp: 8

### Changed Categories
- current_employer: 112
- any_drp: 27
- drp_count: 15
- has_bankrupt: 11
- has_judgment: 5
- has_customer_complaint: 4
- has_criminal: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260914T192110Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260914T192110Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
