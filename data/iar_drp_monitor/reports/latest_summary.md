# IAR DRP Change Summary: 20261106T202647Z

## Source
- Current source file: `IA_INDVL_Feed_11_06_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_06_2026.xml.zip
- Retrieved at: 2026-11-06T20:26:47+00:00
- XML generated date: 2026-11-06
- XML files parsed from ZIP: 19
- SHA-256: `fe94f15eeb1a430adcfa67e9b7f638b7fa0f19dece7cd1dc1ee87bd083d547d5`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 421,195
- DRP occurrence rows parsed: 59,278
- Representatives with at least one DRP flag: 59,278

## Changes Since Previous Run
- Previous run: `20261105T210456Z`
- Total reported changes: 149
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 79
- representative_removed_from_feed: 19
- drp_category_added: 18
- new_representative_with_drp: 16
- drp_count_changed: 15
- drp_category_removed: 2

### Changed Categories
- current_employer: 79
- any_drp: 35
- drp_count: 15
- has_customer_complaint: 7
- has_judgment: 6
- has_bankrupt: 3
- has_criminal: 2
- has_investigation: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261106T202647Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261106T202647Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
