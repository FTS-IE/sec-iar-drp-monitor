# IAR DRP Change Summary: 20260519T171337Z

## Source
- Current source file: `IA_INDVL_Feed_05_19_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_19_2026.xml.zip
- Retrieved at: 2026-05-19T17:13:37+00:00
- XML generated date: 2026-05-19
- XML files parsed from ZIP: 20
- SHA-256: `77cde7a49c74655f90c09b56b3b09ab45dd9c52cdf53747fd1a6e6b2587547a8`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,414
- DRP occurrence rows parsed: 60,110
- Representatives with at least one DRP flag: 60,110

## Changes Since Previous Run
- Previous run: `20260518T171116Z`
- Total reported changes: 148
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 101
- new_representative_with_drp: 16
- representative_removed_from_feed: 10
- drp_count_changed: 9
- drp_category_added: 8
- drp_category_removed: 4

### Changed Categories
- current_employer: 101
- any_drp: 26
- drp_count: 9
- has_judgment: 5
- has_bankrupt: 3
- has_criminal: 2
- has_civil_judgment: 1
- has_customer_complaint: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260519T171337Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260519T171337Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
