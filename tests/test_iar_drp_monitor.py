import csv
import gzip
import json
import shutil
import tempfile
import unittest
import zipfile
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from scripts.iar_drp_monitor.cli import build_parser, latest, notify_email, run
from scripts.iar_drp_monitor.compare import compare_rollups
from scripts.iar_drp_monitor.downloader import select_individual_feed
from scripts.iar_drp_monitor.emailer import EmailSettings
from scripts.iar_drp_monitor.parser import ParseOutputs, SourceContext, parse_feed_to_csv


FIXTURE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<IAPDIndividualReport GenOn="2026-04-30">
  <Indvls>
    <Indvl>
      <Info lastNm="Smith" firstNm="Alex" midNm="Q" sufNm="" indvlPK="1001" actvAGReg="Y" link="https://adviserinfo.sec.gov/IAPD/Individual/1001"/>
      <DRPs>
        <DRP hasRegAction="Y" hasCriminal="N" hasBankrupt="N" hasCivilJudc="N" hasBond="N" hasJudgment="N" hasInvstgn="N" hasCustComp="N" hasTermination="N"/>
        <DRP hasRegAction="N" hasCriminal="Y" hasBankrupt="N" hasCivilJudc="N" hasBond="N" hasJudgment="N" hasInvstgn="N" hasCustComp="N" hasTermination="N"/>
      </DRPs>
    </Indvl>
    <Indvl>
      <Info lastNm="Jones" firstNm="Bailey" indvlPK="1002" actvAGReg="Y" link="https://adviserinfo.sec.gov/IAPD/Individual/1002"/>
    </Indvl>
  </Indvls>
