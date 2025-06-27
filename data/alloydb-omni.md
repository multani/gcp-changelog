# AlloyDB Omni

## 2025-05-27 00:00:00-07:00

### Feature

The [AlloyDB Omni Kubernetes](/alloydb/omni/current/docs/deploy-kubernetes) operator version 1.4.1 is generally available (GA) and includes the following bug fixes:

* Fix for overriding replication related parameters. This fix lets you override the `wal_keep_size` value. For more information, see [Work with cross-data-center replication](/alloydb/omni/current/docs/cross-data-center-replication/work-with-cross-data-center-replication). This fix requires database version 15.7.1 or later.
* 63-character DBCluster names are supported, which lets you define clearer and more descriptive cluster names.
* Various bug fixes are implemented to enhance stability and the user experience.