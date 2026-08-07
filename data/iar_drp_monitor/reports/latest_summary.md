# IAR DRP Change Summary: 20260807T150813Z

## Source
- Current source file: `IA_INDVL_Feed_08_07_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_07_2026.xml.zip
- Retrieved at: 2026-08-07T15:08:13+00:00
- XML generated date: 2026-08-07
- XML files parsed from ZIP: 20
- SHA-256: `968778320571c7985a900cd43e943c2b241294e3f4ed075c769910ccb1be948a`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,201
- DRP occurrence rows parsed: 60,014
- Representatives with at least one DRP flag: 60,014

## Changes Since Previous Run
- Previous run: `20260805T160849Z`
- Total reported changes: 415
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 297
- representative_removed_from_feed: 36
- drp_count_changed: 28
- new_representative_with_drp: 20
- drp_category_added: 19
- drp_category_removed: 15

### Changed Categories
- current_employer: 297
- any_drp: 56
- drp_count: 28
- has_customer_complaint: 12
- has_judgment: 9
- has_criminal: 6
- has_bankrupt: 5
- has_reg_action: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260807T150813Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260807T150813Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
