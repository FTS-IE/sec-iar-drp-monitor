# IAR DRP Change Summary: 20260709T164008Z

## Source
- Current source file: `IA_INDVL_Feed_07_09_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_09_2026.xml.zip
- Retrieved at: 2026-07-09T16:40:08+00:00
- XML generated date: 2026-07-09
- XML files parsed from ZIP: 20
- SHA-256: `b61614110e897325b030e793d116186614a7611d57299b3d67e58c55e1bc5730`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,669
- DRP occurrence rows parsed: 60,026
- Representatives with at least one DRP flag: 60,026

## Changes Since Previous Run
- Previous run: `20260708T161024Z`
- Total reported changes: 222
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 157
- representative_removed_from_feed: 18
- new_representative_with_drp: 16
- drp_category_added: 15
- drp_count_changed: 14
- drp_category_removed: 2

### Changed Categories
- current_employer: 157
- any_drp: 34
- drp_count: 14
- has_judgment: 6
- has_customer_complaint: 4
- has_reg_action: 2
- has_bankrupt: 2
- has_termination: 1
- has_investigation: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260709T164008Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260709T164008Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
