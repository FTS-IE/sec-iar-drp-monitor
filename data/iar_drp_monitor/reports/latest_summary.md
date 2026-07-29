# IAR DRP Change Summary: 20260729T155802Z

## Source
- Current source file: `IA_INDVL_Feed_07_29_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_29_2026.xml.zip
- Retrieved at: 2026-07-29T15:58:02+00:00
- XML generated date: 2026-07-29
- XML files parsed from ZIP: 20
- SHA-256: `f1a40fa22f739503d0890ab305ddd02daa1faf883c2fff48fa8ce18920f8cbc4`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 436,573
- DRP occurrence rows parsed: 60,023
- Representatives with at least one DRP flag: 60,023

## Changes Since Previous Run
- Previous run: `20260728T162638Z`
- Total reported changes: 101
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 48
- new_representative_with_drp: 16
- representative_removed_from_feed: 14
- drp_count_changed: 11
- drp_category_removed: 6
- drp_category_added: 6

### Changed Categories
- current_employer: 48
- any_drp: 30
- drp_count: 11
- has_bankrupt: 6
- has_customer_complaint: 3
- has_judgment: 2
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260729T155802Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260729T155802Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
