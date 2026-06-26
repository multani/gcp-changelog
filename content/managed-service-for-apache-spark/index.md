# Managed Service for Apache Spark

## 2026-06-22

### Breaking

**Managed Service for Apache Spark** (formerly Dataproc on Compute Engine):
The following new subminor image versions, `1.3.96`, `1.4.81`, `1.5.92`, `2.0.161`, and `2.3.32`,
don't have preconfigured Conda channels, and are not mapped to default aliases
(such as `2.3-debian12` and `2.3-ubuntu22`) until August 25, 2026.
The new 2.1 and 2.2 subminor images continue to have preconfigured Conda channels,
but note the following **Default change schedule:**, which will impact all supported
image versions.

* **Impact:** When creating clusters with these image versions, specify the exact subminor version (for example, `2.3.32-debian12`). Packages cannot be installed using Conda unless channels are manually configured during cluster initialization.
* **Mitigation:** If your workloads require preconfigured Conda channels or default aliases, pin your clusters to the previous image versions.
* **Default change schedule:** The subminor versions `1.3.96`, `1.4.81`, `1.5.92`, and `2.0.161` will become default after August 25, 2026.
  Additionally, newer subminor versions for `2.1`, `2.2`, and `2.3` released after August 25, 2026 will not have preconfigured Conda channels and will be mapped to default aliases.
  All workloads must use new images after August 25, 2026
  since the use of prior subminor versions with preconfigured conda
  channels will be disallowed.

### Announcement

