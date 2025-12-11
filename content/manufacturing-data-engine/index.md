# Manufacturing Data Engine

## 2025-12-10

### Release 1.5.2

This release is a **critical update** if you have an existing deployment of
MDE version 1.5.0. This release introduces a new configuration package upload
option that allows users to automatically enable and activate all entities
created following the upload. It also includes other minor improvements and bug
fixes.

Follow the [Upgrade guide](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/upgrade-guide)
in the MDE documentation for detailed instructions. Note that instructions are
different depending on the MDE version you are upgrading from.

### Changed

* **Improvement (441727217)**: Introduced an option to enable parsers after
  types activation when you upload a new configuration package.
* **Improvement (333321871)**: Refactored scripts to collect additional
  information for the MDE team when you open a support ticket to help
  faster troubleshooting.
* **Improvement (441660844)**: Added `typesMetadataBuckets` and
  `typesTransformations` JSON arrays as responses to the Tags API implementation.
* **Improvement (435358499)**: Enabled Streaming Engine for Dataflow in all
  MDE deployment sizes for optimized consumption, saving resources.

### Security

* **Improvement (448853115)**: Added the ability to
  enable and configure VPC flow logging from Terraform. Collecting VPC flow logs
  is recommended to detect potential intrusions or anomalies.
* **Improvement (450530585)**: Updated container images
  and dependencies to address known security vulnerabilities.
* **Improvement (448854007):** Adjusted IAM roles used
  by some MDE service accounts following the least-privilege approach.
* **Improvement (448148987)**: Switched to DNS-based endpoint with AIM access
  control for GKE control plane, following security best practices.
* **Improvement (448148673)**: Enabled SSL required mode on the Cloud SQL
  instance for additional security enforcement.
* **Improvement (448148275)**: Enabled in-transit encryption and token
  authentication for Redis.

### Libraries

**Release signature**

```
6e178bd
1.5.2
9ee64699a1bdf1cf690e7930d968f002
```

### Fixed

* **Fix (423567127):** Fixed a bug that prevented numeric values to be
  correctly processed when using file ingestion.
* **Fix (441294785):** Fixed a bug that prevented the deletion of a message
  class if the related parser had been deleted beforehand.
* **Fix (443710570)**: Fixed a bug that could use an old version of a parser
  script when uploading a new configuration package that had the same parser name.

---
## 2025-08-29

### Release 1.5.1

This release is a **critical update** if you have an existing deployment of MDE version 1.5.0. This release resolves a bug regarding materialization of metadata instances created prior to MDE 1.5.0. This release also includes other minor improvements and bug fixes.

### Libraries

**Release signature**

```
b0fc163
1.5.1
ffb87d39d343c20abebd2f52df74a2d3

```

### Fixed

* **Fix (417666631):** Fixed an issue with metadata materialization for metadata instances that had been created prior to migrating to MDE 1.5.0.
* **Fix (420921890):** Fixed an error when attempting to update an instance tag metadata and saved it for instances that had been created prior to migrating to MDE 1.5.0.
* **Fix (423535516)**: Fixed inconsistent API response codes when trying to delete non-existing entities.
* **Fix (383519276)**: Fixed missing fields in MDE logging and added more details to make troubleshooting easier.
* **Fix (424077359)**: Fixed instance bucket creation through API. It now adds default `createdTime` as the time when the API call was received.
* **Fix (422991109 and 424084607)**: Fixed `ghost` deletion of Types and Metadata Buckets after removing a configuration package.
* **Fix (423859259)**: Fixed removal of BigQuery views when a Type is manually deleted.
* **Fix (406803212)**: Fixed wrong version materialization on MDE system tables.
* **Fix (407015039)**: Fixed `Delete` button in MDE UI when the system is in PROD mode (Production mode).
* **Fix (435653743)**: Fixed missing Grafana Terraform module.

### Security

* **Improvement (427447932)**: Brought Docker images to versions without vulnerabilities reported at the time of the release.
* **Improvement (361290775)**: Modified Terraform deployment scripts to enforce TLS v1.2 for an external MDE UI Load Balancer.

### Changed

* **Improvement (407009198)**: Improved the error handling when `upload` and `parsing` configuration packages.
* **Improvement (423531705):** Improved MDE logging for BigQuery sink related operations.
* **Improvement (423530033):** Improved manifest validation on configuration package uploads.
* **Improvement (423554635)**: Added `CreatedAt` column with default sorting on the MDE UI configuration packages page.
* **Improvement (430962108):** Added more sorting options on the MDE UI *Configurations* and *Metadata Instances* pages.
* **Improvement (423531714)**: Various improvements on Helm charts, including image tag management, and k8s secrets/configmaps.
* **Improvement (407037164)**: More descriptive message added to MDE UI to confirm Type deletion.

---
