# IAR DRP Change Summary: 20260520T172846Z

## Source
- Current source file: `IA_INDVL_Feed_05_20_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_20_2026.xml.zip
- Retrieved at: 2026-05-20T17:28:46+00:00
- XML generated date: 2026-05-20
- XML files parsed from ZIP: 20
- SHA-256: `d51f62fac722038ce4a02c6008320d26aea79974ca7a40287a6c9d39b98ad77f`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,454
- DRP occurrence rows parsed: 60,110
- Representatives with at least one DRP flag: 60,110

## Changes Since Previous Run
- Previous run: `20260519T171337Z`
- Total reported changes: 136
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 94
- representative_removed_from_feed: 12
- drp_count_changed: 10
- new_representative_with_drp: 10
- drp_category_added: 6
- drp_category_removed: 4

### Changed Categories
- current_employer: 94
- any_drp: 22
- drp_count: 10
- has_bankrupt: 5
- has_judgment: 4
- has_customer_complaint: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260520T172846Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260520T172846Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
