# IAR DRP Change Summary: 20260609T164656Z

## Source
- Current source file: `IA_INDVL_Feed_06_09_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_09_2026.xml.zip
- Retrieved at: 2026-06-09T16:46:56+00:00
- XML generated date: 2026-06-09
- XML files parsed from ZIP: 20
- SHA-256: `5a699af534be405651f27bd1a7fa00607bab54de28752a9c86c18a8704b476ad`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,325
- DRP occurrence rows parsed: 60,076
- Representatives with at least one DRP flag: 60,076

## Changes Since Previous Run
- Previous run: `20260608T172914Z`
- Total reported changes: 141
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 104
- new_representative_with_drp: 13
- representative_removed_from_feed: 11
- drp_count_changed: 6
- drp_category_added: 5
- drp_category_removed: 2

### Changed Categories
- current_employer: 104
- any_drp: 24
- drp_count: 6
- has_customer_complaint: 4
- has_judgment: 2
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260609T164656Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260609T164656Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
