# IAR DRP Change Summary: 20260630T163108Z

## Source
- Current source file: `IA_INDVL_Feed_06_30_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_30_2026.xml.zip
- Retrieved at: 2026-06-30T16:31:08+00:00
- XML generated date: 2026-06-30
- XML files parsed from ZIP: 20
- SHA-256: `b7b928f1a12b55986889bb11cd23b855ef6dbdf16a592d49afb4cb17ca613035`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,366
- DRP occurrence rows parsed: 60,083
- Representatives with at least one DRP flag: 60,083

## Changes Since Previous Run
- Previous run: `20260629T171208Z`
- Total reported changes: 358
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 285
- new_representative_with_drp: 21
- drp_count_changed: 18
- drp_category_removed: 13
- drp_category_added: 11
- representative_removed_from_feed: 10

### Changed Categories
- current_employer: 285
- any_drp: 31
- drp_count: 18
- has_bankrupt: 12
- has_judgment: 8
- has_customer_complaint: 4

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260630T163108Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260630T163108Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
