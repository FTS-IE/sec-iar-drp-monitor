# IAR DRP Change Summary: 20260730T160002Z

## Source
- Current source file: `IA_INDVL_Feed_07_30_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_30_2026.xml.zip
- Retrieved at: 2026-07-30T16:00:02+00:00
- XML generated date: 2026-07-30
- XML files parsed from ZIP: 20
- SHA-256: `f6574911f006987a98367c2de4d2bf65cd3f81db8daf3b1d50c74bf711e0df98`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 436,716
- DRP occurrence rows parsed: 60,024
- Representatives with at least one DRP flag: 60,024

## Changes Since Previous Run
- Previous run: `20260729T155802Z`
- Total reported changes: 110
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 67
- representative_removed_from_feed: 12
- new_representative_with_drp: 10
- drp_count_changed: 9
- drp_category_added: 7
- drp_category_removed: 5

### Changed Categories
- current_employer: 67
- any_drp: 22
- drp_count: 9
- has_judgment: 4
- has_bankrupt: 3
- has_customer_complaint: 3
- has_criminal: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260730T160002Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260730T160002Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
