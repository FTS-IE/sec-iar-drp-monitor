# IAR DRP Change Summary: 20260817T144321Z

## Source
- Current source file: `IA_INDVL_Feed_08_17_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_08_17_2026.xml.zip
- Retrieved at: 2026-08-17T14:43:21+00:00
- XML generated date: 2026-08-17
- XML files parsed from ZIP: 20
- SHA-256: `f491764de7f2da65ec6213f49436af540b6b24db5be6195a98dd7732ef839fc8`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 437,726
- DRP occurrence rows parsed: 60,010
- Representatives with at least one DRP flag: 60,010

## Changes Since Previous Run
- Previous run: `20260814T150626Z`
- Total reported changes: 182
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

### Change Types
- current_employer_changed: 115
- representative_removed_from_feed: 19
- drp_category_removed: 14
- drp_count_changed: 14
- new_representative_with_drp: 11
- drp_category_added: 9

### Changed Categories
- current_employer: 115
- any_drp: 30
- drp_count: 14
- has_bankrupt: 12
- has_judgment: 9
- has_customer_complaint: 1
- has_reg_action: 1

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260817T144321Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260817T144321Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
