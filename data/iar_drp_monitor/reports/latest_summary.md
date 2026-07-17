# IAR DRP Change Summary: 20260717T153803Z

## Source
- Current source file: `IA_INDVL_Feed_07_17_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_17_2026.xml.zip
- Retrieved at: 2026-07-17T15:38:03+00:00
- XML generated date: 2026-07-17
- XML files parsed from ZIP: 20
- SHA-256: `af2bf559458646113df576610801b1d4d28f19c910f327c1d5885eeba3cdc6f9`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,999
- DRP occurrence rows parsed: 60,043
- Representatives with at least one DRP flag: 60,043

## Changes Since Previous Run
- Previous run: `20260716T154627Z`
- Total reported changes: 174
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 104
- drp_count_changed: 23
- drp_category_added: 16
- drp_category_removed: 13
- new_representative_with_drp: 9
- representative_removed_from_feed: 9

### Changed Categories
- current_employer: 104
- drp_count: 23
- any_drp: 18
- has_customer_complaint: 14
- has_judgment: 11
- has_bankrupt: 2
- has_reg_action: 1
- has_investigation: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260717T153803Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260717T153803Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
