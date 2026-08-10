# IAR DRP Change Summary: 20260810T151601Z

## Source
- Current source file: `IA_INDVL_Feed_08_10_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_10_2026.xml.zip
- Retrieved at: 2026-08-10T15:16:01+00:00
- XML generated date: 2026-08-10
- XML files parsed from ZIP: 20
- SHA-256: `7f2ef2cc5db457cdb15ed34bb1f59eaac3d42d869eb1383cd54119e82534bf09`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,257
- DRP occurrence rows parsed: 60,008
- Representatives with at least one DRP flag: 60,008

## Changes Since Previous Run
- Previous run: `20260807T150813Z`
- Total reported changes: 131
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 73
- representative_removed_from_feed: 15
- drp_count_changed: 15
- new_representative_with_drp: 12
- drp_category_removed: 9
- drp_category_added: 7

### Changed Categories
- current_employer: 73
- any_drp: 27
- drp_count: 15
- has_bankrupt: 8
- has_judgment: 4
- has_customer_complaint: 3
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260810T151601Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260810T151601Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
