# IAR DRP Change Summary: 20261028T193300Z

## Source
- Current source file: `IA_INDVL_Feed_10_28_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_28_2026.xml.zip
- Retrieved at: 2026-10-28T19:33:00+00:00
- XML generated date: 2026-10-28
- XML files parsed from ZIP: 20
- SHA-256: `064a93c77df84b0e6ace83b4a562cdcb25773288f799c5e3a637d59bfae0ab6d`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 442,755
- DRP occurrence rows parsed: 60,090
- Representatives with at least one DRP flag: 60,090

## Changes Since Previous Run
- Previous run: `20261027T193133Z`
- Total reported changes: 182
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 116
- new_representative_with_drp: 20
- drp_category_added: 17
- drp_count_changed: 17
- drp_category_removed: 6
- representative_removed_from_feed: 6

### Changed Categories
- current_employer: 116
- any_drp: 26
- drp_count: 17
- has_judgment: 10
- has_customer_complaint: 7
- has_criminal: 2
- has_bankrupt: 2
- has_civil_judgment: 1
- has_investigation: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261028T193300Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261028T193300Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
