# IAR DRP Change Summary: 20261019T195513Z

## Source
- Current source file: `IA_INDVL_Feed_10_19_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_19_2026.xml.zip
- Retrieved at: 2026-10-19T19:55:13+00:00
- XML generated date: 2026-10-19
- XML files parsed from ZIP: 20
- SHA-256: `b59e9a9972d4b2714df3db45782208975903bd2490e4ab67e006f89def018976`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 441,948
- DRP occurrence rows parsed: 60,029
- Representatives with at least one DRP flag: 60,029

## Changes Since Previous Run
- Previous run: `20261016T180255Z`
- Total reported changes: 642
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 566
- new_representative_with_drp: 21
- drp_count_changed: 17
- representative_removed_from_feed: 16
- drp_category_removed: 12
- drp_category_added: 10

### Changed Categories
- current_employer: 566
- any_drp: 37
- drp_count: 17
- has_bankrupt: 14
- has_judgment: 3
- has_customer_complaint: 3
- has_reg_action: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261019T195513Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261019T195513Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
