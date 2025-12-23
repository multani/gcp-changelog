# Backup and DR

## 2025-12-22

### Feature

Enhanced performance for restore and clone of VMware VMs.

Expanded Linux CBT support for new kernels on RHEL 8 and 9.

### Security

Addressed multiple OpenSSH vulnerabilities, including CVE-2025-26465 and CVE-2025-26466.

### Fixed

Resolved issues with DB2 migration scripts and various SAP HANA backup failures, including differential and log backups.

Improved system stability and diagnostics by enhancing logging, adding log rotation, and correcting unit reporting in dashboards.

Corrected the data copy reporting for Persistent Disk (PD) based backups, ensuring it accurately reflects zero data copied.

---
## 2025-12-17

### Feature

Backup Vault: CMEK support for Compute Engine (GA) Backup Vault now supports
data protection for Compute Engine instances and Persistent Disks encrypted with
Customer-Managed Encryption Keys (CMEK). This capability is currently available
via Allow-list General Availability; please contact your Google Cloud sales
representative to request access.

---
## 2025-12-16

### Feature

Cloud SQL enhanced backups are now generally available (GA).
With enhanced backups, backups are managed and stored in a centralized backup
management project that leverages
[Backup and DR service](https://cloud.google.com/backup-disaster-recovery)
to provide enforced retention, granular scheduling, and longer retention.
Enhanced backups now also support
[point-in-time-recovery (PITR) after instance deletion](https://cloud.google.com/sql/docs/mysql/backup-recovery/restore).

For more information about the available options and their limitations, see
[Backup options](https://cloud.google.com/sql/docs/mysql/backup-recovery/backups#backup-options).

For more information about enhanced backups pricing, see [Backup and DR pricing](https://cloud.google.com/backup-disaster-recovery/pricing).

---
## 2025-11-19

### Feature

Added Change Block Tracking (CBT) support for RHEL 8.8 SAP kernels.

### Fixed

* Resolved an issue with SAP HANA datafile validation on scale-out clusters.
* Fixed a bug causing SAP HANA log backups to fail when the log mode is not 'normal'.
* Addressed failures in Db2 dump full backups in some environments.
* Corrected an issue where Db2 restore jobs with the roll-forward option were not applying logs completely.

### Security

Resolved a decryption failure that occurred when accessing KMS keys.

---
## 2025-11-07

### Feature

Announcing the public preview launch of Database Center support for
resources protected with Backup and DR Service. Database Center is an
AI-assisted dashboard that highlights fleet-wide data points.The integration is
designed to provide Database Center users with a single, unified, and
accurate view of the data protection posture for all databases protected by
Backup and DR Service.This capability is available today, at no additional cost,
for all Cloud SQL customers who have protected their databases through
Backup and DR Service enhanced protection.

---
## 2025-10-30

### Feature

A new backup vault setting, **Prevent deletion for duration specified in backup rule**,
is now available. When enabled, this feature locks backups for the exact retention
period defined in the associated backup plan, overriding the vault's local minimum
retention and preventing manual deletion.

### Feature

Announcing the **Public Preview** launch of AlloyDB for PostgreSQL enhanced backups with Backup and DR Service. This enables advanced data protection capabilities offered by Backup and DR Service including backup vault support, granular scheduling through backup plans, and centralized management.

---
## 2025-10-21

### Feature

* Change Block Tracking (CBT) support has been added for latest kernel versions in RHEL 8.10, 9.2, 9.4 and 9.6.
* Improved alerting for long-running jobs by adding application type and name to the alerts.

### Security

The following CVEs have been addressed in this release: CVE-2022-1471, CVE-2025-31651, CVE-2025-31650, CVE-2022-42003, CVE-2025-25193, CVE-2024-6763, CVE-2025-52999, CVE-2025-24970, CVE-2025-49125, CVE-2025-48734, CVE-2024-52317, CVE-2025-48988, CVE-2025-46701

### Fixed

* Resolved a problem with timestamp conversions during recovery range calculations in SAP HANA
* Fixed a bug that prevented the identification of persistent disk names in some SAP HANA environments
* Fixed DB2 restore issue wrt pre-flight checks and instances with a large number of archive logs
* Fixed a logging issue during Postgres upgrades where an incorrect version was displayed after a rollback
* Resolved a restore failure when using a combination of full and incremental backups for SAP ASE
* Fixed a connection leak and an issue with executor service shutdown in the VMware hypervisor integration, improving reliability.

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
