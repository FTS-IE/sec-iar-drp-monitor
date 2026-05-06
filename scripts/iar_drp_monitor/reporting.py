from __future__ import annotations

from pathlib import Path

from .compare import CompareResult
from .parser import ParseStats


def write_markdown_report(
    path: Path,
    run_state: dict,
    previous_state: dict | None,
    parse_stats: ParseStats,
    compare_result: CompareResult,
    changes_csv: Path,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    previous_run_id = previous_state.get("run_id", "") if previous_state else ""

    lines = [
        f"# IAR DRP Change Summary: {run_state['run_id']}",
        "",
        "## Source",
        f"- Current source file: `{run_state['source_file']}`",
        f"- Source URL: {run_state['source_url']}",
        f"- Retrieved at: {run_state['retrieved_at']}",
        f"- XML generated date: {parse_stats.source_generated_date or 'Not provided'}",
        f"- XML files parsed from ZIP: {parse_stats.source_xml_member_count:,}",
        f"- SHA-256: `{run_state['source_sha256']}`",
        "",
        "## Scope And Method",
        "- Scope: Registered Investment Adviser Representative compilation feed only.",
        "- Change detection: DRP rollup flags and current employer lists; other profile changes are not reported.",
        "- Method: stream-parse the SEC/IAPD XML feed, normalize each representative's DRP category flags and current employers, compare the current rollup with the previous successful local run.",
        "- Reporting caution: a DRP flag is a disclosure signal in the source feed, not an independent finding that misconduct occurred.",
        "",
        "## Current Run Counts",
        f"- Representatives parsed: {parse_stats.representative_count:,}",
        f"- DRP occurrence rows parsed: {parse_stats.drp_record_count:,}",
        f"- Representatives with at least one DRP flag: {parse_stats.representatives_with_drp:,}",
        "",
    ]

    comparison_skipped_reason = run_state.get("comparison_skipped_reason", "")
    if not previous_state:
        lines.extend(
            [
                "## Changes Since Previous Run",
                "No prior successful run was found. This run is the baseline for future comparisons.",
                f"- Empty change CSV: `{changes_csv}`",
                "",
            ]
        )
    elif comparison_skipped_reason:
        lines.extend(
            [
                "## Changes Since Previous Run",
                f"- Previous run: `{previous_run_id}`",
                f"- Comparison skipped: {comparison_skipped_reason}.",
                "This run is the baseline for future comparisons.",
                f"- Empty change CSV: `{changes_csv}`",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "## Changes Since Previous Run",
                f"- Previous run: `{previous_run_id}`",
                f"- Total reported changes: {len(compare_result.changes):,}",
                f"- Change CSV: `{changes_csv}`",
                "",
            ]
        )
        if compare_result.changes:
            lines.append("### Change Types")
            for change_type, count in compare_result.counts_by_type.most_common():
                lines.append(f"- {change_type}: {count:,}")
            lines.append("")
            lines.append("### Changed Categories")
            for category, count in compare_result.counts_by_category.most_common():
                lines.append(f"- {category}: {count:,}")
            lines.append("")
        else:
            lines.extend(["No monitored changes were detected.", ""])

    lines.extend(
        [
            "## Output Files",
            f"- Representatives CSV: `{run_state['representatives_csv']}`",
            f"- DRP occurrence CSV: `{run_state['drps_csv']}`",
            f"- Rollup CSV: `{run_state['rollup_csv']}`",
            f"- Change CSV: `{changes_csv}`",
            "",
        ]
    )

    path.write_text("\n".join(lines), encoding="utf-8")
