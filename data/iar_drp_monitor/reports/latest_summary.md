# IAR DRP Change Summary: 20261014T183706Z

## Source
- Current source file: `IA_INDVL_Feed_10_14_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_14_2026.xml.zip
- Retrieved at: 2026-10-14T18:37:06+00:00
- XML generated date: 2026-10-14
- XML files parsed from ZIP: 20
- SHA-256: `6e272cf6425143b4856730d4bfedee37134f3596555eb387b3892e4c45c0c4ea`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 441,731
- DRP occurrence rows parsed: 60,027
- Representatives with at least one DRP flag: 60,027

## Changes Since Previous Run
- Previous run: `20261013T201453Z`
- Total reported changes: 179
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 82
- representative_removed_from_feed: 29
- new_representative_with_drp: 20
- drp_count_changed: 20
- drp_category_removed: 14
- drp_category_added: 14

### Changed Categories
- current_employer: 82
- any_drp: 49
- drp_count: 20
- has_bankrupt: 11
- has_judgment: 8
- has_customer_complaint: 6
- has_civil_judgment: 1
- has_termination: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261014T183706Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261014T183706Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
