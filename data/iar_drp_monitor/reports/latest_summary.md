# IAR DRP Change Summary: 20260831T200441Z

## Source
- Current source file: `IA_INDVL_Feed_08_31_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_31_2026.xml.zip
- Retrieved at: 2026-08-31T20:04:41+00:00
- XML generated date: 2026-08-31
- XML files parsed from ZIP: 20
- SHA-256: `aee3a907994eaa87a9b21fe3c9e7eaef3c95cc22b83c8e7b441aa3ec319d8d1b`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 438,826
- DRP occurrence rows parsed: 60,022
- Representatives with at least one DRP flag: 60,022

## Changes Since Previous Run
- Previous run: `20260828T233312Z`
- Total reported changes: 167
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 98
- drp_count_changed: 20
- drp_category_removed: 19
- new_representative_with_drp: 15
- drp_category_added: 9
- representative_removed_from_feed: 6

### Changed Categories
- current_employer: 98
- any_drp: 21
- drp_count: 20
- has_bankrupt: 18
- has_customer_complaint: 5
- has_judgment: 4
- has_investigation: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260831T200441Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260831T200441Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
