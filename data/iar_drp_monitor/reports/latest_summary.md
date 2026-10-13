# IAR DRP Change Summary: 20261013T201453Z

## Source
- Current source file: `IA_INDVL_Feed_10_13_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_13_2026.xml.zip
- Retrieved at: 2026-10-13T20:14:53+00:00
- XML generated date: 2026-10-13
- XML files parsed from ZIP: 20
- SHA-256: `a433e5d9b15416db835bb1f13f13edb7e647985492ef07b7342c599f649e35cf`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 441,593
- DRP occurrence rows parsed: 60,034
- Representatives with at least one DRP flag: 60,034

## Changes Since Previous Run
- Previous run: `20261012T220816Z`
- Total reported changes: 137
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 93
- representative_removed_from_feed: 15
- drp_count_changed: 10
- drp_category_added: 7
- drp_category_removed: 6
- new_representative_with_drp: 6

### Changed Categories
- current_employer: 93
- any_drp: 21
- drp_count: 10
- has_bankrupt: 5
- has_judgment: 4
- has_customer_complaint: 4

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261013T201453Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261013T201453Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
