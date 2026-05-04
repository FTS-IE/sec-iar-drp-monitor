# IAR DRP Change Summary: 20260504T151753Z

## Source
- Current source file: `IA_INDVL_Feed_05_04_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_04_2026.xml.zip
- Retrieved at: 2026-05-04T15:17:53+00:00
- XML generated date: 2026-05-04
- SHA-256: `624f3200c89c24c89eb5811f48014d5e6fa7a7ab5d41b843f04fb7460ea0611a`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags only; non-DRP profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 21,638
- DRP occurrence rows parsed: 4,865
- Representatives with at least one DRP flag: 4,865

## Changes Since Previous Run
- Previous run: `20260501T155422Z`
- Total DRP-related changes: 9,077
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- new_representative_with_drp: 4,859
- representative_removed_from_feed: 4,218

### Changed Categories
- any_drp: 9,077

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260504T151753Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260504T151753Z_drps.csv`
- DRP rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
