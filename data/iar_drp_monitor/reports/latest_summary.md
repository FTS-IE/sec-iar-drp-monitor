# IAR DRP Change Summary: 20261125T230525Z

## Source
- Current source file: `IA_INDVL_Feed_11_25_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_25_2026.xml.zip
- Retrieved at: 2026-11-25T23:05:25+00:00
- XML generated date: 2026-11-25
- XML files parsed from ZIP: 20
- SHA-256: `2ea4952026e5060cd1be86daed0e88713974b42cadeb15173c3f76da0362aa9c`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 444,478
- DRP occurrence rows parsed: 60,108
- Representatives with at least one DRP flag: 60,108

## Changes Since Previous Run
- Previous run: `20261124T232849Z`
- Total reported changes: 152
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 84
- new_representative_with_drp: 19
- representative_removed_from_feed: 18
- drp_count_changed: 12
- drp_category_added: 10
- drp_category_removed: 9

### Changed Categories
- current_employer: 84
- any_drp: 37
- has_judgment: 12
- drp_count: 12
- has_bankrupt: 3
- has_criminal: 2
- has_customer_complaint: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261125T230525Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261125T230525Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