New [**Managed Service for Apache Spark** (formerly Dataproc on Compute Engine) subminor cluster image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-version-lists#supported-dataproc-image-versions):

* 1.3.96-debian10, 1.3.96-ubuntu18
* 1.4.81-debian10, 1.4.81-ubuntu18
* 1.5.92-debian10, 1.5.92-rocky8, 1.5.92-ubuntu18
* 2.0.161-debian10, 2.0.161-rocky8, 2.0.161-ubuntu18
* 2.1.115-debian11, 2.1.115-rocky8, 2.1.115-ubuntu20, 2.1.115-ubuntu20-arm
* 2.1.116-debian11, 2.1.116-rocky8, 2.1.116-ubuntu20, 2.1.116-ubuntu20-arm
* 2.2.83-debian12, 2.2.83-rocky9, 2.2.83-ubuntu22, 2.2.83-ubuntu22-arm
* 2.2.84-debian12, 2.2.84-rocky9, 2.2.84-ubuntu22, 2.2.84-ubuntu22-arm
* 2.3.31-debian12, 2.3.31-ml-ubuntu22, 2.3.31-rocky9, 2.3.31-ubuntu22, 2.3.31-ubuntu22-arm
* 2.3.32-debian12, 2.3.32-ml-ubuntu22, 2.3.32-rocky9, 2.3.32-ubuntu22, 2.3.32-ubuntu22-arm

### Announcement

**Managed Service for Apache Spark** (formerly Dataproc on Compute Engine):
Key updates in these image versions include:

* **Iceberg support**: Added support for Iceberg 1.10 in Dataproc 2.3 images. This change only applies to 2.3 clusters created with the `ICEBERG` optional component. Users can opt-in to Iceberg 1.10 by setting the `dataproc:dataproc.iceberg.version` cluster property to `1.10` during cluster creation.
* **Spark optimizations**: Enabled Spark skewed-join and self-join optimizations by default in new GCE image versions.
* **Scheduler exitTimeout**: Configured `spark.scheduler.listenerbus.exitTimeout` to 30s for Compute Engine deployments.

---
## 2026-06-16

### Announcement

**Managed Service for Apache Spark** (formerly Dataproc on Compute Engine): Rollout of the [new sub-minor versions without pre-configured channels](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions) will begin on June 22, 2026, delayed from the previously planned date of June 15, 2026 ETA.

---
## 2026-05-29

### Announcement

**Managed Service for Apache Spark** (formerly Dataproc on Compute Engine):
Added support for selecting specific [Confidential Computing](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/confidential-compute) technologies (AMD SEV, AMD SEV-SNP, Intel TDX) when creating clusters using the new `--confidential-compute-type` flag in `gcloud` and the `confidentialInstanceType` field in the API. The boolean `--enable-confidential-compute` flag is now deprecated but will continue to function, defaulting to AMD SEV for backward compatibility.

* Introduced `confidentialInstanceType` enum in the [API](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#confidentialinstanceconfig).
* The `--enable-confidential-compute` flag and `enableConfidentialCompute` field are deprecated in favor of the new type-specific flag/field.
* Clusters created with the deprecated boolean flag will default to `SEV`.
* Added validation for machine type compatibility for `SEV`, `SEV-SNP`, and `TDX`.
* Updated live migration logic to support compatible machine types and CPU platforms for each technology, including N2D and C3D for SEV.

---
## 2026-05-25

### Announcement

**Managed Service for Apache Spark** (formerly Dataproc on Compute Engine): The following subminor image versions announced on [May 19, 2026](https://docs.cloud.google.com/managed-spark/docs/release-notes#May_19_2026) have been rolled back:

* 2.2.82-debian12, 2.2.82-rocky9, 2.2.82-ubuntu22, 2.2.82-ubuntu22-arm

---
## 2026-05-19

### Announcement

New [**Managed Service for Apache Spark** (formerly Dataproc on Compute Engine) subminor cluster image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-version-lists#supported-dataproc-image-versions):

* 2.1.114-debian11, 2.1.114-rocky8, 2.1.114-ubuntu20, 2.1.114-ubuntu20-arm
* 2.2.82-debian12, 2.2.82-rocky9, 2.2.82-ubuntu22, 2.2.82-ubuntu22-arm
* 2.3.30-debian12, 2.3.30-ml-ubuntu22, 2.3.30-rocky9, 2.3.30-ubuntu22, 2.3.30-ubuntu22-arm

**Rollback Notice:** The `2.2.82` image versions were rolled back on [May 25, 2026](https://cloud.google.com/managed-spark/docs/release-notes#May_25_2026).

### Breaking

**Managed Service for Apache Spark** (formerly Dataproc on Compute Engine):
The configuration for Spark shuffle partitions (`spark.sql.shuffle.partitions`) has changed from an integer to a string type.

This change impacts image versions `2.3.30` and later in version `2.3`, and `2.2.82` and later in version `2.2`.

* **Impact:** This change only affects users who are programmatically setting the configuration in code using `spark.conf.set()` with an integer literal.
  + **Impacted example:** `spark.conf.set("spark.sql.shuffle.partitions", 100)`
* **User action:** Update your code to pass a string literal instead of an integer.
  + **Example fix:** `spark.conf.set("spark.sql.shuffle.partitions", "100")`
* **Not impacted:** Setting the configuration via command-line arguments (e.g., `spark-submit --conf spark.sql.shuffle.partitions=100`), properties files, or Spark SQL commands (`spark.sql("SET spark.sql.shuffle.partitions=100")`) remains unaffected, as these methods naturally parse the input as strings.

---
## 2026-05-11

### Announcement

New [**Managed Service for Apache Spark** (formerly Google Cloud Serverless for Apache Spark) subminor runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions):

* 1.2.80
* 2.2.80
* 2.3.33

---
## 2026-05-03

### Announcement

New [**Managed Service for Apache Spark** (formerly Dataproc on Compute Engine) subminor cluster image versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions) for 3.0 (Preview):

* 3.0.0-RC2-debian13, 3.0.0-RC2-ml-ubuntu24, 3.0.0-RC2-rocky9, 3.0.0-RC2-ubuntu24

**Key updates in this release**:

* The debian image for 3.0 is upgraded to **Debian 13**.
* The default Java runtime is upgraded to **Java 21**.
* Apache Hadoop upgraded to **3.5.0**.
* Apache Spark upgraded to **4.1.1**.
* Apache Hive upgraded to **4.2.0**.
* Trino upgraded to **480**.
* Apache Solr upgraded to **9.10.1**.
* Apache Kafka upgraded to **3.9.2**.
* Docker upgraded to **28.1**.
* Apache Flink upgraded to **2.2.0**.
* Scala upgraded to **2.13.17**.
* Cloud Storage Connector upgraded to **3.1.13**.
* Apache Zookeeper upgraded to **3.9.5**.
* BigQuery Connector upgraded to **0.44.1-Preview**.
* Zeppelin Notebook upgraded to **0.12.0**.
* JupyterLab upgraded to **4.5.7**.
* **[Pixi](https://pixi.prefix.dev)** is used as python package manager instead of conda.

### Announcement

New [**Managed Service for Apache Spark** (formerly Google Cloud Serverless for Apache Spark) subminor runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions):

* 1.2.79
* 2.2.79
* 2.3.32

**Key updates in this release**:

* Upgraded Metastore Proxy version to `v0.0.79`.
* Upgraded Spark RAPIDS to version `26.04.0` version in the Managed Service
  for Apache Spark version `3.0` serverless runtime.

---
## 2026-04-27

### Announcement

New [**Managed Service for Apache Spark** (formerly Dataproc on Compute Engine) subminor cluster image versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions):

* 2.1.113-debian11, 2.1.113-rocky8, 2.1.113-ubuntu20, 2.1.113-ubuntu20-arm
* 2.2.81-debian12, 2.2.81-rocky9, 2.2.81-ubuntu22, 2.2.81-ubuntu22-arm
* 2.3.29-debian12, 2.3.29-ml-ubuntu22, 2.3.29-rocky9, 2.3.29-ubuntu22, 2.3.29-ubuntu22-arm

---
