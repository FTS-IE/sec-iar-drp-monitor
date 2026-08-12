# IAR DRP Change Summary: 20260812T151906Z

## Source
- Current source file: `IA_INDVL_Feed_08_12_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_12_2026.xml.zip
- Retrieved at: 2026-08-12T15:19:06+00:00
- XML generated date: 2026-08-12
- XML files parsed from ZIP: 20
- SHA-256: `dada24d9b3d06b5f4b6fd04dc9a0783dee66cdb16c53f4ce522b3f6e338d483f`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,465
- DRP occurrence rows parsed: 60,009
- Representatives with at least one DRP flag: 60,009

## Changes Since Previous Run
- Previous run: `20260811T151516Z`
- Total reported changes: 140
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 93
- representative_removed_from_feed: 14
- drp_count_changed: 10
- drp_category_added: 10
- new_representative_with_drp: 8
- drp_category_removed: 5

### Changed Categories
- current_employer: 93
- any_drp: 22
- drp_count: 10
- has_customer_complaint: 4
- has_judgment: 4
- has_bankrupt: 4
- has_investigation: 2
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260812T151906Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260812T151906Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
