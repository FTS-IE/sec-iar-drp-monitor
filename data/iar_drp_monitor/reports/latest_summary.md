# IAR DRP Change Summary: 20261104T205123Z

## Source
- Current source file: `IA_INDVL_Feed_11_04_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_04_2026.xml.zip
- Retrieved at: 2026-11-04T20:51:23+00:00
- XML generated date: 2026-11-04
- XML files parsed from ZIP: 19
- SHA-256: `1cc992d9d617cd9084f19debae4d543304b49f5ca6dfed4259aae139b820e07e`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 420,962
- DRP occurrence rows parsed: 59,260
- Representatives with at least one DRP flag: 59,260

## Changes Since Previous Run
- Previous run: `20261103T204057Z`
- Total reported changes: 162
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 99
- representative_removed_from_feed: 19
- new_representative_with_drp: 16
- drp_count_changed: 12
- drp_category_added: 12
- drp_category_removed: 4

### Changed Categories
- current_employer: 99
- any_drp: 35
- drp_count: 12
- has_customer_complaint: 6
- has_judgment: 6
- has_bankrupt: 3
- has_criminal: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261104T205123Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261104T205123Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
