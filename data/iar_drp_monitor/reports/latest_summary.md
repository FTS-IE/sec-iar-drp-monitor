# IAR DRP Change Summary: 20260915T181129Z

## Source
- Current source file: `IA_INDVL_Feed_09_15_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_15_2026.xml.zip
- Retrieved at: 2026-09-15T18:11:29+00:00
- XML generated date: 2026-09-15
- XML files parsed from ZIP: 20
- SHA-256: `f604363ed4118090abaedec59ee816f65799faa4234b139c10870030b124deaa`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,548
- DRP occurrence rows parsed: 59,988
- Representatives with at least one DRP flag: 59,988

## Changes Since Previous Run
- Previous run: `20260914T192110Z`
- Total reported changes: 163
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 94
- drp_count_changed: 18
- representative_removed_from_feed: 16
- new_representative_with_drp: 14
- drp_category_added: 13
- drp_category_removed: 8

### Changed Categories
- current_employer: 94
- any_drp: 30
- drp_count: 18
- has_customer_complaint: 9
- has_judgment: 5
- has_bankrupt: 3
- has_criminal: 3
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260915T181129Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260915T181129Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
