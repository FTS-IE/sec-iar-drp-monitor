# IAR DRP Change Summary: 20261006T193201Z

## Source
- Current source file: `IA_INDVL_Feed_10_06_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_06_2026.xml.zip
- Retrieved at: 2026-10-06T19:32:01+00:00
- XML generated date: 2026-10-06
- XML files parsed from ZIP: 20
- SHA-256: `542d369a27795223568b61636e294890cc8853cb1cb8628c4f1e4dfaaafc8b1d`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 441,121
- DRP occurrence rows parsed: 60,024
- Representatives with at least one DRP flag: 60,024

## Changes Since Previous Run
- Previous run: `20261005T212920Z`
- Total reported changes: 291
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 238
- representative_removed_from_feed: 20
- new_representative_with_drp: 16
- drp_count_changed: 7
- drp_category_removed: 6
- drp_category_added: 4

### Changed Categories
- current_employer: 238
- any_drp: 36
- drp_count: 7
- has_customer_complaint: 5
- has_judgment: 3
- has_bankrupt: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261006T193201Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261006T193201Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
