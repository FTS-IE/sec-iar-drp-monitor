# IAR DRP Change Summary: 20260708T161024Z

## Source
- Current source file: `IA_INDVL_Feed_07_08_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_08_2026.xml.zip
- Retrieved at: 2026-07-08T16:10:24+00:00
- XML generated date: 2026-07-08
- XML files parsed from ZIP: 20
- SHA-256: `963685ed2bec3676b1744a0dae395b62bbbfbddd653a6897329dbebd16d70bd8`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,619
- DRP occurrence rows parsed: 60,018
- Representatives with at least one DRP flag: 60,018

## Changes Since Previous Run
- Previous run: `20260707T164133Z`
- Total reported changes: 260
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 184
- representative_removed_from_feed: 40
- drp_count_changed: 11
- drp_category_added: 9
- new_representative_with_drp: 9
- drp_category_removed: 7

### Changed Categories
- current_employer: 184
- any_drp: 49
- drp_count: 11
- has_customer_complaint: 7
- has_bankrupt: 5
- has_judgment: 3
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260708T161024Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260708T161024Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
