# IAR DRP Change Summary: 20260608T172914Z

## Source
- Current source file: `IA_INDVL_Feed_06_08_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_08_2026.xml.zip
- Retrieved at: 2026-06-08T17:29:14+00:00
- XML generated date: 2026-06-08
- XML files parsed from ZIP: 20
- SHA-256: `1f43732f06970607f9b7512d512ad49d5dd9d6db776a65765e8c8560c9a60155`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,245
- DRP occurrence rows parsed: 60,072
- Representatives with at least one DRP flag: 60,072

## Changes Since Previous Run
- Previous run: `20260605T164001Z`
- Total reported changes: 168
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 95
- representative_removed_from_feed: 20
- drp_count_changed: 19
- drp_category_removed: 14
- drp_category_added: 12
- new_representative_with_drp: 8

### Changed Categories
- current_employer: 95
- any_drp: 28
- drp_count: 19
- has_bankrupt: 14
- has_customer_complaint: 6
- has_judgment: 5
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260608T172914Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260608T172914Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
