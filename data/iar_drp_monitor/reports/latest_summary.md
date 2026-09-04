# IAR DRP Change Summary: 20260904T173539Z

## Source
- Current source file: `IA_INDVL_Feed_09_04_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_04_2026.xml.zip
- Retrieved at: 2026-09-04T17:35:39+00:00
- XML generated date: 2026-09-04
- XML files parsed from ZIP: 20
- SHA-256: `f8d12d76fe8f2f3fc6b394264d48f1879b60371a3b408175202a165f6b471eeb`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,097
- DRP occurrence rows parsed: 60,010
- Representatives with at least one DRP flag: 60,010

## Changes Since Previous Run
- Previous run: `20260903T175209Z`
- Total reported changes: 174
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 108
- representative_removed_from_feed: 23
- drp_count_changed: 17
- drp_category_added: 13
- drp_category_removed: 9
- new_representative_with_drp: 4

### Changed Categories
- current_employer: 108
- any_drp: 27
- drp_count: 17
- has_judgment: 8
- has_customer_complaint: 6
- has_criminal: 4
- has_bankrupt: 3
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260904T173539Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260904T173539Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
