# AlloyDB for PostgreSQL

## 2025-06-17 00:00:00-07:00

### Feature

You can use the columnar engine to improve the performance of vector similarity
searches, specifically K-Nearest Neighbor (KNN) searches, when combined with
highly-selective predicate filtering. For more information, see
[Accelerate your filtered vector search](https://cloud.google.com/alloydb/docs/ai/perform-vector-search#accelerate-filtered-vector-search). This feature is in
[Preview](https://cloud.google.com/products#product-launch-stages).## 2025-06-02 00:00:00-07:00

### Feature

You can let [AlloyDB automatically create Private Service Connect endpoints](https://cloud.google.com/alloydb/docs/configure-private-service-connect#create_the_endpoint_automatically)
for authorized projects when you create Private Service Connect-enabled
instances, based on your defined service connection policy. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).### Feature

You can create AlloyDB clusters with [Private Services Connect](https://cloud.google.com/alloydb/docs/configure-private-service-connect#create_the_endpoint_automatically) through the Google Cloud console.## 2025-05-29 00:00:00-07:00

### Feature

You can now
[start, stop, and restart your primary and read pool AlloyDB instances](https://cloud.google.com/alloydb/docs/instance-start-stop-restart)
using the Google Cloud console and the Google Cloud CLI. This feature is
generally available
([GA](https://cloud.google.com/products#product-launch-stages)).## 2025-05-27 00:00:00-07:00

### Feature

The [AlloyDB Omni Kubernetes](/alloydb/omni/current/docs/deploy-kubernetes) operator version 1.4.1 is generally available (GA) and includes the following bug fixes:

* Fix for overriding replication related parameters. This fix lets you override the `wal_keep_size` value. For more information, see [Work with cross-data-center replication](/alloydb/omni/current/docs/cross-data-center-replication/work-with-cross-data-center-replication). This fix requires database version 15.7.1 or later.
* 63-character DBCluster names are supported, which lets you define clearer and more descriptive cluster names.
* Various bug fixes are implemented to enhance stability and the user experience.