# Google SecOps Marketplace

## 2026-04-29

### Change

**UrlScan.io**: Version 30.0

* Added `is_risky` handling to the following action:

  + **Url Check**

### Change

**Siemplify**: Version 107.0

* **Integration**: Updated TIPCommon dependency.

### Change

**Microsoft Graph Mail**: Version 41.0

* Updated MSG attachments processing logic in the following connector:

  + **Microsoft Graph Mail Connector**

### Change

**Zerofox**: Version 4.0

* **Integration**: Updated documentation link.

### Change

**MISP**: Version 39.0

* Updated tag retrieval logic in the following actions:

  + **Add Tag to an Attribute**
  + **Add Tag to an Event**
  + **Remove Tag from an Attribute**
  + **Remove Tag from an Event**

### Change

**Anomali ThreatStream**: Version 16.0

* Added `is_risky` handling to the following action:

  + **Enrich Entities**

### Change

**Microsoft Graph Mail Delegated**: Version 18.0

* Updated MSG attachments processing logic in the following connector:

  + **Microsoft Graph Mail Delegated Connector**

### Change

**Palo Alto Cortex XDR**: Version 28.0

* Added the ability to ignore specific artifact types to the following
  connector:

  + **Palo Alto Cortex XDR Connector**

### Change

Source code is now publicly available on [GitHub](https://github.com/chronicle/content-hub)
for the following integrations:

* **Cisco Orbital**: Version 9.0
* **F5 Big IQ**: Version 8.0
* **FireEye EX**: Version 14.0
* **HCL BigFix Inventory**: Version 6.0
* **Illusive Networks**: Version 8.0
* **Lastline**: Version 10.0
* **McAfee ATD**: Version 18.0
* **McAfee Active Response**: Version 10.0
* **ObserveIT**: Version 6.0
* **Outpost24**: Version 9.0
* **Site24x7**: Version 7.0
* **Splash**: Version 8.0
* **Websense**: Version 15.0

---
## 2026-04-22

### Feature

**Netskope**: Version 17.0

* The following new actions have been added:

  + **Add Entities to URL List**
  + **Deploy URL List Changes**

### Change

**Netskope**: Version 17.0

* Added a new `Use V2 API` parameter to the following actions:

  + **List Clients**
  + **List Quarantined Files**
* **Integration**: Added support for V2 API endpoints and OAuth 2.0
  authentication.

### Change

**Qualys VM**: Version 26.0

* **Integration**: Migrated to the latest Qualys API endpoints.

### Change

**SCC Enterprise**: Version 21.0

* Updated ticket synchronization logic in the following job:

  + **Sync SCC Jira Tickets**

### Change

**McAfee Mvision EDR**: Version 12.0

* **Integration**: Added support for configuring the `Login API Root` as a
  customizable parameter.

---
## 2026-04-15

### Feature

**SentinelOneV2**: Version 50.0

* The following new job has been added:

  + **Sync Threats**

### Feature

**CrowdStrike Falcon**: Version 76.0

* The following new job has been added:

  + **Sync Alerts**

### Change

**ServiceNow**: Version 64.0

* Added support for disabling overflow settings and updated ticket processing
  and environment mapping logic in the following connector:

  + **ServiceNow Connector**

### Change

**Zscaler**: Version 14.0

* Added the ability to provide IOCs using input parameters to the following
  actions:

  + **Add To Blacklist**
  + **Add To Whitelist**
  + **Remove From Blacklist**
  + **Remove From Whitelist**
* **Integration**: Added support for OAuth authentication.

### Change

**Mandiant Threat Intelligence**: Version 17.0

* Optimized execution performance and entity processing logic in the following
  action:

  + **Enrich Entities**

---
## 2026-04-10

### Feature

**Gmail**: Version 9.0

* A new predefined widget has been added to the following action:

  + **Delete Email**

### Feature

**Tanium**: Version 19.0

* A new predefined widget has been added to the following action:

  + **Create Connection**

### Feature

**Cynet**: Version 13.0

* New predefined widgets have been added to the following actions:

  + **Delete Hash In Hosts**
  + **Kill Hash In Hosts**
  + **Quarantine Hash In Hosts**

### Feature

**Area1**: Version 9.0

* A new predefined widget has been added to the following action:

  + **Search Indicator**

### Feature

**Azure Active Directory**: Version 26.0

* A new predefined widget has been added to the following action:

  + **Is User In a Group**

### Feature

**MX ToolBox**: Version 14.0

* A new predefined widget has been added to the following action:

  + **SPF Lookup**

### Feature

**Active Directory**: Version 41.0

* New predefined widgets have been added to the following actions:

  + **Is User In Group**
  + **List User Groups**

### Feature

**Cisco Threat Grid**: Version 18.0

* New predefined widgets have been added to the following actions:

  + **Get Hash Associated Domains**
  + **Get Hash Associated IPs**

### Feature

**Google Chronicle**: Version 81.0

* The following new action has been added:

  + **Is CIDR In Data Table**

### Feature

**Endgame**: Version 15.0

* New predefined widgets have been added to the following actions:

  + **Collect Autoruns**
  + **Drivers Survey** (Windows only)
  + **Firewall Survey** (Windows only)
  + **Process Survey**
  + **Removable Media Survey** (Windows only)
  + **Software Survey** (Windows only)
  + **User Sessions Survey**

### Feature

**AWS Identity and Access Management (IAM)**: Version 10.0

* A new predefined widget has been added to the following action:

  + **Disable User Access**

### Feature

**Carbon Black Response**: Version 39.0

* A new predefined widget has been added to the following action:

  + **Download Binary**

### Feature

**Carbon Black Protection**: Version 13.0

* A new predefined widget has been added to the following action:

  + **Get Computers By File**

### Feature

**McAfee ATD**: Version 17.0

* A new predefined widget has been added to the following action:

  + **Check Hash**

### Feature

**UnshortenMe**: Version 9.0

* A new predefined widget has been added to the following action:

  + **Unshorten URL**

### Feature

**CiscoUmbrella**: Version 19.0

* A new predefined widget has been added to the following action:

  + **Get Associated Domains**

### Feature

**Microsoft Graph Mail**: Version 40.0

* A new predefined widget has been added to the following action:

  + **Get Mailbox Account Out Of Facility Settings**

### Change

**Exabeam Advanced Analytics**: Version 10.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**Check Point SandBlast**: Version 8.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Query**
  + **Upload File**

### Change

**Palo Alto AutoFocus**: Version 12.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Hunt Domain**
  + **Hunt File**
  + **Hunt Ip**
  + **Hunt Url**

### Change

**XForce**: Version 19.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Hash Info**
  + **Get IP Info**
  + **Get IP malware**
  + **Get Url Info**

### Change

**Trend Micro Apex Central**: Version 7.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Create Entity UDSO**
  + **Create File UDSO**
  + **Enrich Entities**

### Change

**BulkWhoIs**: Version 18.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **WhoIs Details**

### Change

**Any.Run**: Version 12.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Report**

### Change

**Siemplify ThreatFuse**: Version 19.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**Google Cloud Policy Intelligence**: Version 7.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Search Service Account Activity**

### Change

**MISP**: Version 38.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Get Event Details**
  + **Get Related Events**

### Change

**ReversingLabs Titanium**: Version 12.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Malware Details**

### Change

**MX ToolBox**: Version 14.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **A Record Lookup**
  + **Blacklist Check**
  + **MX Record Lookup**
  + **Reverse DNS Lookup**

### Change

**Google Rapid Response (GRR)**: Version 11.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Client Details**
  + **List Clients**
  + **List Launched Flows**

### Change

**Armis**: Version 15.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**Lastline**: Version 9.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Analysis Results**

### Change

**McAfee Mvision EPO**: Version 11.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Endpoint**

### Change

**Office 365 Cloud App Security**: Version 26.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get IP related activities**
  + **Get User related activities**

### Change

**SSL Labs**: Version 11.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Analyse Entity**

### Change

**Qualys VM**: Version 25.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Host**
  + **List Endpoint Detections**

### Change

**Exchange**: Version 123.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Account Out Of Facility Settings**
  + **Send Email And Wait**

### Change

**Microsoft Defender ATP**: Version 31.0

* Added Graph API V2 version support to the following actions:

  + **Get User Related Alerts**
  + **List Alerts**
  + **Ping**
  + **Update Alert**
* Deprecated the following actions:

  + **Get File Related Alerts**
  + **Get Machine Related Alerts**
* Added Graph API V2 version support to the following connector:

  (REGRESSIVE) The connector must be updated by April 10, 2026.

  **Note:** You must update ontology mapping. Alerts created with the new API have a different
  structure and require additional permissions. We recommend using
  **Microsoft 365 Defender - Incidents Connector** as a replacement.
  + **Microsoft Defender ATP Connector V2**
* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Execute Live Response Command**
  + **Get File Related Alerts**
  + **Get File Related Machines**
  + **Get Machine Logon Users**
  + **Get Machine Recommendations**
  + **Get Machine Related Alerts**
  + **Get Machine Vulnerabilities**
  + **Get User Related Alerts**

### Change

**Cisco AMP**: Version 23.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Computer Info**
  + **Get Computers By File Hash**
  + **Get Computers By File Name**
  + **Get Computers By Network Activity (Ip)**
  + **Get Computers By Network Activity (URL)**
  + **Isolate Machine**
  + **Unisolate Machine**

### Change

**HaveIBeenPwned**: Version 10.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Check Account**

### Change

**Symantec Blue Coat ProxySG**: Version 7.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Block Entities**
  + **Enrich Entities**

### Change

**Cybereason**: Version 25.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Get Sensor Details**
  + **Is Probe Connected**

### Change

**Cofense Triage**: Version 21.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **EnrichURL**
  + **Get Domain Details**
  + **Get Threat Indicator Details**

### Change

**Slack**: Version 30.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Send Advanced Message**
  + **Send Message**

### Change

**IPVoid**: Version 12.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Ip Reputation**

### Change

**RSA NetWitness EDR**: Version 9.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Endpoint**
  + **Get IOC Details**

### Change

**Microsoft Intune**: Version 8.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Managed Device**

### Change

**Trend Micro DDAN**: Version 6.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Submit File**
  + **Submit File URL**

### Change

**Tenable.io**: Version 17.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **List Endpoint Vulnerabilities**

### Change

**JoeSandbox**: Version 11.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Search Hash**
  + **Search Url**

### Change

**Endgame**: Version 15.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Network Survey**
  + **System Survey**

### Change

**ThreatQ**: Version 19.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich CVE**
  + **Enrich Email**
  + **Enrich Hash**
  + **Enrich IP**
  + **Enrich URL**
  + **Get Indicator Details**
  + **Get Malware Details**
  + **Link Entities**
  + **Link Entities To Object**
  + **List Entity Related Objects**
  + **Update Indicator Score**
  + **Update Indicator Status**

### Change

**RSA NetWitness Platform**: Version 17.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Endpoint**
  + **Enrich File**
  + **Query NetWitness For Events Around Host**
  + **Query NetWitness For Events Around IP**
  + **Query NetWitness For Events Around User**

### Change

**McAfee TIEDXL**: Version 9.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get File Reputation**

### Change

**Symantec Endpoint Protection 14**: Version 21.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **GetSystemInfo**

### Change

**FireEye AX**: Version 9.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Submit URL**

### Change

**Splash**: Version 7.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**MalShare**: Version 11.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Hash**

### Change

**Elastica CloudSOC**: Version 8.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get User Activities**

### Change

**Amazon Macie**: Version 10.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Findings**

### Change

**CiscoUmbrella**: Version 19.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Domain Security Info**
  + **Get Domain Status**
  + **Get Whois**
  + **Is Domain In Cisco Popularity List**

### Change

**SCCM**: Version 21.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Get Computer Properties**
  + **Get Login History**

### Change

**Web Risk**: Version 4.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Submit Entities**

### Change

**DShield**: Version 8.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Ip Info**

### Change

**Tenable Security Center**: Version 22.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich IP**
  + **Get Related Assets**
  + **Get Vulnerabilities for IP**

### Change

**ServiceNow**: Version 63.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **List Records Related To User**

### Change

**McAfee EPO**: Version 37.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Compare Server and Agent DAT**
  + **Get Agent Information**
  + **Get Dat Version**
  + **Get Endpoint Events**
  + **Get Events For Hash**
  + **Get Host IPS Status**
  + **Get Host Network IPS Status**
  + **Get Last Communication Time**
  + **Get McAfee Epo Agent Version**
  + **Get System Information**
  + **Get Virus Engine Agent Version**
  + **Run Full Scan**
  + **Update Mcafee Agent**

### Change

**RSA NetWitness**: Version 20.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Query NetWitness For Events Around Host**
  + **Query NetWitness For Events Around IP**
  + **Query NetWitness For Events Around User**

### Change

**Axonius**: Version 7.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Add Note**
  + **Enrich Entities**

### Change

**Automox**: Version 8.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Execute Device Command**
  + **Execute Policy**

### Change

**Cylance**: Version 19.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Get Threat**
  + **Get Threat Devices**
  + **Get Threat Download Link**

### Change

**Anomali**: Version 15.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **GetThreatInfo**

### Change

**TruSTAR**: Version 9.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**PhishingInitiative**: Version 12.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Url Status**

### Change

**Digital Shadows**: Version 12.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **EnrichCVE**
  + **EnrichHash**
  + **EnrichIP**
  + **EnrichURL**

### Change

**iBoss**: Version 14.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **URL Lookup**

### Change

**Google Cloud IAM**: Version 19.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Get Service Account IAM Policy**
  + **Rotate Service Account Keys**
  + **Set Service Account IAM Policy**

### Change

**Sumo Logic Cloud SIEM**: Version 13.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Search Entity Signals**

### Change

**Microsoft Teams**: Version 37.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Create Chat**
  + **Send User Message**

### Change

**FortiAnalyzer**: Version 12.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**Sophos**: Version 21.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Get Events Log**
  + **Get Services Status**

### Change

**Palo Alto Cortex XDR**: Version 27.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Scan Endpoint**

### Change

**Cisco Threat Grid**: Version 18.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Submissions**

### Change

**Intezer**: Version 14.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Submit Hash**

### Change

**Recorded Future**: Version 22.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich CVE**
  + **Enrich Hash**
  + **Enrich Host**
  + **Enrich IP**
  + **Enrich IOC**
  + **Enrich URL**

### Change

**Gmail**: Version 9.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Search For Emails**
  + **Wait For Thread Reply**

### Change

**Illusive Networks**: Version 7.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Run Forensic Scan**

### Change

**VirusTotal**: Version 42.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Domain Report**
  + **Scan Hash**
  + **Scan IP**
  + **Scan URL**
  + **Upload And Scan Files**

### Change

**Anomali ThreatStream**: Version 15.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**ThreatConnect**: Version 17.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**Azure Active Directory**: Version 26.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Host**
  + **Enrich User**
  + **Get Manager Contact Details**
  + **List Users**
  + **List User's Groups Membership**
  + **Revoke User Session**

### Change

**Splunk**: Version 65.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Host Events**

### Change

**Attivo**: Version 10.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**Cisco ISE**: Version 16.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Add Endpoint To Endpoint Identity Group**

### Change

**DeepSight**: Version 11.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Scan Domain**
  + **Scan Email**
  + **Scan File Name**
  + **Scan Hash**
  + **Scan IP**
  + **Scan URL**

### Change

**Symantec Email Security Cloud**: Version 5.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Block Entities**

### Change

**GSuite**: Version 26.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Get Extension Details**
  + **Get Group Details**
  + **Get Host Browser Details**
  + **List Group Privileges**
  + **List User Privileges**
  + **Revoke User Session**
  + **Search User Activity Events**

### Change

**SymantecESCC**: Version 9.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**Google Cloud Compute**: Version 17.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**FireEye HX**: Version 23.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Host Alert Groups**
  + **Get Host Info**
  + **Get List of File Acquisitions For Host**
  + **Is Contain Malware Alerts**

### Change

**Rapid7 InsightVm**: Version 16.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Asset**

### Change

**McAfee Mvision EDRV2**: Version 5.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Create Investigation**

### Change

**HCL BigFix Inventory**: Version 5.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**SiemplifyUtilities**: Version 29.0

* Added support for a custom delimiter in the following action:

  + **Query Joiner**

### Change

**Nmap**: Version 4.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Scan Entities**

### Change

**VMware Carbon Black Enterprise EDR**: Version 10.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Hash**
  + **Get Events Associated With Process by Process Guide**
  + **Process Search**

### Change

**Outpost24**: Version 8.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**PassiveTotal**: Version 14.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **WhoIs Address Reputation**
  + **Whois Host Reputation**
  + **WhoIs Scan Address**
  + **WhoIs Scan Domain**

### Change

**Carbon Black Defense**: Version 12.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Device Info**
  + **Get Events**
  + **Get Processes**

### Change

**QRadar**: Version 67.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Similar Events Query**
  + **Similar Flows Query**

### Change

**SentinelOneV2**: Version 49.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Create Hash Blacklist Record**
  + **Create Hash Exclusion Record**
  + **Get Agent Status**
  + **Get Application List For Endpoint**
  + **Get Events For Endpoint Hours Back**
  + **Get Group Details**
  + **Get Hash Reputation**

### Change

**Zscaler**: Version 13.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Sandbox Report**
  + **Lookup Entity**

### Change

**McAfee Mvision EDR**: Version 11.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Endpoint**

### Change

**Tanium**: Version 19.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Delete File**
  + **Enrich Entities**
  + **List Endpoint Events**
  + **Quarantine Endpoint**

### Change

**VMware Carbon Black Endpoint Standard Live Response**: Version 10.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Create Memdump**
  + **Delete File**
  + **Delete File from Cloud Storage**
  + **Download File**
  + **Execute File**
  + **Kill Process**
  + **List Files**
  + **List Files in Cloud Storage**
  + **List Processes**
  + **Put File**

### Change

**VSphere**: Version 12.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Vm By Ip**

### Change

**Nozomi Networks**: Version 10.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**Active Directory**: Version 41.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich entities**
  + **Get Manager Contact Details**

### Change

**Talos**: Version 20.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Reputation**
  + **WhoIs**

### Change

**Check Point Threat Reputation**: Version 8.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get File Hash Reputation**
  + **Get Host Reputation**
  + **Get IP Reputation**

### Change

**Zabbix**: Version 16.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Execute Script**

### Change

**FireEye Helix**: Version 19.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Add Entities To a List**

### Change

**Malware Domain List**: Version 11.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Check URL**

### Change

**AlienVault USM Appliance**: Version 26.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Assets**
  + **Enrich Vulnerabilities**

### Change

**Alexa**: Version 9.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get URL Rank**

### Change

**AWS GuardDuty**: Version 12.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get a Trusted IP List**
  + **Get Detector Details**
  + **Get Threat Intelligence Set Details**

### Change

**HTTP**: Version 15.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get URL Data**

### Change

**BlueLiv**: Version 13.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **List Entity Threats**

### Change

**Azure AD Identity Protection**: Version 9.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**Carbon Black Response**: Version 39.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Binary**
  + **Enrich Process**
  + **Get System Info**
  + **Hosts By Process**
  + **List Processes**

### Change

**Falcon Sandbox**: Version 21.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Hash Scan Report**
  + **Scan URL**
  + **Submit File**

### Change

**CSV**: Version 41.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **CSV Search by Entity**
  + **CSV Search by String**

### Change

**URLVoid**: Version 14.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get domain reputation**

### Change

**Harmony Mobile**: Version 7.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**Cloudflare**: Version 8.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Add URL To Rule List**

### Change

**Carbon Black Protection**: Version 13.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Analyze File**

### Change

**Jira**: Version 56.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Search Users**

### Change

**Microsoft Graph Mail Delegated**: Version 17.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Mailbox Account Out Of Facility Settings**

### Change

**Trend Vision One**: Version 9.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **Execute Custom Script**
  + **Isolate Endpoint**
  + **Submit File**
  + **Submit URL**
  + **Unisolate Endpoint**

### Change

**Internet Storm Center**: Version 6.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**AlienVaultTI**: Version 14.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enriches Entities**

### Change

**Google Threat Intelligence**: Version 14.0

* Migrated the following connector to new API endpoints:

  **Note:** Duplicate notifications may occur temporarily during the transition.
  + **Google Threat Intelligence - Livehunt Connector**

### Change

**Shodan**: Version 17.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Get Ip Info**

### Change

**Cisco Vulnerability Management**: Version 3.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **List Asset Vulnerabilities**

### Change

**ForeScout CounterACT**: Version 6.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**McAfee ESM**: Version 46.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get Similar Events**
  + **Send Entity Query To ESM**

### Change

**LogRhythm**: Version 23.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **List Entity Events**

### Change

**Mandiant ASM**: Version 13.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Search ASM Entities**

### Change

**Ivanti Endpoint Manager**: Version 10.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **List Endpoint Vulnerabilities**

### Change

**Cuckoo**: Version 14.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Detonate Url**

### Change

**IntSights**: Version 27.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Search IOCs**

### Change

**Vectra**: Version 13.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Endpoint**

### Change

**McAfee ATD**: Version 17.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Submit URL**

### Change

**FortinetFortiSIEM**: Version 10.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**ThreatCrowd**: Version 9.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **EnrichEntities**

### Change

**APIVoid**: Version 14.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Get domain reputation**
  + **Get Ip Reputation**
  + **Get Screenshot**
  + **Get URL Reputation**
  + **Verify Email**

### Change

**McAfee Mvision EPOV2**: Version 8.0

* Introduced light theme support for the predefined widget of the following
  action:

  + **Enrich Endpoint**

### Change

**VMRay**: Version 19.0

* Introduced light theme support for predefined widgets of the following
  actions:

  + **Scan Hash**
  + **Scan URL**

### Change

**Google Chronicle**: Version 81.0

* Added support for CIDR matching to the following action:

  + **Is Value In Reference List**

---
## 2026-04-01

### Feature

**Microsoft 365 Defender**: Version 26.0

* The following new job has been added:

  + **Sync Alerts**

### Feature

**SentinelOneV2**: Version 48.0

* The following new job has been added:

  + **Sync Alerts**

### Change

**Microsoft Teams**: Version 36.0

* Optimized user lookup logic for the following actions:

  + **Add Users To Channel**
  + **Create Chat**

### Change

**Akamai**: Version 6.0

* Updated the JSON results of the following actions:

  + **Add Items To Client List**
  + **Remove Items From Client List**

### Change

Source code is now publicly available on [GitHub](https://github.com/chronicle/content-hub)
for the following integrations:

* **CyberX**: Version 6.0
* **JuniperVSRX**: Version 11.0
* **McAfee NSM**: Version 11.0
* **Micro Focus ITSMA**: Version 7.0
* **Portnox**: Version 9.0
* **ReversingLabs A1000**: Version 10.0
* **Stealthwatch V6.10**: Version 6.0
* **Symantec Content Analysis**: Version 7.0

### Change

**Azure Active Directory**: Version 25.0

* Added the ability to fetch last login time information to the following
  actions:

  + **Enrich User**
  + **Get Manager Contact Details**

---
## 2026-03-25

### Feature

**Azure API**: Version 3.0

* Added predefined widget to the following action:

  + **Ping**

### Feature

**Microsoft Graph Security**: Version 26.0

* Added predefined widget to the following action:

  + **Get Incident**

### Feature

**Google Cloud IAM**: Version 20.0

* The following new action has been added:

  + **Rotate Service Account Keys**

### Feature

**Siemplify**: Version 106.0

* The following new action has been added:

  + **Search Cases**
* Added predefined widget to the following action:

  + **Search Cases**

### Feature

**Microsoft Defender ATP**: Version 30.0

* The following new actions have been added:

  + **Get Machine Recommendations**
  + **Get Machine Vulnerabilities**
  + **Get User Related Alerts**

### Change

**BitSight**: Version 12.0

* IIntroduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Company Details**

### Change

**RSA NetWitness Platform**: Version 16.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Update Incident**

### Change

**CyberArk Credential Provider**: Version 3.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Application Password Value**
  + **Run CLI Application Password SDK Command**

### Change

**CrowdStrike Falcon**: Version 75.0

* Added offline queueing support to the following actions:

  + **Execute Command**
  + **Run Script**

### Change

**MobileIron**: Version 6.0

* **Integration**: The integration's source code is now publicly available on
  [Github](https://github.com/chronicle/content-hub).

### Change

**FireEye HX**: Version 22.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Acknowledge Alert Groups**
  + **Get Indicator**

### Change

**Anomali ThreatStream**: Version 14.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Related Associations**
  + **Get Related Entities**

### Change

**HashiCorp Vault**: Version 6.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Generate AWS Credentials**
  + **List AWS Roles**
  + **List Key-Value Secret Keys**
  + **Read Key-Value Secret**

### Change

**AWS WAF**: Version 11.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Rule Groups**
  + **List Web ACLs**

### Change

**Microsoft Graph Security**: Version 26.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Alert**

### Change

**JoeSandbox**: Version 10.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Detonate File**

### Change

**ThreatQ**: Version 18.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Attribute**
  + **Add Source**
  + **Create Adversary**
  + **Create Event**
  + **Create Indicator**
  + **Create Object**
  + **Link Objects**

### Change

**Symantec Endpoint Security Complete Cloud**: Version 8.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Symantec Endpoint Security Complete Cloud**

### Change

**EmailV2**: Version 40.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Delete Email**
  + **Forward Email**
  + **Save Email Attachments To Case**
  + **Send Email**
  + **Send Thread Reply**
  + **Wait for Email from User**

### Change

**Cofense Triage**: Version 20.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Tags To Report**
  + **Categorize Report**
  + **Download Report Email**
  + **Download Report Preview**
  + **Get Report Reporters**

### Change

**CA Service Desk Manager**: Version 26.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Wait For Status Change**

### Change

**Microsoft Defender ATP**: Version 30.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Update Alert**

### Change

**Akamai**: Version 5.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Activate Client List**
  + **Activate Network List**
  + **Add Items To Network List**
  + **Remove Items From Network List**

### Change

**SSH**: Version 20.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Connections**
  + **List iptables Rules**
  + **List Processes**
  + **Run Command**

### Change

**Microsoft Azure Sentinel**: Version 62.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Comment to Incident**
  + **Create Alert Rule**
  + **Create Custom Hunting Rule**
  + **Get Alert Rule Details**
  + **Get Custom Hunting Rule Details**
  + **Get Incident Statistic**
  + **Update Alert Rule**
  + **Update Custom Hunting Rule**
  + **Update Incident Details**
  + **Update Incident Details v2**
  + **Update Incident Labels**
  + **Update Incident Labels v2**

### Change

**Google Cloud Compute**: Version 16.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add IP To Firewall Rule**
  + **Add Network Tags**
  + **Delete Instance**
  + **Execute VM Patch Job**
  + **Remove IP From Firewall Rule**
  + **Remove Network Tags**
  + **Start Instance**
  + **Stop Instance**
  + **Update Firewall Rule**

### Change

**Microsoft Graph Mail Delegated**: Version 16.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Forward Email**
  + **Save Email to the Case**
  + **Send Email**
  + **Send Email HTML**
  + **Send Thread Reply**
  + **Send Vote Email**
  + **Wait For Email From User**
  + **Wait For Vote Email Results**

### Change

**Extrahop**: Version 8.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Update Detection**

### Change

**Palo Alto Cortex XDR**: Version 26.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Incident Details**
  + **Query**

### Change

**Recorded Future**: Version 21.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Alert Details**

### Change

**VSphere**: Version 11.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get System Info**

### Change

**FireEye CM**: Version 14.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add IOC Feed**
  + **Download Alert Artifacts**

### Change

**Tenable.io**: Version 16.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Scan Endpoints**

### Change

**Remote Agent Utilities**: Version 7.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Serialize A File**

### Change

**FireEye Helix**: Version 18.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Archive Search**
  + **Get Alert Details**
  + **Index Search**

### Change

**Okta**: Version 16.0

* **Integration**: Added support for OAuth authentication.

### Change

**Office 365 CloudApp Security**: Version 25.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add IP To IP Address Range**
  + **Create IP Address Range**
  + **Remove IP From IP Address Range**

### Change

**Palo Alto Prisma Cloud**: Version 6.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Enrich Assets**

### Change

**Google Cloud Armor**: Version 5.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add a Rule to a Security Policy**
  + **Create a Security Policy**
  + **Update a Security Policy**

### Change

**Redis**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add To List**
  + **Get List**

### Change

**Carbon Black Response**: Version 38.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get FileMod Data For Process**
  + **Get Process Tree Data**

### Change

**Microsoft Graph Mail**: Version 39.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Forward Email**
  + **Save Email to the Case**
  + **Send Email**
  + **Send Email HTML**
  + **Send Thread Reply**
  + **Send Vote Email**
  + **Wait For Email From User**
  + **Wait For Vote Email Results**

### Change

**NessusScanner**: Version 12.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Scan Templates**

### Change

**Atlassian Confluence Server**: Version 5.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Child Pages**
  + **Get Page by ID**
  + **Get Page Comments**
  + **List Pages**

### Change

**Slack**: Version 29.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Build Block**
  + **Create Channel**
  + **Get User Details**
  + **Get User Details By Id**
  + **Rename Channel**
  + **Wait For Reply**
  + **Wait For Reply With Webhook**

### Change

**McAfee ATD**: Version 16.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Report**
  + **Submit File**

### Change

**Symantec ICDX**: Version 9.0

* **Integration**: The integration's source code is now publicly available on
  [Github](https://github.com/chronicle/content-hub).

### Change

**McAfee NSM**: Version 10.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Alert Info Data**

### Change

**Cloudflare**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Firewall Rule**
  + **Create Rule List**
  + **Update Firewall Rule**

### Change

**Rapid7 InsightIDR**: Version 12.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Saved Query**
  + **Set Investigation Assignee**
  + **Set Investigation Status**
  + **Update Investigation**

### Change

**Exchange Extension Pack**: Version 13.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Domains to Exchange-Siemplify Mail Flow Rules**
  + **Add Senders to Exchange-Siemplify Mail Flow Rule**
  + **Purge Compliance Search Results**
  + **Remove Domains from Exchange-Siemplify Mail Flow Rules**
  + **Remove Senders from Exchange-Siemplify Mail Flow Rules**
  + **Run Compliance Search**

### Change

**CSV**: Version 40.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Save Json To CSV**

### Change

**Mandiant ASM**: Version 12.0

* IIntroduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Update Issue**

### Change

**Shodan**: Version 16.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **DNS Resolve**
  + **DNS Reverse**
  + **Get Api Info**

### Change

**Google Kubernetes Engine**: Version 9.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Operation Status**
  + **List Clusters**
  + **List Node Pools**
  + **List Operations**
  + **Set Cluster Addons**
  + **Set Cluster Labels**
  + **Set Node Autoscaling**
  + **Set Node Count**
  + **Set Node Pool Management**

### Change

**SiemplifyUtilities**: Version 28.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Delete File**
  + **Filter JSON**
  + **Get Deployment URL**
  + **List Operations**
  + **Parse EML to JSON**

### Change

**Anomali**: Version 14.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Related Associations**

### Change

**Reversinglabs A1000**: Version 9.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Upload File**

### Change

**CyberArk PAM**: Version 9.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Account Password Value**

### Change

**Jira**: Version 55.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Alert Issue**
  + **Create Issue**
  + **List Issues**
  + **Update Issue**

### Change

**Ivanti Endpoint Manager**: Version 9.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Query**
  + **List Column Set Fields**
  + **List Column Sets**
  + **List Delivery Methods**
  + **List Packages**
  + **List Queries**

### Change

**Check Point Firewall**: Version 15.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add a SAM Rule**
  + **Remove SAM Rule**
  + **Run Script**

### Change

**Any.Run**: Version 11.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **AnalyzeFile**
  + **AnalyzeFileURL**
  + **AnalyzeURL**

### Change

**Carbon Black Protection**: Version 12.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get System Info**

### Change

**LogRhythm**: Version 22.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Note To Case**
  + **Create Cas**
  + **Download Case Files**
  + **Update Case**

### Change

**BMC Remedy ITSM**: Version 12.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Incident**
  + **Create Record**
  + **Wait For Incident Fields Update**
  + **Wait For Record Fields Update**

### Change

**AlienVault USM Anywhere**: Version 35.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Alarm Details**

### Change

**Zoho Desk**: Version 11.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Comment To Ticket**
  + **Create Ticket**
  + **Update Ticket**

### Change

**AWS GuardDuty**: Version 11.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create a Detector**
  + **Create a Trusted IP List**
  + **Create Threat Intelligence Set**
  + **Get all Trusted IP lists**
  + **Get Finding Details**
  + **List Detectors**
  + **List Findings for a Detector**
  + **List Threat Intelligence Sets**

### Change

**AWS Elastic Compute Cloud (EC2)**: Version 10.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Instances**
  + **List Security Groups**
  + **Take Snapshot**

### Change

**Cybereason**: Version 24.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Malop**
  + **List Malop Processes**
  + **List Reputation Items**

### Change

**Rapid7 InsightVm**: Version 15.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Scan Results**
  + **Launch Scan**

### Change

**Cisco AMP**: Version 22.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Group**
  + **Get File Lists By Policy**
  + **Get Groups**
  + **Get Policies**

### Change

**Trend Micro Cloud App Security**: Version 11.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Enrich Entities**

### Change

**CiscoUmbrella**: Version 18.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Malicious Domains**

### Change

**Solar Winds Orion**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Enrich Endpoint**
  + **Execute Entity Query**
  + **Execute Query**

### Change

**Tenable Security Center**: Version 21.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add IP To IP List Asset**
  + **Create IP List Asset**
  + **Get Report**
  + **Get Scan Results**
  + **Run Asset Scan**

### Change

**Gmail**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Forward Email**
  + **Save Email To The Case**
  + **Send Email**
  + **Send Thread Reply**

### Change

**FireEye AX**: Version 8.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Appliance Details**

### Change

**FortiAnalyzer**: Version 11.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Comment To Alert**
  + **Update Alert**

### Change

**WMI**: Version 14.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **GetSystemInfo**

### Change

**Google Chat**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Send Advanced Message**
  + **Send Message**

### Change

**SentinelOneV2**: Version 47.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Device Control Rule**
  + **Download Threat File**
  + **Enrich Endpoint**
  + **Get System Status**
  + **Update Alert**
  + **Update Device Control Rule**

### Change

**Google Translate**: Version 6.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Translate Text**
  + **List Languages**

### Change

**Exchange**: Version 122.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Save Mail Attachments To The Case**
  + **Send Mail**
  + **Send Thread Reply**
  + **Send Vote Mail**
  + **Wait for mail from user**
  + **Wait for Vote Mail Results**

### Change

**Symantec ATP**: Version 12.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Incident Comments**

### Change

**Azure API**: Version 3.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Execute HTTP Request**

### Change

**Tanium**: Version 18.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Question**
  + **Download File**
  + **Get Question Results**

### Change

**Site24x7**: Version 6.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Generate Refresh Token**

### Change

**ConnectWise**: Version 21.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Attachment To Ticket**
  + **Get Ticket**

### Change

**Cisco Threat Grid**: Version 17.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Upload Sample**

### Change

**Zendesk**: Version 12.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Ticket Details**
  + **Search Tickets**

### Change

**Symantec Endpoint Protection 12**: Version 15.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **GetReport**

### Change

**ServiceNow**: Version 62.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Comment To Record**
  + **Add Parent Incident**
  + **Create Alert Incident**
  + **Create Incident**
  + **Create Record**
  + **Get Incident**
  + **Get Oauth Token**
  + **Get Record Details**
  + **Update Incident**
  + **Update Record**
  + **Wait For Field Update**
  + **Wait For Status Update**

### Change

**Cuckoo**: Version 13.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Detonate File**
  + **Get Report**

### Change

**Sophos**: Version 20.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Alert Actions**

### Change

**IronPort**: Version 15.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get All Recipients By Sender**
  + **Get All Recipients By Subject**
  + **Get Report**

### Change

**Lastline**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Search Analysis History**
  + **Submit File**
  + **Submit URL**

### Change

**F5 BIG-IP iControl API**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add IP To Address List**
  + **Add IP To Data Group**
  + **Add Port To Port List**
  + **Create Address List**
  + **Create Data Group**
  + **Create iRule**
  + **Create Port List**
  + **Remove IP From Address List**
  + **Remove IP From Data Group**
  + **Remove Port From Port List**
  + **Update iRule**

### Change

**Palo Alto Panorama**: Version 35.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Ips to group**
  + **Block ips in policy**
  + **Block Urls**
  + **Edit Blocked Applications**
  + **Get Blocked Applications**
  + **Remove Ips from group**
  + **Unblock ips in policy**
  + **Unblock Urls**

### Change

**Cynet**: Version 12.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Hash Query**
  + **Remediation Status**

### Change

**Trend Vision One**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Email**
  + **Update Workbench Alert**

### Change

**MalShare**: Version 10.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Upload File**

### Change

**Tor**: Version 9.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Is Exit Node**

### Change

**Qualys VM**: Version 24.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Download Report**
  + **List Ips**

### Change

**BMC Helix Remedyforce**: Version 17.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Record**
  + **Wait For Fields Update**

### Change

**AlienVault USM Appliance**: Version 25.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get PCAP Files For Events**

### Change

**Service Desk Plus**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Request**
  + **Get Request**
  + **Update Request**

### Change

**FireEye NX**: Version 11.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Download Alert Artifacts**

### Change

**Intezer**: Version 13.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Alert**
  + **Submit Alert**
  + **Submit File**
  + **Submit Suspicious Email**

### Change

**MISP**: Version 37.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Event**
  + **Create File Misp Object**
  + **Create IP-Port Misp Object**
  + **Create network-connection Misp Object**
  + **Create Virustotal-Report Object**
  + **Download File**
  + **Publish Event**
  + **Unpublish Event**
  + **Upload File**

### Change

**Palo Alto Next Gen Firewall**: Version 28.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Ips to group**
  + **Block ips in policy**
  + **Block Urls**
  + **Edit Blocked Applications**
  + **Get Blocked Applications**
  + **Remove Ips from group**
  + **Unblock ips in policy**
  + **Unblock Urls**

### Change

**Illusive Networks**: Version 6.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Deceptive Items**

### Change

**Freshworks Freshservice**: Version 18.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Agent**
  + **Deactivate Agent**
  + **Update Agent**

### Change

**Splunk**: Version 64.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Submit Event**

### Change

**AlgoSec**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Allow IP**
  + **Block IP**
  + **Wait for Change Request Status Update**

### Change

**Salesforce**: Version 17.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Case**
  + **Search Records**

### Change

**RSA Archer**: Version 14.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Incident Journal Entry**
  + **Create Incident**
  + **Get Incident Details**
  + **Update Incident**

### Change

**QRadar**: Version 66.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **QRadar AQL Search**
  + **QRadar Simple AQL Search**
  + **Update Offense**

### Change

**Mimecast**: Version 15.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Create Block Sender Policy**

### Change

**Sumo Logic Cloud SIEM**: Version 12.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Tags To Insight**
  + **Add Comment To Insight**
  + **Update Insight**

### Change

**ArcSight**: Version 45.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Resources**

### Change

**Microsoft Teams**: Version 35.0

* **Integration**: Updated dependencies.
* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Channel**
  + **Create Channel**
  + **Send Chat Message**
  + **Send Message Reply**
  + **Wait For Reply**

### Change

**Service Desk Plus V3**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Note**
  + **Add Note And Wait For Reply**
  + **Close Request**
  + **Create Alert Request**
  + **Create Request**
  + **Create Request - Dropdown Lists**
  + **Get Request**
  + **Update Request**
  + **Wait For Field Update**
  + **Wait For Status Update**

### Change

**AWS CloudWatch**: Version 9.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Log Group**
  + **Create Log Stream**

### Change

**Endgame**: Version 14.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Investigation Details**

### Change

**Falcon Sandbox**: Version 20.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Wait For Job and Fetch Report**

### Change

**Google Cloud Recommender**: Version 10.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Apply IAM Recommendations**

### Change

**HTTP Rest API**: Version 14.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Data**
  + **Post Data**

### Change

**Google Threat Intelligence**: Version 13.0

* Improved loading for predefined widgets of the following actions:

  + **Enrich Entities**
  + **Enrich IOC**
* Removed the usage of a deprecated API endpoint and the `Retrieve AI Summary`
  parameter from the following action:

  + **Submit File**

### Change

**IntSights**: Version 26.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Download Alert CSV**

---
## 2026-03-18

### Feature

**Microsoft Graph Mail**: Version 37.0

* A new predefined widget has been added to the following action:

  + **Delete Email**

### Feature

**CrowdStrike Falcon**: Version 73.0

* The following new action has been added:

  + **Hide Hosts**

### Feature

**Endgame**: Version 73.0

* New predefined widgets have been added to following actions:

  + **Get Endpoints**
  + **Get Host Isolation Config**
  + **Hunt File**
  + **Hunt IP**
  + **Hunt Process**
  + **Hunt Registry**
  + **Hunt User**
  + **List Investigations**

### Feature

**Microsoft Graph Security**: Version 24.0

* A new predefined widget has been added to the following action:

  + **List Incidents**

### Change

**Azure Security Center**: Version 14.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Regulatory Standards**
  + **List Regulatory Standard Controls**

### Change

**Zoho Desk**: Version 9.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Ticket Details**

### Change

**Stellar Cyber Starlight**: Version 17.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Advanced Search**
  + **Simple Search**

### Change

**Siemplify ThreatFuse**: Version 17.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Related Associations**
  + **Get Related Domains**
  + **Get Related Email Addresses**
  + **Get Related Hashes**
  + **Get Related IPs**
  + **Get Related URLs**
  + **Submit Observables**

### Change

**Devo**: Version 10.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Advanced Query**
  + **Simple Query**

### Change

**AWS CloudWatch**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Log Groups**
  + **List Log Streams**
  + **Search Log Events**

### Change

**ZScaler**: Version 11.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Url Categories**

### Change

**Google Workspace**: Version 24.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Members To Group**
  + **Block Extension**
  + **Create Group**
  + **Create OU**
  + **Create User**
  + **Delete Extension**
  + **List Group Members**
  + **List OU Of Account**
  + **List Users**
  + **Update OU**
  + **Update User**

### Change

**Azure Active Directory**: Version 23.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Groups**
  + **List Members in the Group**

### Change

**Trend Micro Cloud App Security**: Version 9.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Entity Email Search**

### Change

**Tanium**: Version 16.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Task Details**
  + **List Connections**

### Change

**Intezer**: Version 11.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Detonate File**
  + **Detonate Hash**
  + **Detonate URL**
  + **Get File Report**
  + **Get URL Report**
  + **Index File**

### Change

**RSA NetWitness**: Version 18.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Run General Query**

### Change

**MongoDB**: Version 8.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Free Query**

### Change

**Exchange**: Version 120.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Block Sender by Message ID**
  + **Delete Mail**
  + **Download Attachments**
  + **Extract EML Data**
  + **List Exchange-Siemplify Inbox Rules**
  + **Move Mail To Folder**
  + **Search Mails**
  + **Unblock Sender by Message ID**

### Change

**ThreatQ**: Version 16.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Events**
  + **List Related Objects**

### Change

**RSA NetWitness Platform**: Version 14.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Run General Query**

### Change

**Carbon Black Response**: Version 36.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Binary Free Query**
  + **Process Free Query**

### Change

**Symantec Endpoint Protection**: Version 19.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Report And Enrich**
  + **GetReport**
  + **ListEndpoints**
  + **ListGroups**

### Change

**AlienVault USM Anywhere**: Version 33.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Events**

### Change

**Mandiant Digital Threat Monitoring**: Version 5.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Update Alert**

### Change

**FireEye CM**: Version 12.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Download Custom Rules File**
  + **Download Quarantined Email**
  + **List IOC Feeds**
  + **List Quarantined Emails**

### Change

**Google Threat Intelligence**: Version 11.0

* Updated `is_suspicious` and `is_risky` logic handling in the following
  actions:

  + **Enrich Entities**
  + **Submit File**

### Change

**Shodan**: Version 14.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Search**
  + **SearchForExploits**

### Change

**Snowflake**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Custom Query**
  + **Execute Simple Query**

### Change

**Proofpoint Threat Protection**: Version 2.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Allow List Entries**
  + **Get Block List Entries**

### Change

**Vectra**: Version 11.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Triage Rule Details**

### Change

**MSSQL**: Version 18.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **RunSQLQuery**

### Change

**Rapid7 InsightVm**: Version 13.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Scans**

### Change

**ServiceNow**: Version 60.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Attachment**
  + **Download Attachments**
  + **Get Child Incident Details**
  + **Get CMDB Record Details**
  + **Get User Details**
  + **List CMDB Records**
  + **List Record Comments**
  + **Wait For Comments**

### Change

**CiscoUmbrella**: Version 16.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Top Domains**

### Change

**RSA NetWitness EDR**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add IP To Blacklist**
  + **Add URL To Blacklist**

### Change

**Microsoft 365 Defender**: Version 24.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Custom Query**
  + **Execute Entity Query**
  + **Execute Query**

### Change

**Easy Vista**: Version 6.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get EasyVista Ticket**

### Change

**Sumologic**: Version 18.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Search**

### Change

**Symantec Endpoint Security Complete Cloud**: Version 6.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Device Groups**

### Change

**Google Rapid Response (GRR)**: Version 9.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Hunt Details**
  + **List Hunts**
  + **Start a Hunt**
  + **Stop a Hunt**

### Change

**TruSTAR**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Related IOCs**
  + **Get Related Reports**
  + **List Enclaves**

### Change

**FireEye AX**: Version 6.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Submit File**

### Change

**McAfee ATD**: Version 14.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Analyzer Profiles**

### Change

**Mimecast**: Version 13.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Advanced Archive Search**
  + **Simple Archive Search**

### Change

**Microsoft Azure Sentinel**: Version 60.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Alert Rules**
  + **List Custom Hunting Rules**
  + **List Incidents**
  + **Run Custom Hunting Rule Query**
  + **Run KQL Query**

### Change

**ElasticSearch**: Version 42.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Advanced ES Search**
  + **DSL Search**
  + **Simple ES Search**

### Change

**FireEye HX**: Version 20.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Alert Group Details**
  + **Get Alerts**
  + **Get Alerts in Alert Group**
  + **Get Indicators**

### Change

**FortiGate**: Version 18.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Address Groups**
  + **List Policies**

### Change

**CBProtection**: Version 10.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Find File**

### Change

**BlueLiv**: Version 11.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Add Comment to a Threat**

### Change

**MISP**: Version 35.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Attribute**
  + **Add Sighting to an Attribute**
  + **Add Tag to an Attribute**
  + **Add Tag to an Event**
  + **Create Url Misp Object**
  + **Delete an Attribute**
  + **Delete an Event**
  + **List Event Objects**
  + **List Sightings of an Attribute**
  + **Remove Tag from an Attribute**
  + **Remove Tag from an Event**

### Change

**Exchange Extension Pack**: Version 11.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Fetch Compliance Search Results**
  + **List Exchange-Siemplify Mail Flow Rules**

### Change

**Google Cloud Storage**: Version 13.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Download an Object From a Bucket**
  + **Get a Bucket's Access Control List**
  + **List Bucket Objects**
  + **List Buckets**
  + **Upload an Object To a Bucket**

### Change

**Microsoft Graph Mail Delegated**: Version 14.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Delete Email**
  + **Download Attachments from Email**
  + **Extract Data from Attached EML**
  + **Move Email To Folder**
  + **Run Microsoft Search Query**
  + **Search Emails**

### Change

**Ivanti Endpoint Manager**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Task**
  + **Scan Endpoints**

### Change

**Akamai**: Version 3.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Items To Client List**
  + **Get Client Lists**
  + **Get Network Lists**
  + **Remove Items From Client List**

### Change

**CyberArk PAM**: Version 7.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Accounts**

### Change

**Nozomi Networks**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Vulnerabilities**
  + **Run a Query**

### Change

**iBoss**: Version 12.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Policy Block List Entries**

### Change

**FireEye EX**: Version 12.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Download Alert Artifacts**
  + **Download Quarantined Email**
  + **List Quarantined Emails**

### Change

**AWS Security Hub**: Version 9.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Insight**
  + **Get Insight Details**

### Change

**Mandiant ASM**: Version 10.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get ASM Entity Details**
  + **Search Issues**

### Change

**Cisco Orbital**: Version 17.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Execute Query**

### Change

**IronScales**: Version 5.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Incident Details**
  + **Get Incident Mitigation Details**
  + **Get Mitigation Impersonation Detail**
  + **Get Mitigations Per Mailbox**

### Change

**Google Cloud IAM**: Version 16.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Role**
  + **Create Service Account**
  + **Delete Role**
  + **List Roles**
  + **List Service Accounts**

### Change

**Armis**: Version 13.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Alert Connections**

### Change

**Attivo**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Critical ThreatPath**
  + **List Service ThreatPaths**
  + **List Vulnerability Hosts**

### Change

**Falcon Sandbox**: Version 18.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Analyze File**
  + **Analyze File URL**
  + **Search**

### Change

**Tenable.io**: Version 14.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Vulnerability Details**
  + **List Plugin Families**
  + **List Policies**
  + **List Scanners**

### Change

**Google Chat**: Version 5.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Spaces**

### Change

**IntSights**: Version 24.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Alert Image**

### Change

**Jira**: Version 53.0

* **Integration**: Added support for service account token based authentication.
* **Integration**: Updated issue object handling.
* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Download Attachments**
  + **Get Issues**
  + **List Relation Types**

### Change

**Google BigQuery**: Version 16.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Run Custom Query**
  + **Run SQL Query**

### Change

**ArcSight**: Version 43.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Activelist Entries**
  + **Get Query Results**
  + **Get Report**
  + **Is Value In Activelist Column**
  + **Search**

### Change

**Check Point Firewall**: Version 13.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Download Log Attachment**
  + **List Layers On Site**
  + **List Policies On Site**
  + **Show Logs**

### Change

**FortiAnalyzer**: Version 9.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Search Logs**

### Change

**Microsoft Defender ATP**: Version 28.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Isolate Machine Task**
  + **Create Run Antivirus Scan Task**
  + **Create Stop And Quarantine File Specific Machine Task**
  + **Create Unisolate Machine Task**
  + **Get Current Task Status**
  + **List Alerts**
  + **List Indicators**
  + **List Machines**
  + **Run Advanced Hunting Query**
  + **Wait Task Status**

### Change

**Microsoft Teams**: Version 33.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Chats**
  + **List Teams**
  + **List Users**
  + **Send Message**

### Change

**Recorded Future**: Version 19.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Update Alert**

### Change

**Active Directory**: Version 39.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Group Members**
  + **Search Active Directory**

### Change

**Cofense Triage**: Version 18.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Report Headers**
  + **List Categories**
  + **List Playbooks**
  + **List Reports Related To Threat Indicators**

### Change

**ElasticSearchV7**: Version 20.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Advanced ES Search**
  + **DSL Search**
  + **Simple ES Search**

### Change

**BMC Remedy ITSM**: Version 10.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Incident Details**
  + **Get Record Details**

### Change

**Cloudflare**: Version 5.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add IP To Rule List**
  + **List Firewall Rules**

### Change

**OpenSearch**: Version 2.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Advanced OS Search**
  + **DSL Search**
  + **Simple OS Search**

### Change

**Microsoft Graph Mail**: Version 37.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Download Attachments from Email**
  + **Extract Data from Attached EML**
  + **Move Email To Folder**
  + **Search Emails**

### Change

**F5 BIG-IP Access Policy Manager**: Version 6.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Active Sessions**

### Change

**McAfee Mvision EPO**: Version 9.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Endpoints In Group**
  + **List Groups**
  + **List Tags**

### Change

**Palo Alto Cortex XDR**: Version 24.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Execute XQL Search**

### Change

**XForce**: Version 17.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get IP By Category**

### Change

**Okta**: Version 14.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get User**

### Change

**Microsoft Intune**: Version 6.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Managed Devices**

### Change

**F5 BIG-IP iControl API**: Version 5.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Address Lists**
  + **List Data Groups**
  + **List Port Lists**
  + **List iRules**

### Change

**AppSheet**: Version 4.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Record**
  + **Delete Record**
  + **List Tables**
  + **Search Records**
  + **Update Record**

### Change

**McAfee ESM**: Version 44.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Send Advanced Query To ESM**
  + **Send Query To ESM**

### Change

**Google Cloud Recommender**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Recommendation**
  + **List Recommendations**
  + **Update Recommendation**

### Change

**Any.Run**: Version 9.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Search Report History**

### Change

**FireEye Helix**: Version 16.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Lists**
  + **Get List Items**

### Change

**Area1**: Version 7.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get Recent Indicators**

### Change

**ExabeamAdvancedAnalytics**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Comments To Entity**
  + **Create Watchlist**
  + **List Watchlist Items**
  + **List Watchlists**

### Change

**Azure Monitor**: Version 2.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Search Logs**

### Change

**Rapid7 InsightIDR**: Version 10.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Investigations**
  + **List Saved Queries**
  + **Run Saved Query**

### Change

**Amazon Macie**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Custom Data Identifier**
  + **List Findings**

### Change

**AWS IAM Access Analyzer**: Version 8.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Scan Resources**

### Change

**ProofPoint TAP**: Version 13.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **DecodeURL**
  + **Get Threat Forensics**
  + **GetCampaign**
  + **List Campaigns**
  + **Search Events**

### Change

**Splunk**: Version 62.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Entity Query**
  + **SplunkQuery**

### Change

**LogPoint**: Version 18.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Entity Query**
  + **Execute Query**
  + **List Repos**

### Change

**BitSight**: Version 10.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Company Highlights**
  + **List Company Vulnerabilities**

### Change

**WMI**: Version 12.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **ListServices**
  + **ListUsers**
  + **RunQuery**

### Change

**AWS Identity and Access Management (IAM)**: Version .0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create a Group**
  + **Create a Policy**
  + **Create a User**
  + **List Groups**
  + **List Policies**
  + **List Users**

### Change

**Fortinet FortiSIEM**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Custom Query**
  + **Execute Simple Query**

### Change

**Humio**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Custom Search**
  + **Execute Simple Search**

### Change

**AlgoSec**: Version 5.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Templates**

### Change

**AWS WAF**: Version 9.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create IP Set**
  + **Create Regex Pattern Set**
  + **Create Rule Group**
  + **Create Web ACL**
  + **List IP Sets**
  + **List Regex Pattern Sets**

### Change

**CA Service Desk Manager**: Version 24.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Search Tickets**
  + **Sync Ticket History**

### Change

**Freshworks Freshservice**: Version 16.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Ticket Time Entry**
  + **Add a Ticket Note**
  + **Add a Ticket Reply**
  + **Create Requester**
  + **Create Ticket**
  + **List Agents**
  + **List Requesters**
  + **List Ticket Conversations**
  + **List Ticket Time Entries**
  + **List Tickets**
  + **Update Requester**
  + **Update Ticket**
  + **Update Ticket Time Entry**

### Change

**BMC Helix RemedyForce**: Version 15.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Custom Query**
  + **Execute Simple Query**
  + **Get Record Details**
  + **List Record Types**

### Change

**AWS S3**: Version 6.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Download File From Bucket**
  + **Get Bucket Policy**
  + **List Bucket Objects**
  + **List Buckets**
  + **Upload File To Bucket**

### Change

**Cybereason**: Version 22.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Custom Investigation Search**
  + **Execute Simple Investigation Search**
  + **List Malop Affected Machines**
  + **List Malop Remediations**
  + **List Processes**
  + **List files**
  + **Remediate Malop**

### Change

**SCCM**: Version 19.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Run WQL Query**

### Change

**Netskope**: Version 15.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Alerts**
  + **List Clients**
  + **List Events**

### Change

**Qradar**: Version .0

* Optimized the caching fetched offenses logic in the following connectors:

  + **Qradar Correlation Events Connector V2**
  + **Qradar Offenses Connector**
* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Rule MITRE Coverage**
  + **List Reference Maps**
  + **List Reference Maps of Sets**
  + **List Reference Sets**
  + **List Reference Tables**
  + **Lookup for a Key in Reference Map**
  + **Lookup for a Key in Reference Map of Sets**
  + **Lookup for a Value in Reference Map**
  + **Lookup for a Value in Reference Map of Sets**
  + **Lookup for a Value in Reference Set**
  + **Lookup for a Value in Reference Tables**

### Change

**Google Cloud Compute**: Version 14.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Labels To Instance**
  + **Get Instance IAM Policy**
  + **List Instances**
  + **Remove External IP Addresses**
  + **Set Instance IAM Policy**

### Change

**Cylance**: Version 17.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Global List**
  + **Get Threats**

### Change

**EmailV2**: Version 38.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Search Email**

### Change

**McAfee EPO**: Version 35.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Execute Custom Query**
  + **Execute Entity Query**
  + **Execute Query By ID**
  + **List Queries**
  + **List Tasks**

### Change

**ArcSight Logger**: Version 10.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Send Query**

### Change

**SonicWall-Beta**: Version 7.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Address Groups**
  + **List URI Groups**
  + **List URI Lists**

### Change

**VSphere**: Version 9.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Vms**

### Change

**SiemplifyUtilities**: Version 26.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Export Entities as OpenIOC File**
  + **Extract Top From JSON**

### Change

**Office 365 CloudApp Security**: Version 23.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Enrich Entities**
  + **List Files**

### Change

**Salesforce**: Version 15.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Cases**

### Change

**AWS Elastic Compute Cloud (EC2)**: Version 8.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Start Instance**
  + **Stop Instance**
  + **Terminate Instance**

### Change

**McAfee Mvision ePO V2**: Version 6.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **List Devices**
  + **List Tags**

### Change

**Anomali ThreatStream**: Version 12.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Submit Observables**

### Change

**Automox**: Version 6.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Policies**

### Change

**Microsoft Graph Security**: Version 24.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Alerts**

### Change

**Qualys VM**: Version 22.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Download Vm Scan Results**
  + **Launch VM Scan And Fetch Results**
  + **List Groups**
  + **List Reports**
  + **List Scans**

### Change

**Cloud Logging**: Version 4.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Execute Query**

### Change

**Cisco ISE**: Version 14.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **List Endpoint Identity Group**

### Change

**SentinelOneV2**: Version 45.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Create Path Exclusion Record**
  + **Get Blacklist**
  + **Get Deep Visibility Query Result**
  + **Get Site Agents**
  + **Get Threats**
  + **Initiate Deep Visibility Query**
  + **List Sites**
  + **Mark as Threat**
  + **Mitigate Threat**
  + **Resolve Threat**

### Change

**Palo Alto Panorama**: Version 33.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Correlated Traffic Between IPs**
  + **Search logs**

### Change

**Cisco AMP**: Version 20.0

* Introduced Light Theme compatibility for the predefined widget of the following
  action:

  + **Get File List Items**

### Change

**Slack**: Version 27.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Get Channel Or User Conversation History**
  + **List Channels**
  + **List Users**
  + **Send Interactive Message**

### Change

**LogRhythm**: Version 20.0

* Introduced Light Theme compatibility for predefined widgets of the following
  actions:

  + **Add Alarm To Case**
  + **Attach File To Case**
  + **Get Alarm Details**
  + **List Case Evidence**

---
## 2026-03-12

### Feature

**Microsoft Azure Sentinel**: Version 59.0

* The following new job has been added:

  + **Sync Incidents V2**

### Change

**Microsoft Azure Sentinel**: Version 59.0

* Deprecated the following job:

  + **Sync Incidents V2****Note:** Use the Sync Incidents V2 job for syncing.

---
## 2026-03-11

### Change

**CrowdStrike Falcon**: Version 72.0

* Updated the handling of `Days To Expire` in the following action:

  + **Upload IOCs**

### Change

**Case Federation**: Version 7.0

* **Integration**: Updated to support self-service configuration.

### Change

**ProofPoint TAP**: Version 12.0

* Updated input handling in the following action:

  + **DecodeURL**

### Change

**Microsoft Teams**: Version 32.0

* Updated reply handling in the following action:

  + **Wait for Reply**

### Change

Introduced Light Theme compatibility for predefined widgets in the following
integrations:

* **CrowdStrike Falcon**: Version 72.0
* **Google Chronicle**: Version 79.0
* **Google Cloud API**: Version 8.0
* **Google Cloud Asset Inventory**: Version 13.0
* **Google Security Command Center**: Version 16.0
* **Google Threat Intelligence**: Version 10.0
* **HTTP v2**: Version 13.0
* **MITRE ATT&CK**: Version 17.0
* **ScreenshotMachine**: Version 14.0
* **Siemplify**: Version 104.0
* **UrlScan.io**: Version 28.0
* **Vertex AI**: Version 5.0
* **VirusTotalV3**: Version 38.0
* **Vmware Carbon Black Cloud**: Version 37.0

---
## 2026-03-03

### Feature

**Siemplify**: Version 103.0

* The following new job has been added:

  + **Response Integration & Connector Upgrade**

### Feature

**Akamai**: Version 2.0

* The following new action has been added:

  + **Activate Client List**

### Change

**Splunk**: Version 61.0

* Updated input handling in the following action:

  + **Update Notable Events**

### Change

**CrowdStrike Falcon**: Version 71.0

* Added the ability to define an expiration date for IOCs to the following
  action:

  + **Upload IOCs**
* Added support for hidden hosts in the following action:

  + **Get Host Information**

### Change

**Google Security Command Center**: Version 15.0

* Updated the processing of mute states in the following action:

  + **List Asset Vulnerabilities**

### Change

**AWS GuardDuty**: Version 9.0

* Updated severity handling in the following connector:

  + **AWS GuardDuty - Findings Connector**

### Change

**Microsoft Graph Mail Delegated**: Version 13.0

* Updated folder handling in the following actions:

  + **Forward Email**
  + **Save Email To Case**
  + **Send Email**
  + **Send Email HTML**
  + **Send Thread Reply**
  + **Send Vote Email**
  + **Wait For Email From User**
  + **Wait For Vote Email Results**
* Updated folder handling in the following connector:

  + **Microsoft Graph Mail Delegated Connector**

### Change

**Google Chronicle**: Version 78.0

* Updated raw log data processing in the following actions:

  + **Get Detection Details**
  + **Execute UDM Query**

### Change

**Microsoft Graph Mail**: Version 36.0

* Updated folder handling in the following actions:

  + **Forward Email**
  + **Save Email To Case**
  + **Send Email**
  + **Send Email HTML**
  + **Send Thread Reply**
  + **Send Vote Email**
  + **Wait For Email From User**
  + **Wait For Vote Email Results**
* Updated folder handling in the following connector:

  + **Microsoft Graph Mail Connector**

---
## 2026-02-25

### Feature

**Google Workspace**: Version 23.0

* The following new action has been added:

  + **Remove Extension**

### Change

**Google Chronicle**: Version 77.0

* **Integration**: Updated the error handling for Workload Identity
  authentication.

### Change

**Microsoft 365 Defender**: Version 23.0

* Added support for Graph API to the following actions:

  + **Execute Query**
  + **Execute Custom Query**
  + **Execute Entity Query**

---
## 2026-02-18

### Feature

New **Proofpoint Threat Protection** integration

### Change

**Cofense Triage**: Version 17.0

* Optimized the report processing in the following connector:

  + **Cofense Triage - Reports Connector**

### Change

**Qualys VM**: Version 21.0

* **Integration**: Added the ability to configure the `X-Requested-With` header.

### Change

**QRadar**: Version 63.0

* Updated the logic for offense processing in the following connectors:

  + **Qradar Correlation Events Connector V2**
  + **Qradar Offenses Connector**

### Change

**Palo Alto Cortex XDR**: Version 23.0

* Added the ability to provide agents using input parameters in the following
  actions:

  + **Scan Endpoint**
  + **Isolate Endpoint**
  + **Unisolate Endpoint**

### Change

**Google Chronicle**: Version 76.0

* Restored the previous JSON result structure for empty result sets in the
  following action:

  + **Execute UDM Query**

### Change

**Exchange**: Version 119.0

* Updated the handling of S/MIME emails sent on MacOS in the following
  connectors:

  + **Exchange - Mail Connector v2 with OAuth Authentication**
  + **Exchange - Mail Connector v2**

### Change

**CrowdStrike Falcon**: Version 70.0

* Deprecated the following actions:

  + **Add Incident Comment**
  + **Update Incident**
  + **Add Comment to Detection**
  + **Close Detection**
  + **Update Detection**
* Deprecated the following connectors:

  + **CrowdStrike - Detections Connector**
  + **Crowdstrike - Incidents Connector**

---
## 2026-02-11

### Feature

**CiscoUmbrella**: Version 15.0

* The following new actions have been added:

  + **Is Domain In Cisco Popularity List**
  + **List Top Domains**

### Change

**Tenable.io**: Version 13.0

* Optimized the asset processing of the following connector:

  + **TenableIO - Vulnerabilities Connector**
* Updated the entity processing logic of the following actions:

  + **Enrich Entities**
  + **List Endpoint Vulnerabilities**
  + **Scan Endpoints**

### Change

**Google Threat Intelligence**: Version 9.0

* Added the ability to define the data freshness threshold for available hashes
  to the following action:

  + **Submit File**
* Added the ability to filter using monitor names to the following connector:

  + **Google Threat Intelligence - DTM Alerts Connector**
* **Integration**: Updated the connectivity test method to avoid API quota
  consumption.

### Change

**Palo Alto Cortex XDR**: Version 22.0

* Updated the event processing and dynamic list handling of the following
  connector:

  + **Palo Alto Cortex XDR Connector**
* Added the ability to ignore certain types of artifacts to the following
  connector:

  + **Palo Alto Cortex XDR Connector**

---
## 2026-02-04

### Change

**Siemplify ThreatFuse**: Version 16.0

* Updated the configuration (`Connector.def`) of the following connector::

  + **Siemplify ThreatFuse - Observables Connector**

### Change

**Siemplify**: Version 102.0

* Refactored the following actions:

  + **Get Case Details**
  + **Wait For Custom Fields**
  + **Set Custom Fields**
  + **Get Similar Cases**
  + **Get Custom Field Values**
  + **Export Case**
* Updated error handling in the following action:

  + **Assign Case**

### Change

**Google Chronicle**: Version 75.0

* Optimized performance for large data tables in the following actions:

  + **Is Value In Data Table**
  + **Remove Rows From Data Table**

### Change

**Azure Security Center**: Version 13.0

* Updated the configuration (`Connector.def`) of the following connector:

  + **Azure Security Center - Security Alerts Connector**

---
## 2026-01-28

### Feature

**Google Threat Intelligence**: Version 8.0

* The following new actions have been added:

  + **Add ASM Issue Note**
  + **Add Tag To DTM Alert**

### Change

**Google Chronicle**: Version 74.0

* Reverted the JSON result structure for aggregated queries in the following
  action:

  + **Execute UDM Query**

### Change

**Google Threat Intelligence**: Version 8.0

* Added the ability to automatically set the `is_suspicious` flag on entities
  based on specific GTI score and Engine count thresholds in the following
  action:

  + **Enrich Entities**
* Added the ability to flag entities as `is_risky` within the JSON output when
  GTI scores or Engine counts meet specified criteria to the following action:

  + **Submit File**

### Change

**Siemplify**: Version 101.0

* Added support to set custom fields upon alert closure to the following action:

  + **Close Alert**
* Added support to set custom fields upon case closure to the following action:

  + **Close Case**

### Change

**Salesforce**: Version 14.0

* **Integration**: Updated the Salesforce SDK to the latest version

### Change

**Proofpoint Cloud Threat Response**: Version 2.0

* **Integration**: Updated dependencies.

### Change

**Jira**: Version 52.0

* Optimized ticket processing workflows in the following job:

  + **Sync Closure Job**

### Change

**Azure Active Directory**: Version 22.0

* Added the ability to fetch MFA information to the following actions:

  + **Enrich User**
  + **Get Manager Contact Details**

---
## 2026-01-21

### Feature

New **Azure API** integration

### Feature

**Okta**: Version 13.0

* The following new action has been added:

  + **Clear Okta User Session**

### Change

**Azure Active Directory**: Version 21.0

* Updated the JSON result example of the following action:

  + **List Members in The Group**
* Added more metadata to the JSON result example of the following action:

  + **List Groups**

### Change

**Google Cloud API**: Version 7.0

* Updated `Expected Response Values` description in the following action:

  + **Execute HTTP Request**

### Change

**Google Chronicle**: Version 73.0

* Updated the processing of queries in the following action:

  + **Execute UDM Query**

### Change

**QRadar**: Version 62.0

* Updated the event processing logic of the following connector:

  + **QRadar Correlations Connector V2**

### Change

**Microsoft 365 Defender**: Version 22.0

* Updated the tracking logic for alerts in the following connector:

  + **Microsoft 365 Defender - Incidents Connector**

### Change

**HTTP v2**: Version 12.0

* Updated `Expected Response Values` description in the following action:

  + **Execute HTTP Request**

### Change

**Netskope**: Version 14.0

* Refactored the following action:

  + **Ping**

---
## 2026-01-14

### Change

**Azure Active Directory**: Version 20.0

* Updated the action to include the email ID in the action output and expanded
  capabilities to return all metadata fields in the following action:

  + **Get Manager Contact Details**
* **Integration**: Updated the code to handle special characters in identifiers
  by implementing URL encoding and OData escaping.

### Change

**Slack**: Version 26.0

* Updated the Base URL construction logic for the following action:

  + **Build Block**

### Change

**Okta**: Version 12.0

* Updated the pagination processing mechanismthe in following action:

  + **List Users**

### Change

**Microsoft Graph Mail Delegated**: Version 12.0

* Improved the "mark emails as read" functionality in the following connector:

  + **Microsoft Graph Mail Delegated Connector**

### Change

**Microsoft Graph Mail**: Version 35.0

* Improved the "mark emails as read" functionality in the following connector:

  + **Microsoft Graph Mail Connector**

### Change

**Siemplify**: Version 100.0

* Updated the following action to include the JSON result in the action output:

  + **Get Custom Field Values**

---
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
