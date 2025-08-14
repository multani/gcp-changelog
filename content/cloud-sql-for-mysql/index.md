# Cloud SQL for MySQL

## 2025-08-13

### Feature

Cloud SQL now supports Private Service Connect (PSC) outbound connectivity. With PSC outbound connectivity, you can attach a PSC interface to your existing Cloud SQL PSC-enabled instances to allow your instances to make outbound connections to your network. This is required for [homogeneous migrations using Database Migration Service](https://cloud.google.com/database-migration/docs/homogeneous-migrations). For more information, see [PSC outbound connections](https://cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-outbound).

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
