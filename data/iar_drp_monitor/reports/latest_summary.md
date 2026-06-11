# IAR DRP Change Summary: 20260611T174547Z

## Source
- Current source file: `IA_INDVL_Feed_06_11_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_11_2026.xml.zip
- Retrieved at: 2026-06-11T17:45:47+00:00
- XML generated date: 2026-06-11
- XML files parsed from ZIP: 20
- SHA-256: `ddd691fdda073a4a48fb2deaaadef0cf9156e6c1f11d71e3a47b4d5650d51ebe`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,535
- DRP occurrence rows parsed: 60,077
- Representatives with at least one DRP flag: 60,077

## Changes Since Previous Run
- Previous run: `20260610T173423Z`
- Total reported changes: 127
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 86
- new_representative_with_drp: 14
- representative_removed_from_feed: 13
- drp_count_changed: 6
- drp_category_added: 5
- drp_category_removed: 3

### Changed Categories
- current_employer: 86
- any_drp: 27
- drp_count: 6
- has_judgment: 4
- has_customer_complaint: 4

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260611T174547Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260611T174547Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
