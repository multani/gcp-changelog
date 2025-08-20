# Dataproc

## 2025-08-19

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.0.146-debian10, 2.0.146-ubuntu18, 2.0.146-rocky8,
* 2.1.95-debian11, 2.1.95-ubuntu20, 2.1.95-ubuntu20-arm, 2.1.95-rocky8
* 2.2.63-debian12, 2.2.63-ubuntu22, 2.2.63-ubuntu22-arm, 2.2.63-rocky9
* 2.3.9-debian12, 2.3.9-ubuntu22, 2.3.9-ubuntu22-arm, 2.3.9-ml-ubuntu22, 2.3.9-rocky9

---
## 2025-08-14

### Announcement

New [Dataproc Serverless for Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.2.57
* 2.2.57
* 2.3.8

---
## 2025-08-12

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.0.145-debian10, 2.0.145-ubuntu18, 2.0.145-rocky8,
* 2.1.94-debian11, 2.1.94-ubuntu20, 2.1.94-ubuntu20-arm, 2.1.94-rocky8
* 2.2.62-debian12, 2.2.62-ubuntu22, 2.2.62-ubuntu22-arm, 2.2.62-rocky9
* 2.3.8-debian12, 2.3.8-ubuntu22, 2.3.8-ubuntu22-arm, 2.3.8-ml-ubuntu22, 2.3.8-rocky9

### Announcement

New [Dataproc Serverless for Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.2.56
* 2.2.56
* 2.3.7

### Feature

**Dataproc on Compute Engine: Image versions `2.2` and `2.3`**: The [Iceberg optional component](https://cloud.google.com/dataproc/docs/concepts/components/iceberg) supports the BigLake Iceberg REST catalog.

### Feature

**Dataproc on Compute Engine**: **[Sharing checkpoint diagnostic data:](https://cloud.google.com/dataproc/docs/support/diagnose-clusters#enable_and_share_checkpoint_diagnostic_data)** Setting the [`dataproc:diagnostic.capture.access=GOOGLE_DATAPROC_DIAGNOSE`](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/cluster-properties#dataproc_service_properties_table) property during cluster creation shares all of the [temp bucket](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket) contents with Google Cloud support if [uniform bucket-level access](https://cloud.google.com/storage/docs/uniform-bucket-level-access) is enabled on temp bucket. If object-level access control is in effect on the temp bucket, only the [checkpoint diagnostic data folder](https://cloud.google.com/dataproc/docs/support/diagnose-clusters#checkpoint_data_location) corresponding to the cluster in Cloud Storage is shared.

---
## 2025-08-11

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.1.93-debian11, 2.1.93-rocky8, 2.1.93-ubuntu20, 2.1.93-ubuntu20-arm
* 2.2.61-debian12, 2.2.61-rocky9, 2.2.61-ubuntu22

---
## 2025-07-31

### Announcement

New [Dataproc Serverless for Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.1.111
* 1.2.55
* 2.2.55
* 2.3.6

### Announcement

**Dataproc Serverless for Spark:** Subminor version `1.1.111` is the last release of runtime version [`1.1`](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions#unsupported-dataproc-serverless-for-spark-runtime-versions), which will no longer be supported and will not receive new releases.

---
## 2025-07-25

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

`2.3.7-debian12`, `2.3.7-ubuntu22`, `2.3.7-ml-ubuntu22`, and `2.3.7-rocky9`.

The `2.3.7-ml-ubuntu22` image extends the 2.3 base image with [ML-specific libraries](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.3#image_version_23_machine_learning_ml_components).

---
## 2025-07-15

### Announcement

**Dataproc on Compute Engine:** Starting August 18, 2025, the following diagnostic properties will be enabled by default for newly created Dataproc clusters:

* `dataproc:diagnostic.capture.enabled`: Enables the collection of [checkpoint data](https://cloud.google.com/dataproc/docs/support/diagnose-clusters#checkpoint_data) in the cluster [temp bucket](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket).
* `dataproc:dataproc.logging.extended.enabled`: Enables the collection of logs for the [Knox, Zeppelin, Ranger-usersync, Jupyter\_notebook, Jupyter\_kernel\_gateway components](https://cloud.google.com/dataproc/docs/concepts/components/overview) and the [Spark History-Server](https://cloud.google.com/dataproc/docs/concepts/jobs/history-server) in [Cloud Logging](https://cloud.google.com/dataproc/docs/guides/logging#cluster_logs_in).
* `dataproc:dataproc.logging.syslog.enabled`: Enables the collection of VM syslogs in [Cloud Logging](https://cloud.google.com/dataproc/docs/guides/logging#cluster_logs_in).

  To continue using the [Ops Agent](https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) initialization action [`opsagent.sh`](https://github.com/GoogleCloudDataproc/initialization-actions/blob/main/opsagent/opsagent.sh) to ingest syslogs from Dataproc cluster nodes, do one of the following:

  + Recommended: Use [`opsagent_nosyslog.sh`](https://github.com/GoogleCloudDataproc/initialization-actions/blob/main/opsagent/opsagent_nosyslog.sh) since
    VM syslogs will now be emitted by default from Dataproc clusters.
  + Set the `dataproc:dataproc.logging.syslog.enabled=false` and continue using [`opsagent.sh`](https://github.com/GoogleCloudDataproc/initialization-actions/blob/main/opsagent/opsagent.sh)
    to ingest syslogs.

**Note:** To disable any of these features, set the corresponding property to `false` during cluster creation.

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

`2.3.6-debian12`, `2.3.6-ubuntu22`, `2.3.6-ml-ubuntu22`, and `2.3.6-rocky9`.

The `2.3.6-ml-ubuntu22` image extends the 2.3 base image with [ML-specific libraries](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.3#image_version_23_machine_learning_ml_components).

### Feature

Dataproc now allows Dynamic update of [multi-tenancy clusters](https://cloud.google.com/dataproc/docs/concepts/iam/sa-multi-tenancy#create_a_secure_multi-tenancy_cluster).

---
## 2025-07-07

### Feature

The [Cluster Scheduled Stop](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/scheduled-stop) feature is available in [preview](https://cloud.google.com/products#product-launch-stages). You can use this feature to stop clusters after a specified idle period, at a specified future time, or after a specified period from the cluster creation or update request.

---
## 2025-07-04

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

`2.3.5-debian12`, `2.3.5-ubuntu22`, `2.3.5-ml-ubuntu22`, and `2.3.5-rocky9`.

The `2.3.5-ml-ubuntu22` image extends the 2.3 base image with [ML-specific libraries](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.3#image_version_23_machine_learning_ml_components).

### Changed

[**Serverless for Apache Spark**](https://cloud.google.com/dataproc-serverless/docs) (formerly known as **Dataproc Serverless for Spark**) now supports [OS Login organization policy](https://cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#set-org-policy). Organizations, folders, and projects that enforce the OS Login policy can now use Serverless for Apache Spark.

---
## 2025-07-01

### Announcement

New [Dataproc Serverless for Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.1.110
* 1.2.54
* 2.2.54
* 2.3.5

---
## 2025-06-20

### Announcement

New [Dataproc Serverless for Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.1.109
* 1.2.53
* 2.2.53
* 2.3.4

### Changed

**Dataproc Serverless for Spark:** Upgraded the Cloud Storage connector version to `2.2.28` in the `1.1` runtime.

### Changed

**Dataproc Serverless for Spark:** The built-in Iceberg now supports the BigLake Iceberg REST catalog on the `2.2` runtime.

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters#supported_dataproc_versions):

* 2.0.144-debian10, 2.0.144-rocky8, 2.0.144-ubuntu18
* 2.1.92-debian11, 2.1.92-rocky8, 2.1.92-ubuntu20, 2.1.92-ubuntu20-arm
* 2.2.60-debian12, 2.2.60-rocky9, 2.2.60-ubuntu22
* 2.3.4-debian12, 2.3.4-rocky9, 2.3.4-ubuntu22

### Changed

**Dataproc on Compute Engine:** Upgraded the Cloud Storage connector version to `2.2.28` in the latest `2.0` and `2.1` images.

### Changed

**Dataproc on Compute Engine:** Dataproc now automatically configures Knox Gateway configuration properties `gateway.dispatch.whitelist.services` and `gateway.dispatch.whitelist` for component web UIs within the cluster.

### Fixed

**Dataproc on Compute Engine:** Fixed a bug in `trino-jvm cluster properties`. To configure Trino JVM options prefixed with `trino-jvm`, follow these guidelines:

* Configure JVM options starting with `-XX:`, without `:`. For JVM flags without a value, add `=` at the end. For example, add `trino-jvm:-XX+HeapDumpOnOutOfMemoryError=` as -`XX:+HeapDumpOnOutOfMemoryError` in the `jvm.config`.
* Specify JVM options system properties with a `-D` prefix the same way. For example, `trino-jvm:-Dsystem.property.name=value`.
* Any value containing `:` cannot be provided as a cluster property.

### Fixed

**Dataproc on Compute Engine & Dataproc Serverless:** Backported [GH-3198](https://github.com/apache/parquet-java/pull/3199) in Parquet addressing [CVE-2025-46762](https://nvd.nist.gov/vuln/detail/cve-2025-46762).

---
## 2025-06-10

### Announcement

New [Dataproc Serverless for Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.1.108
* 1.2.52
* 2.2.52
* 2.3.3

---
## 2025-06-09

### Announcement

Announcing the GA release of [Dataproc on Compute Engine image version 2.3](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.3):

Image Version 2.3 is a lightweight image that contains only core components, reducing exposure to Common Vulnerabilities and Exposures (CVEs). For higher security compliance requirements, use the image version 2.3 or later when creating a Dataproc cluster. Optional components can still be deployed on-demand.

The following images are the latest available `2.3` subminor image versions:

* `2.3.3-debian12`, `2.3.3-rocky9`, and `2.3.3-ubuntu22`

`2.3` images include the components listed in [2.3.x release versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.3).

---
## 2025-06-06

### Announcement

New [Dataproc Serverless for Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.1.107
* 1.2.51
* 2.2.51
* 2.3.2

### Fixed

**Dataproc Serverless for Spark:** Fixed a bug that prevented the `spark.executorEnv` property from correctly setting specific executor environment variables across all runtimes.

---
## 2025-06-01

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters#supported_dataproc_versions):

* 2.0.143-debian10, 2.0.143-rocky8, 2.0.143-ubuntu18
* 2.1.91-debian11, 2.1.90-rocky8, 2.1.91-ubuntu20, 2.1.91-ubuntu20-arm
* 2.2.59-debian12, 2.2.59-rocky9, 2.2.59-ubuntu22

### Fixed

**Dataproc on Compute Engine**: Fixed the ordering of log entries generated from clusters created with `2.2+` image versions by assigning timestamps closer to the log generation time.

---
## 2025-05-30

### Announcement

New [Dataproc Serverless for Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.1.106
* 1.2.50
* 2.2.50
* 2.3.1

### Announcement

The support dates for **Dataproc on Compute Engine** image versions `2.0`, `2.1`, and `2.2` have been extended, as follows:

* Image version `2.2`: Supported until 03/31/2027
* Image version `2.1`: Supported until 03/31/2026
* Image version `2.0` Supported until 09/30/2025

---
## 2025-05-28

### Announcement

Announcing the [General Availability](https://cloud.google.com/products#product-launch-stages) release of **Spark on BigQuery**, which lets you create a serverless Spark session in a [BigQuery Studio](https://cloud.google.com/bigquery/docs/query-overview#bigquery-studio) notebook. Use this feature to create, run, and test Spark jobs quickly and easily. For more information, see [Run PySpark code in BigQuery Studio notebooks](https://cloud.google.com/bigquery/docs/use-spark).

### Announcement

New [Dataproc Serverless for Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.1.105
* 1.2.49
* 2.2.49
* 2.3.0

### Announcement

Announcing the [General Availability (GA)](https://cloud.google.com/products#product-launch-stages) release of Dataproc Serverless for Spark runtime versions [2.3](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/spark-runtime-versions#spark_runtime_version_23), which include the following components:

* Spark 3.5.1
* BigQuery Spark Connector 0.42.3
* Cloud Storage Connector 3.1.2
* Java 17
* Python 3.11
* R 4.3
* Scala 2.13

---
