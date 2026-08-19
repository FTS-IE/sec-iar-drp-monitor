# IAR DRP Change Summary: 20260819T145303Z

## Source
- Current source file: `IA_INDVL_Feed_08_19_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_19_2026.xml.zip
- Retrieved at: 2026-08-19T14:53:03+00:00
- XML generated date: 2026-08-19
- XML files parsed from ZIP: 20
- SHA-256: `cb015cd6055e0551f6d2730c66375c94b3aef9323e4deb2c8ee516252222ed36`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,859
- DRP occurrence rows parsed: 60,015
- Representatives with at least one DRP flag: 60,015

## Changes Since Previous Run
- Previous run: `20260818T145208Z`
- Total reported changes: 167
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 92
- drp_count_changed: 22
- drp_category_added: 16
- representative_removed_from_feed: 15
- new_representative_with_drp: 14
- drp_category_removed: 8

### Changed Categories
- current_employer: 92
- any_drp: 29
- drp_count: 22
- has_bankrupt: 10
- has_judgment: 5
- has_customer_complaint: 4
- has_termination: 2
- has_criminal: 2
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260819T145303Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260819T145303Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
