# Bigtable

## 2025-06-30

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.61.0](https://github.com/googleapis/java-bigtable/compare/v2.60.0...v2.61.0) (2025-06-27)

##### Features

* Add getter for universe domain in JwtCredentialsWithAudience ([#2598](https://github.com/googleapis/java-bigtable/issues/2598)) ([9ad66b1](https://github.com/googleapis/java-bigtable/commit/9ad66b129923500cdeb794fc2e4570ad8b1d92fd))

##### Bug Fixes

* Add name elements for the pom.xml files ([a873719](https://github.com/googleapis/java-bigtable/commit/a873719e7e32a0cd21dc259911a193520f20797e))
* Populate table ID for materialized view ([#2610](https://github.com/googleapis/java-bigtable/issues/2610)) ([50c3fe2](https://github.com/googleapis/java-bigtable/commit/50c3fe2ffe66acaba8cb408dc3b1a4d13a4a2556))

##### Dependencies

* Update shared dependencies ([#2605](https://github.com/googleapis/java-bigtable/issues/2605)) ([4cc7246](https://github.com/googleapis/java-bigtable/commit/4cc7246ff8e2e0e26d2edc0aee8866a32ec1c8ab))

---
## 2025-06-24

### Feature

You can use [Data Boost](https://cloud.google.com/bigquery/docs/create-bigtable-external-table#compute) to analyze your Bigtable data with BigQuery without impacting the performance of the clusters that handle your application traffic. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-06-09

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.60.0](https://github.com/googleapis/java-bigtable/compare/v2.59.0...v2.60.0) (2025-06-06)

##### Features

* Improve error message on malformed struct ([#2592](https://github.com/googleapis/java-bigtable/issues/2592)) ([7f5fdf0](https://github.com/googleapis/java-bigtable/commit/7f5fdf094c5fe140807ce6abcea0b891462ba809))
* Run ExecuteQuery conformance tests ([#2557](https://github.com/googleapis/java-bigtable/issues/2557)) ([0bbc083](https://github.com/googleapis/java-bigtable/commit/0bbc083b9e798e5b557f3ffe7090b45e66c9ada5))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.59.0 ([65782aa](https://github.com/googleapis/java-bigtable/commit/65782aaf89ad78aafd7f5928e81e513c3016b471))
* Ensure that multiple instances of a client in the same process don't clobber each other ([#2590](https://github.com/googleapis/java-bigtable/issues/2590)) ([8d3dca4](https://github.com/googleapis/java-bigtable/commit/8d3dca43224179829829bcf91972610c666b130b))

##### Dependencies

* Update shared dependencies ([#2587](https://github.com/googleapis/java-bigtable/issues/2587)) ([8ec0339](https://github.com/googleapis/java-bigtable/commit/8ec033994f20b2b3aea0dfcdaffbdd1c6d19fdad))

---
## 2025-06-02

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [6.1.0](https://github.com/googleapis/nodejs-bigtable/compare/v6.0.0...v6.1.0) (2025-05-30)

##### Features

* Add full support for the universe domain ([#1604](https://github.com/googleapis/nodejs-bigtable/issues/1604)) ([4562e23](https://github.com/googleapis/nodejs-bigtable/commit/4562e2329e734c0c9d9f00cfa83aa2be13e9a7fe))

---
## 2025-05-29

### Changed

The [Bigtable Spark connector](https://cloud.google.com/bigtable/docs/use-bigtable-spark-connector) supports Scala versions 2.12 and 2.13 in all connector versions and has been updated as follows:

* Connector versions 0.5.0 and later support [dynamic columns](https://github.com/GoogleCloudDataproc/spark-bigtable-connector?tab=readme-ov-file#catalog-with-variable-column-definitions).
* Connector versions 0.6.0 and later support [custom authentication providers](https://github.com/GoogleCloudDataproc/spark-bigtable-connector/?tab=readme-ov-file#how-do-i-authenticate-outside-gce--dataproc) and [efficient joins with data sources](https://github.com/GoogleCloudDataproc/spark-bigtable-connector/?tab=readme-ov-file#efficient-joins-with-other-data-sources).

---
## 2025-05-27

### Announcement

You can delete logical and continuous materialized views in the Google Cloud console. For more information, see [Delete a logical view](https://cloud.google.com/bigtable/docs/create-manage-logical-views#delete) or [Delete a continuous materialized view](https://cloud.google.com/bigtable/docs/manage-continuous-materialized-views#delete).

---
