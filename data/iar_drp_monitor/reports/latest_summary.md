# IAR DRP Change Summary: 20260805T160849Z

## Source
- Current source file: `IA_INDVL_Feed_08_05_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_05_2026.xml.zip
- Retrieved at: 2026-08-05T16:08:49+00:00
- XML generated date: 2026-08-05
- XML files parsed from ZIP: 20
- SHA-256: `6a4f0f555b66fc2ce74d55447dd0ad41127c80fc772765c40604f2b00a73d64d`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,104
- DRP occurrence rows parsed: 60,024
- Representatives with at least one DRP flag: 60,024

## Changes Since Previous Run
- Previous run: `20260804T162150Z`
- Total reported changes: 195
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 129
- new_representative_with_drp: 21
- representative_removed_from_feed: 15
- drp_count_changed: 13
- drp_category_added: 9
- drp_category_removed: 8

### Changed Categories
- current_employer: 129
- any_drp: 36
- drp_count: 13
- has_judgment: 8
- has_bankrupt: 5
- has_reg_action: 2
- has_criminal: 1
- has_customer_complaint: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260805T160849Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260805T160849Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
