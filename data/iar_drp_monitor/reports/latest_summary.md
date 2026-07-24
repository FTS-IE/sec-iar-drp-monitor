# IAR DRP Change Summary: 20260724T154337Z

## Source
- Current source file: `IA_INDVL_Feed_07_24_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_24_2026.xml.zip
- Retrieved at: 2026-07-24T15:43:37+00:00
- XML generated date: 2026-07-24
- XML files parsed from ZIP: 20
- SHA-256: `d4c0a851545afb01eece167445d7d8fb28d15d4bf05f6b935166e50bdc7c0e49`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 436,290
- DRP occurrence rows parsed: 60,023
- Representatives with at least one DRP flag: 60,023

## Changes Since Previous Run
- Previous run: `20260723T160220Z`
- Total reported changes: 117
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 70
- representative_removed_from_feed: 16
- drp_count_changed: 11
- drp_category_added: 11
- new_representative_with_drp: 6
- drp_category_removed: 3

### Changed Categories
- current_employer: 70
- any_drp: 22
- drp_count: 11
- has_customer_complaint: 5
- has_bankrupt: 3
- has_reg_action: 2
- has_judgment: 2
- has_criminal: 1
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260724T154337Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260724T154337Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
