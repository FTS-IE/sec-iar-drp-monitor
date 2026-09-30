# IAR DRP Change Summary: 20260930T192252Z

## Source
- Current source file: `IA_INDVL_Feed_09_30_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_30_2026.xml.zip
- Retrieved at: 2026-09-30T19:22:52+00:00
- XML generated date: 2026-09-30
- XML files parsed from ZIP: 19
- SHA-256: `5e54b4c9d91f411dabb8e7033c3a2294f03c0f32604b90a387642949795deb28`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 418,795
- DRP occurrence rows parsed: 59,406
- Representatives with at least one DRP flag: 59,406

## Changes Since Previous Run
- Previous run: `20260929T192527Z`
- Total reported changes: 1,009
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- representative_removed_from_feed: 659
- current_employer_changed: 294
- new_representative_with_drp: 18
- drp_count_changed: 17
- drp_category_added: 12
- drp_category_removed: 9

### Changed Categories
- any_drp: 677
- current_employer: 294
- drp_count: 17
- has_bankrupt: 8
- has_customer_complaint: 7
- has_criminal: 2
- has_judgment: 2
- has_investigation: 1
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260930T192252Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260930T192252Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
