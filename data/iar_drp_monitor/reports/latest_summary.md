# IAR DRP Change Summary: 20260521T164903Z

## Source
- Current source file: `IA_INDVL_Feed_05_21_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_21_2026.xml.zip
- Retrieved at: 2026-05-21T16:49:03+00:00
- XML generated date: 2026-05-21
- XML files parsed from ZIP: 20
- SHA-256: `85d500be4d4b82dfca4093005003979784d4aae5c8cc333820bdd6b1b3394a42`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,515
- DRP occurrence rows parsed: 60,114
- Representatives with at least one DRP flag: 60,114

## Changes Since Previous Run
- Previous run: `20260520T172846Z`
- Total reported changes: 165
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 113
- representative_removed_from_feed: 16
- new_representative_with_drp: 16
- drp_category_added: 9
- drp_count_changed: 8
- drp_category_removed: 3

### Changed Categories
- current_employer: 113
- any_drp: 32
- drp_count: 8
- has_judgment: 7
- has_customer_complaint: 3
- has_bankrupt: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260521T164903Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260521T164903Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