</IAPDIndividualReport>
"""


class IarDrpMonitorTests(unittest.TestCase):
    def test_select_individual_feed_from_manifest(self):
        manifest = {
            "files": [
                {"name": "IA_FIRM_SEC_Feed_04_30_2026.xml.gz", "size": "77 MB", "date": "04/30/2026"},
                {"name": "IA_INDVL_Feed_04_30_2026.xml.zip", "size": "166 MB", "date": "04/30/2026"},
            ]
        }

        feed = select_individual_feed(manifest, "https://example.test/reports")

        self.assertEqual(feed.name, "IA_INDVL_Feed_04_30_2026.xml.zip")
        self.assertEqual(feed.url, "https://example.test/reports/IA_INDVL_Feed_04_30_2026.xml.zip")

    def test_parse_feed_to_csv_rolls_up_drp_flags(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            zip_path = _write_fixture_zip(root / "sample.xml.zip", FIXTURE_XML)
            outputs = ParseOutputs(
                representatives_csv=root / "representatives.csv",
                drps_csv=root / "drps.csv",
                rollup_csv=root / "rollup.csv",
            )
            stats = parse_feed_to_csv(
                zip_path,
                SourceContext(
                    run_id="run-current",
                    source_file="sample.xml.zip",
                    source_url="local:sample.xml.zip",
                    retrieved_at="2026-04-30T00:00:00+00:00",
                ),
                outputs,
            )

            rollup = _read_csv_by_key(outputs.rollup_csv, "indvl_pk")

            self.assertEqual(stats.source_generated_date, "2026-04-30")
            self.assertEqual(stats.representative_count, 2)
            self.assertEqual(stats.drp_record_count, 2)
            self.assertEqual(rollup["1001"]["drp_count"], "2")
            self.assertEqual(rollup["1001"]["has_reg_action"], "Y")
            self.assertEqual(rollup["1001"]["has_criminal"], "Y")
            self.assertEqual(rollup["1002"]["has_any_drp"], "N")

    def test_parse_feed_to_csv_includes_current_employers(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            zip_path = _write_fixture_zip(
                root / "sample.xml.zip",
                _fixture_xml_with_current_employers(
                    [
                        ("222", "BETA CAPITAL LLC"),
                        ("111", "ALPHA ADVISERS LLC"),
                    ]
                ),
            )
            outputs = ParseOutputs(
                representatives_csv=root / "representatives.csv",
                drps_csv=root / "drps.csv",
                rollup_csv=root / "rollup.csv",
            )

            parse_feed_to_csv(
                zip_path,
                SourceContext(
                    run_id="run-current",
                    source_file="sample.xml.zip",
                    source_url="local:sample.xml.zip",
                    retrieved_at="2026-04-30T00:00:00+00:00",
                ),
                outputs,
            )

            rollup = _read_csv_by_key(outputs.rollup_csv, "indvl_pk")

            self.assertEqual(rollup["1001"]["current_employer_count"], "2")
            self.assertEqual(rollup["1001"]["current_employer_org_pks"], "111 | 222")
            self.assertEqual(
                rollup["1001"]["current_employer_names"],
                "ALPHA ADVISERS LLC | BETA CAPITAL LLC",
            )
            self.assertEqual(
                rollup["1001"]["current_employers"],
                "111: ALPHA ADVISERS LLC | 222: BETA CAPITAL LLC",
            )

    def test_compare_rollups_reports_added_removed_and_count_changes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            previous_zip = _write_fixture_zip(root / "previous.xml.zip", _fixture_xml(criminal="N"))
            current_zip = _write_fixture_zip(root / "current.xml.zip", _fixture_xml(criminal="Y"))
            previous_outputs = _parse_fixture(previous_zip, root / "previous", "previous-run")
            current_outputs = _parse_fixture(current_zip, root / "current", "current-run")

            result = compare_rollups(
                current_outputs.rollup_csv,
                previous_outputs.rollup_csv,
                run_id="current-run",
                previous_run_id="previous-run",
            )

            change_types = [change["change_type"] for change in result.changes]
            categories = [change["category"] for change in result.changes]

            self.assertIn("drp_count_changed", change_types)
            self.assertIn("drp_category_added", change_types)
            self.assertIn("has_criminal", categories)

    def test_compare_rollups_reads_all_zip_xml_members_before_comparing(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            previous_zip = _write_fixture_zip_members(
                root / "previous.xml.zip",
                [
                    ("b.xml", _fixture_xml_with_individual("1002", "Bailey", "Jones", "N")),
                    ("a.xml", _fixture_xml_with_individual("1001", "Alex", "Smith", "Y")),
                ],
            )
            current_zip = _write_fixture_zip_members(
                root / "current.xml.zip",
                [
                    ("a.xml", _fixture_xml_with_individual("1001", "Alex", "Smith", "Y")),
                    ("b.xml", _fixture_xml_with_individual("1002", "Bailey", "Jones", "N")),
                ],
            )
            previous_outputs = _parse_fixture(previous_zip, root / "previous", "previous-run")
            current_outputs = _parse_fixture(current_zip, root / "current", "current-run")

            previous_rollup = _read_csv_by_key(previous_outputs.rollup_csv, "indvl_pk")
            current_rollup = _read_csv_by_key(current_outputs.rollup_csv, "indvl_pk")
            result = compare_rollups(
                current_outputs.rollup_csv,
                previous_outputs.rollup_csv,
                run_id="current-run",
                previous_run_id="previous-run",
            )

            self.assertEqual(set(previous_rollup), {"1001", "1002"})
            self.assertEqual(set(current_rollup), {"1001", "1002"})
            self.assertEqual(result.changes, [])

    def test_compare_rollups_reads_gzipped_previous_rollup_baseline(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            previous_zip = _write_fixture_zip(root / "previous.xml.zip", FIXTURE_XML)
            current_zip = _write_fixture_zip(root / "current.xml.zip", FIXTURE_XML)
            previous_outputs = _parse_fixture(previous_zip, root / "previous", "previous-run")
            current_outputs = _parse_fixture(current_zip, root / "current", "current-run")
            gzipped_previous_rollup = root / "previous_rollup.csv.gz"
            with (
                previous_outputs.rollup_csv.open("rb") as source,
                gzip.open(gzipped_previous_rollup, "wb") as destination,
            ):
                shutil.copyfileobj(source, destination)

            result = compare_rollups(
                current_outputs.rollup_csv,
                gzipped_previous_rollup,
                run_id="current-run",
                previous_run_id="previous-run",
            )

            self.assertEqual(result.changes, [])

    def test_compare_rollups_reports_current_employer_changes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            previous_zip = _write_fixture_zip(
                root / "previous.xml.zip",
                _fixture_xml_with_current_employers([("111", "ALPHA ADVISERS LLC")]),
            )
            current_zip = _write_fixture_zip(
                root / "current.xml.zip",
                _fixture_xml_with_current_employers([("222", "BETA CAPITAL LLC")]),
            )
            previous_outputs = _parse_fixture(previous_zip, root / "previous", "previous-run")
            current_outputs = _parse_fixture(current_zip, root / "current", "current-run")

            result = compare_rollups(
                current_outputs.rollup_csv,
                previous_outputs.rollup_csv,
                run_id="current-run",
                previous_run_id="previous-run",
            )

            employer_changes = [
                change
                for change in result.changes
                if change["change_type"] == "current_employer_changed"
            ]

            self.assertEqual(len(employer_changes), 1)
            self.assertEqual(employer_changes[0]["category"], "current_employer")
            self.assertEqual(employer_changes[0]["previous_value"], "111: ALPHA ADVISERS LLC")
            self.assertEqual(employer_changes[0]["current_value"], "222: BETA CAPITAL LLC")

    def test_compare_rollups_skips_employer_changes_for_legacy_baselines(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            current_zip = _write_fixture_zip(
                root / "current.xml.zip",
                _fixture_xml_with_current_employers([("222", "BETA CAPITAL LLC")]),
            )
            current_outputs = _parse_fixture(current_zip, root / "current", "current-run")
            legacy_rollup = root / "legacy_rollup.csv"
            legacy_rollup.write_text(
                "\n".join(
                    [
                        "run_id,source_file,source_url,source_generated_date,retrieved_at,indvl_pk,first_name,middle_name,last_name,suffix,active_ag_registration,profile_link,drp_count,has_any_drp,has_reg_action,has_criminal,has_bankrupt,has_civil_judgment,has_bond,has_judgment,has_investigation,has_customer_complaint,has_termination",
                        "previous-run,previous.xml.zip,local:previous.xml.zip,2026-04-30,2026-04-30T00:00:00+00:00,1001,Alex,,Smith,,Y,https://adviserinfo.sec.gov/IAPD/Individual/1001,0,N,N,N,N,N,N,N,N,N,N",
                        "",
                    ]
                ),
                encoding="utf-8",
            )

            result = compare_rollups(
                current_outputs.rollup_csv,
                legacy_rollup,
                run_id="current-run",
                previous_run_id="previous-run",
            )

            self.assertNotIn(
                "current_employer_changed",
                [change["change_type"] for change in result.changes],
            )

    def test_cli_local_zip_creates_baseline_outputs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            zip_path = _write_fixture_zip(root / "IA_INDVL_Feed_sample.xml.zip", FIXTURE_XML)
            args = build_parser().parse_args(
                [
                    "run",
                    "--input-zip",
                    str(zip_path),
                    "--data-dir",
                    str(root / "data"),
                    "--run-id",
                    "fixture-run",
                ]
            )

            state = run(args)

            self.assertEqual(state["run_id"], "fixture-run")
            self.assertEqual(state["change_count"], 0)
            self.assertTrue(Path(state["summary_md"]).exists())
            self.assertTrue(Path(state["changes_csv"]).exists())
            latest = json.loads((root / "data/state/latest_successful_run.json").read_text())
            self.assertEqual(latest["run_id"], "fixture-run")

    def test_cli_stable_latest_outputs_are_written_for_github_actions(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            zip_path = _write_fixture_zip(root / "IA_INDVL_Feed_sample.xml.zip", FIXTURE_XML)
            args = build_parser().parse_args(
                [
                    "run",
                    "--input-zip",
                    str(zip_path),
                    "--data-dir",
                    str(root / "data"),
                    "--run-id",
                    "fixture-run",
                    "--stable-latest",
                ]
            )

            state = run(args)

            self.assertEqual(state["rollup_csv"], str(root / "data/processed/latest_drp_rollup.csv.gz"))
            self.assertEqual(state["summary_md"], str(root / "data/reports/latest_summary.md"))
            self.assertEqual(state["changes_csv"], str(root / "data/reports/latest_drp_changes.csv"))
            self.assertTrue(Path(state["rollup_csv"]).exists())
            self.assertFalse((root / "data/processed/latest_drp_rollup.csv").exists())
            self.assertTrue(Path(state["summary_md"]).exists())
            self.assertTrue(Path(state["changes_csv"]).exists())
            latest = json.loads((root / "data/state/latest_successful_run.json").read_text())
            self.assertEqual(latest["rollup_csv"], str(root / "data/processed/latest_drp_rollup.csv.gz"))

    def test_cli_skips_comparison_against_unversioned_partial_rollup_baseline(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            data_dir = root / "data"
            processed_dir = data_dir / "processed"
            state_dir = data_dir / "state"
            processed_dir.mkdir(parents=True)
            state_dir.mkdir(parents=True)
            previous_rollup = processed_dir / "previous_rollup.csv"
            previous_rollup.write_text(
                "\n".join(
                    [
                        "run_id,source_file,source_url,source_generated_date,retrieved_at,indvl_pk,first_name,middle_name,last_name,suffix,active_ag_registration,profile_link,drp_count,has_any_drp,has_reg_action,has_criminal,has_bankrupt,has_civil_judgment,has_bond,has_judgment,has_investigation,has_customer_complaint,has_termination",
                        "previous-run,previous.xml.zip,local:previous.xml.zip,2026-04-30,2026-04-30T00:00:00+00:00,1002,Bailey,,Jones,,Y,https://adviserinfo.sec.gov/IAPD/Individual/1002,0,N,N,N,N,N,N,N,N,N,N",
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            (state_dir / "latest_successful_run.json").write_text(
                json.dumps(
                    {
                        "run_id": "previous-run",
                        "rollup_csv": str(previous_rollup),
                    }
                ),
                encoding="utf-8",
            )
            zip_path = _write_fixture_zip_members(
                root / "current.xml.zip",
                [
                    ("a.xml", _fixture_xml_with_individual("1001", "Alex", "Smith", "Y")),
                    ("b.xml", _fixture_xml_with_individual("1002", "Bailey", "Jones", "N")),
                ],
            )
            args = build_parser().parse_args(
                [
                    "run",
                    "--input-zip",
                    str(zip_path),
                    "--data-dir",
                    str(data_dir),
                    "--run-id",
                    "current-run",
                ]
            )

            state = run(args)

            self.assertEqual(state["change_count"], 0)
            self.assertEqual(state["source_xml_member_count"], 2)
            self.assertIn("rollup_parser_version", state)
            self.assertIn("comparison_skipped_reason", state)

    def test_latest_command_prints_latest_successful_run(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            state_dir = root / "data/state"
            state_dir.mkdir(parents=True)
            (state_dir / "latest_successful_run.json").write_text(
                json.dumps(
                    {
                        "run_id": "latest-run",
                        "source_file": "IA_INDVL_Feed_sample.xml.zip",
                        "retrieved_at": "2026-04-30T12:00:00+00:00",
                        "summary_md": "data/reports/latest-run_summary.md",
                        "changes_csv": "data/reports/latest-run_drp_changes.csv",
                        "change_count": 3,
                        "representative_count": 10,
                        "drp_record_count": 4,
                        "representatives_with_drp": 2,
                    }
                ),
                encoding="utf-8",
            )
            args = build_parser().parse_args(["latest", "--data-dir", str(root / "data")])
            output = StringIO()

            with redirect_stdout(output):
                state = latest(args)

            self.assertEqual(state["run_id"], "latest-run")
            self.assertIn("Latest successful run: latest-run", output.getvalue())
            self.assertIn("Reported changes: 3", output.getvalue())

    def test_notify_email_dry_run_uses_latest_summary(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            data_dir = root / "data"
            state_dir = data_dir / "state"
            reports_dir = data_dir / "reports"
            state_dir.mkdir(parents=True)
            reports_dir.mkdir(parents=True)
            summary_path = reports_dir / "latest_summary.md"
            changes_path = reports_dir / "latest_drp_changes.csv"
            summary_path.write_text("# Summary\n\nDRP changes found.\n", encoding="utf-8")
            changes_path.write_text("change_type\nexample\n", encoding="utf-8")
            (state_dir / "latest_successful_run.json").write_text(
                json.dumps(
                    {
                        "run_id": "latest-run",
                        "source_file": "IA_INDVL_Feed_sample.xml.zip",
                        "retrieved_at": "2026-04-30T12:00:00+00:00",
                        "summary_md": str(summary_path),
                        "changes_csv": str(changes_path),
                        "change_count": 2,
                    }
                ),
                encoding="utf-8",
            )
            args = build_parser().parse_args(
                [
                    "notify-email",
                    "--data-dir",
                    str(data_dir),
                    "--dry-run",
                    "--smtp-from",
                    "alerts@example.test",
                    "--smtp-to",
                    "editor@example.test",
                ]
            )
            output = StringIO()

            with redirect_stdout(output):
                sent = notify_email(args)

            self.assertTrue(sent)
            self.assertIn("Dry run: email not sent", output.getvalue())
            self.assertIn("IAR DRP Monitor: 2 change(s) in latest-run", output.getvalue())

    def test_notify_email_skips_when_only_if_changes_and_no_changes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            state_dir = root / "data/state"
            state_dir.mkdir(parents=True)
            (state_dir / "latest_successful_run.json").write_text(
                json.dumps({"run_id": "latest-run", "change_count": 0}),
                encoding="utf-8",
            )
            args = build_parser().parse_args(
                [
                    "notify-email",
                    "--data-dir",
                    str(root / "data"),
                    "--only-if-changes",
                    "--dry-run",
                ]
            )
            output = StringIO()

            with redirect_stdout(output):
                sent = notify_email(args)

            self.assertFalse(sent)
            self.assertIn("No reportable changes detected; skipping email.", output.getvalue())

    def test_email_settings_defaults_blank_port_to_587(self):
        args = build_parser().parse_args(
            [
                "notify-email",
                "--smtp-host",
                "smtp.example.test",
                "--smtp-port",
                "",
                "--smtp-from",
                "alerts@example.test",
                "--smtp-to",
                "editor@example.test",
            ]
        )

        settings = EmailSettings.from_args_env(args)

        self.assertEqual(settings.port, 587)

    def test_workflow_runs_live_monitor_only_for_schedule_or_manual_events(self):
        workflow = (
            Path(__file__).resolve().parents[1]
            / ".github/workflows/iar-drp-monitor.yml"
        ).read_text(encoding="utf-8")
        live_monitor_steps = [
            "Run monitor",
            "Add summary to workflow run",
            "Upload latest report artifacts",
            "Commit latest comparison state",
            "Send change notification email",
            "Send failure notification email",
        ]

        for step_name in live_monitor_steps:
            block = _workflow_step_block(workflow, step_name)
            condition = _workflow_step_if_condition(block)

            self.assertIn("github.event_name == 'schedule'", condition)
            self.assertIn("github.event_name == 'workflow_dispatch'", condition)
            self.assertNotIn("github.event_name != 'pull_request'", condition)

    def test_workflow_pushes_monitor_state_to_explicit_branch_ref(self):
        workflow = (
            Path(__file__).resolve().parents[1]
            / ".github/workflows/iar-drp-monitor.yml"
        ).read_text(encoding="utf-8")
        block = "\n".join(_workflow_step_block(workflow, "Commit latest comparison state"))

        self.assertIn('branch="${GITHUB_REF_NAME:-main}"', block)
        self.assertIn('git fetch origin "$branch"', block)
        self.assertIn('git rebase "origin/$branch"', block)
        self.assertIn('git push origin "HEAD:$branch"', block)
        self.assertNotIn("git pull --rebase", block)
        self.assertNotIn("\n            git push\n", block)

    def test_workflow_commits_compressed_monitor_rollup_state(self):
        workflow = (
            Path(__file__).resolve().parents[1]
            / ".github/workflows/iar-drp-monitor.yml"
        ).read_text(encoding="utf-8")
        block = "\n".join(_workflow_step_block(workflow, "Commit latest comparison state"))

        self.assertIn("git add data/iar_drp_monitor/processed/latest_drp_rollup.csv.gz", block)
        self.assertNotIn("git add data/iar_drp_monitor/processed/latest_drp_rollup.csv\n", block)


def _write_fixture_zip(path: Path, xml: str) -> Path:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("fixture.xml", xml)
    return path


def _write_fixture_zip_members(path: Path, members: list[tuple[str, str]]) -> Path:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, xml in members:
            archive.writestr(name, xml)
    return path


def _parse_fixture(zip_path: Path, output_dir: Path, run_id: str) -> ParseOutputs:
    output_dir.mkdir(parents=True)
    outputs = ParseOutputs(
        representatives_csv=output_dir / "representatives.csv",
        drps_csv=output_dir / "drps.csv",
        rollup_csv=output_dir / "rollup.csv",
    )
    parse_feed_to_csv(
        zip_path,
        SourceContext(
            run_id=run_id,
            source_file=zip_path.name,
            source_url=f"local:{zip_path}",
            retrieved_at="2026-04-30T00:00:00+00:00",
        ),
        outputs,
    )
    return outputs


def _read_csv_by_key(path: Path, key: str) -> dict[str, dict]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return {row[key]: row for row in csv.DictReader(handle)}


def _workflow_step_block(workflow: str, step_name: str) -> list[str]:
    lines = workflow.splitlines()
    start = next(
        index for index, line in enumerate(lines) if line.strip() == f"- name: {step_name}"
    )
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].strip().startswith("- name: "):
            end = index
            break
    return lines[start:end]


def _workflow_step_if_condition(step_block: list[str]) -> str:
    if_lines = [line.strip() for line in step_block if line.strip().startswith("if: ")]
    if not if_lines:
        raise AssertionError(f"Step has no if condition: {step_block[0].strip()}")
    return if_lines[0]


def _fixture_xml(criminal: str) -> str:
    extra_drp = ""
    if criminal == "Y":
        extra_drp = '<DRP hasRegAction="N" hasCriminal="Y" hasBankrupt="N" hasCivilJudc="N" hasBond="N" hasJudgment="N" hasInvstgn="N" hasCustComp="N" hasTermination="N"/>'
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<IAPDIndividualReport GenOn="2026-04-30">
  <Indvls>
    <Indvl>
      <Info lastNm="Smith" firstNm="Alex" indvlPK="1001" actvAGReg="Y" link="https://adviserinfo.sec.gov/IAPD/Individual/1001"/>
      <DRPs>
        <DRP hasRegAction="Y" hasCriminal="N" hasBankrupt="N" hasCivilJudc="N" hasBond="N" hasJudgment="N" hasInvstgn="N" hasCustComp="N" hasTermination="N"/>
        {extra_drp}
      </DRPs>
    </Indvl>
  </Indvls>
</IAPDIndividualReport>
"""


