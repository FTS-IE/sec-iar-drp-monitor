# IAR DRP Change Summary: 20260624T163241Z

## Source
- Current source file: `IA_INDVL_Feed_06_24_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_24_2026.xml.zip
- Retrieved at: 2026-06-24T16:32:41+00:00
- XML generated date: 2026-06-24
- XML files parsed from ZIP: 20
- SHA-256: `8f50b031db2cea96e6970128e035150053f8137a1c787b84b79b119f382488d9`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,151
- DRP occurrence rows parsed: 60,074
- Representatives with at least one DRP flag: 60,074

## Changes Since Previous Run
- Previous run: `20260623T164054Z`
- Total reported changes: 150
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 95
- new_representative_with_drp: 16
- drp_count_changed: 12
- representative_removed_from_feed: 11
- drp_category_removed: 10
- drp_category_added: 6

### Changed Categories
- current_employer: 95
- any_drp: 27
- drp_count: 12
- has_judgment: 5
- has_bankrupt: 5
- has_customer_complaint: 4
- has_criminal: 1
- has_civil_judgment: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260624T163241Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260624T163241Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
