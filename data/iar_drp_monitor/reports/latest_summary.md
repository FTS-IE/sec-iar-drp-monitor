# IAR DRP Change Summary: 20260604T172216Z

## Source
- Current source file: `IA_INDVL_Feed_06_04_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_04_2026.xml.zip
- Retrieved at: 2026-06-04T17:22:16+00:00
- XML generated date: 2026-06-04
- XML files parsed from ZIP: 20
- SHA-256: `ad2ec2cc3e14f326fa0083dc76f004514f50ebdb3f31a9335b8ff9fe3caad955`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,161
- DRP occurrence rows parsed: 60,097
- Representatives with at least one DRP flag: 60,097

## Changes Since Previous Run
- Previous run: `20260603T183228Z`
- Total reported changes: 163
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 106
- representative_removed_from_feed: 17
- new_representative_with_drp: 16
- drp_count_changed: 11
- drp_category_added: 9
- drp_category_removed: 4

### Changed Categories
- current_employer: 106
- any_drp: 33
- drp_count: 11
- has_judgment: 5
- has_bankrupt: 4
- has_criminal: 2
- has_customer_complaint: 1
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260604T172216Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260604T172216Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
