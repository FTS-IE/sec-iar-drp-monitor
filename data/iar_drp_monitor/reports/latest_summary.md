# IAR DRP Change Summary: 20260924T183210Z

## Source
- Current source file: `IA_INDVL_Feed_09_24_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_24_2026.xml.zip
- Retrieved at: 2026-09-24T18:32:10+00:00
- XML generated date: 2026-09-24
- XML files parsed from ZIP: 20
- SHA-256: `d1533d41d1c77cf3e5fbcdf5930d605d7290aa7b757daaec29aa26bc1cf70278`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 440,358
- DRP occurrence rows parsed: 60,039
- Representatives with at least one DRP flag: 60,039

## Changes Since Previous Run
- Previous run: `20260923T184853Z`
- Total reported changes: 194
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 133
- drp_category_added: 17
- drp_count_changed: 16
- new_representative_with_drp: 13
- representative_removed_from_feed: 10
- drp_category_removed: 5

### Changed Categories
- current_employer: 133
- any_drp: 23
- drp_count: 16
- has_judgment: 9
- has_customer_complaint: 6
- has_criminal: 3
- has_reg_action: 2
- has_bankrupt: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260924T183210Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260924T183210Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
