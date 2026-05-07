# Google Distributed Cloud (software only) for VMware

## 2026-05-06

### Announcement

Google Distributed Cloud (software only) for VMware 1.35.0-gke.525 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).
Google Distributed Cloud 1.35.0-gke.525 runs on Kubernetes v1.35.2-gke.300.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

### Announcement

The following features were added in 1.35.0-gke.525:

* Platform update to Kubernetes 1.35: This release updates the underlying Kubernetes version to 1.35.

  This release requires the use of `cgroupsv2`. Using `cgroupsv1` is no longer supported and cluster creation or upgrades will fail. A preflight check will actively block the operation if `cgroupsv1` is detected.
  + As part of the sunset of `cgroupsv1`, the legacy `ubuntu`, `ubuntu_containerd`, and `cos` `OSImageType` options are no longer supported in this release.
  + For more information on migrating to `cgroupsv2`, see the Kubernetes documentation on [migrating to cgroupv2](https://kubernetes.io/docs/concepts/architecture/cgroups/#migrating-cgroupv2).
  + This release also upgrades the container runtime, containerd, from version 2.0 to 2.1.
* The Ubuntu image has been upgraded to 24.04 on all node types for 1.35.0-gke.525.
  When you upgrade your control plane and node pools, the nodes are
  automatically recreated with the new operating system image.
* `gkectl` prints the Operation ID and Operation Type to the console after
  cluster operations.
* For advanced clusters, the default node pool update policy is changed to parallel
  instead of sequential. This applies to all advanced clusters (both new and
  existing upon upgrade). To customize or revert this behavior, use the
  `nodePoolUpdatePolicy` and `maximumConcurrentNodePoolUpdate` fields in the
  cluster configuration file.
* The default Docker bridge IP for advanced clusters has been changed to `169.
  254.123.1/24` instead of `172.17.0/16`. This change reduces the likelihood of
  conflicts with user-configured networks. If you use the `172.17.0/16` range
  for other purposes, cluster creation might fail due to this conflict.
* `vsphere-csi-controller` in advanced clusters is deployed on the user
  cluster control plane nodes instead of worker nodes. This architectural
  change happens automatically during upgrade and does not impact resource
  sizing recommendations.

### Fixed

The following issues were fixed in 1.35.0-gke.525:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).
* Resolved an issue that caused VMware cluster upgrades from non-advanced
  clusters to advanced clusters to get stuck. The system attempted to update
  immutable fields in the Hub membership. With this fix, the cluster operator
  preserves the original membership fields during the upgrade process instead of
  attempting to overwrite them so that the migration to an advanced cluster
  completes successfully.
* Fixed an issue in Advanced user clusters where the `cloud.google.com/
  gke-nodepool` label for workload node pools unexpectedly included an `-np`
  suffix. This caused pods using `nodeSelector` targeting the original pool
  name (such as Apigee workloads) to fail to schedule. For clusters on older
  versions experiencing this issue, you can work around it by manually setting
  the expected label in the node pool configuration.
* Fixed an issue where setting the deprecated `stackdriver.enableVPC` field to
  `true` in a cluster configuration file would block upgrades to an Advanced
  Cluster. The `stackdriver.enableVPC` field has been deprecated and its
  setting will be ignored during the upgrade validation process. For clusters on
  older versions experiencing this issue, you can work around it by removing
  the field or setting it to `false` in your configuration file before
  upgrading.
* Fixed an issue where the node-problem-detector was incorrectly deployed onto
  non-Advanced VMware clusters. This caused the containerd runtime to
  continuously restart on affected nodes due to incompatible health check
  configurations, leading to ETCD/CRI failures (such as errors connecting to
  `/run/containerd/containerd.sock`) and unsuccessful cluster upgrades.
* Fixed an issue where leading or trailing whitespaces in the proxy.url field,
  or spaces after commas in the proxy.noProxy list in the cluster configuration
  file, caused advanced cluster creation or upgrades to fail. This release adds
  validation to reject such malformed configurations before operations begin.
  For upgrades, logic has been added to automatically handle and clean up these
  spaces in the operator cluster state to prevent upgrade failures. If you are
  using an older version and encounter this issue, ensure that all proxy
  configuration fields are free of extraneous spaces.
