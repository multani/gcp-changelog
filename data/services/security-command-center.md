# Security Command Center

## 2025-07-10

### Changed

In the Google Cloud console, the [Google Kubernetes Engine (GKE) security posture dashboard](https://cloud.google.com/security-command-center/docs/concepts-security-sources#gke-security-posture-dashboard) shows the top software vulnerabilities that affect your GKE workloads. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-07-01

### Changed

Security Command Center now supports the [detection of Chokepoints](https://cloud.google.com/security-command-center/docs/toxic-combinations-overview) for the following cloud service provider platforms:

* Amazon Web Services (AWS)
* Microsoft Azure

Support for Chokepoints with Microsoft Azure and AWS is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-06-30

### Feature

You can download risk reports as PDFs. Risk reports help you understand the results of the attack path simulations (virtual red teaming) that Security Command Center runs. This feature is in [Preview](http://cloud.google.com/products#product-launch-stages) and is available for customers on the Enterprise or Premium service tiers. For more information, see [Risk reports overview](https://cloud.google.com/security-command-center/docs/risk-reports-overview).

### Feature

The following [Virtual Machine Threat Detection](https://cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview) detectors are in [General Availability](https://cloud.google.com/products#product-launch-stages).

* `Defense Evasion: Unexpected ftrace handler`
* `Defense Evasion: Unexpected interrupt handler`
* `Defense Evasion: Unexpected kernel modules`
* `Defense Evasion: Unexpected kernel read-only data modification`
* `Defense Evasion: Unexpected kprobe handler`
* `Defense Evasion: Unexpected processes in runqueue`
* `Defense Evasion: Unexpected system call handler`

### Deprecated

The `Defense Evasion: Unexpected kernel code modification` detector of Virtual Machine Threat Detection is shut down. For more information, see [Detector shutdowns](https://cloud.google.com/security-command-center/docs/deprecations).

---
## 2025-06-27

### Changed

The following [Event Threat Detection](https://cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) detectors have been released to [GA](https://cloud.google.com/products#product-launch-stages).

* `Exfiltration: Cloud SQL Data Exfiltration`
* `Credential Access: CloudDB Failed login from Anonymizing Proxy IP`
* `Initial Access: CloudDB Successful login from Anonymizing Proxy IP`

---
## 2025-06-20

### Changed

The display name for the following [Event Threat Detection](https://cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) rules have changed. Please update any artifacts that use these values, such as finding filters, finding queries, or mute rules.

| Previous display name | New display name |
| --- | --- |
| `Defensive Evasion: Static Pod Created` | `Defense Evasion: Static Pod Created` |
| `Data Destruction: Deleted Google Cloud Backup and DR Backup` | `Impact: Deleted Google Cloud Backup and DR Backup` |
| `Inhibit System Recovery: Deleted Google Cloud Backup and DR host` | `Impact: Deleted Google Cloud Backup and DR host` |
| `Inhibit System Recovery: Deleted Google Cloud Backup and DR plan association` | `Impact: Deleted Google Cloud Backup and DR plan association` |
| `Inhibit System Recovery: Deleted Google Cloud Backup and DR Vault` | `Impact: Deleted Google Cloud Backup and DR Vault` |
| `Inhibit System Recovery: Google Cloud Backup and DR delete policy` | `Impact: Google Cloud Backup and DR delete policy` |
| `Inhibit System Recovery: Google Cloud Backup and DR delete profile` | `Impact: Google Cloud Backup and DR delete profile` |
| `Inhibit System Recovery: Google Cloud Backup and DR delete storage pool` | `Impact: Google Cloud Backup and DR delete storage pool` |
| `Inhibit System Recovery: Google Cloud Backup and DR delete template` | `Impact: Google Cloud Backup and DR delete template` |
| `Data Destruction: Google Cloud Backup and DR expire image` | `Impact: Google Cloud Backup and DR expire image` |
| `Data Destruction: Google Cloud Backup and DR remove appliance` | `Impact: Google Cloud Backup and DR remove appliance` |
| `Inhibit System Recovery: Google Cloud Backup and DR remove plan` | `Impact: Google Cloud Backup and DR remove plan` |
| `Impair Defenses: Strong Authentication Disabled` | `Persistence: Strong Authentication Disabled` |
| `Credential Access: External Member Added To Privileged Group` | `Privilege Escalation: External Member Added To Privileged Group` |
| `Persistence: Impersonation Role Granted For Dormant Service Account` | `Privilege Escalation: Impersonation Role Granted For Dormant Service Account` |
| `Credential Access: Privileged Group Opened To Public` | `Privilege Escalation: Privileged Group Opened To Public` |
| `Credential Access: Sensitive Role Granted To Hybrid Group` | `Privilege Escalation: Sensitive Role Granted To Hybrid Group` |

### Changed

Risk Engine includes the `aiplatform.googleapis.com/Model` resource type in the default high-value resource set. For more information, see the [list of default resource types](https://cloud.google.com/security-command-center/docs/attack-exposure-learn#default-high-value-resource-set).

---
## 2025-06-19

### Changed

The prompt injection and jailbreak detection filter in Model Armor flags more threats across various attack vectors, and offers an improved detection rate for high-confidence malicious prompts. This filter is available in us-east1.

### Changed

**CVEs with no known exploitation activity are not considered in attack path simulations**

Vulnerability findings in Security Command Center are enriched by Mandiant Threat Intelligence. A CVE with wide exploitation activity is more likely to be used in an attack path compared to a CVE with only anticipated exploitation activity. Vulnerabilities with no known exploitation activity are not considered in attack path simulations. For more information, see [Incorporation of CVE data](https://cloud.google.com/security-command-center/docs/attack-exposure-learn#incorporation_of_cve_data).

---
## 2025-06-18

### Announcement

The **Set security marks** option in the [new Security Command Center Enterprise Findings and Assets pages](https://cloud.google.com/security-command-center/docs/release-notes#May_08_2025) is temporarily unavailable. You can opt-out of the new Security Command Center Enterprise experience to manage security marks using the Cloud console. Or, you can manage security marks using the [Security Command Center API](https://cloud.google.com/security-command-center/docs/how-to-api-add-manage-security-marks).

---
## 2025-06-13

### Feature

The following [Event Threat Detection](https://cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) detectors for Vertex AI have been released to [Preview](https://cloud.google.com/products#product-launch-stages):

* `Persistence: New Geography for AI Service`
* `Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Admin Activity`
* `Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Data Access`
* `Privilege Escalation: Anomalous Service Account Impersonator for AI Admin Activity`
* `Privilege Escalation: Anomalous Service Account Impersonator for AI Data Access`
* `Privilege Escalation: Anomalous Impersonation of Service Account for AI Admin Activity`
* `Persistence: New AI API Method`
* `Initial Access: Dormant Service Account Activity in AI Service`

---
## 2025-06-08

### Feature

Model Armor supports screening text in the following document types for malicious content.

* DOCX, DOCM, DOTX, DOTM documents
* PPTX, PPTM, POTX, POT presentations
* XLSX, XLSM, XLTX, XLTM spreadsheets

### Feature

**Multi-language support for Model Armor filters**

The Responsible AI and prompt injection and jailbreak detection filters are tested in English, Spanish, French, Italian, Portuguese, German, Chinese (Mandarin), Japanese, and Korean. These filters can work in other languages, but the quality of results might vary.

For more information, see [Languages supported](https://cloud.google.com/security-command-center/docs/model-armor-overview#languages-supported).

---
## 2025-06-06

### Changed

The [Security Risk Overview dashboard for Compute Engine](https://cloud.google.com/compute/docs/monitor-security-risks-console) is in [General Availability](https://cloud.google.com/products#product-launch-stages). In addition, it provides a **Top CVE findings** table that lists the most severe CVEs that affect your Compute Engine instances.

---
## 2025-06-05

### Feature

[Vulnerability Assessment for Google Cloud](https://cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud) supports scanning on Google Kubernetes Engine (GKE) nodes and containers. This feature has been released to [Preview](https://cloud.google.com/products#product-launch-stages).

### Changed

Muted findings are no longer considered in the Security Command Center Risk Engine. As a result, they no longer get [attack exposure scores](https://cloud.google.com/security-command-center/docs/attack-exposure-learn).

---
## 2025-06-04

### Feature

Security Command Center Premium customers can now access toxic combinations, which are in [General Availability](https://cloud.google.com/products#product-launch-stages), and chokepoints, which are in [Preview](https://cloud.google.com/products?e=48754805#product-launch-stages). These are available at the organization level. For more information, see [Toxic combinations and chokepoints overview](https://cloud.google.com/security-command-center/docs/toxic-combinations-overview).

---
## 2025-06-03

### Feature

The following [Container Threat Detection](https://cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) detectors for Google Kubernetes Engine have been released to [General Availability](https://cloud.google.com/products#product-launch-stages):

* `Credential Access: Find Google Cloud Credentials`
* `Credential Access: GPG Key Reconnaissance`
* `Defense Evasion: Base64 ELF File Command Line`
* `Defense Evasion: Base64 Encoded Python Script Executed`
* `Defense Evasion: Base64 Encoded Shell Script Executed`
* `Execution: Fileless Execution in /memfd:`
* `Execution: Suspicious OpenSSL Shared Object Loaded`
* `Privilege Escalation: Fileless Execution in /dev/shm`

---
## 2025-05-29

### Changed

Domain tagging for [toxic combinations and chokepoints](https://cloud.google.com/security-command-center/docs/toxic-combinations-overview) has been improved to be more precise. The following filters are available for [issues](https://cloud.google.com/security-command-center/docs/issues-overview):

* CVE Vulnerabilities
* Identity
* Data
* AI Security

---
## 2025-05-28

### Changed

**Model Armor enhancements**

* Model Armor supports multi-regional endpoints. For more information, see [Locations for the Model Armor API](https://cloud.google.com/security-command-center/docs/regional-endpoints#locations-model-armor).
* All Model Armor filters support up to 2,000 tokens.

---
## 2025-05-27

### Changed

Enhanced [data residency support](https://cloud.google.com/security-command-center/docs/data-residency-support) in the European Union and United States is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
