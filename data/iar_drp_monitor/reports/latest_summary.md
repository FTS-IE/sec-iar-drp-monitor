# IAR DRP Change Summary: 20260921T192704Z

## Source
- Current source file: `IA_INDVL_Feed_09_21_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_21_2026.xml.zip
- Retrieved at: 2026-09-21T19:27:04+00:00
- XML generated date: 2026-09-21
- XML files parsed from ZIP: 20
- SHA-256: `80877f30a425e00f6ef04b2258ecefd6d3cb98588d232b79928cc7202d8690df`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,956
- DRP occurrence rows parsed: 60,023
- Representatives with at least one DRP flag: 60,023

## Changes Since Previous Run
- Previous run: `20260918T174051Z`
- Total reported changes: 192
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 123
- new_representative_with_drp: 22
- representative_removed_from_feed: 16
- drp_count_changed: 12
- drp_category_added: 10
- drp_category_removed: 9

### Changed Categories
- current_employer: 123
- any_drp: 38
- drp_count: 12
- has_judgment: 7
- has_bankrupt: 7
- has_customer_complaint: 4
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260921T192704Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260921T192704Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
