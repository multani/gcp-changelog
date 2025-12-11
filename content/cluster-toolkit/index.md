# Cluster Toolkit

## 2025-12-04

### Feature

Cluster Toolkit version v1.74.0 is available. This release adds support
for Google Cloud NetApp Volumes and introduces new blueprint files for TPU 7x
instances. This release also adds a `force_conflicts` flag that you can use when
you apply manifests using the `kubectl` command. This release also updates the
`nccl-tcpxo-installer`, `nri-device-injector`, and `nccl-test` values for
`a3-megagpu-8g` machines. For more information about this release, see the
[Release announcement on
GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4934).

---
## 2025-11-19

### Feature

Cluster Toolkit version v1.73.0 is available. This release adds support
for the
[GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway)
and adds a new blueprint for [A3
High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) machines that
automates the process of building a custom image with a TCPx-patched kernel for
enhanced network performance. This version also includes an initial blueprint
for [G4 machine types](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) and parameterized the
gIB NCCL RDMA plugin installer in the `gke-a4x.yaml` blueprint. For more
information about this release, see the [Release announcement on
GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4857).

---
## 2025-11-13

### Feature

Cluster Toolkit version v1.72.0 is available. This release adds support
for Google Cloud Managed Lustre as an optional storage solution for the
`gke-tpu-v6-advanced` blueprint. This release also adds four example
blueprints to support the deployment of Sycomp storage. In addition, this release makes
improvements to the `gke-node-pool` module and `a4xhigh-slurm-blueprint.yaml`
blueprint. For more information about this release, see the [Release
announcement on
GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/4841).

---
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
