# IAR DRP Change Summary: 20260507T161853Z

## Source
- Current source file: `IA_INDVL_Feed_05_07_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_07_2026.xml.zip
- Retrieved at: 2026-05-07T16:18:53+00:00
- XML generated date: 2026-05-07
- XML files parsed from ZIP: 20
- SHA-256: `a99d24dbb0082c4de948774e6ff22007e56437d4c89e05739457bd8d361ad5eb`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 432,911
- DRP occurrence rows parsed: 60,094
- Representatives with at least one DRP flag: 60,094

## Changes Since Previous Run
- Previous run: `20260506T181615Z`
- Total reported changes: 154
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 101
- representative_removed_from_feed: 13
- drp_count_changed: 13
- drp_category_added: 12
- new_representative_with_drp: 8
- drp_category_removed: 7

### Changed Categories
- current_employer: 101
- any_drp: 21
- drp_count: 13
- has_judgment: 7
- has_bankrupt: 6
- has_customer_complaint: 3
- has_investigation: 2
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260507T161853Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260507T161853Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
