# IAR DRP Change Summary: 20260828T233312Z

## Source
- Current source file: `IA_INDVL_Feed_08_28_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_28_2026.xml.zip
- Retrieved at: 2026-08-28T23:33:12+00:00
- XML generated date: 2026-08-28
- XML files parsed from ZIP: 20
- SHA-256: `f376ce5e5b9d07006b9799e84b5c6743a7f0c53636b67b78b009b52d0f28c232`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 438,695
- DRP occurrence rows parsed: 60,019
- Representatives with at least one DRP flag: 60,019

## Changes Since Previous Run
- Previous run: `20260827T235044Z`
- Total reported changes: 158
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 127
- new_representative_with_drp: 11
- representative_removed_from_feed: 6
- drp_count_changed: 6
- drp_category_added: 6
- drp_category_removed: 2

### Changed Categories
- current_employer: 127
- any_drp: 17
- drp_count: 6
- has_judgment: 3
- has_customer_complaint: 3
- has_criminal: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260828T233312Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260828T233312Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
