# IAR DRP Change Summary: 20260911T174504Z

## Source
- Current source file: `IA_INDVL_Feed_09_11_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_11_2026.xml.zip
- Retrieved at: 2026-09-11T17:45:04+00:00
- XML generated date: 2026-09-11
- XML files parsed from ZIP: 20
- SHA-256: `67282c4278bb99c3649d322db49fe2488a5de82888574b705ef73aeff8b71a35`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,395
- DRP occurrence rows parsed: 59,994
- Representatives with at least one DRP flag: 59,994

## Changes Since Previous Run
- Previous run: `20260910T174259Z`
- Total reported changes: 204
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 156
- representative_removed_from_feed: 19
- new_representative_with_drp: 12
- drp_count_changed: 8
- drp_category_added: 6
- drp_category_removed: 3

### Changed Categories
- current_employer: 156
- any_drp: 31
- drp_count: 8
- has_judgment: 7
- has_reg_action: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260911T174504Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260911T174504Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
