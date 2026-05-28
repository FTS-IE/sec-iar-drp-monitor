# IAR DRP Change Summary: 20260528T174407Z

## Source
- Current source file: `IA_INDVL_Feed_05_28_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_28_2026.xml.zip
- Retrieved at: 2026-05-28T17:44:07+00:00
- XML generated date: 2026-05-28
- XML files parsed from ZIP: 20
- SHA-256: `2ae86bb9f20c80e145e86773c7786f80c70d61b935bc263eb387995ec6b37713`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,748
- DRP occurrence rows parsed: 60,119
- Representatives with at least one DRP flag: 60,119

## Changes Since Previous Run
- Previous run: `20260527T173415Z`
- Total reported changes: 141
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 91
- new_representative_with_drp: 14
- drp_count_changed: 11
- representative_removed_from_feed: 9
- drp_category_added: 8
- drp_category_removed: 8

### Changed Categories
- current_employer: 91
- any_drp: 23
- drp_count: 11
- has_judgment: 7
- has_customer_complaint: 3
- has_bankrupt: 2
- has_termination: 2
- has_civil_judgment: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260528T174407Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260528T174407Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
