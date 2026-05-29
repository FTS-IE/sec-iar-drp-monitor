# IAR DRP Change Summary: 20260529T174431Z

## Source
- Current source file: `IA_INDVL_Feed_05_29_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_29_2026.xml.zip
- Retrieved at: 2026-05-29T17:44:31+00:00
- XML generated date: 2026-05-29
- XML files parsed from ZIP: 20
- SHA-256: `23640739f711023d8d177694a97d25f25032a59fa3be14e6bc564e88f8340c1e`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,836
- DRP occurrence rows parsed: 60,126
- Representatives with at least one DRP flag: 60,126

## Changes Since Previous Run
- Previous run: `20260528T174407Z`
- Total reported changes: 138
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 85
- new_representative_with_drp: 16
- representative_removed_from_feed: 13
- drp_count_changed: 10
- drp_category_added: 9
- drp_category_removed: 5

### Changed Categories
- current_employer: 85
- any_drp: 29
- drp_count: 10
- has_judgment: 6
- has_customer_complaint: 4
- has_bankrupt: 2
- has_termination: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260529T174431Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260529T174431Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
