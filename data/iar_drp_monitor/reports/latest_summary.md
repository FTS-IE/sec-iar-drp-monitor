# IAR DRP Change Summary: 20260605T164001Z

## Source
- Current source file: `IA_INDVL_Feed_06_05_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_05_2026.xml.zip
- Retrieved at: 2026-06-05T16:40:01+00:00
- XML generated date: 2026-06-05
- XML files parsed from ZIP: 20
- SHA-256: `e3170bacfcd68ed917ed011e0a81f900e38c8f62308ab1698ce7da6d2e91c3f4`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,194
- DRP occurrence rows parsed: 60,085
- Representatives with at least one DRP flag: 60,085

## Changes Since Previous Run
- Previous run: `20260604T172216Z`
- Total reported changes: 148
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 94
- representative_removed_from_feed: 21
- drp_count_changed: 11
- new_representative_with_drp: 8
- drp_category_added: 8
- drp_category_removed: 6

### Changed Categories
- current_employer: 94
- any_drp: 29
- drp_count: 11
- has_judgment: 6
- has_customer_complaint: 5
- has_reg_action: 1
- has_termination: 1
- has_bankrupt: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260605T164001Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260605T164001Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
