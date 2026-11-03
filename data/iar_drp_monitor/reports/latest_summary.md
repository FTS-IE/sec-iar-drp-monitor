# IAR DRP Change Summary: 20261103T204057Z

## Source
- Current source file: `IA_INDVL_Feed_11_03_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_03_2026.xml.zip
- Retrieved at: 2026-11-03T20:40:57+00:00
- XML generated date: 2026-11-03
- XML files parsed from ZIP: 19
- SHA-256: `2324ea367786b0d9539d9629207d4bbbce02700a334818daa5240c5953a4f4a1`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 420,925
- DRP occurrence rows parsed: 59,257
- Representatives with at least one DRP flag: 59,257

## Changes Since Previous Run
- Previous run: `20261102T224616Z`
- Total reported changes: 1,130
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- representative_removed_from_feed: 860
- current_employer_changed: 213
- drp_count_changed: 19
- new_representative_with_drp: 17
- drp_category_added: 15
- drp_category_removed: 6

### Changed Categories
- any_drp: 877
- current_employer: 213
- drp_count: 19
- has_customer_complaint: 11
- has_judgment: 3
- has_bankrupt: 3
- has_civil_judgment: 2
- has_criminal: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261103T204057Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261103T204057Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
