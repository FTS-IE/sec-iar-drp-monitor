# IAR DRP Change Summary: 20260619T164045Z

## Source
- Current source file: `IA_INDVL_Feed_06_19_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_19_2026.xml.zip
- Retrieved at: 2026-06-19T16:40:45+00:00
- XML generated date: 2026-06-19
- XML files parsed from ZIP: 20
- SHA-256: `5a865a5b2fe982f3d5e86a62a8886438cd089814f6850a22d9f1ba92927d74a3`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,937
- DRP occurrence rows parsed: 60,081
- Representatives with at least one DRP flag: 60,081

## Changes Since Previous Run
- Previous run: `20260618T172900Z`
- Total reported changes: 153
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 109
- drp_count_changed: 12
- new_representative_with_drp: 10
- representative_removed_from_feed: 9
- drp_category_added: 8
- drp_category_removed: 5

### Changed Categories
- current_employer: 109
- any_drp: 19
- drp_count: 12
- has_customer_complaint: 8
- has_judgment: 4
- has_bankrupt: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260619T164045Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260619T164045Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
