# IAR DRP Change Summary: 20260917T181238Z

## Source
- Current source file: `IA_INDVL_Feed_09_17_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_17_2026.xml.zip
- Retrieved at: 2026-09-17T18:12:38+00:00
- XML generated date: 2026-09-17
- XML files parsed from ZIP: 20
- SHA-256: `3b08f5915c5cf8f74cef8053e60bba9ed6bf232ab8eb6df7636e56712183e2eb`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,739
- DRP occurrence rows parsed: 60,006
- Representatives with at least one DRP flag: 60,006

## Changes Since Previous Run
- Previous run: `20260916T181118Z`
- Total reported changes: 133
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 79
- representative_removed_from_feed: 14
- drp_count_changed: 13
- drp_category_added: 13
- new_representative_with_drp: 11
- drp_category_removed: 3

### Changed Categories
- current_employer: 79
- any_drp: 25
- drp_count: 13
- has_customer_complaint: 10
- has_bankrupt: 3
- has_judgment: 2
- has_bond: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260917T181238Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260917T181238Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
