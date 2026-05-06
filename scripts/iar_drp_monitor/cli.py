from __future__ import annotations

import argparse
import json
import shutil
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from .compare import CompareResult, compare_rollups, write_changes_csv
from .constants import (
    DEFAULT_DATA_DIR,
    DOWNLOAD_BASE_URL,
    MANIFEST_URL,
    ROLLUP_PARSER_VERSION,
)
from .downloader import (
    FeedFile,
    copy_local_feed,
    download_feed,
    fetch_manifest,
    load_manifest,
    select_individual_feed,
)
from .emailer import EmailSettings, send_email
from .parser import ParseOutputs, SourceContext, parse_feed_to_csv
from .reporting import write_markdown_report
from .state import load_latest_state, write_run_state


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "run":
        run(args)
        return 0
    if args.command == "latest":
        return 0 if latest(args) else 1
    if args.command == "notify-email":
        notify_email(args)
        return 0
    parser.print_help()
    return 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m scripts.iar_drp_monitor",
        description=(
            "Download and compare SEC/IAPD IAR DRP disclosure flags and "
            "current employer details."
        ),
    )
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Run the DRP monitor pipeline.")
    run_parser.add_argument(
        "--data-dir",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help="Directory for raw, processed, report, and state outputs.",
    )
    run_parser.add_argument(
        "--manifest-url",
        default=MANIFEST_URL,
        help="SEC/IAPD compilation manifest URL.",
    )
    run_parser.add_argument(
        "--download-base-url",
        default=DOWNLOAD_BASE_URL,
        help="Base URL for compilation report downloads.",
    )
    run_parser.add_argument(
        "--manifest-file",
        type=Path,
        help="Use a local manifest JSON file instead of fetching the live manifest.",
    )
    run_parser.add_argument(
        "--input-zip",
        type=Path,
        help="Use a local IA_INDVL XML ZIP instead of downloading the live file.",
    )
    run_parser.add_argument(
        "--run-id",
        help="Override the generated run ID. Useful for tests or reproducible reruns.",
    )
    run_parser.add_argument(
        "--no-update-state",
        action="store_true",
        help="Write outputs but do not replace the latest successful run pointer.",
    )
    run_parser.add_argument(
        "--stable-latest",
        action="store_true",
        help=(
            "Copy the current rollup, summary, and changes to stable latest_* "
            "paths for GitHub Actions persistence."
        ),
    )

    latest_parser = subparsers.add_parser(
        "latest", help="Show the latest successful local run."
    )
    latest_parser.add_argument(
        "--data-dir",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help="Directory containing monitor state outputs.",
    )

    notify_parser = subparsers.add_parser(
        "notify-email", help="Email the latest run summary or a workflow failure alert."
    )
    notify_parser.add_argument(
        "--data-dir",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help="Directory containing monitor state and report outputs.",
    )
    notify_parser.add_argument(
        "--only-if-changes",
        action="store_true",
        help="Skip the email when the latest successful run has zero reported changes.",
    )
    notify_parser.add_argument(
        "--failure",
        action="store_true",
        help="Send a workflow failure alert instead of the latest run digest.",
    )
    notify_parser.add_argument(
        "--failure-message",
        default="The IAR DRP monitor workflow failed.",
        help="Failure message to include when --failure is used.",
    )
    notify_parser.add_argument(
        "--subject-prefix",
        default="IAR DRP Monitor",
        help="Prefix for notification email subjects.",
    )
    notify_parser.add_argument("--smtp-host", help="SMTP host. Defaults to IAR_DRP_SMTP_HOST.")
    notify_parser.add_argument("--smtp-port", help="SMTP port. Defaults to IAR_DRP_SMTP_PORT or 587.")
    notify_parser.add_argument("--smtp-user", help="SMTP username. Defaults to IAR_DRP_SMTP_USERNAME.")
    notify_parser.add_argument("--smtp-password", help="SMTP password. Defaults to IAR_DRP_SMTP_PASSWORD.")
    notify_parser.add_argument("--smtp-from", help="Sender address. Defaults to IAR_DRP_SMTP_FROM.")
    notify_parser.add_argument("--smtp-to", help="Recipient address list. Defaults to IAR_DRP_SMTP_TO.")
    notify_parser.add_argument(
        "--no-starttls",
        action="store_true",
        help="Do not use STARTTLS. IAR_DRP_SMTP_SSL=true uses SMTP_SSL instead.",
    )
    notify_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the email envelope and subject without sending.",
    )
    return parser


