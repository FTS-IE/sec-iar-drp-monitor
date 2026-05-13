# IAR DRP Change Summary: 20260513T163255Z

## Source
- Current source file: `IA_INDVL_Feed_05_13_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_13_2026.xml.zip
- Retrieved at: 2026-05-13T16:32:55+00:00
- XML generated date: 2026-05-13
- XML files parsed from ZIP: 20
- SHA-256: `9546afcd7a82e6812f87c2eba62f5bcaff320ee8d78b3d811a8d4e089a99fec0`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,079
- DRP occurrence rows parsed: 60,083
- Representatives with at least one DRP flag: 60,083

## Changes Since Previous Run
- Previous run: `20260512T163211Z`
- Total reported changes: 182
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 117
- representative_removed_from_feed: 17
- drp_count_changed: 15
- new_representative_with_drp: 15
- drp_category_added: 13
- drp_category_removed: 5

### Changed Categories
- current_employer: 117
- any_drp: 32
- drp_count: 15
- has_customer_complaint: 8
- has_judgment: 4
- has_bankrupt: 3
- has_criminal: 2
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260513T163255Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260513T163255Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
