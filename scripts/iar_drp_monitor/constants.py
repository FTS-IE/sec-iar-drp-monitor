from pathlib import Path


MANIFEST_URL = (
    "https://reports.adviserinfo.sec.gov/reports/CompilationReports/"
    "CompilationReports.manifest.json"
)
DOWNLOAD_BASE_URL = "https://reports.adviserinfo.sec.gov/reports/CompilationReports"
DEFAULT_DATA_DIR = Path("data/iar_drp_monitor")
ROLLUP_PARSER_VERSION = 2

DRP_FLAG_MAP = {
    "hasRegAction": "has_reg_action",
    "hasCriminal": "has_criminal",
    "hasBankrupt": "has_bankrupt",
    "hasCivilJudc": "has_civil_judgment",
    "hasBond": "has_bond",
    "hasJudgment": "has_judgment",
    "hasInvstgn": "has_investigation",
    "hasCustComp": "has_customer_complaint",
    "hasTermination": "has_termination",
}

DRP_FLAG_FIELDS = list(DRP_FLAG_MAP.values())

CURRENT_EMPLOYERS_FIELD = "current_employers"
CURRENT_EMPLOYER_FIELDS = [
    "current_employer_count",
    "current_employer_org_pks",
    "current_employer_names",
    CURRENT_EMPLOYERS_FIELD,
]

REPRESENTATIVE_FIELDS = [
    "run_id",
    "source_file",
    "source_url",
    "source_generated_date",
    "retrieved_at",
    "indvl_pk",
    "first_name",
    "middle_name",
    "last_name",
    "suffix",
    "active_ag_registration",
    "profile_link",
    *CURRENT_EMPLOYER_FIELDS,
]

DRP_FIELDS = [
    "run_id",
    "source_file",
    "source_url",
    "source_generated_date",
    "retrieved_at",
    "indvl_pk",
    "drp_index",
    *DRP_FLAG_FIELDS,
]

DRP_ROLLUP_FIELDS = [
    "run_id",
    "source_file",
    "source_url",
    "source_generated_date",
    "retrieved_at",
    "indvl_pk",
    "first_name",
    "middle_name",
    "last_name",
    "suffix",
    "active_ag_registration",
    "profile_link",
    *CURRENT_EMPLOYER_FIELDS,
    "drp_count",
    "has_any_drp",
    *DRP_FLAG_FIELDS,
]

CHANGE_FIELDS = [
    "run_id",
    "previous_run_id",
    "change_type",
    "indvl_pk",
    "first_name",
    "middle_name",
    "last_name",
    "suffix",
    "profile_link",
    "category",
    "previous_value",
    "current_value",
    "previous_drp_count",
    "current_drp_count",
    "previous_source_file",
    "current_source_file",
]
