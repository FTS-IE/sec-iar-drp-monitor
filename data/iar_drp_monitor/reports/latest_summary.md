# IAR DRP Change Summary: 20260723T160220Z

## Source
- Current source file: `IA_INDVL_Feed_07_23_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_23_2026.xml.zip
- Retrieved at: 2026-07-23T16:02:20+00:00
- XML generated date: 2026-07-23
- XML files parsed from ZIP: 20
- SHA-256: `93cb02727c0ca86f73bfaa37b4e8a2af0cc50f239662ef2f49a33ecdf21092b5`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 436,245
- DRP occurrence rows parsed: 60,028
- Representatives with at least one DRP flag: 60,028

## Changes Since Previous Run
- Previous run: `20260722T155119Z`
- Total reported changes: 98
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 60
- representative_removed_from_feed: 16
- new_representative_with_drp: 10
- drp_category_added: 7
- drp_count_changed: 4
- drp_category_removed: 1

### Changed Categories
- current_employer: 60
- any_drp: 26
- drp_count: 4
- has_customer_complaint: 4
- has_bankrupt: 2
- has_judgment: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260723T160220Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260723T160220Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
