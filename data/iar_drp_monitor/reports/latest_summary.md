# IAR DRP Change Summary: 20261127T224136Z

## Source
- Current source file: `IA_INDVL_Feed_11_27_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_27_2026.xml.zip
- Retrieved at: 2026-11-27T22:41:36+00:00
- XML generated date: 2026-11-27
- XML files parsed from ZIP: 20
- SHA-256: `e94bc852cab81f48de6e50ef1e36e9796c4324641e789e76fbd3a8937a19fb70`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 444,554
- DRP occurrence rows parsed: 60,108
- Representatives with at least one DRP flag: 60,108

## Changes Since Previous Run
- Previous run: `20261126T225853Z`
- Total reported changes: 8
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 5
- representative_removed_from_feed: 1
- drp_count_changed: 1
- drp_category_added: 1

### Changed Categories
- current_employer: 5
- any_drp: 1
- drp_count: 1
- has_judgment: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261127T224136Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261127T224136Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
