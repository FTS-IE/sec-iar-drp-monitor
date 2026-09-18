# IAR DRP Change Summary: 20260918T174051Z

## Source
- Current source file: `IA_INDVL_Feed_09_18_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_18_2026.xml.zip
- Retrieved at: 2026-09-18T17:40:51+00:00
- XML generated date: 2026-09-18
- XML files parsed from ZIP: 20
- SHA-256: `5895fcc1a21546a1b7a8212e9a91a7f4cd8fb3cc44c731edcc5e29c1423e51c9`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,848
- DRP occurrence rows parsed: 60,017
- Representatives with at least one DRP flag: 60,017

## Changes Since Previous Run
- Previous run: `20260917T181238Z`
- Total reported changes: 118
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 70
- new_representative_with_drp: 19
- representative_removed_from_feed: 13
- drp_category_added: 8
- drp_count_changed: 7
- drp_category_removed: 1

### Changed Categories
- current_employer: 70
- any_drp: 32
- drp_count: 7
- has_judgment: 3
- has_customer_complaint: 2
- has_termination: 2
- has_reg_action: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260918T174051Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260918T174051Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
