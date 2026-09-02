# IAR DRP Change Summary: 20260902T175348Z

## Source
- Current source file: `IA_INDVL_Feed_09_02_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_02_2026.xml.zip
- Retrieved at: 2026-09-02T17:53:48+00:00
- XML generated date: 2026-09-02
- XML files parsed from ZIP: 20
- SHA-256: `5759cb5acfee492bd356a146ce9c8cde18bcf92e705126b0fb4a1f2d290cc971`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,017
- DRP occurrence rows parsed: 60,022
- Representatives with at least one DRP flag: 60,022

## Changes Since Previous Run
- Previous run: `20260901T174858Z`
- Total reported changes: 211
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 148
- new_representative_with_drp: 21
- representative_removed_from_feed: 20
- drp_count_changed: 10
- drp_category_added: 8
- drp_category_removed: 4

### Changed Categories
- current_employer: 148
- any_drp: 41
- drp_count: 10
- has_customer_complaint: 4
- has_judgment: 3
- has_bankrupt: 3
- has_criminal: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260902T175348Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260902T175348Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
