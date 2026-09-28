# IAR DRP Change Summary: 20260928T203309Z

## Source
- Current source file: `IA_INDVL_Feed_09_28_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_28_2026.xml.zip
- Retrieved at: 2026-09-28T20:33:09+00:00
- XML generated date: 2026-09-28
- XML files parsed from ZIP: 20
- SHA-256: `bcaf4fbfe71057de903bad2963be7fa8f7af6a810f75065fafed75e8c9db0e92`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 440,579
- DRP occurrence rows parsed: 60,035
- Representatives with at least one DRP flag: 60,035

## Changes Since Previous Run
- Previous run: `20260925T183547Z`
- Total reported changes: 223
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 145
- drp_count_changed: 20
- new_representative_with_drp: 19
- drp_category_removed: 15
- representative_removed_from_feed: 14
- drp_category_added: 10

### Changed Categories
- current_employer: 145
- any_drp: 33
- drp_count: 20
- has_bankrupt: 14
- has_customer_complaint: 6
- has_judgment: 4
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260928T203309Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260928T203309Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
