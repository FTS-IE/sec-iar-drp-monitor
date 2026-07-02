# IAR DRP Change Summary: 20260702T161617Z

## Source
- Current source file: `IA_INDVL_Feed_07_02_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_02_2026.xml.zip
- Retrieved at: 2026-07-02T16:16:17+00:00
- XML generated date: 2026-07-02
- XML files parsed from ZIP: 20
- SHA-256: `0a1ed67df3405c07281d112530bd98c634089fd33e39e5393ed5da677375742a`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,546
- DRP occurrence rows parsed: 60,062
- Representatives with at least one DRP flag: 60,062

## Changes Since Previous Run
- Previous run: `20260701T163909Z`
- Total reported changes: 252
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 186
- representative_removed_from_feed: 29
- new_representative_with_drp: 13
- drp_count_changed: 11
- drp_category_added: 8
- drp_category_removed: 5

### Changed Categories
- current_employer: 186
- any_drp: 42
- drp_count: 11
- has_judgment: 5
- has_customer_complaint: 3
- has_criminal: 2
- has_reg_action: 1
- has_termination: 1
- has_bankrupt: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260702T161617Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260702T161617Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
