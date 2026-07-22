# IAR DRP Change Summary: 20260722T155119Z

## Source
- Current source file: `IA_INDVL_Feed_07_22_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_22_2026.xml.zip
- Retrieved at: 2026-07-22T15:51:19+00:00
- XML generated date: 2026-07-22
- XML files parsed from ZIP: 20
- SHA-256: `1b5b7b42b41f81e1f8d6132f217c6066c5a11d69027ce6f4ad0cd4cc258df428`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 436,184
- DRP occurrence rows parsed: 60,032
- Representatives with at least one DRP flag: 60,032

## Changes Since Previous Run
- Previous run: `20260721T155244Z`
- Total reported changes: 268
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 208
- representative_removed_from_feed: 16
- drp_count_changed: 14
- new_representative_with_drp: 12
- drp_category_removed: 10
- drp_category_added: 8

### Changed Categories
- current_employer: 208
- any_drp: 28
- drp_count: 14
- has_bankrupt: 6
- has_customer_complaint: 5
- has_judgment: 4
- has_reg_action: 1
- has_investigation: 1
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260722T155119Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260722T155119Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
