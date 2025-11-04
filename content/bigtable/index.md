# Bigtable

## 2025-11-03

### Feature

You can use protocol buffer (protobuf) schemas to query individual fields within protobuf messages stored as bytes in Bigtable. First, [create and manage your protobuf schemas](https://docs.cloud.google.com/bigtable/docs/create-manage-protobuf-schemas). Then, [query your protobuf data](https://docs.cloud.google.com/bigtable/docs/query-protobuf-data) using GoogleSQL for Bigtable or BigQuery external tables. This feature is in [Preview](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages).

---
## 2025-10-28

### Feature

You can use Cloud KMS Autokey in the Google Cloud console to automate the creation and use of [customer-managed encryption keys (CMEK)](https://cloud.google.com/bigtable/docs/cmek) in Bigtable clusters.

---
## 2025-10-27

### Feature

Bigtable provides vector and key-value store integrations for LangChain, an LLM orchestration framework.
For more information, see [Build LLM-powered applications using LangChain](https://cloud.google.com/bigtable/docs/langchain) and [Perform Maximal Marginal Relevance search with LangChain on Bigtable](https://cloud.google.com/bigtable/docs/mmr-vector-search).

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.68.0](https://github.com/googleapis/java-bigtable/compare/v2.67.1...v2.68.0) (2025-10-22)

##### Features

* Add Type API updates needed to support structured keys in materialized views ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))

##### Bug Fixes

* Add ReadRows/SampleRowKeys bindings for materialized views ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.62.3 ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([ed6c03f](https://github.com/googleapis/java-bigtable/commit/ed6c03ff50f42a06472f5be781b68937f48228d1))
* Don't use String.format in Preconditions messages ([#2691](https://github.com/googleapis/java-bigtable/issues/2691)) ([62a1812](https://github.com/googleapis/java-bigtable/commit/62a18128d8ec65484509dde6cd0c2b0322890cc9))
* Fixed the bigtableadmin API name for snippet region tags and possibly other GAPIC attributes ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))

##### Dependencies

* Update shared dependencies ([#2697](https://github.com/googleapis/java-bigtable/issues/2697)) ([611ad20](https://github.com/googleapis/java-bigtable/commit/611ad208359e3c1f2e675d5e4e8c8ade3616b02b))

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.34.0](https://github.com/googleapis/python-bigtable/compare/v2.33.0...v2.34.0) (2025-10-16)

##### Features

* Add support for Python 3.14 ([#1217](https://github.com/googleapis/python-bigtable/issues/1217)) ([263332a](https://github.com/googleapis/python-bigtable/commit/263332af71a229cb4fa598008a708137086a6f67))

---
## 2025-10-20

### Feature

You can [save queries](https://cloud.google.com/bigtable/docs/manage-data-using-console#save-query) and then [view and manage](https://cloud.google.com/bigtable/docs/manage-data-using-console#view_and_manage_saved_queries) the saved queries in Bigtable Studio. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-13

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.67.1](https://github.com/googleapis/java-bigtable/compare/v2.67.0...v2.67.1) (2025-10-08)

##### Dependencies

* Update shared dependencies ([#2686](https://github.com/googleapis/java-bigtable/issues/2686)) ([d7eaa02](https://github.com/googleapis/java-bigtable/commit/d7eaa02d89a63d9f9197d26e430267eff200b126))

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.33.0](https://github.com/googleapis/python-bigtable/compare/v2.32.0...v2.33.0) (2025-10-06)

##### Features

* Add support for Proto and Enum types ([#1202](https://github.com/googleapis/python-bigtable/issues/1202)) ([34ceb86](https://github.com/googleapis/python-bigtable/commit/34ceb86007db08d453fa25cca4968d5b498ffcd6))
* Expose universe\_domain for tpc ([#1150](https://github.com/googleapis/python-bigtable/issues/1150)) ([451fd97](https://github.com/googleapis/python-bigtable/commit/451fd97e435218ffed47d39423680ffc4feccac4))

##### Bug Fixes

* Fix instance registration cleanup on early iterator termination ([#1216](https://github.com/googleapis/python-bigtable/issues/1216)) ([bbfd746](https://github.com/googleapis/python-bigtable/commit/bbfd746c61a6362efa42c7899ec3e34ceb541c83))
* Refactor channel refresh ([#1174](https://github.com/googleapis/python-bigtable/issues/1174)) ([6fa3008](https://github.com/googleapis/python-bigtable/commit/6fa30084058bc34d4487d1fee5c87d7795ff167a))

---
## 2025-10-07

### Feature

The [Cassandra-Bigtable proxy adapter](https://cloud.google.com/bigtable/docs/migrate-from-cassandra), which lets you connect your Apache Cassandra-based applications to Bigtable, is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

### Feature

You can connect to Bigtable from Java applications and other reporting tools that support a generic JDBC adapter by using the [Bigtable JDBC driver](https://cloud.google.com/bigtable/docs/reference/jdbc). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-06

### Feature

You can optimize storage with Bigtable [tiered storage](https://cloud.google.com/bigtable/docs/tiered-storage), reduce storage costs, and retain data for longer. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-29

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.67.0](https://github.com/googleapis/java-bigtable/compare/v2.66.0...v2.67.0) (2025-09-24)

##### Features

* Idle channel eviction ([#2651](https://github.com/googleapis/java-bigtable/issues/2651)) ([70c05c9](https://github.com/googleapis/java-bigtable/commit/70c05c9c09a63c53818384d2a66c622c9b95e00e))
* Load balancing options for BigtableChannelPool ([#2667](https://github.com/googleapis/java-bigtable/issues/2667)) ([5adaa84](https://github.com/googleapis/java-bigtable/commit/5adaa84d80df08779da7c36a50de4632049cfe96))

##### Bug Fixes

* Add missing break; to PROTO and ENUM value type check ([#2672](https://github.com/googleapis/java-bigtable/issues/2672)) ([337e432](https://github.com/googleapis/java-bigtable/commit/337e4325f6cb5d11309ec5f33550d47d97cbe3c3))
* Remove beta api annotation for query paginator ([#2660](https://github.com/googleapis/java-bigtable/issues/2660)) ([f68a1fa](https://github.com/googleapis/java-bigtable/commit/f68a1fae49b701d1fb9942e2af2fa84a1e5b508a))

##### Dependencies

* Update shared dependencies ([#2679](https://github.com/googleapis/java-bigtable/issues/2679)) ([a5b8260](https://github.com/googleapis/java-bigtable/commit/a5b82609c365ae4792ed822e59039c1a046ef3ff))

---
## 2025-09-15

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [6.4.1](https://github.com/googleapis/nodejs-bigtable/compare/v6.4.0...v6.4.1) (2025-09-09)

##### Bug Fixes

* Directly import JS-native impl for crc32c on non-x64 platforms to avoid segfault ([#1715](https://github.com/googleapis/nodejs-bigtable/issues/1715)) ([9848963](https://github.com/googleapis/nodejs-bigtable/commit/98489637befe779df0438f466eecb0428222a29a))

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.66.0](https://github.com/googleapis/java-bigtable/compare/v2.65.1...v2.66.0) (2025-09-10)

##### Features

* Add support for Proto and Enum types ([#2662](https://github.com/googleapis/java-bigtable/issues/2662)) ([da3065d](https://github.com/googleapis/java-bigtable/commit/da3065db331be191fdf9e06be71e45c7832574ea))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#2668](https://github.com/googleapis/java-bigtable/issues/2668)) ([06ac93e](https://github.com/googleapis/java-bigtable/commit/06ac93e810830f9c04920b488d9a10af8995a6f3))

---
## 2025-09-01

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.65.1](https://github.com/googleapis/java-bigtable/compare/v2.65.0...v2.65.1) (2025-08-27)

##### Dependencies

* Update shared dependencies ([#2664](https://github.com/googleapis/java-bigtable/issues/2664)) ([841318b](https://github.com/googleapis/java-bigtable/commit/841318b2248dcda89d8482bc2e84c838bd8be8d0))

---
## 2025-08-28

### Announcement

Bigtable tools are available in [Agent Development Kit (ADK)](https://google.github.io/adk-docs/). With these tools, you can build AI agents that can interact with Bigtable data and metadata in the following ways:

* Obtain metadata about Bigtable tables and instances.
* Execute LLM-powered SQL queries.

---
## 2025-08-25

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [6.4.0](https://github.com/googleapis/nodejs-bigtable/compare/v6.3.0...v6.4.0) (2025-08-21)

##### Features

* Enable csm by default ([#1695](https://github.com/googleapis/nodejs-bigtable/issues/1695)) ([9744aa3](https://github.com/googleapis/nodejs-bigtable/commit/9744aa355e87c2170019c52b58d1045160f19e7c))
* For application latencies timed stream a few cosmetic changes are needed ([#1645](https://github.com/googleapis/nodejs-bigtable/issues/1645)) ([75d1a6f](https://github.com/googleapis/nodejs-bigtable/commit/75d1a6f5bc8d8cd74214bdf3c9db9d06786f9575))

---
## 2025-08-18

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [6.3.0](https://github.com/googleapis/nodejs-bigtable/compare/v6.2.0...v6.3.0) (2025-08-11)

##### Features

* Add client side metrics for checkAndMutateRow calls ([#1661](https://github.com/googleapis/nodejs-bigtable/issues/1661)) ([c258ea1](https://github.com/googleapis/nodejs-bigtable/commit/c258ea1b29203aad3eaaf9cfe64ddabb8c1018bf))
* Add client side metrics for readModifyWriteRow calls ([#1656](https://github.com/googleapis/nodejs-bigtable/issues/1656)) ([2129312](https://github.com/googleapis/nodejs-bigtable/commit/2129312401bf9f5b8e51b13ac576cb765de401df))
* Client side metrics support for mutateRows ([#1638](https://github.com/googleapis/nodejs-bigtable/issues/1638)) ([7601e4d](https://github.com/googleapis/nodejs-bigtable/commit/7601e4da115ff6a5da411cc857917b579c70ced7))
* Collect client side metrics for sampleRowKeys calls ([#1660](https://github.com/googleapis/nodejs-bigtable/issues/1660)) ([6ed98fa](https://github.com/googleapis/nodejs-bigtable/commit/6ed98faefe446e67f83fd5394aae30374fd3ec3a))
* For client side metrics, record metrics as MUTATE\_ROW for single row mutates ([#1650](https://github.com/googleapis/nodejs-bigtable/issues/1650)) ([f190a8c](https://github.com/googleapis/nodejs-bigtable/commit/f190a8c322498ddfbe73406759a43a268c16bdc4))
* Record ReadRows application latencies for client side metrics ([#1647](https://github.com/googleapis/nodejs-bigtable/issues/1647)) ([8af801b](https://github.com/googleapis/nodejs-bigtable/commit/8af801b3ecd7ff5e30e6c8cc67bd4123bdf34ee9))

##### Bug Fixes

* FirstResponseLatencies should only be collected for readRows calls ([#1658](https://github.com/googleapis/nodejs-bigtable/issues/1658)) ([99cf5a6](https://github.com/googleapis/nodejs-bigtable/commit/99cf5a6010249ed0eedd88f23b2d32cacb106c07))

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.65.0](https://github.com/googleapis/java-bigtable/compare/v2.64.0...v2.65.0) (2025-08-12)

##### Features

* **bigtable:** Lower the value for max rpc channels as channel resize is slow (1m, 2 channel) ([#2656](https://github.com/googleapis/java-bigtable/issues/2656)) ([d8055c1](https://github.com/googleapis/java-bigtable/commit/d8055c1fb75a616cda1503b92d7cddb9da47d42b))

---
## 2025-08-11

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.64.0](https://github.com/googleapis/java-bigtable/compare/v2.63.0...v2.64.0) (2025-08-08)

##### Features

* Add tags field to Instance proto (stable branch) ([089d527](https://github.com/googleapis/java-bigtable/commit/089d52700c225015fabfaa763163c5874b96d830))

##### Dependencies

* Update shared dependencies ([#2654](https://github.com/googleapis/java-bigtable/issues/2654)) ([4b706f4](https://github.com/googleapis/java-bigtable/commit/4b706f4f76a8152556aa99656b440adb30f37a4c))
* Update the Java code generator (gapic-generator-java) to 2.61.0 ([089d527](https://github.com/googleapis/java-bigtable/commit/089d52700c225015fabfaa763163c5874b96d830))

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.32.0](https://github.com/googleapis/python-bigtable/compare/v2.31.0...v2.32.0) (2025-08-01)

##### Features

* Add Idempotency to Cloud Bigtable MutateRowsRequest API ([#1143](https://github.com/googleapis/python-bigtable/issues/1143)) ([c3e3eb0](https://github.com/googleapis/python-bigtable/commit/c3e3eb0e4ce44ece72b150dc5822846627074fba))
* Add support for AddToCell in Data Client ([#1147](https://github.com/googleapis/python-bigtable/issues/1147)) ([1a5b4b5](https://github.com/googleapis/python-bigtable/commit/1a5b4b514cadae5c83d61296314285d3774992c5))
* Implement SQL support in test proxy ([#1106](https://github.com/googleapis/python-bigtable/issues/1106)) ([7a91bbf](https://github.com/googleapis/python-bigtable/commit/7a91bbfb9df23f7e93c40b88648840342af6f16f))
* Modernized Bigtable Admin Client featuring selective GAPIC generation ([#1177](https://github.com/googleapis/python-bigtable/issues/1177)) ([58e7d37](https://github.com/googleapis/python-bigtable/commit/58e7d3782df6b13a42af053263afc575222a6b83))

---
## 2025-08-04

### Announcement

You can add the [Cassandra to Bigtable client for Java](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/blob/main/cassandra-bigtable-migration-tools/cassandra-bigtable-java-client/cassandra-bigtable-java-client-lib/README.md) library to your Java project from the Maven Central repository.

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.63.0](https://github.com/googleapis/java-bigtable/compare/v2.62.0...v2.63.0) (2025-07-30)

##### Features

* Add Idempotency to Cloud Bigtable MutateRowsRequest API ([bc58b4f](https://github.com/googleapis/java-bigtable/commit/bc58b4f31ef457bd322f270b044735e4b62d298f))
* Add port as a parameter for the Bigtable emulator ([#2645](https://github.com/googleapis/java-bigtable/issues/2645)) ([5acd3dc](https://github.com/googleapis/java-bigtable/commit/5acd3dc01c36072bd28248d560c5d923c34b1817))
* Add type support for Proto and Enum ([bc58b4f](https://github.com/googleapis/java-bigtable/commit/bc58b4f31ef457bd322f270b044735e4b62d298f))
* Publish Proto and Enum types to CBT data API ([ace12d5](https://github.com/googleapis/java-bigtable/commit/ace12d53fe9f4d3779b2b1a2aed69ceeedd11600))
* Selective GAPIC autogeneration for Python Bigtable Admin ([e219c38](https://github.com/googleapis/java-bigtable/commit/e219c387487673869fb8bb55a5060bdc9d37bbcb))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([e219c38](https://github.com/googleapis/java-bigtable/commit/e219c387487673869fb8bb55a5060bdc9d37bbcb))
* Update routing\_parameters.path\_template ([e219c38](https://github.com/googleapis/java-bigtable/commit/e219c387487673869fb8bb55a5060bdc9d37bbcb))

##### Dependencies

* Update sdk-platorm-java-config to 3.50.2 ([#2646](https://github.com/googleapis/java-bigtable/issues/2646)) ([03e6961](https://github.com/googleapis/java-bigtable/commit/03e6961e758a9a0c39cb168c73c853328c14bfd1))

##### Documentation

* Sync generated comments from the API Protos ([bc58b4f](https://github.com/googleapis/java-bigtable/commit/bc58b4f31ef457bd322f270b044735e4b62d298f))

---
## 2025-07-31

### Feature

[Logical views](https://cloud.google.com/bigtable/docs/create-manage-logical-views) for Bigtable are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Logical views let you save a SQL query as a specific, shareable view of your data—even with a flexible schema—and then control who has permission to see the results.

---
## 2025-07-28

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [6.2.0](https://github.com/googleapis/nodejs-bigtable/compare/v6.1.0...v6.2.0) (2025-07-23)

##### Features

* Add client-side metrics collection to readRows calls ([#1571](https://github.com/googleapis/nodejs-bigtable/issues/1571)) ([71f4d78](https://github.com/googleapis/nodejs-bigtable/commit/71f4d78422137c88f1521be45004982367dbda31))
* Add plumbing to support unary calls for client side metric collection ([#1631](https://github.com/googleapis/nodejs-bigtable/issues/1631)) ([c267ede](https://github.com/googleapis/nodejs-bigtable/commit/c267ede0140aa29bc75feada93899a4945980375))
* Add support for Execute Query ([#1613](https://github.com/googleapis/nodejs-bigtable/issues/1613)) ([e3894ed](https://github.com/googleapis/nodejs-bigtable/commit/e3894edf4fc881153432f77ce976141397dc0348))
* Initial timed stream implementation for application latencies ([#1639](https://github.com/googleapis/nodejs-bigtable/issues/1639)) ([ca490e8](https://github.com/googleapis/nodejs-bigtable/commit/ca490e80f2359156475e52c5f72fe0a9fe8e9740))

##### Bug Fixes

* In client-side metrics, make sure that the right views get created for the right metrics ([#1590](https://github.com/googleapis/nodejs-bigtable/issues/1590)) ([6cb7cdd](https://github.com/googleapis/nodejs-bigtable/commit/6cb7cddf42ff1fe29b2ae4a729739bc12c3d4942))

---
## 2025-07-21

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.62.0](https://github.com/googleapis/java-bigtable/compare/v2.61.0...v2.62.0) (2025-07-15)

##### Features

* Add Idempotency to Cloud Bigtable MutateRowRequest API ([b5acca6](https://github.com/googleapis/java-bigtable/commit/b5acca6ac4f1eec420adb27bc77aa1bda0ec2dca))
* Add SchemaBundles API ([b5acca6](https://github.com/googleapis/java-bigtable/commit/b5acca6ac4f1eec420adb27bc77aa1bda0ec2dca))
* **bigtable:** Add schema bundle support ([#2619](https://github.com/googleapis/java-bigtable/issues/2619)) ([7d7b9a9](https://github.com/googleapis/java-bigtable/commit/7d7b9a966d3ef7b7a0ef3f82038ab73f4d791427))
* Next release from main branch is 2.62.0 ([#2621](https://github.com/googleapis/java-bigtable/issues/2621)) ([202b211](https://github.com/googleapis/java-bigtable/commit/202b21102e71da71ff56f19a12d8a00a59cd8107))

##### Dependencies

* Minor cleanup ([#2623](https://github.com/googleapis/java-bigtable/issues/2623)) ([7b230e8](https://github.com/googleapis/java-bigtable/commit/7b230e86902b5733c06e45fad90da76653ee1096))
* Update shared dependencies ([#2616](https://github.com/googleapis/java-bigtable/issues/2616)) ([eb7cfd5](https://github.com/googleapis/java-bigtable/commit/eb7cfd526aa999c614b7b8285d32759e2739ff9a))

---
## 2025-07-07

### Changed

When you [undelete a table](https://cloud.google.com/bigtable/docs/managing-tables#undelete-table), Bigtable automatically enables deletion protection for that table.

---
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
