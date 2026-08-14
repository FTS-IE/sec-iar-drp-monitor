# IAR DRP Change Summary: 20260814T150626Z

## Source
- Current source file: `IA_INDVL_Feed_08_14_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_14_2026.xml.zip
- Retrieved at: 2026-08-14T15:06:26+00:00
- XML generated date: 2026-08-14
- XML files parsed from ZIP: 20
- SHA-256: `cbb99c798118cb64e2e445e4faabd257051ab47354ebbac620c70edea7cc7d38`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,654
- DRP occurrence rows parsed: 60,022
- Representatives with at least one DRP flag: 60,022

## Changes Since Previous Run
- Previous run: `20260813T152718Z`
- Total reported changes: 104
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 63
- representative_removed_from_feed: 11
- drp_count_changed: 11
- drp_category_added: 9
- new_representative_with_drp: 6
- drp_category_removed: 4

### Changed Categories
- current_employer: 63
- any_drp: 17
- drp_count: 11
- has_customer_complaint: 7
- has_judgment: 4
- has_bankrupt: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260814T150626Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260814T150626Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
