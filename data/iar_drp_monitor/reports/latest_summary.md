# IAR DRP Change Summary: 20260618T172900Z

## Source
- Current source file: `IA_INDVL_Feed_06_18_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_18_2026.xml.zip
- Retrieved at: 2026-06-18T17:29:00+00:00
- XML generated date: 2026-06-18
- XML files parsed from ZIP: 20
- SHA-256: `72d08b1781a1ae3ee1638a5d4d7dccf9a3f69375a54ce7f7252a581c6033d9b0`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,860
- DRP occurrence rows parsed: 60,076
- Representatives with at least one DRP flag: 60,076

## Changes Since Previous Run
- Previous run: `20260617T172305Z`
- Total reported changes: 165
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 101
- new_representative_with_drp: 20
- representative_removed_from_feed: 15
- drp_count_changed: 13
- drp_category_added: 11
- drp_category_removed: 5

### Changed Categories
- current_employer: 101
- any_drp: 35
- drp_count: 13
- has_judgment: 6
- has_customer_complaint: 4
- has_criminal: 3
- has_reg_action: 1
- has_bankrupt: 1
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260618T172900Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260618T172900Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
