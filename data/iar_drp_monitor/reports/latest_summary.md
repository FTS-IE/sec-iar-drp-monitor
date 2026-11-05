# IAR DRP Change Summary: 20261105T210456Z

## Source
- Current source file: `IA_INDVL_Feed_11_05_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_05_2026.xml.zip
- Retrieved at: 2026-11-05T21:04:56+00:00
- XML generated date: 2026-11-05
- XML files parsed from ZIP: 19
- SHA-256: `26583f56560a7fd7bfce7f41dab3716f04925730fae8fe8cdc67fa7857bbbefb`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 421,093
- DRP occurrence rows parsed: 59,268
- Representatives with at least one DRP flag: 59,268

## Changes Since Previous Run
- Previous run: `20261104T205123Z`
- Total reported changes: 138
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 86
- new_representative_with_drp: 19
- representative_removed_from_feed: 16
- drp_category_added: 9
- drp_count_changed: 7
- drp_category_removed: 1

### Changed Categories
- current_employer: 86
- any_drp: 35
- drp_count: 7
- has_bankrupt: 3
- has_judgment: 2
- has_criminal: 2
- has_customer_complaint: 2
- has_civil_judgment: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261105T210456Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261105T210456Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
