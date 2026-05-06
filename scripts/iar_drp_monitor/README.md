# IAR DRP Monitor

This pipeline downloads the SEC/IAPD Registered Investment Adviser Representative
bulk compilation feed, extracts Disclosure Reporting Page (DRP) flags and
current employer details, and
summarizes what changed since the previous successful local run.

## Run

```bash
python3 -m scripts.iar_drp_monitor run
```

Check the most recent successful run:

```bash
python3 -m scripts.iar_drp_monitor latest
```

Send the latest summary by email:

```bash
python3 -m scripts.iar_drp_monitor notify-email
```

Generated files are written under `data/iar_drp_monitor/`:

- `raw/` stores the source ZIP, manifest copy, and checksum metadata in state.
- `processed/` stores normalized representatives, DRP occurrences, and rollups.
- `reports/` stores the Markdown summary and change CSV.
- `state/` stores the latest successful run pointer for comparison.

## Offline Fixture Run

Use a local XML ZIP without hitting the network:

```bash
python3 -m scripts.iar_drp_monitor run --input-zip path/to/IA_INDVL_sample.xml.zip
```

## GitHub Actions Schedule

The workflow at `.github/workflows/iar-drp-monitor.yml` runs on weekdays at 14:17 UTC, which is 9:17 a.m. Eastern Standard Time or 10:17 a.m. Eastern Daylight Time. It can also be run manually from the GitHub Actions tab.

The workflow runs tests, downloads and processes the current SEC/IAPD IAR compilation feed, writes stable latest files needed for the next comparison, commits only lightweight latest outputs and a compressed rollup baseline back to the repo, uploads the latest report files as a 30-day artifact, emails the summary when monitored changes are detected, and emails a failure alert when the workflow fails.

Large raw source ZIPs and run-specific full outputs stay ignored by git.

## Email Setup

Add these repository secrets in GitHub under Settings -> Secrets and variables -> Actions:

- `IAR_DRP_SMTP_HOST`
- `IAR_DRP_SMTP_PORT`
- `IAR_DRP_SMTP_USERNAME`
- `IAR_DRP_SMTP_PASSWORD`
- `IAR_DRP_SMTP_FROM`
- `IAR_DRP_SMTP_TO`

`IAR_DRP_SMTP_PORT` defaults to `587` if omitted. `IAR_DRP_SMTP_TO` can contain one address or a comma-separated list. STARTTLS is used by default. Set `IAR_DRP_SMTP_SSL=true` if your SMTP provider requires SMTP over SSL instead.

For local testing without sending:

```bash
python3 -m scripts.iar_drp_monitor notify-email --dry-run
```

## Reporting Caution

The output tracks DRP disclosure flags and current employer values in the SEC/IAPD
compilation feed. A DRP flag is a source-data signal for reporting follow-up,
not an independent finding that misconduct occurred.
