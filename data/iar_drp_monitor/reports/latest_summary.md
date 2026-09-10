# IAR DRP Change Summary: 20260910T174259Z

## Source
- Current source file: `IA_INDVL_Feed_09_10_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_10_2026.xml.zip
- Retrieved at: 2026-09-10T17:42:59+00:00
- XML generated date: 2026-09-10
- XML files parsed from ZIP: 20
- SHA-256: `ff514f61e918f6a565710220af87a67ff47b2870f27d3abb6d13f7f5be71e584`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,320
- DRP occurrence rows parsed: 59,997
- Representatives with at least one DRP flag: 59,997

## Changes Since Previous Run
- Previous run: `20260909T175115Z`
- Total reported changes: 162
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 100
- representative_removed_from_feed: 16
- drp_count_changed: 16
- drp_category_added: 13
- new_representative_with_drp: 11
- drp_category_removed: 6

### Changed Categories
- current_employer: 100
- any_drp: 27
- drp_count: 16
- has_customer_complaint: 8
- has_judgment: 7
- has_bankrupt: 3
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260910T174259Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260910T174259Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
