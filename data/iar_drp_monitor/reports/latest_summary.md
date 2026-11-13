# IAR DRP Change Summary: 20261113T205354Z

## Source
- Current source file: `IA_INDVL_Feed_11_13_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_11_13_2026.xml.zip
- Retrieved at: 2026-11-13T20:53:54+00:00
- XML generated date: 2026-11-13
- XML files parsed from ZIP: 20
- SHA-256: `67a11a440af414d86154e5a80437a58d067736afee98cffdb92a6431bfa9b233`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 443,777
- DRP occurrence rows parsed: 60,109
- Representatives with at least one DRP flag: 60,109

## Changes Since Previous Run
- Previous run: `20261112T212807Z`
- Total reported changes: 2,797
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 2,749
- new_representative_with_drp: 16
- representative_removed_from_feed: 15
- drp_count_changed: 8
- drp_category_added: 7
- drp_category_removed: 2

### Changed Categories
- current_employer: 2,749
- any_drp: 31
- drp_count: 8
- has_judgment: 2
- has_customer_complaint: 2
- has_bankrupt: 2
- has_criminal: 2
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261113T205354Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261113T205354Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
