# IAR DRP Change Summary: 20260824T152220Z

## Source
- Current source file: `IA_INDVL_Feed_08_24_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_24_2026.xml.zip
- Retrieved at: 2026-08-24T15:22:20+00:00
- XML generated date: 2026-08-24
- XML files parsed from ZIP: 20
- SHA-256: `da4b08183fff8d4665456e62314509467b68b44cacd89a4894a07cc3391134a6`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 438,192
- DRP occurrence rows parsed: 59,996
- Representatives with at least one DRP flag: 59,996

## Changes Since Previous Run
- Previous run: `20260821T145245Z`
- Total reported changes: 180
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 108
- drp_count_changed: 18
- representative_removed_from_feed: 17
- drp_category_removed: 16
- new_representative_with_drp: 13
- drp_category_added: 8

### Changed Categories
- current_employer: 108
- any_drp: 30
- drp_count: 18
- has_bankrupt: 11
- has_customer_complaint: 5
- has_judgment: 4
- has_criminal: 2
- has_civil_judgment: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260824T152220Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260824T152220Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
