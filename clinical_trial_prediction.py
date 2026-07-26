# ==========================================================
# Clinical Trial Success Prediction & Investment Risk Analysis
# Author: Shruti
# ==========================================================


# ==========================
# STEP 1: Import Libraries
# ==========================

import os

import pandas as pd
import requests

# ==========================
# STEP 2: Create Project Directories
# ==========================

folders = [
    "data",
    "data/raw",
    "data/processed",
    "models",
    "reports"
]


for folder in folders:
    os.makedirs(folder, exist_ok=True)
    # os.makedirs() creates directories recursively.
    # exist_ok=True prevents an error if the folder already exists.


print("Project folders are ready!")


# ==========================================================
# STEP 3: Connect to ClinicalTrials.gov API
# ==========================================================
class ClinicalTrialProjectError(Exception):
    """Base exception for the project."""

page_size = 1000
all_studies = []
next_page_token = None

while True:
    if next_page_token is None:
        api_url = (f"https://clinicaltrials.gov/api/v2/studies?"
                       f"pageSize={page_size}")
    else:
        api_url = (f"https://clinicaltrials.gov/api/v2/studies?"
                       f"pageSize={page_size}&nextPageToken={next_page_token}")

    response = requests.get(api_url)
    if response.status_code != 200:
        raise ClinicalTrialProjectError(
        f"API request failed with status code {response.status_code}"
    )

    data = response.json()
    studies = data["studies"]
    all_studies.extend(studies)
    print(f"Collected studies: {len(all_studies)}")

    next_page_token = data.get("nextPageToken")
    if not next_page_token:
        break


print("\nData collection completed!")
print(f"Total studies collected: {len(all_studies)}")

# Explore first study
studies = all_studies

data_study = studies[0]

print(data_study.keys())


# ==========================================================
# STEP 5: Explore Required Modules
# ==========================================================


print(data_study["protocolSection"].keys())


# Identification module

identification = data_study["protocolSection"]["identificationModule"]

print(type(identification))
print(identification.keys())


# Status module

status = data_study["protocolSection"]["statusModule"]

print(type(status))
print(status.keys())


overall_status = status["overallStatus"]

print(f"Overall Status: {overall_status}")


# Design module

design = data_study["protocolSection"]["designModule"]

print(type(design))
print(design.keys())


# Enrollment information

enrollment_info = design["enrollmentInfo"]

print(type(enrollment_info))
print(enrollment_info.keys())


enrollment_count = enrollment_info["count"]

print(f"Enrollment Count: {enrollment_count}")


# Conditions module

conditions = data_study["protocolSection"]["conditionsModule"]

print(type(conditions))
print(conditions.keys())


conditions_list = conditions["conditions"]

print(type(conditions_list))
print(conditions_list)


# ==========================================================
# STEP 6: Extract Required Features From All Studies
# ==========================================================


extracted_data = []


for study in studies:

    # Access different JSON modules

    identification = study["protocolSection"]["identificationModule"]

    status = study["protocolSection"]["statusModule"]

    design = study["protocolSection"]["designModule"]

    conditions = study["protocolSection"]["conditionsModule"]


    # Create clean record

    record = {

        # Identifier
        "nct_id": identification["nctId"],

        # Study information
        "title": identification["briefTitle"],

        # Target variable
        "overall_status": status["overallStatus"],

        # Features
        "study_type": design["studyType"],

        "phase": design["phases"],

        "enrollment": design["enrollmentInfo"]["count"],

        "conditions": conditions["conditions"]
    }


    # Store each study record

    extracted_data.append(record)



# ==========================================================
# STEP 7: Convert Extracted Data Into DataFrame
# ==========================================================


df = pd.DataFrame(extracted_data)


print("\nFirst 5 Records:")
print(df.head())


print("\nDataset Information:")
df.info()


print("\nDataset Columns:")
print(df.columns)


# ==========================================================
# STEP 8: Save Raw Dataset
# ==========================================================


df.to_csv(
    "data/raw/clinical_trials_raw.csv",
    index=False
)


print("\nRaw dataset saved successfully!")