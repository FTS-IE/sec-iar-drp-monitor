# IAR DRP Change Summary: 20260629T171208Z

## Source
- Current source file: `IA_INDVL_Feed_06_29_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_29_2026.xml.zip
- Retrieved at: 2026-06-29T17:12:08+00:00
- XML generated date: 2026-06-29
- XML files parsed from ZIP: 20
- SHA-256: `44626c4df7186b606adb519693e932314c06bf4719ef6c5386ee05fb47574e60`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,305
- DRP occurrence rows parsed: 60,074
- Representatives with at least one DRP flag: 60,074

## Changes Since Previous Run
- Previous run: `20260626T162742Z`
- Total reported changes: 283
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 213
- representative_removed_from_feed: 23
- drp_count_changed: 15
- new_representative_with_drp: 11
- drp_category_added: 11
- drp_category_removed: 10

### Changed Categories
- current_employer: 213
- any_drp: 34
- drp_count: 15
- has_bankrupt: 8
- has_customer_complaint: 6
- has_judgment: 4
- has_reg_action: 1
- has_investigation: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260629T171208Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260629T171208Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
