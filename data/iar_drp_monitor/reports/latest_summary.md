# IAR DRP Change Summary: 20261111T212432Z

## Source
- Current source file: `IA_INDVL_Feed_11_11_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_11_2026.xml.zip
- Retrieved at: 2026-11-11T21:24:32+00:00
- XML generated date: 2026-11-11
- XML files parsed from ZIP: 20
- SHA-256: `9e8854243735f9f1595c5293382d6eaaa6a2974e863ec88998963ae47213c4ae`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 443,684
- DRP occurrence rows parsed: 60,111
- Representatives with at least one DRP flag: 60,111

## Changes Since Previous Run
- Previous run: `20261110T204846Z`
- Total reported changes: 170
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 100
- new_representative_with_drp: 22
- representative_removed_from_feed: 21
- drp_count_changed: 12
- drp_category_added: 9
- drp_category_removed: 6

### Changed Categories
- current_employer: 100
- any_drp: 43
- drp_count: 12
- has_customer_complaint: 6
- has_bankrupt: 3
- has_reg_action: 2
- has_judgment: 2
- has_civil_judgment: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261111T212432Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261111T212432Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
