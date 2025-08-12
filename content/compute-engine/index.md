# Compute Engine

## 2025-08-11

### Feature

**Preview**: The
[G4 accelerator-optimized machine series](https://cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)
is designed for graphics-intensive workloads such as NVIDIA Omniverse
simulations, video transcoding, and virtual desktops. The G4 machine series also
provides a cost-effective solution for single-host inference and model tuning.

Powered by the 5th Generation AMD EPYC Turin CPU platform and featuring
[NVIDIA RTX PRO 6000 Blackwell Server Edition](https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/)
GPUs, the G4 machine series offer significant performance improvements over the
previous G2 machine series. For available G4
regions and zones, see
[GPU regions and zones](https://cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).

To get started with G4 machine types, contact your Google account team.

### Feature

You can attach up to 128 instances to the same Hyperdisk ML volume whose size is between 2 TiB and 16 TiB. The previous limit was 30. For more information, see [Share a disk between instances](https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

---
## 2025-08-05

### Feature

For Hyperdisk Throughput, the maximum IOPS for a single volume has increased from 600 MiB/s to 2,400 MiB/s. The maximum IOPS for a single volume has increased from 2,400 IOPS to 9,600 IOPS. Hyperdisk Throughput volumes are designed for cost-sensitive workloads, analytics workloads, and workloads that have sequential I/O and large block sizes. For more information, see [About Hyperdisk Throughput](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput).

### Feature

**Generally Available**: The storage-optimized Z3 machine series offers a bare metal (`z3-highmem-192-highlssd-metal`) machine type with 192 vCPUs, 1,536 GB of memory, and 72 TiB of Local SSD storage.

Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. Z3 uses [Titanium](https://cloud.google.com/titanium) to deliver more compute and memory resources for your workloads by offloading network and I/O processing from the host hardware. To learn more, see [Z3 machine series](https://cloud.google.com/compute/docs/storage-optimized-machines#z3_series). For information about bare metal instances, including regional availability, see [Bare metal instances on Compute Engine](https://cloud.google.com/compute/docs/instances/bare-metal-instances).

### Deprecated

The Compute Engine feature that deploys containers on VMs during VM creation is deprecated. For more information about the alternative solutions for running containers on VMs and MIGs, see [Compute Engine container startup agent deprecation](https://cloud.google.com/compute/docs/deprecations/container-startup-agent-on-compute).

---
## 2025-07-30

### Feature

**Generally available**: The general purpose C4 machine series now supports the following machine types on Intel's Xeon 6 processor (Granite Rapids):

* C4 VMs with Titanium Local SSD attached using new machine types:
  + `c4-standard-*-lssd`
  + `c4-highmem-*-lssd`
* New bare metal machine types:
  + `c4-standard-288-metal`
  + `c4-highmem-288-metal`
* C4 `standard`, `highmem`, and `highcpu` VMs with 144 and 288 vCPUs

To learn more, see the [C4 machine series](https://cloud.google.com/compute/docs/general-purpose-machines#c4_series).

For more information, about the attached Local SSD disks, see [Machine types that automatically attach Local SSD disks](https://cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed).

---
## 2025-07-25

### Changed

Hyperdisk Extreme is available in all regions and zones.
For more information, see [About Hyperdisk Extreme](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme).

### Changed

You can now resize Hyperdisk Balanced volumes twice within a 4-hour window. For more information, see [Capacity changes](https://cloud.google.com/compute/docs/disks/modify-hyperdisks#capacity_changes).

---
## 2025-07-24

### Feature

**Generally available**: The general-purpose C4 machine series now supports Hyperdisk Balanced High Availability. For more information, see [Supported disk types for C4](https://cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4).

---
## 2025-07-23

### Changed

When a regional Persistent Disk volume is fully replicated, Compute Engine now refreshes its replica recovery checkpoint every 15 minutes.

Learn more about [Regional Persistent Disk replica recovery checkpoints](https://cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd-replica-recovery-checkpoint) and [how to use checkpoints to recover a degraded disk](https://cloud.google.com/compute/docs/disks/repd-failover#recover-repd-using-checkpoint).

---
## 2025-07-22

### Feature

**Preview**: Multi-writer support for Hyperdisk Extreme disks. You can give up to 16 instances simultaneous read-write access to the same disk. For more information, see [Share disks between instances](https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

---
## 2025-07-21

### Feature

**Generally available**: The general-purpose C4D machine series offers the following bare metal machine types:

* `c4d-standard-384-metal`
* `c4d-highcpu-384-metal`
* `c4d-highmem-384-metal`

This is the first machine series to offer AMD-based bare metal instances. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. C4D uses [Titanium](https://cloud.google.com/titanium) to deliver more compute and memory resources for your workloads by offloading network and I/O processing from the host hardware. To learn more, see [C4D machine series](https://cloud.google.com/compute/docs/general-purpose-machines#c4d_series). For information about bare metal instances, including regional availability, see [Bare metal instances on Compute Engine](https://cloud.google.com/compute/docs/instances/bare-metal-instances#c4d-metal).

---
## 2025-07-18

### Feature

**Generally available**: You can create instant and standard snapshots from Hyperdisk volumes in multi-writer mode. You can also clone Hyperdisk volumes in multi-writer mode.

For more information, see [Share disks between instances](https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

---
## 2025-07-15

### Changed

Compute flexible committed use discounts (CUDs) offer expanded coverage by
supporting the following resources and services:

* Memory-optimized M1, M2, M3, and M4 VMs
* Compute-optimized H3 instances
* Cloud Run services with request-based billing
* Cloud Run Functions

To receive the expanded coverage for flexible CUDs, you must opt in to the new
spend-based CUD model. Cloud Billing accounts that meet specific criteria are
automatically opted into the new model. On January 21, 2026, all remaining
accounts will automatically migrate to the new model. You can opt in before that
date to start receiving the expanded coverage. To learn more about the new model
and the opt-in details, see
[Spend-based CUDs program improvements](https://cloud.google.com/docs/cuds-multiprice).

To learn more about this change and how your flexible CUDs apply after you opt
in, see
[Compute flexible CUDs](https://cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).

---
## 2025-07-02

### Feature

**Preview**: You can reserve GPU VMs that use A4 and A3 Ultra machine types by using future reservations in calendar mode. This feature lets you reserve up to 80 GPU VMs for up to 90 days to obtain capacity for the following workloads:

* Model pre-training jobs
* Model fine-tuning jobs
* High performance computing (HPC) simulation workloads
* Short-term expected increases in inference workloads

For more information, see [About future reservation requests in calendar mode](https://cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

### Feature

**Generally available**: You can create Z3 VMs using smaller machine types, ranging in size from 14 to 88 vCPUs. Also, Z3 now offers `-standardlssd` and `-highlssd` predefined machine types. These new machine types have different amounts of Local SSD capacity per vCPU.

When you use Local SSD disks with Z3 VMs, you can receive committed use discounts (CUDs) without needing to [attach reservations to your commitments](https://cloud.google.com/compute/docs/instances/reservations-with-commitments#committed_resources_that_require_attached_reservations).

For more information, see [Storage-optimized machines](https://cloud.google.com/compute/docs/storage-optimized-machines).

### Feature

**Preview**: The general purpose C4 machine series now supports the following machine types on Intel's Xeon 6 processor (Granite Rapids):

* C4 VMs with Titanium Local SSD attached using two new machine types:
  + `c4-standard-*-lssd`
  + `c4-highmem-*-lssd`
* Three new bare metal machine types:
  + `c4-standard-288-metal`
  + `c4-highcpu-288-metal`
  + `c4-highmem-288-metal`
* C4 `standard`, `highmem`, and `highcpu` VMs with 144 and 288 vCPUs

To learn more, see the [C4 machine series](https://cloud.google.com/compute/docs/general-purpose-machines#c4_series).

For more information, about the attached Local SSD disks, see [Machine types that automatically attach Local SSD disks](https://cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed).

---
## 2025-06-30

### Feature

**Generally available**: You can now modify licenses attached to your disks. Previously, licenses on disk resources were immutable. You had to delete and recreate disks, or engage our support team to change licenses.

This feature provides greater flexibility for managing your disk licenses. You can now:

* Append, remove, replace, and view the history of license updates.
* Perform in-place license upgrades, such as [Ubuntu to Ubuntu Pro](https://cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu), using the `gcloud` CLI and REST.
* [Switch from PAYG to BYOS billing](https://cloud.google.com/compute/docs/licenses/switch-between-payg-and-byos) models.
* Review [license changes and restrictions](https://cloud.google.com/compute/docs/licenses/license-changes-and-restrictions) and [append a RHEL ELS](https://cloud.google.com/compute/docs/images/premium/rhel/append-els-licenses) license to a newer version.

For more information on how to manage licenses, see [Manage licenses](https://cloud.google.com//compute/docs/licenses/manage).

---
## 2025-06-27

### Feature

**Generally available**: You can specify a custom ephemeral external IPv6 address when creating an instance. For more information, see [Create instances that use IPv6 addresses](https://cloud.google.com/compute/docs/instances/create-ipv6-instance).

---
## 2025-06-13

### Feature

**Generally available**: General purpose [C4D machine types](https://cloud.google.com/compute/docs/general-purpose-machines#c4d_series), powered by the fifth generation AMD EPYC processors (Turin) and Google Titanium, are generally available.

C4D is designed to run mission-critical workloads including web app and game servers, AI inference, web serving, video streaming, and data centric applications like analytics, relational, and in-memory databases.

C4D is available in `standard`, `highmem`, and `highcpu` machine types and supports only Google Cloud Hyperdisk storage and Titanium SSD. To learn more about C4D, refer to the [C4D release blog](https://www.google.com/url?q=https://cloud.google.com/blog/products/compute/c4d-vms-unparalleled-performance-for-business-workloads). For details about where you can create C4D instances, see the [Regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) page.

### Feature

**Preview**: Dynamic NICs let you add or remove network interfaces to or from an instance without having to restart or recreate the instance.

You can also use Dynamic NICs when you need more network interfaces. The maximum number of vNICs for most machine types in Google Cloud is 10; however, you can configure up to 16 total interfaces by using Dynamic NICs.

For more information, see the following:

* [Multiple network interfaces overview](https://cloud.google.com/vpc/docs/multiple-interfaces-concepts)
* [Create VM instances with multiple network interfaces](https://cloud.google.com/vpc/docs/create-use-multiple-interfaces)
* [Add Dynamic NICs to an instance](https://cloud.google.com/vpc/docs/add-dynamic-nics)

---
## 2025-06-11

### Feature

**Preview**: The storage-optimized Z3 machine series offers a bare metal (`-metal`) machine type with 192 vCPUs. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. To learn more, see [Z3 machine series](https://cloud.google.com/compute/docs/storage-optimized-machines#z3_series). For information about bare metal instances, including regional availability, see [Bare metal instances on Compute Engine](https://cloud.google.com/compute/docs/instances/bare-metal-instances).

---
## 2025-06-10

### Security

A vulnerability (CVE-2025-2884) affecting Shielded VMs using virtual Trusted Platform Module (vTPM) was discovered and is being addressed. For more information, see the [GCP-2025-031 security bulletin](https://cloud.google.com/compute/docs/security-bulletins#gcp-2025-031).

---
## 2025-06-06

### Changed

**Generally available**: The [Security Risk Overview dashboard for Compute Engine](https://cloud.google.com/compute/docs/monitor-security-risks-console) is generally available. In addition, it provides a **Top CVE findings** table that lists the most severe CVEs that affect your Compute Engine instances.

---
## 2025-06-04

### Feature

**Preview**: OS Login now supports connections from SSH certificates in addition to SSH keys. For more information, see [Set up OS Login to require SSH certificates for SSH connections](https://cloud.google.com/compute/docs/oslogin/certificates).

---
## 2025-06-03

### Feature

**Preview**: You can enable your project to send HTTP requests to a Compute Engine feature alpha URI. This action lets you test and develop with experimental features in the alpha stage using REST. For more information, see [Use the Compute Engine API in alpha](https://cloud.google.com/compute/docs/reference/rest/alpha).

---
## 2025-06-02

### Feature

**Preview**: The general-purpose C4D machine series offers bare metal (`-metal`) machine types with 384 vCPUs. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. To learn more, see [C4D machine series](https://cloud.google.com/compute/docs/general-purpose-machines#c4d_series). For information about bare metal instances, including regional availability, see [Bare metal instances on Compute Engine](https://cloud.google.com/compute/docs/instances/bare-metal-instances).

---
