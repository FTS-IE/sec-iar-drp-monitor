# IAR DRP Change Summary: 20260525T163148Z

## Source
- Current source file: `IA_INDVL_Feed_05_25_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_25_2026.xml.zip
- Retrieved at: 2026-05-25T16:31:48+00:00
- XML generated date: 2026-05-25
- XML files parsed from ZIP: 20
- SHA-256: `cf5e7e341eae19f53139af968202e955a7cdde3f4adacc558a33051b5d464712`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,599
- DRP occurrence rows parsed: 60,106
- Representatives with at least one DRP flag: 60,106

## Changes Since Previous Run
- Previous run: `20260522T163718Z`
- Total reported changes: 115
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 62
- drp_category_removed: 15
- drp_count_changed: 13
- representative_removed_from_feed: 11
- new_representative_with_drp: 8
- drp_category_added: 6

### Changed Categories
- current_employer: 62
- any_drp: 19
- drp_count: 13
- has_bankrupt: 9
- has_judgment: 7
- has_customer_complaint: 3
- has_criminal: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260525T163148Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260525T163148Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
