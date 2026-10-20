# IAR DRP Change Summary: 20261020T182733Z

## Source
- Current source file: `IA_INDVL_Feed_10_20_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_20_2026.xml.zip
- Retrieved at: 2026-10-20T18:27:33+00:00
- XML generated date: 2026-10-20
- XML files parsed from ZIP: 20
- SHA-256: `6d037f3d54cf2e9faba833339d5793bcbd50e7f6b8172b99979b0a1c8d102e9e`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 442,046
- DRP occurrence rows parsed: 60,024
- Representatives with at least one DRP flag: 60,024

## Changes Since Previous Run
- Previous run: `20261019T195513Z`
- Total reported changes: 194
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 129
- drp_count_changed: 22
- drp_category_added: 13
- drp_category_removed: 13
- representative_removed_from_feed: 11
- new_representative_with_drp: 6

### Changed Categories
- current_employer: 129
- drp_count: 22
- any_drp: 17
- has_customer_complaint: 10
- has_bankrupt: 8
- has_judgment: 7
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261020T182733Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261020T182733Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
