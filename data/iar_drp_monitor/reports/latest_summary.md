# IAR DRP Change Summary: 20260826T155223Z

## Source
- Current source file: `IA_INDVL_Feed_08_26_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_26_2026.xml.zip
- Retrieved at: 2026-08-26T15:52:23+00:00
- XML generated date: 2026-08-26
- XML files parsed from ZIP: 20
- SHA-256: `4ee53584435f16cf8827008373bf41797e8ffd432ce1a83f1aa6e0c2f74c5b0c`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 438,473
- DRP occurrence rows parsed: 60,003
- Representatives with at least one DRP flag: 60,003

## Changes Since Previous Run
- Previous run: `20260825T150415Z`
- Total reported changes: 153
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 87
- drp_count_changed: 21
- drp_category_added: 12
- drp_category_removed: 12
- new_representative_with_drp: 12
- representative_removed_from_feed: 9

### Changed Categories
- current_employer: 87
- any_drp: 21
- drp_count: 21
- has_judgment: 12
- has_customer_complaint: 5
- has_bankrupt: 4
- has_criminal: 2
- has_civil_judgment: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260826T155223Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260826T155223Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
