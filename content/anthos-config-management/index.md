# Anthos Config Management

## 2025-09-02

### Announcement

Config Sync is now available as part of the standard GKE offering and no longer requires GKE Enterprise. For more details on the removal of GKE Enterprise, see the [GKE release notes](https://cloud.google.com/kubernetes-engine/docs/release-notes#September_02_2025).

---
## 2025-08-21

### Announcement

Announcing experimental features: help shape the future of Config Sync features by providing direct feedback.

* Introducing PostSync, a feature that lets you run custom actions like cleanup scripts or notifications right after your configurations are synced. We're looking for your feedback to shape its future! Check out the [Post Sync discussion](https://github.com/GoogleContainerTools/kpt-config-sync/discussions/1830) to share your thoughts, suggestions, and bug reports before December 1, 2025.

### Feature

Config Sync now supports syncing from Secure Source Manager git repositories. For more information, see [Grant access to Git](https://cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/installing-config-sync#git-creds-secret).

### Changed

Addressed multiple Common Vulnerabilities and Exposures (CVEs) by updating dependencies.

---
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
