# IAR DRP Change Summary: 20261124T232849Z

## Source
- Current source file: `IA_INDVL_Feed_11_24_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_24_2026.xml.zip
- Retrieved at: 2026-11-24T23:28:49+00:00
- XML generated date: 2026-11-24
- XML files parsed from ZIP: 20
- SHA-256: `71e0e90db3bafda48acdc79dbb062bf6d3c0c00064115af89e1242721576e4a4`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 444,349
- DRP occurrence rows parsed: 60,105
- Representatives with at least one DRP flag: 60,105

## Changes Since Previous Run
- Previous run: `20261124T013954Z`
- Total reported changes: 139
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 100
- new_representative_with_drp: 13
- drp_category_added: 9
- representative_removed_from_feed: 9
- drp_count_changed: 7
- drp_category_removed: 1

### Changed Categories
- current_employer: 100
- any_drp: 22
- drp_count: 7
- has_bankrupt: 5
- has_judgment: 3
- has_customer_complaint: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261124T232849Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261124T232849Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
