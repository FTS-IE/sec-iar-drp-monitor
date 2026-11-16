# IAR DRP Change Summary: 20261116T232326Z

## Source
- Current source file: `IA_INDVL_Feed_11_16_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_16_2026.xml.zip
- Retrieved at: 2026-11-16T23:23:26+00:00
- XML generated date: 2026-11-16
- XML files parsed from ZIP: 20
- SHA-256: `3a0610a01c71628f93295356042cd7d1334c66b04ce977c7f8849b8c4b1071bc`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 443,856
- DRP occurrence rows parsed: 60,101
- Representatives with at least one DRP flag: 60,101

## Changes Since Previous Run
- Previous run: `20261113T205354Z`
- Total reported changes: 180
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 111
- drp_count_changed: 20
- representative_removed_from_feed: 16
- drp_category_removed: 13
- new_representative_with_drp: 10
- drp_category_added: 10

### Changed Categories
- current_employer: 111
- any_drp: 26
- drp_count: 20
- has_bankrupt: 11
- has_customer_complaint: 5
- has_termination: 3
- has_judgment: 2
- has_criminal: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261116T232326Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261116T232326Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
