# AlloyDB for PostgreSQL

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

* You can now [automatically create ScaNN indexes](https://cloud.google.com/alloydb/docs/ai/create-scann-index) that are optimized for search performance or for a balance between index build times and search performance with the auto index feature.
* AlloyDB AI's [adaptive filtering](https://cloud.google.com/alloydb/docs/ai/adaptive-filtering) for filtered vector searches now dynamically switches between pre-filtering and inline filtering. This enhancement further optimizes query performance by allowing the query optimizer to dynamically choose the most efficient filtering strategy. For more information, see [Activate adaptive filtering in AlloyDB AI](https://cloud.google.com/alloydb/docs/ai/activate-adaptive-filtering).
* AlloyDB AI now [integrates ScaNN indexes with the columnar engine](https://cloud.google.com/alloydb/docs/columnar-engine/configure#configure-index-cache). You can now accelerate your vector similarity search by [loading ScaNN indexes into the columnar engine](https://cloud.google.com/alloydb/docs/columnar-engine/manage-content-manually#manage-index-cache).
* The `alloydb_scann` extension now provides a satisfy limit feature that improves query recall for vector searches. If a search returns fewer results than specified in the `LIMIT` clause, the scan continues until the `LIMIT` is met or a configured upper bound is reached. To enable this feature, set the [`scann.satisfy_limit`](https://cloud.google.com/alloydb/docs/reference/ai/scann-index-reference#scann-satisfy-limit) flag to `relaxed order`. You can also use the [`scann.max_pct_leaves_to_search`](https://cloud.google.com/alloydb/docs/reference/ai/scann-index-reference#scann-max-pct-leaves-to-search) flag to configure the upper bound for the search.
* You can enable vector search index recommendations for Scalable Nearest Neighbors (ScaNN) indexes using the AlloyDB index advisor. For more information, see [Use the AlloyDB index advisor with query insights](https://cloud.google.com/alloydb/docs/use-index-advisor-with-query-insights#enable-extensions) or [View the index advisor's index recommendations](https://cloud.google.com/alloydb/docs/use-index-advisor#view-recommendations).
* You can configure automatic index maintenance using the following flags:

  + [`scann.max_background_workers`](https://cloud.google.com/alloydb/docs/reference/alloydb-flags#scann.max_background_workers) flag to control the number of background workers and increase throughput across multiple indexes.
  + [`scann.maintenance_background_naptime_s`](https://cloud.google.com/alloydb/docs/reference/alloydb-flags#scann.maintenance_background_naptime_s) flag to control the minimum delay between maintenance runs.

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
