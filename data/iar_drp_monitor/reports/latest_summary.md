# IAR DRP Change Summary: 20261110T204846Z

## Source
- Current source file: `IA_INDVL_Feed_11_10_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_10_2026.xml.zip
- Retrieved at: 2026-11-10T20:48:46+00:00
- XML generated date: 2026-11-10
- XML files parsed from ZIP: 20
- SHA-256: `d679b9d84dfdf4dc9030f081f38cda909b2c844af60e2ac948f288be5bfa62ac`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 443,573
- DRP occurrence rows parsed: 60,108
- Representatives with at least one DRP flag: 60,108

## Changes Since Previous Run
- Previous run: `20261109T232629Z`
- Total reported changes: 948
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- new_representative_with_drp: 846
- current_employer_changed: 61
- drp_category_added: 12
- representative_removed_from_feed: 12
- drp_count_changed: 12
- drp_category_removed: 5

### Changed Categories
- any_drp: 858
- current_employer: 61
- drp_count: 12
- has_customer_complaint: 6
- has_bankrupt: 4
- has_judgment: 3
- has_investigation: 2
- has_criminal: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261110T204846Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261110T204846Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
