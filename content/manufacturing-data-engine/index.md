# Manufacturing Data Engine

## 2025-08-29

### Announcement



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
