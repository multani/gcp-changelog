# Cloud SQL for SQL Server

## 2026-02-18

### Deprecated

Control of MCP use with organization policies is deprecated.
After March 17, 2026, organization policies that use the
`gcp.managed.allowedMCPServices` constraint won't work,
and you can control MCP use with IAM deny policies.
For more information about controlling MCP use, see
[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

### Change

After March 17, 2026, when you enable the Cloud SQL Admin API
(`sqladmin.googleapis.com`), the Cloud SQL remote MCP server is
enabled automatically.

The Cloud SQL remote MCP server is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2026-02-17

### Announcement

New best practices are available for securing generative AI agents using
Model Context Protocol (MCP) with Google Cloud databases. This guide covers
key security measures like least privilege, native database controls, and
secure agent design to help you build safer AI applications.
For more information, see [Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/sql/docs/sqlserver/secure-agent-interactions-mcp).

---
## 2026-02-09

### Feature

You can now use the [Cloud SQL remote MCP server](https://docs.cloud.google.com/sql/docs/sqlserver/use-cloudsql-mcp).
The Cloud SQL remote MCP server lets you interact easily with Cloud SQL
instances from LLMs, AI applications, and AI-enabled development platforms.

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2026-02-02

### Feature

You can now update the server certificate authority (CA) mode of an existing
Cloud SQL instance. You can update existing instances that use the per-instance
CA option (`GOOGLE_MANAGED_INTERNAL_CA`) to use the shared CA option
(`GOOGLE_MANAGED_CAS_CA`) or the customer-managed CA option (`CUSTOMER_MANAGED_CAS_CA`).

For more information about the different server CA mode options, see
[Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#ca-hierarchies).

---
## 2025-12-16

### Feature

Cloud SQL enhanced backups are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

With enhanced backups, backups are managed and stored in a centralized
backup management project that leverages the
[Backup and DR service](https://docs.cloud.google.com/backup-disaster-recovery), and
provides enforced retention, granular scheduling, and longer retention.

Enhanced backups now also support
[point-in-time-recovery (PITR) after instance deletion](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore).

For more information about the available options and their limitations, see
[Backup options](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backup-options).
For more information about enhanced backups pricing, see
[Backup and DR pricing](https://cloud.google.com/backup-disaster-recovery/pricing).

---
## 2025-12-11

### Feature

[Cloud SQL for SQL Server integration with Microsoft Entra ID](https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id)
([Preview](https://cloud.google.com/products#product-launch-stages))
provides centralized identity and access management (IAM) for your databases
using your existing Microsoft Entra ID tenant.

---
## 2025-10-29

### Feature

You can integrate Cloud SQL for SQL Server with customer-managed Active Directory (CMAD).

CMAD provides capabilities such as authentication and authorization. Joining an
instance to a CMAD domain lets you sign in using Windows Authentication with an
AD-based identity.

[Customer-managed Active Directory (CMAD)](https://docs.cloud.google.com/sql/docs/sqlserver/cmad)
is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-10-17

### Feature

Cloud SQL Enterprise edition now supports a new machine series called the N4 machine series. This machine series provides balanced price-to-performance and uses the Hyperdisk Balanced storage. You can create custom machine types for the N4 machine series with up to 80 vCPUs and up to 640 GB memory. The N4 machine series is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

For more information about the N4 machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview).

---
## 2025-10-06

### Feature

You can now use [advanced disaster recovery (DR)](https://cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery#advanced-dr) for your Private Service Connect (PSC) enabled Cloud SQL Enterprise Plus edition instances. With advanced DR, you can:

* Designate a cross-region disaster recovery (DR) replica
* Perform a cross-region replica failover for disaster recovery
* Restore your original deployment by using zero-data loss switchover

You can also use switchover to simulate disaster recovery without data loss. For more information, see
[Use advanced disaster recovery (DR)](https://cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery)
. This feature is
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

---
## 2025-09-29

### Feature

You can now [use Gemini's capabilities to fix errors in a query within Cloud SQL Studio](https://cloud.google.com/sql/docs/sqlserver/write-sql-gemini#fix-query) ([Preview](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-09-23

### Feature

You can now provision, manage and query your databases using the dedicated Gemini CLI extension for Cloud SQL for SQL Server. The extension provides full lifecycle control of your database—from provisioning instances, to exploring schemas and troubleshooting issues—from your command-line interface.

For more information, see [Use Cloud SQL for SQL Server with MCP, Gemini CLI, and other agents](https://cloud.google.com/sql/docs/sqlserver/pre-built-tools-with-mcp-toolbox).

### Feature

You can now retain point-in-time recovery (PITR) logs for an instance after its deletion for a specified retention period. These logs can be used to restore the deleted instance to a specific point in time. For more information, see [Restore a deleted instance using PITR](https://cloud.google.com/sql/docs/sqlserver/backup-recovery/restore#deleted-instance).

---
## 2025-09-08

### Feature

You can have Cloud SQL create a [Private Service Connect](https://cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint) endpoint automatically. You can use this endpoint to access Cloud SQL instances through a VPC network. For more information, see [Create a Private Service Connect endpoint automatically](https://cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#create-endpoint-automatically).

This feature is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-09-03

### Feature

You can now enable your instance to take a final backup at instance deletion and define its retention period by setting the final backup [instance setting](https://cloud.google.com/sql/docs/sqlserver/instance-settings).

You can also create a [custom organization policy](https://cloud.google.com/sql/docs/sqlserver/org-policy/custom-org-policy) to define final backup instance settings.
For more information, see [Final backup](https://cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#final-backup).

---
## 2025-08-29

### Feature

[`Max degree of parallelism (MAXDOP)`](https://cloud.google.com/sql/docs/sqlserver/flags#max-degree-of-parallelism) is a Microsoft database flag available for use in Cloud SQL for SQL Server. This flag lets you limit the maximum number of threads used when running a single query in a parallel plan.

---
## 2025-08-21

### Feature

You can save and manage SQL queries in Cloud SQL Studio. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Saved queries overview](https://cloud.google.com/sql/docs/sqlserver/saved-queries).

---
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
