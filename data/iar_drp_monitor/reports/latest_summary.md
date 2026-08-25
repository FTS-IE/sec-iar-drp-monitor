# IAR DRP Change Summary: 20260825T150415Z

## Source
- Current source file: `IA_INDVL_Feed_08_25_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_25_2026.xml.zip
- Retrieved at: 2026-08-25T15:04:15+00:00
- XML generated date: 2026-08-25
- XML files parsed from ZIP: 20
- SHA-256: `c2b3fa6a4c63d6bc337ef2ebf79b4f3633eecb1ed84d88a207c6665cca30244e`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 438,355
- DRP occurrence rows parsed: 59,999
- Representatives with at least one DRP flag: 59,999

## Changes Since Previous Run
- Previous run: `20260824T152220Z`
- Total reported changes: 169
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 94
- representative_removed_from_feed: 19
- drp_count_changed: 19
- drp_category_added: 15
- new_representative_with_drp: 13
- drp_category_removed: 9

### Changed Categories
- current_employer: 94
- any_drp: 32
- drp_count: 19
- has_customer_complaint: 9
- has_bankrupt: 7
- has_judgment: 6
- has_criminal: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260825T150415Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260825T150415Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
