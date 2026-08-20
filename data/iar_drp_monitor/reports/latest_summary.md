# IAR DRP Change Summary: 20260820T151413Z

## Source
- Current source file: `IA_INDVL_Feed_08_20_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_20_2026.xml.zip
- Retrieved at: 2026-08-20T15:14:13+00:00
- XML generated date: 2026-08-20
- XML files parsed from ZIP: 20
- SHA-256: `ce5a53c67bdf61d8e80696e802325b9e74aa4e1f73b31025162bbed96a9b0dfd`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,914
- DRP occurrence rows parsed: 60,009
- Representatives with at least one DRP flag: 60,009

## Changes Since Previous Run
- Previous run: `20260819T145303Z`
- Total reported changes: 136
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 77
- representative_removed_from_feed: 24
- new_representative_with_drp: 13
- drp_count_changed: 9
- drp_category_added: 8
- drp_category_removed: 5

### Changed Categories
- current_employer: 77
- any_drp: 37
- drp_count: 9
- has_judgment: 6
- has_customer_complaint: 4
- has_termination: 2
- has_investigation: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260820T151413Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260820T151413Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
