# IAR DRP Change Summary: 20260925T183547Z

## Source
- Current source file: `IA_INDVL_Feed_09_25_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_25_2026.xml.zip
- Retrieved at: 2026-09-25T18:35:47+00:00
- XML generated date: 2026-09-25
- XML files parsed from ZIP: 20
- SHA-256: `a5da91700c3920835aea5cfa36de33378b69b9e3def641bb3bb17b93546858fe`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 440,448
- DRP occurrence rows parsed: 60,036
- Representatives with at least one DRP flag: 60,036

## Changes Since Previous Run
- Previous run: `20260924T183210Z`
- Total reported changes: 167
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 108
- representative_removed_from_feed: 18
- drp_count_changed: 13
- new_representative_with_drp: 12
- drp_category_added: 9
- drp_category_removed: 7

### Changed Categories
- current_employer: 108
- any_drp: 30
- drp_count: 13
- has_judgment: 8
- has_customer_complaint: 4
- has_civil_judgment: 2
- has_bankrupt: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260925T183547Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260925T183547Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
