# Anthos Config Management

## 2025-07-24

### Changed

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

### Fixed

Updated the git-sync image from v4.3.0 to v4.4.2, which fixes an issue that could cause the git-sync container to crash loop. For more information see [git-sync releases](https://github.com/kubernetes/git-sync/releases).

### Fixed

Fixed a regression introduced in 1.21.0 that occasionally caused Config Sync to become stuck when applying [mutation ignored objects](https://cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/concepts/configs#ignoring).

### Fixed

Fixed an issue where Config Sync waited longer than intended between retry attempts after failing to sync from Helm and OCI sources.

---
## 2025-06-26

### Changed

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

### Fixed

Fixed an issue with the nomos CLI which prevented setting up autocomplete by using the `nomos completion` command. For more information see [Use the nomos command-line tool](https://cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/nomos-command).

### Fixed

Fixed an issue which prevented a resource conflict metric from being recorded in rare cases.

---
## 2025-05-29

### Changed

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

---
