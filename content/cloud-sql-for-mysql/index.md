# Cloud SQL for MySQL

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
