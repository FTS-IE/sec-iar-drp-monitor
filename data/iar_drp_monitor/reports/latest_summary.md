# IAR DRP Change Summary: 20260909T175115Z

## Source
- Current source file: `IA_INDVL_Feed_09_09_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_09_2026.xml.zip
- Retrieved at: 2026-09-09T17:51:15+00:00
- XML generated date: 2026-09-09
- XML files parsed from ZIP: 20
- SHA-256: `a48a190fd235a192a33c8d30794071349dd9a97f738161e7eea046818d63308b`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,263
- DRP occurrence rows parsed: 59,996
- Representatives with at least one DRP flag: 59,996

## Changes Since Previous Run
- Previous run: `20260908T175553Z`
- Total reported changes: 165
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 100
- drp_count_changed: 16
- representative_removed_from_feed: 13
- drp_category_added: 13
- drp_category_removed: 12
- new_representative_with_drp: 11

### Changed Categories
- current_employer: 100
- any_drp: 24
- drp_count: 16
- has_judgment: 10
- has_customer_complaint: 7
- has_reg_action: 3
- has_bankrupt: 3
- has_investigation: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260909T175115Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260909T175115Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
