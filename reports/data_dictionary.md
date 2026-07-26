# Data Dictionary

## Project
Clinical Trial Success Prediction & Investment Risk Analysis

---

| Feature | JSON Path | Data Type | ML Role | Description |
|---------|-----------|-----------|---------|-------------|
| NCT ID | protocolSection → identificationModule → nctId | String | Identifier | Unique ClinicalTrials.gov study ID |
| Study Title | protocolSection → identificationModule → briefTitle | String | Reference | Public title of the clinical trial |
| Overall Status | protocolSection → statusModule → overallStatus | Categorical | Target | Current status of the clinical trial |
| Phase | protocolSection → designModule → phases | List | Feature | Clinical trial phase |
| Enrollment Count | protocolSection → designModule → enrollmentInfo → count | Integer | Feature | Number of participants |
| Enrollment Type | protocolSection → designModule → enrollmentInfo → type | String | Metadata | Planned or Actual enrollment |
| Conditions | protocolSection → conditionsModule → conditions | List | Feature | Diseases being studied |