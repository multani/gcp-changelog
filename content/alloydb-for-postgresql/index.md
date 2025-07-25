# AlloyDB for PostgreSQL

## 2025-07-23

### Announcement

[AlloyDB Omni](https://cloud.google.com/alloydb/omni/current/docs)
version 16.8.0 is generally available
([GA](https://cloud.google.com/products#product-launch-stages)). Version 16.8.0
includes the following features and changes:

* AlloyDB Omni supports PostgreSQL version
  [16.8](https://www.postgresql.org/docs/release/16.8/).
* AlloyDB Omni supports the
  [`pg_squeeze`](/alloydb/omni/current/docs/reference/extensions) extension
  that addresses table bloat and improves data locality.
* You can set up the columnar engine storage cache on dedicated devices. For
  more information, see
  [Configure the columnar engine in AlloyDB Omni](/alloydb/omni/16.8.0/docs/columnar-engine/configure).
* [Improved I/O acceleration](/alloydb/omni/16.8.0/docs/improve-database-performance-using-io-acceleration)
  due to bug fixes in `libaio`.
* [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) authentication integration is generally available ([GA](https://cloud.google.com/products#product-launch-stages)), providing robust user authentication for your database clusters. For more information, see [Integrate Active Directory with AlloyDB Omni](/alloydb/omni/16.8.0/docs/integrate-active-directory).
* Active Directory group-based authorization is available in [Preview](https://cloud.google.com/products#product-launch-stages), enabling granular permission management based on your Active Directory groups. For more information, see [Integrate Active Directory group support with AlloyDB Omni](/alloydb/omni/16.8.0/docs/integrate-ad-group-support-alloydb-omni).

### Announcement

[AlloyDB Omni](https://cloud.google.com/alloydb/omni/current/docs)
version 15.12.0 is generally available
([GA](https://cloud.google.com/products#product-launch-stages)). Version 15.12.0
includes the following features and changes:

* AlloyDB Omni supports PostgreSQL version
  [15.12](https://www.postgresql.org/docs/release/15.12/).
* AlloyDB Omni supports the
  [`pg_squeeze`](/alloydb/omni/current/docs/reference/extensions) extension
  that addresses table bloat and improves data locality.
* You can set up the columnar engine storage cache on dedicated devices. For
  more information, see
  [Configure the columnar engine in AlloyDB Omni](/alloydb/omni/15.12.0/docs/columnar-engine/configure).

### Announcement

The [AlloyDB Omni Kubernetes operator](/alloydb/omni/current/docs/deploy-kubernetes) version 1.5.0 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) and includes the following features and bug fixes:

* You can install the operator using the [Operator Lifecycle Manager (OLM)](https://olm.operatorframework.io/) for Kubernetes and OpenShift environments. See "Install the AlloyDB Omni operator" for AlloyDB Omni [15.12.0](/alloydb/omni/15.12.0/docs/deploy-kubernetes#olm) and [16.8.0](/alloydb/omni/16.8.0/docs/deploy-kubernetes#olm) for details.
* Low downtime, minor version upgrades for a database cluster in a high availability setup are available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see "Perform a minor database version upgrade for AlloyDB Omni on Kubernetes" in the documentation for AlloyDB Omni [15.12.0](/alloydb/omni/15.12.0/docs/upgrade-kubernetes-database-minor-version) and [16.8.0](/alloydb/omni/16.8.0/docs/upgrade-kubernetes-database-minor-version).
* [Active Directory](https://en.wikipedia.org/wiki/Active_Directory) authentication integration on your Kubernetes-based AlloyDB Omni database cluster is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Integrate Active Directory with AlloyDB Omni on Kubernetes](/alloydb/omni/16.8.0/docs/integrate-active-directory-kubernetes-operator).
* Active Directory group-based authorization on your Kubernetes-based AlloyDB Omni database cluster is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integrate Active Directory group support on Kubernetes](/alloydb/omni/16.8.0/docs/integrate-ad-group-support-kubernetes-operator).
* You can configure backups to be taken directly from a standby Kubernetes cluster in a high availability (HA) setup to offload backup operations from your primary instance. See "Backup and restore in Kubernetes" for AlloyDB Omni [15.12.0](/alloydb/omni/15.12.0/docs/backup-kubernetes) and [16.8.0](/alloydb/omni/16.8.0/docs/backup-kubernetes) for details.
* The operator fully automatically replicates replication slots for cross-data-center replication to work with primary database clusters that have high availability (HA) enabled. You still need to make sure you have reliable and low latency network connectivity between the primary and secondary data centers, which is crucial for cross-data-center replication to function effectively. For more information, see "Work with cross-data-center replication" for AlloyDB Omni [15.12.0](/alloydb/omni/15.12.0/docs/cross-data-center-replication/work-with-cross-data-center-replication) and [16.8.0](/alloydb/omni/16.8.0/docs/cross-data-center-replication/work-with-cross-data-center-replication).
* AlloyDB Omni Kubernetes images are now built on Red Hat's Universal Base Image (UBI) 9. For more information, see "Install AlloyDB Omni on Kubernetes" for AlloyDB Omni [15.12.0](/alloydb/omni/15.12.0/docs/deploy-kubernetes#base-image) and [16.8.0](/alloydb/omni/16.8.0/docs/deploy-kubernetes#base-image).
* AlloyDB AI requires AlloyDB Omni version 15.5.5 or later.

### Issue

When upgrading your AlloyDB Omni database clusters, be aware of specific upgrade paths and prerequisites depending on your current `controlPlaneAgentsVersion` and environment:

* If your database cluster's `controlPlaneAgentsVersion` is `1.0.0`, you must first upgrade to `1.1.1` before you upgrade to `1.5.0` or higher. You can directly upgrade database clusters with `controlPlaneAgentsVersion` `1.1.0` or later to `1.5.0`.
* If you use an OpenShift database cluster that runs `controlPlaneAgentsVersion` `1.4.1` or earlier, you must run prerequisite steps before updating to `1.5.0`. For more information, see "Update OpenShift database clusters from version `1.4.1` or earlier" for AlloyDB Omni [15.12.0](/alloydb/omni/15.12.0/docs/upgrade-kubernetes-operator-version#update-openshift) and [16.8.0](/alloydb/omni/16.8.0/docs/upgrade-kubernetes-operator-version#update-openshift).

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
