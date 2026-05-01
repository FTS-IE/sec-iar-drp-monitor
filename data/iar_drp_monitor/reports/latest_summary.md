# IAR DRP Change Summary: 20260501T155422Z

## Source
- Current source file: `IA_INDVL_Feed_05_01_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_01_2026.xml.zip
- Retrieved at: 2026-05-01T15:54:22+00:00
- XML generated date: 2026-05-01
- SHA-256: `91d34f21dfefd46e678cd24c8b765dc1ca6faf4a17c4464513667d4a63389240`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags only; non-DRP profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 21,636
- DRP occurrence rows parsed: 4,224
- Representatives with at least one DRP flag: 4,224

## Changes Since Previous Run
No prior successful run was found. This run is the baseline for future comparisons.
- Empty change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260501T155422Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260501T155422Z_drps.csv`
- DRP rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
