# Google SecOps

## 2025-12-17

### Announcement

The [Change views per alert feature](https://docs.cloud.google.com/chronicle/docs/secops/release-notes#December_07_2025) has been rolled back.

---
## 2025-12-10

### Announcement

**Learn key differences between SPL and YARA-L 2.0**

A new guide is available to explain the key differences between Splunk Search Processing Language (SPL) and Google Security Operations YARA-L 2.0. The guide provides examples for converting common SPL queries and aims to accelerate the onboarding process for security professionals who transition to YARA-L 2.0.
For more information, see [Transition from SPL to YARA-L](https://docs.cloud.google.com/chronicle/docs/yara-l/transition_spl_yaral).

---
## 2025-12-09

### Feature

**Create new reference lists**

You can still create new reference lists.

This feature nullifies certain content in the [release note from August 19, 2025](https://docs.cloud.google.com/chronicle/docs/release-notes#August_19_2025), which specified that from October 2025, you would no longer be able to create new reference lists.

**Note:** Because the reference list functionality is being phased out of the Google SecOps platform (see "Reference lists" in [Feature deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations)), we recommend that you use [data tables](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables) to provide expanded functionality, instead of reference lists.

---
## 2025-12-08

### Feature

**N OF and OR syntax updates**

You can now use the N OF syntax and the `or` operator to write flexible and
conditional logic within the `condition` section of your query. These features
let you combine multiple conditions, reducing the overall complexity of your
query syntax.

For more information, see [Use or in the condition section](https://docs.cloud.google.com/chronicle/docs/yara-l/multievent-or) and [Use N OF syntax with event variables](https://docs.cloud.google.com/chronicle/docs/yara-l/multievent-n-of).

---
## 2025-12-07

### Feature

**Change views per alert**

The **Alert Overview** page now includes a new option to select a specific view for each alert. If several playbooks have run on an alert, and those playbooks have customized views, you can now select and display any of those customized views for that alert.

---
## 2025-12-03

### Change

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

* 1Password (`ONEPASSWORD`)
* A10 Load Balancer (`A10_LOAD_BALANCER`)
* Abnormal Security (`ABNORMAL_SECURITY`)
* AIX system (`AIX_SYSTEM`)
* Akamai SIEM Connector (`AKAMAI_SIEM_CONNECTOR`)
* AlgoSec Security Management (`ALGOSEC`)
* Amazon API Gateway (`AWS_API_GATEWAY`)
* Amazon VPC Transit Gateway Flow Logs (`AWS_VPC_TRANSIT_GATEWAY`)
* Apache (`APACHE`)
* Arcsight CEF (`ARCSIGHT_CEF`)
* Arista Switch (`ARISTA_SWITCH`)
* Armis Activities (`ARMIS_ACTIVITIES`)
* Aruba (`ARUBA_WIRELESS`)
* Aruba Switch (`ARUBA_SWITCH`)
* Attivo Networks (`ATTIVO`)
* Auth0 (`AUTH_ZERO`)
* AWS Aurora (`AWS_AURORA`)
* AWS CloudFront (`AWS_CLOUDFRONT`)
* AWS Cloudtrail (`AWS_CLOUDTRAIL`)
* AWS CloudWatch (`AWS_CLOUDWATCH`)
* AWS Config (`AWS_CONFIG`)
* AWS GuardDuty (`GUARDDUTY`)
* AWS Security Hub (`AWS_SECURITY_HUB`)
* AWS Session Manager (`AWS_SESSION_MANAGER`)
* AWS VPC Flow (`AWS_VPC_FLOW`)
* Azure AD (`AZURE_AD`)
* Azure AD Directory Audit (`AZURE_AD_AUDIT`)
* Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
* Azure Firewall (`AZURE_FIREWALL`)
* Azure Storage Audit (`AZURE_STORAGE_AUDIT`)
* Barracuda Firewall (`BARRACUDA_FIREWALL`)
* BeyondTrust (`BOMGAR`)
* BeyondTrust BeyondInsight (`BEYONDTRUST_BEYONDINSIGHT`)
* BeyondTrust Secure Remote Access (`BEYONDTRUST_REMOTE_ACCESS`)
* Bindplane Agent (`BINDPLANE_AGENT`)
* Bitdefender (`BITDEFENDER`)
* Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
* Cambium Networks (`CAMBIUM_NETWORKS`)
* Carbon Black (`CB_EDR`)
* Carbon Black App Control (`CB_APP_CONTROL`)
* Cequence Bot Defense (`CEQUENCE_BOT_DEFENSE`)
* Check Point (`CHECKPOINT_FIREWALL`)
* Check Point Sandblast (`CHECKPOINT_EDR`)
* Chrome Management (`CHROME_MANAGEMENT`)
* CipherTrust Manager (`CIPHERTRUST_MANAGER`)
* Cisco AMP (`CISCO_AMP`)
* Cisco ASA (`CISCO_ASA_FIREWALL`)
* Cisco Email Security (`CISCO_EMAIL_SECURITY`)
* Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
* Cisco Firewall Services Module (`CISCO_FWSM`)
* Cisco Internetwork Operating System (`CISCO_IOS`)
* Cisco IronPort (`CISCO_IRONPORT`)
* Cisco ISE (`CISCO_ISE`)
* Cisco Meraki (`CISCO_MERAKI`)
* Cisco Router (`CISCO_ROUTER`)
* Cisco Secure Access (`CISCO_SECURE_ACCESS`)
* Cisco Stealthwatch (`CISCO_STEALTHWATCH`)
* Cisco Switch (`CISCO_SWITCH`)
* Cisco UCM (`CISCO_UCM`)
* Cisco Umbrella Audit (`CISCO_UMBRELLA_AUDIT`)
* Cisco Umbrella Cloud Firewall (`UMBRELLA_FIREWALL`)
* Cisco Umbrella DNS (`UMBRELLA_DNS`)
* Cisco Umbrella IP (`UMBRELLA_IP`)
* Cisco Umbrella SWG DLP (`CISCO_UMBRELLA_SWG_DLP`)
* Cisco Umbrella Web Proxy (`UMBRELLA_WEBPROXY`)
* Cisco WSA (`CISCO_WSA`)
* Citrix Netscaler (`CITRIX_NETSCALER`)
* Claroty Continuous Threat Detection (`CLAROTY_CTD`)
* Claroty Xdome (`CLAROTY_XDOME`)
* Cloudflare (`CLOUDFLARE`)
* Cloudflare Network Analytics (`CLOUDFLARE_NETWORK_ANALYTICS`)
* Cloudflare WAF (`CLOUDFLARE_WAF`)
* Cloudflare Warp (`CLOUDFLARE_WARP`)
* Code42 Incydr (`CODE42_INCYDR`)
* Corelight (`CORELIGHT`)
* CoSoSys Protector (`ENDPOINT_PROTECTOR_DLP`)
* CrowdStrike Alerts API (`CS_ALERTS`)
* CrowdStrike Falcon (`CS_EDR`)
* CrowdStrike Falcon Stream (`CS_STREAM`)
* Cyber 2.0 IDS (`CYBER_2_IDS`)
* CyberArk Endpoint Privilege Manager (EPM) (`CYBERARK_EPM`)
* Cyberark Privilege Cloud (`CYBERARK_PRIVILEGE_CLOUD`)
* CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
* Cybereason EDR (`CYBEREASON_EDR`)
* Cynet 360 AutoXDR (`CYNET_360_AUTOXDR`)
* Cyolo Secure Remote Access for OT (`CYOLO_OT`)
* Darktrace (`DARKTRACE`)
* Delinea Secret Server (`DELINEA_SECRET_SERVER`)
* Digital Guardian DLP (`DIGITALGUARDIAN_DLP`)
* Digital Guardian EDR (`DIGITALGUARDIAN_EDR`)
* DigitalArts i-Filter (`DIGITALARTS_IFILTER`)
* Dummy LogType (`DUMMY_LOGTYPE`)
* EfficientIP DDI (`EFFICIENTIP_DDI`)
* ESET AV (`ESET_AV`)
* ESET Threat Intelligence (`ESET_IOC`)
* Extreme Networks Switch (`EXTREME_SWITCH`)
* F5 Advanced Firewall Management (`F5_AFM`)
* F5 ASM (`F5_ASM`)
* F5 BIGIP Access Policy Manager (`F5_BIGIP_APM`)
* F5 Silverline (`F5_SILVERLINE`)
* FireEye ETP (`FIREEYE_ETP`)
* Fluentd Logs (`FLUENTD`)
* Forcepoint NGFW (`FORCEPOINT_FIREWALL`)
* Forcepoint DLP (`FORCEPOINT_DLP`)
* Forcepoint Proxy (`FORCEPOINT_WEBPROXY`)
* Forescout NAC (`FORESCOUT_NAC`)
* FortiGate (`FORTINET_FIREWALL`)
* Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
* Fortinet FortiEDR (`FORTINET_FORTIEDR`)
* GCP Abuse Events Logs (`GCP_ABUSE_EVENTS`)
* GitHub (`GITHUB`)
* GMV Checker ATM Security (`GMV_CHECKER`)
* Google Cloud Apigee (`GCP_APIGEE`)
* Google Cloud Audit (`GCP_CLOUDAUDIT`)
* Google Cloud Security Center Threat (`GCP_SECURITYCENTER_THREAT`)
* Google Threat Intelligence IOC (`GTI_IOC`)
* GTB Technologies DLP (`GTB_DLP`)
* H3C Comware Platform Switch (`H3C_SWITCH`)
* Halcyon Anti Ransomware (`HALCYON`)
* HP Aruba (ClearPass) (`CLEARPASS`)
* HP Linux (`HP_LINUX`)
* HP Procurve Switch (`HP_PROCURVE`)
* IBM AS/400 (`IBM_AS400`)
* IBM Security Verify Access (`IBM_SVA`)
* IBM WebSEAL (`IBM_WEBSEAL`)
* IBM Websphere Application Server (`IBM_WEBSPHERE_APP_SERVER`)
* IBM z/OS (`IBM_ZOS`)
* Imperva (`IMPERVA_WAF`)
* Imperva DRA (`IMPERVA_DRA`)
* Imperva SecureSphere Management (`IMPERVA_SECURESPHERE`)
* Infoblox (`INFOBLOX`)
* Infoblox DHCP (`INFOBLOX_DHCP`)
* Infoblox DNS (`INFOBLOX_DNS`)
* ION Spectrum (`ION_SPECTRUM`)
* Ionix (`IONIX`)
* Ipswitch MOVEit Transfer (`IPSWITCH_MOVEIT_TRANSFER`)
* Island Browser logs (`ISLAND_BROWSER`)
* JAMF Pro (`JAMF_PRO`)
* Jamf Protect Telemetry V2 (`JAMF_TELEMETRY_V2`)
* JFrog Artifactory (`JFROG_ARTIFACTORY`)
* Journald (`JOURNALD`)
* JumpCloud Directory Insights (`JUMPCLOUD_DIRECTORY_INSIGHTS`)
* Juniper (`JUNIPER_FIREWALL`)
* Juniper Junos (`JUNIPER_JUNOS`)
* Kaspersky AV (`KASPERSKY_AV`)
* Kaspersky Endpoint (`KASPERSKY_ENDPOINT`)
* Keycloak (`KEYCLOAK`)
* Kiteworks (`KITEWORKS`)
* Kubernetes Node (`KUBERNETES_NODE`)
* Linux Auditing System (AuditD) (`AUDITD`)
* Linux Sysmon (`LINUX_SYSMON`)
* McAfee ePolicy Orchestrator (`MCAFEE_EPO`)
* Microsoft AD FS (`ADFS`)
* Microsoft Azure NSG Flow (`AZURE_NSG_FLOW`)
* Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
* Microsoft Defender for Office 365 (`MICROSOFT_DEFENDER_MAIL`)
* Microsoft Exchange (`EXCHANGE_MAIL`)
* Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
* Microsoft IIS (`IIS`)
* Microsoft Intune (`AZURE_MDM_INTUNE`)
* Microsoft PowerShell (`POWERSHELL`)
* Microsoft Sentinel (`MICROSOFT_SENTINEL`)
* Microsoft SQL Server (`MICROSOFT_SQL`)
* Mikrotik Router (`MIKROTIK_ROUTER`)
* Mimecast Mail V2 (`MIMECAST_MAIL_V2`)
* MISP Threat Intelligence (`MISP_IOC`)
* Mobileiron (`MOBILEIRON`)
* NetApp ONTAP (`NETAPP_ONTAP`)
* Netscout (`ARBOR_EDGE_DEFENSE`)
* Netskope CASB (`NETSKOPE_CASB`)
* Netskope V2 (`NETSKOPE_ALERT_V2`)
* Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
* Nexus Sonatype (`NEXUS_SONATYPE`)
* Nozomi Networks Scada Guardian (`NOZOMI_GUARDIAN`)
* Obsidian (`OBSIDIAN`)
* Office 365 (`OFFICE_365`)
* Okta (`OKTA`)
* Open Cybersecurity Schema Framework (OCSF) (`OCSF`)
* Open LDAP (`OPENLDAP`)
* Opnsense (`OPNSENSE`)
* Opswat Metadefender (`OPSWAT_METADEFENDER`)
* Oracle (`ORACLE_DB`)
* Oracle Cloud Infrastructure Audit Logs (`OCI_AUDIT`)
* Oracle Cloud Infrastructure VCN Flow Logs (`OCI_FLOW`)
* Orca Cloud Security Platform (`ORCA`)
* Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
* Palo Alto Cortex XDR Events (`PAN_CORTEX_XDR_EVENTS`)
* Palo Alto Networks Firewall (`PAN_FIREWALL`)
* Palo Alto Panorama (`PAN_PANORAMA`)
* Palo Alto Prisma Cloud Alert payload (`PAN_PRISMA_CA`)
* Passwordstate (`PASSWORDSTATE`)
* Ping Federate (`PING_FEDERATE`)
* Ping Identity (`PING`)
* Ping One (`PING_ONE`)
* PingIdentity Directory Server Logs (`PING_DIRECTORY`)
* PostFix Mail (`POSTFIX_MAIL`)
* PostgreSQL (`POSTGRESQL`)
* Proofpoint Observeit (`OBSERVEIT`)
* Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
* Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
* Proofpoint Threat Response (`PROOFPOINT_TRAP`)
* Radware Web Application Firewall (`RADWARE_FIREWALL`)
* RSA (`RSA_AUTH_MANAGER`)
* Ruckus Networks (`RUCKUS_WIRELESS`)
* SailPoint IAM (`SAILPOINT_IAM`)
* Salesforce (`SALESFORCE`)
* Sangfor Next Generation Firewall (`SANGFOR_NGAF`)
* Security Command Center Chokepoint (`GCP_SECURITYCENTER_CHOKEPOINT`)
* Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
* Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
* Semperis DSP (`SEMPERIS_DSP`)
* Sentinelone Activity (`SENTINELONE_ACTIVITY`)
* SentinelOne Deep Visibility (`SENTINEL_DV`)
* ServiceNow Audit (`SERVICENOW_AUDIT`)
* Solaris system (`SOLARIS_SYSTEM`)
* SonicWall (`SONIC_FIREWALL`)
* Squid Web Proxy (`SQUID_WEBPROXY`)
* STIX Threat Intelligence (`STIX`)
* Swift Alliance Messaging Hub (`SWIFT_AMH`)
* Symantec Endpoint Protection (`SEP`)
* Tanium Audit (`TANIUM_AUDIT`)
* Tanium Integrity Monitor (`TANIUM_INTEGRITY_MONITOR`)
* Tanium Threat Response (`TANIUM_THREAT_RESPONSE`)
* Teleport Access Plane (`TELEPORT_ACCESS_PLANE`)
* Tenable Active Directory Security (`TENABLE_ADS`)
* Tenable OT (`TENABLE_OT`)
* tenable.io (`TENABLE_IO`)
* Thales Luna Hardware Security Module (`THALES_LUNA_HSM`)
* Thales MFA (`THALES_MFA`)
* Trellix HX Event Streamer (`TRELLIX_HX_ES`)
* Trend Micro (`TIPPING_POINT`)
* Trend Micro Apex one (`TRENDMICRO_APEX_ONE`)
* Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
* Trend Micro Vision One Audit (`TRENDMICRO_VISION_ONE_AUDIT`)
* Trend Micro Vision One Detections (`TRENDMICRO_VISION_ONE_DETECTIONS`)
* Trend Micro Vision One Observerd Attack Techniques (`TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES`)
* TXOne Stellar (`TRENDMICRO_STELLAR`)
* Ubika Waf (`UBIKA_WAF`)
* Unix system (`NIX_SYSTEM`)
* Upstream Vehicle SOC Alerts (`UPSTREAM_VSOC_ALERTS`)
* Varonis (`VARONIS`)
* Vectra Stream (`VECTRA_STREAM`)
* Venafi ZTPKI (`VENAFI_ZTPKI`)
* Veritas NetBackup (`VERITAS_NETBACKUP`)
* Versa Firewall (`VERSA_FIREWALL`)
* Vmware Avinetworks iWAF (`VMWARE_AVINETWORKS_IWAF`)
* VMware ESXi (`VMWARE_ESX`)
* VMware NSX (`VMWARE_NSX`)
* VMware vCenter (`VMWARE_VCENTER`)
* WatchGuard (`WATCHGUARD`)
* Windows DNS (`WINDOWS_DNS`)
* Windows Event (`WINEVTLOG`)
* Windows Event (XML) (`WINEVTLOG_XML`)
* Windows Sysmon (`WINDOWS_SYSMON`)
* wiz.io (`WIZ_IO`)
* Workday User Activity (`WORKDAY_USER_ACTIVITY`)
* Workspace Activities (`WORKSPACE_ACTIVITY`)
* Workspace Alerts (`WORKSPACE_ALERTS`)
* Workspace Users (`WORKSPACE_USERS`)
* Zendesk CRM (`ZENDESK_CRM`)
* Zoom Operation Logs (`ZOOM_OPERATION_LOGS`)
* Zscaler (`ZSCALER_WEBPROXY`)
* ZScaler NGFW (`ZSCALER_FIREWALL`)
* Zscaler Private Access (`ZSCALER_ZPA`)
* Zscaler Secure Private Access Audit Logs (`ZSCALER_ZPA_AUDIT`)

The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

* Absolute Secure Endpoint (`ABSOLUTE_SECURE_ENDPOINT`)
* Airbus Security Logging (ACD AISD) (`AIRBUS_SECURITY_LOG`)
* Azure Recovery Services Vaults (`AZURE_RECOVERY_SERVICES_VAULTS`)
* Boeing Onboard Network System Logging (`BOEING_ONS`)
* Cisco Firepower Threat Defense (`CISCO_FIREPOWER_THREAT_DEFENSE`)
* Cisco Security Cloud Control (`CISCO_SECURITY_CLOUD_CONTROL`)
* Pico Corvilnet Engine (`CORVILNET_ENGINE`)
* CrowdStrike Falcon Shield (`CROWDSTRIKE_FALCON_SHIELD`)
* Easy NAC (`EASY_NAC`)
* FairXchange Horizon (`FAIRXCHANGE_HORIZON`)
* Google Threat Intelligence (`GCP_THREATINTEL`)
* HPE Alletra (`HPE_ALLETRA`)
* Huawei Cloud Trace Service Audit (`HUAWEI_CTS_AUDIT`)
* Huawei SecMaster (`HUAWEI_SECMASTER`)
* IBM ILO (`IBM_ILO`)
* Infisical (`INFISICAL`)
* JSCAPE SFTP (`JSCAPE_SFTP`)
* Juniper Edge (`JUNIPER_EDGE`)
* Kaspersky for Microsoft Office 365 (`KASPERSKY_O365_EVENTS`)
* Microsoft Defender for Cloud Apps (`MICROSOFT_DEFENDER_CLOUD_APPS`)
* Oracle Cloud Infrastructure Network Firewall (`OCI_FIREWALL`)
* Okta Workflows (`OKTA_WORKFLOWS`)
* Phosphorus (`PHOSPHORUS`)
* Rapid7 Cloud Security (`RAPID7_CLOUDSEC`)
* Research and Education Networks Information Sharing and Analysis Center (`REN_ISAC`)
* Risk Resecurity (`RISK_RESECURITY`)
* Sangfor Network Detection and Response (`SANGFOR_NDR`)
* SAP Enterprise Threat Detection (`SAP_ETD`)
* SAP IAS Context (`SAP_IAS_CONTEXT`)
* Sectigo SCM (`SECTIGO_SCM`)
* ServiceNow Node (`SERVICENOW_NODE`)
* ServiceNow Outbound HTTP (`SERVICENOW_OUTBOUNDHTTP`)
* ServiceNow System log (`SERVICENOW_SYSLOG`)
* ServiceNow Transaction (`SERVICENOW_TRANSACTION`)
* Seti S4 (`SETI_S4`)
* ThousandEyes (`THOUSAND_EYES`)
* Transmit Security Mosaic CIAM (`TRANSMIT_MOSAIC_CIAM`)
* Transmit Security Mosaic Fraud Prevention (`TRANSMIT_MOSAIC_FRAUD_PREVENTION`)
* Transmit Security Mosaic Identity Verification (`TRANSMIT_MOSAIC_IDENTITY_VERIFICATION`)
* Transmit Security Mosaic Management (`TRANSMIT_MOSAIC_MANAGEMENT`)
* Tripwire Security Configuration Management (`TRIPWIRE_SCM`)
* Valimail (`VALIMAIL`)
* WSO2 IS AM (`WSO2_IS_AM`)
* XDR.Net Digital Twin (`XDRNET_DIGITALTWIN`)
* Zimbra Mail (`ZIMBRA_MAIL`)
* Zscaler Email DLP (`ZSCALER_EMAIL_DLP`)

---
## 2025-11-13

### Feature

**Raw log search enhancements**

Google SecOps now includes enhancements to raw log search to boost usability,
performance, and data analysis:

* **New filtering options**: Filter raw log results by their parsing status or
  by one or more log sources.
* **Optimized results view**: Expand or collapse the Trend over time graph,
  providing more space for results.
* **Download raw log results**: Download raw log results to a CSV file. By default,
  the **Timestamp**, **Event Type**, and **Raw log** columns are included. You can
  select additional columns through **Column Manager**.
* **Enhanced search visibility**: The search query and applied filters are now
  displayed on the **Search** page.
* **New API for raw log search**: Use the **legacySearchRawLogsV2** API to search
  for raw logs within a specified Google SecOps instance.

For more details, see the following topics:

* [Filter data in Raw Log Search](https://docs.cloud.google.com/chronicle/docs/investigation/filter-data-raw-log-scan-view)
* [Conduct a raw log search](https://docs.cloud.google.com/chronicle/docs/investigation/raw-log-search-in-investigate)
* [Use raw log search](https://docs.cloud.google.com/chronicle/docs/investigation/search-raw-logs)
* [Method: legacy.legacySearchRawLogsV2](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacySearchRawLogsV2)

---
## 2025-11-12

### Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

* [Collect Absolute Secure Endpoint logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/absolute-se)
* [Collect AIDE (Advanced Intrusion Detection Environment) logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/aide)
* [Collect Akamai Enterprise Application Access logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-eaa)
* [Collect Apache Hadoop logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/apache-hadoop)
* [Collect Armis Vulnerabilities logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-vulnerabilities)
* [Collect Array Networks SSL VPN logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/arraynetworks-vpn)
* [Collect Aruba IPS logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-ips)
* [Collect Atlassian Confluence logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-confluence)
* [Collect Cisco AMP for Endpoints logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-amp-for-endpoints)
* [Collect Cisco APIC logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-apic)
* [Collect Cisco Application Centric Infrastructure (ACI) logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-aci)
* [Collect Cisco CallManager logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-callmanager)
* [Collect Cisco CloudLock CASB logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-cloudlock-casb)
* [Collect Cisco DNA Center Platform logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-dnac)
* [Collect Cisco eStreamer logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-estreamer)
* [Collect Cribl Stream logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cribl-stream)
* [Collect CrowdStrike FileVantage logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-filevantage)
* [Collect CrowdStrike IDP Services logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-idp)
* [Collect Cynet 360 AutoXDR logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cynet360-autoxdr)
* [Collect Digital Shadows SearchLight logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-searchlight)
* [Collect Duo Telephony logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-telephony)
* [Collect Edgio WAF logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/edgio-waf)
* [Collect Elastic Auditbeat logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-auditbeat)
* [Collect Elastic Packet Beats logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-packetbeats)
* [Collect Elasticsearch logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/elasticsearch)
* [Collect Entrust nShield HSM audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/entrust-nshield-hsm-audit)
* [Collect Imperva Advanced Bot Protection logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-abp)
* [Collect Imperva Attack Analytics logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-aa)
* [Collect Imperva Audit Trail logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-audit-trail)
* [Collect Imperva CEF logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-cef)
* [Collect Imperva Data Risk Analytics (DRA) logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-dra)
* [Collect Imperva Database logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-db)
* [Collect Imperva FlexProtect logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-flexprotect)
* [Collect Imperva SecureSphere Management logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-ssm)
* [Collect Kiteworks (formally Accellion) logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/accellion)
* [Collect Proofpoint Emerging Threats Pro IOC logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-etp-ioc)
* [Collect ServiceNow audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-audit)
* [Collect Team Cymru Scout Threat Intelligence data](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/team-cymru-scout-ti)
* [Collect URLScan IO logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/urlscan-io)
* [Collect Uptycs EDR logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/uptycs-edr)
* [Collect VanDyke VShell SFTP logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/vandyke-vshell-sftp)
* [Collect Zendesk CRM logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/zendesk-crm)
* [Collect ZeroFox Platform logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/zerofox-platform)

### Feature

**Enhance threat visibility and detection with Emerging Threats**

The new **Emerging Threats** page provides AI-powered threat intelligence to help
you understand how current threat campaigns might affect your organization.
Powered by Google Threat Intelligence (GTI) and Gemini models, this page offers
a curated view of critical global threats relevant to your environment.

Emerging Threats continuously aligns intelligence from GTI with your organization's
telemetry to highlight detection coverage and identify gaps. When it finds a gap,
it uses Gemini to automatically draft new detection rules to accelerate your response.

For more details, see [Emerging Threats overview](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats),
[Emerging Threats feed](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats-feed),and
[Emerging Threats detailed view](https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats-detailed-view).

### Feature

**Use the Triage Agent to investigate alerts**

You can now use Triage Agent, an AI-powered investigation assistant, to
analyze alerts in Google SecOps. Triage Agent determines if an
alert is a true or false positive, provides a summarized explanation for its
conclusion, and suggests next steps for further investigation.

You can trigger investigations manually or have them run automatically on
supported alert types. Each investigation produces a detailed report that includes
the agent's disposition, a summary of its findings, and a timeline of the analysis.

For more details, see [Use Triage Agent to investigate alerts](https://docs.cloud.google.com/chronicle/docs/secops/triage-agent).

---
## 2025-11-10

### Feature

**Nested if**

You can now use `if` statements in both the `outcome` and `events` sections and
also within the `then` `else` clauses of another `if` statement. This capability
lets you introduce more complicated logic to your query and is supported in
Rules, Search, and Dashboards.

For more information, see
[Use nested if statements for more complex logic](https://docs.cloud.google.com/chronicle/docs/yara-l/nested-if).

---
## 2025-11-07

### Changed

**MITRE ATT&CK coverage dashboard is now available**

The new [MITRE ATT&CK coverage dashboard](https://docs.cloud.google.com/chronicle/docs/detection/mitre-dashboard) lets you measure your security posture against the MITRE ATT&CK framework, helping you:

* Assess threat coverage
* Identify gaps
* Prioritize security efforts

---
## 2025-10-31

### Changed

**Custom log type rename**

From now on, all custom log types will be renamed with the custom suffix to prevent confusion with prebuilt log types. The following custom log types already reflect the new naming convention:

* HUAWEI\_SECMASTER\_CUSTOM
* GTI\_THREAT\_FEED\_CUSTOM
* GTI\_IOC\_STREAM\_CUSTOM
* ABSOLUTE\_SECURE\_ENDPOINT\_CUSTOM
* GTI\_IOC\_CUSTOM
* IBM\_ILO\_CUSTOM
* GCP\_THREATINTEL\_CUSTOM
* SAP\_ETD\_CUSTOM

### Feature

**Search usability enhancements**

Google SecOps has introduced the following capabilities to improve usability,
performance, and customization in search results:

* **Improved performance for large result sets**: For broad queries, Google SecOps
  now provides paginated search results. You can select the number of rows to
  display per page. This pagination applies to the 10,000 results displayed in the table.
* **Optimized results view**: The search editor now automatically collapses after
  a query runs, providing more space for results. You can also hide or show the
  **Charts** and **Aggregations** panels with the **View Options** list.
* **Customizable column views**: You can now create, save, and share custom sets
  of columns in the **Events** table for consistent analysis across teams.

For more details, see [Search for events and alerts](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search).

---
## 2025-10-30

### Announcement

**Upgraded Chronicle API ingestion methods from alpha to beta**

We've upgraded the Chronicle API ingestion methods from alpha to beta. This upgrade signals API stability and functional completeness, unblocking customer and partner adoption for production integrations.

For more information, see
[Ingestion methods](https://cloud.google.com/chronicle/docs/reference/ingestion-methods).

### Feature

**YARA-L functions**

The following new YARA-L functions are now generally available:

* [strings.ends\_with](https://docs.cloud.google.com/chronicle/docs/yara-l/functions#stringsends_with):
  Takes two strings (value, suffix) and returns true if the suffix is
  non-empty and at end-of-value.
* [strings.split](https://docs.cloud.google.com/chronicle/docs/yara-l/functions#stringssplit): Splits
  string value using a delimiter argument (by default, a comma).
* [window.range](https://docs.cloud.google.com/chronicle/docs/yara-l/functions#windowrange): Returns the
  range of the values input values found.

---
## 2025-10-29

### Feature

**Improved Support for Chrome Enterprise Premium**

This feature is currently in Preview.

An improved integration for Chrome Enterprise Premium is now available that includes:

* Streamlined connection to Google SecOps, using recommended security defaults
* Enhanced log events with Google Safe Browsing context
* Updated parser and integration documentation: [Collect Google Chrome logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-management)
* Curated dashboards for Chrome Enterprise Premium
* Google Workspace SOAR actions to manage Chrome extension blocklist policies ([Block Extension](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-workspace#block_extension) and [Delete Extension](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-workspace#delete_extension))

---
## 2025-10-28

### Feature

**Risk-based alerting with entity-only rules**

With the new `ENTITY_RISK_CHANGE` UDM event type, you can now write YARA-L
detection rules that trigger independently of ingested events. This capability
lets you focus specifically on changes in an entity's risk score, significantly
decreasing the time required for Google Security Operations to detect and alert
on shifting entity risk levels.

For more information, see
[Risk-based alerting with entity-only rules](https://docs.cloud.google.com/chronicle/docs/detection/risk-based-alerting).

---
## 2025-10-27

### Announcement

**New rules for Chrome Enterprise Premium**

Curated Detections has been enhanced with additional Chrome Enterprise Premium Browser Threat detections.
The following rules have been added to the rulepack:

* Archive Exfiltration Event to Non-Google Websites
* Google Chrome Navigation Event to Shortened URLs
* Suspicious Download from Filehosting or Chat Platform in Chrome Management
* Chrome Suspicious Download Event from Newly Observed Domain in Environment

---
## 2025-10-26

### Feature

**Delete high-load SOAR environments**

You can now easily delete environments with heavy loads directly from the platform.

---
## 2025-10-21

### Announcement

**Premium [Fortinet Firewall parser](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fw) now available as Release Candidate**

This enhanced parser is available as a **Release Candidate** for the next 2 months. To opt in and begin testing it, go to **SIEM Settings > Parsers**. We encourage you to try it out and evaluate the improvements before it becomes the default.

---
## 2025-10-15

### Deprecated

The Netskope v1 API feed has been deprecated by Netskope. If you are using the Netskope REST API v1 with Google SecOps, you must switch to the Netskope REST API v2.

---
## 2025-10-09

### Feature

**Customize Events table columns in Search**

You can now specify which columns appear in the **Events** table on the
**Search** page and in tables within your dashboard widgets. Use the `select`
and `unselect` keywords to define the displayed columns.

For more information, see [Control columns using select and unselect keywords](https://cloud.google.com/chronicle/docs/investigation/select-unselect).

---
## 2025-10-08

### Feature

**Multi-stage queries in YARA-L**

This feature is currently in Preview.

Multi-stage queries in YARA-L are now available as a Preview feature. Multi-stage queries in YARA-L let you feed the output of one query stage directly into the input of a subsequent stage. This process gives you greater control over data transformation than single, monolithic query. They are supported in both **Dashboards** and **Search**. Multi-stage queries can contain between 1 and 4 named stages, in addition to a root stage.

For more information, see [Create multi-stage queries in YARA-L](https://docs.cloud.google.com/chronicle/docs/investigation/multi-stage-yaral).

---
## 2025-10-07

### Feature

**Manage parser versions**

This feature is in preview.

You now have granular control over how new pre-built parser versions are deployed within your environment.

This feature lets you manage parser updates by taking the following actions:

* Opt in or opt out of automatic parser updates.
* Review and compare the processing logic between different parser versions.
* Manually update a parser to a newer version.
* Revert to a previously deployed, stable parser version.

For details, see [Manage prebuilt parser versions](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates#manage-parser-versions).

### Announcement

**Azure AD Organizational Context default parser rollback**

The recent update to the pre-built Azure AD Organizational Context (`AZURE_AD_CONTEXT`) parser has been rolled back. This action was necessary to resolve a performance degradation issue that was introduced in the latest parser version. For more information about the exact changes and rollback timeline, see the [change log for the pre-built parser](https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates#manage_parser_updates).

---
## 2025-10-06

### Feature

**Advanced BigQuery Export**

This feature is in preview.

This feature is available for Google SecOps Enterprise Plus customers only.

Advanced BigQuery Export automatically provisions and manages essential Google SecOps datasets in a secure, Google-managed BigQuery project. You gain secure, read-only access to this data through a BigQuery linked dataset, which appears directly in your own Google Cloud project. This functionality lets you query your security data as if it were stored locally, but without the overhead of managing the data pipeline or storage.

For details, see [Use Advanced BigQuery Export](https://docs.cloud.google.com/chronicle/docs/reports/bigquery-export).

---
## 2025-10-05

### Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

* [Collect AlphaSOC alert logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asoc-alert)
* [Collect AlphaSOC alert logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rippling-activitylogs)
* [Collect Cisco vManage SD-WAN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-sdwan)
* [Collect Citrix Analytics logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-analytics)
* [Collect Citrix Monitor Service logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-ms)
* [Collect Citrix StoreFront logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-storefront)
* [Collect Delinea SSO logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-sso)
* [Collect SailPoint IAM logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sailpoint-iam)
* [Collect Sentry logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentry)
* [Collect Snipe-IT logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snipe-it)
* [Collect Sophos AV logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-av)
* [Collect Sophos Capsule8 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-cap8)
* [Collect Sophos DHCP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-dhcp)
* [Collect Sophos Intercept EDR logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-edr)
* [Collect Swimlane Platform logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/swimlane)
* [Collect Symantec WSS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-wss)
* [Collect Tailscale logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tailscale)
* [Collect Tanium Asset logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-asset)
* [Collect Tanium audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-audit)
* [Collect Tanium Comply logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-comply)
* [Collect Tanium Discover logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-discover)
* [Collect Tanium Insight logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-insight)
* [Collect Tanium Integrity Monitor logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-im)
* [Collect Tanium Patch logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-patch)
* [Collect Tanium Question logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-question)
* [Collect Tanium Reveal logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-reveal)
* [Collect Tanium Stream logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-stream)
* [Collect Tanium Threat Response logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-tr)
* [Collect TeamViewer logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teamviewer)
* [Collect Tines audit logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tines)

---
## 2025-10-03

### Changed

**Customer-managed encryption key compliance now includes support for data tables**

Google SecOps has expanded its coverage of Customer-Managed Encryption Key
(CMEK) compliance to now include support for data tables.

For more information, see
[CMEK for Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops).

---
## 2025-09-30

### Feature

**Customize Events table columns in Search**

You can now specify which columns appear in the **Events** table on the
**Search** page and in **tables** within your **dashboard widgets**. Use the `select`
and `unselect` keywords to define the displayed columns.

For more information, see [Control columns using select and unselect keywords](https://docs.cloud.google.com/chronicle/docs/investigation/select-unselect).

---
## 2025-09-28

### Announcement

**Forwarder component: end-of-life and migration**

The forwarder component is being phased out of the Google SecOps platform and will reach end-of-life (EOL) in January 2027. This impact will change all any data collection pipelines that currently use the forwarder.

**Action required**: If you're currently using the forwarder component, you must migrate your data collection workflows to an alternative mechanism before April 1, 2027. You'll need to use another data pipeline management application for log ingestion.

We recommend that you migrate to the [Bindplane OpenTelemetry (OTel) collector](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent), which provides a scalable, open-standard solution for log and metric ingestion.

The following are key dates to note:

* **Apr 1, 2026**: New Google SecOps customers cannot use the forwarder component.
* **Jan 1, 2027**: The forwarder is officially EOL. No further patches, including security patches, will be released.
* **Apr 1, 2027**: Data is no longer allowed to be ingested from the forwarder component.

### Announcement

**Update CrowdStrike API permissions before decommission**

CrowdStrike is decommissioning its Detects API on September 30, 2025. This API
has been replaced by the Alerts API. To ensure that your data feeds continue without
interruption, you may need to update your API permissions.

This change impacts you if your Google SecOps tenant meets both of the following conditions:

* You use the CrowdStrike Detection Monitoring API connector, which ingests the `CS_DETECTS` log type.
* The CrowdStrike API client configured for that feed lacks the permissions to read alerts Read.

To prevent disruption to your CrowdStrike data ingestion, you must update your API
client permissions before September 30, 2025.
Follow the instructions in [Migrate from CrowdStrike Detects API to Alerts API](https://docs.cloud.google.com/chronicle/docs/detection/migrate-detects-api-to-alerts-api)
to migrate your configuration to use the Alerts API.

For more details, see [CrowdStrike’s official decommissioning notice](https://supportportal.crowdstrike.com/s/article/Tech-Alert-30-Day-Notice-Planned-Decommission-Announcement-of-the-DetectionSummaryEvent-and-detects-API).

### Feature

**Podman support for Remote Agents**

You can now install a Remote Agent using Podman. This new functionality provides a streamlined deployment workflow—a lightweight alternative to existing installation methods.
For details, see [Deploy an agent with Podman](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-podman).

### Feature

**Debian support for remote agents**

You can now install a Remote Agent using Debian. This new functionality provides a streamlined deployment workflow—an alternative to existing installation methods.
For details, see [Deploy an agent with Debian](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-on-debian).

### Announcement

Remote Agent, Release 2.5.0 contains the following changes:

### Changed

**Increased Alert Trimming limit for Remote Agent**

The default setting for Alert Trimming has been increased to 25 MB.

### Changed

**Publisher Connector package size limit enforced**

The maximum allowed size for a Publisher's Connector Package is now limited to 25 MB.

---
## 2025-09-27

### Feature

**Use joins in YARA-L Search queries**

These changes are currently in Preview.

You can now use joins in statistical Search queries that include a `match` section
to correlate data from multiple sources. This feature lets you link related
sources directly within a single query.

For more information, see [Use joins in Search](https://docs.cloud.google.com/chronicle/docs/investigation/search-joins).

---
## 2025-09-23

### Changed

**Transport-layer migration for third-party API feeds**

Google SecOps is migrating the transport layer for third-party API feeds to a new platform to improve performance and reliability. This migration will be completed in phases and is expected to finish by the end of October 2025. The migration should not impact any existing or new, third-party API feeds. If you experience any unexpected issues with your feeds during the migration, contact your Google SecOps representative.

---
## 2025-09-16

### Announcement

**Migrate SOAR to Google Cloud**

We're actively migrating all SOAR customers and partners to their respective Google Cloud projects. This migration unifies your SOAR experience with your existing cloud environment. For more information, see [SOAR migration overview](https://cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp) and [FAQ](https://cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-faq).

---
## 2025-09-11

### Feature

**SecOps Labs**

This feature is in preview.

You can now configure and run Google SecOps Gemini and other intelligence *experiments* without disrupting your existing production systems—and benefit from their output. The experiments comply with the Role-Based Access Control (RBAC) configuration of your environment, and they have streamlined configurations with clear actionable results and output.

For details, see [Use Gemini and other experiments in Google SecOps](https://cloud.google.com/chronicle/docs/secops/google-secops-labs).

---
## 2025-09-10

### Feature

**View data retention start date**

You can now view the start date for your account's data retention period. A new, read-only page, **Data Retention**, is available under **SIEM Settings**. This page also shows the start date for your Google SecOps account's data retention period.

For more information, see [View data retention in your Google SecOps account](https://cloud.google.com/chronicle/docs/about/data-retention).

---
## 2025-09-08

### Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

[Collect Akamai Cloud Monitor logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-cm)   
[Collect Akamai DataStream 2 logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-ds2)   
[Collect Aware audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/aware-audit)   
[Collect AWS API Gateway access logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-api-gateway)   
[Collect AWS VPC Transit Gateway flow logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpc-tgflow)   
[Collect Bitwarden Enterprise event logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/bitwarden-ent-event)   
[Collect Box Collaboration JSON logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/box-collaboration-json)   
[Collect Censys logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/censys)   
[Collect Code42 Incydr core datasets](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/code42-incydr)   
[Collect CSV Custom IOC files](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/csv-custom-ioc)   
[Collect Deep Instinct EDR logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/deep-ins-edr)   
[Collect DigiCert audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/digicert-audit)   
[Collect DomainTools Iris Investigate results](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/dt-iris-investigate)   
[Collect Duo administrator logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-admin)   
[Collect Duo authentication logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-auth)   
[Collect Duo entity context logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-entity)   
[Collect Google Cloud Abuse Events logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-abuse-events)   
[Collect Harness IO audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/harness-io-audit)   
[Collect HPE Aruba Networking Central logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-anc)   
[Collect Jamf Pro context logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-pro-context)   
[Collect PingOne Advanced Identity Cloud logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/pingone-advanced-identity)   
[Collect Slack audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/slack-audit)   
[Collect Snyk group-level audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-group-audit)   
[Collect Snyk group-level audit and issues logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-group-issues)   
[Collect Venafi Zero Touch PKI logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/venafi-ztpki)   
[Collect Veritas NetBackup logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/veritas-netbackup)   
[Collect VMware AirWatch logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-airwatch)   
[Collect VMware Avi Load Balancer WAF logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-avilb-waf)   
[Collect VMware Horizon logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-horizon)   
[Collect VMware VeloCloud SD-WAN logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-velocloud-sdwan)   
[Collect Zoom operation logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/zoom-operations)

---
## 2025-09-07

### Feature

**Advanced job scheduling**

The job scheduling functionality has been enhanced with advanced options. This functionality provides more precise control and flexible, calendar-like scheduling for your scripts.

For more information, see [Configure a new job with advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling).

### Feature

**Use custom fields in the Close Case dialog**

Administrators can now add custom fields to the **Close Case** dialog. This new functionality provides a more streamlined workflow and replaces the **Dynamic Fields** feature.

For more information, see [Use custom fields in the Close Case dialog](https://cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/custom-fields-in-case-closure).

---
## 2025-09-05

### Changed

**Advanced filtering in alerts and search results**

You can now filter alerts and search results by any field in the detection object. This update provides more granular control over your queries, letting you filter by nested fields from events and entities within a detection.

---
## 2025-09-04

### Changed

**Time zone override for forwarder logs**

Google SecOps now lets you override the default time zone for your logs when you create or configure a forwarder.

For details, see [Add collector configuration](https://cloud.google.com/chronicle/docs/install/forwarder-management-configurations#add-collectors).

### Changed

**Improved Okta and Symantec Endpoint Protection parsers**

These changes are currently in Preview.

The Okta and Symantec Endpoint Protection parsers are now more efficient, with increased log-field coverage and more-accurate log-field mappings. These changes include new UDM fields and updated field mappings. We advise you to opt-in and get these new versions.

* For details on the Okta parser, see [UDM mapping table](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/okta#udm_mapping_table) and [UDM mapping delta reference](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/okta#udm_mapping_delta_reference).
* For details on the Symantec Endpoint Protection parser, see [Collect Symantec Endpoint Protection logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-endpoint-protection#udm_mapping_table) and [UDM mapping delta reference](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-endpoint-protection#udm-mapping-delta).

### Announcement

**CBN alerts functionality removed from all prebuilt parsers**

As part of deprecating the Configuration Based Normalization (CBN) alerts functionality, all [prebuilt parsers](https://cloud.google.com/chronicle/docs/event-processing/manage-parser-updates#types_of_parsers) that included the CBN alerts functionality were updated, and the functionality was removed.

**Note:** For information about how you can migrate CBN alerts to YARA-L detection alerts, see [Migrate CBN alerts to YARA-L detection rule alerts](https://cloud.google.com/chronicle/docs/detection/migrate-cbn-alerts).

---
## 2025-09-03

### Changed

**Extended match window for multi-event rules**

You can now configure rules to analyze data over a longer period. The maximum match window for these rules has been extended to 14 days. The run frequency for multi-event rules is automatically set based on the rule's match window:

* For a window size of 1 to 48 hours, the run frequency is 1 hour.
* For a window size greater than 48 hours, the run frequency is 24 hours.

---
## 2025-08-29

### Changed

**MITRE ATT&CK coverage dashboard is now available**

**This feature is currently in Preview.**

The new [MITRE ATT&CK coverage dashboard](https://cloud.google.com/chronicle/docs/detection/mitre-dashboard) lets you measure your security posture against the MITRE ATT&CK framework, helping you:

* Assess threat coverage
* Identify gaps
* Prioritize security efforts

---
## 2025-08-28

### Changed

**Composite detections for MITRE ATT&CK**

The [Curated Detections](https://cloud.google.com/chronicle/docs/detection/use-curated-detections) feature has been enhanced with new [composite rules](https://cloud.google.com/chronicle/docs/detection/composite-rules) that define chains of MITRE ATT&CK tactics and techniques.

These powerful new rule packs are now in public preview for customers with a [Google SecOps Enterprise or Enterprise Plus license](https://cloud.google.com/security/products/security-operations).

To learn more, a companion blog post will be published on the [Google Security Cloud Community](https://security.googlecloudcommunity.com/) on September 9, 2025.

---
## 2025-08-27

### Changed

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

* A10 Load Balancer (`A10_LOAD_BALANCER`)
* AIX system (`AIX_SYSTEM`)
* Apache (`APACHE`)
* Arcsight CEF (`ARCSIGHT_CEF`)
* Aruba Switch (`ARUBA_SWITCH`)
* Aruba (`ARUBA_WIRELESS`)
* Attivo Networks (`ATTIVO`)
* Auth0 (`AUTH_ZERO`)
* Amazon VPC Transit Gateway Flow Logs (`AWS_VPC_TRANSIT_GATEWAY`)
* AWS WAF (`AWS_WAF`)
* Azure AD (`AZURE_AD`)
* Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
* Azure Firewall (`AZURE_FIREWALL`)
* Azure Front Door (`AZURE_FRONT_DOOR`)
* Carbon Black App Control (`CB_APP_CONTROL`)
* None (`CHROME_MANAGEMENT`)
* Cisco ASA (`CISCO_ASA_FIREWALL`)
* Cisco DNA Center Platform (`CISCO_DNAC`)
* Cisco Email Security (`CISCO_EMAIL_SECURITY`)
* Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
* Cisco Internetwork Operating System (`CISCO_IOS`)
* Cisco IronPort (`CISCO_IRONPORT`)
* Cisco ISE (`CISCO_ISE`)
* Cisco Router (`CISCO_ROUTER`)
* Cisco vManage SD-WAN (`CISCO_SDWAN`)
* Cisco Switch (`CISCO_SWITCH`)
* Cisco Umbrella Audit (`CISCO_UMBRELLA_AUDIT`)
* Cisco VCS Expressway (`CISCO_VCS`)
* Cisco WSA (`CISCO_WSA`)
* Citrix Netscaler (`CITRIX_NETSCALER`)
* Claroty Xdome (`CLAROTY_XDOME`)
* HP Aruba (ClearPass) (`CLEARPASS`)
* Cloudflare (`CLOUDFLARE`)
* Cloudflare WAF (`CLOUDFLARE_WAF`)
* Corelight (`CORELIGHT`)
* Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
* CrowdStrike Alerts API (`CS_ALERTS`)
* CrowdStrike Detection Monitoring (`CS_DETECTS`)
* CrowdStrike Falcon (`CS_EDR`)
* CrowdStrike Falcon Stream (`CS_STREAM`)
* Cyberark Privilege Cloud (`CYBERARK_PRIVILEGE_CLOUD`)
* Darktrace (`DARKTRACE`)
* Datadog (`DATADOG`)
* Elastic Defend (`ELASTIC_DEFEND`)
* F5 ASM (`F5_ASM`)
* F5 Distributed Cloud Services (`F5_DCS`)
* F5 Silverline (`F5_SILVERLINE`)
* Fidelis Network (`FIDELIS_NETWORK`)
* FireEye (`FIREEYE_ALERT`)
* FireEye NX (`FIREEYE_NX`)
* Forcepoint DLP (`FORCEPOINT_DLP`)
* ForgeRock Identity Cloud (`FORGEROCK_IDENTITY_CLOUD`)
* FortiGate (`FORTINET_FIREWALL`)
* Cloud SQL (`GCP_CLOUDSQL`)
* Google Cloud DNS Threat Detector (`GCP_DNS_ATD`)
* Cloud Load Balancing (`GCP_LOADBALANCING`)
* None (`GCP_SECURITYCENTER_THREAT`)
* VPC Flow Logs (`GCP_VPC_FLOW`)
* AWS GuardDuty (`GUARDDUTY`)
* IBM-i Operating System (`IBM_I`)
* Imperva (`IMPERVA_WAF`)
* Infoblox DHCP (`INFOBLOX_DHCP`)
* Jamf Protect Telemetry V2 (`JAMF_TELEMETRY_V2`)
* Kemp Load Balancer (`KEMP_LOADBALANCER`)
* Kubernetes Node (`KUBERNETES_NODE`)
* ManageEngine AD360 (`MANAGE_ENGINE_AD360`)
* McAfee ePolicy Orchestrator (`MCAFEE_EPO`)
* McAfee IPS (`MCAFEE_IPS`)
* Medigate IoT (`MEDIGATE_IOT`)
* Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
* Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
* Microsoft Sentinel (`MICROSOFT_SENTINEL`)
* Microsoft SQL Server (`MICROSOFT_SQL`)
* Mikrotik Router (`MIKROTIK_ROUTER`)
* Netskope V2 (`NETSKOPE_ALERT_V2`)
* Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
* Unix system (`NIX_SYSTEM`)
* Oracle Cloud Infrastructure VCN Flow Logs (`OCI_FLOW`)
* Office 365 (`OFFICE_365`)
* Office 365 Message Trace (`OFFICE_365_MESSAGETRACE`)
* Okta (`OKTA`)
* Okta Scaleft (`OKTA_SCALEFT`)
* Oracle (`ORACLE_DB`)
* Orca Cloud Security Platform (`ORCA`)
* Proofpoint Threat Response (`PROOFPOINT_TRAP`)
* Quest Active Directory (`QUEST_AD`)
* Radware Web Application Firewall (`RADWARE_FIREWALL`)
* Red Hat OpenShift (`REDHAT_OPENSHIFT`)
* Symantec Endpoint Protection (`SEP`)
* Silverfort Authentication Platform (`SILVERFORT`)
* Squid Web Proxy (`SQUID_WEBPROXY`)
* STIX Threat Intelligence (`STIX`)
* Symantec DLP (`SYMANTEC_DLP`)
* Sysdig (`SYSDIG`)
* Tenable Security Center (`TENABLE_SC`)
* Trend Micro (`TIPPING_POINT`)
* Trellix HX Event Streamer (`TRELLIX_HX_ES`)
* Trend Micro Apex one (`TRENDMICRO_APEX_ONE`)
* Trend Micro Vision One Activity (`TRENDMICRO_VISION_ONE_ACTIVITY`)
* Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
* Trend Micro Vision One Workbench (`TRENDMICRO_VISION_ONE_WORKBENCH`)
* Ubiquiti UniFi Switch (`UBIQUITI_SWITCH`)
* Cisco Umbrella DNS (`UMBRELLA_DNS`)
* Cisco Umbrella IP (`UMBRELLA_IP`)
* Varonis (`VARONIS`)
* Vectra XDR (`VECTRA_XDR`)
* VMware vCenter (`VMWARE_VCENTER`)
* VMware vRealize Suite (VMware Aria) (`VMWARE_VREALIZE`)
* Windows Event (`WINEVTLOG`)
* Windows Event (XML) (`WINEVTLOG_XML`)
* Zscaler CASB (`ZSCALER_CASB`)
* ZScaler Deception (`ZSCALER_DECEPTION`)
* Zscaler DLP (`ZSCALER_DLP`)
* ZScaler DNS (`ZSCALER_DNS`)
* ZScaler NGFW (`ZSCALER_FIREWALL`)
* Zscaler Internet Access Audit Logs (`ZSCALER_INTERNET_ACCESS`)
* Zscaler Tunnel (`ZSCALER_TUNNEL`)
* Zscaler (`ZSCALER_WEBPROXY`)
* Zscaler Secure Private Access Audit Logs (`ZSCALER_ZPA_AUDIT`)
* Zscaler Private Access (`ZSCALER_ZPA`)

The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

* Alicloud ApsaraDB (`ALICLOUD_APSARADB`)
* AliCloud Firewall (`ALICLOUD_FIREWALL`)
* AuthMind (`AUTHMIND`)
* Microsoft Entra Recommendations (`MS_ENTRA_RECOMMENDATIONS`)
* Palo Alto Networks Prisma Access (`PAN_PRISMA_ACCESS`)
* Trellix Malware Analysis (`TRELLIX_AX`)
* Everfox ULTRA (`ULTRA`)
* ZScaler NSS VM (`ZSCALER_NSS_VM`)

---
## 2025-08-21

### Feature

[Enhanced curated detections](https://cloud.google.com/chronicle/docs/detection/use-curated-detections) has been enhanced with composite detection content for Mandiant Hunt Cloud Classification, including AWS, GCP, and Azure. This rule pack is available for Mandiant Threat Defense (MTD) customers with a Google Security Operations Enterprise or Enterprise Plus license.

---
## 2025-08-20

### Changed

**New rules added to rule pack**

Curated Detections has been enhanced with additional Chrome Enterprise Premium Browser Threat detections. The following rules have been added to the rule pack:

* Dangerous Download with Matching Hashes by multiple users in Chrome Management
* GTI High Severity File Download Event in Chrome Management
* GTI Medium Severity File Download Event in Chrome Management
* GTI Low Severity File Download Event in Chrome Management
* Safe-browsing High Severity File Download Event in Chrome Management
* Multiple Dangerous Download Events by same user in Chrome Management
* Url Event to Newly Created Domain in Chrome Management

### Feature

**Composite detections are now generally available**

The [composite detections](https://cloud.google.com/chronicle/docs/secops/release-notes#April_23_2025) feature is now in General Availability. Composite detections lets you link multiple YARA-L rules to detect complex, multistage threats. This capability enhances detection by correlating alerts that individual rules might not detect.

For more information, see [Overview of composite detections](https://cloud.google.com/chronicle/docs/detection/composite-detections).

---
## 2025-08-19

### Announcement

**Reference lists retiring**

The reference list functionality is being phased out of the Google SecOps platform.

* **October 2025**: You'll no longer be able to create new reference lists. Instead, use data tables to provide expanded functionality.
* **Migration period**: All existing reference lists will be automatically migrated to data tables. During this migration period, you can continue to use your existing reference lists without changes.
* **September 2026**: The legacy reference list functionality will be fully retired from the platform. After that date, all data will be available only through the data table interface.

---
## 2025-08-13

### Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

* [Collect Anomali ThreatStream IOC logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/anomali-threatstream-ioc)
* [Collect Cisco Application Control Engine (ACE)](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ace)
* [Collect Cisco Firepower NGFW logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-firepower-firewall)
* [Collect Cisco Firewall Service Module (FWSM)](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-fwsm)
* [Collect Cisco IronPort logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ironport)
* [Collect Cisco PIX logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-pix-firewall)
* [Collect Cisco Prime logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-prime)
* [Collect Cisco Wireless Intrusion Prevention System (WIPS) logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wips)
* [Collect Cisco Wireless LAN Controller (WLC) logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless)
* [Collect Cisco Wireless Security Management (WiSM) logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsm)
* [Collect Cloudian HyperStore logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudian-hs)
* [Collect CrushFTP logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/crushftp)
* [Collect Delinea Distributed Engine logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-de)
* [Collect Duo User context logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-user)
* [Collect ExtraHop DNS logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop-dns)
* [Collect ExtraHop RevealX logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop-revealx)
* [Collect Extreme Networks switch logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-switch)
* [Collect Extreme Networks Wireless logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/extreme-wireless)
* [Collect MuleSoft Anypoint logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/mulesoft-anypoint)
* [Collect Palo Alto Prisma SD-WAN logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-prisma-sd-wan)
* [Collect Recorded Future IOC logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/recorded-future-ioc)
* [Collect Veeam logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/veeam)
* [Collect Veridium ID logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/veridium-id)
* [Collect VMware Tanzu logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-tanzu)
* [Collect VMware vCenter logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vcenter)
* [Collect VMware vRealize logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vrealize)
* [Collect VMware vSphere logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vsphere)
* [Collect VSFTPD logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/vsftpd)
* [Collect VyOS logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/vyos)
* [Collect Workday audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/workday-audit)
* [Collect Yamaha router logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/yamaha-router)

---
## 2025-08-12

### Changed

**Data RBAC self-service enablement**

Data RBAC now includes a self-service option for direct enablement. This makes the initial onboarding process faster and simpler. For details, see [Configure data RBAC for users](https://cloud.google.com/chronicle/docs/administration/configure-datarbac-users).

---
## 2025-08-10

### Announcement

**New permissions for Content Hub**

To access all modules in the Content Hub, you must set the correct IAM role permissions.

For full details, see [Google SecOps Content Hub overview](https://cloud.google.com/chronicle/docs/secops/content_hub).

### Feature

**Updated permissions for accessing product-centric feeds**

If you have assigned **Custom IAM Roles**, you can now grant access to the product-centric feeds by adding the following permissions to the role:

* `chronicle.feedPacks.get`
* `chronicle.feedPacks.list`

To learn more about how to configure feeds using the product-centric feeds UI, see [Configure feeds by product.](https://cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds)

### Feature

**Expression Builder enhancements**

The **Expression Builder** has been enhanced with a new set of pre-built filters to help streamline query creation.

We've improved the information within the platform for all filters, both new and existing. The supporting documentation provides clearer descriptions and practical examples for each transformer, making it easier to understand their purpose and syntax.

For details, see [Use the Expression Builder](https://cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder).

### Feature

**Remote agent notifications**

Agent notifications will alert you to new remote agent version releases and agent downtime based on your permissions and associated environments. Agent notifications are now enabled by default. You can opt out of these notifications at any time from your user preferences.

For details, see [Agent notifications](https://cloud.google.com/chronicle/docs/soar/working-with-remote-agents/what-is-a-remote-agent#agent-notifications).

---
## 2025-08-08

### Changed

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

* 1Password (`ONEPASSWORD`)
* A10 Load Balancer (`A10_LOAD_BALANCER`)
* AIX system (`AIX_SYSTEM`)
* Akamai Enterprise Application Access (`AKAMAI_EAA`)
* Akamai WAF (`AKAMAI_WAF`)
* Apache (`APACHE`)
* Aqua Security (`AQUA_SECURITY`)
* Aruba (`ARUBA_WIRELESS`)
* Attivo Networks (`ATTIVO`)
* Auth0 (`AUTH_ZERO`)
* AWS Config (`AWS_CONFIG`)
* AWS GuardDuty (`GUARDDUTY`)
* AWS Lambda Function (`AWS_LAMBDA_FUNCTION`)
* AWS RDS (`AWS_RDS`)
* AWS VPC Flow (`AWS_VPC_FLOW`)
* Azure AD (`AZURE_AD`)
* Azure AD Directory Audit (`AZURE_AD_AUDIT`)
* Azure AD Sign-In (`AZURE_AD_SIGNIN`)
* Azure Key Vault logging (`AZURE_KEYVAULT_AUDIT`)
* Azure VNET Flow (`AZURE_VNET_FLOW`)
* Barracuda Email (`BARRACUDA_EMAIL`)
* Barracuda WAF (`BARRACUDA_WAF`)
* BeyondTrust BeyondInsight (`BEYONDTRUST_BEYONDINSIGHT`)
* Bitdefender (`BITDEFENDER`)
* Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
* Check Point (`CHECKPOINT_FIREWALL`)
* Check Point Sandblast (`CHECKPOINT_EDR`)
* Chrome Management (`N/A`)
* Cisco Email Security (`CISCO_EMAIL_SECURITY`)
* Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
* Cisco Internetwork Operating System (`CISCO_IOS`)
* Cisco IronPort (`CISCO_IRONPORT`)
* Cisco ISE (`CISCO_ISE`)
* Cisco Meraki (`CISCO_MERAKI`)
* Cisco NX-OS (`CISCO_NX_OS`)
* Cisco Router (`CISCO_ROUTER`)
* Cisco Stealthwatch (`CISCO_STEALTHWATCH`)
* Cisco Umbrella SWG DLP (`CISCO_UMBRELLA_SWG_DLP`)
* Cisco vManage SD-WAN (`CISCO_SDWAN`)
* Cisco WLC/WCS (`CISCO_WIRELESS`)
* Cisco WSA (`CISCO_WSA`)
* Citrix Netscaler (`CITRIX_NETSCALER`)
* Cloud Audit Logs (`N/A`)
* Cloud DNS (`N/A`)
* Cloud Load Balancing (`GCP_LOADBALANCING`)
* Cloudflare (`CLOUDFLARE`)
* Corelight (`CORELIGHT`)
* CrowdStrike Alerts API (`CS_ALERTS`)
* CrowdStrike Detection Monitoring (`CS_DETECTS`)
* CrowdStrike Falcon (`CS_EDR`)
* CrowdStrike Falcon Stream (`CS_STREAM`)
* CSV Custom IOC (`CSV_CUSTOM_IOC`)
* CyberArk (`CYBERARK`)
* Cybereason EDR (`CYBEREASON_EDR`)
* Darktrace (`DARKTRACE`)
* EfficientIP DDI (`EFFICIENTIP_DDI`)
* Elastic Defend (`ELASTIC_DEFEND`)
* EPIC Systems (`EPIC`)
* ExtraHop RevealX (`EXTRAHOP`)
* F5 Advanced Firewall Management (`F5_AFM`)
* F5 ASM (`F5_ASM`)
* F5 BIGIP Access Policy Manager (`F5_BIGIP_APM`)
* F5 BIGIP LTM (`F5_BIGIP_LTM`)
* F5 DNS (`F5_DNS`)
* F5 Silverline (`F5_SILVERLINE`)
* Fidelis Network (`FIDELIS_NETWORK`)
* FireEye ETP (`FIREEYE_ETP`)
* ForgeRock Identity Cloud (`FORGEROCK_IDENTITY_CLOUD`)
* FortiGate (`FORTINET_FIREWALL`)
* Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
* Fortinet Proxy (`FORTINET_WEBPROXY`)
* Fortinet Web Application Firewall (`FORTINET_FORTIWEB`)
* GitHub (`GITHUB`)
* Halcyon Anti Ransomware (`HALCYON`)
* HAProxy (`HAPROXY`)
* HP Aruba (ClearPass) (`CLEARPASS`)
* IBM DataPower Gateway (`IBM_DATAPOWER`)
* Imperva (`IMPERVA_WAF`)
* Imperva SecureSphere Management (`IMPERVA_SECURESPHERE`)
* Infoblox DHCP (`INFOBLOX_DHCP`)
* Jamf pro context (`JAMF_PRO_CONTEXT`)
* Kubernetes Node (`KUBERNETES_NODE`)
* Lacework Cloud Security (`LACEWORK`)
* Linux Auditing System (AuditD) (`AUDITD`)
* Linux Sysmon (`LINUX_SYSMON`)
* McAfee IPS (`MCAFEE_IPS`)
* Menlo Security (`MENLO_SECURITY`)
* Microsoft AD (`WINDOWS_AD`)
* Microsoft Azure Activity (`AZURE_ACTIVITY`)
* Microsoft Defender for Identity (`MICROSOFT_DEFENDER_IDENTITY`)
* Microsoft IIS (`IIS`)
* Mimecast (`MIMECAST_MAIL`)
* Mimecast Mail V2 (`MIMECAST_MAIL_V2`)
* MISP Threat Intelligence (`MISP_IOC`)
* NetApp ONTAP (`NETAPP_ONTAP`)
* Netskope V2 (`NETSKOPE_ALERT_V2`)
* Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
* NGINX (`NGINX`)
* One Identity Identity Manager (`ONE_IDENTITY_IDENTITY_MANAGER`)
* Opnsense (`OPNSENSE`)
* Orca Cloud Security Platform (`ORCA`)
* Palo Alto Cortex XDR Events (`PAN_CORTEX_XDR_EVENTS`)
* Palo Alto Networks Firewall (`PAN_FIREWALL`)
* Palo Alto Panorama (`PAN_PANORAMA`)
* Palo Alto Prisma Access (`PAN_CASB`)
* pfSense (`PFSENSE`)
* Ping Federate (`PING_FEDERATE`)
* Proofpoint Observeit (`OBSERVEIT`)
* Proofpoint On Demand (`PROOFPOINT_ON_DEMAND`)
* Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
* Qualys VM (`QUALYS_VM`)
* Remediant SecureONE (`REMEDIANT_SECUREONE`)
* SAP SM20 (`SAP_SM20`)
* SecureAuth (`SECUREAUTH_SSO`)
* SentinelOne EDR (`SENTINEL_EDR`)
* Silverfort Authentication Platform (`SILVERFORT`)
* Sophos Central (`SOPHOS_CENTRAL`)
* Sophos UTM (`SOPHOS_UTM`)
* Squid Web Proxy (`SQUID_WEBPROXY`)
* Symantec DLP (`SYMANTEC_DLP`)
* Symantec Web Security Service (`SYMANTEC_WSS`)
* Tenable Active Directory Security (`TENABLE_ADS`)
* Tenable Security Center (`TENABLE_SC`)
* Thinkst Canary (`THINKST_CANARY`)
* Trellix HX Event Streamer (`TRELLIX_HX_ES`)
* Trend Micro Apex one (`TRENDMICRO_APEX_ONE`)
* Trend Micro Cloud one (`TRENDMICRO_CLOUDONE`)
* Trend Micro Vision One Activity (`TRENDMICRO_VISION_ONE_ACTIVITY`)
* Trend Micro Vision One Observerd Attack Techniques (`TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES`)
* Trend Micro Vision One Workbench (`TRENDMICRO_VISION_ONE_WORKBENCH`)
* Tripwire (`TRIPWIRE_FIM`)
* Unix system (`NIX_SYSTEM`)
* VMware Horizon (`VMWARE_HORIZON`)
* VMware vCenter (`VMWARE_VCENTER`)
* VMware vRealize Suite (VMware Aria) (`VMWARE_VREALIZE`)
* WatchGuard (`WATCHGUARD`)
* Windows Event (`WINEVTLOG`)
* Windows Event (XML) (`WINEVTLOG_XML`)
* Workday Audit Logs (`WORKDAY_AUDIT`)
* Workspace Activities (`WORKSPACE_ACTIVITY`)
* Workspace Users (`WORKSPACE_USERS`)
* ZScaler Deception (`ZSCALER_DECEPTION`)

The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

* Akamai MFA (`AKAMAI_MFA`)
* Azure Org Context (`AZURE_ORG_CONTEXT`)
* Cisco Remote Access VPN (`CISCO_RAVPN`)
* CoreView Audit-log SIEM integration (`COREVIEW`)
* Fortinet Network Detection and Response (`FORTINET_FORTINDR`)
* GCP Security Command Center Chokepoint (`GCP_SECURITYCENTER_CHOKEPOINT`)
* Imperva Cloud WAF (`IMPERVA_CLOUD_WAF`)
* Lumu Universal SIEM (`LUMU`)
* Microsoft Azure Databricks (`MICROSOFT_DATABRICKS_WORKSPACES`)
* Microsoft Insights/Components (`MICROSOFT_INSIGHTS_COMPONENTS`)
* Microsoft ServiceBus/Namespaces (`MICROSOFT_SERVICEBUS_NAMESPACES`)
* Microsoft Azure SQL Managed Instances (`MICROSOFT_SQL_MANAGED_INSTANCES`)
* Moveworks (`MOVEWORKS`)
* Network Box Unified Threat Management+ (`NETWORKBOX_UTM`)
* Oracle Cloud Infrastructure Identity Cloud Service (`OCI_IDENTITY_CLOUD_SERVICE`)
* SAP Commerce Cloud (`SAP_HAC`)
* Sonatype Lifecycle (`SONATYPE_LIFECYCLE`)
* TeamViewer Tensor (`TEAMVIEWER_TENSOR`)
* Torq Audit Logs (`TORQ_AUDIT_LOGS`)
* Velociraptor - digital forensic & incident response tool (`VELOCIRAPTOR`)
* Zoom Activity Logs (`ZOOM_ACTIVITY`)

For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

---
## 2025-08-05

### Feature

**New YARA-L features**

The following capabilities have been added to YARA-L 2.0 to enhance search precision, data analysis, and investigative workflows:

* [**Conditions in UDM search and dashboards**](https://cloud.google.com/chronicle/docs/investigation/yara-l-2-0-conditions)

  You can now filter aggregates defined in the `outcome` section using the new `condition` clause. This gives you more precise control over your results and supports more targeted investigations.

  + New functionality includes support for `OR` and `n` of `[a, b, c.. z]` expressions.
  + General availability for search and dashboards.
* [**Deduplicate events in searches and dashboards**](https://cloud.google.com/chronicle/docs/investigation/deduplication-yaral)

  The new `dedup` section lets you remove duplicate events after the `match` clause in both standard UDM searches and YARA-L 2.0 queries.

  General availability for search and dashboards.
* [**Use metrics functions in UDM searches**](https://cloud.google.com/chronicle/docs/investigation/yara-l-2-0-metrics-search)

  You can now apply `metrics` functions in the `outcome` section of your search to access aggregated historical data directly in your search queries.

  + Uses the same syntax as `metrics` in rules.
  + General availability for search.
* [**Increased limits for array and array\_distinct**](https://cloud.google.com/chronicle/docs/detection/yara-l-2-0-syntax#aggregations)

  The element limit for `array` and `array_distinct` aggregation functions in YARA-L has increased from 25 to 1,000.

  + General availability for search and dashboards.
  + Private preview for rules.
* **Restrict search results using limit**

  The `limit` keyword now lets you restrict the number of results returned by a search. Use this to quickly preview data, optimize performance, or focus on a subset of results.

  General availability for search and dashboards.
* [**`earliest`**](https://cloud.google.com/chronicle/docs/investigation/statistics-aggregations-in-udm-search#earliest) and [**`latest`**](https://cloud.google.com/chronicle/docs/investigation/statistics-aggregations-in-udm-search#latest) **timestamps**

  New `earliest` and `latest` timestamps let you extract the time range of your data (within microseconds) during aggregation.

  General availability for search.
* **Layer aggregations and analytics across multi-stage queries**

  Recent updates to multi-stage queries let you:

  + Layer aggregations and data statistical functions. Calculate baselines, deviations, and trends across multiple stages of data processing.
  + Conduct joins both within and across stages.

  Private preview for search and dashboards. Contact your Google SecOps representative to enroll.
* **Join events, the entity graph, and data tables**

  You can now perform Inner joins between events, the entity graph, and data tables. These queries require a `match` clause for these joins and return results as statistics.

  Private preview for search and dashboards. Contact your Google SecOps representative to enroll.

---
## 2025-08-04

### Changed

**New rules added to rule pack**

Curated detections has been enhanced with additional Chrome Enterprise Premium Browser Threat detections. The following rules have been added to the rule pack:

Malware Transfer Event in Chrome Management

Password Breach Event By Admin User

Phishing Navigation Event Containing Suspicious Parameters In Chrome Management

Chrome Password Event on Newly Observed Domain in Environment

### Feature

[Auto Extraction](https://cloud.google.com/chronicle/docs/event-processing/auto-extraction) supports XML formatted logs in addition to JSON formatted logs. This enhancement will be available starting this week.

---
## 2025-08-03

### Feature

**Automated retries for failed playbook actions**

This feature is in Preview.

Playbook functionality now supports automatic retries for individual actions that encounter temporary issues, such as network outages, API rate limits, or service unavailability. You can define the number of retry attempts and the intervals between retries directly at the step level within playbooks.

For more information on configuring and using action retries, see [Configure action retries in playbooks](https://cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/retry-actions).

### Feature

**Custom Fields Form widget is now supported in Playbook View**

The **Custom Fields Form** widget is now supported in Playbook View.

---
## 2025-07-27

### Feature

**Automate tasks with Playbook Loops**

This feature is in Preview.

Playbook functionality has been enhanced to include **Playbook Loops**. This feature update lets playbooks iterate over lists or entities, performing one or more actions for each item. It streamlines automation by eliminating the need for duplicated steps or custom actions when processing multiple items. You can configure Playbook Loops directly within a playbook or inside a playbook block.

For setup instructions and use case examples , see [Automate tasks with Playbook Loops](https://cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-loops).

### Feature

**Playbook Simulator enhancements for loops**

The Playbook Simulator now supports visualization and debugging of playbooks that contain loops. This lets you clearly see and navigate through each loop iteration within the simulator viewer.

Additionally, the step display order has been updated to show actions from top to bottom (oldest at the top, newest at the bottom), with automatic scrolling to the most recent activity.

For more details, see [Loops in the Playbook Simulator](https://cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-loops#loops-in-the-playbook-simulator).

---
## 2025-07-22

### Feature

**Silent Host Monitoring**

New configuration options are now available for Silent Host Monitoring. You can now define detection rule-based Silent Host Monitoring in SecOps using UDM fields or labels, configurable within a specified time window.

For more information, see [Silent host monitoring](https://cloud.google.com/chronicle/docs/ingestion/silent-host-monitoring).

---
## 2025-07-21

### Feature

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

[Collect Apache Tomcat logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/tomcat)

[Collect Appian Cloud logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/appian-cloud)

[Collect Archer IRM logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/archer-irm)

[Collect ArcSight CEF logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/arcsight-cef)

[Collect Area 1 logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/area1)

[Collect Aruba EdgeConnect SD-WAN logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba)

[Collect Atlassian Cloud Admin Audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-audit)

[Collect Avatier logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/avatier)

[Collect Avigilon Access Control Manager logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/avigilon-access-logs)

[Collect AWS CloudTrail logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-aws-logs-into-chronicle)

[Collect Barracuda CloudGen Firewall logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-cloudgen-firewall)

[Collect Barracuda Web Filter logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-webfilter)

[Collect Broadcom CA PAM logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ca-pam)

[Collect Broadcom SSL VA logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ssl-va)

[Collect Cato Networks logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cato-networks)

[Collect Check Point Harmony logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-harmony)

[Collect CipherTrust Manager logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/ciphertrust-manager)

[Collect Cisco VCS logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-vcs)

[Collect Cisco VPN logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-vpn)

[Collect Cisco WSA logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsa)

[Collect CyberArk Privilege Cloud logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-privilege-cloud)

[Collect Digi Modems logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/digi-modems)

[Collect F5 DNS logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/F5-dns)

[Collect F5 VPN logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/F5-vpn)

[Collect Forcepoint CASB logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-casb)

[Collect HPE BladeSystem c7000 logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/hpe-bladesystem-c7000)

[Collect Skyhigh Security logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/skyhigh-security)

[Collect Trellix IPS logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-ips)

---
## 2025-07-07

### Feature

**Dashboards for enhanced visualizations and threat hunting**

You can now use the Google SecOps Dashboards to enhance data visualization, investigations, and threat hunting.

Key capabilities include:

* SOAR data availability
* Downloadable reports
* Custom drilldowns
* Markdown widgets
* 51 curated dashboards covering a broad range of security categories and use cases.

For more information, see [Dashboards](https://cloud.google.com/chronicle/docs/reports/native-dashboards).

---
## 2025-07-05

### Feature

**Share Case Queue Filters**

You can now share case queue filters with other users. These filters can be saved with specific criteria, such as assignee roles, and shared with individual users, SOC roles, or all users in your organization for quick access.

For more information, see [Apply and save filters](https://cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/apply-and-save-filters).

---
## 2025-07-02

### Changed

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have been updated. Each parser is listed by product name and `log_type` value, where applicable. This list includes both released default parsers and pending parser updates.

* 1Password (`ONEPASSWORD`)
* Apache (`APACHE`)
* Arcsight CEF (`ARCSIGHT_CEF`)
* Aruba Switch (`ARUBA_SWITCH`)
* AWS Cloudtrail (`AWS_CLOUDTRAIL`)
* AWS CloudWatch (`AWS_CLOUDWATCH`)
* AWS GuardDuty (`GUARDDUTY`)
* AWS Lambda Function (`AWS_LAMBDA_FUNCTION`)
* AWS S3 Server Access (`AWS_S3_SERVER_ACCESS`)
* AWS VPC Flow (`AWS_VPC_FLOW`)
* AWS VPC Flow (CSV) (`AWS_VPC_FLOW_CSV`)
* Azure AD (`AZURE_AD`)
* Azure Application Gateway (`AZURE_GATEWAY`)
* Azure Firewall (`AZURE_FIREWALL`)
* Azure Storage Audit (`AZURE_STORAGE_AUDIT`)
* Azure VNET Flow (`AZURE_VNET_FLOW`)
* BIND (`BIND_DNS`)
* Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
* Brocade Switch (`BROCADE_SWITCH`)
* Carbon Black (`CB_EDR`)
* Carbon Black App Control (`CB_APP_CONTROL`)
* Check Point (`CHECKPOINT_FIREWALL`)
* Chronicle SOAR Audit (`CHRONICLE_SOAR_AUDIT`)
* Cisco Application Centric Infrastructure (`CISCO_ACI`)
* Cisco ASA (`CISCO_ASA_FIREWALL`)
* Cisco Email Security (`CISCO_EMAIL_SECURITY`)
* Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
* Cisco Internetwork Operating System (`CISCO_IOS`)
* Cisco IronPort (`CISCO_IRONPORT`)
* Cisco ISE (`CISCO_ISE`)
* Cisco NX-OS (`CISCO_NX_OS`)
* Cisco Router (`CISCO_ROUTER`)
* Cisco Umbrella Web Proxy (`UMBRELLA_WEBPROXY`)
* Cisco vManage SD-WAN (`CISCO_SDWAN`)
* Citrix Netscaler (`CITRIX_NETSCALER`)
* Claroty Continuous Threat Detection (`CLAROTY_CTD`)
* Cloudflare (`CLOUDFLARE`)
* CrowdStrike Detection Monitoring (`CS_DETECTS`)
* CrowdStrike Falcon (`CS_EDR`)
* Crowdstrike IOC (`CROWDSTRIKE_IOC`)
* Custom Security Data Analytics (`CUSTOM_SECURITY_DATA_ANALYTICS`)
* CyberArk Endpoint Privilege Manager (EPM) (`CYBERARK_EPM`)
* Cyberark Privilege Cloud (`CYBERARK_PRIVILEGE_CLOUD`)
* Darktrace (`DARKTRACE`)
* Datadog (`DATADOG`)
* Dell Switch (`DELL_SWITCH`)
* Elastic Defend (`ELASTIC_DEFEND`)
* ESET AV (`ESET_AV`)
* ExtraHop RevealX (`EXTRAHOP`)
* F5 Advanced Firewall Management (`F5_AFM`)
* F5 ASM (`F5_ASM`)
* FireEye ETP (`FIREEYE_ETP`)
* FireEye NX (`FIREEYE_NX`)
* FortiGate (`FORTINET_FIREWALL`)
* Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
* Fortinet Web Application Firewall (`FORTINET_FORTIWEB`)
* GitHub (`GITHUB`)
* Guardicore Centra (`GUARDICORE_CENTRA`)
* H3C Comware Platform Switch (`H3C_SWITCH`)
* IBM Cloud Activity Tracker (`IBM_CLOUD_ACTIVITY_TRACKER`)
* IBM Security Verify Access (`IBM_SVA`)
* IBM zSecure Alert (`IBM_ZSECURE_ALERT`)
* Imperva (`IMPERVA_WAF`)
* Infoblox (`INFOBLOX`)
* Infoblox DHCP (`INFOBLOX_DHCP`)
* KnowBe4 PhishER (`KNOWBE4_PHISHER`)
* LastPass Password Management (`LASTPASS`)
* Linux Auditing System (AuditD) (`AUDITD`)
* Microsoft AD (`WINDOWS_AD`)
* Microsoft AD FS (`ADFS`)
* Microsoft Azure Activity (`AZURE_ACTIVITY`)
* Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
* Microsoft Graph API Alerts (`MICROSOFT_GRAPH_ALERT`)
* Microsoft IIS (`IIS`)
* Netskope V2 (`NETSKOPE_ALERT_V2`)
* NGINX (`NGINX`)
* Nozomi Networks Scada Guardian (`NOZOMI_GUARDIAN`)
* Office 365 (`OFFICE_365`)
* Okta (`OKTA`)
* Openpath (`OPENPATH`)
* Opnsense (`OPNSENSE`)
* Palo Alto Cortex XDR Alerts (`CORTEX_XDR`)
* Palo Alto Cortex XDR Events (`PAN_CORTEX_XDR_EVENTS`)
* Palo Alto Networks Firewall (`PAN_FIREWALL`)
* Palo Alto Panorama (`PAN_PANORAMA`)
* Palo Alto Prisma Access (`PAN_CASB`)
* Ping Federate (`PING_FEDERATE`)
* Ping Identity (`PING`)
* PostgreSQL (`POSTGRESQL`)
* Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
* Proofpoint Threat Response (`PROOFPOINT_TRAP`)
* Radware Web Application Firewall (`RADWARE_FIREWALL`)
* Red Hat OpenShift (`REDHAT_OPENSHIFT`)
* Remediant SecureONE (`REMEDIANT_SECUREONE`)
* Riverbed Steelhead (`STEELHEAD`)
* SailPoint IAM (`SAILPOINT_IAM`)
* Security Command Center Posture Violation (`GCP_SECURITYCENTER_POSTURE_VIOLATION`)
* Security Command Center Threat (`N/A`)
* Security Command Center Toxic Combination (`GCP_SECURITYCENTER_TOXIC_COMBINATION`)
* Symantec DLP (`SYMANTEC_DLP`)
* Sysdig (`SYSDIG`)
* Teradata DB (`TERADATA_DB`)
* Terraform Enterprise Audit (`TERRAFORM_ENTERPRISE`)
* Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
* Tripwire (`TRIPWIRE_FIM`)
* Vectra Detect (`VECTRA_DETECT`)
* Vectra Stream (`VECTRA_STREAM`)
* Versa Firewall (`VERSA_FIREWALL`)
* VMware AirWatch (`AIRWATCH`)
* VMware ESXi (`VMWARE_ESX`)
* Voltage (`VOLTAGE`)
* WatchGuard (`WATCHGUARD`)
* Windows DHCP (`WINDOWS_DHCP`)
* Windows Event (`WINEVTLOG`)
* Windows Event (XML) (`WINEVTLOG_XML`)
* Windows Hyper-V (`WINDOWS_HYPERV`)
* wiz.io (`WIZ_IO`)
* Workday (`WORKDAY`)
* Workspace Activities (`WORKSPACE_ACTIVITY`)
* Zscaler (`ZSCALER_WEBPROXY`)
* Zscaler CASB (`ZSCALER_CASB`)
* ZScaler Deception (`ZSCALER_DECEPTION`)
* Zscaler DLP (`ZSCALER_DLP`)
* Zscaler Tunnel (`ZSCALER_TUNNEL`)

The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, where applicable.

* Akamai Kona Edge Grid (`AKAMAI_KONA_EDGE_GRID`)
* Azure Compute (`AZURE_COMPUTE`)
* Bluecat Micetro IP Address Management (`BLUECAT_MICETRO_IPAM`)
* Cloudera Ranger (`CLOUDERA_RANGER`)
* Cyberark Identity (`CYBERARK_IDENTITY`)
* Fortinet FortiDLP (`FORTINET_FORTIDLP`)
* IBM Cognos Analytics (`IBM_COGNOS`)
* IBM Planning Analytics (`IBM_PA`)
* Ironclad (`IRONCLAD`)
* Ivanti Endpoint Manager Mobile (`IVANTI_ENDPOINT_MANAGER_MOBILE`)
* Mimecast Mail V2 (`MIMECAST_MAIL_V2`)
* Minsait Sigefi (`MINSAIT_SIGEFI`)
* Netskope One Secure SD-WAN (`NETSKOPE_SDWAN`)
* Proxmox (`PROXMOX`)
* Radware Bot (`RADWARE_BOT`)
* ScaleFusion for Windows MDM (`SCALEFUSION`)
* Titan SFTP Server (`TITAN_SFTP`)
* ZoomInfo (`ZOOMINFO`)
* Zscaler Email DLP Insights (`ZSCALER_EMAIL_DLP_INSIGHTS`)

For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

---
## 2025-06-30

### Changed

[Data tables](https://cloud.google.com/chronicle/docs/investigation/data-tables) are multicolumn constructs that let you input your own data into Google SecOps. You can create or import data tables to your Google SecOps account using the Google SecOps UI, the Data Tables API, or by using YARA-L queries in rules. This feature is now available to all customers.

What's new for this release:

* Multiple web interface enhancements have been made, including a new default table view for data table management.
* Support for the `number` data type is now available for data table columns.
* Support for repeated fields in data table columns.
* The [Limitations](https://cloud.google.com/chronicle/docs/investigation/data-tables#limitations) section has additional details.

---
## 2025-06-26

### Announcement

**Premium [Fortinet Firewall parser](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fw) now available as Release Candidate**

This enhanced parser is available as a **Release Candidate** for the next 3 months. To opt in and begin testing it, go to **SIEM Settings > Parsers**. We encourage you to try it out and evaluate the improvements before it becomes the default.

---
## 2025-06-23

### Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

[Collect BeyondTrust BeyondInsight logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/beyond-trust-beyondinsight)

[Collect BloxOne Threat Defense logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/bloxone)

[Collect BlueCat Edge DNS Resolver logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-edge)

[Collect Cambium Networks logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cambium-networks)

[Collect Check Point Audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-audit)

[Collect Check Point EDR logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-edr)

[Collect Check Point SmartDefense logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-smartdefense)

[Collect Commvault logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/commvault)

[Collect Comodo AV logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/comodo-av)

[Collect Cylance PROTECT logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cylance-protect)

[Collect Cyolo OT logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cyolo-ot)

[Collect Delinea PAM logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/delinea-pam)

[Collect Dell CyberSense logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-cybersense)

[Collect Dell EMC Data Domain logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-data-domain)

[Collect Dell EMC Isilon NAS logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-isilon-nas)

[Collect Dell EMC PowerStore logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-powerstore)

[Collect Dell OpenManage logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-openmanage)

[Collect Endpoint Protector DLP logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/endpoint-protector-dlp)

[Collect ESET AV logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-av)

[Collect ESET EDR logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/eset-edr)

[Collect F5 AFM logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/F5-afm)

[Collect F5 ASM logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/F5-asm)

[Collect FileZilla FTP logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/filezilla-ftp)

[Collect Forescout NAC logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/forescout-nac)

[Collect ForgeRock OpenAM logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-openam)

[Collect HAProxy logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/haproxy)

[Collect Kaseya Datto File Protection logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/kaseya-datto-file-protection)

[Collect ManageEngine AD360 logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/manage-engine-ad360)

[Collect Palo Alto Cortex XDR Events logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/cortex-xdr-events)

[Collect Snowflake logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/snowflake)

[Collect Trellix DLP logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-dlp)

[Collect Trellix ePO logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-epo)

[Collect Trend Micro DDI logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-ddi)

[Collect Trend Micro Email Security logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-security)

[Collect Trend Micro Vision One Activity logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-activity)

[Collect Trend Micro Vision One Audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-audit)

[Collect Trend Micro Vision One Container Vulnerability logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-container-vulnerability)

[Collect Trend Micro Vision One Detections logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-detections)

[Collect Trend Micro Vision One Observed Attack Techniques logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-observed-attack-techniques)

[Collect Trend Micro Vision One Workbench logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/trend-micro-vision-one-workbench)

---
## 2025-06-19

### Feature

**Content Hub**

This feature is currently in Preview.

The new Content Hub page offers a centralized experience for managing all your Google SecOps content needs. On this page, you can do the following:

* Onboard Google SecOps content using content packs for top data sources
* View and manage native dashboards.
* Access and configure search queries.
* View, filter, and review curated detections rule logic.
* Configure response integrations.
* Install and run power ups.

For more information, see [Google SecOps Content Hub](https://cloud.google.com/chronicle/docs/secops/content_hub).

### Feature

**Product Centric Feed Management**

This feature is currently in Preview.

You can now configure multiple log-type feeds for the same product type on a single page. This new product-led experience simplifies the feed configuration flow and provides additional in-product guidance. For more information, see [Configure feeds by product](https://cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

---
## 2025-06-18

### Feature

You can now remove existing UDM field mappings by using parser extensions in Google SecOps.

For more information, see [Remove UDM field mappings using parser extensions](https://cloud.google.com/chronicle/docs/event-processing/using-parser-extensions#remove_udm_field_mappings_using_parser_extensions) and [Code snippet - Remove existing mappings](https://cloud.google.com/chronicle/docs/event-processing/parser-extension-examples#code_snippet_remove_existing_mappings)

### Feature

New data ingestion and health dashboard widgets are now available.

* **Silent host monitoring**: displays hosts that were active in the last 7 days, but haven't reported recently, including a count of days since their last ingestion.
* **BindPlane agent logging and health**: visualizes logging activity and agent health. Requires Bindplane agent logs to be ingested into Google SecOps.
* **Throughput in bytes**: shows ingestion volume over time.
* **Improved log type distribution charts**: updates charts for better readability and usability.

---
## 2025-06-16

### Announcement

The Release Candidate period of the following premium parsers has been extended from the end of May to the week of July 21, 2025:

* Crowdstrike Detection Monitoring (CS\_DETECTS)
* Crowdstrike Falcon (CS\_EDR)
* Microsoft Defender for Endpoint

We recommend that you opt-in early and make any necessary adjustments before these updates become the default.

---
## 2025-06-08

### Feature

**Playbook Permissions: Support for API Key Roles**

The platform has been updated to extend playbook permissions to also support the SOC Roles associated with API keys, in addition to the user SOC Roles.

This enhancement affects how integrations using API keys interact with playbooks that have specific permission configurations. For example, GitSync now uses this capability to synchronize playbooks with restricted permissions.

For more information on how playbook permissions work with users and API keys, see [Playbook permissions](http://cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-permissions).

For specific instructions on configuring GitSync with restricted playbooks, see [GitSync - Work with playbook permissions](https://cloud.google.com/chronicle/docs/soar/marketplace/power-ups/gitsync#work-with-playbook-permissions).

### Feature

**Advanced Reports: Case Custom Fields**

Advanced Reports (Looker) has been enhanced to include support for custom fields created for Cases.

This enhancement allows users to leverage organization-specific data captured in custom fields to gain deeper insights and create tailored visualizations within Looker reports. Specific LookML formulas and filtering guidance are now available.

For more information on how to use custom fields in Advanced Reports, see [Use Custom Fields in Advanced Reports](https://cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/adding-custom-fields#use-custom-fields-in-advanced-reports).

---
## 2025-06-04

### Announcement

The following parser documentation is now available:

[Collect Abnormal Security logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/abnormal-security)

[Collect Apache Cassandra logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/apache-cassandra)

[Collect Darktrace logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/darktrace)

[Collect Nix Systems Ubuntu Server (Unix System) logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/nix-systems-ubuntu)

[Collect 1Password logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword)

[Collect 1Password audit logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword-audit-events)

[Collect Symantec Endpoint Protection logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-endpoint-protection)

[Collect Symantec VIP Authentication Hub logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-vip-authhub)

[Collect Symantec VIP Enterprise Gateway logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-vip)

[Collect Symantec Web Isolation logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-web-isolation)

[Collect Varonis logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/varonis)

[Collect Oracle DB logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-db)

[Collect Akeyless Vault logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/akeyless-vault)

[Collect Attivo Networks BOTsink logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/attivo)

[Collect Avaya Aura logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/avaya-aura)

[Collect BeyondTrust Endpoint Privilege Management logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-epm)

[Collect BeyondTrust Privileged Identity logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-pi)

[Collect Blue Coat ProxySG logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecoat-proxysg)

[Collect Microsoft Exchange logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-exchange)

[Collect MYSQL logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/mysql)

[Collect Signal Sciences WAF logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/signal-sciences-waf)

[Collect Symantec CloudSOC CASB logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-cloudsoc-casb)

---
## 2025-06-03

### Fixed

**User interface fixes**

There was an issue with highlighting regular expressions in **Search** and **Rules Editor**. Once you entered a regular expression, all subsequent text on the line would be highlighted as if it was also a regular expression (whether it was or wasn't). This issue has been fixed. Note that both string literals (specified with back ticks) and regular expressions are highlighted in the same color.

There was an issue with uppercase keywords in **Search** and **Rules Editor**. They weren't being highlighted correctly. This issue has been fixed.

---
## 2025-05-29

### Changed

Google SecOps has updated the list of supported default parsers. Parsers are updated gradually, so it might take one to four days before you see the changes reflected in your region.

The following supported default parsers have changed. Each parser is listed by product name and `log_type` value, if applicable. This list now includes both released default parsers and pending parser updates.

* AIX system (`AIX_SYSTEM`)
* Akamai WAF (`AKAMAI_WAF`)
* Apache (`APACHE`)
* Appian Cloud (`APPIAN_CLOUD`)
* Auth0 (`AUTH_ZERO`)
* AWS CloudFront (`AWS_CLOUDFRONT`)
* AWS Cloudtrail (`AWS_CLOUDTRAIL`)
* AWS GuardDuty (`GUARDDUTY`)
* AWS Macie (`AWS_MACIE`)
* AWS Session Manager (`AWS_SESSION_MANAGER`)
* AWS VPC Flow (`AWS_VPC_FLOW`)
* AWS VPC Flow (CSV) (`AWS_VPC_FLOW_CSV`)
* Azure AD (`AZURE_AD`)
* Azure AD Organizational Context (`AZURE_AD_CONTEXT`)
* Azure Firewall (`AZURE_FIREWALL`)
* Azure Storage Audit (`AZURE_STORAGE_AUDIT`)
* Barracuda Firewall (`BARRACUDA_FIREWALL`)
* BeyondTrust BeyondInsight (`BEYONDTRUST_BEYONDINSIGHT`)
* BIND (`BIND_DNS`)
* Bitdefender (`BITDEFENDER`)
* Blue Coat Proxy (`BLUECOAT_WEBPROXY`)
* Brocade Switch (`BROCADE_SWITCH`)
* Carbon Black (`CB_EDR`)
* CircleCI (`CIRCLECI`)
* Cisco ASA (`CISCO_ASA_FIREWALL`)
* Cisco Firepower NGFW (`CISCO_FIREPOWER_FIREWALL`)
* Cisco Internetwork Operating System (`CISCO_IOS`)
* Cisco ISE (`CISCO_ISE`)
* Cisco NX-OS (`CISCO_NX_OS`)
* Cisco Prime (`CISCO_PRIME`)
* Cisco Switch (`CISCO_SWITCH`)
* Cisco Unity Connection (`CISCO_UNITY_CONNECTION`)
* Cloud Audit Logs (`N/A`)
* CrowdStrike Alerts API (`CS_ALERTS`)
* CrowdStrike Falcon (`CS_EDR`)
* CyberArk Endpoint Privilege Manager (EPM) (`CYBERARK_EPM`)
* CyberArk Privileged Access Manager (PAM) (`CYBERARK_PAM`)
* Cylance Protect (`CYLANCE_PROTECT`)
* Darktrace (`DARKTRACE`)
* Dell OpenManage (`DELL_OPENMANAGE`)
* EfficientIP DDI (`EFFICIENTIP_DDI`)
* Elastic Defend (`ELASTIC_DEFEND`)
* Elastic Windows Event Log Beats (`ELASTIC_WINLOGBEAT`)
* ExtraHop RevealX (`EXTRAHOP`)
* F5 ASM (`F5_ASM`)
* F5 BIGIP LTM (`F5_BIGIP_LTM`)
* F5 DNS (`F5_DNS`)
* Fastly WAF (`FASTLY_WAF`)
* FireEye HX (`FIREEYE_HX`)
* FortiGate (`FORTINET_FIREWALL`)
* Fortinet FortiAnalyzer (`FORTINET_FORTIANALYZER`)
* Fortinet FortiAuthenticator (`FORTINET_FORTIAUTHENTICATOR`)
* Fortinet FortiNAC (`FORTINET_FORTINAC`)
* Fortinet Web Application Firewall (`FORTINET_FORTIWEB`)
* GitHub (`GITHUB`)
* Gitlab (`GITLAB`)
* HP Aruba (ClearPass) (`CLEARPASS`)
* Ipswitch SFTP (`IPSWITCH_SFTP`)
* Juniper (`JUNIPER_FIREWALL`)
* Linux Auditing System (AuditD) (`AUDITD`)
* ManageEngine ADManager Plus (`ADMANAGER_PLUS`)
* McAfee ePolicy Orchestrator (`MCAFEE_EPO`)
* Microsoft AD FS (`ADFS`)
* Microsoft Defender for Endpoint (`MICROSOFT_DEFENDER_ENDPOINT`)
* Microsoft Defender for Identity (`MICROSOFT_DEFENDER_IDENTITY`)
* Microsoft IIS (`IIS`)
* Microsoft PowerShell (`POWERSHELL`)
* Netskope Web Proxy (`NETSKOPE_WEBPROXY`)
* Nokia Router (`NOKIA_ROUTER`)
* Office 365 (`OFFICE_365`)
* Oracle (`ORACLE_DB`)
* Palo Alto Cortex XDR Events (`PAN_CORTEX_XDR_EVENTS`)
* Palo Alto Prisma Access (`PAN_CASB`)
* Ping Federate (`PING_FEDERATE`)
* Ping Identity (`PING`)
* Proofpoint Tap Alerts (`PROOFPOINT_MAIL`)
* Radware Web Application Firewall (`RADWARE_FIREWALL`)
* ServiceNow Audit (`SERVICENOW_AUDIT`)
* Snare System Diagnostic Logs (`SNARE_SOLUTIONS`)
* Symantec DLP (`SYMANTEC_DLP`)
* Symantec Security Analytics (`SYMANTEC_SA`)
* Sysdig (`SYSDIG`)
* Tanium Question (`TANIUM_QUESTION`)
* Trend Micro Vision One (`TRENDMICRO_VISION_ONE`)
* Trend Micro Vision One Workbench (`TRENDMICRO_VISION_ONE_WORKBENCH`)
* TrendMicro Deep Discovery Inspector (`TRENDMICRO_DDI`)
* VanDyke SFTP (`VANDYKE_SFTP`)
* Vectra Detect (`VECTRA_DETECT`)
* Vectra Stream (`VECTRA_STREAM`)
* Vectra XDR (`VECTRA_XDR`)
* VMware ESXi (`VMWARE_ESX`)
* VMWare VSphere (`VMWARE_VSPHERE`)
* WatchGuard (`WATCHGUARD`)
* Windows Event (XML) (`WINEVTLOG_XML`)
* Workspace Activities (`WORKSPACE_ACTIVITY`)
* Zscaler (`ZSCALER_WEBPROXY`)
* Zscaler CASB (`ZSCALER_CASB`)
* Zscaler DLP (`ZSCALER_DLP`)
* ZScaler DNS (`ZSCALER_DNS`)
* Zscaler Internet Access Audit Logs (`ZSCALER_INTERNET_ACCESS`)
* ZScaler NGFW (`ZSCALER_FIREWALL`)
* Zscaler Private Access (`ZSCALER_ZPA`)
* Zscaler Secure Private Access Audit Logs (`ZSCALER_ZPA_AUDIT`)
* Zscaler Tunnel (`ZSCALER_TUNNEL`)

The following log types were added without a default parser. Each parser is listed by product name and `log_type` value, if applicable.

* Azure App Configuration (`AZURE_APPCONFIGURATION`)
* Azure App Platform (`AZURE_APPPLATFORM`)
* Azure ArcData (`AZURE_ARCDATA`)
* Azure Authorization (`AZURE_AUTHORIZATION`)
* Azure Change Analysis (`AZURE_CHANGEANALYSIS`)
* Azure DataFactory (`AZURE_DATAFACTORY`)
* Doppel (`DOPPEL`)
* Genian NAC (`GENIAN_NAC`)
* Penta Security Wapples (`PENTA_WAPPLES`)
* Redmine (`REDMINE`)
* S2W Quaxar (`S2W_QUAXAR`)
* SecurityBridge Dev (`SECURITYBRIDGE_DEV`)
* TeamT5 ThreatSonar EDR (`TEAMT5_THREATSONAR_EDR`)
* WorkDay User Sign In (`WORKDAY_USER_SIGNIN`)

For a list of supported log types and details about default parser changes, see [Supported log types and default parsers](https://cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

---
