# Spanner

## 2025-07-14

### Feature

[Spanner Data Boost](https://cloud.google.com/spanner/docs/databoost/databoost-overview) supports data stored on hard disk drives (HDD). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

---
## 2025-06-30

### Feature

Spanner supports the following new client-side metrics to the Spanner API frontend (AFE) and Google frontend (GFE) for Java and Go applications:

* AFE connectivity error count
* AFE latencies
* GFE connectivity error count
* GFE latencies

These metrics can be used with server-side metrics to enable faster troubleshooting of performance and latency issues. For more information, see
[Client-side metrics descriptions](https://cloud.google.com/spanner/docs/client-side-metrics-descriptions).

### Feature

To troubleshoot or understand your Spanner queries better, you can download and save your [query execution plan](https://cloud.google.com/spanner/docs/query-execution-plans) as a JSON file. You can now use the content of this file to see a visualization of the query execution plan in Spanner Studio. For more information, see [Take a tour of the query plan visualizer](https://cloud.google.com/spanner/docs/tune-query-with-visualizer#visual-plan-tour).

### Libraries

A monthly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [spanner/admin/database/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/spanner/admin/database/apiv1)

#### [1.83.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.82.0...spanner/v1.83.0) (2025-06-27)

##### Features

* **spanner/spansql:** Add support for TOKENIZE\_JSON. ([#12338](https://github.com/googleapis/google-cloud-go/issues/12338)) ([72225a5](https://github.com/googleapis/google-cloud-go/commit/72225a52c0f6bc6eac6d4e450dad0b566e79553f))
* **spanner/spansql:** Support EXISTS in query parsing ([#12439](https://github.com/googleapis/google-cloud-go/issues/12439)) ([f5cb67b](https://github.com/googleapis/google-cloud-go/commit/f5cb67b104e4d99196064fb4474e0644e90c9a00))
* **spanner:** Add new change\_stream.proto ([40b60a4](https://github.com/googleapis/google-cloud-go/commit/40b60a4b268040ca3debd71ebcbcd126b5d58eaa))
* **spanner:** Add option for how to call BeginTransaction ([#12436](https://github.com/googleapis/google-cloud-go/issues/12436)) ([2cba13b](https://github.com/googleapis/google-cloud-go/commit/2cba13b8fef80b6cb5980e3b5b2bfc6dc796a03e))
* **spanner:** Wrap proto mutation ([#12497](https://github.com/googleapis/google-cloud-go/issues/12497)) ([e655889](https://github.com/googleapis/google-cloud-go/commit/e655889e2fd6a55f901d1d8b146e7aa5efdca705))

##### Bug Fixes

* **spanner:** Pointer type custom struct decoder ([#12496](https://github.com/googleapis/google-cloud-go/issues/12496)) ([ac3cafb](https://github.com/googleapis/google-cloud-go/commit/ac3cafbac435a3ac98fd4693bac84a3f4a260c5b))

### Java

### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)

#### [6.95.0](https://github.com/googleapis/java-spanner/compare/v6.94.0...v6.95.0) (2025-06-05)

##### Features

* Enable ALTS hard bound token in DirectPath ([#3904](https://github.com/googleapis/java-spanner/issues/3904)) ([2b0f2ff](https://github.com/googleapis/java-spanner/commit/2b0f2ff214f4b68dd5957bc4280edb713b77a763))
* Enable grpc and afe metrics ([#3896](https://github.com/googleapis/java-spanner/issues/3896)) ([706f794](https://github.com/googleapis/java-spanner/commit/706f794f044c2cb1112cfdae6f379e5f2bc3f26f))
* Last statement sample ([#3830](https://github.com/googleapis/java-spanner/issues/3830)) ([2f62816](https://github.com/googleapis/java-spanner/commit/2f62816b0af9aced1b73e25525f60f8e3e923454))
* **spanner:** Add new change\_stream.proto ([f385698](https://github.com/googleapis/java-spanner/commit/f38569865de7465ae9a37b844a9dd983571d3688))

##### Bug Fixes

* Directpath\_enabled attribute ([#3897](https://github.com/googleapis/java-spanner/issues/3897)) ([53bc510](https://github.com/googleapis/java-spanner/commit/53bc510145921d00bc3df04aa4cf407179ed8d8e))

##### Dependencies

* Update dependency io.opentelemetry:opentelemetry-bom to v1.50.0 ([#3887](https://github.com/googleapis/java-spanner/issues/3887)) ([94b879c](https://github.com/googleapis/java-spanner/commit/94b879c8c1848fa0b14dbe8cda8390cfe9e8fce6))

#### [6.95.1](https://github.com/googleapis/java-spanner/compare/v6.95.0...v6.95.1) (2025-06-06)

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#3909](https://github.com/googleapis/java-spanner/issues/3909)) ([3de8502](https://github.com/googleapis/java-spanner/commit/3de8502b98ebb90526fc2339e279f9b710816b3b))
* Update googleapis/sdk-platform-java action to v2.59.0 ([#3910](https://github.com/googleapis/java-spanner/issues/3910)) ([aed8bd6](https://github.com/googleapis/java-spanner/commit/aed8bd6d5a0b1e0dfab345e0de68f285e8b8aedb))

#### [6.96.0](https://github.com/googleapis/java-spanner/compare/v6.95.1...v6.96.0) (2025-06-27)

##### Features

* Allow JDBC to configure directpath for connection ([#3929](https://github.com/googleapis/java-spanner/issues/3929)) ([d754f1f](https://github.com/googleapis/java-spanner/commit/d754f1f99294d86ec881583f217fa09f291a3d7a))
* Support getOrNull and getOrDefault in Struct ([#3914](https://github.com/googleapis/java-spanner/issues/3914)) ([1dc5a3e](https://github.com/googleapis/java-spanner/commit/1dc5a3ec0ca9ea530e8691df5c2734c0a1ece559))
* Use multiplexed sessions for read-only transactions ([#3917](https://github.com/googleapis/java-spanner/issues/3917)) ([37fdc27](https://github.com/googleapis/java-spanner/commit/37fdc27aab4e71ac141c2a2c979f864e97395a97))

##### Bug Fixes

* Allow zero durations to be set for connections ([#3916](https://github.com/googleapis/java-spanner/issues/3916)) ([43ea4fa](https://github.com/googleapis/java-spanner/commit/43ea4fa68eac00801beb8e58c1eb09e9f32e5ce5))

##### Documentation

* Add snippet for Repeatable Read configuration at client and transaction ([#3908](https://github.com/googleapis/java-spanner/issues/3908)) ([ff3d212](https://github.com/googleapis/java-spanner/commit/ff3d212c98276c4084f44619916d0444c9652803))
* Update SpannerSample.java to align with best practices ([#3625](https://github.com/googleapis/java-spanner/issues/3625)) ([7bfc62d](https://github.com/googleapis/java-spanner/commit/7bfc62d3d9e57242e0dfddea090208f8c65f0f8e))

---
## 2025-06-24

### Feature

You can directly connect and interact with your Spanner database using the Spanner CLI, an interactive shell for Spanner that is built into the Google Cloud CLI. You can use the Spanner CLI to start an interactive session and automate SQL executions from the shell or an input file. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Spanner CLI quickstart](https://cloud.google.com/spanner/docs/spanner-cli).

---
## 2025-06-20

### Feature

A new free trial creation work flow makes it easier to start your Spanner free trial. With a free trial instance, you can learn and explore Spanner for 90 days at no cost. You can create relational (GoogleSQL and PostgreSQL) databases and deploy NoSQL models (Spanner Graph, Vector search, and Full-text search) in a single, fully managed database. For more information, see [Spanner free trial instances overview](https://cloud.google.com/spanner/docs/free-trial-instance).

---
## 2025-06-11

### Feature

Column operations statistics are [generally available](https://cloud.google.com/products#product-launch-stages). They help you get insights into and monitor the usage of columns in your database. For more information, see [Column operations statistics](https://cloud.google.com/spanner/docs/introspection/column-operations-statistics).

---
## 2025-06-02

### Feature

BigQuery now supports using [Spanner external datasets](https://cloud.google.com/bigquery/docs/spanner-external-datasets) with [authorized views](https://cloud.google.com/bigquery/docs/authorized-views), [authorized routines](https://cloud.google.com/bigquery/docs/authorized-routines), and [Cloud resource connections](https://cloud.google.com/bigquery/docs/create-cloud-resource-connection). This feature is [generally available](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages) (GA).

### Libraries

A monthly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [spanner/admin/database/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/spanner/admin/database/apiv1)

#### [1.81.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.80.0...spanner/v1.81.0) (2025-05-09)

##### Features

* **spanner/spansql:** Add support for DROP SEARCH INDEX and ALTER SEARCH INDEX ([#11961](https://github.com/googleapis/google-cloud-go/issues/11961)) ([952cd7f](https://github.com/googleapis/google-cloud-go/commit/952cd7fd419af9eb74f5d30a111ae936094b0645))

##### Bug Fixes

* **spanner:** Row mismatch in SelectAll using custom type ([#12222](https://github.com/googleapis/google-cloud-go/issues/12222)) ([ce6a23a](https://github.com/googleapis/google-cloud-go/commit/ce6a23a45fe66cc12e1b5014d2d45f1968ddc067))

#### [1.81.1](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.81.0...spanner/v1.81.1) (2025-05-15)

##### Features

* **spanner:** Add support of AFE and GRPC metrics in client-side metrics ([#12067](https://github.com/googleapis/google-cloud-go/issues/12067)) ([7b77038](https://github.com/googleapis/google-cloud-go/commit/7b77038eb4afe31b1a0d42f7c35aeabce0f48810))

#### [1.82.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.81.1...spanner/v1.82.0) (2025-05-20)

##### Features

* **spanner/admin/database:** Add throughput\_mode to UpdateDatabaseDdlRequest to be used by Spanner Migration Tool. See https ([#12287](https://github.com/googleapis/google-cloud-go/issues/12287)) ([2a9d8ee](https://github.com/googleapis/google-cloud-go/commit/2a9d8eec71a7e6803eb534287c8d2f64903dcddd))

### Java

### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)

#### [6.92.0](https://github.com/googleapis/java-spanner/compare/v6.91.1...v6.92.0) (2025-04-29)

* **spanner:** Do not export metrics during shutdown if prev export was less than 30 seconds ago ([#12266](https://github.com/googleapis/google-cloud-go/issues/12266)) ([8ad7511](https://github.com/googleapis/google-cloud-go/commit/8ad75111433be5424f9fff8aafd73463cb467734))
* **spanner:** Fix invalid trace in case of skipping trailers ([#12235](https://github.com/googleapis/google-cloud-go/issues/12235)) ([e54c439](https://github.com/googleapis/google-cloud-go/commit/e54c4398831b5a1c2998f9e8d159f0118aee1d0b))
  ### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)
  #### [6.94.0](https://github.com/googleapis/java-spanner/compare/v6.93.0...v6.94.0) (2025-05-21)

##### Features

* [Internal] client-side metrics for afe latency and connectivity error ([#3819](https://github.com/googleapis/java-spanner/issues/3819)) ([a8dba0a](https://github.com/googleapis/java-spanner/commit/a8dba0a83939fdbbc324f0a7aa6c44180462fa3a))
* Support begin with AbortedException for manager interface ([#3835](https://github.com/googleapis/java-spanner/issues/3835)) ([5783116](https://github.com/googleapis/java-spanner/commit/578311693bed836c8916f4b4ffa0782a468c1af3))
* Add throughput\_mode to UpdateDatabaseDdlRequest to be used by Spanner Migration Tool. See https://github.com/GoogleCloudPlatform/spanner-migration-tool ([3070f1d](https://github.com/googleapis/java-spanner/commit/3070f1db97788c2a55c553ab8a4de3419d1ccf5c))
* Enable AFE and gRPC metrics for DP ([#3852](https://github.com/googleapis/java-spanner/issues/3852)) ([203baae](https://github.com/googleapis/java-spanner/commit/203baae3996378435095cb90e3b2c7ee71a643cd))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.56.2 ([11bfd90](https://github.com/googleapis/java-spanner/commit/11bfd90daa244dbd31a76bc5a1d2e694e43fa292))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.58.0 ([3070f1d](https://github.com/googleapis/java-spanner/commit/3070f1db97788c2a55c553ab8a4de3419d1ccf5c))
* Remove trailing semicolons in DDL ([#3879](https://github.com/googleapis/java-spanner/issues/3879)) ([ca3a67d](https://github.com/googleapis/java-spanner/commit/ca3a67db715f398943382df1f8a9979905811ff8))
* Change server timing duration attribute to float as per w3c ([#3851](https://github.com/googleapis/java-spanner/issues/3851)) ([da8dd8d](https://github.com/googleapis/java-spanner/commit/da8dd8da3171a073d7b450d4413936351a4c1060))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.57.0 ([23b985c](https://github.com/googleapis/java-spanner/commit/23b985c9a04837b0b38f2cfc5d96469e1d664d67))
* Non-ASCII Unicode characters in code ([#3844](https://github.com/googleapis/java-spanner/issues/3844)) ([85a0820](https://github.com/googleapis/java-spanner/commit/85a0820505889ae6482a9e4f845cd53430dd6b44))
* Only close and return sessions once ([#3846](https://github.com/googleapis/java-spanner/issues/3846)) ([32b2373](https://github.com/googleapis/java-spanner/commit/32b2373d62cac3047d9686c56af278c706d7c488))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#3836](https://github.com/googleapis/java-spanner/issues/3836)) ([2ee7f97](https://github.com/googleapis/java-spanner/commit/2ee7f971f3374b01d22e5a7f8f2483cf60c3363d))

#### [6.93.0](https://github.com/googleapis/java-spanner/compare/v6.92.0...v6.93.0) (2025-05-09)

* Update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#3869](https://github.com/googleapis/java-spanner/issues/3869)) ([afa17f7](https://github.com/googleapis/java-spanner/commit/afa17f73beab80639467916bc73b5c96305093aa))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#3880](https://github.com/googleapis/java-spanner/issues/3880)) ([f3b00b6](https://github.com/googleapis/java-spanner/commit/f3b00b663aa897fda1bc21222d29726e6be630cb))
* Update dependency com.google.cloud.opentelemetry:exporter-metrics to v0.34.0 ([#3861](https://github.com/googleapis/java-spanner/issues/3861)) ([676b14f](https://github.com/googleapis/java-spanner/commit/676b14f916dea783b40ddec4061bd7af157b5d98))
* Update dependency commons-io:commons-io to v2.19.0 ([#3863](https://github.com/googleapis/java-spanner/issues/3863)) ([80a6af8](https://github.com/googleapis/java-spanner/commit/80a6af836ca29ec196a2f509831e1d36c557168f))
* Update dependency io.opentelemetry:opentelemetry-bom to v1.50.0 ([#3865](https://github.com/googleapis/java-spanner/issues/3865)) ([ae63050](https://github.com/googleapis/java-spanner/commit/ae6305089b394be0c1eaf8ff7e188711288d87ad))
* Update googleapis/sdk-platform-java action to v2.58.0 ([#3870](https://github.com/googleapis/java-spanner/issues/3870)) ([d1e45fa](https://github.com/googleapis/java-spanner/commit/d1e45fa88bb005529bcfb2a6ff2df44065be0fd2))
* Update opentelemetry.version to v1.50.0 ([#3866](https://github.com/googleapis/java-spanner/issues/3866)) ([f7e09b8](https://github.com/googleapis/java-spanner/commit/f7e09b8148c0e51503255694bd3347c637724b34))

##### Documentation

* Add samples for unnamed (positional) parameters ([#3849](https://github.com/googleapis/java-spanner/issues/3849)) ([035cadd](https://github.com/googleapis/java-spanner/commit/035cadd5bb77a8f9f6fb25ac8c8e5a3e186d9a22))

### Node.js

### Changes for [@google-cloud/spanner](https://github.com/googleapis/nodejs-spanner)

#### [8.0.0](https://github.com/googleapis/nodejs-spanner/compare/v7.21.0...v8.0.0) (2025-05-12)

##### ⚠ BREAKING CHANGES

* remove the arrify package ([#2292](https://github.com/googleapis/nodejs-spanner/issues/2292))
* migrate to Node 18 ([#2271](https://github.com/googleapis/nodejs-spanner/issues/2271))

##### Features

* Add promise based signatures for createQueryPartitions ([#2284](https://github.com/googleapis/nodejs-spanner/issues/2284)) ([255d8a6](https://github.com/googleapis/nodejs-spanner/commit/255d8a6a5749b6a05cd87dd7444cab7dd75d3e42))
* Add promise based signatures on createReadPartitions ([#2300](https://github.com/googleapis/nodejs-spanner/issues/2300)) ([7b8a1f7](https://github.com/googleapis/nodejs-spanner/commit/7b8a1f70f0de3aa5886a2cde9325c9a36222a311))
* Support promise based signatures for execute method ([#2301](https://github.com/googleapis/nodejs-spanner/issues/2301)) ([bb857e1](https://github.com/googleapis/nodejs-spanner/commit/bb857e18459f717d67b9b3d144c2b022178363cb))

##### Bug Fixes

* **deps:** Update dependency @google-cloud/kms to v5 ([#2289](https://github.com/googleapis/nodejs-spanner/issues/2289)) ([1ccb505](https://github.com/googleapis/nodejs-spanner/commit/1ccb505935e70b6f576f06e566325146ee68f3ff))
* **deps:** Update dependency @google-cloud/precise-date to v5 ([#2290](https://github.com/googleapis/nodejs-spanner/issues/2290)) ([44f7575](https://github.com/googleapis/nodejs-spanner/commit/44f7575efd3751d0595beef2ec4eb9f39bc426d7))
* **deps:** Update dependency big.js to v7 ([#2286](https://github.com/googleapis/nodejs-spanner/issues/2286)) ([0911297](https://github.com/googleapis/nodejs-spanner/commit/0911297cc33aec93c09ef2be42413f20c75fc2bf))

##### Miscellaneous Chores

* Migrate to Node 18 ([#2271](https://github.com/googleapis/nodejs-spanner/issues/2271)) ([cab3f22](https://github.com/googleapis/nodejs-spanner/commit/cab3f229ccb2189bd5af0c25a3006b553f8a5453))
* Remove the arrify package ([#2292](https://github.com/googleapis/nodejs-spanner/issues/2292)) ([e8f5ca1](https://github.com/googleapis/nodejs-spanner/commit/e8f5ca15125d570949769e6e66f0d911cb21f58d))

### Python

### Changes for [google-cloud-spanner](https://github.com/googleapis/python-spanner)

#### [3.54.0](https://github.com/googleapis/python-spanner/compare/v3.53.0...v3.54.0) (2025-04-28)

##### Features

* Add interval type support ([#1340](https://github.com/googleapis/python-spanner/issues/1340)) ([6ca9b43](https://github.com/googleapis/python-spanner/commit/6ca9b43c3038eca1317c7c9b7e3543b5f1bc68ad))
* Add sample for pre-split feature ([#1333](https://github.com/googleapis/python-spanner/issues/1333)) ([ca76108](https://github.com/googleapis/python-spanner/commit/ca76108809174e4f3eea38d7ac2463d9b4c73304))
* Add SQL statement for begin transaction isolation level ([#1331](https://github.com/googleapis/python-spanner/issues/1331)) ([3ac0f91](https://github.com/googleapis/python-spanner/commit/3ac0f9131b38e5cfb2b574d3d73b03736b871712))
* Support transaction isolation level in dbapi ([#1327](https://github.com/googleapis/python-spanner/issues/1327)) ([03400c4](https://github.com/googleapis/python-spanner/commit/03400c40f1c1cc73e51733f2a28910a8dd78e7d9))

##### Bug Fixes

* Improve client-side regex statement parser ([#1328](https://github.com/googleapis/python-spanner/issues/1328)) ([b3c259d](https://github.com/googleapis/python-spanner/commit/b3c259deec817812fd8e4940faacf4a927d0d69c))

#### [3.55.0](https://github.com/googleapis/python-spanner/compare/v3.54.0...v3.55.0) (2025-05-28)

##### Features

* Add a `last` field in the `PartialResultSet` ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* Add support for multiplexed sessions ([#1381](https://github.com/googleapis/python-spanner/issues/1381)) ([97d7268](https://github.com/googleapis/python-spanner/commit/97d7268ac12a57d9d116ee3d9475580e1e7e07ae))
* Add throughput\_mode to UpdateDatabaseDdlRequest to be used by Spanner Migration Tool. See https://github.com/GoogleCloudPlatform/spanner-migration-tool ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* Support fine-grained permissions database roles in connect ([#1338](https://github.com/googleapis/python-spanner/issues/1338)) ([064d9dc](https://github.com/googleapis/python-spanner/commit/064d9dc3441a617cbc80af6e16493bc42c89b3c9))

##### Bug Fixes

* E2E tracing metadata append issue ([#1357](https://github.com/googleapis/python-spanner/issues/1357)) ([3943885](https://github.com/googleapis/python-spanner/commit/394388595a312f60b423dfbfd7aaf2724cc4454f))
* Pass through kwargs in dbapi connect ([#1368](https://github.com/googleapis/python-spanner/issues/1368)) ([aae8d61](https://github.com/googleapis/python-spanner/commit/aae8d6161580c88354d813fe75a297c318f1c2c7))
* Remove setup.cfg configuration for creating universal wheels ([#1324](https://github.com/googleapis/python-spanner/issues/1324)) ([e064474](https://github.com/googleapis/python-spanner/commit/e0644744d7f3fcea42b461996fc0ee22d4218599))

##### Documentation

* A comment for field `chunked_value` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `precommit_token` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `precommit_token` in message `.google.spanner.v1.ResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `query_plan` in message `.google.spanner.v1.ResultSetStats` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `row_count_lower_bound` in message `.google.spanner.v1.ResultSetStats` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `row_type` in message `.google.spanner.v1.ResultSetMetadata` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `rows` in message `.google.spanner.v1.ResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `stats` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `stats` in message `.google.spanner.v1.ResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `values` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for message `ResultSetMetadata` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for message `ResultSetStats` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* Fix markdown formatting in transactions page ([#1377](https://github.com/googleapis/python-spanner/issues/1377)) ([de322f8](https://github.com/googleapis/python-spanner/commit/de322f89642a3c13b6b1d4b9b1a2cdf4c8f550fb))

---
## 2025-05-27

### Feature

Spanner now supports [cross regional federated queries](https://cloud.google.com/bigquery/docs/spanner-federated-queries#cross_region_queries) from BigQuery, which allows BigQuery users to query Spanner tables from regions other than their BigQuery region. Users will not incur any Spanner [network egress charges](https://cloud.google.com/spanner/pricing#network) during the preview period. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