* Fixed an issue where retrying the gkectl upgrade admin command after a
  previous failure would fail with a "failed to create credential namespace in
  bootstrap cluster" error. This occurred because the setup process failed to
  handle resources that already existed from the previous attempt. This fix
  resolves the issue described in [`gkectl upgrade admin` fails on retry with "AlreadyExists" errors in the bootstrap cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#gkectl-upgrade-admin-fails-on-retry-with-alreadyexists-errors-in-the-bootstrap-cluster), eliminating the need to manually delete conflicting
  resources from the bootstrap cluster before retrying.
* Fixed an issue where the system's root certificates were ignored when a
  custom CA certificate was configured for a registry mirror or private
  registry. This caused cluster creation or upgrades to fail with an x509:
  certificate signed by unknown authority error when attempting to pull images.
  The system honors both the custom CA and the system's root certificates.
* Fixed an issue where vSphere VM creation could hang indefinitely, with the
  operation remaining stuck in the Creating phase and logs repeatedly reporting
  "VM creation in progress." This fix introduces a one-hour timeout for VM
  creation and ensures the machine status is updated in Kubernetes during each
  reconciliation, eliminating the need to manually delete the stuck VM resource
  from the temporary bootstrap cluster to recover.
* Fixed an issue where upgrading non-advanced clusters with OIDC configuration
  to advanced clusters caused users to fail to log in via Anthos Identity
  Service (AIS) immediately after the upgrade.

---
## 2026-04-23

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.1100-gke.84 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).
Google Distributed Cloud 1.32.1100-gke.84 runs on Kubernetes v1.32.13-gke.100.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.32.1100-gke.84:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).
* Resolved an issue that caused VMware cluster upgrades from non-advanced
  clusters to advanced clusters to get stuck. The system attempted to update
  immutable fields in the Hub membership. With this fix, the cluster operator
  preserves the original membership fields during the upgrade process instead of
  attempting to overwrite them so that the migration to an advanced cluster
  completes successfully.

---
## 2026-04-22

### Announcement

Google Distributed Cloud (software only) for VMware 1.33.700-gke.71 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).
Google Distributed Cloud 1.33.700-gke.71 runs on Kubernetes v1.33.5-gke.2200.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.33.700-gke.71:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history).
* Resolved an issue that caused VMware cluster upgrades from non-advanced
  clusters to advanced clusters to get stuck. The system attempted to update
  immutable fields in the Hub membership. With this fix, the cluster operator
  preserves the original membership fields during the upgrade process instead of
  attempting to overwrite them so that the migration to an advanced cluster
  completes successfully.
* Fixed an issue in advanced user clusters where the `cloud.google.com/gke-nodepool` label for workload node pools unexpectedly included an `-np`
  suffix. This caused pods using `nodeSelector` targeting the original pool
  name (such as Apigee workloads) to fail to schedule. For clusters on older
  versions experiencing this issue, you can manually set
  the expected label in the node pool configuration.
* Fixed an issue where setting the deprecated `stackdriver.enableVPC` field to
  `true` in a cluster configuration file would block upgrades to an Advanced
  Cluster. The `stackdriver.enableVPC` field has been deprecated and its
  setting is now ignored during the upgrade validation process. For clusters on
  older versions experiencing this issue, remove
  the field or set it to `false` in your configuration file before
  you upgrade.
* Fixed an issue where the `node-problem-detector` was incorrectly deployed onto
  non-Advanced VMware clusters. This caused the `containerd` runtime to
  continuously restart on affected nodes due to incompatible health check
  configurations, leading to ETCD/CRI failures (such as errors connecting to
  `/run/containerd/containerd.sock`) and unsuccessful cluster upgrades.

### Feature

The following feature was added in 1.33.700-gke.71:

* Improved the resilience of migration from regular clusters to advanced
  clusters. If a migration attempt fails or is interrupted, you can now safely
  retry the process without manual cleanup. The system automatically reuses
  existing resources and the temporary bootstrap cluster when you retry.
  **Important:** If a migration fails, do not delete the bootstrap cluster,
  because deleting the bootstrap cluster can cause data loss and prevent
  recovery.

---
## 2026-04-15

### Announcement

Google Distributed Cloud (software only) for VMware 1.34.300-gke.59 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).
Google Distributed Cloud 1.34.300-gke.59 runs on Kubernetes v1.34.3-gke.400.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.34.300-gke.59:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).
* Fixed an issue where upgrading to an Advanced Cluster caused an unexpected -np suffix
  to be appended to node pool labels (such as cloud.google.com/gke-nodepool). This could
  prevent pods from being scheduled on the correct nodes if they rely on node selectors
  with exact matches for these labels.
* Fixed an issue where setting the deprecated `stackdriver.enableVPC` field to `true` in
  a cluster configuration file blocked upgrades to an Advanced Cluster. This field has no
  current function, and the upgrade validation now ignores it, allowing
  upgrades to proceed.
