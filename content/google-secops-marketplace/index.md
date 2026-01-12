# Google SecOps Marketplace

## 2026-01-07

### Feature

**Microsoft Defender ATP**: Version 27.0

* The following new action has been added:

  + **Execute Live Response Command**

### Feature

**Palo Alto Cortex XDR**: Version 21.0

* The following new job has been added:

  + **Sync Incidents**

### Change

**Exchange**: Version 118.0

* Added new parameters (`Event Fields to Exclude` and `Exclude Attachments`) to
  the following connectors:

  + **Exchange - Mail Connector v2**
  + **Exchange - Mail Connector v2 with OAuth Authentication**

### Change

**Siemplify**: Version 99.0

* Updated the TIPCommon method in the following action:

  + **Get Case Details**

### Change

Updated the file management logic of the `Download Attachment From Email`
action in the following integrations:

* **Microsoft Graph Mail**: Version 34.0
* **Microsoft Graph Mail Delegated**: Version 11.0

### Change

**SCC Enterprise**: Version 19.0

* **Integration**: Refactored code to work with the updated API.

### Change

Updated the dependencies of the following integrations:

* **BMC Helix RemedyForce**: Version 14.0
* **EmailV2**: Version 37.0
* **Google Cloud Storage**: Version 12.0
* **HTTP v2**: Version 11.0
* **Jira**: Version 51.0
* **JuniperVSRX**: Version 9.0
* **McAfee Active Response**: Version 8.0
* **PassiveTotal**: Version 12.0
* **Salesforce**: Version 13.0
* **SCCM**: Version 18.0
* **SiemplifyUtilities**: Version 25.0
* **ThreatConnect**: Version 15.0
* **Websense**: Version 13.0
* **WMI**: Version 11.0

### Change

**Google Chronicle**: Version 72.0

* Added support for curated rules in the following action:

  + **Get Rule Details**
* Updated rule severity filter logic in the following connector:

  + **Google Chronicle - Chronicle Alerts Connector**

---
## 2025-12-24

### Feature

New **OpenSearch** integration

### Feature

New **Proofpoint Cloud Threat Response** integration

### Feature

**Siemplify**: Version 98.0

* The following new action has been added:

  + **Export Case**

### Change

**Google Chronicle**: Version 71.0

* Updated event processing and ontology mapping in the following connector:

  + **Google Chronicle - Chronicle Alerts Connector**
* Added support for returning raw logs related to UDM events to the following
  actions:

  + **Get Detection Details**
  + **Execute UDM Search**

### Change

**Fortigate**: Version 17.0

* Expanded the supported log filter in the following connector:

  + **Fortigate - Threat Logs Connector**

---
## 2025-12-17

### Change

**Cofense Triage**: Version 16.0

* Added the ability to disable the overflow mechanism in the following
  connector:

  + **Cofense Triage - Reports Connector**

### Change

**Netskope**: Version 13.0

* **Integration**: Updated the dependencies to include the Netscope SDK library.

### Change

**Siemplify**: Version 97.0

* Extended the capabilities of the following action:

  + **Assign Case**
* Added the ability to add multiple tags using a delimiter to the following
  action:

  + **Case Tag**
* Added a JSON result to the following action:

  + **Create Entity**

### Change

**Splunk**: Version 60.0

* Added support for the latest ES version to the following connector:

  + **Splunk Notable Events Connector**

### Change

**AWS WAF**: Version 8.0

* **Integration**: Updated the authentication logic.

---
## 2025-12-10

### Feature

**Google Threat Intelligence**: Version 7.0

* The following new action has been added:

  + **Private Submit URL**

### Change

**Google Chronicle**: Version 70.0

* Updated the error handling of the API limit and input processing of the
  following action:

  + **Is Value In Data Table**

### Change

**Tenable.io**: Version 12.0

* Updated the entity processing mechanism in the following actions:

  + **List Endpoint Vulnerabilities**
  + **Enrich Entities**
  + **Scan Endpoints**

### Change

**Siemplify**: Version 96.0

* Refactored the following action:

  + **Resume Alert SLA**

### Change

**MISP**: Version 34.0

* Refactored the following actions:

  + **Publish Event**
  + **Unpublish Event**
* Updated the predefined widget of the following action:

  + **Enrich Entities**

---
## 2025-12-04

### Change

**CSV**: Version 38.0

* **Integration**: Updated dependencies.

### Change

**Tenable Security Center**: Version 19.0

* **Integration**: Added support to authenticate using an Access Key and a
  Secret Key.

### Change

**Cofense Triage**: Version 15.0

* Improved category based filtering in the following connector:

  + **Cofense Triage - Reports Connector**

### Change

**Gmail**: Version 6.0

* **Integration**: Updated the dependency files.

---
## 2025-11-26

### Feature

**Google Chronicle**: Version 69.0

* The following new actions have been added:

  + **Generate UDM Query**
  + **Add Entry To Watchlist**

### Change

**CSV**: Version 37.0

* Updated support for nested JSONs in the following action:

  + **Save Json to CSV**

### Change

