# SAP on Google Cloud

## 2026-01-22

### Announcement

**BigQuery Connector for SAP version 2.12**

Version 2.12 of the BigQuery Connector for SAP is generally available (GA).
This version offers file-based replication to Cloud Storage,
table schema caching for streaming replication to BigQuery,
and enhanced Unicode data handling.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new#version-2-12).

---
## 2025-12-23

### Change

**Updated IpAddr2 resource configuration for HA clusters**

To make the SAP HANA and SAP NetWeaver HA cluster configurations forward
compatible with OS version updates, we recommend that you update the `IpAddr2`
resource configuration to use `nic=lo` instead of `nic=eth0`.

For updated guidance, see the HA cluster configuration for your scenario:

* [HA scale-up cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel)
* [HA scale-up cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles)
* [HA scale-out cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-config-sles)
* [HA scale-out cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-config-rhel)
* [HA cluster manual configuration guide for SAP NetWeaver on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles)
* [HA cluster manual configuration guide for SAP NetWeaver on RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel)

---
## 2025-12-19

### Announcement

**Introducing emergent host maintenance events for X4 instances running SAP HANA**

To perform non-critical hardware repairs that help in preventing host errors on
X4 instances, we've introduced *emergent maintenance* - a new type of host
maintenance event.

While this is a type of unplanned maintenance, it's similar in nature to a
[planned host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) because of the following features:

* It has a 14-day advance notification period.
* You can manually trigger it, or let Google trigger it for you at the planned
  start date and time.

