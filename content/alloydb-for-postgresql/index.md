# AlloyDB for PostgreSQL

## 2026-02-09

### Fixed

We are announcing the release of support for the AlloyDB language connectors and
Auth Proxy with [Auto IAM Authentication](https://docs.cloud.google.com/alloydb/docs/connect-iam#automatic)
and managed connection pooling. This feature and the fix for the issue from
below is available starting with maintenance version 20260107.02\_05. Clusters
with a maintenance window that may not have received this release can use
[self-service maintenance](https://docs.cloud.google.com/alloydb/docs/self-service-maintenance)
to perform a maintenance update.

---
## 2026-02-05

### Feature

[Virtual columns for
expressions](https://cloud.google.com/alloydb/docs/columnar-engine/add-frequent-expressions)
is a feature of the columnar engine in
[Preview](https://cloud.google.com/products#product-launch-stages) that
significantly improves query performance and reduces CPU consumption. It caches
the results of frequently used expressions, which is especially beneficial for
analytical workloads on large datasets.

---
## 2026-01-27

### Feature

Database server compatibility with PostgreSQL version 18 is now available for
preview ([Preview](https://cloud.google.com/products#product-launch-stages)).
You can
[create AlloyDB clusters](https://cloud.google.com/alloydb/docs/cluster-create#procedure)
with PostgreSQL 18 compatibility.

---
## 2026-01-21

### Issue

Automatic IAM authentication is unavailable when you use managed connection
pooling with the AlloyDB Auth Proxy and Language Connectors. To sign into your
database without a password, use manual IAM authentication. For more
information, see [Connect using an IAM account](https://docs.cloud.google.com/alloydb/docs/connect-iam)

---
## 2026-01-20

### Feature

You can
[create AlloyDB cluster instances](https://docs.cloud.google.com/alloydb/docs/cluster-create)
in Bangkok, Thailand (`asia-southeast3`). For more information, see
[AlloyDB locations](https://docs.cloud.google.com/alloydb/docs/locations) and
[AlloyDB for PostgreSQL pricing](https://cloud.google.com/alloydb/pricing).

---
## 2026-01-19

### Feature

AlloyDB now supports the Z3 machine series, which are powered by 4th generation Intel x86 processors (Sapphire Rapids) with Titanium SSD. These instances offer machine sizes, with up to 88 vCPU and 704 GiB RAM, that let you run storage-intensive workloads with large working datasets. For more information, see [Choose an AlloyDB machine type](https://docs.cloud.google.com/alloydb/docs/choose-machine-type#z3-standardlssd). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2026-01-15

### Fixed

Memory usage estimation is more accurate for high-dimensional vector indexes. This
fix prevents out of memory (OOM) errors by enforcing defined memory constraints
throughout the index build process. You might need to increase your
`maintenance_work_mem settings` to align with the real usage estimates.

---
## 2025-12-24

### Change

The extension `vector`, which includes `pgvector` functions and operators, is updated to version 0.8.1.

---
## 2025-12-18

### Feature

Managed connection pooling is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). This feature optimizes resource usage to improve workload scalability and reliability. It is compatible with the AlloyDB Auth Proxy and Language Connectors. For more information, see [Configure managed connection pooling](https://docs.cloud.google.com/alloydb/docs/configure-managed-connection-pooling).

### Feature

AlloyDB database [performance snapshot reports](https://docs.cloud.google.com/alloydb/docs/optimize-database-performance-compare-snapshots#generate-a-performance-snapshot-report) now include a SQL Report section, which lists the top 50 queries by total elapsed time, read I/O, and standard deviation of elapsed time. This helps you identify and optimize resource-intensive queries.

---
## 2025-12-17

### Feature

You can now use Gemini 3.0 Flash
([Preview](https://cloud.google.com/products#product-launch-stages))
when you call generative AI functions in AlloyDB, such as `AI.GENERATE`. Use the
model name `gemini-3-flash-preview`. For more information, see
[Use Gemini 3.0 models](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators#use-gemini-model-3).

### Feature

You can build data agents that interact with the data in your
database using conversational language. Use these data agents as tools to
empower your applications. For more information, see [Data agents overview](https://docs.cloud.google.com/alloydb/docs/ai/data-agent-overview). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages), and access to it requires a [sign-up](https://forms.gle/pJByTWfenZAWbaXo7).

---
## 2025-12-11

### Feature

AlloyDB now supports the C4 machine series, which are powered by 6th generation Intel Xeon Granite Rapids processors. These instances offer massive machine sizes, with up to 288 vCPU and 2232 GiB RAM, that let you run extremely demanding workloads. For more information,
see [Choose an AlloyDB machine type](https://docs.cloud.google.com/alloydb/docs/choose-machine-type). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-12-08

### Feature

You can now use Gemini to [fix query errors in the AlloyDB Studio query editor](https://docs.cloud.google.com/alloydb/docs/write-sql-gemini#fix-error-in-queries). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-12-05

### Feature

Query plan management ([Preview](https://cloud.google.com/products#product-launch-stages)) ensures query plan stability, and protects your
database performance against the risk of query plan regression due to changes
in the database or the optimizer's behavior. AlloyDB continuously monitors,
captures, and logs potential query execution plans, giving you the granular
control to force the optimizer to choose from approved plans, and prevent
unintended regressions. For more information, see [Manage query plans](https://docs.cloud.google.com/alloydb/docs/query-plan-management).

---
## 2025-11-20

### Feature

AlloyDB now supports horizontal [autoscaling for read pool instances](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-scale#autoscale-read-pool). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-11-19

### Change

The upper limit of the query plans captured per minute is enhanced to 200. For more information, see [Improve query performance using advanced query insights features for AlloyDB](https://docs.cloud.google.com/alloydb/docs/using-advanced-query-insights#gcloud).

### Feature

You can now [perform self-service maintenance](https://docs.cloud.google.com/alloydb/docs/self-service-maintenance)
if you need to apply the latest AlloyDB updates to your clusters as soon as
possible.
Updating to the latest version can unlock AlloyDB features, apply patches,
and let you set deny periods.

---
## 2025-11-18

### Feature

You can now use Gemini 3.0 when you call generative AI functions in AlloyDB, such as `AI.GENERATE`. For more information, see [Use Gemini 3.0 models](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators#use-gemini-model-3).

---
## 2025-11-13

### Feature

AlloyDB AI native vector search accelerator is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). It includes the following features and improvements:

* The `google_columnar_engine` extension is updated to automatically recommend data for searches, so you don't need to manually add vector columns to the table. For more information, see [Perform a vector search](https://docs.cloud.google.com/alloydb/docs/ai/perform-vector-search#accelerate-filtered-vector-search).
* The `alloydb_scann` extension is updated with new metrics for vector index creation. You can now use the [pg\_stat\_ann\_index\_creation](https://docs.cloud.google.com/alloydb/docs/ai/tune-indexes?resource=scann#vector-index-metrics) view to see the number of rows present in a table at the time of index creation.

---
## 2025-11-11

### Feature

You can now use Dataplex Universal Catalog to discover, search, and manage your
AlloyDB resources, including clusters, databases, and tables. This integration
(in [Preview](https://cloud.google.com/products#product-launch-stages)) provides
a unified view of your metadata, enabling better data
governance and easier analysis. For more information, see
[Manage your AlloyDB resources using Dataplex Universal Catalog](https://docs.cloud.google.com/alloydb/docs/dataplex-catalog-integration).

### Feature

Improve query performance for partitioned tables and complex queries using
parallel execution for the `SELECT` portion of an `INSERT INTO ... SELECT`
query. For more information,
see [Improve select insert performance with parallel select](https://docs.cloud.google.com/alloydb/docs/improve-select-insert-performance-parallel-select).

---
## 2025-11-10

### Feature

AlloyDB AI introduces [auto embedding generation](https://docs.cloud.google.com/alloydb/docs/ai/generate-manage-auto-embeddings-for-tables) in [Preview](https://cloud.google.com/products#product-launch-stages). You can now generate large-scale embeddings to leverage in semantic search and Retrieval Augmented Generation (RAG) on text content.

### Feature

AlloyDB now supports PostgreSQL 17 for migrating from Cloud SQL for PostgreSQL
to AlloyDB for PostgreSQL using your Cloud SQL for PostgreSQL backup. The size
limit for these operations is now 15TB. For more information, see
[Migrate from Cloud SQL for PostgreSQL to AlloyDB](https://docs.cloud.google.com/alloydb/docs/migrate-cloud-sql-to-alloydb).

---
## 2025-10-31

### Announcement

The `alloydb_scann` extension version `0.1.3` is updated to include the following vector search improvements, which are now Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)):

* The columnar engine now automatically includes vector columns in searches, so you don't need to add them to the table manually.
  For more information, see [Perform a vector search](https://docs.cloud.google.com/alloydb/docs/ai/perform-vector-search#accelerate-filtered-vector-search).
* You can use the `pg_stat_ann_index_creation` view for metrics about the number of rows at index creation. For more information, see [Vector index metrics](https://docs.cloud.google.com/alloydb/docs/ai/tune-indexes?resource=scann#vector-index-metrics).

---
## 2025-10-30

### Feature

AlloyDB offers enhanced backups
([Preview](https://cloud.google.com/products#product-launch-stages))
that integrate a cluster's backup operations with the Google Cloud
[Backup and DR Service](https://cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).
This integration provides vaulted backups data with retention lock enforcement,
and it uses the Backup and DR Service control plane for centralized policy
management and advanced scheduling for AlloyDB clusters. For more information,
see [Manage enhanced backups](https://cloud.google.com/alloydb/docs/backup/manage-enhanced-backups).

---
## 2025-10-27

### Feature

AlloyDB supports configuring Authorized Networks for Public IP without any
CIDR-range restrictions. Use custom organization policies to limit the size
and number of Authorized Networks. See [Supported custom constraints and
operations](https://cloud.google.com/alloydb/docs/alloydb-custom-constraints#supported-custom-constraints-operations)
for examples.

---
## 2025-10-23

### Feature

You can now perform [time-series forecasting](https://docs.cloud.google.com/alloydb/docs/ai/perform-time-series-forecasting) in AlloyDB to predict future trends based on your historical data. This feature supports various forecasting models, including TimesFM, and is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-06

### Feature

AlloyDB supports the `tds_fdw` extension, which provides a foreign data wrapper
for accessing databases—such as Microsoft SQL Server and Sybase—that
use the Tabular Data Stream (TDS) protocol. For more information, see [Supported database extensions](https://cloud.google.com/alloydb/docs/reference/extensions). This feature is
[generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-09-30

### Feature

You can enable [`alloydb.enable_cache_aware_costing`](https://cloud.google.com/alloydb/docs/reference/alloydb-flags#alloydb.enable_cache_aware_costing) to turn on
cache awareness for AlloyDB for PostgreSQL's query planner. This improves index
scan query plans for query performance and reduces IO costs. This feature
is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-29

### Announcement

The `alloydb_scann` extension version `0.1.3` is updated to include the following vector search improvements in ([Preview](https://cloud.google.com/products#product-launch-stages)):

* You can now [automatically create ScaNN indexes](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index) that are optimized for search performance or for a balance between index build times and search performance with the auto index feature.
* AlloyDB AI's [adaptive filtering](https://docs.cloud.google.com/alloydb/docs/ai/adaptive-filtering) for filtered vector searches now dynamically switches between pre-filtering and inline filtering. This enhancement further optimizes query performance by allowing the query optimizer to dynamically choose the most efficient filtering strategy. For more information, see [Activate adaptive filtering in AlloyDB AI](https://docs.cloud.google.com/alloydb/docs/ai/activate-adaptive-filtering).
* AlloyDB AI now [integrates ScaNN indexes with the columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure#configure-index-cache). You can now accelerate your vector similarity search by [loading ScaNN indexes into the columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-manually#manage-index-cache).
* The `alloydb_scann` extension now provides a satisfy limit feature that improves query recall for vector searches. If a search returns fewer results than specified in the `LIMIT` clause, the scan continues until the `LIMIT` is met or a configured upper bound is reached. To enable this feature, set the [`scann.satisfy_limit`](https://docs.cloud.google.com/alloydb/docs/reference/ai/scann-index-reference#scann-satisfy-limit) flag to `relaxed order`. You can also use the [`scann.max_pct_leaves_to_search`](https://docs.cloud.google.com/alloydb/docs/reference/ai/scann-index-reference#scann-max-pct-leaves-to-search) flag to configure the upper bound for the search.
* You can enable vector search index recommendations for Scalable Nearest Neighbors (ScaNN) indexes using the AlloyDB index advisor. For more information, see [Use the AlloyDB index advisor with query insights](https://docs.cloud.google.com/alloydb/docs/use-index-advisor-with-query-insights#enable-extensions) or [View the index advisor's index recommendations](https://docs.cloud.google.com/alloydb/docs/use-index-advisor#view-recommendations).
* You can configure automatic index maintenance using the following flags:

  + [`scann.max_background_workers`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#scann.max_background_workers) flag to control the number of background workers and increase throughput across multiple indexes.
  + [`scann.maintenance_background_naptime_s`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#scann.maintenance_background_naptime_s) flag to control the minimum delay between maintenance runs.

---
## 2025-09-24

### Feature

You can [create and manage query plan patches](https://cloud.google.com/alloydb/docs/create-manage-query-plan-patches). Query plan patches let you specify the details of the execution plan of your queries. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-23

### Feature

You can now provision, manage, and query your databases using the [dedicated Gemini CLI extensions for AlloyDB](https://cloud.google.com/alloydb/docs/connect-ide-using-mcp-toolbox#connect-alloydb-gemini-cli-extension). The extensions provide full lifecycle control of your database - from provisioning instances to exploring schemas and troubleshooting issues. This feature is available in beta.

---
## 2025-09-22

### Feature

The available memory metric now accurately reflects the memory available to
AlloyDB by taking into consideration usable memory from the OS page cache. This
improvement can lead to a lower value of the metric, which you might notice
when you update your version to PG 17 or later. This feature is generally
available ([GA](https://cloud.google.com/products#product-launch-stages))
and is available for AlloyDB for PostgreSQL version 17 and later. For more information,
see [System insights metrics reference](https://cloud.google.com/alloydb/docs/reference/system-insights-metrics).

### Feature

Database server compatibility with PostgreSQL version 17 is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can [create AlloyDB clusters](https://cloud.google.com/alloydb/docs/cluster-create#procedure) with PostgreSQL 17 compatibility.

---
## 2025-09-11

### Feature

AlloyDB supports
[C4A Arm VMs](https://cloud.google.com/compute/docs/general-purpose-machines#c4a_series)
on Google's custom-built Axion processors. C4A VMs are available as predefined
configurations from 1, 4, 8, 16, 32, 48, 64, and 72 vCPUs, up to 576 GB of DDR5
memory. C4A machines are available in
[limited regions](https://cloud.google.com/alloydb/docs/cluster-create#expandable-1).
For more information, see
[Considerations when using the C4A Axion-based machine series](https://cloud.google.com/alloydb/docs/cluster-create#considerations-c4a).
This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-09-04

### Feature

[Parameterized secure views](https://cloud.google.com/alloydb/docs/parameterized-secure-views-overview) in AlloyDB for PostgreSQL enhance data security and row access control while using SQL, providing a new secure interface for application developers. Access to this [Preview](https://cloud.google.com/products#product-launch-stages) feature no longer requires a signup.

### Feature

[AlloyDB AI natural language](https://cloud.google.com/alloydb/docs/ai/natural-language-overview)
delivers secure and accurate responses for
application end user natural language questions. Natural language offers
fragment-based templates, autogenerated concept types, and SQL summaries.
Access to this [Preview](https://cloud.google.com/products#product-launch-stages)
feature no longer requires a signup.

---
## 2025-09-02

### Feature

You can create [organization policies with custom constraints](https://cloud.google.com/alloydb/docs/org-policy) for AlloyDB backups and clusters, and a custom constraint with any field for an AlloyDB instance. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-08-20

### Feature

You can save and manage your SQL scripts in AlloyDB Studio. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Saved queries overview](https://cloud.google.com/alloydb/docs/saved-queries).

---
## 2025-07-29

### Feature

Database server compatibility with PostgreSQL version 17 is now available in
[Preview](https://cloud.google.com/products#product-launch-stages).
You can [create AlloyDB clusters](https://cloud.google.com/alloydb/docs/cluster-create#procedure)
with PostgreSQL 17 compatibility.

---
## 2025-07-23

### Announcement

[AlloyDB Omni](https://cloud.google.com/alloydb/omni/current/docs)
version 16.8.0 is generally available
([GA](https://cloud.google.com/products#product-launch-stages)). Version 16.8.0
includes the following features and changes:

* AlloyDB Omni supports PostgreSQL version
  [16.8](https://www.postgresql.org/docs/release/16.8/).
* AlloyDB Omni supports the
  [`pg_squeeze`](https://cloud.google.com/alloydb/omni/current/docs/reference/extensions) extension
  that addresses table bloat and improves data locality.
* You can set up the columnar engine storage cache on dedicated devices. For
  more information, see
  [Configure the columnar engine in AlloyDB Omni](https://cloud.google.com/alloydb/omni/16.8.0/docs/columnar-engine/configure).
* [Improved I/O acceleration](https://cloud.google.com/alloydb/omni/16.8.0/docs/improve-database-performance-using-io-acceleration)
  due to bug fixes in `libaio`.
* [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) authentication integration is generally available ([GA](https://cloud.google.com/products#product-launch-stages)), providing robust user authentication for your database clusters. For more information, see [Integrate Active Directory with AlloyDB Omni](https://cloud.google.com/alloydb/omni/16.8.0/docs/integrate-active-directory).
* Active Directory group-based authorization is available in [Preview](https://cloud.google.com/products#product-launch-stages), enabling granular permission management based on your Active Directory groups. For more information, see [Integrate Active Directory group support with AlloyDB Omni](https://cloud.google.com/alloydb/omni/16.8.0/docs/integrate-ad-group-support-alloydb-omni).

### Announcement

[AlloyDB Omni](https://cloud.google.com/alloydb/omni/current/docs)
version 15.12.0 is generally available
([GA](https://cloud.google.com/products#product-launch-stages)). Version 15.12.0
includes the following features and changes:

* AlloyDB Omni supports PostgreSQL version
  [15.12](https://www.postgresql.org/docs/release/15.12/).
* AlloyDB Omni supports the
  [`pg_squeeze`](https://cloud.google.com/alloydb/omni/current/docs/reference/extensions) extension
  that addresses table bloat and improves data locality.
* You can set up the columnar engine storage cache on dedicated devices. For
  more information, see
  [Configure the columnar engine in AlloyDB Omni](https://cloud.google.com/alloydb/omni/15.12.0/docs/columnar-engine/configure).

### Announcement

The [AlloyDB Omni Kubernetes operator](https://cloud.google.com/alloydb/omni/current/docs/deploy-kubernetes) version 1.5.0 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) and includes the following features and bug fixes:

* You can install the operator using the [Operator Lifecycle Manager (OLM)](https://olm.operatorframework.io/) for Kubernetes and OpenShift environments. See "Install the AlloyDB Omni operator" for AlloyDB Omni [15.12.0](https://cloud.google.com/alloydb/omni/15.12.0/docs/deploy-kubernetes#olm) and [16.8.0](https://cloud.google.com/alloydb/omni/16.8.0/docs/deploy-kubernetes#olm) for details.
* Low downtime, minor version upgrades for a database cluster in a high availability setup are available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see "Perform a minor database version upgrade for AlloyDB Omni on Kubernetes" in the documentation for AlloyDB Omni [15.12.0](https://cloud.google.com/alloydb/omni/15.12.0/docs/upgrade-kubernetes-database-minor-version) and [16.8.0](https://cloud.google.com/alloydb/omni/16.8.0/docs/upgrade-kubernetes-database-minor-version).
* [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) authentication integration on your Kubernetes-based AlloyDB Omni database cluster is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Integrate Active Directory with AlloyDB Omni on Kubernetes](https://cloud.google.com/alloydb/omni/16.8.0/docs/integrate-active-directory-kubernetes-operator).
* Active Directory group-based authorization on your Kubernetes-based AlloyDB Omni database cluster is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integrate Active Directory group support on Kubernetes](https://cloud.google.com/alloydb/omni/16.8.0/docs/integrate-ad-group-support-kubernetes-operator).
* You can configure backups to be taken directly from a standby Kubernetes cluster in a high availability (HA) setup to offload backup operations from your primary instance. See "Backup and restore in Kubernetes" for AlloyDB Omni [15.12.0](https://cloud.google.com/alloydb/omni/15.12.0/docs/backup-kubernetes) and [16.8.0](https://cloud.google.com/alloydb/omni/16.8.0/docs/backup-kubernetes) for details.
* The operator fully automatically replicates replication slots for cross-data-center replication to work with primary database clusters that have high availability (HA) enabled. You still need to make sure you have reliable and low latency network connectivity between the primary and secondary data centers, which is crucial for cross-data-center replication to function effectively. For more information, see "Work with cross-data-center replication" for AlloyDB Omni [15.12.0](https://cloud.google.com/alloydb/omni/15.12.0/docs/cross-data-center-replication/work-with-cross-data-center-replication) and [16.8.0](https://cloud.google.com/alloydb/omni/16.8.0/docs/cross-data-center-replication/work-with-cross-data-center-replication).
* AlloyDB Omni Kubernetes images are now built on Red Hat's Universal Base Image (UBI) 9. For more information, see "Install AlloyDB Omni on Kubernetes" for AlloyDB Omni [15.12.0](https://cloud.google.com/alloydb/omni/15.12.0/docs/deploy-kubernetes#base-image) and [16.8.0](https://cloud.google.com/alloydb/omni/16.8.0/docs/deploy-kubernetes#base-image).
* AlloyDB AI requires AlloyDB Omni version 15.5.5 or later.

### Issue

When upgrading your AlloyDB Omni database clusters, be aware of specific upgrade paths and prerequisites depending on your current `controlPlaneAgentsVersion` and environment:

* If your database cluster's `controlPlaneAgentsVersion` is `1.0.0`, you must first upgrade to `1.1.1` before you upgrade to `1.5.0` or higher. You can directly upgrade database clusters with `controlPlaneAgentsVersion` `1.1.0` or later to `1.5.0`.
* If you use an OpenShift database cluster that runs `controlPlaneAgentsVersion` `1.4.1` or earlier, you must run prerequisite steps before updating to `1.5.0`. For more information, see "Update OpenShift database clusters from version `1.4.1` or earlier" for AlloyDB Omni [15.12.0](https://cloud.google.com/alloydb/omni/15.12.0/docs/upgrade-kubernetes-operator-version#update-openshift) and [16.8.0](https://cloud.google.com/alloydb/omni/16.8.0/docs/upgrade-kubernetes-operator-version#update-openshift).

---
## 2025-07-14

### Feature

You can now create an AlloyDB instance with a specific IP address range using the Google Cloud CLI, Terraform, or REST API. You can also override IP address range allocations configured during cluster creation. For more information, see [Create an instance with a specific IP address range](https://cloud.google.com/alloydb/docs/cluster-create#ip-instance). This feature is generally available [GA](https://cloud.google.com/products#product-launch-stages).

---
## 2025-06-17

### Feature

You can use the columnar engine to improve the performance of vector similarity
searches, specifically K-Nearest Neighbor (KNN) searches, when combined with
highly-selective predicate filtering. For more information, see
[Accelerate your filtered vector search](https://cloud.google.com/alloydb/docs/ai/perform-vector-search#accelerate-filtered-vector-search). This feature is in
[Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-06-02

### Feature

You can let [AlloyDB automatically create Private Service Connect endpoints](https://cloud.google.com/alloydb/docs/configure-private-service-connect#create_the_endpoint_automatically)
for authorized projects when you create Private Service Connect-enabled
instances, based on your defined service connection policy. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

### Feature

You can create AlloyDB clusters with [Private Services Connect](https://cloud.google.com/alloydb/docs/configure-private-service-connect#create_the_endpoint_automatically) through the Google Cloud console.

---
## 2025-05-29

### Feature

You can now
[start, stop, and restart your primary and read pool AlloyDB instances](https://cloud.google.com/alloydb/docs/instance-start-stop-restart)
using the Google Cloud console and the Google Cloud CLI. This feature is
generally available
([GA](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-05-27

### Feature

The [AlloyDB Omni Kubernetes](/alloydb/omni/current/docs/deploy-kubernetes) operator version 1.4.1 is generally available (GA) and includes the following bug fixes:

* Fix for overriding replication related parameters. This fix lets you override the `wal_keep_size` value. For more information, see [Work with cross-data-center replication](/alloydb/omni/current/docs/cross-data-center-replication/work-with-cross-data-center-replication). This fix requires database version 15.7.1 or later.
* 63-character DBCluster names are supported, which lets you define clearer and more descriptive cluster names.
* Various bug fixes are implemented to enhance stability and the user experience.

---