def _fixture_xml_with_individual(
    indvl_pk: str, first_name: str, last_name: str, has_reg_action: str
) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<IAPDIndividualReport GenOn="2026-04-30">
  <Indvls>
    <Indvl>
      <Info lastNm="{last_name}" firstNm="{first_name}" indvlPK="{indvl_pk}" actvAGReg="Y" link="https://adviserinfo.sec.gov/IAPD/Individual/{indvl_pk}"/>
      <DRPs>
        <DRP hasRegAction="{has_reg_action}" hasCriminal="N" hasBankrupt="N" hasCivilJudc="N" hasBond="N" hasJudgment="N" hasInvstgn="N" hasCustComp="N" hasTermination="N"/>
      </DRPs>
    </Indvl>
  </Indvls>
</IAPDIndividualReport>
"""


def _fixture_xml_with_current_employers(employers: list[tuple[str, str]]) -> str:
    employer_xml = "\n".join(
        f'<CrntEmp orgNm="{name}" orgPK="{org_pk}" city="Boston" state="MA" cntry="United States"/>'
        for org_pk, name in employers
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<IAPDIndividualReport GenOn="2026-04-30">
  <Indvls>
    <Indvl>
      <Info lastNm="Smith" firstNm="Alex" indvlPK="1001" actvAGReg="Y" link="https://adviserinfo.sec.gov/IAPD/Individual/1001"/>
      <CrntEmps>
        {employer_xml}
      </CrntEmps>
    </Indvl>
  </Indvls>
</IAPDIndividualReport>
"""


if __name__ == "__main__":
    unittest.main()
