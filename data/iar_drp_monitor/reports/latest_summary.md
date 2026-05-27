# IAR DRP Change Summary: 20260527T173415Z

## Source
- Current source file: `IA_INDVL_Feed_05_27_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_27_2026.xml.zip
- Retrieved at: 2026-05-27T17:34:15+00:00
- XML generated date: 2026-05-27
- XML files parsed from ZIP: 20
- SHA-256: `d9cff58284ed385826e0fff1bcb515789f1164e4b59ce063d741ef790bb5d258`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,662
- DRP occurrence rows parsed: 60,113
- Representatives with at least one DRP flag: 60,113

## Changes Since Previous Run
- Previous run: `20260526T173508Z`
- Total reported changes: 144
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 70
- drp_count_changed: 21
- new_representative_with_drp: 15
- drp_category_added: 14
- representative_removed_from_feed: 13
- drp_category_removed: 11

### Changed Categories
- current_employer: 70
- any_drp: 28
- drp_count: 21
- has_customer_complaint: 9
- has_judgment: 6
- has_bankrupt: 6
- has_criminal: 3
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260527T173415Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260527T173415Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
