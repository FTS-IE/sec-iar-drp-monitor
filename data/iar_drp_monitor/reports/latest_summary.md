# IAR DRP Change Summary: 20260512T163211Z

## Source
- Current source file: `IA_INDVL_Feed_05_12_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_12_2026.xml.zip
- Retrieved at: 2026-05-12T16:32:11+00:00
- XML generated date: 2026-05-12
- XML files parsed from ZIP: 20
- SHA-256: `83a021ff061b653a6b6e583ad863ff0869c8ef0a29e1e22217aed6fe9deec311`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,017
- DRP occurrence rows parsed: 60,080
- Representatives with at least one DRP flag: 60,080

## Changes Since Previous Run
- Previous run: `20260511T164642Z`
- Total reported changes: 180
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 131
- representative_removed_from_feed: 16
- drp_count_changed: 11
- drp_category_added: 9
- new_representative_with_drp: 8
- drp_category_removed: 5

### Changed Categories
- current_employer: 131
- any_drp: 24
- drp_count: 11
- has_judgment: 6
- has_customer_complaint: 5
- has_bankrupt: 3

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260512T163211Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260512T163211Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
