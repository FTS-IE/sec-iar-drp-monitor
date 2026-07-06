# IAR DRP Change Summary: 20260706T171531Z

## Source
- Current source file: `IA_INDVL_Feed_07_06_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_06_2026.xml.zip
- Retrieved at: 2026-07-06T17:15:31+00:00
- XML generated date: 2026-07-06
- XML files parsed from ZIP: 20
- SHA-256: `52d4b9b24302c2a2f7021d73d9b0cf883132a5daf7bb88de854ad515422262a9`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 435,632
- DRP occurrence rows parsed: 60,059
- Representatives with at least one DRP flag: 60,059

## Changes Since Previous Run
- Previous run: `20260703T160040Z`
- Total reported changes: 46
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 31
- new_representative_with_drp: 6
- representative_removed_from_feed: 4
- drp_category_removed: 3
- drp_count_changed: 2

### Changed Categories
- current_employer: 31
- any_drp: 10
- has_bankrupt: 3
- drp_count: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260706T171531Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260706T171531Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
