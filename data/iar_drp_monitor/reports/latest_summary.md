# IAR DRP Change Summary: 20260615T184634Z

## Source
- Current source file: `IA_INDVL_Feed_06_15_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_15_2026.xml.zip
- Retrieved at: 2026-06-15T18:46:34+00:00
- XML generated date: 2026-06-15
- XML files parsed from ZIP: 20
- SHA-256: `c08a15294cd431fcb8f0ad90d76949734b87c374232a4d41adb037d07a374148`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,660
- DRP occurrence rows parsed: 60,060
- Representatives with at least one DRP flag: 60,060

## Changes Since Previous Run
- Previous run: `20260612T171513Z`
- Total reported changes: 208
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 145
- representative_removed_from_feed: 18
- new_representative_with_drp: 14
- drp_count_changed: 12
- drp_category_added: 11
- drp_category_removed: 8

### Changed Categories
- current_employer: 145
- any_drp: 32
- drp_count: 12
- has_bankrupt: 8
- has_customer_complaint: 4
- has_termination: 2
- has_judgment: 2
- has_reg_action: 2
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260615T184634Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260615T184634Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
