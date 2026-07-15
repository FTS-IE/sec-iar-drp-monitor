# IAR DRP Change Summary: 20260715T154926Z

## Source
- Current source file: `IA_INDVL_Feed_07_15_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_15_2026.xml.zip
- Retrieved at: 2026-07-15T15:49:26+00:00
- XML generated date: 2026-07-15
- XML files parsed from ZIP: 20
- SHA-256: `450a79a917a262eb4c751e986aacd0145b0ba30c0644b1542434ea3d1097029f`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,850
- DRP occurrence rows parsed: 60,037
- Representatives with at least one DRP flag: 60,037

## Changes Since Previous Run
- Previous run: `20260714T154435Z`
- Total reported changes: 302
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 251
- representative_removed_from_feed: 16
- new_representative_with_drp: 13
- drp_count_changed: 10
- drp_category_added: 8
- drp_category_removed: 4

### Changed Categories
- current_employer: 251
- any_drp: 29
- drp_count: 10
- has_judgment: 5
- has_bankrupt: 3
- has_customer_complaint: 1
- has_termination: 1
- has_reg_action: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260715T154926Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260715T154926Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
