from __future__ import annotations

import csv
import zipfile
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET

from .constants import (
    DRP_FIELDS,
    DRP_FLAG_FIELDS,
    DRP_FLAG_MAP,
    DRP_ROLLUP_FIELDS,
    CURRENT_EMPLOYER_FIELDS,
    REPRESENTATIVE_FIELDS,
)


@dataclass(frozen=True)
class SourceContext:
    run_id: str
    source_file: str
    source_url: str
    retrieved_at: str


@dataclass(frozen=True)
class ParseOutputs:
    representatives_csv: Path
    drps_csv: Path
    rollup_csv: Path


@dataclass(frozen=True)
class ParseStats:
    source_generated_date: str
    source_xml_member_count: int
    representative_count: int
    drp_record_count: int
    representatives_with_drp: int


def parse_feed_to_csv(zip_path: Path, source: SourceContext, outputs: ParseOutputs) -> ParseStats:
    outputs.representatives_csv.parent.mkdir(parents=True, exist_ok=True)
    outputs.drps_csv.parent.mkdir(parents=True, exist_ok=True)
    outputs.rollup_csv.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path) as archive:
        member_names = _find_xml_members(archive)
        with (
            outputs.representatives_csv.open("w", encoding="utf-8", newline="") as reps_handle,
            outputs.drps_csv.open("w", encoding="utf-8", newline="") as drps_handle,
            outputs.rollup_csv.open("w", encoding="utf-8", newline="") as rollup_handle,
        ):
            reps_writer = csv.DictWriter(reps_handle, fieldnames=REPRESENTATIVE_FIELDS)
            drps_writer = csv.DictWriter(drps_handle, fieldnames=DRP_FIELDS)
            rollup_writer = csv.DictWriter(rollup_handle, fieldnames=DRP_ROLLUP_FIELDS)
            reps_writer.writeheader()
            drps_writer.writeheader()
            rollup_writer.writeheader()

            source_generated_date = ""
            representative_count = 0
            drp_record_count = 0
            representatives_with_drp = 0
            for member_name in member_names:
                with archive.open(member_name) as xml_file:
                    stats = _parse_xml_stream(
                        xml_file,
                        source,
                        reps_writer,
                        drps_writer,
                        rollup_writer,
                    )
                source_generated_date = source_generated_date or stats.source_generated_date
                representative_count += stats.representative_count
                drp_record_count += stats.drp_record_count
                representatives_with_drp += stats.representatives_with_drp

    return ParseStats(
        source_generated_date=source_generated_date,
        source_xml_member_count=len(member_names),
        representative_count=representative_count,
        drp_record_count=drp_record_count,
        representatives_with_drp=representatives_with_drp,
    )


def _find_xml_members(archive: zipfile.ZipFile) -> list[str]:
    xml_members = [
        name
        for name in archive.namelist()
        if name.lower().endswith(".xml") and not name.endswith("/")
    ]
    if not xml_members:
        raise ValueError("The ZIP archive does not contain an XML file.")
    return sorted(xml_members)


def _parse_xml_stream(
    xml_file,
    source: SourceContext,
    reps_writer: csv.DictWriter,
    drps_writer: csv.DictWriter,
    rollup_writer: csv.DictWriter,
) -> ParseStats:
    source_generated_date = ""
    representative_count = 0
    drp_record_count = 0
    representatives_with_drp = 0

    context = ET.iterparse(xml_file, events=("start", "end"))
    for event, element in context:
        tag = _local_name(element.tag)
        if event == "start" and tag == "IAPDIndividualReport":
            source_generated_date = element.attrib.get("GenOn", "")
        elif event == "end" and tag == "Indvl":
            rep_row, drp_rows, rollup_row = _extract_individual(
                element, source, source_generated_date
            )
            reps_writer.writerow(rep_row)
            for drp_row in drp_rows:
                drps_writer.writerow(drp_row)
            rollup_writer.writerow(rollup_row)

            representative_count += 1
            drp_record_count += len(drp_rows)
            if rollup_row["has_any_drp"] == "Y":
                representatives_with_drp += 1
            element.clear()

    return ParseStats(
        source_generated_date=source_generated_date,
        source_xml_member_count=1,
        representative_count=representative_count,
        drp_record_count=drp_record_count,
        representatives_with_drp=representatives_with_drp,
    )


