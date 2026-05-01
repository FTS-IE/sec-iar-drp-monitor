from __future__ import annotations

import json
from pathlib import Path


LATEST_STATE_NAME = "latest_successful_run.json"


def load_latest_state(state_dir: Path) -> dict | None:
    path = state_dir / LATEST_STATE_NAME
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_run_state(state_dir: Path, run_state: dict, update_latest: bool = True) -> Path:
    state_dir.mkdir(parents=True, exist_ok=True)
    run_path = state_dir / f"{run_state['run_id']}.json"
    with run_path.open("w", encoding="utf-8") as handle:
        json.dump(run_state, handle, indent=2, sort_keys=True)
        handle.write("\n")

    if update_latest:
        latest_path = state_dir / LATEST_STATE_NAME
        with latest_path.open("w", encoding="utf-8") as handle:
            json.dump(run_state, handle, indent=2, sort_keys=True)
            handle.write("\n")

    return run_path
