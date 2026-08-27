# IAR DRP Change Summary: 20260827T235044Z

## Source
- Current source file: `IA_INDVL_Feed_08_27_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_27_2026.xml.zip
- Retrieved at: 2026-08-27T23:50:44+00:00
- XML generated date: 2026-08-27
- XML files parsed from ZIP: 20
- SHA-256: `e95b08effcd787ca9f7f452076ada4ca137fe57ee1f54c35fdefbb377b2dbd6b`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 438,588
- DRP occurrence rows parsed: 60,010
- Representatives with at least one DRP flag: 60,010

## Changes Since Previous Run
- Previous run: `20260826T155223Z`
- Total reported changes: 109
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 79
- new_representative_with_drp: 11
- drp_category_added: 6
- drp_count_changed: 5
- representative_removed_from_feed: 5
- drp_category_removed: 3

### Changed Categories
- current_employer: 79
- any_drp: 16
- drp_count: 5
- has_customer_complaint: 3
- has_judgment: 2
- has_reg_action: 1
- has_criminal: 1
- has_civil_judgment: 1
- has_bankrupt: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260827T235044Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260827T235044Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
