# IAR DRP Change Summary: 20260720T160114Z

## Source
- Current source file: `IA_INDVL_Feed_07_20_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_20_2026.xml.zip
- Retrieved at: 2026-07-20T16:01:14+00:00
- XML generated date: 2026-07-20
- XML files parsed from ZIP: 20
- SHA-256: `600fafe309eba1c34cb9c83aac46d99b22950fa85df0ad8a20f2ff97b22a7231`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 436,091
- DRP occurrence rows parsed: 60,036
- Representatives with at least one DRP flag: 60,036

## Changes Since Previous Run
- Previous run: `20260717T153803Z`
- Total reported changes: 232
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 178
- representative_removed_from_feed: 15
- drp_count_changed: 12
- new_representative_with_drp: 12
- drp_category_removed: 11
- drp_category_added: 4

### Changed Categories
- current_employer: 178
- any_drp: 27
- drp_count: 12
- has_bankrupt: 8
- has_customer_complaint: 4
- has_reg_action: 2
- has_judgment: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260720T160114Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260720T160114Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
