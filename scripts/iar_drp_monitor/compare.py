from __future__ import annotations

import csv
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from .constants import CHANGE_FIELDS, DRP_FLAG_FIELDS


@dataclass(frozen=True)
class CompareResult:
    changes: list[dict]
    counts_by_type: Counter
    counts_by_category: Counter


def compare_rollups(
    current_rollup_csv: Path,
    previous_rollup_csv: Path | None,
    run_id: str,
    previous_run_id: str = "",
) -> CompareResult:
    current = _read_rollup(current_rollup_csv)
    previous = _read_rollup(previous_rollup_csv) if previous_rollup_csv else {}

    changes: list[dict] = []
    for indvl_pk in sorted(set(current) | set(previous)):
        current_row = current.get(indvl_pk)
        previous_row = previous.get(indvl_pk)

        if previous_row is None and current_row is not None:
            if current_row.get("has_any_drp") == "Y":
                changes.append(
                    _change(
                        run_id,
                        previous_run_id,
                        "new_representative_with_drp",
                        current_row,
                        None,
                        "any_drp",
                        "",
                        "Y",
                    )
                )
            continue

        if current_row is None and previous_row is not None:
            if previous_row.get("has_any_drp") == "Y":
                changes.append(
                    _change(
                        run_id,
                        previous_run_id,
                        "representative_removed_from_feed",
                        None,
                        previous_row,
                        "any_drp",
                        "Y",
                        "",
                    )
                )
            continue

        if current_row is None or previous_row is None:
            continue

        if current_row.get("drp_count", "0") != previous_row.get("drp_count", "0"):
            changes.append(
                _change(
                    run_id,
                    previous_run_id,
                    "drp_count_changed",
                    current_row,
                    previous_row,
                    "drp_count",
                    previous_row.get("drp_count", ""),
                    current_row.get("drp_count", ""),
                )
            )

        for field in DRP_FLAG_FIELDS:
            previous_value = previous_row.get(field, "")
            current_value = current_row.get(field, "")
            if previous_value == current_value:
                continue
            if previous_value != "Y" and current_value == "Y":
                change_type = "drp_category_added"
            elif previous_value == "Y" and current_value != "Y":
                change_type = "drp_category_removed"
            else:
                change_type = "drp_category_changed"
            changes.append(
                _change(
                    run_id,
                    previous_run_id,
                    change_type,
                    current_row,
                    previous_row,
                    field,
                    previous_value,
                    current_value,
                )
            )

    return CompareResult(
        changes=changes,
        counts_by_type=Counter(change["change_type"] for change in changes),
        counts_by_category=Counter(change["category"] for change in changes),
    )


def write_changes_csv(path: Path, changes: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CHANGE_FIELDS)
        writer.writeheader()
        writer.writerows(changes)


def _read_rollup(path: Path | None) -> dict[str, dict]:
    if path is None or not path.exists():
        return {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        return {
            row["indvl_pk"]: row
            for row in csv.DictReader(handle)
            if row.get("indvl_pk")
        }


def _change(
    run_id: str,
    previous_run_id: str,
    change_type: str,
    current_row: dict | None,
    previous_row: dict | None,
    category: str,
    previous_value: str,
    current_value: str,
) -> dict:
    display_row = current_row or previous_row or {}
    current_row = current_row or {}
    previous_row = previous_row or {}
    return {
        "run_id": run_id,
        "previous_run_id": previous_run_id,
        "change_type": change_type,
        "indvl_pk": display_row.get("indvl_pk", ""),
        "first_name": display_row.get("first_name", ""),
        "middle_name": display_row.get("middle_name", ""),
        "last_name": display_row.get("last_name", ""),
        "suffix": display_row.get("suffix", ""),
        "profile_link": display_row.get("profile_link", ""),
        "category": category,
        "previous_value": previous_value,
        "current_value": current_value,
        "previous_drp_count": previous_row.get("drp_count", ""),
        "current_drp_count": current_row.get("drp_count", ""),
        "previous_source_file": previous_row.get("source_file", ""),
        "current_source_file": current_row.get("source_file", ""),
    }
