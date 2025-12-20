# Security Command Center

## 2025-12-16

### Feature

The following
[Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)
detectors have been released to
[General Availability](https://cloud.google.com/products#product-launch-stages):

* `Command and Control: Piped Encoded Code Execution Detected`
* `Command and Control: Piped Encoded Download`

---
## 2025-12-15

### Feature

You can [configure Model Armor floor
settings](https://docs.cloud.google.com/model-armor/configure-floor-settings) for Google-managed Model
Context Protocol (MCP) servers to define baseline safety and security filters.
This feature is in
[Preview](https://cloud.google.com/products#product-launch-stages).

You can also [configure Cloud Logging for sanitization
operations](https://docs.cloud.google.com/model-armor/configure-logging#configure-logging-floor-settings).
The
Model Armor floor settings perform these operations on traffic to and from
Google-managed MCP servers and Vertex AI models.

---
## 2025-12-12

### Feature

[AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) is generally
available ([GA](https://cloud.google.com/products#product-launch-stages)) in the
Security Command Center Enterprise tier and is available as a
[Preview](https://cloud.google.com/products#product-launch-stages) in the
Security Command Center Premium tier.

### Change

Multiple pages in Security Command Center Standard have been improved:

* The [Risk overview](https://docs.cloud.google.com/security-command-center/docs/assess-risk) page is enhanced to
  provide separate views for misconfiguration, vulnerabilities and identity-related
  findings.
* The
  [Findings page](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#edit-finding-query)
  includes predefined filter views for vulnerabilities and identity findings.
* The [left navigation](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#features)
  has been updated.

---
## 2025-12-11

### Feature

Security Command Center [Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features) supports
Cloud Build Attack Paths with Cloud Build Resources supported in
the high-value resource set.

---
## 2025-12-10

### Feature

You can configure Model Armor to enhance the security of your agentic
AI applications that interact with Google Cloud Model Context Protocol (MCP)
servers. This feature is in
[Preview](https://cloud.google.com/products#product-launch-stages). For
configuration details, see [Model Armor integration with Google Cloud
MCP servers](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration).

---
## 2025-12-05

### Change

Security Command Center [Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features)
uses the [`storage.restrictAuthTypes`](https://docs.cloud.google.com/storage/docs/org-policy-constraints#restrict-auth-types)
organization policy constraint to determine whether Cloud Storage buckets are
reachable using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

---
## 2025-12-04

### Feature

[The monitoring dashboard](https://docs.cloud.google.com/model-armor/monitoring-dashboard)
is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-12-03

### Feature

[Model Armor integration with Vertex AI](https://docs.cloud.google.com/model-armor/model-armor-vertex-integration)
is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-11-20

### Change

The following updates simplify Security Command Center Standard and Premium tier activation
for organizations:

* You need fewer [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier#required-roles)
  to activate Security Command Center.
* A variety of [services](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier#premium-services)
  are automatically enabled during activation. [Service-specific service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-specific)
  are automatically enabled with the IAM roles and permissions that are
  required for these services to function.

See the following for detailed information about activating a specific tier:

* [Activate Security Command Center Standard tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier)
* [Activate Security Command Center Premium tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier)

---
## 2025-11-17

### Feature

The following
[AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) features are
available:

* [AI Security dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection): The
  dashboard has an updated AI Inventory section, which includes an overview of
  AI agents.
* [Assets page](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console): You can
  filter for AI resources, including AI agents that are deployed to
  Vertex AI Agent Engine.

AI Protection is available in
[Preview](https://cloud.google.com/products#product-launch-stages) to the
Security Command Center Enterprise tier.

### Feature

[Agent Engine Threat
Detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview), a built-in
service of Security Command Center, is available in
[Preview](https://cloud.google.com/products#product-launch-stages) to the Security
Command Center Enterprise and Premium tiers. This service helps you detect and
investigate potential attacks on AI agents that are deployed to
[Vertex AI Agent Engine](https://docs.cloud.google.com/agent-builder/agent-engine/overview) Runtime.

---
## 2025-11-14

### Feature

[Data Security Posture Management (DSPM)](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security) supports the
Security Command Center Premium tier at the organization level.

---
## 2025-11-11

### Changed

Several features and updates have been made available to Security Command Center in a [federated identity](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services#security-command-center) environment:

* Exporting findings to a CSV file.
* Exporting findings to Cloud Storage.

The following features aren't supported by identity federation but are being moved to other sections in the documentation:

* Sending feedback in Security Command Center
* Managing Google SecOps settings.

---
## 2025-11-10

### Feature

[Data Security Posture Management (DSPM)](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security) has been released
to [General Availability](https://cloud.google.com/products#product-launch-stages)
for the Security Command Center Enterprise tier.

### Feature

Model Armor is available in the following regions:

* `europe-west1` (Belgium)
* `europe-west2` (London)
* `europe-west3` (Frankfurt)
* `asia-south1` (Mumbai)

For more information, see [Locations for the Model Armor API](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#locations-model-armor).

---
## 2025-11-07

### Feature

The monitoring and auditing capabilities for
[Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager/overview)
have been released to [General
Availability](https://cloud.google.com/products#product-launch-stages).

### Feature

You can use customer-managed encryption keys (CMEK) organization policies with
Security Command Center. For more information, see [Use CMEK organization policies with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/cmek#org-policies).

---
## 2025-11-06

### Feature

Security Command Center [Risk Engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features)
supports Cloud Run attack paths for the following high-value
resources:

* `run.googleapis.com/Job`
* `run.googleapis.com/Service`

---
## 2025-11-03

### Feature

[Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview)
supports the Security Command Center Premium tier at the organization level.

---
## 2025-10-30

### Feature

In addition to the Enterprise service tier, [Issues](https://docs.cloud.google.com/security-command-center/docs/issues-overview)
are available on the Security Command Center Premium service tier at the organization level.
This update includes capabilities such as [Toxic Combinations, Chokepoints](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview),
and [Graph Search](https://docs.cloud.google.com/security-command-center/docs/graph-search)
([Preview](https://cloud.google.com/products#product-launch-stages)). The
console navigation has been updated to reflect an **Issues** page for Premium
tier users.

---
## 2025-10-21

### Changed

The release note for Security Command Center and [attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn),
published on October 16, 2025, was updated to clarify that
[attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn)
use Compute Engine and Google Kubernetes Engine OS and software
vulnerability *findings* to detect toxic combinations and
chokepoints.

---
## 2025-10-20

### Feature

[Container image vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#ar-vuln-assessment)
has been released to [General
Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-17

### Feature

Customers with an organization-level activation of Security Command Center
Premium have an organization-level discovery subscription
at no charge from Sensitive Data Protection. For more information, see
[Sensitive data discovery in Security Command Center
Premium](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery#sensitive-data-discovery-scc-premium).

---
## 2025-10-16

### Changed

Security Command Center and [attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn)
use Compute Engine and Google Kubernetes Engine operating system and software
vulnerabilities to detect toxic combinations and chokepoints.

**UPDATE**: [Attack path simulations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn)
analyze OS and software vulnerability findings for Compute Engine and
Google Kubernetes Engine resources to detect toxic combinations and chokepoints.

---
## 2025-10-15

### Changed

The following features in Compliance Manager are available in [General
Availability](https://cloud.google.com/products#product-launch-stages):

* [Applying and updating built-in frameworks and cloud
  controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework)
* Creating, applying, and editing custom frameworks and cloud controls
* [Support for VPC Service Control
  perimeters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-configure-vpc-sc)
* [Audit logging](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit-logging)
* [Client
  libraries](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/libraries)
* [REST APIs](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest)

---
## 2025-10-10

### Feature

[Correlated Threats](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview) is available
in [Preview](https://cloud.google.com/products#product-launch-stages). This
feature combines related threat findings together by using the security graph,
helping you to prioritize and respond to active threats.

---
## 2025-10-09

### Feature

Data Security Posture Management (available in [Preview](https://cloud.google.com/products#product-launch-stages))
lets you deploy frameworks with advanced data security cloud controls to
app-enabled folders. For more information, see [Deploy advanced data security cloud controls](https://docs.cloud.google.com/security-command-center/docs/dspm-use-data-security#deploy-advanced-data-security-cloud-controls).

---
## 2025-10-07

### Changed

Google Cloud console pages for all Security Command Center tiers have been enhanced.

* The following changes were made to all service tiers—Standard, Premium,
  and Enterprise:

  + You can refresh findings in the **Finding query results** panel.
  + The **JSON** tab on the detail pane of the **Findings** page displays the raw
    findings JSON object, making it compatible with APIs.
  + Autocompletion of a query in the **Findings** page query editor is improved.
  + The **Findings > Quick filters** panel shows default
    values if there is an error fetching results.
  + The **Findings > Quick filters** panel shows separate
    **State** and **Mute** filter sections.
* The following changes were made to the Enterprise service tier:

  + Added support for the **Vulnerabilities** page.
  + Added support for security marks.
  + Added support for the **Threats** dashboard on the **Risk overview** page.
  + The finding detail panel on the **Issues** page is updated. Open the panel
    using the **View details** button when viewing a toxic combination issue type.
  + Additional query operators and query functions are available.
  + The opt-out banner is no longer available.

---
## 2025-09-27

### Feature

Model Armor limits the maximum input size for files and text to 4 MB,
automatically skipping any content that exceeds this threshold.

---
## 2025-09-23

### Feature

[Bulk export findings to BigQuery](https://cloud.google.com/security-command-center/docs/bulk-exports-to-big-query)
is available in [General Availability](https://cloud.google.com/products#product-launch-stages).
Bulk exports are supported for organizations, projects, and folders.

### Changed

The upgraded model for the prompt injection and jailbreak detection filter is
available in EU multi-region. This model has improved detection rates across several
attack vectors, including the following:

* Do Anything Now prompts
* System instruction manipulation
* Unauthorized action execution
* Sensitive information retrieval

---
## 2025-09-22

### Feature

[Graph search](https://cloud.google.com/security-command-center/docs/graph-search) lets you explore the security graph
using custom queries. This product is available in [Preview](https://cloud.google.com/products#product-launch-stages)
in the Security Command Center Enterprise tier.

---
## 2025-09-16

### Feature

Model Armor is integrated with Google Agentspace to provide greater
insights and enhanced security of your agent interactions by default. For more
information, see
[Integration with Google Agentspace](https://cloud.google.com/security-command-center/docs/model-armor-agentspace-integration).

---
## 2025-09-15

### Feature

[Model Armor integration with Google Kubernetes Engine](https://cloud.google.com/security-command-center/docs/model-armor-gke-integration)
is available in
[General Availability](https://cloud.google.com/products#product-launch-stages).

### Changed

The **Findings** page in Security Command Center has been improved.

* With Security Command Center Premium and Enterprise, the page includes the following
  predefined filter views that return a specific category of findings.

  + Premium service tier: **All Findings**, **Vulnerabilities**, **Identity**,
    and **Threats**.
  + Enterprise service tier: **All Findings**, **Vulnerabilities**,
    **Identity**, **Data**, and **Code**.
* With Security Command Center Enterprise, the page includes a selector to filter by cloud
  provider: Google Cloud, Amazon Web Service (AWS), and Microsoft Azure.

For more information, see
[Review and manage findings](https://cloud.google.com/security-command-center/docs/review-manage-findings#use_predefined_filter_views).

---
## 2025-09-12

### Changed

Security Command Center has improved the automatic selection of resources when running
attack path simulations using the default high-value resource set.

[Risk Engine](https://cloud.google.com/security-command-center/docs/attack-exposure-supported-features) uses
heuristics to identify resources used for non-production purposes. To help
ensure that you have information about the most important assets, Risk Engine
calculates the attack exposure score for all other resources in the default
high-value resource set before calculating the attack exposure score for these
non-production resources.

To customize the high-value resource set, see
[Define and manage your high-value resource set](https://cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set).
For information about Risk Engine, see
[Attack exposure scores and attack paths](https://cloud.google.com/security-command-center/docs/attack-exposure-learn).

### Changed

Security Command Center changed how Google Cloud subnets are handled when running
[attack path simulations](https://cloud.google.com/security-command-center/docs/attack-exposure-learn). The result
is that attack paths are more accurate in relation to networking. Certain
customers with specific Google Cloud subnet configurations, for example, when a
VPC connector accesses a subnetwork, may see significant changes to toxic
combinations, chokepoints, and attack exposure scores.

---
## 2025-09-11

### Feature

Assured Open Source Software (Assured OSS) now supports Go packages. For more information,
see
[Download Go packages using direct repository access](https://cloud.google.com/security-command-center/docs/aoss-download-go-packages).

---
## 2025-09-10

### Feature

[Cloud Run Threat Detection](https://cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview)
is available in
[General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-08

### Feature

The Model Armor monitoring dashboard provides a centralized view to
track interactions and violations within your projects. This feature is
available in [Preview](https://cloud.google.com/products#product-launch-stages).
For more information, see
[View the monitoring dashboard](https://cloud.google.com/security-command-center/docs/model-armor-monitoring-dashboard).

### Changed

Multiple pages in Security Command Center Premium have been improved:

* The [Risk overview](https://cloud.google.com/security-command-center/docs/assess-risk#threats) page is enhanced to
  provide a view of threats, vulnerabilities, and misconfigurations.
* The
  [Findings page](https://cloud.google.com/security-command-center/docs/review-manage-findings#edit-finding-query)
  includes predefined filter views for vulnerabilities and identity findings.
* Information previously on the Threats page is available in the
  [Threats dashboard](https://cloud.google.com/security-command-center/docs/assess-risk#threats) on the Risk
  overview page.
* Information previously on the Vulnerabilities page is now available on the
  [Vulnerabilities dashboard](https://cloud.google.com/security-command-center/docs/assess-risk#vulnerabilities) on
  the Risk overview page.

---
## 2025-09-02

### Feature

Vulnerability assessment for Google Cloud supports scanning disks configured
with customer-managed encryption keys (CMEK) for projects that are outside of
VPC Service Controls perimeters. For more information about how to scan disks
configured with CMEK, see
[Run Vulnerability Scans for CMEK disks](https://cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud#run-cmek-vulns).

---
## 2025-08-27

### Changed

Compliance Manager (available in
[Preview](https://cloud.google.com/products#product-launch-stages)) now lets you
[remove resources from deployed frameworks](https://cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#remove-resource-assignments).

---
## 2025-08-20

### Changed

[Issues, chokepoints (for Google Cloud), and predefined security graph rules](https://cloud.google.com/security-command-center/docs/issues-overview) have been released to [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-08-15

### Feature

[AI Protection](https://cloud.google.com/security-command-center/docs/ai-protection-overview) helps you manage the security posture of your AI workloads by detecting threats and helping you to mitigate risks to your AI asset inventory. This product is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Enterprise tier.

---
## 2025-08-14

### Feature

You can use customer-managed encryption keys (CMEKs) to protect data at rest in Security Command Center. This feature is available in General Availability. For more information, see [Enable CMEK for Security Command Center](https://cloud.google.com/security-command-center/docs/cmek).

---
## 2025-08-12

### Feature

[Data Security Posture Management (DSPM)](https://cloud.google.com/security-command-center/docs/dspm-data-security) lets you define, deploy, monitor, and audit data security postures for your Google Cloud environment. This product is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Enterprise tier.

---
## 2025-08-07

### Feature

Risk reports generated and downloaded from Security Command Center include a system attack exposure page that shows the organization's exposure risk over time and lists the projects and resources that have the highest risk.

### Feature

The following [Container Threat Detection](https://cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) detectors have been released to [General Availability](https://cloud.google.com/products#product-launch-stages):

* `Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47177)`
* `Execution: Socat Reverse Shell Detected`
* `Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287)`
* `Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)`
* `Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)`

---
## 2025-08-04

### Changed

Model Armor supports the `asia-southeast1` location. For information about supported locations, see [Locations for the Model Armor API](https://cloud.google.com/security-command-center/docs/regional-endpoints#locations-model-armor).

---
## 2025-08-01

### Feature

[Compliance Manager](https://cloud.google.com/security-command-center/docs/compliance-manager-overview) helps ensure that your Google Cloud infrastructure, workloads, and data meet the security and regulatory requirements of your organization. This product is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Enterprise tier.

---
## 2025-07-29

### Feature

**Model Armor and Vertex AI integration**

Model Armor integrates with Vertex AI, providing a default security configuration for all new prediction endpoints. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integration with Vertex AI](https://cloud.google.com/security-command-center/docs/model-armor-vertex-integration).

### Feature

You can send a bulk export of Security Command Center findings to a BigQuery dataset. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Bulk export findings to BigQuery](https://cloud.google.com/security-command-center/docs/bulk-exports-to-big-query).

### Feature

You can use Terraform to manage Model Armor floor settings and templates. This helps reduce manual overhead with Model Armor deployments. For more information, see [Terraform resources for Security Command Center](https://cloud.google.com/security-command-center/docs/terraform#resources).

---
## 2025-07-28

### Changed

**Model Armor filter updates**

* The prompt injection and jailbreak detection filter now supports 10,000 tokens.
* For the Sensitive Data Protection filter, `SKIP_DETECTION` is returned if the prompt or response exceeds the token limit.
* For all other filters, if the prompt or response exceeds the token limit, `MATCH_FOUND` is returned if malicious content is found, and `SKIP_DETECTION` is returned if no malicious content is found.

---
## 2025-07-25

### Changed

[Cloud Infrastructure Entitlement Management (CIEM)](https://cloud.google.com/security-command-center/docs/ciem-overview) has launched support for log ingestion from Microsoft Azure management groups. This capability lets users set up log ingestion and then consume findings at an Azure management group level, rather than at the subscription level. For more information, see [Configure Microsoft Azure log ingestion for management groups](https://cloud.google.com/security-command-center/docs/connect-secops-azure#mgmt-group). This capability is available in [Preview](https://cloud.google.com/products#product-launch-stages).

### Changed

A new risk scoring algorithm is launched. As a result, you might see slight changes in [attack exposure scores for resources and findings](https://cloud.google.com/security-command-center/docs/attack-exposure-learn). The new algorithm better reflects attacker behavior and gives a fairer representation of the relative risk level of your organization. We will monitor the results of this change and might perform further adjustments, if necessary.

---
## 2025-07-24

### Feature

For the Enterprise service tier, Security Command Center offers [data residency support](https://cloud.google.com/security-command-center/docs/data-residency-support) in the European Union, Saudi Arabia, and United States. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-07-22

### Changed

The [Setup guide](https://cloud.google.com/security-command-center/docs/activate-enterprise-tier#monitor-configure-enterprise-tab) in Security Command Center Enterprise, used to monitor the activation progress and configure services, is now in [General Availability](https://cloud.google.com/products#product-launch-stages).

### Changed

The `Impair Defenses: Two Step Verification Disabled` finding type of Event Threat Detection was renamed to `Persistence: Two Step Verification Disabled`. For a complete list of Event Threat Detection finding types, see [Event Threat Detection overview](https://cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).

---
## 2025-07-21

### Changed

The **Aggregations** panel on the **Findings** page in Security Command Center Enterprise has been enhanced and is now called **Quick Filters**. For information about filtering results on the Findings page, see [Review and manage findings](https://cloud.google.com/security-command-center/docs/review-manage-findings).

---
## 2025-07-17

### Feature

The following [Container Threat Detection](https://cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) detectors for file monitoring are in [Preview](https://cloud.google.com/products#product-launch-stages):

* `Collection: Pam.d Modification`
* `Credential Access: Access Sensitive Files on Nodes`
* `Defense Evasion: Disable or modify Linux audit system`
* `Defense Evasion: Root Certificate Installed`
* `Execution: Suspicious Cron Modification`
* `Persistence: Modify ld.so.preload`

### Changed

The following Security Command Center Enterprise pages in the Google Cloud
console now fully replace equivalent pages that you accessed previously in the
Google Security Operations console.

* [Risk Overview](https://cloud.google.com/security-command-center/docs/assess-risk)
* [Issues](https://cloud.google.com/security-command-center/docs/issues-overview)
* [Assets](https://cloud.google.com/security-command-center/docs/work-with-resources-in-the-console) (previously called Resources)
* [Findings](https://cloud.google.com/security-command-center/docs/review-manage-findings)

Left navigation links in the Google Security Operations console open the related Google Cloud console page. See the earlier [release announcement](https://cloud.google.com/security-command-center/docs/release-notes#May_08_2025) about these pages.

---
## 2025-07-14

### Changed

In the [Google Kubernetes Engine (GKE) security posture dashboard](https://cloud.google.com/security-command-center/docs/concepts-security-sources#gke-security-posture-dashboard), the software vulnerabilities pane is available in [Preview](https://cloud.google.com/products#product-launch-stages), not General Availability.

---
## 2025-07-11

### Feature

[Notebook Security Scanner](https://cloud.google.com/security-command-center/docs/concepts-security-sources#notebook-security-scanner) is a built-in package vulnerability detection service of Security Command Center. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Premium or Enterprise tier.

You can enable and use Notebook Security Scanner to detect vulnerabilities in Python packages that are used in Colab Enterprise notebooks (files with the `ipynb` filename extension) and resolve those package vulnerability findings.

---
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
