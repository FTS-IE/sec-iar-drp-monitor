# IAR DRP Change Summary: 20260731T161039Z

## Source
- Current source file: `IA_INDVL_Feed_07_31_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_07_31_2026.xml.zip
- Retrieved at: 2026-07-31T16:10:39+00:00
- XML generated date: 2026-07-31
- XML files parsed from ZIP: 20
- SHA-256: `01d69a60b0bcdb80929951719044f7a308cdaf98ea4bff11d40d5252d4b3b8ca`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 436,800
- DRP occurrence rows parsed: 60,038
- Representatives with at least one DRP flag: 60,038

## Changes Since Previous Run
- Previous run: `20260730T160002Z`
- Total reported changes: 156
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 95
- new_representative_with_drp: 17
- drp_count_changed: 14
- drp_category_added: 14
- representative_removed_from_feed: 11
- drp_category_removed: 5

### Changed Categories
- current_employer: 95
- any_drp: 28
- drp_count: 14
- has_customer_complaint: 7
- has_judgment: 6
- has_termination: 3
- has_bankrupt: 3

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260731T161039Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260731T161039Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
