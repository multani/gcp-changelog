# Google SecOps Marketplace

## 2025-10-09

### Changed

**Google Workspace**: Version 22.0

* Updated the action description to reflect that the action deletes the
  extension from the blocklist rather than deleting the extension from the
  organizational unit in the following action:

  + **Delete Extension**

### Changed

**Google Chronicle**: Version 66.0

* Updated processing of reference list rows in the following action:

  + **Get Reference Lists**

### Changed

**Google Threat Intelligence**: Version 5.0

* Added ability to filter by issue name in the following connector:

  + **Google Threat Intelligence - ASM Issues Connector**
* Added ability to filter events in the following connector:

  + **Google Threat Intelligence - DTM Alerts Connector**

### Changed

**Microsoft Teams**: Version 29.0

* Refactored action logic in the following actions:

  + **Get Authorization**
  + **Generate Token**

---
## 2025-09-25

### Feature

New **Apache Kafka** integration

### Feature

**Microsoft Azure Sentinel**: Version 57.0

* The following new job has been added:

  + **Sync Incidents**

### Changed

**Any.Run**: Version 8.0

* Updated the available privacy settings in the following actions:

  + **Analyze URL**
  + **Analyze File URL**
  + **Analyze File**

### Changed

**CrowdStrike Falcon**: Version 64.0

* Updated timeout handling in the following connector:

  + **Crowdstrike Falcon - Streaming Events Connector**
* **Integration**: Updated authentication to support multi-tenancy execution.

### Changed

**Google Workspace**: Version 21.0

* Expanded capabilities of the following action:

  + **List OU Of Account**
* Updated processing of the organization unit inside the following actions:

  + **Block Extension**
  + **Delete Extension**
  + **List OU Of Account**

### Changed

**Orca Security**: Version 12.0

* **Integration**: (REGRESSIVE) Updated to support the latest API version.

  Ontology has been updated. Overwrite current ontology mapping to align
  with the new API alert structure.

### Changed

**Google Chronicle**: Version 65.0

* Updated the filtering mechanism of the following action:

  + **Get Data Tables**

---
## 2025-09-17

### Feature

**SentinelOneV2**: Version 41.0

* The following new action has been added:

  + **Update Alert**
* The following new connector has been added:

  + **SentinelOne - Alert Connector**
* A new predefined widget has been added to the following action:

  + **Update Alert**

### Feature

**Google Threat Intelligence**: Version 4.0

* The following new action has been added:

  + **Set DTM Alert Analysis**

### Feature

**Palo Alto Cortex XDR**: Version 18.0

* The following new actions have been added:

  + **Add Comment To Incident**
  + **Execute XQL Search**
  + **Get Incident Details**

### Changed

**Google Threat Intelligence**: Version 4.0

* Updated the processing of the threat actor entity in the following action:

  + **Enrich Entities**
* Updated the predefined widget in the following actions:

  (REGRESSIVE) The widget now works with GTI information. To see the changes, the widget must be re-added to the existing views in playbooks.

  + **Enrich Entities**
  + **Enrich IOCs**
* Added JSON samples to the following action:

  + **Enrich Entities**

### Changed

**Trend Vision One**: Version 6.0

* Added support for Agent UUID in the following actions:

  + **Enrich Entities**
  + **Execute Custom Script**
  + **Isolate Endpoint**
  + **Unisolate Endpoint**

### Changed

**Splunk**: Version 58.0

* Updated the alert processing logic in the following connector:

  + **Splunk ES - Notable Events Connector**

### Changed

**Jira**: Version 48.0

* **Integration**: Updated the SDK version.

### Changed

Added the ability to modify the `API Root` and `Login API Root` in the following integrations:

* **Azure Active Directory**: Version 18.0
* **Azure AD Identity Protection**: Version 7.0
* **Microsoft Teams**: Version 28.0

### Changed

**Vertex AI**: Version 4.0

* **Integration**: Increased the default timeout for API requests.

### Changed

**Microsoft Azure Sentinel**: Version 56.0

* Updated mapping for the `ScheduledAlert` event types in the following connector:

  + **Microsoft Azure Sentinel Incident Connector v2**

---
## 2025-09-03

### Changed

**Google Threat Intelligence**: Version 3.0

* Extended supported filters in the following connector:

  + **Google Threat Intelligence - ASM Issues Connector**

---
## 2025-08-27

### Feature

**Google Workspace**: Version 20.0

* The following new actions have been added:

  + **Block Extension**
  + **Delete Extension**
  + **Get Extension Details**
  + **Get Host Browser Details**
  + **Search User Activity Events**

### Changed

**Google Threat Intelligence**: Version 3.0

* **Integration:** Updated authentication flow.

---
## 2025-08-20

### Changed

**CrowdStrike Falcon**: Version 63.0

* Updated processing of `On-Demand Scan` alerts in the following connector:

  + **Crowdstrike Falcon - Alerts Connector**

### Changed

**Google Chronicle**: Version 64.0

* Added support for aggregated searches in the following action:

  + **Execute UDM Query**

### Changed

**Microsoft Graph Mail**: Version 30.0

* Improved handling of `Case Name Template` in the following connector:

  + **Microsoft Graph Mail - Microsoft Graph Mail Connector**

### Changed

**Microsoft Graph Mail Delegated**: Version 6.0

* Improved handling of `Case Name Template` in the following connector:

  + **Microsoft Graph Mail Delegated - Microsoft Graph Mail Delegated Connector**

---
## 2025-08-13

### Feature

New **CyberArk Credential Provider** integration

### Changed

**Jira**: Version 47.0

* Updated timestamp processing logic in the following jobs:

  + **Sync Comments**
  + **Sync Closure**
* Updated logic for processing closed tickets in the following job:

  + **Sync Closure**

### Changed

**Microsoft Graph Mail**: Version 29.0

* **Integration**: Updated dependencies.

---
## 2025-08-04

### Feature

**Google Chronicle**: Version 63.0

* The following new actions have been added:

  + **Ask Gemini**
  + **Enrich Entities**

### Changed

**Case Federation**: Version 4.0

* **Integration:** Refactored the code.

### Changed

**Gmail**: Version 5.0

* **Integration**: Improved error handling.

### Changed

**Google Chronicle**: Version 63.0

* The following actions have been deprecated:

  + **Enrich Domain**
  + **Enrich IP**

### Changed

**QRadar**: Version 60.0

* Updated offense processing logic in the following connector:

  + **Qradar - Baseline Offenses Connector**

### Changed

**SentinelOneV2**: Version 40.0

* Added ability to fetch agent information in the following actions:

  + **Disconnect Agent From Network**
  + **Enrich Endpoint**
  + **Get Agent Status**
  + **Get Application List For Endpoint**
  + **Get Events For Endpoint Hours Back**
  + **Initiate Full Scan**
  + **Move Agents**
  + **Reconnect Agent To The Network**

---
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
