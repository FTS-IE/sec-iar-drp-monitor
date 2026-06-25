# IAR DRP Change Summary: 20260625T163550Z

## Source
- Current source file: `IA_INDVL_Feed_06_25_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_25_2026.xml.zip
- Retrieved at: 2026-06-25T16:35:50+00:00
- XML generated date: 2026-06-25
- XML files parsed from ZIP: 20
- SHA-256: `872c88549fce9ef4a3135e94431e67d1494034ddce8db79bd70b2a957faeb3a9`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,223
- DRP occurrence rows parsed: 60,084
- Representatives with at least one DRP flag: 60,084

## Changes Since Previous Run
- Previous run: `20260624T163241Z`
- Total reported changes: 155
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 111
- new_representative_with_drp: 13
- drp_count_changed: 10
- drp_category_added: 9
- representative_removed_from_feed: 9
- drp_category_removed: 3

### Changed Categories
- current_employer: 111
- any_drp: 22
- drp_count: 10
- has_customer_complaint: 4
- has_criminal: 3
- has_bankrupt: 3
- has_judgment: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260625T163550Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260625T163550Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
