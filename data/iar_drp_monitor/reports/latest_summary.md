# IAR DRP Change Summary: 20260821T145245Z

## Source
- Current source file: `IA_INDVL_Feed_08_21_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_21_2026.xml.zip
- Retrieved at: 2026-08-21T14:52:45+00:00
- XML generated date: 2026-08-21
- XML files parsed from ZIP: 20
- SHA-256: `54c7ad91266ec7f35a2eb4dc6a9a4fe70fa0e5f8be80fc5a186621d6f46883e9`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,976
- DRP occurrence rows parsed: 60,012
- Representatives with at least one DRP flag: 60,012

## Changes Since Previous Run
- Previous run: `20260820T151413Z`
- Total reported changes: 170
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 136
- drp_count_changed: 8
- new_representative_with_drp: 8
- representative_removed_from_feed: 7
- drp_category_added: 6
- drp_category_removed: 5

### Changed Categories
- current_employer: 136
- any_drp: 15
- drp_count: 8
- has_judgment: 5
- has_customer_complaint: 4
- has_criminal: 1
- has_bankrupt: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260821T145245Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260821T145245Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
