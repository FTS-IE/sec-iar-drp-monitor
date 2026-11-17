# IAR DRP Change Summary: 20261117T222132Z

## Source
- Current source file: `IA_INDVL_Feed_11_17_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_17_2026.xml.zip
- Retrieved at: 2026-11-17T22:21:32+00:00
- XML generated date: 2026-11-17
- XML files parsed from ZIP: 20
- SHA-256: `d0f06167460f344cd24fef9e90b0c2206317cf48aee4d86dc63e9397befd432a`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 443,907
- DRP occurrence rows parsed: 60,100
- Representatives with at least one DRP flag: 60,100

## Changes Since Previous Run
- Previous run: `20261116T232326Z`
- Total reported changes: 375
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 319
- representative_removed_from_feed: 19
- new_representative_with_drp: 15
- drp_count_changed: 9
- drp_category_added: 8
- drp_category_removed: 5

### Changed Categories
- current_employer: 319
- any_drp: 34
- drp_count: 9
- has_bankrupt: 6
- has_judgment: 3
- has_customer_complaint: 2
- has_reg_action: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261117T222132Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261117T222132Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
