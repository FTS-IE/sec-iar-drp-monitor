# IAR DRP Change Summary: 20261016T180255Z

## Source
- Current source file: `IA_INDVL_Feed_10_16_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_16_2026.xml.zip
- Retrieved at: 2026-10-16T18:02:55+00:00
- XML generated date: 2026-10-16
- XML files parsed from ZIP: 20
- SHA-256: `1a07790692f1332151af18c93668c49bc43ab393d7f0e546cf1bdbbf3c1703e6`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 441,884
- DRP occurrence rows parsed: 60,027
- Representatives with at least one DRP flag: 60,027

## Changes Since Previous Run
- Previous run: `20261015T181730Z`
- Total reported changes: 249
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 179
- drp_category_added: 20
- drp_count_changed: 19
- representative_removed_from_feed: 15
- new_representative_with_drp: 11
- drp_category_removed: 5

### Changed Categories
- current_employer: 179
- any_drp: 26
- drp_count: 19
- has_customer_complaint: 14
- has_judgment: 8
- has_criminal: 2
- has_bankrupt: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261016T180255Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261016T180255Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
