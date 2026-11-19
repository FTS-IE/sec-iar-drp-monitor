# IAR DRP Change Summary: 20261119T220859Z

## Source
- Current source file: `IA_INDVL_Feed_11_19_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_19_2026.xml.zip
- Retrieved at: 2026-11-19T22:08:59+00:00
- XML generated date: 2026-11-19
- XML files parsed from ZIP: 20
- SHA-256: `41ce80972203b1de9958841915c1b8031d72e9c88c01f9ccaabb9566ad7f268a`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 444,069
- DRP occurrence rows parsed: 60,089
- Representatives with at least one DRP flag: 60,089

## Changes Since Previous Run
- Previous run: `20261118T215543Z`
- Total reported changes: 150
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 105
- representative_removed_from_feed: 19
- new_representative_with_drp: 10
- drp_category_added: 8
- drp_count_changed: 7
- drp_category_removed: 1

### Changed Categories
- current_employer: 105
- any_drp: 29
- drp_count: 7
- has_customer_complaint: 5
- has_judgment: 4

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261119T220859Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261119T220859Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
