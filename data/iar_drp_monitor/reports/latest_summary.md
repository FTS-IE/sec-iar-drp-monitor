# IAR DRP Change Summary: 20261023T181958Z

## Source
- Current source file: `IA_INDVL_Feed_10_23_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_23_2026.xml.zip
- Retrieved at: 2026-10-23T18:19:58+00:00
- XML generated date: 2026-10-23
- XML files parsed from ZIP: 18
- SHA-256: `ae2c916f8a08634a73b7e0588f313d866da17c25595189a458c3d34d30ac7f26`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 398,212
- DRP occurrence rows parsed: 54,546
- Representatives with at least one DRP flag: 54,546

## Changes Since Previous Run
- Previous run: `20261022T183142Z`
- Total reported changes: 4,352
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- representative_removed_from_feed: 4,217
- current_employer_changed: 92
- drp_count_changed: 14
- new_representative_with_drp: 14
- drp_category_added: 13
- drp_category_removed: 2

### Changed Categories
- any_drp: 4,231
- current_employer: 92
- drp_count: 14
- has_customer_complaint: 6
- has_judgment: 5
- has_termination: 2
- has_bankrupt: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261023T181958Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261023T181958Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
