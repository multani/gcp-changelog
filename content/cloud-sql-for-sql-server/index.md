# Cloud SQL for SQL Server

## 2026-04-20

### Feature

You can use the [Database Insights remote MCP server](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/databaseinsights/mcp)
to analyze Cloud SQL for SQL Server's performance and system metrics. This
feature is in [GA](https://cloud.google.com/products/#product-launch-stages).

---
## 2026-04-18

### Feature

Newly created Cloud SQL instances are integrating with Knowledge Catalog
(formerly Dataplex Universal Catalog) for data discovery. As part of this
automatic enablement, we will send metadata to Knowledge Catalog. You can verify
if your instance is enabled for integration with Knowledge Catalog by looking at
the configuration pane in the Knowledge Catalog console. If you don't want your
instance to be integrated with Knowledge Catalog, you can [turn off this
feature](https://docs.cloud.google.com/sql/docs/sqlserver/dataplex-catalog-integration#deactivate-dataplex-catalog).

For more information, see [Create a new instance with Knowledge Catalog
integration
enabled](https://docs.cloud.google.com/sql/docs/sqlserver/dataplex-catalog-integration#enable-new).

---
## 2026-04-17

### Feature

You can now integrate Cloud SQL for SQL Server with Vertex AI and third-party models ([Preview](https://docs.cloud.google.com/products#product-launch-stages)).

By integrating your Cloud SQL for SQL Server instance with Vertex AI, you can
generate vector embeddings from models hosted in Vertex AI directly from your
Cloud SQL instance.

Cloud SQL for SQL Server supports model endpoints from the following sources:

* Vertex AI
* Hugging Face
* OpenAI

For more information, see [Integrate Cloud SQL for SQL Server with Vertex AI](https://docs.cloud.google.com/sql/docs/sqlserver/integrate-cloud-sql-with-vertex-ai).

---
## 2026-04-16

### Feature

The [Cloud SQL remote MCP server](https://docs.cloud.google.com/sql/docs/sqlserver/use-cloudsql-mcp)
is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).
The Cloud SQL remote MCP server lets you interact easily with Cloud SQL
instances from LLMs, AI applications, and AI-enabled development platforms.

### Feature

You can use
[DNS automation](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#dns-automation)
on Cloud SQL instances where Private Service Connect is enabled to provision
and manage per-instance DNS records automatically. On Enterprise Plus edition
instances where DNS automation is enabled, you can also enable a global write
endpoint DNS that automatically resolves to your current primary instance.

This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

---
## 2026-04-14

### Breaking

As of April 10, 2026, you can create, run, and edit
[Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations) only
if you have a [Premium Support contract](https://cloud.google.com/support/premium).
You can use Gemini Cloud
Assist investigations to [monitor and troubleshoot your
Cloud SQL instance with AI assistance](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-troubleshoot-with-ai).

If you ran an investigation prior to April 10, 2026,
then the results of the investigation continue to be
available to you in the Google Cloud console.

---
## 2026-04-06

### Feature

If the storage capacity of a Cloud SQL instance is larger than your application
needs, then you can manually reduce, or shrink, your storage capacity to a smaller
size.

Depending on underlying disk size, storage shrink operations might incur
considerable downtime. If your instance requires limited downtime, rather than
using storage shrink capabilities, we recommend migrating your data to a new,
smaller instance using Database Migration Service.

For more information, see
[About storage shrink](https://docs.cloud.google.com/sql/docs/sqlserver/about-storage-shrink).

### Feature

Cloud SQL for SQL Server now supports SQL Server 2025 ([GA](https://cloud.google.com/products/#product-launch-stages)):

* SQL Server 2025 Standard
* SQL Server 2025 Enterprise
* SQL Server 2025 Express

For more information, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions)
and [Choose a machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview).

### Feature

[Cloud SQL for SQL Server integration with Microsoft Entra ID](https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id)
([GA](https://cloud.google.com/products/#product-launch-stages))
provides centralized identity and access management (IAM) for your databases
using your existing Microsoft Entra ID tenant.

---
## 2026-04-02

### Feature

Cloud SQL for SQL server read pools are now generally available and provide
operational simplicity and scaling for your read workloads.

Read pools provide a single endpoint in front of up to seven read pool nodes and
automatically load balance traffic.

You can scale your read pool in several ways:

* **Scale in or out**: scale load balancing capacity horizontally by modifying
  the number of read pool nodes in the read pool. Each read pool supports between
  1 and 7 read pool nodes.
* **Scale up or down**: scale load balancing capacity vertically by modifying the
  machine type associated with a read pool node. Once defined, configuration is
  uniformly applied across each read pool node in the read pool.

For more information, see [About read pools](https://docs.cloud.google.com/sql/docs/sqlserver/about-read-pools).

---
## 2026-03-17

### Feature

Cloud SQL supports cross-project PITR operations for instances protected by
backup and DR ([GA](https://cloud.google.com/products/#product-launch-stages)).

This feature lets you restore a Cloud SQL instance to a project other than the
project where either the source instance or the backup vault is located.

For more information, see [Perform a cross-project PITR](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr#perform_a_cross-project_pitr).

### Change

Point-in-time recovery (PITR) default enablement behavior has changed:

* PITR is now enabled by default when you create a
  [Cloud SQL Enterprise edition](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro)
  instance in the Google Cloud console.
* PITR is enabled by default when you create a [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro)
  instance, regardless of the method used.

For more information, see [Configure point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/configure-pitr).

### Feature

[Multi-region backup vaults for Cloud SQL enhanced backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#multi-regions)
are generally available (GA).

This feature lets you store your backup data in
multi-region storage locations, providing higher availability and protection
against regional outages.

For more information, see [Enhanced backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backup-options#enhanced-backups).

---
## 2026-03-13

### Feature

You can now enable automatic server certificate rotation for your Cloud SQL instance.
This feature is specifically designed for instances utilizing the Certificate
Authority Service (CAS). Automatic server certificate rotation helps you maintain high security standards while removing the operational burden of manual rotation.

For more information about enabling automatic server certificate rotation for
your instance, see [Enable automatic server certificate rotation](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance#automatic-server-certificate-rotation-cas).

---
## 2026-02-23

### Feature

Gemini Cloud Assist investigation capabilities are now supported in
Cloud SQL for SQL Server ([Preview](https://cloud.google.com/products/#product-launch-stages)).

For more information, see
[Troubleshoot slow queries with AI assistance](https://docs.cloud.google.com/sql/docs/sqlserver/troubleshoot-slow-queries).

---
## 2026-02-18

### Change

After March 17, 2026, when you enable the Cloud SQL Admin API
(`sqladmin.googleapis.com`), the Cloud SQL remote MCP server is
enabled automatically.

The Cloud SQL remote MCP server is in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Deprecated

Control of MCP use with organization policies is deprecated.
After March 17, 2026, organization policies that use the
`gcp.managed.allowedMCPServices` constraint won't work,
and you can control MCP use with IAM deny policies.
For more information about controlling MCP use, see
[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

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
