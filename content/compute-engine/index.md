# Compute Engine

## 2026-01-07

### Feature

**Generally available**: You can view future resource availability before you
create a future reservation request in calendar mode. This action helps increase
the likelihood that Google Cloud approves your request. For more information,
see
[View resource future availability](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode#view-availability).

---
## 2025-12-19

### Feature

**Generally available**: The G4 accelerator-optimized machine series supports
the flex-start provisioning model. When you specify the flex-start provisioning
model for your G4 virtual machine (VM) instances, you receive a discount up to
50% for vCPUs, memory, and GPUs. Flex-start is ideal for fault-tolerant or
temporary workloads that can benefit from lower costs by having a flexible start
time. For more information, see
[About Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms).

### Feature

**Public Preview**: The C4A VM family now offers a `c4a-highmem-96-metal` bare
metal instance. This machine type has 96 vCPUs and 768 GB of DDR5 memory,
[Titanium I/O offload processing](https://cloud.google.com/titanium),
and supports Hyperdisk Balanced, Hyperdisk Extreme, and Hyperdisk ML storage volumes.
This bare metal instance is offered
in select [regions and zones](https://docs.cloud.google.com/compute/docs/bare-metal-instances#regions_zones).
For more information, see
[C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series).

---
## 2025-12-17

### Feature

**Generally available**: You can create future reservation requests in calendar
mode to reserve GPU, TPU, or H4D resources for your virtual machine (VM)
instances. Use these requests to obtain high-demand resources for creating VMs
that you plan to run for up to 90 days, such as when you want to run model
pre-training, model fine-tuning, or high performance computing (HPC) jobs. For
more information, see
[About future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

---
## 2025-12-16

### Feature

Sole-tenancy is now supported for the following GPU machine types:

* A2 Ultra, A2 Mega, and A2 High machine types.
  You can provision sole-tenant nodes using the following node types:
  + `a2-ultragpu-node-96-1360-lssd`
  + `a2-megagpu-node-96-1360`
  + `a2-highgpu-node-96-680`
* A3 Mega and A3 High machine types.
  You can provision sole-tenant nodes using the following node types:
  + `a3-megagpu-node-208-1872-lssd`
  + `a3-highgpu-node-208-1872-lssd`

For more information, see [Sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

---
## 2025-12-14

### Feature

Instance flexibility in regional managed instance
groups (MIGs) support the `ANY` target distribution shape. Selecting this shape
lets you maximize resource obtainability and the utilization of unused zonal
reservations. For more information, see
[About instance flexibility in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

---
## 2025-12-12

### Feature

The memory-optimized X4 machine series offers additional bare metal machine
types with 6 TB, 8 TB, and 12 TB of memory. For more information,
see [X4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_series).

### Issue

Workloads on A4 VMs might experience interruptions due to a firmware issue
for NVIDIA B200 GPUs. To help prevent the issue, we recommend resetting the GPUs
on A4 VMs at least once every 60 days. For more information, see the
[known issue](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/known-issues#a4-firmware).

---
## 2025-12-10

### Fixed

If you clone a source disk that's encrypted with a customer-supplied encryption
key or customer-managed encryption key, you must use the same key to encrypt the
clone.

For more information, see [Create a clone of an encrypted source disk](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks#encrypted-source).

### Feature

**Generally available**: The general purpose C4 machine series now supports the
following machine types on Intel's Xeon 6 processor (Granite Rapids):

* `c4-standard-288-lssd-metal`
* `c4-highmem-288-lssd-metal`

To learn more, see the [C4 machine series](https://cloud.google.com/compute/docs/general-purpose-machines#c4_series).

For more information, see
[Machine types that automatically attach Local SSD disks](https://cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed)
and
[Bare metal instances on Compute Engine](https://cloud.google.com/compute/docs/instances/bare-metal-instances).

---
## 2025-12-08

### Feature

**Preview**: VM Extension Manager lets you manage Compute Engine
guest agent extensions on your virtual machines (VMs). You can use VM Extension Manager to install and manage extensions, such as Ops Agent and Agent for SAP, on your
Compute Engine VMs at scale, without connecting to each VM.

Use VM Extension Manager to create policies that install extensions on
your VMs. You can install extensions based on a specific criteria, such as VM labels,
for both existing and new VMs that match the criteria. VM Extension Manager
automates the lifecycle of extensions across
your entire fleet of VMs and monitors their health status while they are running.

For more information, see the following:

* [About VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager)
* [Install VM extensions by creating extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy)
* [Manage VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions)

---
## 2025-11-26

### Issue

C4 machine type virtual machine (VM) instances running on sole tenant nodes
might encounter unexpected VM terminations due to host errors or VM
creation failures. For more information, see
[known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#c4-oom-errors).

---
## 2025-11-24

### Feature

**Public Preview**: You can now access the VM metadata server using IPv6 connectivity
from single-stack IPv6 VM instances. For more information, see
[About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).

---
## 2025-11-19

### Fixed

For the Windows operating system, gVNIC driver version 2.0.15 is
available.

This version fixes the handling for highly fragmented TSO packets. Without this
updated driver version, you might experience intermittent network
connectivity loss on Windows VMs that use any Compute Engine machine types.
The affected versions are 2.0.7 - 2.0.14.

Symptoms include ARP resolution failures and an inability to reach local
subnet IPs, including the metadata server. We recommend upgrading your Windows
instances to this latest version of the driver. To learn about upgrading, read
the [Windows components](https://docs.cloud.google.com/compute/docs/images/guest-environment#windows-components)
section of the Guest environment documentation.

---
## 2025-11-18

### Feature

**Preview**: The general purpose C4 machine series now supports the following
machine types on Intel's Xeon 6 processor (Granite Rapids):

* `c4-standard-288-lssd-metal`
* `c4-highmem-288-lssd-metal`

To learn more, see the [C4 machine series](https://cloud.google.com/compute/docs/general-purpose-machines#c4_series).

For more information, see
[Machine types that automatically attach Local SSD disks](https://cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed)
and
[Bare metal instances on Compute Engine](https://cloud.google.com/compute/docs/instances/bare-metal-instances).

### Feature

You can autoscale a regional managed instance group
(MIG) that has the target distribution shape set to `ANY` or `ANY_SINGLE_ZONE`.
These shapes are particularly beneficial for batch workloads.
For more information about target distribution shapes, see
[Regional MIG target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).

---
## 2025-11-13

### Feature

**Preview**: Future reservation requests in calendar mode support reserving
capacity for `a3-megagpu-8g` and `a3-highgpu-8g` machine types. Use future
reservation requests in calendar mode to obtain resources for running model
pre-training, model fine-tuning, simulation, and inference workloads. For more
information, see
[About future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

---
## 2025-11-10

### Issue

The Windows guest agent identifies administrator accounts and groups using
string matching. Therefore, credential management features only function
correctly when you use English language names for user accounts and groups,
for example, `Administrators`. If you use non-English language names, credential
management features such as generating or resetting passwords might not function
as expected. For more information about managing Windows user accounts, see
[Manage accounts and credentials on Windows VMs](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials) and
[Known issues for Windows VM instances](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-non-english-credentials).

### Feature

**Generally available**: Two new features that provide better observability for
Compute Engine reservations and deeper insights into their capacity usage and
costs:

* A new `consumedReservation` field in the VM instance details showing the
  full resource name of the consumed reservation, providing reservation
  consumption status on VMs and better visibility for resource management and
  troubleshooting.
* Two new system labels in the BigQuery billing export for instances
  consuming a reservation and the unused portion of a reservation, providing
  more detailed cost analysis:
  + `compute.googleapis.com/reservation_name`: the short name of the
    Compute Engine reservation.
  + `compute.googleapis.com/reservation_project_id`: the Project ID owning
    the Compute Engine reservation.

For more information, see the following:

* [View consumption history for a given instance](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#view_consumption_for_a_given_instance).
* [Analyze usage distribution per project for a shared reservation](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#analyze_usage_distribution_for_a_given_reservation).
* [List all the instances consuming a reservation](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#list_all_the_instances_consuming_a_reservation).

---
## 2025-11-07

### Feature

**Generally available**: N4D VMs are powered by the fifth generation AMD EPYC
Turin processor and
[Titanium I/O offload processing](https://cloud.google.com/titanium).
N4D machine types have up to 96 vCPUs and up to 768 GB of DDR5 memory,
and a max-boost frequency of 4.1 GHz. They are offered in predefined and
custom machine types and are available in select
[regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

N4D VM instances support standard networking with up to 50 Gbps of
networking bandwidth and Hyperdisk storage. For more information, see
[General-purpose machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series).

---
## 2025-11-06

### Feature

**Preview**: N4A VMs are powered by Google's next-generation Axion processor, which is built on the Arm Neoverse N3 platform. N4A includes machine types with up to 64 vCPUs and 512 GB of DDR5 memory. N4A is available as standard, high-mem, high-cpu, and custom machine types with extended memory and up to 50 Gbps of standard networking. These machine types are available in limited [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). For more information, see [N4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series).

To access these VMs, complete [this access request form](https://docs.google.com/forms/d/e/1FAIpQLSddzdVNnkbi5oKB3DURruA28S9MdxdKcvxwuheqojGHCldLRw/viewform), or speak to your account team.

---
## 2025-11-04

### Feature

**Generally available**: You can verify which reservation a VM consumes and
view a list of VMs that consume a reservation. For more information,
see [View reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view_reservation_consumption).

### Feature

**Public preview**: You can configure a regional managed instance group (MIG) to
repair a VM in an alternate zone when the MIG can't repair the VM in its
original zone. Repairing a VM in an alternate zone can improve your
application's resiliency and resource obtainability. For more information, see
[Repair a VM in an alternate zone](https://docs.cloud.google.com/compute/docs/instance-groups/repair-vm-in-alternate-zone).

---
## 2025-11-02

### Feature

If you need to synchronize time with high accuracy and monitor its accuracy for
your Compute Engine instances, you can sync your VM clock with its host
server clock using `chrony` and `ptp_kvm`. This configuration provides accuracy
within 1 ms for supported setups. For more information, see
[Configure accurate time for Compute Engine VMs](https://docs.cloud.google.com/compute/docs/instances/time-synchronization).

---
## 2025-10-31

### Fixed

Version `20251030.02` includes fixes for the plugin-based architecture that is used by guest agent. For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

* The Clock Skew module no longer causes time inconsistencies on VMs. The agent no longer attempts to synchronize the hardware clock (`hwclock`) when the VM's Real-time Clock (RTC) isn't set to Coordinated Universal Time 0(UTC). For more information about how the guest agent handles clock synchronization, see [Clock Synchronization](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#clock-synchronization).
* The `vlan_setup_enabled` option now correctly sets up Dynamic Network Interfaces (NICs). [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics) now initialize reliably.
* The agent now prevents a race condition in network interface and route setup. Previously, routes were temporarily flushed if they were added before a DHCP lease was acquired. The agent now ensures routes persist correctly, preventing a brief period of missing routes. These routes were previously auto-corrected after approximately one minute.

---
## 2025-10-30

### Feature

**Generally available**: Dynamic NICs let you add or remove network interfaces
to or from an instance without restarting or recreating the instance.

You can also use Dynamic NICs when you need more network interfaces. The
maximum number of vNICs for most machine types in Google Cloud is 10; however,
you can configure up to 16 total interfaces by using Dynamic NICs.

For more information, see the following:

* [Multiple network interfaces overview](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts)
* [Create VM instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)
* [Add Dynamic NICs to an instance](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics)

---
## 2025-10-28

### Feature

**Generally available**: You can create managed instance groups (MIGs) that consist
of IPv6-only VM instances.

For more information, see
[Basic scenarios for creating managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

---
## 2025-10-21

### Fixed

Version `20251009.01` of the guest agent, announced in the [October 20, 2025 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#October_20_2025), has been rolled back. This version introduced the plugin-based architecture to Windows but contained a bug in the [WSFC module](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#windows-failover).
To resolve this issue, guest agent version `20251011.00` is now available for Windows, which excludes the new plugin-based architecture.

### Changed

As part of the consolidation of CIQ's kernel trees, the kernel `dist-tag` that supports the Rocky Linux Optimized and Accelerator images on Compute Engine is changing from `elX_ycld_next` to `elX_y_ciq`. There are no changes to Secure Boot or GPG signing keys.

For example, `6.12.0-55.32.1.el10_0cld_next.2.1` changes to `6.12.0-55.39.1.el10_0_ciq.2.1`, where `ciq` replaces the `cld_next` tag.

This change affects the Rocky Linux 8, 9, and 10 optimized and accelerator images in an upcoming kernel update over the next month. The major version 8 and 9 kernels now include FIPS 140-3 patches as part of CIQ's ongoing FIPS 140-3 validation efforts for Rocky Linux. These patches have no effect if FIPS mode is not enabled. There are no code changes to the major version 10 kernel.

You can find the kernel source tree in the CIQ [kernel-src-tree](https://github.com/ctrliq/kernel-src-tree) GitHub repository.

### Feature

**Generally available**: Future reservations let you reserve capacity for a
specific date up to one year in advance. For more information, see
[About future reservation requests](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).

---
## 2025-10-20

### Feature

Version `20251009.01` of the guest agent, which introduces the plugin-based
architecture to Windows, is now available.

For more information about the plugin-based architecture, see
[Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

### Security

A vulnerability affecting AMD Zen 5 processors (Turin) is being addressed. For more information, see the
[GCP-2025-058 security bulletin](https://docs.cloud.google.com/compute/docs/security-bulletins#gcp-2025-058).

### Feature

**Generally Available**: The G4
[accelerator-optimized machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)
is designed for graphics-intensive workloads such as NVIDIA Omniverse simulations,
video transcoding, and virtual desktops. The G4 machine series also provides a
cost-effective solution for single-host inference and model tuning.
The G4 machine series is available in the following regions and zones:

* APAC
  + Jurong West, Singapore: `asia-southeast1-b`
* Europe
  + Eemshaven, Netherlands: `europe-west4-a`
* North America
  + Council Bluffs, Iowa: `us-central1-b`
  + Ashburn, Virginia: `us-east4-c`
  + Columbus, Ohio: `us-east5-c`

To get started with G4 machine types, see
[Create a G2 or G4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-g-series).

---
## 2025-10-18

### Feature

**Generally Available**: You can use the Compute Engine alpha API at the
project level through a self-service process. By enabling the alpha API, you can
use the Google Cloud console, Google Cloud CLI, API, and Terraform to view and manage
preview features. For more information, see [Use the Compute Engine alpha API](https://docs.cloud.google.com/compute/docs/reference/rest/alpha).

---
## 2025-10-17

### Feature

**Generally Available**: You can use the Compute Engine alpha API at the
project level through a self-service process. By enabling the alpha API, you can
use the Google Cloud console, Google Cloud CLI, API, and Terraform to view and manage
preview features. For more information, see [Use the Compute Engine alpha API](https://docs.cloud.google.com/compute/docs/reference/rest/alpha).

---
## 2025-10-16

### Changed

Starting with SUSE Linux Enterprise Server (SLES) 16, including variants for SAP, the default file system for the root partition (`/`) is [Btrfs](https://en.wikipedia.org/wiki/Btrfs), which replaces the previous default of XFS. For more information, see [File systems in SLES](https://documentation.suse.com/sles/15-SP7/html/SLES-all/cha-filesystems.html#sec-filesystems-major-btrfs-suse) in the SUSE documentation.

---
## 2025-10-06

### Changed

The Google Cloud optimized (`-optimized-gcp`) and accelerated
(`optimized-gcp-nvidia-*`) versions of the Rocky Linux images now include the
[CIQ SIG/Cloud Next repository](https://docs.ciq.com/rlc/ciq-sig-cloud-next/).
This repository provides a cloud-optimized kernel. Additionally, the accelerated
images now also include the [CIQ SIG/Cloud Next Nonfree
repository](https://gitlab.com/ctrl-iq-public/sig-cloud-next/next-nonfree),
which provides access to proprietary GPU drivers for the cloud-optimized kernel.

This update is applied to images created on or after September 12, 2025.

For more information about Rocky Linux OS images, see [Rocky
Linux](https://docs.cloud.google.com/compute/docs/images/os-details#rocky_linux) on
the operating system details page.

---
## 2025-10-02

### Feature

Version `20250930.01` of the guest agent, which introduces the plugin-based
architecture to Debian 11, is now available.

For more information about the plugin-based architecture, see
[Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

---
## 2025-09-30

### Fixed

Version `20250930.01` includes the following fixes for issues found in the
plugin-based architecture. For more information about the plugin-based
architecture, see [Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

* Fixes an issue where the networking module incorrectly added routes when
  `ip_forwarding` and `target_instance_ips` settings were disabled in `/etc/default/instance_configs.cfg`.
* Prevents unnecessary error logs in the OS Login module caused by attempts to
  read a non-existent file.

---
## 2025-09-26

### Feature

Version `20250926.00` of the guest agent is now available. This guest agent
version introduces the plugin-based architecture to Debian 12.

For more information about the plugin-based architecture, see
[Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

---
## 2025-09-22

### Feature

**Generally available**: You can create and use Flex-start VMs. Flex-start VMs are virtual machine (VM) instances that can run for up to seven days, and that use the flex-start provisioning model. This model provisions resources from a secure pool of capacity, increasing your chances of obtaining high-demand resources like GPUs. These features make Flex-start VMs suitable for short-duration workloads that can start at any time, such as the following:

* Small model pre-training
* Model fine-tuning
* High performance computing (HPC) simulation
* Batch inference

You can create standalone Flex-start VMs, or add Flex-start VMs all at once to a managed instance group (MIG) by using resize requests. Based on the machine type that your Flex-start VMs use, you get discounts for vCPUs, memory, and any attached GPUs.

For more information, see [About Flex-start VMs](https://cloud.google.com/compute/docs/instances/about-flex-start-vms).

---
## 2025-09-18

### Feature

Version `20250918.01` of the guest agent is now available. This guest agent
version introduces the plugin-based architecture to the following Debian and
Enterprise Linux 10 operating systems:

* Red Hat Enterprise Linux (RHEL) 10
* Rocky Linux 10
* CentOS Stream 10
* Debian 13

For more information about the plugin-based architecture, see
[Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

### Fixed

Version `20250918.01` includes the following fixes for issues found in
plugin-based architecture. For more information about the plugin-based
architecture, see [Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

* Corrects an issue in the OS Login module that was incorrectly writing `perm_denied=die`
  [PAM](https://en.wikipedia.org/wiki/Pluggable_Authentication_Module) module
  configuration when two-factor authentication isn't enabled.
* Fixes an issue in the metadata-based SSH module where re-adding a user didn't
  add the user to the sudoers group.

---
## 2025-09-17

### Changed

Compute Engine enforces limits to the total baseline performance that a project's Hyperdisk Balanced and Hyperdisk Balanced High Availability disks that are in the same zone can consume at the same time. The aggregate baseline performance limit is 50 GiB/s of throughput and 500,000 IOPS, and it only applies to baseline performance. For a detailed explanation, see [Concurrent consumption limits for baseline performance](https://cloud.google.com/compute/docs/disks/hyperdisk-performance#baseline_consumption_limits).

---
## 2025-09-15

### Feature

**Generally available**: You can decrease a Compute Engine instance shutdown time by skipping the guest OS shutdown. This action speeds up an instance stop or deletion operation to release resources and quota faster. However, as abrupt guest OS shutdowns may cause data loss or corrupt file system data, we recommend that you skip a guest OS shutdown only when you delete instances, or when you stop instances which boot disks you don't plan to reuse. For more information, see [Decrease Compute Engine instances shutdown time](https://cloud.google.com/compute/docs/instances/decrease-shutdown-time).

---
## 2025-09-12

### Feature

**Preview**: H4D VMs, designed for high performance computing (HPC) workloads, are now in preview. Based on 5th generation AMD EPYC Turin with Cloud RDMA 200 Gbps networking, H4D VMs offer 192 cores (SMT disabled), up to 1,488 GB of memory, and 3,750 GiB of Local SSD. H4D is optimized for tightly-coupled applications that scale across multiple nodes and offers RDMA-enabled 200 Gbps networking.

For more information, see [H4D machine series](https://cloud.google.com/compute/docs/compute-optimized-machines#h4d_series).

---
## 2025-09-10

### Feature

**Generally available**: The [accelerator-optimized A4X machine type](https://cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms), the first GPU VM to run on Arm, is available on Compute Engine. The A4X machine series has the NVIDIA GB200 Grace Blackwell Superchips attached and runs on the NVIDIA GB200 NVL72 platform. Use this machine type to run your large artificial intelligence (AI) models, machine learning (ML), and high performance computing (HPC) workloads. The A4X machine type is currently available in the `us-central1-a` zone.

---
## 2025-09-09

### Feature

Version `20250907.00` of the guest agent, which introduces the plugin-based
architecture to Enterprise Linux 8 operating systems, is now available. For more
information about the plugin-based architecture, see [Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

With this version, the plugin-based guest agent is now also available for the
following operating systems:

* Red Hat Enterprise Linux (RHEL) 8
* Rocky Linux 8
* CentOS Stream 8
* Oracle Linux 8
* AlmaLinux 8

### Fixed

Version `20250907.00` includes the following fixes for issues found in guest
agent version `20250901.00`:

* Corrects an issue in the OS Login module that was incorrectly handling
  optional runtime systemd dependencies and causing an error log.
* Fixes a bug that could cause the metadata SSH key module to enter an infinite
  loop when setting up SSH keys. This occurred if an initial setup attempt failed
  and the metadata server returned the SSH keys in a different order on a
  subsequent retry.

### Changed

Hyperdisk Balanced High Availability disks are available in all regions.
Hyperdisk Balanced High Availability disks synchronously replicate disk data from one zone to another. Cross-zonal replication provides data protection in the unlikely event of a zonal outage. For more information, see [About Hyperdisk Balanced High Availability](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha).

### Feature

**Preview:** Eight new organization policy constraints are available to help you
enforce security best practices for Compute Engine virtual machine (VM)
instances.

These [managed constraints](https://cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints)
simplify governance for common security scenarios and integrate with safe
rollout tools like
[dry-run](https://cloud.google.com/resource-manager/docs/organization-policy/dry-run-policy)
and
[simulation](https://cloud.google.com/policy-intelligence/docs/test-organization-policies),
letting you test their impact before enforcement.

The new constraints are as follows:

* `compute.managed.disableNestedVirtualization`
* `compute.managed.disableSerialPortAccess`
* `compute.managed.disableSerialPortLogging`
* `compute.managed.disallowGlobalDns`
* `compute.managed.requireOsConfig`
* `compute.managed.requireOsLogin`
* `compute.managed.vmCanIpForward`
* `compute.managed.vmExternalIpAccess`

These constraints can evaluate metadata values at the [VM instance, project, or
zonal level](https://cloud.google.com/compute/docs/metadata/overview#metadata-directories). For more information about these managed constraints, see [Managed
Constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#managed-constraints) in the Resource Manager documentation.

---
## 2025-09-04

### Feature

Hyperdisk Balanced High Availability (Hyperdisk Balanced HA) volumes attached to C3 instances have increased performance limits for several C3 machine types. The new limits for the updated machine types are as follows:

* `c3-*-8`: 50,000 IOPS and 800 MiB/s of throughput
* `c3-*-22`: 120,000 IOPS and 1,800 MiB/s of throughput
* `c3-*-44`: 160,000 IOPS and 2,400 MiB/s of throughput
* `c3-*-88`: 160,000 IOPS and 4,800 MiB/s of throughput
* `c3-*-176`: 160,000 IOPS and 10,000 MiB/s of throughput
* `c3-*-192`: 160,000 IOPS and 10,000 MiB/s of throughput

For more information, see [Performance limits when attached to an instance](https://cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#perf-limits).

### Feature

**Generally available**: [Windows OS images](https://cloud.google.com/compute/docs/images/os-details#network-features) have been updated with a new version of the gVNIC driver. Third generation and later compute instances that use these updated Windows OS images support up to [200 Gbps networking bandwidth](https://cloud.google.com/compute/docs/network-bandwidth#summary-table) and [Jumbo frames](https://cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).

---
## 2025-08-28

### Feature

**Generally available:** [M4 memory-optimized hypermem VMs](https://cloud.google.com/compute/docs/memory-optimized-machines#m4_series) are now generally available. These smaller machine types expand the memory-optimized family to allow for greater flexibility in matching your specific application needs. Hypermem VMs have a GB/vCPU ratio of 15.5:1 and are offered in the following sizes:

* m4-hypermem-16
* m4-hypermem-32
* m4-hypermem-64

See the [Regions and zones](https://cloud.google.com/compute/docs/regions-zones) page to learn where you can create M4 VMs.

---
## 2025-08-26

### Feature

**Generally available**: You can create instances that use only IPv6 IP addresses. For more information, see [Create an IPv6-only instance](https://cloud.google.com/compute/docs/instances/create-ipv6-instance#create-vm-ipv6-only).

---
## 2025-08-20

### Feature

You can use instant snapshots to back up Extreme Persistent Disk volumes. For more information, see [About instant snapshots](https://cloud.google.com/compute/docs/disks/instant-snapshots).

---
## 2025-08-14

### Feature

**Public Preview**: You can now access the Compute Engine alpha API at the project level through a self-service process. By enabling the alpha API, you can use the Google Cloud console, gcloud CLI, API, and Terraform to view and manage Preview features. For more information, see [Use the Compute Engine alpha API](https://cloud.google.com/compute/docs/reference/rest/alpha).

---
## 2025-08-13

### Feature

**Generally available:** License Manager is now generally available. License Manager lets you subscribe, manage, and track your third-party license usage on Google Cloud. As an administrator, you can use License Manager to offer per-user licensing products, like Microsoft Office, to your users with no long-term commitments and no overhead of managing compliance.

For more information, see [About License Manager](https://cloud.google.com/compute/docs/instances/windows/license-manager).

---
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
