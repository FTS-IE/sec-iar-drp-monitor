# IAR DRP Change Summary: 20260603T183228Z

## Source
- Current source file: `IA_INDVL_Feed_06_03_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_03_2026.xml.zip
- Retrieved at: 2026-06-03T18:32:28+00:00
- XML generated date: 2026-06-03
- XML files parsed from ZIP: 20
- SHA-256: `e96481d1734d4761e00c04df470d58fee7cff0739699f7d021e57673aab78819`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,062
- DRP occurrence rows parsed: 60,095
- Representatives with at least one DRP flag: 60,095

## Changes Since Previous Run
- Previous run: `20260602T181102Z`
- Total reported changes: 193
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 130
- representative_removed_from_feed: 19
- new_representative_with_drp: 18
- drp_count_changed: 12
- drp_category_added: 9
- drp_category_removed: 5

### Changed Categories
- current_employer: 130
- any_drp: 37
- drp_count: 12
- has_bankrupt: 4
- has_customer_complaint: 3
- has_judgment: 3
- has_reg_action: 2
- has_investigation: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260603T183228Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260603T183228Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
