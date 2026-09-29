# IAR DRP Change Summary: 20260929T192527Z

## Source
- Current source file: `IA_INDVL_Feed_09_29_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_09_29_2026.xml.zip
- Retrieved at: 2026-09-29T19:25:27+00:00
- XML generated date: 2026-09-29
- XML files parsed from ZIP: 20
- SHA-256: `c42a384c43c8f5e2842ecf275d5bd05419415dd792f0978071900c74952799e5`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 440,685
- DRP occurrence rows parsed: 60,042
- Representatives with at least one DRP flag: 60,042

## Changes Since Previous Run
- Previous run: `20260928T203309Z`
- Total reported changes: 164
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 111
- new_representative_with_drp: 17
- representative_removed_from_feed: 14
- drp_count_changed: 10
- drp_category_added: 8
- drp_category_removed: 4

### Changed Categories
- current_employer: 111
- any_drp: 31
- drp_count: 10
- has_customer_complaint: 5
- has_judgment: 3
- has_bankrupt: 3
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260929T192527Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260929T192527Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
