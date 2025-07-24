# Google SecOps Marketplace

## 2025-07-23

### Feature

**Siemplify**: Version 94.0

* The following new actions have been added:

  + **Get Custom Field Values**
  + **Resume Case SLA**
  + **Pause Case SLA**

### Changed

**Sophos**: Version 18.0

Added ability to work with new authentication method in the following action:

* **Get Events Log**

---
## 2025-07-16

### Feature

**Google Chronicle**: Version 62.0

* The following new actions have been added:

  + **Remove Rows From Data Table**
  + **Get Data Tables**
  + **Is Value In Data Table**
  + **Add Rows To Data Table**

### Changed

**Azure Security Center**: Version 11.0

* **Integration**: Refactored the integration code to support the updated API.

### Changed

**Mandiant Threat Intelligence**: Version 14.0

* Improved entity processing logic in the following action:

  + **Enrich Entities**

### Changed

**Microsoft Azure Sentinel**: Version 55.0

* Updated logger initialization in the following connector:

  + **Microsoft Azure Sentinel - Incident Connector v2**

### Changed

**MySQL**: Version 5.0

* Refined query processing in the following action:

  + **Run SQL Query**

---
## 2025-07-09

### Changed

**BMC Remedy ITSM**: Version 9.0

* Updated input parameter processing in the following action:

  + **Create Incident**

### Changed

**ServiceNow**: Version 58.0

* Updated processing of record object in the following connector:

  + **ServiceNow - ServiceNow Connector**

### Changed

**Siemplify**: Version 93.0

* Updated action logic in the following actions:

  + **Get Case Details**
  + **Get Similar Cases**

---
## 2025-07-02

### Feature

**Okta**: Version 9.0

* The following new action has been added:

  + **Send SSF to Okta**

### Changed

**CrowdStrike Falcon**: Version 62.0

* Updated JSON Result structure in the following action:

  + **List Hosts**

### Changed

**Google Chronicle**: Version 61.0

* Updated action processing logic in the following action:

  + **Execute UDM Query**

### Changed

**Vertex AI**: Version 3.0

* **Integration**: Updated the handling of non-Google models.

---
## 2025-06-27

### Changed

**Siemplify**: Version 92.0

* Updated action logic in the following actions:

  + **Get Case Details**
  + **Get Similar Cases**
  + **Update Case Description**

---
## 2025-06-25

### Changed

Refactored the code to work with updated API in the following integrations:

* **Case Federation**: Version 3.0
* **Siemplify**: Version 91.0

### Changed

**Microsoft Azure Sentinel**: Version 54.0

* Added an ability to not process the alert until Scheduled/NRT alert objects are available from API in the following connectors:

  + **Microsoft Azure Sentinel - Incident Connector v2**
  + **Microsoft Azure Sentinel - Incident Tracking Connector**

### Changed

**SentinelOneV2**: Version 39.0

* Updated ontology mapping in the following connector:

  + **SentinelOneV2 - Threats Connector**

### Changed

**Siemplify**: Version 91.0

* Updated Predefined Widget in the following action:

  + **Get Similar Cases**

---
## 2025-06-18

### Changed

**Google Chronicle**: Version 60.0

* Updated risk score handling in the following connector:

  + **Google Chronicle - Alerts Connector**

### Changed

**Microsoft Teams**: Version 27.0

* **Integration**: Refactored the code to work with updated API.

---
## 2025-06-11

### Feature

New **Akamai** integration

### Feature

New **Google Threat Intelligence** integration

### Changed

**Darktrace**: Version 18.0

* Added ability to filter model breaches by priority in the following connector:

  + **Darktrace - Model Breaches Connector**

### Changed

Refactored the code to work with updated API in the following integrations:

* **Exchange**: Version 113.0
* **ServiceNow**: Version 57.0
* **Microsoft Graph Mail Delegated**: Version 5.0

Refactored the code in the following integrations:

* **Gmail**: Version 4.0
* **Google Cloud API**: Version 6.0
* **HTTP v2**: Version 9.0
* **Microsoft Graph Mail**: Version 28.0
* **Tor**: Version 7.0

---
## 2025-06-04

### Changed

Refactored the code to work with updated API in the following integrations:

* **BMC Remedy ITSM**: Version 8.0
* **Gmail**: Version 3.0
* **Google Cloud API**: Version 5.0
* **Microsoft Graph Mail**: Version 27.0
* **Service Desk Plus V3**: Version 6.0
* **Vertex AI**: Version 2.0

### Changed

**Google Chronicle**: Version 59.0

* Updated the API root to be configurable in IDE in the following connector:
  + **Google Chronicle - Chronicle Alerts Connector**

### Changed

**Nmap**: Version 2.0

* Updated JSON Result structure in the following action:
  + **Scan Entities**

### Changed

**Vertex AI**: Version 2.0

* Fixed non-Google models that weren't working

---