Updated the dependency files in the following integrations:

* **Exchange**: Version 117.0
* **HTTP V2**: Version 10.0

### Change

**Urlscan.io**: Version 27.0

* Added support for the Domain entity in the following action:

  + **Search For Scans**

### Change

**Jira**: Version 50.0

* Improved handling of comments with additional styling in the following action:

  + **Add Comment**
* Improved handling of comments with additional styling in the following job:

  + **Sync Comments**

---
## 2025-11-19

### Feature

**Google Threat Intelligence**: Version 6.0

* The following new action has been added:

  + **Get Related Associations**

### Change

**Splunk**: Version 59.0

* Refactored the following integration items to use the new API endpoints:

  + **Ping**
  + **Get Host Events**
  + **Splunk Notable Events Connector**
  + **Sync Splunk ES Closed Events**
  + **Sync Splunk ES Comments**

### Change

**Cofense Triage**: Version 14.0

* Added the ability to filter based on category to the following connector:

  + **Cofense Triage - Reports Connector**

### Change

**Google Chronicle**: Version 68.0

* Improved error handling in the following jobs:

  + **Google Chronicle Sync Job**
  + **Google Chronicle Alerts Creator Job**

### Change

**Okta**: Version 11.0

* Updated the pagination processing mechanism in the following actions:

  + **List Users**
  + **Add Group**
  + **Get Group**
  + **List Providers**

### Change

**SentinelOneV2**: Version 44.0

* Updated the mechanism for fetching agent information in the following actions:

  + **Disconnect Agent From Network**
  + **Enrich Endpoint**
  + **Get Agent Status**
  + **Get Application List For Endpoint**
  + **Get Events For Endpoint Hours Back**
  + **Initiate Full Scan**
  + **Move Agents**
  + **Reconnect Agent To The Network**

---
## 2025-11-12

### Feature

New **Azure Monitor** integration

### Feature

**Siemplify**: Version 95.0

* The following new action has been added:

  + **Get Case Alerts**

### Changed

**CrowdStrike Falcon**: Version 69.0

* Refactored the pagination and filtering mechanism in the following actions:

  + **List Uploaded IOCs**
  + **List Hosts**
* Added support for wildcards to `File Paths to Scan` in the following action:

  + **On-Demand Scan**

### Changed

Updated action definitions to meet the new requirements of IDE in the following
integrations:

Updated Integrations (45)

* **Active Directory**: Version 38.0
* **AlienVault USM Appliance**: Version 22.0
* **AlienVault USM Anywhere**: Version 32.0
* **Area1**: Version 6.0
* **BulkWhoIs**: Version 16.0
* **CA Service Desk Manager**: Version 23.0
* **Carbon Black Response**: Version 35.0
* **Case Federation**: Version 6.0
* **ConnectWise**: Version 19.0
* **CSV**: Version 36.0
* **DeepSight**: Version 9.0
* **DomainTools**: Version 9.0
* **Email V2**: Version 36.0
* **Endgame**: Version 11.0
* **Exchange**: Version 116.0
* **F5 Big IQ**: Version 6.0
* **FileOperation**: Version 12.0
* **HTTP**: Version 12.0
* **IntSights**: Version 23.0
* **Jira**: Version 49.0
* **JuniperVSRX**: Version 8.0
* **McAfee EPO**: Version 17.0
* **McAfee NSM**: Version 8.0
* **Microsoft Graph Security**: Version 23.0
* **MSSQL**: Version 17.0
* **Palo Alto Next Gen Firewall**: Version 26.0
* **PhishRod**: Version 4.0
* **RSA NetWitness**: Version 17.0
* **Runners**: Version 5.0
* **Salesforce**: Version 12.0
* **SCC Enterprise**: Version 18.0
* **ServiceNow**: Version 59.0
* **Siemplify**: Version 95.0
* **SSH**: Version 18.0
* **Symantec Endpoint Protection**: Version 18.0
* **Symantec Endpoint Protection 12**: Version 13.0
* **Symantec ICDX**: Version 7.0
* **Tenable Security Center**: Version 18.0
* **Twilio**: Version 14.0
* **VSphere**: Version 8.0
* **VirusTotal**: Version 40.0
* **WildFire**: Version 8.0
* **WMI**: Version 10.0
* **XForce**: Version 16.0
* **Zabbix**: Version 14.0
* **Zendesk**: Version 10.0

### Changed

**Cybereason**: Version 21.0

* **Integration**: Added ability to provide a CA Certificate file as part of the
  configuration.

### Changed

**Google Chronicle**: Version 67.0

* Updated curated detections processing logic in the following action:

  + **Get Detection Details**

### Changed

The following integrations are now GUS recommended:

* **CrowdStrike Falcon**: Version 69.0
* **Wiz**: Version 3.0
* **Fortigate**: Version 16.0

### Changed

Updated the dependency files in the following integrations:

* **Microsoft Graph Mail**: Version 33.0
* **Microsoft Graph Mail Delegated**: Version 10.0

### Changed

**Google Security Command Center**: Version 14.0

