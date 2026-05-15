# IAR DRP Change Summary: 20260515T161529Z

## Source
- Current source file: `IA_INDVL_Feed_05_15_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_15_2026.xml.zip
- Retrieved at: 2026-05-15T16:15:29+00:00
- XML generated date: 2026-05-15
- XML files parsed from ZIP: 20
- SHA-256: `69e19cfe57323e18d586d2cb8f650b8b4241a6ded2a98831d6e1646cc6ebe186`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,284
- DRP occurrence rows parsed: 60,111
- Representatives with at least one DRP flag: 60,111

## Changes Since Previous Run
- Previous run: `20260514T162012Z`
- Total reported changes: 146
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 85
- new_representative_with_drp: 17
- drp_count_changed: 14
- drp_category_added: 13
- representative_removed_from_feed: 11
- drp_category_removed: 6

### Changed Categories
- current_employer: 85
- any_drp: 28
- drp_count: 14
- has_customer_complaint: 6
- has_judgment: 5
- has_criminal: 3
- has_reg_action: 2
- has_bankrupt: 2
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260515T161529Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260515T161529Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
