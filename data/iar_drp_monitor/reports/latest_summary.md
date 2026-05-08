# IAR DRP Change Summary: 20260508T155129Z

## Source
- Current source file: `IA_INDVL_Feed_05_08_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_08_2026.xml.zip
- Retrieved at: 2026-05-08T15:51:29+00:00
- XML generated date: 2026-05-08
- XML files parsed from ZIP: 20
- SHA-256: `67723826e9c8ae114f53912b8a2fb468b6ddaadcd4d8220f1c842e641e51aaf9`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 432,871
- DRP occurrence rows parsed: 60,085
- Representatives with at least one DRP flag: 60,085

## Changes Since Previous Run
- Previous run: `20260507T161853Z`
- Total reported changes: 279
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 210
- representative_removed_from_feed: 26
- drp_category_added: 14
- drp_count_changed: 13
- new_representative_with_drp: 12
- drp_category_removed: 4

### Changed Categories
- current_employer: 210
- any_drp: 38
- drp_count: 13
- has_judgment: 7
- has_customer_complaint: 4
- has_reg_action: 3
- has_termination: 2
- has_investigation: 1
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260508T155129Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260508T155129Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