def notify_email(args: argparse.Namespace) -> bool:
    settings = EmailSettings.from_args_env(args, require_server=not args.dry_run)

    if args.failure:
        subject = f"{args.subject_prefix}: workflow failure"
        body = _failure_email_body(args.failure_message)
        send_email(settings, subject, body, dry_run=args.dry_run)
        return True

    state = load_latest_state(args.data_dir / "state")
    if not state:
        print(f"No latest successful run found under {args.data_dir / 'state'}.")
        return False

    change_count = int(state.get("change_count") or 0)
    if args.only_if_changes and change_count == 0:
        print("No reportable changes detected; skipping email.")
        return False

    summary_path = Path(state.get("summary_md", ""))
    changes_path = Path(state.get("changes_csv", ""))
    summary_text = summary_path.read_text(encoding="utf-8") if summary_path.exists() else ""
    subject = f"{args.subject_prefix}: {change_count} change(s) in {state.get('run_id', '')}"
    body = _latest_email_body(state, summary_text)
    attachments = [changes_path] if changes_path.exists() else []
    send_email(settings, subject, body, attachments=attachments, dry_run=args.dry_run)
    return True


def latest(args: argparse.Namespace) -> dict | None:
    state = load_latest_state(args.data_dir / "state")
    if not state:
        print(f"No latest successful run found under {args.data_dir / 'state'}.")
        return None

    print(f"Latest successful run: {state.get('run_id', '')}")
    print(f"Source file: {state.get('source_file', '')}")
    print(f"Retrieved at: {state.get('retrieved_at', '')}")
    print(f"Representatives parsed: {state.get('representative_count', '')}")
    print(f"DRP occurrence rows: {state.get('drp_record_count', '')}")
    print(f"Representatives with DRPs: {state.get('representatives_with_drp', '')}")
    print(f"Reported changes: {state.get('change_count', '')}")
    print(f"Summary: {state.get('summary_md', '')}")
    print(f"Change CSV: {state.get('changes_csv', '')}")
    return state


def run(args: argparse.Namespace) -> dict:
    run_id = args.run_id or _default_run_id()
    retrieved_at = _utc_now()
    paths = _prepare_paths(args.data_dir, run_id)

    manifest = None
    feed: FeedFile
    reused_existing = False
    if args.input_zip:
        source_zip = args.input_zip.resolve()
        if not source_zip.exists():
            raise FileNotFoundError(source_zip)
        raw_zip, source_sha256 = copy_local_feed(source_zip, paths["raw"])
        feed = _feed_from_local_zip(source_zip)
        if args.manifest_file:
            manifest = load_manifest(args.manifest_file)
    else:
        manifest = load_manifest(args.manifest_file) if args.manifest_file else fetch_manifest(args.manifest_url)
        feed = select_individual_feed(manifest, args.download_base_url)
        raw_zip, source_sha256, reused_existing = download_feed(feed, paths["raw"], run_id)

    if manifest is not None:
        manifest_path = paths["raw"] / f"{run_id}_manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    outputs = ParseOutputs(
        representatives_csv=paths["processed"] / f"{run_id}_representatives.csv",
        drps_csv=paths["processed"] / f"{run_id}_drps.csv",
        rollup_csv=paths["processed"] / f"{run_id}_drp_rollup.csv",
    )
    source = SourceContext(
        run_id=run_id,
        source_file=feed.name,
        source_url=feed.url,
        retrieved_at=retrieved_at,
    )
    parse_stats = parse_feed_to_csv(raw_zip, source, outputs)

    previous_state = load_latest_state(paths["state"])
    previous_rollup_path = (
        Path(previous_state["rollup_csv"]) if previous_state and previous_state.get("rollup_csv") else None
    )
    previous_run_id = previous_state.get("run_id", "") if previous_state else ""
    comparison_skipped_reason = ""
    if previous_state and _previous_state_is_comparable(previous_state, previous_rollup_path):
        compare_result = compare_rollups(
            outputs.rollup_csv,
            previous_rollup_path,
            run_id=run_id,
            previous_run_id=previous_run_id,
        )
    elif previous_state:
        comparison_skipped_reason = _comparison_skipped_reason(
            previous_state, previous_rollup_path
        )
        compare_result = CompareResult([], Counter(), Counter())
    else:
        compare_result = CompareResult([], Counter(), Counter())

    run_changes_csv = paths["reports"] / f"{run_id}_drp_changes.csv"
    run_summary_md = paths["reports"] / f"{run_id}_summary.md"
    write_changes_csv(run_changes_csv, compare_result.changes)

    run_state = {
        "run_id": run_id,
        "source_file": feed.name,
        "source_url": feed.url,
        "source_size": feed.size,
        "source_date": feed.date,
        "source_sha256": source_sha256,
        "source_generated_date": parse_stats.source_generated_date,
        "source_xml_member_count": parse_stats.source_xml_member_count,
        "rollup_parser_version": ROLLUP_PARSER_VERSION,
        "retrieved_at": retrieved_at,
        "processed_at": _utc_now(),
        "raw_zip": str(raw_zip),
        "representatives_csv": str(outputs.representatives_csv),
        "drps_csv": str(outputs.drps_csv),
        "rollup_csv": str(outputs.rollup_csv),
        "changes_csv": str(run_changes_csv),
        "summary_md": str(run_summary_md),
        "representative_count": parse_stats.representative_count,
        "drp_record_count": parse_stats.drp_record_count,
        "representatives_with_drp": parse_stats.representatives_with_drp,
        "change_count": len(compare_result.changes),
        "reused_existing_raw_file": reused_existing,
    }
    if comparison_skipped_reason:
        run_state["comparison_skipped_reason"] = comparison_skipped_reason

    summary_md = run_summary_md
    changes_csv = run_changes_csv
    if args.stable_latest:
        latest_rollup = paths["processed"] / "latest_drp_rollup.csv"
        latest_changes = paths["reports"] / "latest_drp_changes.csv"
        latest_summary = paths["reports"] / "latest_summary.md"
        shutil.copy2(outputs.rollup_csv, latest_rollup)
        shutil.copy2(run_changes_csv, latest_changes)
        run_state["rollup_csv"] = str(latest_rollup)
        run_state["changes_csv"] = str(latest_changes)
        run_state["summary_md"] = str(latest_summary)
        summary_md = latest_summary
        changes_csv = latest_changes

    write_markdown_report(
        summary_md,
        run_state,
        previous_state,
        parse_stats,
        compare_result,
        changes_csv,
    )
    state_path = write_run_state(
        paths["state"], run_state, update_latest=not args.no_update_state
    )

    print(f"Run ID: {run_id}")
    print(f"Source file: {feed.name}")
    print(f"Representatives parsed: {parse_stats.representative_count}")
    print(f"Reported changes: {len(compare_result.changes)}")
    print(f"Summary: {summary_md}")
    print(f"State: {state_path}")
    return run_state


