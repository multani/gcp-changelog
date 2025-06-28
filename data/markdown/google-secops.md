# Google SecOps

## 2025-06-23

### Announcement

**New parser documentation now available**

New parser documentation is available to help you ingest and normalize logs from the following sources:

[Collect BeyondTrust BeyondInsight logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/beyond-trust-beyondinsight)

[Collect BloxOne Threat Defense logs](https://cloud.google.com/chronicle/docs/ingestion/default-parsers/bloxone)

[Collect BlueCat Edge DNS Resolver logs](https://cloud.devsite.corp.google.com/chronicle/docs/ingestion/default-parsers/bluecat-edge)

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

## 2025-06-16

### Announcement

The Release Candidate period of the following premium parsers has been extended from the end of May to the week of July 21, 2025:

* Crowdstrike Detection Monitoring (CS\_DETECTS)
* Crowdstrike Falcon (CS\_EDR)
* Microsoft Defender for Endpoint

We recommend that you opt-in early and make any necessary adjustments before these updates become the default.

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

## 2025-06-03

### Fixed

**User interface fixes**

There was an issue with highlighting regular expressions in **Search** and **Rules Editor**. Once you entered a regular expression, all subsequent text on the line would be highlighted as if it was also a regular expression (whether it was or wasn't). This issue has been fixed. Note that both string literals (specified with back ticks) and regular expressions are highlighted in the same color.

There was an issue with uppercase keywords in **Search** and **Rules Editor**. They weren't being highlighted correctly. This issue has been fixed.

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

