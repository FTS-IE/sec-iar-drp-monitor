# IAR DRP Change Summary: 20260803T164004Z

## Source
- Current source file: `IA_INDVL_Feed_08_03_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_03_2026.xml.zip
- Retrieved at: 2026-08-03T16:40:04+00:00
- XML generated date: 2026-08-03
- XML files parsed from ZIP: 20
- SHA-256: `75cb2e836d0c2bc37035a33df7af1da7cb6cef886bd8e7471711fcae45bf3d7a`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 436,931
- DRP occurrence rows parsed: 60,027
- Representatives with at least one DRP flag: 60,027

## Changes Since Previous Run
- Previous run: `20260731T161039Z`
- Total reported changes: 215
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 124
- drp_category_removed: 23
- drp_count_changed: 22
- representative_removed_from_feed: 20
- new_representative_with_drp: 19
- drp_category_added: 7

### Changed Categories
- current_employer: 124
- any_drp: 39
- drp_count: 22
- has_bankrupt: 20
- has_judgment: 7
- has_customer_complaint: 3

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260803T164004Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260803T164004Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
