# Backup and DR

## 2025-10-30

### Feature

Announcing the **Public Preview** launch of AlloyDB for PostgreSQL enhanced backups with Backup and DR Service. This enables advanced data protection capabilities offered by Backup and DR Service including backup vault support, granular scheduling through backup plans, and centralized management.

### Feature

A new backup vault setting, **Prevent deletion for duration specified in backup rule**, is now available. When enabled, this feature locks backups for the exact retention period defined in the associated backup plan, overriding the vault's local minimum retention and preventing manual deletion.

---
## 2025-10-21

### Fixed

* Resolved a problem with timestamp conversions during recovery range calculations in SAP HANA
* Fixed a bug that prevented the identification of persistent disk names in some SAP HANA environments
* Fixed DB2 restore issue wrt pre-flight checks and instances with a large number of archive logs
* Fixed a logging issue during Postgres upgrades where an incorrect version was displayed after a rollback
* Resolved a restore failure when using a combination of full and incremental backups for SAP ASE
* Fixed a connection leak and an issue with executor service shutdown in the VMware hypervisor integration, improving reliability.

### Feature

* Change Block Tracking (CBT) support has been added for latest kernel versions in RHEL 8.10, 9.2, 9.4 and 9.6.
* Improved alerting for long-running jobs by adding application type and name to the alerts.

### Security

The following CVEs have been addressed in this release: CVE-2022-1471, CVE-2025-31651, CVE-2025-31650, CVE-2022-42003, CVE-2025-25193, CVE-2024-6763, CVE-2025-52999, CVE-2025-24970, CVE-2025-49125, CVE-2025-48734, CVE-2024-52317, CVE-2025-48988, CVE-2025-46701

---
## 2025-10-15

### Announcement

Backup and DR Service 11.0.16.253 is now available to update your backup/recovery appliances. Refer to these [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

* Guardrails have been defined for each backup/recovery appliance to specify the number of supported job slots, ensuring smooth parallel backup and mount jobs.

Introducing notifications and alerts for the following critical events:

* Processes not running on a backup/recovery appliance
* Expired certificates
* No jobs running on a backup/recovery appliance
* CPU and memory usage exceeding threshold values
* Backup/recovery appliance appliance version out of support
* Backup/recovery appliance updates available

You can subscribe to these events and configure email alerts.

---
## 2025-10-14

### Feature

You can now set up backup vault specific workload quotas for critical resources like data sources, backups, backup plans, and backup plan associations. Until now these quotas were set up only at the project level, not at the workload level.

---
## 2025-08-12

### Announcement

Announcing the General Availability (GA) of Backup Vault support for independent Persistent Disks and Hyperdisks!

This new capability empowers you to protect application data, databases, and file shares stored on individual disks (where a full VM backup is not required) — all within a secure, immutable, logically air-gapped vault designed to withstand malicious deletion and advanced threats like ransomware.

---
## 2025-07-31

### Announcement

Announcing the **Public Preview launch of Cloud SQL enhanced backups** with Backup and DR. This enables advanced data protection capabilities offered by Backup and DR including backup vault support, granular scheduling through backup plans, and centralized management.

---
## 2025-07-11

### Announcement

We're excited to announce the launch of Editable Backup Plans, a new feature designed to give you more flexibility and control over your data protection strategy. You can now modify your existing backup plans directly, eliminating the need to create new plans and reassign them when your requirements change. This makes it easier than ever to adapt to evolving business needs, optimize for cost, and correct configuration errors on the fly.

What's new:

* Directly Edit Key Settings: You can now change the description, schedule, backup window, and retention periods of your existing backup plans. You can also add or remove backup rules as needed.
* Automatic Updates: Once a plan is edited, the changes are automatically applied to all resources protected by that plan for all future backups. There's no need to manually detach and reattach the plan.
* Backward Compatibility: This new capability is available for all backup plans, including those created before this update.

Important Note: While most settings in a backup plan are now editable, the assigned backup vault cannot be changed. To store backups in a different vault, a new backup plan must be created.

---
