# BigQuery

## 2025-06-26 00:00:00-07:00

### Feature

You can now use the
use the `PARTITION BY` clause of the
[`CREATE VECTOR INDEX` statement](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_vector_index_statement) to [partition TreeAH vector indexes](https://cloud.google.com/bigquery/docs/vector-index#partitions). Partitioning enables partition pruning and can decrease I/O costs. This feature is in [preview](https://cloud.google.com/products/#product-launch-stages).### Feature

[BigQuery search indexes](https://cloud.google.com/bigquery/docs/search-intro) provide free index management until your organization reaches the [limit](https://cloud.google.com/bigquery/quotas#index_limits) in a given region. You can now use the [`INFORMATION_SCHEMA.SEARCH_INDEXES_BY_ORGANIZATION` view](https://cloud.google.com/bigquery/docs/information-schema-indexes-by-organization) to understand your current consumption towards that limit, broken down by projects and tables. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).## 2025-06-23 00:00:00-07:00

### Feature

You can now use the [Apache Iceberg REST catalog in BigLake metastore](https://cloud.google.com/bigquery/docs/blms-rest-catalog) to create interoperability between your query engines by allowing your open source engines to access Iceberg data in Cloud Storage. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).### Feature

Colab Enterprise notebooks in BigQuery let you do the following in [Preview](https://cloud.google.com/products/#product-launch-stages):

* [Explain code with Gemini assistance](https://cloud.google.com/bigquery/docs/write-sql-gemini#explain_python_code)
* [Fix and explain errors with Gemini assistance](https://cloud.google.com/bigquery/docs/write-sql-gemini#fix_and_explain_python_errors)## 2025-06-18 00:00:00-07:00

### Feature

You can now [publish the results of a data quality scan as Dataplex Universal Catalog metadata](https://cloud.google.com/bigquery/docs/data-quality-scan). Previously, data quality scan results were published only to the Google Cloud console. The latest results are saved to the entry that represents the source table. You can view the results in the Google Cloud console. If you want to enable catalog publishing for an existing data quality scan, you must edit the scan and re-enable the publishing option. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).### Feature

You can now use data insights to have Gemini [generate table and column descriptions from table metadata](https://cloud.google.com/bigquery/docs/data-insights). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).## 2025-06-16 00:00:00-07:00

### Feature

In BigQuery ML, you can now forecast multiple time series at once by using the [`TIME_SERIES_ID_COL` option](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-multivariate-time-series#time_series_id_col) that is available in `ARIMA_PLUS_XREG` multivariate time series models. Try this feature with the [Forecast multiple time series with a multivariate model](https://cloud.google.com/bigquery/docs/arima-plus-xreg-multiple-time-series-forecasting-tutorial) tutorial. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).### Feature

You can now manage [IAM tags](https://cloud.google.com/bigquery/docs/tags) on BigQuery datasets and tables using SQL. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).### Feature

The BigQuery migration assessment is now available for workflows that use [Cloudera and Apache Hadoop](https://cloud.google.com/bigquery/docs/migration-assessment#hadoop-cloudera). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).### Feature

The [Merchant Center best sellers report](https://cloud.google.com/bigquery/docs/merchant-center-best-sellers-schema) supports multi-client accounts (MCAs). If you have an MCA, you can use the `aggregator_id` to query the tables. The `BestSellersEntityProductMapping` table maps the best-selling entities to the products in the sub-accounts' inventory. This provides a consolidated view of best-selling products, which you can then join with product data for more detailed insights. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).### Feature

BigQuery now offers the following Gemini-enhanced SQL translation features:

* Create [Gemini-based configuration YAML files](https://cloud.google.com/bigquery/docs/config-yaml-translation#ai_yaml_guidelines) to generate AI suggestions for batch or interactive SQL translations. This feature is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).
* After making a batch SQL translation, review your translation output, including Gemini-based suggestions, using the [code tab](https://cloud.google.com/bigquery/docs/batch-sql-translator#code-tab) and [configuration tab](https://cloud.google.com/bigquery/docs/batch-sql-translator#configuration_tab). This feature is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).
* When making an interactive SQL translation, [create and apply Gemini-enhanced translation rules](https://cloud.google.com/bigquery/docs/interactive-sql-translator#create-apply-rules) to customize your SQL inputs. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).## 2025-06-12 00:00:00-07:00

### Feature

Dark theme is now available for BigQuery in [Preview](https://cloud.google.com/products#product-launch-stages). To enable the dark theme, in the Google Cloud console, click **Settings and utilities > Preferences**. In the navigation menu, click **Appearance**, and then select your color theme and click **Save**.## 2025-06-11 00:00:00-07:00

### Feature

The following GoogleSQL functions are now available in [preview](https://cloud.google.com/products#product-launch-stages):

* The [`ARRAY_FIRST` function](https://cloud.google.com/bigquery/docs/reference/standard-sql/array_functions#array_first) returns the first element of the input array.
* The [`ARRAY_LAST` function](https://cloud.google.com/bigquery/docs/reference/standard-sql/array_functions#array_last) returns the last element of the input array.
* The [`ARRAY_SLICE` function](https://cloud.google.com/bigquery/docs/reference/standard-sql/array_functions#array_slice) returns an array that contains consecutive elements from the input array.## 2025-06-10 00:00:00-07:00

### Changed

An updated version of the [ODBC driver for BigQuery](https://cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#odbc_release_3121009) is now available.### Feature

For [supported Gemini models](https://cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/supported-models), you can now use [Vertex AI Provisioned Throughput](https://cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/overview) with the [`ML.GENERATE_TEXT`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-text#provisioned-throughput)and [`AI.GENERATE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate#provisioned-throughput) functions to provide consistent high throughput for requests.

This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).## 2025-06-09 00:00:00-07:00

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
* Update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#3811](https://github.com/googleapis/java-bigquery/issues/3811)) ([2c5ede4](https://github.com/googleapis/java-bigquery/commit/2c5ede4b115cf7cdd078d54d29ce93636c1cedf5))### Feature

You can reference [Iceberg external tables in materialized views](https://cloud.google.com/bigquery/docs/materialized-views-create#iceberg) instead of migrating that data to BigQuery-managed storage. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).## 2025-06-04 00:00:00-07:00

### Changed

The organization-level [configuration settings](https://cloud.google.com/bigquery/docs/default-configuration) for `default_sql_dialect_option` and `query_runtime` are unsupported.## 2025-06-03 00:00:00-07:00

### Feature

You can now use the [BigQuery advanced runtime](https://cloud.google.com/bigquery/docs/advanced-runtime) to improve query execution time and slot usage. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).### Feature

BigQuery tables for Apache Iceberg have been renamed [BigLake tables for Apache Iceberg in BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables). This feature is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).### Feature

BigQuery metastore has been renamed [BigLake metastore](https://cloud.google.com/bigquery/docs/about-blms) and is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). The feature formerly known as BigLake metastore has been renamed BigLake metastore (classic).## 2025-06-02 00:00:00-07:00

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
* Use query\_and\_wait in the array parameters sample ([#2202](https://github.com/googleapis/python-bigquery/issues/2202)) ([28a9994](https://github.com/googleapis/python-bigquery/commit/28a9994792ec90a6a4d16835faf2137c09c0fb02))### Feature

In the navigation menu, you can now go to **Settings** and select **Configuration settings** to [customize the BigQuery Studio experience](https://cloud.google.com/bigquery/docs/bigquery-web-ui#navigation_menu) for users within the selected project or organization. This is achieved by showing or hiding user interface elements. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).### Feature

BigQuery now supports using [Spanner external datasets](https://cloud.google.com/bigquery/docs/spanner-external-datasets) with [authorized views](https://cloud.google.com/bigquery/docs/authorized-views), [authorized routines](https://cloud.google.com/bigquery/docs/authorized-routines), and [Cloud resource connections](https://cloud.google.com/bigquery/docs/create-cloud-resource-connection). This feature is [generally available](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages) (GA).### Feature

The [`CREATE EXTERNAL TABLE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_external_table_statement) and [`LOAD DATA`](https://cloud.google.com/bigquery/docs/reference/standard-sql/load-statements) statements now support the following options in [preview](https://cloud.google.com/products/#product-launch-stages):

* `time_zone`: specify a time zone to use when loading data
* `date_format`, `datetime_format`, `time_format`, and `timestamp_format`: define how date and time values are formatted in your source files### Feature

In the BigQuery console, in the **Welcome** tab, you can now try the [Apache Spark demo notebook](https://cloud.google.com/bigquery/docs/bigquery-web-ui#run_spark_notebook_demo_guide) that walks you through the basics of Spark notebook and showcases [serverless Spark in BigQuery](https://cloud.google.com/bigquery/docs/use-spark). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).## 2025-05-29 00:00:00-07:00

### Feature

You can now use the `dbt-bigquery` adapter to run Python code that's defined in BigQuery DataFrames. For more information, see [Use BigQuery DataFrames in dbt](https://cloud.google.com/bigquery/docs/dataframes-dbt). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).### Feature

You can now use your Google Account user credentials to authorize the creation, scheduling, and running of pipelines as well as the scheduling of notebooks and data preparations. For more information, see [Create a pipeline schedule](https://cloud.google.com/bigquery/docs/schedule-pipelines#create-schedule). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).### Feature

You can now create [event-driven transfers](https://cloud.google.com/bigquery/docs/event-driven-transfer) when transferring data from Cloud Storage to BigQuery. Event-driven transfers can automatically trigger transfer runs when data in your Cloud Storage bucket has been modified or added. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).## 2025-05-28 00:00:00-07:00

### Feature

You can now create a [serverless Spark session and run PySpark code in a BigQuery notebook](https://cloud.google.com/bigquery/docs/use-spark). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).### Feature

Column metadata indexing is now available for both [BigQuery tables](https://cloud.google.com/bigquery/docs/metadata-indexing-managed-tables) and [external tables](https://cloud.google.com/bigquery/docs/metadata-caching-external-tables). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).## 2025-05-27 00:00:00-07:00

### Feature

You can now [share Pub/Sub streaming data through BigQuery sharing](https://cloud.google.com/bigquery/docs/analytics-hub-stream-sharing) with additional [client libraries](https://cloud.google.com/bigquery/docs/reference/analytics-hub) support and provider usage metrics. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).### Feature

BigQuery offers [optional job creation mode](https://cloud.google.com/bigquery/docs/running-queries#optional-job-creation) to speed up small queries that you use in your dashboards, data exploration, and other workflows. This mode automatically optimizes eligible queries and uses a cache to improve latency. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).