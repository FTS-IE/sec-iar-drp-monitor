# IAR DRP Change Summary: 20261007T195857Z

## Source
- Current source file: `IA_INDVL_Feed_10_07_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_07_2026.xml.zip
- Retrieved at: 2026-10-07T19:58:57+00:00
- XML generated date: 2026-10-07
- XML files parsed from ZIP: 20
- SHA-256: `864ab4c1a0a96c5c6693369827a1142aaf03000dedb54bc42357c77ac23d87db`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 441,268
- DRP occurrence rows parsed: 60,035
- Representatives with at least one DRP flag: 60,035

## Changes Since Previous Run
- Previous run: `20261006T193201Z`
- Total reported changes: 209
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 139
- new_representative_with_drp: 24
- representative_removed_from_feed: 19
- drp_count_changed: 12
- drp_category_added: 11
- drp_category_removed: 4

### Changed Categories
- current_employer: 139
- any_drp: 43
- drp_count: 12
- has_bankrupt: 5
- has_customer_complaint: 4
- has_criminal: 3
- has_judgment: 2
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261007T195857Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261007T195857Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
