# Cluster Toolkit

## 2025-11-03

### Feature

Cluster Toolkit version v1.71.0 is available. This release includes a
fix for a munge mount on login failure due to slow controller Slurm v6 setup, and
adds Managed Lustre support in the `gke-a4x` blueprint. For more information about
this release, see the [Release announcement on
GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4810).

---
## 2025-10-24

### Feature

Cluster Toolkit version v1.70.0 is available. This release adds
automated TPU support and Cloud Storage FUSE mounts in the TPU v6 blueprint and refactors
the H4D blueprint. This version also includes breaking changes, such as removing
support for the `maintenance_interval` field for reservations created by [Technical Account Managers (TAMs)](https://cloud.google.com/tam) and
migrating Jobset from static manifests to a Helm chart. For a complete list of
changes, see the [Release announcement on
GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4783).

---
## 2025-10-21

### Feature

Cluster Toolkit version v1.69.0 is available. This release adds
NUMA-aware scheduling in GKE clusters for G4 machines and adds a new module that
provides mount scripts for WEKA filesystems. This version also includes PSA
updates and adds a GKE sample for running the `nvidia-bug-report` shell script. For details, see
the [Release announcement on
GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4772).

---
## 2025-10-10

### Feature

Cluster Toolkit release version v1.68.0 is available. This release
introduces the option to download the NVIDIA Collective Communications Library
(NCCL) software packages `libnccl2` and `libnccl-dev` for A3U and A4H machine
types, as well as other minor changes. For more information about this release,
see the [Release Announcement on
GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4756).

This release supports the generally available, open-source IBM Spectrum Symphony
HostFactory connectors for Google Compute Engine and Google Kubernetes Engine
(GKE), which can be deployed through Cluster Toolkit to extend your on-premises
cluster or run entirely within Google Cloud. For more information, see [Run IBM
Spectrum Symphony
workloads](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony).

---
## 2025-09-19

### Feature

Cluster Toolkit release version v1.67.0 is available. This release
introduces additional support for aarch64-based architecture, as well as other
minor changes. For more information about this release, see the [Release
Announcement on
GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4674).

---
## 2025-09-15

### Feature

Cluster Toolkit release version v1.66.0 is available. This release
enables Cloud Storage FUSE for H4D machine types and sets the
default cluster availability to zonal, as well as other minor changes. For more
information about this release, see the [Release Announcement on
GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4655).

---
## 2025-08-14

### Feature

Cluster Toolkit version v1.62.0 is available. This release adds new
blueprints for A4X instances and introduces a community scheduler module for
Slinky (Slurm on Kubernetes). For more details, see the [Release announcement on
GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4514).

---
