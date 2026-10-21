# IAR DRP Change Summary: 20261021T183752Z

## Source
- Current source file: `IA_INDVL_Feed_10_21_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_21_2026.xml.zip
- Retrieved at: 2026-10-21T18:37:52+00:00
- XML generated date: 2026-10-21
- XML files parsed from ZIP: 20
- SHA-256: `60717553ff54f315f98b3c7a7ac0178b0d1a3263fd7721ad4be78bd1008f2e2b`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 442,150
- DRP occurrence rows parsed: 60,036
- Representatives with at least one DRP flag: 60,036

## Changes Since Previous Run
- Previous run: `20261020T182733Z`
- Total reported changes: 150
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 100
- new_representative_with_drp: 18
- drp_count_changed: 11
- drp_category_added: 7
- drp_category_removed: 7
- representative_removed_from_feed: 7

### Changed Categories
- current_employer: 100
- any_drp: 25
- drp_count: 11
- has_judgment: 9
- has_bankrupt: 3
- has_customer_complaint: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261021T183752Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261021T183752Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
