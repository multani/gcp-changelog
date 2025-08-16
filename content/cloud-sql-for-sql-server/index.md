# Cloud SQL for SQL Server

## 2025-08-15

### Feature

Now you can use [Private Service Connect backends](https://cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-backend), as an alternative to Private Service Connect endpoints, to access Cloud SQL instances.

### Feature

Now you can create an IPv6 endpoint for Private Service Connect (PSC) connections. For more information, see [Connect to an instance using Private Service Connect](https://cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#create-psc-endpoint).

### Deprecated

You can no longer set a deny maintenance period for instances that are running a maintenance version older than 12 months. To update your instance, [perform self-service maintenance](https://cloud.google.com/sql/docs/sqlserver/self-service-maintenance) or wait until the [next maintenance window](https://cloud.google.com/sql/docs/sqlserver/set-maintenance-window#find-maintenance-api) to update your instance automatically. For more information about maintenance, see [Maintenance updates on Cloud SQL instances](https://cloud.google.com/sql/docs/sqlserver/maintenance).

---
## 2025-08-13

### Feature

Cloud SQL now supports Private Service Connect (PSC) outbound connectivity. With PSC outbound connectivity, you can attach a PSC interface to your existing Cloud SQL PSC-enabled instances to allow your instances to make outbound connections to your network. For more information, see [PSC outbound connections](https://cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-outbound).

---
## 2025-08-07

### Feature

Cloud SQL now offers planned maintenance and machine tier upgrades for your Cloud SQL Enterprise plus instances with near-zero downtime for eligible instances.

For more information, see [Maintenance updates on Cloud SQL instances](https://cloud.google.com/sql/docs/sqlserver/maintenance#nearzero).

---
## 2025-07-31

### Feature

Cloud SQL now offers two options of backup services to manage your instance's backups:

* **Enhanced backups** ([Preview](https://cloud.google.com/products?#product-launch-stages)): backups are managed and stored in a centralized backup management project that leverages the [Backup and DR service](https://cloud.google.com/backup-disaster-recovery), and provides enforced retention, granular scheduling, and longer retention.
* **Standard backups** (existing option): backups are created, managed, and stored in the same project as your Cloud SQL instances.

You can choose between these options based on your instance's requirements and needs. Although instances can't use both backup options at the same time, Cloud SQL gives you the ability to switch between these backup options as necessary.

For more information about the available options and their limitations, see [Backup options](https://cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#backup-options).

---
## 2025-07-08

### Feature

Cloud SQL for SQL Server now offers Active Directory support for write endpoints. For more information, see [Write endpoints across forests](https://cloud.google.com/sql/docs/sqlserver/configure-private-ip#cross-forest-trusts).

---
## 2025-05-28

### Feature

Cloud SQL for SQL Server now offers the maximum server memory recommender.

Database instances running with an allocation of memory that's either too low or too high might experience performance issues.

The `max server memory (mb)` flag limits the amount of memory that Cloud SQL can allocate for its internal pools. You can manually set a value for this flag, or omit the flag and let Cloud SQL manage memory limits for you automatically.

For more information, see [Optimize maximum server memory usage](https://cloud.google.com/sql/docs/sqlserver/recommender-maximum-server-memory).

---
