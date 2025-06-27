# Compute Engine

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

## 2025-06-11

### Feature

**Preview**: The storage-optimized Z3 machine series offers a bare metal (`-metal`) machine type with 192 vCPUs. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. To learn more, see [Z3 machine series](https://cloud.google.com/compute/docs/storage-optimized-machines#z3_series). For information about bare metal instances, including regional availability, see [Bare metal instances on Compute Engine](https://cloud.google.com/compute/docs/instances/bare-metal-instances).

## 2025-06-10

### Security

A vulnerability (CVE-2025-2884) affecting Shielded VMs using virtual Trusted Platform Module (vTPM) was discovered and is being addressed. For more information, see the [GCP-2025-031 security bulletin](https://cloud.google.com/compute/docs/security-bulletins#gcp-2025-031).

## 2025-06-06

### Changed

**Generally available**: The [Security Risk Overview dashboard for Compute Engine](https://cloud.google.com/compute/docs/monitor-security-risks-console) is generally available. In addition, it provides a **Top CVE findings** table that lists the most severe CVEs that affect your Compute Engine instances.

## 2025-06-04

### Feature

**Preview**: OS Login now supports connections from SSH certificates in addition to SSH keys. For more information, see [Set up OS Login to require SSH certificates for SSH connections](https://cloud.google.com/compute/docs/oslogin/certificates).

## 2025-06-03

### Feature

**Preview**: You can enable your project to send HTTP requests to a Compute Engine feature alpha URI. This action lets you test and develop with experimental features in the alpha stage using REST. For more information, see [Use the Compute Engine API in alpha](https://cloud.google.com/compute/docs/reference/rest/alpha).

## 2025-06-02

### Feature

**Preview**: The general-purpose C4D machine series offers bare metal (`-metal`) machine types with 384 vCPUs. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. To learn more, see [C4D machine series](https://cloud.google.com/compute/docs/general-purpose-machines#c4d_series). For information about bare metal instances, including regional availability, see [Bare metal instances on Compute Engine](https://cloud.google.com/compute/docs/instances/bare-metal-instances).

