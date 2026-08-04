# IAR DRP Change Summary: 20260804T162150Z

## Source
- Current source file: `IA_INDVL_Feed_08_04_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_04_2026.xml.zip
- Retrieved at: 2026-08-04T16:21:50+00:00
- XML generated date: 2026-08-04
- XML files parsed from ZIP: 20
- SHA-256: `095a75e19b73e47c8c16c096fd6db175d6ec1aabe45db4c3d64086c63d696fa7`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,005
- DRP occurrence rows parsed: 60,019
- Representatives with at least one DRP flag: 60,019

## Changes Since Previous Run
- Previous run: `20260803T164004Z`
- Total reported changes: 177
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 116
- representative_removed_from_feed: 20
- drp_count_changed: 14
- new_representative_with_drp: 10
- drp_category_added: 9
- drp_category_removed: 8

### Changed Categories
- current_employer: 116
- any_drp: 30
- drp_count: 14
- has_customer_complaint: 6
- has_bankrupt: 6
- has_judgment: 4
- has_civil_judgment: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260804T162150Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260804T162150Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
