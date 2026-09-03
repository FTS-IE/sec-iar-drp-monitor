# IAR DRP Change Summary: 20260903T175209Z

## Source
- Current source file: `IA_INDVL_Feed_09_03_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_03_2026.xml.zip
- Retrieved at: 2026-09-03T17:52:09+00:00
- XML generated date: 2026-09-03
- XML files parsed from ZIP: 20
- SHA-256: `9eb32dd92faff600731f8556997d4bfd9420d11f5083d4f4fe20992de627506d`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 439,043
- DRP occurrence rows parsed: 60,026
- Representatives with at least one DRP flag: 60,026

## Changes Since Previous Run
- Previous run: `20260902T175348Z`
- Total reported changes: 184
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 114
- representative_removed_from_feed: 21
- new_representative_with_drp: 19
- drp_count_changed: 14
- drp_category_added: 12
- drp_category_removed: 4

### Changed Categories
- current_employer: 114
- any_drp: 40
- drp_count: 14
- has_judgment: 8
- has_customer_complaint: 5
- has_bankrupt: 2
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260903T175209Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260903T175209Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
