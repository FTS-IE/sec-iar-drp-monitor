# IAR DRP Change Summary: 20260506T181615Z

## Source
- Current source file: `IA_INDVL_Feed_05_06_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_06_2026.xml.zip
- Retrieved at: 2026-05-06T18:16:15+00:00
- XML generated date: 2026-05-06
- XML files parsed from ZIP: 20
- SHA-256: `ae65ca73efd7d6292167820f76785585dc99e27a432d074528467809319bb972`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 432,837
- DRP occurrence rows parsed: 60,096
- Representatives with at least one DRP flag: 60,096

## Changes Since Previous Run
- Previous run: `20260506T161034Z`
- Comparison skipped: the previous rollup CSV was not found at data/iar_drp_monitor/processed/latest_drp_rollup.csv.
This run is the baseline for future comparisons.
- Empty change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260506T181615Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260506T181615Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