def _extract_individual(element: ET.Element, source: SourceContext, generated_date: str):
    info = _find_child(element, "Info")
    info_attrs = info.attrib if info is not None else {}
    indvl_pk = _clean(info_attrs.get("indvlPK", ""))

    base = {
        "run_id": source.run_id,
        "source_file": source.source_file,
        "source_url": source.source_url,
        "source_generated_date": generated_date,
        "retrieved_at": source.retrieved_at,
        "indvl_pk": indvl_pk,
        "first_name": _clean(info_attrs.get("firstNm", "")),
        "middle_name": _clean(info_attrs.get("midNm", "")),
        "last_name": _clean(info_attrs.get("lastNm", "")),
        "suffix": _clean(info_attrs.get("sufNm", "")),
        "active_ag_registration": _normalize_yn(info_attrs.get("actvAGReg", "")),
        "profile_link": _clean(info_attrs.get("link", "")),
        **_current_employer_fields(element),
    }

    drp_rows = []
    rollup_flags = {field: "N" for field in DRP_FLAG_FIELDS}
    drps = _find_child(element, "DRPs")
    if drps is not None:
        for index, drp in enumerate(_iter_children(drps, "DRP"), start=1):
            drp_row = {
                "run_id": source.run_id,
                "source_file": source.source_file,
                "source_url": source.source_url,
                "source_generated_date": generated_date,
                "retrieved_at": source.retrieved_at,
                "indvl_pk": indvl_pk,
                "drp_index": str(index),
            }
            for xml_attr, output_field in DRP_FLAG_MAP.items():
                value = _normalize_yn(drp.attrib.get(xml_attr, ""))
                drp_row[output_field] = value
                if value == "Y":
                    rollup_flags[output_field] = "Y"
            drp_rows.append(drp_row)

    has_any_drp = "Y" if any(value == "Y" for value in rollup_flags.values()) else "N"
    rollup_row = {
        **base,
        "drp_count": str(len(drp_rows)),
        "has_any_drp": has_any_drp,
        **rollup_flags,
    }
    return base, drp_rows, rollup_row


def _current_employer_fields(element: ET.Element) -> dict[str, str]:
    employers = _current_employers(element)
    org_pks = [employer["org_pk"] for employer in employers if employer["org_pk"]]
    org_names = [employer["org_name"] for employer in employers if employer["org_name"]]
    values = {
        "current_employer_count": str(len(employers)),
        "current_employer_org_pks": " | ".join(org_pks),
        "current_employer_names": " | ".join(org_names),
        "current_employers": " | ".join(_format_employer(employer) for employer in employers),
    }
    return {field: values.get(field, "") for field in CURRENT_EMPLOYER_FIELDS}


def _current_employers(element: ET.Element) -> list[dict[str, str]]:
    current_employers = _find_child(element, "CrntEmps")
    if current_employers is None:
        return []

    employers = []
    seen = set()
    for employer in _iter_children(current_employers, "CrntEmp"):
        org_pk = _clean(employer.attrib.get("orgPK", ""))
        org_name = _clean(employer.attrib.get("orgNm", ""))
        if not org_pk and not org_name:
            continue
        key = (org_pk, org_name)
        if key in seen:
            continue
        seen.add(key)
        employers.append({"org_pk": org_pk, "org_name": org_name})

    return sorted(employers, key=_employer_sort_key)


def _format_employer(employer: dict[str, str]) -> str:
    org_pk = employer["org_pk"]
    org_name = employer["org_name"]
    if org_pk and org_name:
        return f"{org_pk}: {org_name}"
    return org_name or org_pk


def _employer_sort_key(employer: dict[str, str]) -> tuple[str, str]:
    org_pk = employer["org_pk"]
    org_pk_key = org_pk.zfill(20) if org_pk.isdigit() else org_pk.casefold()
    return org_pk_key, employer["org_name"].casefold()


def _find_child(element: ET.Element, name: str) -> ET.Element | None:
    for child in element:
        if _local_name(child.tag) == name:
            return child
    return None


def _iter_children(element: ET.Element, name: str):
    for child in element:
        if _local_name(child.tag) == name:
            yield child


def _local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def _clean(value: object) -> str:
    return str(value or "").strip()


def _normalize_yn(value: object) -> str:
    cleaned = _clean(value).upper()
    if cleaned in {"Y", "YES", "TRUE", "1"}:
        return "Y"
    if cleaned in {"N", "NO", "FALSE", "0"}:
        return "N"
    return ""
