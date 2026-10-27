# IAR DRP Change Summary: 20261027T193133Z

## Source
- Current source file: `IA_INDVL_Feed_10_27_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_27_2026.xml.zip
- Retrieved at: 2026-10-27T19:31:33+00:00
- XML generated date: 2026-10-27
- XML files parsed from ZIP: 20
- SHA-256: `8b589633f08579f204824755b182f481a1cc91efecb75ee0582b208c7363711f`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 442,610
- DRP occurrence rows parsed: 60,067
- Representatives with at least one DRP flag: 60,067

## Changes Since Previous Run
- Previous run: `20261026T195635Z`
- Total reported changes: 5,662
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- new_representative_with_drp: 5,514
- current_employer_changed: 85
- drp_category_added: 23
- drp_count_changed: 22
- representative_removed_from_feed: 10
- drp_category_removed: 8

### Changed Categories
- any_drp: 5,524
- current_employer: 85
- drp_count: 22
- has_customer_complaint: 11
- has_judgment: 10
- has_bankrupt: 6
- has_criminal: 2
- has_investigation: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261027T193133Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261027T193133Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
