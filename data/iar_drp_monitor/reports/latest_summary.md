# IAR DRP Change Summary: 20261001T193121Z

## Source
- Current source file: `IA_INDVL_Feed_10_01_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_01_2026.xml.zip
- Retrieved at: 2026-10-01T19:31:21+00:00
- XML generated date: 2026-10-01
- XML files parsed from ZIP: 19
- SHA-256: `0552a3759d69a6dd55dd49b8e52a8d2f23b06390cdea05d493025900c4d3f5ef`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 418,847
- DRP occurrence rows parsed: 59,400
- Representatives with at least one DRP flag: 59,400

## Changes Since Previous Run
- Previous run: `20260930T192252Z`
- Total reported changes: 312
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 238
- representative_removed_from_feed: 22
- drp_count_changed: 17
- drp_category_added: 14
- new_representative_with_drp: 11
- drp_category_removed: 10

### Changed Categories
- current_employer: 238
- any_drp: 33
- drp_count: 17
- has_bankrupt: 11
- has_customer_complaint: 7
- has_judgment: 5
- has_investigation: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261001T193121Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261001T193121Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
