# IAR DRP Change Summary: 20260602T181102Z

## Source
- Current source file: `IA_INDVL_Feed_06_02_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_02_2026.xml.zip
- Retrieved at: 2026-06-02T18:11:02+00:00
- XML generated date: 2026-06-02
- XML files parsed from ZIP: 20
- SHA-256: `1c0cfdc1576d01da42b5eb1b3f2a7201ae3f4c6f1839e32b059b67d3b8bf6ffc`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 433,958
- DRP occurrence rows parsed: 60,094
- Representatives with at least one DRP flag: 60,094

## Changes Since Previous Run
- Previous run: `20260601T192458Z`
- Total reported changes: 242
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 185
- representative_removed_from_feed: 28
- drp_count_changed: 11
- drp_category_added: 9
- new_representative_with_drp: 5
- drp_category_removed: 4

### Changed Categories
- current_employer: 185
- any_drp: 33
- drp_count: 11
- has_customer_complaint: 5
- has_judgment: 3
- has_reg_action: 2
- has_bankrupt: 2
- has_termination: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260602T181102Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260602T181102Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
