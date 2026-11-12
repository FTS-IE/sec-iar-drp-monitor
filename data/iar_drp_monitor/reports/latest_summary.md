# IAR DRP Change Summary: 20261112T212807Z

## Source
- Current source file: `IA_INDVL_Feed_11_12_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_12_2026.xml.zip
- Retrieved at: 2026-11-12T21:28:07+00:00
- XML generated date: 2026-11-12
- XML files parsed from ZIP: 20
- SHA-256: `96d96df6bf53251e29387020186205ff8c919490a1b861003f7bcfde8f613ce9`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 443,686
- DRP occurrence rows parsed: 60,104
- Representatives with at least one DRP flag: 60,104

## Changes Since Previous Run
- Previous run: `20261111T212432Z`
- Total reported changes: 90
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 57
- representative_removed_from_feed: 14
- drp_count_changed: 8
- drp_category_added: 8
- drp_category_removed: 2
- new_representative_with_drp: 1

### Changed Categories
- current_employer: 57
- any_drp: 15
- drp_count: 8
- has_bankrupt: 3
- has_customer_complaint: 2
- has_criminal: 2
- has_judgment: 2
- has_investigation: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261112T212807Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261112T212807Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
