# IAR DRP Change Summary: 20260617T172305Z

## Source
- Current source file: `IA_INDVL_Feed_06_17_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_06_17_2026.xml.zip
- Retrieved at: 2026-06-17T17:23:05+00:00
- XML generated date: 2026-06-17
- XML files parsed from ZIP: 20
- SHA-256: `478838d34ce0a8b18c659b3761be22668ed9295715c5e4520ac7d9ce41e90a4e`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 434,807
- DRP occurrence rows parsed: 60,064
- Representatives with at least one DRP flag: 60,064

## Changes Since Previous Run
- Previous run: `20260616T183923Z`
- Total reported changes: 171
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 130
- representative_removed_from_feed: 14
- drp_count_changed: 8
- new_representative_with_drp: 8
- drp_category_removed: 6
- drp_category_added: 5

### Changed Categories
- current_employer: 130
- any_drp: 22
- drp_count: 8
- has_customer_complaint: 3
- has_judgment: 3
- has_criminal: 2
- has_bankrupt: 2
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260617T172305Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260617T172305Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
