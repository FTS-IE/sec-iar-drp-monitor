# IAR DRP Change Summary: 20260616T183923Z

## Source
- Current source file: `IA_INDVL_Feed_06_16_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_16_2026.xml.zip
- Retrieved at: 2026-06-16T18:39:23+00:00
- XML generated date: 2026-06-16
- XML files parsed from ZIP: 20
- SHA-256: `f47b516e24a305d19596d3104c0723048ce7b501db4cbf3bf676b9a4419733c6`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,766
- DRP occurrence rows parsed: 60,070
- Representatives with at least one DRP flag: 60,070

## Changes Since Previous Run
- Previous run: `20260615T184634Z`
- Total reported changes: 157
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 97
- new_representative_with_drp: 16
- drp_count_changed: 15
- representative_removed_from_feed: 13
- drp_category_added: 12
- drp_category_removed: 4

### Changed Categories
- current_employer: 97
- any_drp: 29
- drp_count: 15
- has_customer_complaint: 8
- has_judgment: 5
- has_bankrupt: 2
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260616T183923Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260616T183923Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