* Fixed an issue where, during migration to Advanced Clusters, a new version of the
  node-problem-detector was incorrectly deployed onto existing non-Advanced (V1) nodes.
  Because its health check logic was incompatible with these older nodes, it repeatedly
  restarted the container runtime (containerd), causing cluster upgrade failures.
* Fixed an issue where retrying the `gkectl upgrade admin` command after a previous
  failure failed with `AlreadyExists` errors (such as failing to create the credential
  namespace) in the bootstrap cluster. The command was updated to automatically
  handle resources left over from a previous attempt, making it safe to retry directly
  and eliminating the need for manual cleanup.
* Fixed an issue where cluster creation or upgrade failed if the proxy or
  noProxy configuration fields contained leading or trailing whitespaces. These spaces
  resulted in malformed arguments for the control plane load balancer initialization
  job, causing the control plane load balancer initialization to fail.
* Fixed an issue where the system certificate pool was ignored when a custom CA certificate
  was configured for a registry mirror. This caused image pull failures (such as `certificate
  signed by unknown authority` when pulling the Kind image) during cluster upgrades.
* Fixed an issue where if updates or upgrades to advanced admin clusters failed and the external
  bootstrap cluster was deleted, you could lose critical data related to cluster state (not user workload
  data).

---
## 2026-03-27

### Fixed

The following issues were fixed in 1.33.600-gke.40:

* Fixed an issue where if updates or upgrades to advanced admin clusters failed and the external bootstrap cluster was deleted, you could lose critical data.

### Fixed

The following issues were fixed in 1.32.1000-gke.57:

* Fixed an issue where the node-problem-detector was incorrectly deployed onto
  non-Advanced (V1) VMware clusters, causing the containerd runtime to
  continuously restart on affected nodes, leading to ETCD/CRI failures and
  unsuccessful cluster upgrades.
* Fixed an issue where setting the deprecated stackdriver.enableVPC field to
  true in a cluster configuration file would block upgrades to an Advanced
  Cluster. The stackdriver.enableVPC field has been deprecated and its setting is
  now ignored during the upgrade validation process.
* Fixes an issue where Advanced Clusters incorrectly deployed the node problem
  detector onto non-Advanced clusters, which caused containerd to continuously
  restart and led to cluster upgrade failures.
* Fixed an issue where the system certificate pool was ignored when a custom CA
  certificate was configured for a registry mirror.
* Fixed an issue where retrying the `gkectl upgrade admin` command after a
  previous failure could fail with "AlreadyExists" errors in the bootstrap cluster.
* Fixed an issue where cluster creation or upgrade failed if the proxy or
  noProxy configuration fields contained extraneous whitespaces. These spaces
  interfered with internal command-line argument parsing, causing the control
  plane load balancer initialization to fail.
* Fixed an issue where if updates or upgrades to advanced admin clusters failed
  and the external bootstrap cluster was deleted, you could lose critical data.

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.1000-gke.57 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).
Google Distributed Cloud 1.32.1000-gke.57 runs on Kubernetes v1.32.13-gke.1000.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

### Announcement

Google Distributed Cloud (software only) for VMware 1.33.600-gke.40 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).
Google Distributed Cloud 1.33.600-gke.40 runs on Kubernetes 1.33.5-gke.2200.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

---
## 2026-03-23

### Announcement

Google Distributed Cloud (software only) for VMware 1.33.600-gke.39 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).
Google Distributed Cloud 1.33.600-gke.39 runs on Kubernetes v1.33.5-gke.2200.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.33.600-gke.39:

* Fixed an issue where the node-problem-detector was incorrectly deployed onto
  non-Advanced (V1) VMware clusters, causing the containerd runtime to
  continuously restart on affected nodes, leading to ETCD/CRI failures and
  unsuccessful cluster upgrades.
* Fixed an issue where setting the deprecated stackdriver.enableVPC field to
  true in a cluster configuration file would block upgrades to an Advanced
  Cluster. The stackdriver.enableVPC field has been deprecated and its setting is
  now ignored during the upgrade validation process.
* Fixes an issue where Advanced Clusters incorrectly deployed the node problem
  detector onto non-Advanced clusters, which caused containerd to continuously
  restart and led to cluster upgrade failures.
* Fixed an issue where retrying the `gkectl upgrade admin` command after a
  previous failure could fail with "AlreadyExists" errors in the bootstrap cluster.
