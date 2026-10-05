# IAR DRP Change Summary: 20261005T212920Z

## Source
- Current source file: `IA_INDVL_Feed_10_05_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_05_2026.xml.zip
- Retrieved at: 2026-10-05T21:29:20+00:00
- XML generated date: 2026-10-05
- XML files parsed from ZIP: 20
- SHA-256: `634d453fdd217e2ba2a8d537620437bc29fc46c78ec99832f13deab7b88eb704`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 441,027
- DRP occurrence rows parsed: 60,029
- Representatives with at least one DRP flag: 60,029

## Changes Since Previous Run
- Previous run: `20261002T191825Z`
- Total reported changes: 243
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 171
- representative_removed_from_feed: 28
- new_representative_with_drp: 15
- drp_count_changed: 13
- drp_category_removed: 9
- drp_category_added: 7

### Changed Categories
- current_employer: 171
- any_drp: 43
- drp_count: 13
- has_customer_complaint: 7
- has_bankrupt: 5
- has_judgment: 3
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261005T212920Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261005T212920Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