* Added the ability to ingest Toxic Combinations and Chokepoints in the
  following connector:

  + **Google Security Command Center - Findings Connector**

---
## 2025-11-05

### Feature

**SentinelOneV2**: Version 43.0

* The following new action has been added:

  + **Get Site Agents**

### Changed

**FortiAnalyzer**: Version 8.0

* Updated search processing logic in the following action:

  + **Search Logs**

### Changed

**Freshworks Freshservice**: Version 15.0

* Added the ability to provide a department in the integration configuration for
  the following action:

  + **Create Ticket**

### Changed

**Microsoft Teams**: Version 31.0

* **Integration**: Updated the integration's action definitions to meet the new
  requirements of the IDE.

### Feature

**Palo Alto XDR**: Version 20.0

* The following new action has been added:

  + **Scan Endpoint**

### Changed

**AWS Identity and Access Management**: Version 7.0

* Refactored the following actions:

  + **Create User**
  + **Create Group**
  + **Create Policy**
  + **List Users**
  + **List Groups**
  + **List Policies**

---
## 2025-10-29

### Changed

**Palo Alto Cortex XDR**: Version 19.0

* Updated incident processing logic in the following action:

  + **Get Incident Details**
* Added new filtering options, the ability to create a SecOps alert for every
  Palo Alto XDR alert, and the ability to track updates to an incident in the
  following connector:

  + **Palo Alto Cortex XDR Connector**

### Changed

**Tanium**: Version 15.0

* (REGRESSIVE) Updated JSON result to return data for multiple columns in the
  following action:

  + **Get Question Results**

### Changed

**ZScaler**: Version 10.0

* Added support for domain entity type in the following actions:

  + **Add to Whitelist**
  + **Lookup Entity**

### Changed

**Microsoft Graph Mail Delegated**: Version 9.0

* Updated the file management logic in the following action:

  + **Download Attachments from Email**

### Changed

**CSV**: Version 35.0

* Updated file path processing logic in the following connector:

  + **CSV Connector**

### Changed

**Exchange**: Version 115.0

* Updated the file management logic in the following action:

  + **Download Attachments**

### Changed

**Microsoft Graph Mail**: Version 32.0

* Updated the file management logic in the following action:

  + **Download Attachments from Email**

### Changed

**CrowdStrike Falcon**: Version 68.0

* Update the following action to check if there is an existing identical running
  scan for a provided hostname before creating a new one:

  + **On-Demand Scan**

---
## 2025-10-22

### Changed

**CrowdStrike Falcon**: Version 67.0

* Fixed a bug where the Contains filter would fail to find hosts when the
  `Max Hosts To Return` limit was applied in the following action:

  + **List Host**

### Feature

**SentinelOneV2**: Version 42.0

* The following new actions have been added:

  + **Create Device Control Rule**
  + **Delete Device Control Rule**
  + **Update Device Control Rule**

### Changed

**CSV**: Version 34.0

* Fixed a bug that caused inconsistent column order for the same JSON input by
  stabilizing the order based on the keys of the first object in the list in the
  following action:

  + **Save Json to CSV**

### Changed

**DomainTools**: Version 8.0

* Extended capabilities in the following action:

  + **Get Domain Risk**
* Added support for the domain entity type in the following actions:

  + **Get Domain Profile**
  + **Get Domain Risk**
  + **Reverse Domain**

---
## 2025-10-15

### Changed

**Microsoft Teams**: Version 30.0

* **Integration**: Fixed an issue with the special characters in the query
  parameters.

### Changed

**Okta**: Version 10.0

* Updated the pagination processing mechanism in the following actions:

  + **List Users**
  + **Add Group**
  + **Get Group**
  + **List Providers**

### Changed

**CrowdStrike Falcon**: Version 66.0

* Updated entity processing logic in the following actions:

  + **Contain Endpoint**
  + **Download File**
  + **Execute Command**
  + **Get Host Information**
  + **Lift Contained Endpoint**
  + **List Host Vulnerabilities**
  + **On-Demand Scan**
  + **Run Script**

### Changed

**Azure Active Directory**: Version 19.0

* Improved performance by implementing a direct API filter query for group name
  searches, which avoids fetching all groups and significantly reduces execution
  time in large-group environments, in the following action:

  + **List Members in Group**

### Changed

Updated dependencies in the following integrations:

* **Microsoft Teams**: Version 30.0
* **Microsoft Graph Mail Delegated**: Version 8.0
* **Exchange**: Version 114.0
* **Case Federation**: Version 5.0
* **Azure Security Center**: Version 12.0

### Changed

**UrlScan.io**: Version 26.0

* Added ability to scan domains and IPs in the following action:

  + **URL Check**

### Changed

**ThreatQ**: Version 15.0

* Updated the API request payload to align with a change in the ThreatQ API in
  the following actions:

  + **Enrich IP**
  + **Enrich URL**
  + **Enrich Email**
  + **Enrich Hash**
  + **Enrich CVE**

### Feature

**CrowdStrike Falcon**: Version 66.0

* The following new action has been added:

  + **Get Alert Details**

---
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