* Fixed an issue where cluster creation or upgrade failed if the proxy or
  noProxy configuration fields contained extraneous whitespaces. These spaces
  interfered with internal command-line argument parsing, causing the control
  plane load balancer initialization to fail.
* Fixed an issue where the system certificate pool was ignored when a custom CA
  certificate was configured for a registry mirror.

---
## 2026-03-20

### Change

**Important: Mandatory flag for admin cluster upgrades**

If an update or upgrade to advanced admin clusters fails in versions 1.32 and newer, don't delete the external bootstrap cluster from the workstation. The bootstrap cluster contains required information about states that you need to resume the update or upgrade. If an update or upgrade to admin clusters fails, and you re-run `gkectl upgrade admin`, you must add the flag `--reuse-bootstrap-cluster` or you can lose critical data.

---
## 2026-03-18

### Fixed

The following issues were fixed in 1.34.200-gke.68:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).
* Google Distributed Cloud (software only) for VMware V2 (Advanced Clusters) versions 1.31
  and earlier were missing a configuration step in the node startup script that
  defined the Docker default bridge IP range. As a result, Docker defaulted to
  using the 172.17.0.0/16 (and in some cases 172.16.0.0/16) address range.
* Fixed an issue where an admin cluster upgrade appeared to be stuck indefinitely
  and users would see the `VSphereMachine` remaining in the `Creating` phase
  without actionable error messages.

### Announcement

Google Distributed Cloud (software only) for VMware 1.34.200-gke.68 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).

**Important: There is a mandatory flag for admin cluster upgrades; see the updated entry for [March 20, 2026](#March_20_2026).**

Google Distributed Cloud 1.34.200-gke.68 runs on Kubernetes v1.34.3-gke.400.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

---
## 2026-03-05

### Fixed

The following issues were fixed in 1.32.900-gke.60:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.900-gke.60 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).

**Important: There is a mandatory flag for admin cluster upgrades; see the updated entry for [March 20, 2026](#March_20_2026).**

Google Distributed Cloud 1.32.900-gke.60 runs on Kubernetes v1.32.11-gke.200.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

### Change

Google Distributed Cloud (software only) for VMware V2 (Advanced Clusters) versions 1.31
and earlier were missing a configuration step in the node startup script that
defined the Docker default bridge IP range. As a result, Docker defaulted to
using the 172.17.0.0/16 (and in some cases 172.16.0.0/16) address range.

If this default range overlaps with customer network infrastructure,
connectivity failures during cluster creation or operation can occur.

This issue has been resolved. The Docker default bridge IP for cluster nodes in
advanced clusters is now explicitly set to 169.254.123.1/24.

---
## 2026-03-03

### Fixed

The following issues were fixed in 1.33.500-gke.63:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

### Announcement

Google Distributed Cloud (software only) for VMware V2 (Advanced Clusters) versions 1.31
and earlier were missing a configuration step in the node startup script that
defined the Docker default bridge IP range. As a result, Docker defaulted to
using the 172.17.0.0/16 (and in some cases 172.16.0.0/16) address range.

If this default range overlaps with customer network infrastructure,
connectivity failures during cluster creation or operation can occur.

This issue has been resolved. The Docker default bridge IP for cluster nodes in
advanced clusters is now explicitly set to 169.254.123.1/24.

### Announcement

Google Distributed Cloud (software only) for VMware 1.33.500-gke.63 is now available
for download. To upgrade, see [Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading.md).

**Important: There is a mandatory flag for admin cluster upgrades; see the updated entry for [March 20, 2026](#March_20_2026).**

Google Distributed Cloud 1.33.500-gke.63 runs on Kubernetes v1.33.5-gke.2200.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

---
## 2026-02-19

### Breaking

Upgrading to advanced clusters overwrites any existing `cert-manager`. For more
information, see [Upgrade to `cert-manager` bundled with advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster#upgrade-cert-manager).

---
## 2026-02-13

### Announcement

Google Distributed Cloud (software only) for VMware 1.34.100-gke.93 is now available
for download. To upgrade, see Upgrade a cluster. Google Distributed Cloud
1.34.100-gke.93 runs on Kubernetes v1.34.1-gke.4700.

If you are using a third-party storage vendor, check the Google Distributed Cloud-ready
storage partners document to make sure the storage vendor has already passed the
qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become
available for use with GKE On-Prem API clients: the Google Cloud console, the
gcloud CLI, and Terraform.

### Feature

The following feature was added in 1.34.100-gke.93:

You can deploy `vsphere-csi-controller` in the advanced cluster on the user
cluster control plane nodes.

---
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
