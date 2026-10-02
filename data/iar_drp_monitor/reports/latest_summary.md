# IAR DRP Change Summary: 20261002T191825Z

## Source
- Current source file: `IA_INDVL_Feed_10_02_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_10_02_2026.xml.zip
- Retrieved at: 2026-10-02T19:18:25+00:00
- XML generated date: 2026-10-02
- XML files parsed from ZIP: 20
- SHA-256: `8b27c1ca7c90d3e9f595380cff99730d363d47c66de5d9c8bd4e47028acfd3bd`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 440,914
- DRP occurrence rows parsed: 60,043
- Representatives with at least one DRP flag: 60,043

## Changes Since Previous Run
- Previous run: `20261001T193121Z`
- Total reported changes: 964
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- new_representative_with_drp: 666
- current_employer_changed: 234
- representative_removed_from_feed: 35
- drp_category_added: 14
- drp_count_changed: 14
- drp_category_removed: 1

### Changed Categories
- any_drp: 701
- current_employer: 234
- drp_count: 14
- has_customer_complaint: 6
- has_judgment: 5
- has_reg_action: 2
- has_bankrupt: 2

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20261002T191825Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20261002T191825Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
