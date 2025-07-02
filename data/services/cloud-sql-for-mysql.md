# Cloud SQL for MySQL

## 2025-07-02

### Feature

The write endpoint feature for Cloud SQL Enterprise Plus edition instances is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This endpoint is a global domain name service (DNS) name and resolves to the IP address of the current primary Cloud SQL instance that's enabled with private services access.

By using a write endpoint, you can avoid having to make application connection changes after performing a switchover or replica failover operation to test or mitigate a regional failure.

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
