# IAR DRP Change Summary: 20261102T224616Z

## Source
- Current source file: `IA_INDVL_Feed_11_02_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_02_2026.xml.zip
- Retrieved at: 2026-11-02T22:46:16+00:00
- XML generated date: 2026-11-02
- XML files parsed from ZIP: 20
- SHA-256: `e931fbab72b2a4f0f7f85b2f3cb70a17163d1f4195a3cdc176adb19b76e51379`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 443,059
- DRP occurrence rows parsed: 60,091
- Representatives with at least one DRP flag: 60,091

## Changes Since Previous Run
- Previous run: `20261030T192022Z`
- Total reported changes: 277
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 177
- drp_count_changed: 31
- drp_category_removed: 25
- representative_removed_from_feed: 18
- new_representative_with_drp: 13
- drp_category_added: 13

### Changed Categories
- current_employer: 177
- any_drp: 31
- drp_count: 31
- has_bankrupt: 25
- has_judgment: 6
- has_customer_complaint: 6
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261102T224616Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261102T224616Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
