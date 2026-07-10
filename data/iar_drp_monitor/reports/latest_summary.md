# IAR DRP Change Summary: 20260710T163345Z

## Source
- Current source file: `IA_INDVL_Feed_07_10_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_10_2026.xml.zip
- Retrieved at: 2026-07-10T16:33:45+00:00
- XML generated date: 2026-07-10
- XML files parsed from ZIP: 20
- SHA-256: `d1eee224d2ffbceb83a94b9f60432062e638dea99ea4c682be9e9ca73d987a51`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,686
- DRP occurrence rows parsed: 60,033
- Representatives with at least one DRP flag: 60,033

## Changes Since Previous Run
- Previous run: `20260709T164008Z`
- Total reported changes: 189
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 120
- representative_removed_from_feed: 19
- new_representative_with_drp: 16
- drp_count_changed: 16
- drp_category_added: 15
- drp_category_removed: 3

### Changed Categories
- current_employer: 120
- any_drp: 35
- drp_count: 16
- has_customer_complaint: 7
- has_judgment: 5
- has_bankrupt: 5
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260710T163345Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260710T163345Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
