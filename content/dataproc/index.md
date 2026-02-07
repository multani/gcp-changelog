# Dataproc

## 2026-02-06

### Announcement

New [Serverless for Apache Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.2.69
* 2.2.69
* 2.3.22
* 3.0.5

### Feature

**Serverless for Apache Spark:** Added support for removing `conscrypt`
from Serverless for Apache Spark `2.3`+ runtimes using the
[`dataproc.artifacts.remove`](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/properties#other_properties)
property .

---
## 2026-02-05

### Fixed

Fixed the `spark.driver.extraClassPath` delimiter for the Jupyter SparkMonitor Listener.

### Feature

Added a new `dataproc:pypi.repository` property to customize the PyPI repository used for pip. The value can be a URL, or `google` to use a Google-hosted cache of PyPI, accessible without public internet connectivity. Starting in image version 3.1, `google` will be the default; to opt out and return to public PyPI, use the value `pypi`.

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions):

* 2.0.158-debian10, 2.0.158-ubuntu18, 2.0.158-rocky8
* 2.1.107-debian11, 2.1.107-ubuntu20, 2.1.107-ubuntu20-arm, 2.1.107-rocky8
* 2.2.75-debian12, 2.2.75-ubuntu22, 2.2.75-ubuntu22-arm, 2.2.75-rocky9
* 2.3.22-debian12, 2.3.22-ml-ubuntu22, 2.3.22-rocky9, 2.3.22-ubuntu22, 2.3.22-ubuntu22-arm

### Feature

Parquet CLI version upgraded to 1.15.2 in 2.1 and 2.2 images.

### Fixed

Fixed a bug in the ARM image that prevented connecting to a Dataproc Metastore instance with a gRPC protocol endpoint.

### Feature

Apache Pig is now available in ARM images.

### Feature

Delta subminor version upgraded to 3.2.1 in Dataproc on Compute Engine image 2.2 and 2.3.

### Change

Removed use of deprecated Hadoop configuration properties `fs.default.name` and `yarn.resourcemanager.system-metrics-publisher.enabled`.

---
## 2026-02-04

### Announcement

**Upcoming Spark data lineage changes** See the upcoming May,
2026 Dataproc and Serverless for Apache Spark release notes for an announcement
of a change that will automatically enable
[Dataproc Spark data lineage](https://docs.cloud.google.com/dataproc/docs/guides/spark-lineage) and
[Serverless for Apache Spark data lineage](https://docs.cloud.google.com/dataproc-serverless/docs/guides/data-lineage)
when you enable the Data Lineage API (see
[Control lineage ingestion for a service](https://docs.cloud.google.com/dataplex/docs/use-lineage#control-ingestion))
without requiring additional project, cluster, batch workload, or
interactive session settings.

---
## 2026-01-30

### Announcement

New [Serverless for Apache Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 3.0.4

### Announcement

**Dataproc on Compute Engine:** The following subminor image versions announced on [January 24, 2026](https://docs.cloud.google.com/dataproc/docs/release-notes#January_24_2026) have been rolled back:

* 2.0.157-debian10, 2.0.157-ubuntu18, 2.0.157-rocky8
* 2.1.106-debian11, 2.1.106-ubuntu20, 2.1.106-ubuntu20-arm, 2.1.106-rocky8
* 2.2.74-debian12, 2.2.74-ubuntu22, 2.2.74-ubuntu22-arm, 2.2.74-rocky9
* 2.3.21-debian12, 2.3.21-ml-ubuntu22, 2.3.21-rocky9, 2.3.21-ubuntu22, 2.3.21-ubuntu22-arm

---
## 2026-01-24

### Feature

Upgraded the Delta subminor version to `3.2.1` in images `2.2` and `2.3`.

### Fixed

Fixed a bug in the ARM image that prevented connecting to a Dataproc Metastore instance with a
gRPC protocol endpoint.

### Fixed

Fixed the `spark.driver.extraClassPath` delimiter for the Jupyter SparkMonitor Listener.

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions):

* 2.0.157-debian10, 2.0.157-ubuntu18, 2.0.157-rocky8
* 2.1.106-debian11, 2.1.106-ubuntu20, 2.1.106-ubuntu20-arm, 2.1.106-rocky8
* 2.2.74-debian12, 2.2.74-ubuntu22, 2.2.74-ubuntu22-arm, 2.2.74-rocky9
* 2.3.21-debian12, 2.3.21-ml-ubuntu22, 2.3.21-rocky9, 2.3.21-ubuntu22, 2.3.21-ubuntu22-arm

**Rollback Notice:** These image versions were rolled back on [January 30, 2026](https://docs.cloud.google.com/dataproc/docs/release-notes#January_30_2026).

### Feature

Added a new `dataproc:pypi.repository` property to customize the PyPI repository that `pip` uses.
The value can be a internet-accessible URL, or you can specify `google` to use a Google-hosted cache of PyPI, which
is accessible without public internet connectivity. Starting with Dataproc image version
`3.1`, `google` will be the default (you can specify the `pypi` property value to use public PyPI instead of the default `google` 3.1 value).

### Feature

Apache Pig is now available in ARM images.

### Change

Removed the use of deprecated Hadoop configuration properties `fs.default.name` and
`yarn.resourcemanager.system-metrics-publisher.enabled`.

---
## 2026-01-23

### Fixed

* Applied patch for [SPARK-48292](https://issues.apache.org/jira/browse/SPARK-48292) in Serverless for Apache Spark [1.2](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/versions/spark-runtime-1.2) and [2.2](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/versions/spark-runtime-2.2) runtimes.

### Announcement

New [Serverless for Apache Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.2.67
* 2.2.67
* 2.3.20
* 3.0.3

---
## 2026-01-13

### Announcement

**Dataproc on Compute Engine:** The following subminor image versions announced on [January 06, 2026](https://docs.cloud.google.com/dataproc/docs/release-notes#January_06_2026) have been rolled back:

* 2.0.156-debian10, 2.0.156-ubuntu18, 2.0.156-rocky8
* 2.1.105-debian11, 2.1.105-ubuntu20, 2.1.105-ubuntu20-arm, 2.1.105-rocky8
* 2.2.73-debian12, 2.2.73-ubuntu22, 2.2.73-ubuntu22-arm, 2.2.73-rocky9
* 2.3.20-debian12, 2.3.20-ml-ubuntu22, 2.3.20-rocky9, 2.3.20-ubuntu22, 2.3.20-ubuntu22-arm

---
## 2026-01-09

### Announcement

New [Serverless for Apache Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.2.66
* 2.2.66
* 2.3.19
* 3.0.1

---
## 2026-01-06

### Change

Removed use of deprecated Hadoop configuration properties `fs.default.name` and `yarn.resourcemanager.system-metrics-publisher.enabled`.

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions):

* 2.0.156-debian10, 2.0.156-ubuntu18, 2.0.156-rocky8
* 2.1.105-debian11, 2.1.105-ubuntu20, 2.1.105-ubuntu20-arm, 2.1.105-rocky8
* 2.2.73-debian12, 2.2.73-ubuntu22, 2.2.73-ubuntu22-arm, 2.2.73-rocky9
* 2.3.20-debian12, 2.3.20-ml-ubuntu22, 2.3.20-rocky9, 2.3.20-ubuntu22, 2.3.20-ubuntu22-arm

**Rollback Notice:** These image versions were rolled back on [January 13, 2026](https://docs.cloud.google.com/dataproc/docs/release-notes#January_13_2026).

### Fixed

Fixed the `spark.driver.extraClassPath` delimiter for the Jupyter SparkMonitor Listener.

### Feature

Added a new property `dataproc:pypi.repository` to customize the PyPI repository used for pip. The value can be a URL, or `google` to use a Google-hosted cache of PyPI, accessible without public internet connectivity. Starting in image version 3.1, `google` will be the default; to opt out and return to public PyPI, use the value `pypi`.

---
## 2025-12-22

### Announcement

New [Serverless for Apache Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.2.65
* 2.2.65
* 2.3.18

---
## 2025-12-20

### Breaking

The following **Dataproc on Compute Engine** subminor image versions,
released on [December 05, 2025](https://docs.cloud.google.com/dataproc/docs/release-notes#December_05_2025), are now **blocklisted**:

* 2.2.72-debian12, 2.2.72-ubuntu22, 2.2.72-ubuntu22-arm, 2.2.72-rocky9
* 2.3.19-debian12, 2.3.19-ubuntu22, 2.3.19-ubuntu22-arm, 2.3.19-ml-ubuntu22, 2.3.19-rocky9

---
## 2025-12-05

### Feature

`dataproc-ml` is available by default in `2.3` `-ml` images.

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions):

* 2.0.155-debian10, 2.0.155-ubuntu18, 2.0.155-rocky8
* 2.1.104-debian11, 2.1.104-ubuntu20, 2.1.104-ubuntu20-arm, 2.1.104-rocky8
* 2.2.72-debian12, 2.2.72-ubuntu22, 2.2.72-ubuntu22-arm, 2.2.72-rocky9
* 2.3.19-debian12, 2.3.19-ubuntu22, 2.3.19-ubuntu22-arm, 2.3.19-ml-ubuntu22, 2.3.19-rocky9

**Blocklist update:** The `2.2.72` and `2.3.19`
subminor image versions were blocklisted on
December 20, 2025.

---
## 2025-12-04

### Announcement

**Serverless for Apache Spark:** Runtime version [3.0](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-3.0) is now generally available. This version simplifies onboarding, improves reliability, reduces startup latency, and adds support for Spark 4.0.

* Features and improvements:

  + Regional and multi-zonal workloads are used by default to increase obtainability of compute resources
  + Faster startup than previous runtimes
  + Fast resource cleanup that allows faster release of VPC IPs after workload completion
  + End-user credentials are used for all workloads by default
  + New `bigquery` Spark catalog, pre-configured for out-of-the-box BigQuery
    native table interactions
  + New Spark Serverless-specific IAM roles
  + New `dataproc-rm.googleapis.com` API enablement is required

---
## 2025-11-22

### Change

**Dataproc on Compute Engine**: Updated Cloud Storage connector:

* Updated to `3.1.10` in image version `2.3.18`.
* Updated to `3.0.15` in image version `2.2.71`.
* Updated to `hadoop3-2.2.30` in image versions `2.1.103` and `2.0.154`.

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.0.154-debian10, 2.0.154-ubuntu18, 2.0.154-rocky8
* 2.1.103-debian11, 2.1.103-ubuntu20, 2.1.103-ubuntu20-arm, 2.1.103-rocky8
* 2.2.71-debian12, 2.2.71-ubuntu22, 2.2.71-ubuntu22-arm, 2.2.71-rocky9
* 2.3.18-debian12, 2.3.18-ubuntu22, 2.3.18-ubuntu22-arm, 2.3.18-ml-ubuntu22, 2.3.18-rocky9

---
## 2025-11-13

### Announcement

New [Serverless for Apache Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.2.62
* 2.2.62
* 2.3.15

### Feature

**Serverless for Apache Spark:** Added the
[`dataproc.artifacts.remove`](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/properties#other_properties) property,
which lets users remove default artifacts, such as `spark-bigquery-connector`,
`iceberg`, and `delta-lake` from a Serverless for Apache Spark runtime.

---
## 2025-11-07

### Announcement

**Serverless for Apache Spark:** Apache Spark upgrade to version [3.5.3](https://spark.apache.org/releases/spark-release-3-5-3.html)
for the [1.2](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/versions/spark-runtime-1.2)
and [2.2](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/versions/spark-runtime-2.2)
Serverless for Apache Spark runtime versions announced on
[October 13, 2025](https://docs.cloud.google.com/dataproc/docs/release-notes#October_13_2025)
has been rolled back.

---
## 2025-10-29

### Breaking

Dataproc on Compute Engine subminor image version
[`2.3.16`](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.3), announced on
[October 20, 2025](https://docs.cloud.google.com/dataproc/docs/release-notes#October_20_2025)
has been blocklisted and cannot be used when creating a new cluster.

---
## 2025-10-28

### Fixed

Fixed a Jupyter Kernel Gateway bug that caused failures while restarting kernels.

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.0.153-debian10, 2.0.153-ubuntu18, 2.0.153-rocky8
* 2.1.102-debian11, 2.1.102-ubuntu20, 2.1.102-ubuntu20-arm, 2.1.102-rocky8
* 2.2.70-debian12, 2.2.70-ubuntu22, 2.2.70-ubuntu22-arm, 2.2.70-rocky9
* 2.3.17-debian12, 2.3.17-ubuntu22, 2.3.17-ubuntu22-arm, 2.3.17-ml-ubuntu22, 2.3.17-rocky9

---
## 2025-10-22

### Announcement

Announcing the General Availability (GA) of [Lightning Engine for Google Cloud Serverless for Apache Spark](https://cloud.google.com/dataproc-serverless/docs/guides/lightning-engine). Lightning Engine is a [high-performance query accelerator](https://cloud.google.com/blog/products/data-analytics/introducing-lightning-engine-for-apache-spark) that delivers up to 4.3x faster performance for Spark workloads compared to open-source Spark, as measured on TPC-H-like benchmarks.

For more details on enabling Lightning Engine and its advanced features like Native Query Execution (NQE), see [the official documentation](https://cloud.google.com/dataproc-serverless/docs/guides/lightning-engine).

### Changed

**Serverless for Apache Spark:** With the Lightning Engine GA release, the property to enable [Native Query Execution (NQE) feature](https://cloud.google.com/dataproc-serverless/docs/guides/lightning-engine#native_query_execution) has been updated.

In order to use Lightning Engine, submit your jobs in the Premium tier. Under Lightning Engine, if you would like to use the NQE feature, set the new flag: [`spark.dataproc.lightningEngine.runtime=native`](https://cloud.google.com/dataproc-serverless/docs/concepts/properties#engine_and_runtime_properties). Users are encouraged to try this feature to explore the full potential of Lightning Engine.

For backward compatibility, the legacy property that was used to enable NQE `spark.dataproc.runtimeEngine=native` will continue to be honored in the existing runtimes 1.2, 2.2 and 2.3, but it's not supported in future releases (3.0+ runtimes).

---
## 2025-10-20

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.0.152-debian10, 2.0.152-ubuntu18, 2.0.152-rocky8
* 2.1.101-debian11, 2.1.101-ubuntu20, 2.1.101-ubuntu20-arm, 2.1.101-rocky8
* 2.2.69-debian12, 2.2.69-ubuntu22, 2.2.69-ubuntu22-arm, 2.2.69-rocky9
* 2.3.16-debian12, 2.3.16-ubuntu22, 2.3.16-ubuntu22-arm, 2.3.16-ml-ubuntu22, 2.3.16-rocky9

**Note:** Dataproc on Compute Engine subminor image version
[`2.3.16`](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.3)
was blocklisted on
[October, 29, 2025](https://docs.cloud.google.com/dataproc/docs/release-notes#October_29_2025),
and cannot be used when creating a new cluster.

---
## 2025-10-16

### Announcement

New [Serverless for Apache Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 3.0.0-RC6

### Changed

**Dataproc on Compute Engine**: The default image version of premium tier clusters is now **2.3**.

---
## 2025-10-14

### Fixed

Fixed startup race condition in [multi-tenant clusters](https://docs.cloud.google.com/dataproc/docs/concepts/iam/sa-multi-tenancy) using the `dataproc:pip.packages` property that could cause authentication failures while starting Jupyter notebook kernels.

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.0.151-debian10, 2.0.151-ubuntu18, 2.0.151-rocky8
* 2.1.100-debian11, 2.1.100-ubuntu20, 2.1.100-ubuntu20-arm, 2.1.100-rocky8
* 2.2.68-debian12, 2.2.68-ubuntu22, 2.2.68-ubuntu22-arm, 2.2.68-rocky9
* 2.3.15-debian12, 2.3.15-ubuntu22, 2.3.15-ubuntu22-arm, 2.3.15-ml-ubuntu22, 2.3.15-rocky9

---
## 2025-10-13

### Announcement

**Serverless for Apache Spark:** Runtimes rollout with Apache Spark upgrade to version [3.5.3](https://spark.apache.org/releases/spark-release-3-5-3.html) in the latest [1.2](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/versions/spark-runtime-1.2) and [2.2](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/versions/spark-runtime-2.2) Serverless for Apache Spark runtime versions has started and is expected to finish by October 16th.

---
## 2025-10-06

### Changed

**Dataproc on Compute Engine:** The following diagnostic properties are now enabled by default for new Dataproc clusters created with **2.0+** image versions:

* `dataproc:diagnostic.capture.enabled`: Collects [checkpoint diagnostic data](https://docs.cloud.google.com/dataproc/docs/support/diagnose-clusters#checkpoint_diagnostic_data) in the cluster [temp bucket](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket).
* `dataproc:dataproc.logging.extended.enabled`: Collects logs for the [Knox, Zeppelin, Ranger-usersync, Jupyter\_notebook, Jupyter\_kernel\_gateway components](https://cloud.google.com/dataproc/docs/concepts/components/overview) and the [Spark History-Server](https://docs.cloud.google.com/dataproc/docs/concepts/jobs/history-server) in [Cloud Logging](https://docs.cloud.google.com/dataproc/docs/guides/logging#cluster-logs).
* `dataproc:dataproc.logging.syslog.enabled`: Collects VM syslogs in [Cloud Logging](https://docs.cloud.google.com/dataproc/docs/guides/logging#cluster-logs).

**Note:** To disable any of these features, set the corresponding property to `false` during cluster creation.

To continue using the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) initialization action [`opsagent.sh`](https://github.com/GoogleCloudDataproc/initialization-actions/blob/main/opsagent/opsagent.sh) to ingest syslogs from Dataproc cluster nodes, do one of the following:

* **Recommended:** Use [`opsagent_nosyslog.sh`](https://github.com/GoogleCloudDataproc/initialization-actions/blob/main/opsagent/opsagent_nosyslog.sh) since
  VM syslogs are emitted by default from Dataproc clusters.
* Set the `dataproc:dataproc.logging.syslog.enabled=false` and continue using [`opsagent.sh`](https://github.com/GoogleCloudDataproc/initialization-actions/blob/main/opsagent/opsagent.sh)
  to ingest syslogs.

### Announcement

New [Serverless for Apache Spark runtime versions](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 2.3.13
* 3.0.0-RC5

### Changed

**Serverless for Apache Spark:** Upgraded Apache Spark to version [3.5.3](https://spark.apache.org/releases/spark-release-3-5-3.html) in the latest [2.3](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/versions/spark-runtime-versions#spark_runtime_version_23) Serverless for Apache Spark runtime versions.

---
## 2025-10-03

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.0.150-debian10, 2.0.150-ubuntu18, 2.0.150-rocky8
* 2.1.99-debian11, 2.1.99-ubuntu20, 2.1.99-ubuntu20-arm, 2.1.99-rocky8
* 2.2.67-debian12, 2.2.67-ubuntu22, 2.2.67-ubuntu22-arm, 2.2.67-rocky9
* 2.3.14-debian12, 2.3.14-ubuntu22, 2.3.14-ubuntu22-arm, 2.3.14-ml-ubuntu22, 2.3.14-rocky9

---
## 2025-09-15

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.0.149-debian10, 2.0.149-ubuntu18, 2.0.149-rocky8
* 2.1.98-debian11, 2.1.98-ubuntu20, 2.1.98-ubuntu20-arm, 2.1.98-rocky8
* 2.2.66-debian12, 2.2.66-ubuntu22, 2.2.66-ubuntu22-arm, 2.2.66-rocky9
* 2.3.13-debian12, 2.3.13-ubuntu22, 2.3.13-ubuntu22-arm, 2.3.13-ml-ubuntu22, 2.3.13-rocky9

---
## 2025-09-11

### Announcement

New [Serverless for Apache Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.2.61
* 2.2.61
* 2.3.12
* 3.0.0-RC4

---
## 2025-09-08

### Announcement

Announcing the [Preview release](https://cloud.google.com/products#product-launch-stages) of [Dataproc on Compute Engine image version 3.0.0-RC1](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-3.0):

* Spark 4.0.0
* Hadoop 3.4.1
* Hive 4.1.0
* Tez 0.10.5
* Cloud Storage Connector 3.1.4
* Conda 24.11
* Java 17
* Python 3.11
* R 4.3
* Scala 2.13

### Announcement

Announcing the [Preview release](https://cloud.google.com/products#product-launch-stages) of [Serverless for Apache Spark 3.0.0-RC3 runtime](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/spark-runtime-3.0):

* Spark 4.0.0
* BigQuery Spark Connector 0.42.3
* Cloud Storage Connector 3.1.5
* Conda 25.3.0
* Java 21
* Python 3.12
* R 4.4
* Scala 2.13

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.3.11-debian12, 2.3.11-ubuntu22, 2.3.11-ubuntu22-arm, 2.3.11-ml-ubuntu22, 2.3.11-rocky9

---
## 2025-09-05

### Announcement

New [Dataproc Serverless for Spark runtime versions:](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions)

* 1.2.60
* 2.2.60
* 2.3.11

---
## 2025-09-02

### Feature

[Multi-tenant clusters](https://cloud.google.com/dataproc/docs/concepts/iam/sa-multi-tenancy) are now available in Preview. Many data engineers and scientists can share a multi-tenant cluster to execute their workloads in isolation from each other.

---
## 2025-08-29

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.0.147-debian10, 2.0.147-ubuntu18, 2.0.147-rocky8
* 2.1.96-debian11, 2.1.96-ubuntu20, 2.1.96-ubuntu20-arm, 2.1.96-rocky8
* 2.2.64-debian12, 2.2.64-ubuntu22, 2.2.64-ubuntu22-arm, 2.2.64-rocky9
* 2.3.10-debian12, 2.3.10-ubuntu22, 2.3.10-ubuntu22-arm, 2.3.10-ml-ubuntu22, 2.3.10-rocky9

### Announcement

New [Dataproc Serverless for Spark runtime versions:](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions)

* 1.2.59
* 2.2.59
* 2.3.10

---
## 2025-08-22

### Announcement

New [Dataproc Serverless for Spark runtime versions](https://cloud.google.com/dataproc-serverless/docs/concepts/versions/dataproc-serverless-versions):

* 1.2.58
* 2.2.58
* 2.3.9

---
## 2025-08-21

### Fixed

**Serverless for Apache Spark:** Fixed a bug in Dataproc Batches that occasionally caused higher latency before an application was started.

---
## 2025-08-19

### Announcement

New [Dataproc on Compute Engine subminor image versions](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters):

* 2.0.146-debian10, 2.0.146-ubuntu18, 2.0.146-rocky8
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

* 2.0.145-debian10, 2.0.145-ubuntu18, 2.0.145-rocky8
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
* 2.2.61-debian12, 2.2.61-rocky9, 2.2.61-ubuntu22, 2.2.61-ubuntu22-arm

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

`2.3.7-debian12`, `2.3.7-ubuntu22`, `2.3.7-ubuntu22-arm`, `2.3.7-ml-ubuntu22`, and `2.3.7-rocky9`

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
