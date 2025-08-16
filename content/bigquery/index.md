# BigQuery

## 2025-08-14

### Feature

You can now [visualize your geospatial query results](https://cloud.google.com/bigquery/docs/geospatial-visualize) on an interactive map in BigQuery studio. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

### Feature

You can use [cross region federated queries](https://cloud.google.com/bigquery/docs/spanner-federated-queries#cross_region_queries) to query Spanner tables from regions other than the source BigQuery region. These cross region queries incur additional [Spanner network egress charges](https://cloud.google.com/spanner/pricing#network). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

---
## 2025-08-13

### Feature

You can aggregate table data with Gemini assistance in your [BigQuery data preparations](https://cloud.google.com/bigquery/docs/data-prep-get-suggestions). Aggregations in data preparations are in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-08-12

### Feature

You can now [save query results to Cloud Storage](https://cloud.google.com/bigquery/docs/export-file#saving-query-results-to-cloud-storage). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-08-11

### Feature

BigQuery [resource utilization charts](https://cloud.google.com/bigquery/docs/admin-resource-charts#view-resource-utilization) are [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

### Feature

You can now use [`WITH` expressions](https://cloud.google.com/bigquery/docs/reference/standard-sql/operators#with_expression) in your GoogleSQL queries to create temporary variables. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

### Feature

You can now use [chained function call syntax](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-reference#chained-function-calls) in GoogleSQL to make deeply nested function calls easier to read. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

### Changed

BigQuery data preparations are now represented in the SQLX format and in the pipe query syntax to simplify the CI/CD code review process. For more information, see [Manage data preparations](https://cloud.google.com/bigquery/docs/manage-data-preparations).

---
## 2025-08-06

### Feature

Enabling the advanced runtime now includes [short query optimizations](https://cloud.google.com/bigquery/docs/advanced-runtime#short_query_optimizations). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-08-04

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigquery](https://github.com/googleapis/java-bigquery)

#### [2.54.0](https://github.com/googleapis/java-bigquery/compare/v2.53.0...v2.54.0) (2025-07-31)

##### Features

* **bigquery:** Add OpenTelemetry Samples ([#3899](https://github.com/googleapis/java-bigquery/issues/3899)) ([e3d9ed9](https://github.com/googleapis/java-bigquery/commit/e3d9ed92ca5d9b58b5747960d74f895ed8733ebf))
* **bigquery:** Add otel metrics to request headers ([#3900](https://github.com/googleapis/java-bigquery/issues/3900)) ([4071e4c](https://github.com/googleapis/java-bigquery/commit/4071e4cb2547b236183fd4fbb92c73f074cf2fa0))

##### Dependencies

* update dependency com.google.cloud:google-cloud-bigquerystorage-bom to v3.16.1 (#3912) (https://github.com/googleapis/java-bigquery/commit/bb6f6dcb90b1ddf72e630c4dc64737cf2c2ebd2e)
* Update dependency com.google.api.grpc:proto-google-cloud-bigqueryconnection-v1 to v2.70.0 ([#3890](https://github.com/googleapis/java-bigquery/issues/3890)) ([84207e2](https://github.com/googleapis/java-bigquery/commit/84207e297eec75bcb4f1cc1b64423d7c2ddd6c30))
* Update dependency com.google.apis:google-api-services-bigquery to v2-rev20250706-2.0.0 ([#3910](https://github.com/googleapis/java-bigquery/issues/3910)) ([ae5c971](https://github.com/googleapis/java-bigquery/commit/ae5c97146c7076e90c000fd98b797ec8e08a9cd8))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#3901](https://github.com/googleapis/java-bigquery/issues/3901)) ([8205623](https://github.com/googleapis/java-bigquery/commit/82056237f194a6c99ec4fb3a4315023efdedff1b))
* Update dependency io.opentelemetry:opentelemetry-api to v1.52.0 ([#3902](https://github.com/googleapis/java-bigquery/issues/3902)) ([772407b](https://github.com/googleapis/java-bigquery/commit/772407b12f4da005f79eafc944d4c53f0eec5c27))
* Update dependency io.opentelemetry:opentelemetry-bom to v1.52.0 ([#3903](https://github.com/googleapis/java-bigquery/issues/3903)) ([509a6fc](https://github.com/googleapis/java-bigquery/commit/509a6fc0bb7e7a101bf0d4334a3ff1adde2cab09))
* Update dependency io.opentelemetry:opentelemetry-context to v1.52.0 ([#3904](https://github.com/googleapis/java-bigquery/issues/3904)) ([96c1bae](https://github.com/googleapis/java-bigquery/commit/96c1bae0fcdfdfc2dbb25dcae5007c5d02111a8c))
* Update dependency io.opentelemetry:opentelemetry-exporter-logging to v1.52.0 ([#3905](https://github.com/googleapis/java-bigquery/issues/3905)) ([28ee4c9](https://github.com/googleapis/java-bigquery/commit/28ee4c941b99b1fe3803aefbe7a8ae57100d76cb))

### Feature

You can now use the new [Data Science Agent (DSA)](https://cloud.google.com/bigquery/docs/colab-data-science-agent) for Colab Enterprise and BigQuery to automate exploratory data analysis, perform
machine learning tasks, and deliver insights all within a
Colab Enterprise notebook. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-07-31

### Feature

You can manage data profile scans and data quality scans across your project by using the **Metadata curation** page in the Google Cloud console. For more information, see [Profile your data](https://cloud.google.com/bigquery/docs/data-profile-scan) and [Scan for data quality issues](https://cloud.google.com/bigquery/docs/data-quality-scan). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Changed

BigQuery ML has improved throughput by more than 100x for the following
generative AI functions:

* [`ML.GENERATE_TEXT`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-text)
* [`AI.GENERATE_TABLE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-table)
* [`AI.GENERATE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate)
* [`AI.GENERATE_BOOL`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-bool)
* [`AI.GENERATE_DOUBLE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-double)
* [`AI.GENERATE_INT`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-int)

Actual performance varies based on the number of input and output tokens in the
request, but a typical 6-hour job can now process millions of rows. For more
information, see
[Generative AI functions](https://cloud.google.com/bigquery/quotas#generative_ai_functions).

### Changed

BigQuery ML now can automatically detect model quota increases in Vertex AI, and automatically adjusts the quota for any BigQuery ML functions that use those models. You no longer need to email the BigQuery ML team to increase model quota.

### Feature

You can now use [continuous queries](https://cloud.google.com/bigquery/docs/continuous-queries-introduction) to [export BigQuery data to Spanner in real time](https://cloud.google.com/bigquery/docs/export-to-spanner). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-07-30

### Announcement

The Gemini for Google Cloud API (cloudaicompanion.googleapis.com) is now enabled by default for most BigQuery projects. Exceptions include projects where customers have opted out, and those linked to accounts based in EMEA regions including [BigQuery Europe, Middle East, and Africa regions](https://cloud.google.com/bigquery/docs/locations#supported_locations).

---
## 2025-07-28

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigquery](https://github.com/googleapis/nodejs-bigquery)

#### [8.1.1](https://github.com/googleapis/nodejs-bigquery/compare/v8.1.0...v8.1.1) (2025-07-23)

##### Bug Fixes

* Remove `is` package as dependency ([#1500](https://github.com/googleapis/nodejs-bigquery/issues/1500)) ([926c9f8](https://github.com/googleapis/nodejs-bigquery/commit/926c9f879521f0c06ab4f96b0b86e426aff3543c))

### Python

### Changes for [google-cloud-bigquery](https://github.com/googleapis/python-bigquery)

#### [3.35.1](https://github.com/googleapis/python-bigquery/compare/v3.35.0...v3.35.1) (2025-07-21)

##### Documentation

* Specify the inherited-members directive for job classes ([#2244](https://github.com/googleapis/python-bigquery/issues/2244)) ([d207f65](https://github.com/googleapis/python-bigquery/commit/d207f6539b7a4c248a5de5719d7f384abbe20abe))

### Feature

You can now associate [data policies directly on columns](https://cloud.google.com/bigquery/docs/column-data-masking#data-policies-on-column). This feature enables direct database administration for controlling access and applying masking and transformation rules at the column level. This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-07-22

### Feature

You can now use the
[`VECTOR_INDEX.STATISTICS` function](https://cloud.google.com/bigquery/docs/reference/standard-sql/vectorindex_functions#vector_indexstatistics) to calculate how much an indexed table's data has drifted between when a
vector index was created and the present. If table data has changed enough
to require a [vector index rebuild](https://cloud.google.com/bigquery/docs/vector-index#rebuild_a_vector_index), you can use the
[`ALTER VECTOR INDEX REBUILD` statement](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#alter_vector_index_rebuild_statement)
to rebuild the vector index. This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

[Access Transparency](https://cloud.google.com/assured-workloads/access-transparency/docs/supported-services) supports [BigQuery data preparation](https://cloud.google.com/bigquery/docs/data-prep-introduction) in the [GA](https://cloud.google.com/products#product-launch-stages) stage.

### Feature

The [`CREATE EXTERNAL TABLE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_external_table_statement) and [`LOAD DATA`](https://cloud.google.com/bigquery/docs/reference/standard-sql/load-statements) statements now support the following options in [Preview](https://cloud.google.com/products#product-launch-stages):

* `null_markers`: define the strings that represent `NULL` values in CSV files.
* `source_column_match`: specify how loaded columns are matched to the schema. You can match columns by position or by name.

### Feature

You can now use the [`MATCH_RECOGNIZE` clause](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#match_recognize_clause) in your SQL queries to filter and aggregate matches across rows in a table. This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-07-21

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigquery](https://github.com/googleapis/java-bigquery)

#### [2.53.0](https://github.com/googleapis/java-bigquery/compare/v2.52.0...v2.53.0) (2025-07-14)

##### Features

* **bigquery:** Add OpenTelemetry support to BigQuery rpcs ([#3860](https://github.com/googleapis/java-bigquery/issues/3860)) ([e2d23c1](https://github.com/googleapis/java-bigquery/commit/e2d23c1b15f2c48a4113f82b920f5c29c4b5dfea))
* **bigquery:** Add support for custom timezones and timestamps ([#3859](https://github.com/googleapis/java-bigquery/issues/3859)) ([e5467c9](https://github.com/googleapis/java-bigquery/commit/e5467c917c63ac066edcbcd902cc2093a39971a3))
* Next release from main branch is 2.53.0 ([#3879](https://github.com/googleapis/java-bigquery/issues/3879)) ([c47a062](https://github.com/googleapis/java-bigquery/commit/c47a062136fea4de91190cafb1f11bac6abbbe3a))

##### Bug Fixes

* Load jobs preserve ascii control characters configuration ([#3876](https://github.com/googleapis/java-bigquery/issues/3876)) ([5cfdf85](https://github.com/googleapis/java-bigquery/commit/5cfdf855fa0cf206660fd89743cbaabf3afa75a3))

##### Dependencies

* Update dependency com.google.api.grpc:proto-google-cloud-bigqueryconnection-v1 to v2.69.0 ([#3870](https://github.com/googleapis/java-bigquery/issues/3870)) ([a7f1007](https://github.com/googleapis/java-bigquery/commit/a7f1007b5242da2c0adebbb309a908d7d4db5974))
* Update dependency com.google.apis:google-api-services-bigquery to v2-rev20250615-2.0.0 ([#3872](https://github.com/googleapis/java-bigquery/issues/3872)) ([f081589](https://github.com/googleapis/java-bigquery/commit/f08158955b7fec3c2ced6332b6e4d76cc13f2e90))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#3878](https://github.com/googleapis/java-bigquery/issues/3878)) ([0e971b8](https://github.com/googleapis/java-bigquery/commit/0e971b8ace013caa31b8a02a21038e94bebae2a5))

##### Documentation

* Update maven format command ([#3877](https://github.com/googleapis/java-bigquery/issues/3877)) ([d2918da](https://github.com/googleapis/java-bigquery/commit/d2918da844cd20ca1602c6fcf9fa1df685f261fc))

### Python

### Changes for [google-cloud-bigquery](https://github.com/googleapis/python-bigquery)

#### [3.35.0](https://github.com/googleapis/python-bigquery/compare/v3.34.0...v3.35.0) (2025-07-15)

##### Features

* Add null\_markers property to LoadJobConfig and CSVOptions ([#2239](https://github.com/googleapis/python-bigquery/issues/2239)) ([289446d](https://github.com/googleapis/python-bigquery/commit/289446dd8c356d11a0b63b8e6275629b1ae5dc08))
* Add total slot ms to RowIterator ([#2233](https://github.com/googleapis/python-bigquery/issues/2233)) ([d44bf02](https://github.com/googleapis/python-bigquery/commit/d44bf0231e6e96369e4e03667a3f96618fb664e2))
* Add UpdateMode to update\_dataset ([#2204](https://github.com/googleapis/python-bigquery/issues/2204)) ([eb9c2af](https://github.com/googleapis/python-bigquery/commit/eb9c2aff242c5107f968bbd8b6a9d30cecc877f6))
* Adds dataset\_view parameter to get\_dataset method ([#2198](https://github.com/googleapis/python-bigquery/issues/2198)) ([28a5750](https://github.com/googleapis/python-bigquery/commit/28a5750d455f0381548df6f9b1f7661823837d81))
* Adds date\_format to load job and external config ([#2231](https://github.com/googleapis/python-bigquery/issues/2231)) ([7d31828](https://github.com/googleapis/python-bigquery/commit/7d3182802deccfceb0646b87fc8d12275d0a569b))
* Adds datetime\_format as an option ([#2236](https://github.com/googleapis/python-bigquery/issues/2236)) ([54d3dc6](https://github.com/googleapis/python-bigquery/commit/54d3dc66244d50a031e3c80d43d372d2743ecbc3))
* Adds source\_column\_match and associated tests ([#2227](https://github.com/googleapis/python-bigquery/issues/2227)) ([6d5d236](https://github.com/googleapis/python-bigquery/commit/6d5d23685cd457d85955356705c1101e9ec3cdcd))
* Adds time\_format and timestamp\_format and associated tests ([#2238](https://github.com/googleapis/python-bigquery/issues/2238)) ([371ad29](https://github.com/googleapis/python-bigquery/commit/371ad292df537278767dba71d81822ed57dd8e7d))
* Adds time\_zone to external config and load job ([#2229](https://github.com/googleapis/python-bigquery/issues/2229)) ([b2300d0](https://github.com/googleapis/python-bigquery/commit/b2300d032843512b7e4a5703377632fe60ef3f8d))

##### Bug Fixes

* Adds magics.context.project to eliminate issues with unit tests … ([#2228](https://github.com/googleapis/python-bigquery/issues/2228)) ([27ff3a8](https://github.com/googleapis/python-bigquery/commit/27ff3a89a5f97305fa3ff673aa9183baa7df200f))
* Fix rows returned when both start\_index and page\_size are provided ([#2181](https://github.com/googleapis/python-bigquery/issues/2181)) ([45643a2](https://github.com/googleapis/python-bigquery/commit/45643a2e20ce5d503118522dd195aeca00dec3bc))
* Make AccessEntry equality consistent with from\_api\_repr ([#2218](https://github.com/googleapis/python-bigquery/issues/2218)) ([4941de4](https://github.com/googleapis/python-bigquery/commit/4941de441cb32cabeb55ec0320f305fb62551155))
* Update type hints for various BigQuery files ([#2206](https://github.com/googleapis/python-bigquery/issues/2206)) ([b863291](https://github.com/googleapis/python-bigquery/commit/b86329188ba35e61871db82ae1d95d2a576eed1b))

##### Documentation

* Improve clarity of "Output Only" fields in Dataset class ([#2201](https://github.com/googleapis/python-bigquery/issues/2201)) ([bd5aba8](https://github.com/googleapis/python-bigquery/commit/bd5aba8ba40c2f35fb672a68eed11d6baedb304f))

### Feature

You can now use the [`DISTINCT` pipe operator](https://cloud.google.com/bigquery/docs/reference/standard-sql/pipe-syntax#distinct_pipe_operator) to select distinct rows from a table in your pipe syntax queries. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

---
## 2025-07-17

### Feature

You can now use the [`WITH` pipe operator](https://cloud.google.com/bigquery/docs/reference/standard-sql/pipe-syntax#with_pipe_operator) to define common table expressions in your pipe syntax queries. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

### Feature

You can now use [named windows](https://cloud.google.com/bigquery/docs/reference/standard-sql/pipe-syntax#select_pipe_operator) in your pipe syntax queries. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

---
## 2025-07-16

### Feature

You can now add comments to [notebooks](https://cloud.google.com/bigquery/docs/create-notebooks#create-notebook-console), [data canvases](https://cloud.google.com/bigquery/docs/data-canvas#work-with-data-canvas), [data preparation files](https://cloud.google.com/bigquery/docs/data-prep-get-suggestions#open-data-prep-editor), or [saved queries](https://cloud.google.com/bigquery/docs/work-with-saved-queries#create_saved_queries). You can also reply to existing comments or get a link to them. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

You can now create [BigQuery ML models by using the
Google Cloud console user interface](https://cloud.google.com/bigquery/docs/create-machine-learning-model-console). This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-07-15

### Feature

You can now [commercialize your BigQuery sharing listings on Google Cloud Marketplace](https://cloud.google.com/bigquery/docs/analytics-hub-cloud-marketplace). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

You can flatten [JSON columns](https://cloud.google.com/bigquery/docs/data-prep-get-suggestions#flatten-json) in BigQuery data preparation with a single operation. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-07-08

### Announcement

Starting August 1, 2025, GoogleSQL will become the default dialect for queries run from the command line interface (CLI) or API. To use LegacySQL, you will need to explicitly specify it in your requests or [set the configuration setting](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#alter_project_set_options_statement) `default_sql_dialect_option` to `'default_legacy_sql'` at the project or organization level.

---
## 2025-07-07

### Feature

You can now use your Google Account user credentials to authorize the execution of a data preparation in development. For more information, see
[Manually run a data preparation in development](https://cloud.google.com/bigquery/docs/orchestrate-data-preparations#run-undeployed-manually). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-07-01

### Feature

You can now [update a Cloud KMS encryption key](https://cloud.google.com/bigquery/docs/customer-managed-encryption#key_rotation) by updating the table with the same key. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

You can use the [`@@location` system variable](https://cloud.google.com/bigquery/docs/reference/system-variables) to set the location in which to run a query. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

BigQuery now supports the following Apache Hadoop migration features in [Preview](https://cloud.google.com/products#product-launch-stages):

* [Use the `dwh-migration-dumper` tool to migrate the metadata](https://cloud.google.com/bigquery/docs/hadoop-metadata) necessary for a Hadoop permissions and data migration.
* [Migrate permissions from Apache Hadoop, Apache Hive, and Ranger HDFS](https://cloud.google.com/bigquery/docs/hadoop-permissions-migration) to BigQuery.
* [Migrate tables from a HDFS data lake](https://cloud.google.com/bigquery/docs/hdfs-data-lake-transfer) to Google Cloud.

---
## 2025-06-30

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigquery](https://github.com/googleapis/java-bigquery)

#### [2.52.0](https://github.com/googleapis/java-bigquery/compare/v2.51.0...v2.52.0) (2025-06-25)

##### Features

* **bigquery:** Integrate Otel in client lib ([#3747](https://github.com/googleapis/java-bigquery/issues/3747)) ([6e3e07a](https://github.com/googleapis/java-bigquery/commit/6e3e07a22b8397e1e9d5b567589e44abc55961f2))
* **bigquery:** Integrate Otel into retries, jobs, and more ([#3842](https://github.com/googleapis/java-bigquery/issues/3842)) ([4b28c47](https://github.com/googleapis/java-bigquery/commit/4b28c479c1bc22326c8d2501354fb86ec2ce1744))

##### Bug Fixes

* **bigquery:** Add MY\_VIEW\_DATASET\_NAME*TEST* to resource clean up sample ([#3838](https://github.com/googleapis/java-bigquery/issues/3838)) ([b1962a7](https://github.com/googleapis/java-bigquery/commit/b1962a7f0084ee4c3e248266b50406cf575cd657))

##### Dependencies

* Remove version declaration of open-telemetry-bom ([#3855](https://github.com/googleapis/java-bigquery/issues/3855)) ([6f9f77d](https://github.com/googleapis/java-bigquery/commit/6f9f77d47596b00b7317c8a0d4a10c3d849ad57b))
* Update dependency com.google.api.grpc:proto-google-cloud-bigqueryconnection-v1 to v2.66.0 ([#3835](https://github.com/googleapis/java-bigquery/issues/3835)) ([69be5e7](https://github.com/googleapis/java-bigquery/commit/69be5e7345fb8ca69d633d9dc99cf6c15fa5227b))
* Update dependency com.google.api.grpc:proto-google-cloud-bigqueryconnection-v1 to v2.68.0 ([#3858](https://github.com/googleapis/java-bigquery/issues/3858)) ([d4ca353](https://github.com/googleapis/java-bigquery/commit/d4ca3535f54f3282aec133337103bbfa2c9a3653))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.49.2 ([#3853](https://github.com/googleapis/java-bigquery/issues/3853)) ([cf864df](https://github.com/googleapis/java-bigquery/commit/cf864df739bbb820e99999b7c1592a3635fea4ec))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.50.0 ([#3861](https://github.com/googleapis/java-bigquery/issues/3861)) ([eb26dee](https://github.com/googleapis/java-bigquery/commit/eb26deee37119389aee3962eea5ad67d63f26c70))
* Update dependency io.opentelemetry:opentelemetry-bom to v1.51.0 ([#3840](https://github.com/googleapis/java-bigquery/issues/3840)) ([51321c2](https://github.com/googleapis/java-bigquery/commit/51321c22778fd41134cc0cdfc70bdc47f05883f1))
* Update ossf/scorecard-action action to v2.4.2 ([#3810](https://github.com/googleapis/java-bigquery/issues/3810)) ([414f61d](https://github.com/googleapis/java-bigquery/commit/414f61d7efcfa568c1446bd41945d7a8e2450649))

### Feature

You can now [create and manage scheduled notebooks](https://cloud.google.com/bigquery/docs/orchestrate-notebooks) using the **Schedule details** pane in BigQuery Studio. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-06-26

### Feature

You can now use the
use the `PARTITION BY` clause of the
[`CREATE VECTOR INDEX` statement](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_vector_index_statement) to [partition TreeAH vector indexes](https://cloud.google.com/bigquery/docs/vector-index#partitions). Partitioning enables partition pruning and can decrease I/O costs. This feature is in [preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

[BigQuery search indexes](https://cloud.google.com/bigquery/docs/search-intro) provide free index management until your organization reaches the [limit](https://cloud.google.com/bigquery/quotas#index_limits) in a given region. You can now use the [`INFORMATION_SCHEMA.SEARCH_INDEXES_BY_ORGANIZATION` view](https://cloud.google.com/bigquery/docs/information-schema-indexes-by-organization) to understand your current consumption towards that limit, broken down by projects and tables. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-06-23

### Feature

You can now use the [Apache Iceberg REST catalog in BigLake metastore](https://cloud.google.com/bigquery/docs/blms-rest-catalog) to create interoperability between your query engines by allowing your open source engines to access Iceberg data in Cloud Storage. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

Colab Enterprise notebooks in BigQuery let you do the following in [Preview](https://cloud.google.com/products/#product-launch-stages):

* [Explain code with Gemini assistance](https://cloud.google.com/bigquery/docs/write-sql-gemini#explain_python_code)
* [Fix and explain errors with Gemini assistance](https://cloud.google.com/bigquery/docs/write-sql-gemini#fix_and_explain_python_errors)

---
## 2025-06-18

### Feature

You can now [publish the results of a data quality scan as Dataplex Universal Catalog metadata](https://cloud.google.com/bigquery/docs/data-quality-scan). Previously, data quality scan results were published only to the Google Cloud console. The latest results are saved to the entry that represents the source table. You can view the results in the Google Cloud console. If you want to enable catalog publishing for an existing data quality scan, you must edit the scan and re-enable the publishing option. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

You can now use data insights to have Gemini [generate table and column descriptions from table metadata](https://cloud.google.com/bigquery/docs/data-insights). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-06-16

### Feature

In BigQuery ML, you can now forecast multiple time series at once by using the [`TIME_SERIES_ID_COL` option](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-multivariate-time-series#time_series_id_col) that is available in `ARIMA_PLUS_XREG` multivariate time series models. Try this feature with the [Forecast multiple time series with a multivariate model](https://cloud.google.com/bigquery/docs/arima-plus-xreg-multiple-time-series-forecasting-tutorial) tutorial. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

### Feature

You can now manage [IAM tags](https://cloud.google.com/bigquery/docs/tags) on BigQuery datasets and tables using SQL. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

### Feature

The BigQuery migration assessment is now available for workflows that use [Cloudera and Apache Hadoop](https://cloud.google.com/bigquery/docs/migration-assessment#hadoop-cloudera). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

The [Merchant Center best sellers report](https://cloud.google.com/bigquery/docs/merchant-center-best-sellers-schema) supports multi-client accounts (MCAs). If you have an MCA, you can use the `aggregator_id` to query the tables. The `BestSellersEntityProductMapping` table maps the best-selling entities to the products in the sub-accounts' inventory. This provides a consolidated view of best-selling products, which you can then join with product data for more detailed insights. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

BigQuery now offers the following Gemini-enhanced SQL translation features:

* Create [Gemini-based configuration YAML files](https://cloud.google.com/bigquery/docs/config-yaml-translation#ai_yaml_guidelines) to generate AI suggestions for batch or interactive SQL translations. This feature is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).
* After making a batch SQL translation, review your translation output, including Gemini-based suggestions, using the [code tab](https://cloud.google.com/bigquery/docs/batch-sql-translator#code-tab) and [configuration tab](https://cloud.google.com/bigquery/docs/batch-sql-translator#configuration_tab). This feature is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).
* When making an interactive SQL translation, [create and apply Gemini-enhanced translation rules](https://cloud.google.com/bigquery/docs/interactive-sql-translator#create-apply-rules) to customize your SQL inputs. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-06-12

### Feature

Dark theme is now available for BigQuery in [Preview](https://cloud.google.com/products#product-launch-stages). To enable the dark theme, in the Google Cloud console, click **Settings and utilities > Preferences**. In the navigation menu, click **Appearance**, and then select your color theme and click **Save**.

---
## 2025-06-11

### Feature

The following GoogleSQL functions are now available in [preview](https://cloud.google.com/products#product-launch-stages):

* The [`ARRAY_FIRST` function](https://cloud.google.com/bigquery/docs/reference/standard-sql/array_functions#array_first) returns the first element of the input array.
* The [`ARRAY_LAST` function](https://cloud.google.com/bigquery/docs/reference/standard-sql/array_functions#array_last) returns the last element of the input array.
* The [`ARRAY_SLICE` function](https://cloud.google.com/bigquery/docs/reference/standard-sql/array_functions#array_slice) returns an array that contains consecutive elements from the input array.

---
## 2025-06-10

### Changed

An updated version of the [ODBC driver for BigQuery](https://cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#odbc_release_3121009) is now available.

### Feature

For [supported Gemini models](https://cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/supported-models), you can now use [Vertex AI Provisioned Throughput](https://cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/overview) with the [`ML.GENERATE_TEXT`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-text#provisioned-throughput)and [`AI.GENERATE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate#provisioned-throughput) functions to provide consistent high throughput for requests.

This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

---
## 2025-06-09

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigquery](https://github.com/googleapis/java-bigquery)

#### [2.51.0](https://github.com/googleapis/java-bigquery/compare/v2.50.1...v2.51.0) (2025-06-06)

##### Features

* **bigquery:** Job creation mode GA ([#3804](https://github.com/googleapis/java-bigquery/issues/3804)) ([a21cde8](https://github.com/googleapis/java-bigquery/commit/a21cde8994e93337326cc4a2deb4bafd1596b77f))
* **bigquery:** Support Fine Grained ACLs for Datasets ([#3803](https://github.com/googleapis/java-bigquery/issues/3803)) ([bebf1c6](https://github.com/googleapis/java-bigquery/commit/bebf1c610e6d050c49fc05f30d3fa0247b7dfdcb))

##### Dependencies

* Rollback netty.version to v4.1.119.Final ([#3827](https://github.com/googleapis/java-bigquery/issues/3827)) ([94c71a0](https://github.com/googleapis/java-bigquery/commit/94c71a090eab745c81dd9530bcdd3c8c1e734788))
* Update dependency com.google.api.grpc:proto-google-cloud-bigqueryconnection-v1 to v2.65.0 ([#3787](https://github.com/googleapis/java-bigquery/issues/3787)) ([0574ecc](https://github.com/googleapis/java-bigquery/commit/0574eccec2975738804be7d0ccb4c973459c82c9))
* Update dependency com.google.apis:google-api-services-bigquery to v2-rev20250511-2.0.0 ([#3794](https://github.com/googleapis/java-bigquery/issues/3794)) ([d3bf724](https://github.com/googleapis/java-bigquery/commit/d3bf724feef91469b44e1e5068738604d2b3cead))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#3811](https://github.com/googleapis/java-bigquery/issues/3811)) ([2c5ede4](https://github.com/googleapis/java-bigquery/commit/2c5ede4b115cf7cdd078d54d29ce93636c1cedf5))

### Feature

You can reference [Iceberg external tables in materialized views](https://cloud.google.com/bigquery/docs/materialized-views-create#iceberg) instead of migrating that data to BigQuery-managed storage. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

---
## 2025-06-04

### Changed

The organization-level [configuration settings](https://cloud.google.com/bigquery/docs/default-configuration) for `default_sql_dialect_option` and `query_runtime` are unsupported.

---
## 2025-06-03

### Feature

You can now use the [BigQuery advanced runtime](https://cloud.google.com/bigquery/docs/advanced-runtime) to improve query execution time and slot usage. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

BigQuery tables for Apache Iceberg have been renamed [BigLake tables for Apache Iceberg in BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables). This feature is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

BigQuery metastore has been renamed [BigLake metastore](https://cloud.google.com/bigquery/docs/about-blms) and is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). The feature formerly known as BigLake metastore has been renamed BigLake metastore (classic).

---
## 2025-06-02

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigquery](https://github.com/googleapis/nodejs-bigquery)

#### [8.1.0](https://github.com/googleapis/nodejs-bigquery/compare/v8.0.0...v8.1.0) (2025-05-29)

##### Features

* Job creation mode GA ([#1480](https://github.com/googleapis/nodejs-bigquery/issues/1480)) ([b51359a](https://github.com/googleapis/nodejs-bigquery/commit/b51359a61d93a5d9cff729221f457a50a5c7a52f))
* Support per-job reservation assignment ([#1477](https://github.com/googleapis/nodejs-bigquery/issues/1477)) ([8151e72](https://github.com/googleapis/nodejs-bigquery/commit/8151e72bb1e149f6f36f7acdba25629d208b1074))

### Go

### Changes for [bigquery/storage/apiv1beta1](https://github.com/googleapis/google-cloud-go/tree/main/bigquery/storage/apiv1beta1)

#### [1.69.0](https://github.com/googleapis/google-cloud-go/compare/bigquery/v1.68.0...bigquery/v1.69.0) (2025-05-27)

##### Features

* **bigquery/analyticshub:** Add support for Analytics Hub & Marketplace Integration ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery/analyticshub:** Adding allow\_only\_metadata\_sharing to Listing resource ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery/analyticshub:** Adding CommercialInfo message to the Listing and Subscription resources ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery/analyticshub:** Adding delete\_commercial and revoke\_commercial to DeleteListingRequest and RevokeSubscriptionRequest ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery/analyticshub:** Adding DestinationDataset to the Subscription resource ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery/analyticshub:** Adding routine field to the SharedResource message ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery:** Add support for dataset view and update modes ([#12290](https://github.com/googleapis/google-cloud-go/issues/12290)) ([7c1f961](https://github.com/googleapis/google-cloud-go/commit/7c1f9616b7ea95436582eb3c40c94e6bd9b48610))
* **bigquery:** Job creation mode GA ([#12225](https://github.com/googleapis/google-cloud-go/issues/12225)) ([1d8990d](https://github.com/googleapis/google-cloud-go/commit/1d8990dbf2563a5fbc96769ac9c6ea4ed06b239e))

### Python

### Changes for [google-cloud-bigquery](https://github.com/googleapis/python-bigquery)

#### [3.34.0](https://github.com/googleapis/python-bigquery/compare/v3.33.0...v3.34.0) (2025-05-27)

##### Features

* Job creation mode GA ([#2190](https://github.com/googleapis/python-bigquery/issues/2190)) ([64cd39f](https://github.com/googleapis/python-bigquery/commit/64cd39fb395c4a03ef6d2ec8261e1709477b2186))

##### Bug Fixes

* **deps:** Update all dependencies ([#2184](https://github.com/googleapis/python-bigquery/issues/2184)) ([12490f2](https://github.com/googleapis/python-bigquery/commit/12490f2f03681516465fc34217dcdf57000f6fdd))

##### Documentation

* Update query.py ([#2192](https://github.com/googleapis/python-bigquery/issues/2192)) ([9b5ee78](https://github.com/googleapis/python-bigquery/commit/9b5ee78f046d9ca3f758eeca6244b8485fe35875))
* Use query\_and\_wait in the array parameters sample ([#2202](https://github.com/googleapis/python-bigquery/issues/2202)) ([28a9994](https://github.com/googleapis/python-bigquery/commit/28a9994792ec90a6a4d16835faf2137c09c0fb02))

### Feature

In the navigation menu, you can now go to **Settings** and select **Configuration settings** to [customize the BigQuery Studio experience](https://cloud.google.com/bigquery/docs/bigquery-web-ui#navigation_menu) for users within the selected project or organization. This is achieved by showing or hiding user interface elements. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

### Feature

BigQuery now supports using [Spanner external datasets](https://cloud.google.com/bigquery/docs/spanner-external-datasets) with [authorized views](https://cloud.google.com/bigquery/docs/authorized-views), [authorized routines](https://cloud.google.com/bigquery/docs/authorized-routines), and [Cloud resource connections](https://cloud.google.com/bigquery/docs/create-cloud-resource-connection). This feature is [generally available](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages) (GA).

### Feature

The [`CREATE EXTERNAL TABLE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_external_table_statement) and [`LOAD DATA`](https://cloud.google.com/bigquery/docs/reference/standard-sql/load-statements) statements now support the following options in [preview](https://cloud.google.com/products/#product-launch-stages):

* `time_zone`: specify a time zone to use when loading data
* `date_format`, `datetime_format`, `time_format`, and `timestamp_format`: define how date and time values are formatted in your source files

### Feature

In the BigQuery console, in the **Welcome** tab, you can now try the [Apache Spark demo notebook](https://cloud.google.com/bigquery/docs/bigquery-web-ui#run_spark_notebook_demo_guide) that walks you through the basics of Spark notebook and showcases [serverless Spark in BigQuery](https://cloud.google.com/bigquery/docs/use-spark). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-05-29

### Feature

You can now use the `dbt-bigquery` adapter to run Python code that's defined in BigQuery DataFrames. For more information, see [Use BigQuery DataFrames in dbt](https://cloud.google.com/bigquery/docs/dataframes-dbt). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

### Feature

You can now use your Google Account user credentials to authorize the creation, scheduling, and running of pipelines as well as the scheduling of notebooks and data preparations. For more information, see [Create a pipeline schedule](https://cloud.google.com/bigquery/docs/schedule-pipelines#create-schedule). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

### Feature

You can now create [event-driven transfers](https://cloud.google.com/bigquery/docs/event-driven-transfer) when transferring data from Cloud Storage to BigQuery. Event-driven transfers can automatically trigger transfer runs when data in your Cloud Storage bucket has been modified or added. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

---
## 2025-05-28

### Feature

You can now create a [serverless Spark session and run PySpark code in a BigQuery notebook](https://cloud.google.com/bigquery/docs/use-spark). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

Column metadata indexing is now available for both [BigQuery tables](https://cloud.google.com/bigquery/docs/metadata-indexing-managed-tables) and [external tables](https://cloud.google.com/bigquery/docs/metadata-caching-external-tables). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

---
## 2025-05-27

### Feature

You can now [share Pub/Sub streaming data through BigQuery sharing](https://cloud.google.com/bigquery/docs/analytics-hub-stream-sharing) with additional [client libraries](https://cloud.google.com/bigquery/docs/reference/analytics-hub) support and provider usage metrics. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

BigQuery offers [optional job creation mode](https://cloud.google.com/bigquery/docs/running-queries#optional-job-creation) to speed up small queries that you use in your dashboards, data exploration, and other workflows. This mode automatically optimizes eligible queries and uses a cache to improve latency. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
