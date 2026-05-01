from __future__ import annotations

import hashlib
import json
import shutil
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

from .constants import DOWNLOAD_BASE_URL, MANIFEST_URL


USER_AGENT = "mooc-starter-kit-iar-drp-monitor/0.1"


@dataclass(frozen=True)
class FeedFile:
    name: str
    size: str
    date: str
    url: str


def _request(url: str) -> urllib.request.Request:
    return urllib.request.Request(url, headers={"User-Agent": USER_AGENT})


def fetch_manifest(manifest_url: str = MANIFEST_URL) -> dict:
    with urllib.request.urlopen(_request(manifest_url), timeout=120) as response:
        return json.loads(response.read().decode("utf-8"))


def load_manifest(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def select_individual_feed(
    manifest: dict, download_base_url: str = DOWNLOAD_BASE_URL
) -> FeedFile:
    files = manifest.get("files")
    if not isinstance(files, list):
        raise ValueError("Manifest did not contain a top-level 'files' list.")

    matches = [
        item
        for item in files
        if isinstance(item, dict)
        and str(item.get("name", "")).startswith("IA_INDVL_Feed_")
        and str(item.get("name", "")).endswith(".xml.zip")
    ]
    if not matches:
        raise ValueError("No IA_INDVL_Feed_*.xml.zip file found in manifest.")
    if len(matches) > 1:
        raise ValueError(
            "Manifest contained multiple IA_INDVL_Feed_*.xml.zip files; "
            "manual review is needed."
        )

    item = matches[0]
    name = str(item["name"])
    return FeedFile(
        name=name,
        size=str(item.get("size", "")),
        date=str(item.get("date", "")),
        url=f"{download_base_url.rstrip('/')}/{quote(name)}",
    )


def hash_file(path: Path) -> str:
    sha256 = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def download_feed(feed: FeedFile, raw_dir: Path, run_id: str | None = None) -> tuple[Path, str, bool]:
    raw_dir.mkdir(parents=True, exist_ok=True)
    destination_name = f"{run_id}_{feed.name}" if run_id else feed.name
    destination = raw_dir / destination_name
    reused_existing = destination.exists()

    if not reused_existing:
        with urllib.request.urlopen(_request(feed.url), timeout=300) as response:
            with destination.open("wb") as output:
                shutil.copyfileobj(response, output)

    return destination, hash_file(destination), reused_existing


def copy_local_feed(input_zip: Path, raw_dir: Path) -> tuple[Path, str]:
    raw_dir.mkdir(parents=True, exist_ok=True)
    destination = raw_dir / input_zip.name
    if input_zip.resolve() != destination.resolve():
        shutil.copy2(input_zip, destination)
    return destination, hash_file(destination)
