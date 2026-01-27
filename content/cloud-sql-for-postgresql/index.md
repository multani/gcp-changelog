# Cloud SQL for PostgreSQL

## 2026-01-26

### Feature

You can now assign database roles to built-in database users and IAM database
users when you create or update users. For more information about assigning
roles, see [built-in database authentication](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating)
or [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#add-db-roles).

---
## 2026-01-15

### Feature

Cloud SQL for PostgreSQL now supports fast clone operations within the same zone ([GA](https://cloud.google.com/products#product-launch-stages)).

For more information, see [Clone an instance](https://docs.cloud.google.com/sql/docs/postgres/clone-instance).

---
## 2025-12-17

### Feature

You can build data agents that interact with the data in your
database using conversational language. Use these data agents as tools to
empower your applications. For more information, see [Data agents overview](https://docs.cloud.google.com/sql/docs/postgres/data-agent-overview). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages), and access to it requires a [sign-up](https://forms.gle/pJByTWfenZAWbaXo7).

---
## 2025-12-16

### Feature

Cloud SQL enhanced backups are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

With enhanced backups, backups are managed and stored in a centralized
backup management project that leverages the
[Backup and DR service](https://docs.cloud.google.com/backup-disaster-recovery), and
provides enforced retention, granular scheduling, and longer retention.

Enhanced backups now also support
[point-in-time-recovery (PITR) after instance deletion](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore).

For more information about the available options and their limitations, see
[Backup options](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backup-options).
For more information about enhanced backups pricing, see
[Backup and DR pricing](https://cloud.google.com/backup-disaster-recovery/pricing).

---
## 2025-11-20

### Feature

PostgreSQL version 18 is now
[generally available](https://cloud.google.com/products#product-launch-stages)
for Cloud SQL for PostgreSQL.

You can now use [Database Migration Service](https://docs.cloud.google.com/database-migration/docs)
with Cloud SQL for PostgreSQL when using PostgreSQL version 18.

To upgrade your instance to PostgreSQL 18, see
[Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace).

The following extensions are also now available for PostgreSQL 18:

* `pg_hint_plan`
* `pgrouting`
* `anonymizer`
* `pg_wait_sampling`
* `tds_fdw`
* `plpgsql_check`

For more information about these extensions, see
[Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

---
## 2025-11-19

### Feature

The rollout of the following minor version and extension upgrades is complete:

**Minor versions**

* 13.22 is upgraded to 13.23.
* 14.19 is upgraded to 14.20.
* 15.14 is upgraded to 15.15.
* 16.10 is upgraded to 16.11.
* 17.6 is upgraded to 17.7.
* 18 is upgraded to 18.1.

**Extensions**

* `Pgvector` is upgraded from 0.8.0 to 0.8.1.

To use these versions of the extensions and plugins, update your instance to
`[PostgreSQL version].R20251004.01_19`.

If you use a maintenance window, then the updates to the minor, extension, and
plugin versions happen according to the timeframe that you set in the window.
Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see
[Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance).
To find your maintenance window or to manage maintenance updates, see
[Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

### Feature

Cloud SQL for PostgreSQL now supports Vector assist ([Preview](https://cloud.google.com/products#product-launch-stages)).

Vector assist is a Cloud SQL for PostgreSQL extension that simplifies the
deployment and management of your Cloud SQL vector workloads. It helps you set
up production-ready vector search capabilities, such as embedding generation,
query optimization, and index creation.

For more information about vector assist, how it works, and its limitations,
see [Vector assist overview](https://docs.cloud.google.com/sql/docs/postgres/vector-assist-overview).

---
## 2025-11-17

### Feature

Cloud SQL now offers a free trial instance for both existing and new Google
Cloud customers. A free trial instance lets you test advanced Cloud SQL
capabilities and features for up to 30 days without any financial commitment.

For information about a free trial instance, and its inclusions and conditions,
see [Free trial instance overview](https://cloud.google.com/sql/docs/postgres/free-trial-instance).

---
## 2025-11-14

### Feature

Cloud SQL for PostgreSQL now supports [read pool autoscaling](https://docs.cloud.google.com/sql/docs/postgres/read-pool-autoscaling)
[(GA)](https://cloud.google.com/products#product-launch-stages), which helps you
more easily manage your application's workload needs.

This feature automates read pool scale in and scale out operations based on one
or both of the following conditions:

* Allowed CPU usage of the read pool
* Allowed number of client connections to the read pool

---
## 2025-11-05

### Feature

The rollout of the following extension versions, plugin versions, and
extension support is underway:

**Extensions and plugins**

* `plpgsql_check` is upgraded from 2.8.1 to 2.8.3 for PostgreSQL versions
  14 and later.
* `pg_wait_sampling` is upgraded from 1.1.6 to 1.1.9 for PostgreSQL versions
  13 and later.
* `tds_fdw` is upgraded from 2.0.4 to 2.0.5.

The following extensions are available for PostgreSQL 18:

* `anon`
* `pg_hint_plan`
* `pg_wait_sampling`
* `plpgsql_check`
* `tds_fdw`

To use these versions of the extensions and plugins, update your instance to
`[PostgreSQL version].R20251004.01_14`.

If you use a maintenance window, then the updates to the minor, extension, and
plugin versions happen according to the timeframe that you set in the window.
Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see
[Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find
your maintenance window or to manage maintenance updates, see
[Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

---
## 2025-10-27

### Feature

The rollout of the following extension versions and plugin versions is underway:

**Extensions and plugins**

* `pg_squeeze` is upgraded from 1.8 to 1.9 for PostgreSQL version
  13 and later.
* `pg_cron` is upgraded from 1.6.4 to 1.6.7 for PostgreSQL version
  10 and later.
* `postgis` is upgraded from 3.5.2 to 3.6.0 for PostgreSQL version
  13 and later.
* `rdkit` is upgraded from 4.6.1 to 4.7.0.

To use these versions of the extensions and plugins, update your instance to
`[PostgreSQL version].R20251004.01_07`.

If you use a maintenance window, then the updates to the minor, extension, and
plugin versions happen according to the timeframe that you set in the window.
Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see
[Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find
your maintenance window or to manage maintenance updates, see
[Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

---
## 2025-10-23

### Feature

Cloud SQL now proactively detects and works to cancel high memory usage
connections to prevent out-of-memory (OOM) failures. For more information,
see [Cancelled queries due to high memory usage](https://cloud.google.com/sql/docs/postgres/manage-memory-usage-best-practices#cancelled-query).

---
## 2025-10-17

### Feature

Cloud SQL Enterprise edition now supports a new machine series called the N4 machine series. This machine series provides balanced price-to-performance and uses the Hyperdisk Balanced storage. You can create custom machine types for the N4 machine series with up to 80 vCPUs and up to 640 GB memory. The N4 machine series is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

For more information about the N4 machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview).

### Feature

The [C4A machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview#c4a) is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

The C4A machine series is supported for Cloud SQL Enterprise Plus edition instances, and provides optimized price-performance and delivers predictable high performance for high demand Cloud SQL workloads. It uses the Hyperdisk Balanced storage.

For more information about the C4A machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview).

---
## 2025-10-06

### Feature

You can now assess the upgrade readiness of your Cloud SQL for PostgreSQL instances before a major version upgrade by running a precheck. This precheck either confirms your instance can be upgraded, or lists issues and their solutions that need to be fixed prior to upgrading. For more information, see [Assess upgrade readiness for your instance](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace#precheck).

---
## 2025-10-03

### Feature

Cloud SQL for PostgreSQL now supports PostgreSQL version 18 in [Preview](https://cloud.google.com/products#product-launch-stages).

PostgreSQL 18 is a newly supported version. We strongly recommend that you review the changes in the release and validate the readiness of your instance thoroughly prior to upgrading your instance to this version.

The following information applies to flags and extensions for PostgreSQL 18:

**Flags**

The following new flags are available for PostgreSQL 18 only:

* `autovacuum_vacuum_max_threshold`
* `autovacuum_worker_slots`
* `enable_distinct_reordering`
* `enable_self_join_elimitation`
* `io_max_concurrency`
* `io_method`
* `io_workers`
* `log_lock_failures`
* `max_active_replecation_origins`
* `track_cost_delay_timing`
* `vacuum_max_eager_freeze_failure_rate`
* `vacuum_truncate`

For more information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

**Extensions**

The following extensions aren't available for PostgreSQL 18:

* `pgRouting`
* `plpgsql_check`
* `pg_hint_plan`
* `pgrouting`
* `anonymizer`
* `pg_wait_sampling`
* `tds_fdw`

For more information, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

To create a new instance using PostgreSQL 18, see [Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

---
## 2025-09-29

### Feature

You can now [use Gemini's capabilities to fix errors in a query within Cloud SQL Studio](https://cloud.google.com/sql/docs/postgres/write-sql-gemini#fix-query) ([Preview](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-09-25

### Feature

Cloud SQL Managed Connection Pooling is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Managed Connection Pooling lets you scale your workloads by optimizing resource utilization for Cloud SQL instances using pooling. You can now also use [IAM authentication](https://cloud.google.com/sql/docs/postgres/iam-authentication) to secure connections when using Managed Connection Pooling.

For more information, see [Managed Connection Pooling overview](https://cloud.google.com/sql/docs/postgres/managed-connection-pooling).

---
## 2025-09-23

### Feature

You can now provision, manage and query your databases using the dedicated Gemini CLI extension for Cloud SQL for PostgreSQL. The extension provides full lifecycle control of your database—from provisioning instances, to exploring schemas and troubleshooting issues—from your command-line interface.

For more information, see [Use Cloud SQL for PostgreSQL with MCP, Gemini CLI, and other agents](https://cloud.google.com/sql/docs/postgres/pre-built-tools-with-mcp-toolbox).

### Feature

You can now retain point-in-time recovery (PITR) logs for an instance after its deletion for a specified retention period. These logs can be used to restore the deleted instance to a specific point in time. For more information, see [Restore a deleted instance using PITR](https://cloud.google.com/sql/docs/postgres/backup-recovery/restore#deleted-instance).

---
## 2025-09-17

### Feature

The rollout of the following minor version upgrades is complete:

**Minor versions**

* 13.21 is upgraded to 13.22.
* 14.18 is upgraded to 14.19.
* 15.13 is upgraded to 15.14.
* 16.9 is upgraded to 16.10.
* 17.5 is upgraded to 17.6.

Cloud SQL for PostgreSQL adds support for the following extensions:

**Extensions**

* `plpgsql_check 2.8` is available for PostgreSQL version 14 and later.
* `roaringbitmap 0.5` is available for PostgreSQL version 12 and later.

To use these minor versions and the new extensions, update your instance to `[PostgreSQL version].R20250727.00_23`.

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](https://cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://cloud.google.com/sql/docs/postgres/set-maintenance-window).

---
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
