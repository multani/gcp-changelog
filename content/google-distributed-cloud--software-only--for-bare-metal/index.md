# Google Distributed Cloud (software only) for bare metal

## 2026-02-13

### Feature

The following feature was added in 1.34.100-gke.93:

The `spec.taints` field in the `NodePoolClaim` resource is mutable. You can
add or remove taints on existing node pools without recreating the
`NodePoolClaim`. You can use this field to manage GPU nodes.

### Announcement

Google Distributed Cloud (software only) for bare metal 1.34.100-gke.93 is now available for
download. To upgrade, see Upgrade clusters. Google Distributed Cloud for bare metal
1.34.100-gke.93 runs on Kubernetes v1.34.1-gke.4700.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the GKE On-Prem API clients: the
Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release of Google Distributed Cloud for bare metal.

---
## 2026-02-05

### Announcement

Google Distributed Cloud (software only) for bare metal 1.32.800-gke.126 is now
available for download. To upgrade, see [Upgrade clusters](how-to/upgrade).
Google Distributed Cloud for bare metal 1.32.800-gke.126 runs on Kubernetes
v1.32.11-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the GKE On-Prem API clients: the
Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed
the qualification for this release of Google Distributed Cloud for bare metal.

---
## 2026-02-04

### Announcement

Google Distributed Cloud (software only) for bare metal 1.33.400-gke.113 is now
available for download. To upgrade, see [Upgrade clusters](how-to/upgrade). Google Distributed Cloud for
bare metal 1.33.400-gke.113 runs on Kubernetes v1.33.5-gke.1900.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the GKE On-Prem API clients: the
Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed
the qualification for this release of Google Distributed Cloud for bare metal.

---
## 2026-01-30

### Security

Multiple security vulnerabilities have been identified in the OpenSSL library.
The most significant finding is CVE-2025-15467, a critical vulnerability that
might allow for remote code execution (RCE) or denial of service (DoS) attacks
via network-based vectors.

