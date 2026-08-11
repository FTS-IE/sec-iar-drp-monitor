# IAR DRP Change Summary: 20260811T151516Z

## Source
- Current source file: `IA_INDVL_Feed_08_11_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_11_2026.xml.zip
- Retrieved at: 2026-08-11T15:15:16+00:00
- XML generated date: 2026-08-11
- XML files parsed from ZIP: 20
- SHA-256: `bd0e724d9ceeb1535a6ec23c9036a0da192bb395698cd37560ed30e37a6fa987`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,363
- DRP occurrence rows parsed: 60,011
- Representatives with at least one DRP flag: 60,011

## Changes Since Previous Run
- Previous run: `20260810T151601Z`
- Total reported changes: 194
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 131
- representative_removed_from_feed: 17
- drp_count_changed: 16
- drp_category_added: 15
- new_representative_with_drp: 10
- drp_category_removed: 5

### Changed Categories
- current_employer: 131
- any_drp: 27
- drp_count: 16
- has_customer_complaint: 9
- has_bankrupt: 6
- has_criminal: 2
- has_judgment: 2
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260811T151516Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260811T151516Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
