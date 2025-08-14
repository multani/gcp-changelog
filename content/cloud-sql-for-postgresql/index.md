# Cloud SQL for PostgreSQL

## 2025-08-13

### Feature

Cloud SQL now supports Private Service Connect (PSC) outbound connectivity. With PSC outbound connectivity, you can attach a PSC interface to your existing Cloud SQL PSC-enabled instances to allow your instances to make outbound connections to your network. This is required for [homogeneous migrations using Database Migration Service](https://cloud.google.com/database-migration/docs/homogeneous-migrations). For more information, see [PSC outbound connections](https://cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound).

---
## 2025-08-07

### Changed

Cloud SQL for Enterprise Plus edition supports quality enhancements for [AI-assisted troubleshooting](https://cloud.google.com/sql/docs/postgres/observe-troubleshoot-with-ai). With AI-assisted troubleshooting, you can resolve complex database performance issues like [slow queries](https://cloud.google.com/sql/docs/postgres/troubleshoot-slow-queries) and [high load](https://cloud.google.com/sql/docs/postgres/troubleshoot-high-database-load) for your instances in a guided manner. To use AI-assisted troubleshooting, you need [Gemini Cloud Assist](https://cloud.google.com/gemini/docs/cloud-assist/overview) and [query insights](https://cloud.google.com/sql/docs/postgres/using-query-insights#enable-insights) for Enterprise Plus edition.

---
## 2025-08-04

### Issue

PostgreSQL has identified a [bug](https://www.postgresql.org/message-id/flat/680bdaf6-f7d1-4536-b580-05c2760c67c6%40deepbluecap.com) in [PostgreSQL's May 8, 2025 release](https://www.postgresql.org/about/news/postgresql-175-169-1513-1418-and-1321-released-3072/) that is causing logical replication to halt. Cloud SQL for PostgreSQL released `[PostgreSQL version].R20250302.00_19` on [May 22, 2025](https://cloud.google.com/sql/docs/postgres/release-notes#May_22_2025), which is impacted by this bug.

If you use logical replication with your Cloud SQL for PostgreSQL instances, then we recommend that you don't update your instances to this version or any self-service maintenance version released after May 22, 2025, due to this PostgreSQL bug. We also recommend not performing a [major version upgrade](https://cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace) on your instances, since it adopts the latest self-service maintenance version.

We expect a fix for this issue in the next automatically-scheduled maintenance. For more information about this bug, see [Logical replication 'invalid memory alloc request size 1585837200' after upgrading to 17.5](https://www.postgresql.org/message-id/flat/680bdaf6-f7d1-4536-b580-05c2760c67c6%40deepbluecap.com).

---
## 2025-07-31

### Feature

Cloud SQL now offers two options of backup services to manage your instance's backups:

* **Enhanced backups** ([Preview](https://cloud.google.com/products?#product-launch-stages)): backups are managed and stored in a centralized backup management project that leverages the [Backup and DR service](https://cloud.google.com/backup-disaster-recovery), and provides enforced retention, granular scheduling, and longer retention.
* **Standard backups** (existing option): backups are created, managed, and stored in the same project as your Cloud SQL instances.

You can choose between these options based on your instance's requirements and needs. Although instances can't use both backup options at the same time, Cloud SQL gives you the ability to switch between these backup options as necessary.

For more information about the available options and their limitations, see [Backup options](https://cloud.google.com/sql/docs/postgres/backup-recovery/backups#backup-options).

---
## 2025-07-02

### Feature

The write endpoint feature for Cloud SQL Enterprise Plus edition instances is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This endpoint is a global domain name service (DNS) name and resolves to the IP address of the current primary Cloud SQL instance that's enabled with private services access.

By using a write endpoint, you can avoid having to make application connection changes after performing a switchover or replica failover operation to test or mitigate a region failure.

For more information, see [Connect to an instance using a write endpoint](https://cloud.google.com/sql/docs/postgres/connect-to-instance-using-write-endpoint).

---
## 2025-07-01

### Feature

The write endpoint feature for Cloud SQL Enterprise Plus edition instances is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This endpoint is a global domain name service (DNS) name and resolves to the IP address of the current primary Cloud SQL instance that's enabled with private services access.

By using a write endpoint, you can avoid having to make application connection changes after performing a switchover or replica failover operation to test or mitigate a regional failure.

For more information, see [Connect to an instance using a write endpoint](https://cloud.google.com/sql/docs/postgres/connect-to-instance-using-write-endpoint).

---
