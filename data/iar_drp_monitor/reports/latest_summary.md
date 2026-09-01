# IAR DRP Change Summary: 20260901T174858Z

## Source
- Current source file: `IA_INDVL_Feed_09_01_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_01_2026.xml.zip
- Retrieved at: 2026-09-01T17:48:58+00:00
- XML generated date: 2026-09-01
- XML files parsed from ZIP: 20
- SHA-256: `b2d7c20571a61759eb7e35ad1d8d9a73ff8729f918bedb1317bb933094a4846e`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 438,937
- DRP occurrence rows parsed: 60,019
- Representatives with at least one DRP flag: 60,019

## Changes Since Previous Run
- Previous run: `20260831T200441Z`
- Total reported changes: 225
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 133
- drp_count_changed: 25
- representative_removed_from_feed: 18
- drp_category_removed: 18
- new_representative_with_drp: 16
- drp_category_added: 15

### Changed Categories
- current_employer: 133
- any_drp: 34
- drp_count: 25
- has_bankrupt: 16
- has_judgment: 8
- has_customer_complaint: 7
- has_criminal: 1
- has_investigation: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260901T174858Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260901T174858Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
