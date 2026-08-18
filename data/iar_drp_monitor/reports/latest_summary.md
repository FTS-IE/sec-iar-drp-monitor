# IAR DRP Change Summary: 20260818T145208Z

## Source
- Current source file: `IA_INDVL_Feed_08_18_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_18_2026.xml.zip
- Retrieved at: 2026-08-18T14:52:08+00:00
- XML generated date: 2026-08-18
- XML files parsed from ZIP: 20
- SHA-256: `1b0aed7f2e2ee4be08b95a02cc8410bcfe289e4650507c9264e97d92bbae5f3a`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,763
- DRP occurrence rows parsed: 60,010
- Representatives with at least one DRP flag: 60,010

## Changes Since Previous Run
- Previous run: `20260817T144321Z`
- Total reported changes: 191
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 120
- representative_removed_from_feed: 23
- new_representative_with_drp: 16
- drp_count_changed: 15
- drp_category_added: 13
- drp_category_removed: 4

### Changed Categories
- current_employer: 120
- any_drp: 39
- drp_count: 15
- has_customer_complaint: 8
- has_judgment: 3
- has_bankrupt: 2
- has_termination: 2
- has_reg_action: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260818T145208Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260818T145208Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
