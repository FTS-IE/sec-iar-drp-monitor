# IAR DRP Change Summary: 20260506T161034Z

## Source
- Current source file: `IA_INDVL_Feed_05_06_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_06_2026.xml.zip
- Retrieved at: 2026-05-06T16:10:34+00:00
- XML generated date: 2026-05-06
- SHA-256: `ae65ca73efd7d6292167820f76785585dc99e27a432d074528467809319bb972`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 21,642
- DRP occurrence rows parsed: 4,864
- Representatives with at least one DRP flag: 4,864

## Changes Since Previous Run
- Previous run: `20260505T154955Z`
- Total reported changes: 9,062
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- new_representative_with_drp: 4,848
- representative_removed_from_feed: 4,214

### Changed Categories
- any_drp: 9,062

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260506T161034Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260506T161034Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
