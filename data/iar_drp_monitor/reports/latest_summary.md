# IAR DRP Change Summary: 20261026T195635Z

## Source
- Current source file: `IA_INDVL_Feed_10_26_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_26_2026.xml.zip
- Retrieved at: 2026-10-26T19:56:35+00:00
- XML generated date: 2026-10-26
- XML files parsed from ZIP: 18
- SHA-256: `d3665ea6e85d4ba68aae4575415a96e7a06fa33d4aeae28fc6269984f88eeb4f`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 398,319
- DRP occurrence rows parsed: 54,553
- Representatives with at least one DRP flag: 54,553

## Changes Since Previous Run
- Previous run: `20261023T181958Z`
- Total reported changes: 182
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 91
- new_representative_with_drp: 26
- representative_removed_from_feed: 26
- drp_count_changed: 17
- drp_category_added: 15
- drp_category_removed: 7

### Changed Categories
- current_employer: 91
- any_drp: 52
- drp_count: 17
- has_customer_complaint: 12
- has_bankrupt: 6
- has_reg_action: 2
- has_criminal: 1
- has_investigation: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261026T195635Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261026T195635Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
