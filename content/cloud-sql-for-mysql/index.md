# Cloud SQL for MySQL

## 2025-11-12

### Feature

Cloud SQL for MySQL now supports minor version
[8.0.44](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-44.html).
To upgrade your existing
instance to the new version, see
[Upgrade the database minor version](https://cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#manual-upgrade).

---
## 2025-11-10

### Feature

Cloud SQL now provides brute-force detection and protection for your Cloud SQL
instances. This helps protect your instances from brute-force access attempts
by identifying the source and mitigating the risk caused by these attempts.
For more information, see
[Use brute-force protection](https://docs.cloud.google.com/sql/docs/mysql/use-brute-force-protection).

---
## 2025-11-04

### Feature

Cloud SQL now supports the
[automatic minor version upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#auto-upgrade)
for Cloud SQL for MySQL 8.0.35 or later instances.
If your Cloud SQL for MySQL instance is running MySQL 8.0.35 or later, but
you didn't select a specific minor version when you created the instance (`databaseVersion=MYSQL_8_0`),
then your MySQL instance is upgraded automatically to the [**default minor version**](https://docs.cloud.google.com/sql/docs/db-versions#database-version-support)
of Cloud SQL for MySQL 8.0 during its [regular scheduled maintenance update](https://docs.cloud.google.com/sql/docs/mysql/maintenance).

All eligible Cloud SQL for MySQL instances receive the first automatic
minor version upgrade during the rollout of [`MYSQL_8_0_[N].R20251004.01_07`](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog/mysql-8-0#mysql_8_0_%5B18,-26,-27,-28,-30,-31,-32,-33,-34,-35,-36,-37,-39,-40,-41,-42,-43%5D.r20251004.01_07).

---
## 2025-10-28

### Feature

Cloud SQL has enhanced the optimized writes feature, which includes
an improved crash recovery algorithm to reduce crash recovery time and utilizes
unused disk I/O throughput adaptively to accelerate buffer pool warm-up.
The optimized writes feature provides a set of write performance improvements
that adjust MySQL configurations dynamically based on workload demand and
underlying infrastructure.

By default these improvements are enabled for all new
Cloud SQL Enterprise Plus edition instances that you create or that you upgrade
to from Cloud SQL Enterprise edition.

For more information about optimized writes, see
[Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-optimized-write).

---
## 2025-10-17

### Feature

Cloud SQL Enterprise edition now supports a new machine series called the N4 machine series. This machine series provides balanced price-to-performance and uses the Hyperdisk Balanced storage. You can create custom machine types for the N4 machine series with up to 80 vCPUs and up to 640 GB memory. The N4 machine series is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

For more information about the N4 machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview).

### Feature

The [C4A machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4a) is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

The C4A machine series is supported for Cloud SQL Enterprise Plus edition instances, and provides optimized price-performance and delivers predictable high performance for high demand Cloud SQL workloads. It uses the Hyperdisk Balanced storage.

For more information about the C4A machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview).

---
## 2025-09-29

### Feature

You can now [use Gemini's capabilities to fix errors in a query within Cloud SQL Studio](https://cloud.google.com/sql/docs/mysql/write-sql-gemini#fix-query) ([Preview](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-09-25

### Feature

Cloud SQL for MySQL now supports minor version 8.0.43. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

---
## 2025-09-24

### Feature

Cloud SQL for MySQL 8.4.5 is upgraded to MySQL 8.4.6. For more information, see the [MySQL 8.4.6 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-6.html).

---
## 2025-09-23

### Feature

You can now provision, manage and query your databases using the dedicated Gemini CLI extension for Cloud SQL for MySQL. The extension provides full lifecycle control of your database—from provisioning instances, to exploring schemas and troubleshooting issues—from your command-line interface.

For more information, see [Use Cloud SQL for MySQL with MCP, Gemini CLI, and other agents](https://cloud.google.com/sql/docs/mysql/pre-built-tools-with-mcp-toolbox).

### Feature

You can now retain point-in-time recovery (PITR) logs for an instance after its deletion for a specified retention period. These logs can be used to restore the deleted instance to a specific point in time. For more information, see [Restore a deleted instance using PITR](https://cloud.google.com/sql/docs/mysql/backup-recovery/restore#deleted-instance).

---
## 2025-09-08

### Feature

Cloud SQL read pools are now generally available and provide operational simplicity and scaling for your read workloads.

Read pools provide a single endpoint in front of up to 20 read pool nodes and automatically load balance traffic.

You can scale your read pool in several ways:

* **Scale in or out**: scale load balancing capacity horizontally by modifying the number of read pool nodes in the read pool. Each read pool supports up to 20 read pool nodes.
* **Scale up or down**: scale load balancing capacity vertically by modifying the machine type associated with a read pool node. Once defined, configuration is uniformly applied across each read pool node in the read pool.

For more information, see
[About read pools](https://cloud.google.com/sql/docs/mysql/about-read-pools).

### Feature

You can have Cloud SQL create a [Private Service Connect](https://cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-endpoint) endpoint automatically. You can use this endpoint to access Cloud SQL instances through a VPC network. For more information, see [Create a Private Service Connect endpoint automatically](https://cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-endpoint-automatically).

This feature is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-09-04

### Changed

The release note on [August 13, 2025](https://cloud.google.com/sql/docs/mysql/release-notes#August_13_2025) regarding Private Service Connect (PSC) outbound connectivity has been updated.

PSC outbound connectivity is required for [homogeneous migrations](https://cloud.google.com/database-migration/docs/homogeneous-migrations) to PSC-enabled Cloud SQL instances using [Database Migration Service](https://cloud.google.com/database-migration/docs). For more information, see [PSC outbound connections](https://cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-outbound).

---
## 2025-09-03

### Feature

Cloud SQL Managed Connection Pooling is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Managed Connection Pooling lets you scale your workloads by optimizing resource utilization for Cloud SQL instances using pooling.

For more information, see [Managed Connection Pooling overview](https://cloud.google.com/sql/docs/mysql/managed-connection-pooling).

### Feature

You can now enable your instance to take a final backup at instance deletion and define its retention period by setting the final backup [instance setting](https://cloud.google.com/sql/docs/mysql/instance-settings).

You can also create a [custom organization policy](https://cloud.google.com/sql/docs/mysql/org-policy/custom-org-policy) to define final backup instance settings.
For more information, see [Final backup](https://cloud.google.com/sql/docs/mysql/backup-recovery/backups#final-backup).

---
## 2025-08-21

### Feature

You can save and manage SQL queries in Cloud SQL Studio. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Saved queries overview](https://cloud.google.com/sql/docs/mysql/saved-queries).

---
## 2025-08-15

### Feature

Now you can use [Private Service Connect backends](https://cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-backend), as an alternative to Private Service Connect endpoints, to access Cloud SQL instances.

### Feature

Now you can create an IPv6 endpoint for Private Service Connect (PSC) connections. For more information, see [Connect to an instance using Private Service Connect](https://cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-psc-endpoint).

### Deprecated

You can no longer set a deny maintenance period for instances that are running a maintenance version older than 12 months. To update your instance, [perform self-service maintenance](https://cloud.google.com/sql/docs/mysql/self-service-maintenance) or wait until the [next maintenance window](https://cloud.google.com/sql/docs/mysql/set-maintenance-window#find-maintenance-api) to update your instance automatically. For more information about maintenance, see [Maintenance updates on Cloud SQL instances](https://cloud.google.com/sql/docs/mysql/maintenance).

---
## 2025-08-13

### Feature

Cloud SQL now supports Private Service Connect (PSC) outbound connectivity. With PSC outbound connectivity, you can attach a PSC interface to your existing Cloud SQL PSC-enabled instances to allow your instances to make outbound connections to your network. This is required for [homogeneous migrations](https://cloud.google.com/database-migration/docs/homogeneous-migrations) to PSC-enabled Cloud SQL instances using [Database Migration Service](https://cloud.google.com/database-migration/docs). For more information, see [PSC outbound connections](https://cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-outbound).

---
## 2025-08-07

### Changed

Cloud SQL for Enterprise Plus edition supports quality enhancements for [AI-assisted troubleshooting](https://cloud.google.com/sql/docs/mysql/observe-troubleshoot-with-ai). With AI-assisted troubleshooting, you can resolve complex database performance issues like [slow queries](https://cloud.google.com/sql/docs/mysql/troubleshoot-slow-queries) and [high load](https://cloud.google.com/sql/docs/mysql/troubleshoot-high-database-load) for your instances in a guided manner. To use AI-assisted troubleshooting, you need [Gemini Cloud Assist](https://cloud.google.com/gemini/docs/cloud-assist/overview) and [query insights](https://cloud.google.com/sql/docs/mysql/using-query-insights#enable-insights) for Enterprise Plus edition.

---
## 2025-08-04

### Feature

Cloud SQL for MySQL now supports [model endpoint management](https://cloud.google.com/sql/docs/mysql/model-endpoint-overview) to help you build your generative AI applications. With model endpoint management, you can register and call remote AI model providers or access the Vertex AI integration. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages) and available in Cloud SQL for MySQL version 8.0.36 and later, which includes Cloud SQL for MySQL version 8.4.

To use model endpoint management, update your instance to [`[MySQL version].R20250531.01_14`](https://cloud.google.com/sql/docs/mysql/maintenance-changelog) or later, and make sure that you've enabled the [integration with Vertex AI](https://cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai) on your instance. You can [perform self-service maintenance](https://cloud.google.com/sql/docs/mysql/self-service-maintenance) or wait until the [next maintenance window](https://cloud.google.com/sql/docs/mysql/set-maintenance-window#find-maintenance-api) to update the maintenance version of your instance automatically.

---
## 2025-07-31

### Feature

Cloud SQL now offers two options of backup services to manage your instance's backups:

* **Enhanced backups** ([Preview](https://cloud.google.com/products?#product-launch-stages)): backups are managed and stored in a centralized backup management project that leverages the [Backup and DR service](https://cloud.google.com/backup-disaster-recovery), and provides enforced retention, granular scheduling, and longer retention.
* **Standard backups** (existing option): backups are created, managed, and stored in the same project as your Cloud SQL instances.

You can choose between these options based on your instance's requirements and needs. Although instances can't use both backup options at the same time, Cloud SQL gives you the ability to switch between these backup options as necessary.

For more information about the available options and their limitations, see [Backup options](https://cloud.google.com/sql/docs/mysql/backup-recovery/backups#backup-options).

---
## 2025-07-02

### Feature

The write endpoint feature for Cloud SQL Enterprise Plus edition instances is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This endpoint is a global domain name service (DNS) name and resolves to the IP address of the current primary Cloud SQL instance that's enabled with private services access.

By using a write endpoint, you can avoid having to make application connection changes after performing a switchover or replica failover operation to test or mitigate a region failure.

For more information, see [Connect to an instance using a write endpoint](https://cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint).

---
## 2025-07-01

### Feature

The write endpoint feature for Cloud SQL Enterprise Plus edition instances is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This endpoint is a global domain name service (DNS) name and resolves to the IP address of the current primary Cloud SQL instance that's enabled with private services access.

By using a write endpoint, you can avoid having to make application connection changes after performing a switchover or replica failover operation to test or mitigate a regional failure.

For more information, see [Connect to an instance using a write endpoint](https://cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint).

---
## 2025-06-17

### Changed

You no longer have to upgrade your instance to MySQL 8.0.37 before you upgrade to Cloud SQL for MySQL 8.4. You can upgrade to Cloud SQL for MySQL 8.4 from any minor version of Cloud SQL for MySQL 8.0. For more information about upgrading the major version of a Cloud SQL instance, see [Upgrade the database major version-place](https://cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace).

---
