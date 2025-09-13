# Cloud SQL for PostgreSQL

## 2025-09-12

### Feature

If a specific active query is blocked or running much longer than expected, it can block other dependent queries. Cloud SQL for PostgreSQL offers an optional feature that lets you terminate specific long-running or blocked active queries.

For more information, see [Blocked active queries (Preview)](https://cloud.google.com/sql/docs/postgres/monitor-active-queries#blocked-active-queries).

---
## 2025-09-09

### Feature

The rollout of the following extension versions is complete:

**Extensions and plugins**

* `pg_ivm` is upgraded from 1.9 to 1.11.
* `pg_background` is upgraded from 1.2 to 1.3.
* `google_ml_integration` is upgraded from 1.4.2 to 1.4.3.

To use these versions of the extensions, update your instance to [`PostgreSQL version].R20250727.00_14`.
If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](https://cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://cloud.google.com/sql/docs/postgres/set-maintenance-window).

---
## 2025-09-08

### Feature

Cloud SQL read pools are now generally available and provide operational simplicity and scaling for your read workloads.

Read pools provide a single endpoint in front of up to 20 read pool nodes and automatically load balance traffic.

You can scale your read pool in several ways:

* **Scale in or out**: scale load balancing capacity horizontally by modifying the number of read pool nodes in the read pool. Each read pool supports up to 20 read pool nodes.
* **Scale up or down**: scale load balancing capacity vertically by modifying the machine type associated with a read pool node. Once defined, configuration is uniformly applied across each read pool node in the read pool.

For more information, see
[About read pools](https://cloud.google.com/sql/docs/postgres/about-read-pools).

### Feature

You can have Cloud SQL create a [Private Service Connect](https://cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint) endpoint automatically. You can use this endpoint to access Cloud SQL instances through a VPC network. For more information, see [Create a Private Service Connect endpoint automatically](https://cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-endpoint-automatically).

This feature is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-09-04

### Changed

The release note on [August 13, 2025](https://cloud.google.com/sql/docs/postgres/release-notes#August_13_2025) regarding Private Service Connect (PSC) outbound connectivity has been updated.

PSC outbound connectivity is required for [homogeneous migrations](https://cloud.google.com/database-migration/docs/homogeneous-migrations) to PSC-enabled Cloud SQL instances using [Database Migration Service](https://cloud.google.com/database-migration/docs). For more information, see [PSC outbound connections](https://cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound).

---
## 2025-09-03

### Feature

You can now enable your instance to take a final backup at instance deletion and define its retention period by setting the final backup [instance setting](https://cloud.google.com/sql/docs/postgres/instance-settings).

You can also create a [custom organization policy](https://cloud.google.com/sql/docs/postgres/org-policy/custom-org-policy) to define final backup instance settings.
For more information, see [Final backup](https://cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backup).

---
## 2025-08-21

### Feature

You can save and manage SQL queries in Cloud SQL Studio. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Saved queries overview](https://cloud.google.com/sql/docs/postgres/saved-queries).

---
## 2025-08-15

### Feature

Now you can use [Private Service Connect backends](https://cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-backend), as an alternative to Private Service Connect endpoints, to access Cloud SQL instances.

### Feature

Now you can create an IPv6 endpoint for Private Service Connect (PSC) connections. For more information, see [Connect to an instance using Private Service Connect](https://cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-psc-endpoint).

### Deprecated

You can no longer set a deny maintenance period for instances that are running a maintenance version older than 12 months. To update your instance, [perform self-service maintenance](https://cloud.google.com/sql/docs/postgres/self-service-maintenance) or wait until the [next maintenance window](https://cloud.google.com/sql/docs/postgres/set-maintenance-window#find-maintenance-api) to update your instance automatically. For more information about maintenance, see [Maintenance updates on Cloud SQL instances](https://cloud.google.com/sql/docs/postgres/maintenance).

---
## 2025-08-13

### Feature

Cloud SQL now supports Private Service Connect (PSC) outbound connectivity. With PSC outbound connectivity, you can attach a PSC interface to your existing Cloud SQL PSC-enabled instances to allow your instances to make outbound connections to your network. This is required for [homogeneous migrations](https://cloud.google.com/database-migration/docs/homogeneous-migrations) to PSC-enabled Cloud SQL instances using [Database Migration Service](https://cloud.google.com/database-migration/docs). For more information, see [PSC outbound connections](https://cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound).

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
