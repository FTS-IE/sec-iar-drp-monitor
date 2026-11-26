# IAR DRP Change Summary: 20261126T225853Z

## Source
- Current source file: `IA_INDVL_Feed_11_26_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_26_2026.xml.zip
- Retrieved at: 2026-11-26T22:58:53+00:00
- XML generated date: 2026-11-26
- XML files parsed from ZIP: 20
- SHA-256: `37321b27f2c295328de746545fef5eebc4f224376992d6ce8723b51d6aa69352`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 444,559
- DRP occurrence rows parsed: 60,108
- Representatives with at least one DRP flag: 60,108

## Changes Since Previous Run
- Previous run: `20261125T230525Z`
- Total reported changes: 124
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 79
- drp_count_changed: 13
- drp_category_added: 12
- representative_removed_from_feed: 10
- drp_category_removed: 5
- new_representative_with_drp: 5

### Changed Categories
- current_employer: 79
- any_drp: 15
- drp_count: 13
- has_judgment: 12
- has_customer_complaint: 3
- has_criminal: 1
- has_bankrupt: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261126T225853Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261126T225853Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