For more information, see
[Manage host maintenance events for X4 instances running SAP HANA](https://docs.cloud.google.com/sap/docs/manage-maintenance-events-for-bare-metal-instances).

---
## 2025-12-12

### Announcement

**New SAP certification: 6, 8, and 12 TB X4 machine types for SAP HANA scale-up workloads**

For use with SAP HANA scale-up (OLTP and OLAP) workloads running on
Google Cloud, SAP has certified the following Compute Engine X4
machine types:

* `x4-480-6t-metal` - 6 TB memory
* `x4-480-8t-metal` - 8 TB memory
* `x4-960-12t-metal` - 12 TB memory

With this certification, the names of all X4 machine types have been updated to
convey the memory they offer. For example, `x4-megamem-960-metal` is renamed to
`x4-960-16t-metal` because it offers 16 TB memory. This change is backwards
compatible.

For more information, see
[X4 memory-optimized bare metal machine types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#x4-memory-optimized).

---
## 2025-12-05

### Announcement

**New OS certification: Windows Server 2025 for SAP NetWeaver**

For use with SAP NetWeaver systems on Google Cloud, SAP has certified the
operating system Windows Server 2025.

For more information, see
[Certified SAP applications on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-apps-on-gc).

---
## 2025-12-02

### Announcement

**BigQuery Connector for SAP version 2.11**

Version 2.11 of the BigQuery Connector for SAP is generally available (GA).
This version lets you set up JWT authentication by using project-specific
service accounts for data replication to different Google Cloud projects.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new#version-2-11).

---
## 2025-11-06

### Announcement

**Guidance for RISE with SAP on Google Cloud**

Guidance is available to help you plan for running SAP solutions
on Google Cloud that are managed by SAP under the RISE with SAP program.
This guidance includes the following topics:

* An overview about the architecture and involved components.
* Establishing network connectivity to RISE with SAP on Google Cloud from
  on-premises systems and Google Cloud projects.
* Building extensions for RISE with SAP on Google Cloud by using the
  ABAP SDK for Google Cloud.

For more information, see
[Overview of RISE with SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/rise-overview).

### Feature

**Use of Oracle Automatic Storage Management with Oracle Database**

To run Oracle Database with SAP NetWeaver based applications on
Google Cloud, SAP and Oracle have validated the use of Oracle Automatic
Storage Management (ASM).

For more information, see the following:

* [Plan Oracle Database implementation for SAP NetWeaver](https://cloud.google.com/sap/docs/oracle-planning)
* [Deploy Oracle Database for SAP NetWeaver](https://cloud.google.com/sap/docs/oracle-deployment-single-node)

---
## 2025-11-04

### Announcement

**Google Cloud's Agent for SAP version 3.10**

Version 3.10 of Google Cloud's Agent for SAP is generally available (GA). This
version introduces enhancements for SAP workload evaluations, and disk snapshot
based backup and recovery for SAP HANA.

For more information, see
[What's new with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/whats-new).

---
## 2025-10-08

### Announcement

**BigQuery Connector for SAP version 2.10**

Version 2.10 of the BigQuery Connector for SAP is generally available (GA). This version resolves the non-ASCII character handling issue in CDC replication through Pub/Sub and enhances server-side error handling.

For more information, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new#version-2-10).

### Announcement

**ABAP SDK for Google Cloud version 1.12 (On-premises or any cloud edition)**

Version 1.12 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA). This version lets you integrate Gemma models into your ABAP applications. In addition, the SDK improves your interaction with Gemini models by letting you control the randomness of the model's output and gain insight into the model's reasoning.

For more information, see [What's new with the on-premises or any cloud edition of the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new#version-1-12).

---
## 2025-10-03

### Announcement

**New SAP certification for operating system: RHEL for SAP 9.6**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has certified the operating system Red Hat Enterprise Linux (RHEL) for SAP 9.6.

For more information about SAP-certified operating systems, see:

* [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
* [Certified operating systems for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)

---
## 2025-09-02

### Deprecated

**Support for version 2 of Google Cloud's Agent for SAP has ended**

Support for version 2 of Google Cloud's Agent for SAP ended on July 31, 2025.

If you're using version 2 of the agent, then we strongly recommend that you update to using a supported version as soon as possible. For information about how to update the agent, see [Update Google Cloud's Agent for SAP](https://cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update).

---
## 2025-08-27

### Announcement

**New SAP certifications: Additional M4 memory-optimized machine types**

For use with SAP HANA scale-up (OLAP and OLTP) and SAP NetWeaver workloads, SAP has certified the `m4-hypermem` Compute Engine memory-optimized machine types with 16, 32, and 64 vCPUs.

For more information, see:

* [M4 memory-optimized machine types for SAP HANA](https://cloud.google.com/sap/docs/sap-hana-planning-guide#m4-memory-optimized)
* [Certified machine types for SAP applications](https://cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms)

---
## 2025-08-04

### Announcement

**New SAP certifications: Additional C4 machine tpes**

SAP has certified the following Compute Engine C4 machine types with the Intel Granite Rapids CPU platform:

* For use with SAP HANA scale-up (OLTP and OLAP): `c4-highmem-144`, `c4-highmem-288`, and `c4-highmem-288-metal`
* For use with SAP NetWeaver: `c4-standard-144`, `c4-standard-288`, `c4-standard-288-metal`, `c4-highmem-144`, `c4-highmem-288`, and `c4-highmem-288-metal`

For more information, see the following:

* [C4 general-purpose VM types for SAP HANA](https://cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-c4)
* [Certified machine types for SAP applications](https://cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms)

---
## 2025-07-30

### Announcement

**Google Cloud's Agent for SAP version 3.9**

Version 3.9 of Google Cloud's Agent for SAP is generally available (GA). This version introduces monitoring and supportability enhancements.

For more information, see [What's new with Google Cloud's Agent for SAP](https://cloud.google.com/sap/docs/agent-for-sap/whats-new).

---
## 2025-07-28

### Announcement

**New SAP NetWeaver certification: C4D bare metal machine types**

For use with SAP NetWeaver, SAP has certified the following Compute Engine bare metal machine types: `c4d-standard-384-metal` and `c4d-highmem-384-metal`.

For more information, see the following:

* [Certifications for SAP applications on Google Cloud](https://cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-c4d)
* [C4D machine series](https://cloud.google.com/compute/docs/general-purpose-machines#c4d_series)

---
## 2025-07-18

### Announcement

**New SAP certification for operating system: SLES 15 SP7 for SAP**

For use with SAP HANA and SAP NetWeaver on Google Cloud, SAP has certified the operating system SUSE Linux Enterprise Server (SLES) 15 SP7 for SAP.

For more information, see:

* [Certified operating systems for SAP HANA](https://cloud.google.com/sap/docs/sap-hana-os-support#quick_reference_table)
* [Certified operating systems for SAP NetWeaver](https://cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table)

---
## 2025-07-08

### Announcement

**BigQuery Connector for SAP version 2.9**

Version 2.9 of the BigQuery Connector for SAP is generally available (GA). This version introduces Change Data Capture (CDC) replication of SAP data into BigQuery through Pub/Sub. This replication path keeps your BigQuery tables up-to-date with the latest changes from your SAP data sources, eliminating the need for custom deduplication.

For more information, see [What's new with BigQuery Connector for SAP](https://cloud.google.com/sap/docs/bq-connector/whats-new#version-2-9).

---
## 2025-07-03

### Announcement

**ABAP SDK for Google Cloud version 1.11 (On-premises or any cloud edition)**

Version 1.11 of the on-premises or any cloud edition of the ABAP SDK for Google Cloud is generally available (GA). This version introduces support for Anthropic Claude models through the Vertex AI SDK for ABAP, integration with the Model Armor API for LLM prompt security, and the WIF authentication validation feature. In addition, this version includes minor enhancements and bug fixes.

For more information, see [What's new with the on-premises or any cloud edition of the ABAP SDK for Google Cloud](https://cloud.google.com/solutions/sap/docs/abap-sdk/on-premises-or-any-cloud/whats-new#version-1-11).

---
## 2025-06-13

### Announcement

**New SAP NetWeaver certification: C4D series of general-purpose machine types**

For use with SAP NetWeaver, SAP has certified the Compute Engine general purpose machine types `c4d-standard` and `c4d-highmem`.

For more information, see [Certified C4D general-purpose machine types](https://cloud.google.com/solutions/sap/docs/certifications-sap-apps#sap-certified-vms-gen-purpose-c4d).

---
## 2025-06-09

### Announcement

**Google Cloud's Agent for SAP version 3.8**

Version 3.8 of Google Cloud's Agent for SAP is generally available (GA). This version introduces monitoring and supportability enhancements.

For more information, see [What's new with Google Cloud's Agent for SAP](https://cloud.google.com/solutions/sap/docs/agent-for-sap/whats-new).

---
