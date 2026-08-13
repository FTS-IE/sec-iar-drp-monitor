# IAR DRP Change Summary: 20260813T152718Z

## Source
- Current source file: `IA_INDVL_Feed_08_13_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_13_2026.xml.zip
- Retrieved at: 2026-08-13T15:27:18+00:00
- XML generated date: 2026-08-13
- XML files parsed from ZIP: 20
- SHA-256: `b84e025c7989ba754b0181b3350cd024ab79f0692887177949a99a5a73b958f7`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,579
- DRP occurrence rows parsed: 60,024
- Representatives with at least one DRP flag: 60,024

## Changes Since Previous Run
- Previous run: `20260812T151906Z`
- Total reported changes: 127
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 74
- drp_count_changed: 14
- drp_category_added: 14
- new_representative_with_drp: 13
- representative_removed_from_feed: 8
- drp_category_removed: 4

### Changed Categories
- current_employer: 74
- any_drp: 21
- drp_count: 14
- has_judgment: 9
- has_customer_complaint: 5
- has_bankrupt: 2
- has_civil_judgment: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260813T152718Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260813T152718Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