For more details, see the [GCP-2026-006 security bulletin](https://docs.cloud.google.com/kubernetes-engine/security-bulletins#gcp-2026-006-gdcbm).

---
## 2026-01-16

### Change

Updated the [multiple network interfaces for Pods](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/multi-nic)
and [bundled load balancing with BGP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp)
features to support admin clusters for version 1.34 or higher. Admin cluster
support for these features has also been added to the GKE On-Prem API, so you
can specify these features with clients like [Terraform](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_admin_cluster).

---
## 2026-01-08

### Announcement

Google Distributed Cloud for bare metal 1.31.1200-gke.60 is now available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To
upgrade, see [Upgrade
clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Distributed Cloud for bare metal 1.31.1200-gke.60 runs on
Kubernetes v1.31.13-gke.1100.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release of Distributed Cloud for bare metal.

---
## 2025-12-11

### Announcement

Google Distributed Cloud for bare metal 1.34.0-gke.566 is now available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To
upgrade, see [Upgrade
clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Distributed Cloud for bare metal 1.34.0-gke.566 runs on
Kubernetes v1.34.1-gke.2900.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release of Distributed Cloud for bare metal.

### Feature

The following features were added in 1.34.0-gke.566:

* **Preview**: Vertical Pod autoscaling can now be configured to use your
  Prometheus instance as a persistent history provider for long-term CPU and
  memory usage data.
* **Preview**: Added support for horizontal Pod autoscaling that uses custom
  metrics from your Prometheus server to scale your applications, eliminating
  the operational burden of manually deploying and managing the adapter, its
  configuration, and RBAC. The automated solution handles the entire
  lifecycle, making it simpler to scale applications based on the metrics that
  matter most to your business.
* **Preview**: Added support for fast failover for the egress NAT gateway
  running in high availability. This feature improves both the reliability and
  throughput of egress traffic.
* **GA**: Added support for skip minor version cluster upgrades. You can
  directly upgrade your cluster control plane nodes (and entire cluster if
  worker node pools aren't pinned at a lower version) to two minor versions
  above the current version. Added the [`bmctl upgrade
  intermediate-version`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#upgrade_intermediate-version)
  command to print the intermediate version for a skip minor version upgrade.
* **Preview**: Added support for advanced networking features on admin
  clusters. This capability lets you specify [multiple network interfaces for
  Pods](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/multi-nic)
  and lets you use [bundled load balancing with BGP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/%0A%20docs/how-to/lb-bundled-bgp) on your version 1.34 or higher admin clusters.

  This note is incorrect; see entry for [January 16, 2026](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/release-notes#January_16_2026).

### Change

The following functional changes were made in 1.34.0-gke.566:

* Enabled Ansible SSH pipelining by default to improve performance. This can
  be disabled by adding the annotation
  `preview.baremetal.cluster.gke.io/ansible-ssh-pipelining: "disable"` to the
  Cluster custom resource.
* During cluster creation and update operations, NodePools validate IP address
  uniqueness against all existing underlay Nodes, regardless of status. Node
  deprovisioning is blocked until the associated Kubernetes Node is deleted,
  unless the `node-deletion-timeout-seconds` annotation is present on the
  cluster.
* Upgraded containerd from 1.7 to 2.0.
* Registry mirror configuration information has been migrated to the
  `hosts.toml` containerd config file.
* Upgrade preflight checks now validate PodDisruptionBudgets.
* GKE Identity Service has been migrated from a Deployment to a DaemonSet for
  improved reliability on control plane nodes.
* Added support for Red Hat Enterprise Linux 9.6.
* Removed support for Red Hat Enterprise Linux 9.2 as it is beyond the [Red
  Hat support
  window](https://access.redhat.com/support/policy/updates/errata#RHEL8_and_9_Life_Cycle).
* Added support for the 6.14 kernel package is supported for use with Ubuntu
  24.04 LTS.

### Fixed

The following issues were fixed in 1.34.0-gke.566:

* Updated the `bmctl restore` command so that it restores the Node Problem
  Detector systemd Service for admin clusters.
* Fixed the `etcd-cleanup` job timeout issue caused by the use of incorrect
  certificates.
* Fixed an issue where the cluster restore process leaves the Kubelet
  certificate files as regular files instead of symbolic links, preventing
  certificate rotation.

### Issue

For information about the latest known issues, see [Google Distributed Cloud for
bare metal known
issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

---
## 2025-12-05

### Issue

For information about the latest known issues, see [Google Distributed Cloud for
bare metal known
issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

### Fixed

The following issues were fixed in 1.33.300-gke.60:

* Fixed vulnerabilities listed in [Vulnerability
  fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Announcement

Google Distributed Cloud for bare metal 1.33.300-gke.60 is now available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To
upgrade, see [Upgrade
clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Distributed Cloud for bare metal 1.33.300-gke.60 runs on
Kubernetes v1.33.5-gke.900.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release of Distributed Cloud for bare metal.

---
## 2025-12-02

### Issue

For information about the latest known issues, see [Google Distributed Cloud for
bare metal known
issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

### Fixed

The following issues were fixed in 1.32.700-gke.64:

* Fixed vulnerabilities listed in [Vulnerability
  fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Announcement

Google Distributed Cloud for bare metal 1.32.700-gke.64 is now available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads).
To upgrade, see [Upgrade
clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Google Distributed Cloud for bare metal 1.32.700-gke.64 runs on Kubernetes
v1.32.9-gke.700.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://docs.cloud.google.com/anthos/docs/resources/partner-storage)
document to make sure the storage vendor has already passed the qualification
for this release of Google Distributed Cloud for bare metal.

---
## 2025-11-12

### Announcement

Google Distributed Cloud for bare metal 1.33.200-gke.70 is now available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To
upgrade, see [Upgrade
clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Distributed Cloud for bare metal 1.33.200-gke.70 runs on
Kubernetes v1.33.-gke.900.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release of Distributed Cloud for bare metal.

### Fixed

The following issues were fixed in 1.33.200-gke.70:

* Fixed an issue where configuring your cluster to use [Workload Identity
  Cluster
  Authentication](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/wi-cluster-auth)
  together with a [registry
  mirror](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/registry-mirror)
  caused containerd instability. To use the fix, add the
  `baremetal.cluster.gke.io/enable-gcr-image-credential-refresh: "false"`
  cluster annotation.
* Fixed a timeout issue for the `kubeadm` API server health check that runs
  during bootstrap cluster creation. The timeout issue blocked some cluster
  operations, such as restoring a cluster.
* This patch release doesn't include new [fixes for specific, externally-cited
  vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for
bare metal known
issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

### Issue

For information about the latest known issues, see [Google Distributed Cloud
for bare metal known
issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

### Announcement

Google Distributed Cloud for bare metal 1.31.1100-gke.40 is now available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To
upgrade, see [Upgrade
clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Distributed Cloud for bare metal 1.31.1100-gke.40 runs on
Kubernetes v1.31.12-gke.600.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release of Distributed Cloud for bare metal.

---
## 2025-10-29

### Fixed

The following issues were fixed in 1.32.600-gke.53:

* Fixed the `etcd-cleanup` job timeout issue caused by the use of incorrect certificates.
* Fixed vulnerabilities listed in [Vulnerability
  fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for
bare metal known
issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

### Announcement

Google Distributed Cloud for bare metal 1.32.600-gke.53 is now available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads).
To upgrade, see [Upgrade
clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Google Distributed Cloud for bare metal 1.32.600-gke.53 runs on Kubernetes
v1.32.9-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://docs.cloud.google.com/anthos/docs/resources/partner-storage)
document to make sure the storage vendor has already passed the qualification
for this release of Google Distributed Cloud for bare metal.

---
## 2025-10-15

### Announcement

Google Distributed Cloud for bare metal 1.31.1000-gke.44 is now available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To
upgrade, see [Upgrade
clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Distributed Cloud for bare metal 1.31.1000-gke.44 runs on
Kubernetes v1.31.12-gke.600.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release of Distributed Cloud for bare metal.

### Fixed

The following issues were fixed in 1.31.1000-gke.44:

* Fixed an issue where the cluster restore process leaves the Kubelet
  certificate files as regular files instead of symbolic links, preventing
  certificate rotation.
* Fixed the `etcd-cleanup` job timeout issue caused by the use of incorrect
  certificates.
* Fixed vulnerabilities listed in [Vulnerability
  fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud
for bare metal known
issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

---
## 2025-10-02

### Announcement

Google Distributed Cloud for bare metal 1.33.100-gke.89 is now available for
[download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To
upgrade, see [Upgrade
clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Distributed Cloud for bare metal 1.33.100-gke.89 runs on
Kubernetes v1.33.4-gke.900.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) document
to make sure the storage vendor has already passed the qualification for this
release of Distributed Cloud for bare metal.

### Fixed

The following issues were fixed in 1.33.100-gke.89:

* Fixed an issue where the cluster restore process leaves the Kubelet
  certificate files as regular files instead of symbolic links, preventing
  certificate rotation.
* Fixed the `etcd-cleanup` job timeout issue caused by the use of incorrect
  certificates.
* This patch release doesn't include new [fixes for specific, externally-cited
  vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for
bare metal known
issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

---
## 2025-09-24

### Announcement

Google Distributed Cloud for bare metal 1.32.500-gke.48 is now available for
[download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads).
To upgrade, see [Upgrade
clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Google Distributed Cloud for bare metal 1.32.500-gke.48 runs on Kubernetes
v1.32.8-gke.500.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://cloud.google.com/anthos/docs/resources/partner-storage)
document to make sure the storage vendor has already passed the qualification
for this release of Google Distributed Cloud for bare metal.

### Fixed

The following issues were fixed in 1.32.500-gke.48:

* Fixed an issue where the cluster restore process leaves the Kubelet
  certificate files as regular files instead of symbolic links, preventing
  certificate rotation.
* This patch release doesn't include new [fixes for specific, externally-cited
  vulnerabilities](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for
bare metal known
issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

---
## 2025-09-15

### Announcement

Google Distributed Cloud for bare metal 1.31.900-gke.38 is now available for
[download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads).
To upgrade, see [Upgrade
clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Google Distributed Cloud for bare metal 1.31.900-gke.38 runs on Kubernetes
v1.31.10-gke.300.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://cloud.google.com/anthos/docs/resources/partner-storage)
document to make sure the storage vendor has already passed the qualification
for this release of Google Distributed Cloud for bare metal.

### Fixed

The following issues were fixed in 1.31.900-gke.38:

* Fixed vulnerabilities listed in [Vulnerability
  fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for
bare metal known
issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

---
## 2025-09-02

### Announcement

Google Distributed Cloud for bare metal 1.33.0-gke.799 is now available for
[download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To
upgrade, see [Upgrade
clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Google Distributed Cloud for bare metal 1.33.0-gke.799 runs on Kubernetes
v1.33.2-gke.700.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the
storage vendor has already passed the qualification for this release of Google
Distributed Cloud for bare metal.

### Feature

The following features were added in 1.33.0-gke.799:

* **GA**: Introduced an Envoy sidecar into the GKE Identity Service to
  increase security, reliability, and performance.
* **GA**: Added support for the Ubuntu 24.04 LTS operating system with Linux
  kernel versions, such as 6.8 and 6.11. Support for Linux kernel 6.14 is
  explicitly excluded.
* **GA**: Added the ability to override the cluster-level pod density setting
  for individual node pools.
* **Preview**: Added Node Agent to give you the ability to transition from
  using Ansible over SSH for cluster operations to a more secure, agent-based
  model. Added [`bmctl
  nodeagent`](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#nodeagent)
  commands to provide a straightforward and reliable process of migrating
  existing clusters to use Node Agent.
* **Preview**: Added a bundled version of the [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html#about-the-nvidia-gpu-operator)
  (version 25.3.1). The bundled operator is an open-source solution for
  managing the NVIDIA software components needed to provision and manage GPU
  devices.
* **Preview**: Added Dynamic Resource Allocation, a Kubernetes API that lets
  you request and share generic resources, such as GPUs, among pods and
  containers. When enabled, this capability helps you run AI workloads by
  dynamically and precisely allocating the GPU resources within your bare
  metal clusters, improving resource utilization and performance for demanding
  workloads.
* **Preview**: Added vertical Pod autoscaling, which lets you analyze and set
  CPU and memory resources required by Pods. Instead of having to set
  up-to-date CPU requests and limits and memory requests and limits for the
  containers in your Pods, you can configure vertical Pod autoscaling to
  provide recommended values for CPU and memory requests and limits that you
  can use to manually update your Pods, or you can configure vertical Pod
  autoscaling to automatically update the values.
* **Preview**: Added support for skip minor version cluster upgrades. You can
  directly upgrade your cluster control plane nodes (and entire cluster if
  worker node pools aren't pinned at a lower version) to two minor versions
  above the current version. Added the [`bmctl upgrade
  intermediate-version`](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#upgrade_intermediate-version)
  to print the intermediate version for a skip minor version upgrade.
* Surface failures from node pool status to the `RecentFailures` field in
  cluster status.
* Surface failures from failed preflight checks triggered by the cluster
  controller to the `RecentFailures` field in cluster status.

### Changed

The following functional changes were made in 1.33.0-gke.799:

* Changed logging behavior so that kubeadm logs show up in the journald of the
  node machine where kubeadm runs.
* To help prevent stale ARP cache issues, `iptables-persistent` is installed
  in Debian nodes.
* Cluster manifests are deployed using a Kubernetes job, allowing the cluster
  operator to be more responsive to cluster events.
* Updated the validation checks for cluster upgrades to enforce the [cluster
  version skew
  rules](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_skew)
  for user clusters. If the upgrade version information for a user cluster
  doesn't comply with the version skew rules, the upgrade is halted.
* Updated health checks and upgrade preflight checks to inspect for kubeadm
  certificate expiration.
* Updated etcd version to 3.5.21.
* Removed support for Red Hat Enterprise Linux 8.8 as it is beyond the [Red
  Hat support
  window](https://access.redhat.com/support/policy/updates/errata#RHEL8_and_9_Life_Cycle).
* Removed support for Ubuntu 20.04 LTS as it has reached the end of [standard
  security maintenance in May
  2025](https://ubuntu.com/about/release-cycle#ubuntu-kernel-release-cycle).
* Upgraded `ansible-core` to 2.16.4 to support Python 3.12.
* Increased the RSA key size for Cluster API certifications to 4096 bits for
  improved security.

### Fixed

The following issues were fixed in 1.33.0-gke.799:

* Fixed an issue where restoring a cluster that has a node with a GPU causes
  instability of pods on the nodes.
* Fixed an issue that caused the Ansible playbook for handling Cloud Audit
  Logging to fail and not complete.
* Fixed an issue that caused nodes to get stuck in maintenance mode. Health
  checks have been updated so that the network check job skips connectivity
  checks for nodes that are in maintenance mode.
* Fixed an issue where the CronJob for periodic health checks wasn't updating
  after configuration changes.
* Fixed vulnerabilities listed in [Vulnerability
  fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

---
## 2025-08-28

### Announcement

Google Distributed Cloud for bare metal 1.32.400-gke.68 is now available for
[download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads).
To upgrade, see [Upgrade
clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Google Distributed Cloud for bare metal 1.32.400-gke.68 runs on Kubernetes
v1.32.7-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://cloud.google.com/anthos/docs/resources/partner-storage)
document to make sure the storage vendor has already passed the qualification
for this release of Google Distributed Cloud for bare metal.

### Fixed

The following issues were fixed in 1.32.400-gke.68:

* Fixed an issue that caused the Ansible playbook for handling
  Customer-Acquired Licenses (CAL) to fail and not complete.
* Fixed vulnerabilities listed in [Vulnerability
  fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for
bare metal known
issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

---
## 2025-08-13

### Announcement

Google Distributed Cloud for bare metal 1.31.800-gke.32 is now available for
[download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads).
To upgrade, see [Upgrade
clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).
Google Distributed Cloud for bare metal 1.31.800-gke.32 runs on Kubernetes
v1.31.10-gke.300.

After a release, it takes approximately 7 to 14 days for the version to become
available for installations or upgrades with the [GKE On-Prem API
clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools):
the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage
partners](https://cloud.google.com/anthos/docs/resources/partner-storage)
document to make sure the storage vendor has already passed the qualification
for this release of Google Distributed Cloud for bare metal.

### Fixed

The following issues were fixed in 1.31.800-gke.32:

* Fixed an issue where the CronJob for periodic health checks wasn't updating
  after configuration changes.
* Fixed an issue that caused the Ansible playbook for handling
  Customer-Acquired Licenses (CAL) to fail and not complete.
* Fixed vulnerabilities listed in [Vulnerability
  fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for
bare metal known
issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues)
in the Troubleshooting section.

---
## 2025-08-12

### Announcement

Google Distributed Cloud for bare metal 1.30.1200-gke.63 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.1200-gke.63 runs on Kubernetes v1.30.12-gke.1200. This is the final patch for the 1.30 minor release.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

### Changed

The following functional change was made in 1.30.1200-gke.63:

* Updated the validation checks for cluster upgrades to enforce the [cluster version skew rules](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_skew) for user clusters. If the upgrade version information for a user cluster doesn't comply with the version skew rules, the upgrade is halted.

### Fixed

The following issues were fixed in 1.30.1200-gke.63:

* Fixed an issue where the CronJob for periodic health checks wasn't updating after configuration changes.
* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

---
## 2025-08-08

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

### Announcement

Google Distributed Cloud for bare metal 1.32.300-gke.85 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.300-gke.85 runs on Kubernetes v1.32.4-gke.1000.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

### Changed

The following functional change was made in 1.32.300-gke.85:

* Updated the validation checks for cluster upgrades to enforce the [cluster version skew rules](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_skew) for user clusters. If the upgrade version information for a user cluster doesn't comply with the version skew rules, the upgrade is halted.

### Fixed

The following issues were fixed in 1.32.300-gke.85:

* Fixed a [known issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#keepalived-config-issue) where Keepalived failover is blocked when the corresponding HAProxy instance is unreachable. This issue prevented the control plane VIP from being made available on a new, healthy node.
* Fixed an issue where the CronJob for periodic health checks wasn't updating after configuration changes.
* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

---
## 2025-08-04

### Announcement

Google Distributed Cloud for bare metal 1.32.300-gke.85 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.300-gke.85 runs on Kubernetes v1.32.4-gke.1000.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

### Changed

The following functional change was made in 1.32.300-gke.85:

* Updated the validation checks for cluster upgrades to enforce the [cluster version skew rules](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_skew) for user clusters. If the upgrade version information for a user cluster doesn't comply with the version skew rules, the upgrade is halted.

### Fixed

The following issues were fixed in 1.32.300-gke.85:

* Fixed a [known issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#keepalived-config-issue) where Keepalived failover is blocked when the corresponding HAProxy instance is unreachable. This issue prevented the control plane VIP from being made available on a new, healthy node.
* Fixed an issue where the CronJob for periodic health checks wasn't updating after configuration changes.
* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

---
## 2025-07-22

### Announcement

Google Distributed Cloud for bare metal 1.31.700-gke.72 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.700-gke.72 runs on Kubernetes v1.31.10-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

### Changed

The following functional changes were made in 1.31.700-gke.72:

* Updated the validation checks for cluster upgrades to enforce the [cluster version skew rules](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_skew) for user clusters.

### Fixed

The following issues were fixed in 1.31.700-gke.72:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

---
## 2025-07-21

### Announcement

Google Distributed Cloud for bare metal 1.30.1100-gke.67 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.1100-gke.67 runs on Kubernetes v1.30.12-gke.800.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

### Fixed

The following issues were fixed in 1.30.1100-gke.67:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

---
## 2025-07-17

### Announcement

Google Distributed Cloud for bare metal 1.32.200-gke.104 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.200-gke.104 runs on Kubernetes v1.32.4-gke.1000.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

### Fixed

The following issues were fixed in 1.32.200-gke.104:

* Fixed a [known issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#keepalived-config-issue) where Keepalived failover is blocked when the corresponding HAProxy instance is unreachable. This issue prevented the control plane VIP from being made available on a new, healthy node.
* Fixed an issue that caused nodes to get stuck in maintenance mode. Health checks have been updated so that the network check job skips connectivity checks for nodes that are in maintenance mode.
* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

---
## 2025-06-23

### Announcement

Google Distributed Cloud for bare metal 1.31.600-gke.85 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.600-gke.85 runs on Kubernetes v1.31.8-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

### Fixed

The following issues were fixed in 1.31.600-gke.85:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

---
## 2025-06-10

### Announcement

Google Distributed Cloud for bare metal 1.30.1000-gke.85 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.30.1000-gke.85 runs on Kubernetes v1.30.12-gke.100.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

### Fixed

The following issues were fixed in 1.30.1000-gke.85:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

---
## 2025-06-04

### Announcement

Google Distributed Cloud for bare metal 1.32.100-gke.106 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.100-gke.106 runs on Kubernetes v1.32.4-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

### Changed

Introduced an Envoy sidecar into the GKE Identity Service to increase security, reliability, and performance.

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

---
