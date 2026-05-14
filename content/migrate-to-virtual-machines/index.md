# Migrate to Virtual Machines

## 2026-04-22

### Feature

Migrate to Virtual Machines now lets you use regional disks for the target
virtual machine (VM) instance.

---
## 2026-04-20

### Feature

Migrate to Virtual Machines now supports the following operating systems for
VMware, AWS, Azure, and image import sources:

* Red Hat Enterprise Linux 10
* CentOS 10
* AlmaLinux 10
* Oracle Linux 10
* Rocky Linux 10

CentOS is not supported on ARM architecture.

---
## 2025-11-17

### Feature

You can now use [Hyperdisk Storage Pools](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#configure-target)
with migrating VMs if you need large-scale storage. Hyperdisk Storage Pools
help you manage large-scale storage and can optimize costs and performance.

---
## 2025-10-16

### Feature

Migrate to Virtual Machines now supports all available versions of AlmaLinux
EL 8 and 9.

---
## 2025-08-25

### Feature

**Generally available:** The Basic Input/Output System (BIOS) to Unified Extensible Firmware Interface (UEFI) conversion option is now generally available. Migrate to Virtual Machines lets you convert the OS boot type of a VM instance from BIOS to UEFI. This option is useful when you want to securely boot your VM instance, as secure boot is only supported by UEFI. For more information, see the table in [Configure the target for a migrated VM](https://cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#configure-target).

---
## 2025-06-20

### Feature

Starting with version Migrate Connector 2.7, throttling is supported for a second NIC.

---
