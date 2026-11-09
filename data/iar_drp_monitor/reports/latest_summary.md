# IAR DRP Change Summary: 20261109T232629Z

## Source
- Current source file: `IA_INDVL_Feed_11_09_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_09_2026.xml.zip
- Retrieved at: 2026-11-09T23:26:29+00:00
- XML generated date: 2026-11-09
- XML files parsed from ZIP: 19
- SHA-256: `15eea63fc00d45411c852d5cd5c14a7f6b172a7c7508fcb951cfd943986c718a`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 421,329
- DRP occurrence rows parsed: 59,270
- Representatives with at least one DRP flag: 59,270

## Changes Since Previous Run
- Previous run: `20261106T202647Z`
- Total reported changes: 195
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 133
- representative_removed_from_feed: 18
- drp_count_changed: 14
- new_representative_with_drp: 12
- drp_category_removed: 10
- drp_category_added: 8

### Changed Categories
- current_employer: 133
- any_drp: 30
- drp_count: 14
- has_bankrupt: 9
- has_judgment: 8
- has_customer_complaint: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261109T232629Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261109T232629Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
