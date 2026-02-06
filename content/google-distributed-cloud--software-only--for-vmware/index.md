# Google Distributed Cloud (software only) for VMware

## 2026-02-05

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.800-gke.126 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).
Google Distributed Cloud 1.32.800-gke.126 runs on Kubernetes v1.32.11-gke.200.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

---
## 2026-02-04

### Announcement

Google Distributed Cloud (software only) for VMware 1.33.400-gke.113 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).
Google Distributed Cloud 1.33.400-gke.113 runs on Kubernetes v1.33.5-gke.1900.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

---
## 2026-01-30

### Security

Multiple security vulnerabilities have been identified in the OpenSSL library.
The most significant finding is CVE-2025-15467, a critical vulnerability that
might allow for remote code execution (RCE) or denial of service (DoS) attacks
via network-based vectors.

For more details, see the [GCP-2026-006 security bulletin](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2026-006-gdcvmware).

---
## 2026-01-08

### Announcement

Google Distributed Cloud (software only) for VMware 1.31.1200-gke.60 is now
available for
[download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads).
To upgrade, see
[Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).
Google Distributed Cloud 1.31.1200-gke.60 runs on Kubernetes v1.31.13-gke.1100.

If you are using a third-party storage vendor, check the
[GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage)
document to make sure the storage vendor has already passed the qualification
for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with
[GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

---
## 2025-12-11

### Fixed

The following issues were fixed in 1.34.0-gke.566:

* Fixed vulnerabilities listed in
  [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

### Change

* Upgraded `containerd` from 1.7 to 2.0.
* Registry mirror configuration information has been migrated to the
  hosts.toml `containerd` config file.
* Upgrade preflight checks now validate `PodDisruptionBudgets`.

### Announcement

Google Distributed Cloud (software only) for VMware 1.34.0-gke.566 is now
available for
[download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads).
To upgrade, see
[Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).
Google Distributed Cloud 1.34.0-gke.566 runs on Kubernetes v1.34.1-gke.2900.

If you are using a third-party storage vendor, check the
[GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage)
document to make sure the storage vendor has already passed the qualification
for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with
[GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

### Breaking

Changed the upgrade logic for non-advanced clusters. When you upgrade a
non-advanced cluster from version 1.33 to 1.34, the cluster is automatically
converted to an advanced cluster. If you use custom code that depends on the
non-advanced cluster configuration, this can be a breaking change. For more
information, see
[Key differences after moving to advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster#key_differences_after_moving_to_advanced_clusters).

---
## 2025-12-05

### Fixed

The following issues were fixed in 1.33.300-gke.60:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

### Announcement

Google Distributed Cloud (software only) for VMware 1.33.300-gke.60 is
available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To
upgrade, see [Upgrade a
cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).
Distributed Cloud 1.33.300-gke.60 runs on Kubernetes
v1.33.5-gke.900.

If you are using a third-party storage vendor, check the [GDC Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

---
## 2025-12-02

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.700-gke.64 is
available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To
upgrade, see [Upgrade a
cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).
Distributed Cloud 1.32.700-gke.64 runs on Kubernetes
v1.32.9-gke.700.

If you are using a third-party storage vendor, check the [GDC Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.32.700-gke.64:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-11-12

### Fixed

The following issues were fixed in 1.33.200-gke.70:

* Fixed [an
  issue](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#nonha-to-ha-adv-update-fail)
  that `gkectl update` blocks updating a non-HA non-advanced cluster to HA
  advanced cluster
* Fixed vulnerabilities listed in [Vulnerability
  fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

### Announcement

Google Distributed Cloud (software only) for VMware 1.31.1100-gke.40 is
available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To
upgrade, see [Upgrade a
cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).
Distributed Cloud 1.31.1100-gke.40 runs on Kubernetes
v1.31.12-gke.600.

If you are using a third-party storage vendor, check the [GDC Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.31.1100-gke.40:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

### Announcement

Google Distributed Cloud (software only) for VMware 1.33.200-gke.70 is
available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To
upgrade, see [Upgrade a
cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).
Distributed Cloud 1.33.200-gke.70 runs on Kubernetes
v1.33.5-gke.600.

If you are using a third-party storage vendor, check the [GDC Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

---
## 2025-10-29

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.600-gke.53 is
available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To
upgrade, see [Upgrade a
cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).
Distributed Cloud 1.32.600-gke.53 runs on Kubernetes
v1.32.9-gke.200.

If you are using a third-party storage vendor, check the [GDC Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.32.600-gke.53:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-10-15

### Announcement

Google Distributed Cloud (software only) for VMware 1.31.1000-gke.44 is
available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To
upgrade, see [Upgrade a
cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).
Distributed Cloud 1.31.1000-gke.44 runs on Kubernetes
v1.31.12-gke.600.

If you are using a third-party storage vendor, check the [GDC Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.31.1000-gke.44:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-10-02

### Announcement

Google Distributed Cloud (software only) for VMware 1.33.100-gke.89 is now available for [download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Distributed Cloud 1.33.100-gke.89 runs on Kubernetes v1.33.4-gke.900.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.33.100-gke.89:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-09-24

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.500-gke.48 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Distributed Cloud 1.32.500-gke.48 runs on Kubernetes v1.32.8-gke.500.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.32.500-gke.48:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-09-15

### Announcement

Google Distributed Cloud (software only) for VMware 1.31.900-gke.38 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Distributed Cloud 1.31.900-gke.38 runs on Kubernetes v1.31.12-gke.200.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.31.900-gke.38:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-09-02

### Announcement

Google Distributed Cloud (software only) for VMware 1.33.0-gke.799 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Distributed Cloud 1.33.0-gke.799 runs on Kubernetes v1.33.2-gke.700.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Changed

* GA: Changed the cluster creation process so that all new clusters are [advanced clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters). Additionally, all cluster upgrades to 1.33 are automatically converted to advanced clusters.
* Upgraded the `etcd` component to version 3.4.33.

### Feature

* GA: Enabled the `vsphere-metrics-exporter` component for advanced clusters. This exporter provides greater visibility into the VMware vSphere environment by collecting key performance and health metrics.
* GA: Added support for VM-Host affinity groups in advanced clusters. This feature allows for the creation of rules that constrain cluster nodes to run on specific, predefined groups of hosts.
* GA: Added support for automatic node resizing in advanced clusters. This feature optimizes resource use by automatically adjusting the CPU and memory allocated to control plane nodes in response to workload demands.
* Public Preview: Added support for Virtual Machine (VM) tracking using vSphere
  tags in advanced clusters. This feature simplifies resource management by
  automatically applying identifying tags to cluster VMs.
* GA: Introduced an Envoy proxy sidecar to the GKE Identity Service for clusters
  that use Controlplane V2. This change enhances the security, reliability, and
  performance of the authentication service.

### Fixed

The following issues were fixed in 1.33.0-gke.799:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-08-28

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.400-gke.68 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.32.400-gke.68 runs on Kubernetes v1.32.7-gke.200.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.32.400-gke.68:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-08-13

### Announcement

Google Distributed Cloud (software only) for VMware 1.31.800-gke.32 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.31.800-gke.32 runs on Kubernetes v1.31.10-gke.300.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

---
## 2025-08-12

### Announcement

Google Distributed Cloud (software only) for VMware 1.30.1200-gke.63 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.30.1200-gke.63 runs on Kubernetes v1.30.12-gke.1200. This is the final patch for the 1.30 minor release.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.30.1200-gke.63:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-08-08

### Fixed

The following issues were fixed in 1.32.300-gke.85:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.300-gke.85 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.32.300-gke.85 runs on Kubernetes v1.32.6-gke.200.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

---
## 2025-08-04

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.300-gke.85 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.32.300-gke.85 runs on Kubernetes v1.32.6-gke.200.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.32.300-gke.85:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-07-22

### Announcement

Google Distributed Cloud (software only) for VMware 1.31.700-gke.72 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.31.700-gke.72 runs on Kubernetes v1.31.10-gke.200.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.31.700-gke.72:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-07-21

### Announcement

Google Distributed Cloud (software only) for VMware 1.30.1100-gke.67 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.30.1100-gke.67 runs on Kubernetes v1.30.12-gke.800.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.30.1100-gke.67:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-07-17

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.200-gke.104 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.32.200-gke.104 runs on Kubernetes v1.32.4-gke.1000.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.32.200-gke.104:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-06-23

### Announcement

Google Distributed Cloud (software only) for VMware 1.31.600-gke.85 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.31.600-gke.85 runs on Kubernetes v1.31.8-gke.100.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.31.600-gke.85:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-06-10

### Announcement

Google Distributed Cloud (software only) for VMware 1.30.1000-gke.83 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.30.1000-gke.83 runs on Kubernetes v1.30.12-gke.100.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.30.1000-gke.83:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

---
## 2025-06-04

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.100-gke.106 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.32.100-gke.106 runs on Kubernetes v1.32.4-gke.200.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Changed

For clusters configured with [advanced clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters), introduced an Envoy sidecar into the GKE Identity Service to increase security, reliability, and performance.

---
