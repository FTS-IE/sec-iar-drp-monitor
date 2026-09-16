# IAR DRP Change Summary: 20260916T181118Z

## Source
- Current source file: `IA_INDVL_Feed_09_16_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_16_2026.xml.zip
- Retrieved at: 2026-09-16T18:11:18+00:00
- XML generated date: 2026-09-16
- XML files parsed from ZIP: 20
- SHA-256: `ac3bc52a3719673a0b6329a1e592a38b582262b1a1b40fd57a9fb1f7906ff5fe`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,671
- DRP occurrence rows parsed: 60,002
- Representatives with at least one DRP flag: 60,002

## Changes Since Previous Run
- Previous run: `20260915T181129Z`
- Total reported changes: 156
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 94
- new_representative_with_drp: 19
- drp_count_changed: 13
- drp_category_added: 12
- drp_category_removed: 10
- representative_removed_from_feed: 8

### Changed Categories
- current_employer: 94
- any_drp: 27
- drp_count: 13
- has_bankrupt: 7
- has_judgment: 5
- has_customer_complaint: 4
- has_criminal: 3
- has_termination: 2
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260916T181118Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260916T181118Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
