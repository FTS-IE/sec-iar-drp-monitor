# IAR DRP Change Summary: 20261118T215543Z

## Source
- Current source file: `IA_INDVL_Feed_11_18_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_18_2026.xml.zip
- Retrieved at: 2026-11-18T21:55:43+00:00
- XML generated date: 2026-11-18
- XML files parsed from ZIP: 20
- SHA-256: `360f334bc8cd87f92b5fe4bf0317569bdbd8222a9a5ef6e1d03b64eded9e13a6`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 443,968
- DRP occurrence rows parsed: 60,093
- Representatives with at least one DRP flag: 60,093

## Changes Since Previous Run
- Previous run: `20261117T222132Z`
- Total reported changes: 219
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 143
- representative_removed_from_feed: 23
- drp_count_changed: 17
- new_representative_with_drp: 15
- drp_category_added: 12
- drp_category_removed: 9

### Changed Categories
- current_employer: 143
- any_drp: 38
- drp_count: 17
- has_judgment: 7
- has_bankrupt: 7
- has_customer_complaint: 3
- has_criminal: 2
- has_investigation: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261118T215543Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261118T215543Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
