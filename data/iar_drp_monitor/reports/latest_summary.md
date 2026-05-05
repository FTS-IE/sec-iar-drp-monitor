# IAR DRP Change Summary: 20260505T154955Z

## Source
- Current source file: `IA_INDVL_Feed_05_05_2026.xml.zip`
- Source URL: https://reports.adviserinfo.sec.gov/reports/CompilationReports/IA_INDVL_Feed_05_05_2026.xml.zip
- Retrieved at: 2026-05-05T15:49:55+00:00
- XML generated date: 2026-05-05
- SHA-256: `aeb8cbb5e78b235cad625413d6a9d88923843a3733f5221fdb695e8cc9734154`

## Scope And Method
- Scope: Registered Investment Adviser Representative compilation feed only.
- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.
- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.
- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.

## Current Run Counts
- Representatives parsed: 21,641
- DRP occurrence rows parsed: 4,230
- Representatives with at least one DRP flag: 4,230

## Changes Since Previous Run
- Previous run: `20260505T154836Z`
- Total reported changes: 0
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`

No monitored changes were detected.

## Output Files
- Representatives CSV: `data/iar_drp_monitor/processed/20260505T154955Z_representatives.csv`
- DRP occurrence CSV: `data/iar_drp_monitor/processed/20260505T154955Z_drps.csv`
- Rollup CSV: `data/iar_drp_monitor/processed/latest_drp_rollup.csv`
- Change CSV: `data/iar_drp_monitor/reports/latest_drp_changes.csv`