def _latest_email_body(state: dict, summary_text: str) -> str:
    lines = [
        f"Run ID: {state.get('run_id', '')}",
        f"Source file: {state.get('source_file', '')}",
        f"Retrieved at: {state.get('retrieved_at', '')}",
        f"Reported changes: {state.get('change_count', '')}",
        f"Summary path: {state.get('summary_md', '')}",
        f"Change CSV path: {state.get('changes_csv', '')}",
        "",
        summary_text or "No summary text was available.",
    ]
    return "\n".join(lines)


def _failure_email_body(message: str) -> str:
    return "\n".join(
        [
            message,
            "",
            "Check the GitHub Actions run logs for details.",
        ]
    )


def _previous_state_is_comparable(
    previous_state: dict, previous_rollup_path: Path | None
) -> bool:
    return (
        previous_rollup_path is not None
        and previous_rollup_path.exists()
        and previous_state.get("rollup_parser_version") == ROLLUP_PARSER_VERSION
    )


def _comparison_skipped_reason(
    previous_state: dict, previous_rollup_path: Path | None
) -> str:
    if previous_rollup_path is None:
        return "the previous run state did not record a rollup CSV path"
    if not previous_rollup_path.exists():
        return f"the previous rollup CSV was not found at {previous_rollup_path}"
    previous_version = previous_state.get("rollup_parser_version")
    if previous_version is None:
        return (
            "the previous rollup was generated before full multi-file ZIP parsing "
            "was tracked"
        )
    return (
        f"the previous rollup parser version was {previous_version}, "
        f"but the current parser version is {ROLLUP_PARSER_VERSION}"
    )


def _prepare_paths(data_dir: Path, run_id: str) -> dict[str, Path]:
    paths = {
        "raw": data_dir / "raw",
        "processed": data_dir / "processed",
        "reports": data_dir / "reports",
        "state": data_dir / "state",
    }
    for path in paths.values():
        path.mkdir(parents=True, exist_ok=True)
    return paths


def _feed_from_local_zip(path: Path) -> FeedFile:
    return FeedFile(
        name=path.name,
        size=str(path.stat().st_size),
        date="",
        url=f"local:{path}",
    )


def _default_run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
