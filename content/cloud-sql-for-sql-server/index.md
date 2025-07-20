# Cloud SQL for SQL Server

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
