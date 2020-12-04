# LICENSE: MIT
# Requires: python, pytrials
# pytrials installed via `py -m pip install pytrials`
# Usage info via `py scraper.py --help`
# Example usage: `py scraper.py some+search+query OfficialTitle Phase StudyType
from pytrials.client import ClinicalTrials
import argparse
import csv
import os

available_columns = [
    "NCTId",
    "Acronym",
    "BriefTitle",
    "OfficialTitle",
    "Condition",
    "HealthyVolunteers",
    "InterventionName",
    "InterventionOtherName",
    "InterventionDescription",
    "InterventionType",
    "ArmGroupLabel",
    "ArmGroupDescription",
    "ArmGroupType",
    "PrimaryOutcomeMeasure",
    "PrimaryOutcomeDescription",
    "SecondaryOutcomeMeasure",
    "SecondaryOutcomeDescription",
    "OtherOutcomeMeasure",
    "OtherOutcomeDescription",
    "OutcomeMeasureTitle",
    "OutcomeMeasureDescription",
    "Phase",
    "StdAge",
    "BriefSummary",
    "Keyword",
    "LeadSponsorName",
    "OrgStudyId",
    "SecondaryId",
    "NCTIdAlias",
    "LocationFacility",
    "LocationStatus",
    "LocationState",
    "LocationCountry",
    "LocationCity",
    "BioSpecDescription",
    "ResponsiblePartyInvestigatorFullName",
    "ResponsiblePartyInvestigatorTitle",
    "ResponsiblePartyInvestigatorAffiliation",
    "ResponsiblePartyOldNameTitle",
    "ResponsiblePartyOldOrganization",
    "OverallOfficialAffiliation",
    "OverallOfficialRole",
    "OverallOfficialName",
    "CentralContactName",
    "DesignAllocation",
    "DesignInterventionModel",
    "DesignMasking",
    "DesignWhoMasked",
    "DesignObservationalModel",
    "DesignPrimaryPurpose",
    "DesignTimePerspective",
    "StudyType",
    "ConditionMeshTerm",
    "InterventionMeshTerm",
    "ConditionAncestorTerm",
    "InterventionAncestorTerm",
    "CollaboratorName",
    "LocationContactName",
]

parser = argparse.ArgumentParser(description="Pull data from clinicaltrials.gov")
parser.add_argument(
    "search_query",
    metavar="search_query",
    type=str,
    help="Search query for clinicaltrials.gov",
)

parser.add_argument(
    "columns",
    metavar="column",
    type=str,
    nargs="+",
    choices=available_columns,
    help="Column names",
)

parser.add_argument(
    "--output_csv",
    type=str,
    help="output csv file path [default output.csv]",
    default="output.csv",
)
parser.add_argument(
    "--rows", type=int, help="Max number of rows to export [default 500]", default=500
)

args = parser.parse_args()


ct = ClinicalTrials()

results = ct.get_study_fields(
    search_expr=args.search_query,
    fields=["NCTId"] + args.columns,
    max_studies=args.rows,
    fmt="csv",
)

print("Writing to {}".format(args.output_csv))
with open(args.output_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(results)

os.system("start excel {}".format(args.output_csv))
