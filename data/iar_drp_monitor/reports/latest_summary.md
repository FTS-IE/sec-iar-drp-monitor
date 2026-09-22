# IAR DRP Change Summary: 20260922T180443Z

## Source
- Current source file: `IA_INDVL_Feed_09_22_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_22_2026.xml.zip
- Retrieved at: 2026-09-22T18:04:43+00:00
- XML generated date: 2026-09-22
- XML files parsed from ZIP: 20
- SHA-256: `0480deed6b1a1ae40ca3b59837259f75f1c0bb5d2176f90316a3e8a32dc92bcd`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 440,103
- DRP occurrence rows parsed: 60,021
- Representatives with at least one DRP flag: 60,021

## Changes Since Previous Run
- Previous run: `20260921T192704Z`
- Total reported changes: 191
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 132
- representative_removed_from_feed: 18
- drp_count_changed: 13
- new_representative_with_drp: 13
- drp_category_added: 8
- drp_category_removed: 7

### Changed Categories
- current_employer: 132
- any_drp: 31
- drp_count: 13
- has_judgment: 5
- has_customer_complaint: 3
- has_bankrupt: 3
- has_criminal: 2
- has_civil_judgment: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260922T180443Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260922T180443Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
