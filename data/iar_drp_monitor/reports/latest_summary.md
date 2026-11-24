# IAR DRP Change Summary: 20261124T013954Z

## Source
- Current source file: `IA_INDVL_Feed_11_23_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_23_2026.xml.zip
- Retrieved at: 2026-11-24T01:39:54+00:00
- XML generated date: 2026-11-23
- XML files parsed from ZIP: 20
- SHA-256: `1f31cb15c89b2209a85d4ebef309ae8c3765e01e69d2a933096d2a6fee43b7a3`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 444,252
- DRP occurrence rows parsed: 60,094
- Representatives with at least one DRP flag: 60,094

## Changes Since Previous Run
- Previous run: `20261120T214841Z`
- Total reported changes: 161
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 100
- representative_removed_from_feed: 21
- new_representative_with_drp: 13
- drp_count_changed: 11
- drp_category_removed: 8
- drp_category_added: 8

### Changed Categories
- current_employer: 100
- any_drp: 34
- drp_count: 11
- has_bankrupt: 10
- has_customer_complaint: 4
- has_criminal: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261124T013954Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261124T013954Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
