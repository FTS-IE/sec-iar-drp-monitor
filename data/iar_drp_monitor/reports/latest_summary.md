# IAR DRP Change Summary: 20260601T192458Z

## Source
- Current source file: `IA_INDVL_Feed_06_01_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_01_2026.xml.zip
- Retrieved at: 2026-06-01T19:24:58+00:00
- XML generated date: 2026-06-01
- XML files parsed from ZIP: 20
- SHA-256: `1bb76c17414b1b1ea3d6a5e5b4e08f09817519495e835c87920dc149822e9b0f`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,895
- DRP occurrence rows parsed: 60,114
- Representatives with at least one DRP flag: 60,114

## Changes Since Previous Run
- Previous run: `20260529T174431Z`
- Total reported changes: 163
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 88
- drp_count_changed: 26
- drp_category_removed: 19
- representative_removed_from_feed: 12
- drp_category_added: 10
- new_representative_with_drp: 8

### Changed Categories
- current_employer: 88
- drp_count: 26
- any_drp: 20
- has_bankrupt: 17
- has_customer_complaint: 7
- has_judgment: 4
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260601T192458Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260601T192458Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
