# IAR DRP Change Summary: 20261120T214841Z

## Source
- Current source file: `IA_INDVL_Feed_11_20_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_20_2026.xml.zip
- Retrieved at: 2026-11-20T21:48:41+00:00
- XML generated date: 2026-11-20
- XML files parsed from ZIP: 20
- SHA-256: `d03ab0256aee09a6d0dd7ee3fabbc82e8075396079e93eeec9ddc643492f849f`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 444,159
- DRP occurrence rows parsed: 60,101
- Representatives with at least one DRP flag: 60,101

## Changes Since Previous Run
- Previous run: `20261119T220859Z`
- Total reported changes: 169
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 94
- drp_count_changed: 21
- drp_category_added: 20
- new_representative_with_drp: 15
- representative_removed_from_feed: 12
- drp_category_removed: 7

### Changed Categories
- current_employer: 94
- any_drp: 27
- drp_count: 21
- has_judgment: 10
- has_customer_complaint: 7
- has_bankrupt: 5
- has_criminal: 3
- has_reg_action: 1
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261120T214841Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261120T214841Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
