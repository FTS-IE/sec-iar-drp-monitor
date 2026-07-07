# IAR DRP Change Summary: 20260707T164133Z

## Source
- Current source file: `IA_INDVL_Feed_07_07_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_07_2026.xml.zip
- Retrieved at: 2026-07-07T16:41:33+00:00
- XML generated date: 2026-07-07
- XML files parsed from ZIP: 20
- SHA-256: `c29b4a6827b918a3bbb44bcfe9fdf6a65419428f5496d1205c255470f026656c`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,649
- DRP occurrence rows parsed: 60,050
- Representatives with at least one DRP flag: 60,050

## Changes Since Previous Run
- Previous run: `20260706T171531Z`
- Total reported changes: 186
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 122
- representative_removed_from_feed: 21
- drp_count_changed: 14
- drp_category_added: 11
- new_representative_with_drp: 10
- drp_category_removed: 8

### Changed Categories
- current_employer: 122
- any_drp: 31
- drp_count: 14
- has_customer_complaint: 11
- has_judgment: 4
- has_bankrupt: 4

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260707T164133Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260707T164133Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
