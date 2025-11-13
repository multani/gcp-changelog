# BigQuery

## 2025-11-11

### Feature

You can now use the
[interactive SQL translator](https://docs.cloud.google.com/bigquery/docs/interactive-sql-translator), the
[translation API](https://docs.cloud.google.com/bigquery/docs/api-sql-translator), and the
[batch SQL translator](https://docs.cloud.google.com/bigquery/docs/batch-sql-translator) to translate the
following SQL dialects into GoogleSQL:

* Apache Impala SQL
* GoogleSQL (BigQuery)

These features are in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

The BigQuery [Overview page](https://docs.cloud.google.com/bigquery/docs/bigquery-web-ui#open-overview)
is now your hub for discovering tutorials, features, and resources to help you
get the most out of BigQuery. It provides guided paths for users
of all skill levels. This feature is in
[Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

You can now use [custom constraints](https://docs.cloud.google.com/bigquery/docs/custom-constraints) with an
Organization Policy to provide more granular control over specific fields for
BigQuery dataset resources. This feature is [generally available](https://docs.cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-11-10

### Feature

You can [aggregate](https://docs.cloud.google.com/bigquery/docs/data-prep-get-suggestions#aggregate)
and [deduplicate](https://docs.cloud.google.com/bigquery/docs/data-prep-get-suggestions#deduplicate)
table data with Gemini assistance in your
[BigQuery data preparations](https://docs.cloud.google.com/bigquery/docs/data-prep-introduction).
These features are [generally available](https://docs.cloud.google.com/products#product-launch-stages) (GA).

### Feature

BigQuery ML now offers the
[`AI.DETECT_ANOMALIES` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-detect-anomalies).
Use the `AI.DETECT_ANOMALIES` function with a TimesFM model to
[detect anomalies](https://docs.cloud.google.com/bigquery/docs/anomaly-detection-overview)
in time series data, using historical data as a baseline.
This feature is in
[Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

BigQuery ML now supports the `TimesFM 2.5`
[time series foundational model](https://docs.cloud.google.com/bigquery/docs/timesfm-model).
You can use the `TimesFM 2.5` model in the
[`AI.FORECAST`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-forecast),
[`AI.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-evaluate),
and
[`AI.DETECT_ANOMALIES`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-detect-anomalies)
functions to achieve better forecasting accuracy and lower latency.

### Feature

Partitioning is now available for
[BigLake tables for Apache Iceberg in BigQuery](https://docs.cloud.google.com/bigquery/docs/iceberg-tables#use_partitioning).
This feature is in
[Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-11-06

### Announcement

The research paper [ARIMA\_PLUS: Large-scale, Accurate, Automatic and
Interpretable In-Database Time Series Forecasting and Anomaly Detection in
Google BigQuery](https://arxiv.org/abs/2510.24452) is now publicly available.
This paper describes the algorithms behind the
[`ARIMA_PLUS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-time-series)
and
[`ARIMA_PLUS_XREG`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-multivariate-time-series)
models for time series forecasting and anomaly detection, and demonstrates the
high performance, scalability, explainability, and customizability of the
models.

---
## 2025-11-05

### Feature

You can now generate [data insights](https://docs.cloud.google.com/bigquery/docs/data-insights#rest) when you
create a
[`DataScan`](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.dataScans)
using the Dataplex API. This feature is
[generally available](https://cloud.google.com/products/#product-launch-stages)
(GA).

### Feature

You can now
[generate table and column descriptions](https://docs.cloud.google.com/bigquery/docs/data-insights#generate-column-table-descriptions)
in all supported Gemini languages when you generate data insights.
This feature is
[generally available](https://cloud.google.com/products/#product-launch-stages)
(GA).

### Announcement

The [BigQuery Data Transfer Service for Google Ads](https://docs.cloud.google.com/bigquery/docs/google-ads-transfer) now supports [Google Ads API v21](https://developers.google.com/google-ads/api/fields/v21/overview).

### Feature

You can use the
[`MATCH_RECOGNIZE` clause](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#match_recognize_clause)
in your SQL queries to filter and aggregate matches across rows in a table.
This feature is
[generally available](https://cloud.google.com/products/#product-launch-stages)
(GA).

---
## 2025-11-04

### Feature

You can now use [custom organization policies with the BigQuery migration
service](https://docs.cloud.google.com/bigquery/docs/migration-custom-org-policies) to allow or deny specific
operations during a BigQuery migration to meet your organization's compliance
and security requirements. This includes an option to disable AI suggestions
during a migration. This feature is in
[Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-10-31

### Feature

We have [increased the row capacity](https://workspaceupdates.googleblog.com/2025/10/powerful-pivot-tables-connected-sheets.html)
for pivot tables backed by BigQuery in [Connected Sheets](https://docs.cloud.google.com/bigquery/docs/connected-sheets)
from 100,000 to 200,000 rows.

---
## 2025-10-30

### Feature

The
[Apache Iceberg REST catalog in BigLake metastore](https://docs.cloud.google.com/biglake/docs/blms-rest-catalog)
is now
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA) with several new features, including BigQuery catalog federation,
credential vending, and catalog management in the Google Cloud console.

---
## 2025-10-29

### Feature

You can now [group
reservations](https://docs.cloud.google.com/bigquery/docs/reservations-tasks#prioritize_idle_slots_with_reservation_groups)
together to prioritize idle slot sharing within the group. Reservations within a
reservation group share idle slots with each other before making them available
to other reservations in the project, giving you more control over slot
allocation for high-priority workloads. This feature is in
[Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-10-28

### Feature

Subscriber email logging lets you log the principal identifiers of users
who execute jobs and queries against linked datasets. You can enable
logging at the
[listing level](https://cloud.google.com/bigquery/docs/analytics-hub-manage-listings#create_a_listing)
and the
[data exchange level](https://cloud.google.com/bigquery/docs/analytics-hub-manage-exchanges#create-exchange).
The logged data is available in the `job_principal_subject` field of the
[`INFORMATION_SCHEMA.SHARED_DATASET_USAGE` view](https://docs.cloud.google.com/bigquery/docs/information-schema-shared-dataset-usage).
This feature is
[generally available](https://cloud.google.com/products#product-launch-stages).

### Feature

The BigQuery Data Transfer Service can now transfer data from the
following data sources:

* [Facebook Ads](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer)
* [Salesforce](https://docs.cloud.google.com/bigquery/docs/salesforce-transfer)
* [Salesforce Marketing Cloud](https://docs.cloud.google.com/bigquery/docs/sfmc-transfer)
* [ServiceNow](https://docs.cloud.google.com/bigquery/docs/servicenow-transfer)

Transfers from these data sources are now [generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

---
## 2025-10-27

### Feature

You can now [use the Data Engineering Agent](https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines)
to use Gemini in BigQuery to build and modify data
pipelines to ingest data into BigQuery. This feature is in
[preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

The administrative jobs explorer now includes a [job details
page](https://docs.cloud.google.com/bigquery/docs/admin-jobs-explorer#get-job-details) to help you diagnose
and troubleshoot queries. The **Performance** tab compiles query information
including the execution graph, SQL text, execution history, performance
variance, and system load during execution. You can also [compare two
jobs](https://docs.cloud.google.com/bigquery/docs/admin-jobs-explorer#compare-jobs) to identify discrepancies
and potential areas to improve query performance.

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

BigQuery now offers the following
[managed AI functions](https://docs.cloud.google.com/bigquery/docs/generative-ai-overview#managed_ai_functions)
that use Gemini to help you filter, join, rank, and classify your data:

* [`AI.IF`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-if):
  Filter and join text or multimodal data based on a condition described in natural language.
* [`AI.SCORE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-score):
  Rate text or multimodal input to rank your data by quality, similarity, or other criteria.
* [`AI.CLASSIFY`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-classify):
  Classify text into user-defined categories.

These functions are in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

You can now use the Apache Arrow format to
[stream data to BigQuery with the Storage Write API](https://docs.cloud.google.com/bigquery/docs/write-api#arrow-handling).
This feature is
[generally available](https://cloud.google.com/products/#product-launch-stages)
(GA).

---
## 2025-10-23

### Feature

BigQuery is now offering
[early access](https://cloud.google.com/products/#product-launch-stages)
to conversational analytics. Conversational analytics accelerates data analysis
by enabling quick insights through natural language. Users can chat with their
BigQuery data, create custom agents, and access those agents even outside of
BigQuery. To enroll in conversational analytics early access, fill out the
[request form](https://docs.google.com/forms/d/e/1FAIpQLSe5KhRr81uUce6mKj8YrV1iFezGIydTxOcx8wUTqcBJP3e7vg/viewform).

---
## 2025-10-22

### Feature

You can now use custom constraints with Organization Policy to provide more
granular control over specific fields for some BigQuery sharing
resources. For more information, see
[Manage Sharing data exchanges and listings using custom constraints](https://docs.cloud.google.com/bigquery/docs/analytics-hub-custom-constraints).
This feature is in
[preview](https://cloud.google.com/products#product-launch-stages).

### Issue

Support for
[table parameters in table-value functions (TVFs)](https://docs.cloud.google.com/bigquery/docs/table-functions#table_parameters)
has been temporarily disabled. We are working to restore this feature as soon
as possible.

### Feature

BigQuery ML now offers a built-in
[TimesFM univariate time series forecasting model](https://docs.cloud.google.com/bigquery/docs/timesfm-model)
that implements Google Research's open source TimesFM model. You can use
BigQuery ML's built-in TimesFM model with the following functions:

* Use
  [`AI.FORECAST`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-forecast)
  to perform forecasting. This function now supports a larger context window.
* Use
  [`AI.EVALUATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-evaluate)
  to evaluate forecasted data against a reference time series based on
  historical data.

To try using a TimesFM model with the `AI.FORECAST` function, see
[Forecast a time series with a TimesFM univariate model](https://docs.cloud.google.com/bigquery/docs/timesfm-time-series-forecasting-tutorial).

This feature is
[generally available](https://cloud.google.com/products/#product-launch-stages)
(GA).

---
## 2025-10-21

### Feature

BigQuery now supports TransUnion for
[entity resolution](https://docs.cloud.google.com/bigquery/docs/entity-resolution-setup).
This feature is
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

---
## 2025-10-20

### Feature

You can now use [visualization cells](https://docs.cloud.google.com/bigquery/docs/create-notebooks#cells) to
automatically
[generate a visualization](https://docs.cloud.google.com/bigquery/docs/visualize-data-colab)
of any DataFrame in your notebook.
You can customize the columns, chart type, aggregations, colors , labels, and
title.

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

In BigQuery ML, you can now fully manage open models as Vertex AI endpoints.
BigQuery-managed open models offer the following benefits:

* [Manage Vertex AI resource by using SQL queries](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-open#managed-resources)
* [Automatic or immediate open model undeployment](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-open#managed-model-undeployment)
  to save costs
* [Customize model deployment machine types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-open#machine-type)
  or reserve open model resources by
  [using Compute Engine reservations](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-open#reservation-affinity)

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-10-16

### Feature

The following features are now [generally available](https://cloud.google.com/products/#product-launch-stages) (GA) in BigQuery Studio:

* To streamline resource discovery and access, the [left Explorer
  pane](https://docs.cloud.google.com/bigquery/docs/bigquery-web-ui#explorer_panel) has been reorganized
  into three sections: Explorer, Classic Explorer, and Git repository. You can
  still use the Classic Explorer, which provides the complete resources tree.
* In the Explorer pane, you can use the [search
  feature](https://docs.cloud.google.com/bigquery/docs/bigquery-web-ui#explorer_pane) to find BigQuery
  resources in your organization. The results appear in a new tab in the
  details pane. You can use filters to narrow your search.
* You can access job histories by clicking [Job
  history](https://docs.cloud.google.com/bigquery/docs/managing-jobs) in the Explorer pane. A new tab opens
  that displays a list of job histories. BigQuery Studio no longer has a
  bottom pane for job history.
* To reduce tab proliferation, clicking a resource opens it within the same
  tab. To open the resource in a separate tab, press `Ctrl` (or
  `Command` on macOS) and click the resource. To prevent the current
  tab from getting its content replaced, double-click the tab. The name
  changes from italicized to regular font. If you still
  lose your resource, you can click tab\_recent Recent tabs in the
  details pane to find the resource.
* You can use breadcrumbs to navigate through different tabs and
  resources in the details pane.
* In the Home tab, the [What's new section](https://docs.cloud.google.com/bigquery/docs/bigquery-web-ui#welcome_tab)
  contains a list of new capabilities and changes to the BigQuery Studio.
* The notebook action bar is consolidated by default to give you more screen
  space for writing code.

### Feature

You can now access repositories by clicking Repositories in the Explorer pane.
A new tab opens that displays a list of repositories. The Explorer pane no
longer has a bottom pane for repositories. When you open a workspace in a
repository, it opens in the Git repository pane in the left pane. These
features are available in BigQuery Studio in
[preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-10-15

### Feature

You can
[visualize your geospatial query results](https://docs.cloud.google.com/bigquery/docs/geospatial-visualize)
on an interactive map in BigQuery Studio. This feature is
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

### Feature

You can use the `dbt-bigquery` adapter to run Python code that's defined in
BigQuery DataFrames. For more information, see
[Use BigQuery DataFrames in dbt](https://docs.cloud.google.com/bigquery/docs/dataframes-dbt).
This feature is
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

---
## 2025-10-14

### Feature

You can now use [SQL cells](https://docs.cloud.google.com/bigquery/docs/create-notebooks#cells) to write,
edit, and run SQL queries on your BigQuery data directly from your
notebooks. This feature is in
[Preview](https://cloud.google.com/products#product-launch-stages).

### Announcement

The BigQuery Data Transfer API (bigquerydatatransfer.googleapis.com) is now
enabled by default for every new Google Cloud project. This feature is
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

### Feature

You can now [embed natural language as comments in existing SQL to refine and
transform your code](https://docs.cloud.google.com/bigquery/docs/write-sql-gemini#generate_sql_from_a_comment).
This feature is [preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-09

### Feature

You can [allocate idle slots fairly](https://docs.cloud.google.com/bigquery/docs/slots#fairness) across
reservations within a single admin project. This ensures each reservation
receives an approximately equal share of available capacity. This feature is now
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

### Feature

You can set a [maximum slot
limit](https://docs.cloud.google.com/bigquery/docs/reservations-workload-management#predictable) for a
reservation. You can configure the maximum reservation size when creating or
updating a reservation. This feature is now [generally
available](https://cloud.google.com/products#product-launch-stages) (GA).

### Announcement

[Security, privacy, and compliance for Gemini in
BigQuery](https://docs.cloud.google.com/gemini/docs/bigquery/security-privacy-compliance) details how
customer data is protected and processed by Gemini in BigQuery.

### Changed

An updated version of the [ODBC driver for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers#odbc_release_3151022) is now available.

---
## 2025-10-08

### Breaking

The [default limit of `QueryUsagePerDay`](https://docs.cloud.google.com/bigquery/quotas#query_jobs) for
on-demand pricing has changed. The default limit of all new projects is now 200
TiB. For existing projects, the default limit has been set based on your
project's usage over the last 30 days. Projects that have [custom cost
controls](https://docs.cloud.google.com/bigquery/docs/custom-quotas) configured or that use
[reservations](https://docs.cloud.google.com/bigquery/docs/reservations-workload-management) aren't affected.
If the new limit might affect your workload, create a [custom cost
control](https://docs.cloud.google.com/bigquery/docs/custom-quotas) based on your workload needs.

### Feature

You can set [labels](https://docs.cloud.google.com/bigquery/docs/labels-intro) on reservations. These labels
can be used to organize your reservations and for billing analysis. This feature
is [generally
available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

You can [specify which reservation a query uses at
runtime](https://docs.cloud.google.com/bigquery/docs/reservations-workload-management#flexible), and [set IAM
policies directly on
reservations](https://docs.cloud.google.com/bigquery/docs/reservations-workload-management#securable). This
provides more flexibility and fine-grained control over resource management.
This feature is [generally
available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-10-07

### Announcement

As of February 25, 2025, enhancements to the [workload management
autoscaler](https://docs.cloud.google.com/bigquery/docs/slots-autoscaling-intro) that were announced on [July
31, 2024](https://docs.cloud.google.com/bigquery/docs/release-notes#July_31_2024) have rolled out to all users.
These enhancements are [generally
available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-10-06

### Feature

The [`INFORMATION_SCHEMA.SHARED_DATASET_USAGE` view](https://docs.cloud.google.com/bigquery/docs/information-schema-shared-dataset-usage#schema)
now includes the following schema fields to support usage metrics for
external tables and routines:

* `shared_resource_id`: the ID of the queried resource
* `shared_resource_type`: the type of the queried resource
* `referenced_tables`: Contains `project_id`,
  `dataset_id`, `table_id`, and `processed_bytes`
  fields of the base table.

These fields are
[generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

The BigQuery Data Transfer Service can now [transfer reporting data from Google Analytics 4](https://docs.cloud.google.com/bigquery/docs/google-analytics-4-transfer)
into BigQuery. You can also include custom reports from
Google Analytics 4 in your data transfer. This feature is
[generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

The BigQuery Data Transfer Service can now transfer data from the
following data sources:

* [PayPal](https://docs.cloud.google.com/bigquery/docs/paypal-transfer)
* [Stripe](https://docs.cloud.google.com/bigquery/docs/stripe-transfer)

Transfers from these data sources are supported in [preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

You can now set the priority of BigQuery jobs initiated by
Dataform workflows to run queries as interactive jobs that start
running as quickly as possible or as batch jobs with lower priority. For more
information, see
[Create a pipeline schedule](https://docs.cloud.google.com/bigquery/docs/schedule-pipelines#create-schedule)
and
[InvocationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig).
This feature is
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

### Announcement

Starting March 17, 2026, the BigQuery Data Transfer Service will require the
`bigquery.datasets.setIamPolicy` and the `bigquery.datasets.getIamPolicy`
permissions on the target dataset to create or update a transfer configuration.
For more information, see [Changes to dataset-level access controls](https://docs.cloud.google.com/bigquery/docs/dataset-access-control).

---
## 2025-10-02

### Feature

You can now use the [notebook gallery](https://docs.cloud.google.com/bigquery/docs/notebooks-introduction#notebook_gallery)
in the BigQuery web UI as your central hub for discovering and using prebuilt notebook
templates. This feature is in [preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-10-01

### Feature

You can now apply
[SQL query generated in the Gemini Cloud Assist chat](https://docs.cloud.google.com/bigquery/docs/write-sql-gemini#chat)
to the query open in your editor. This feature is in
[Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-09-29

### Feature

To simplify access management for your Iceberg tables, you
can use [credential vending mode with the Apache Iceberg REST catalog](https://docs.cloud.google.com/bigquery/docs/blms-rest-catalog) in BigLake metastore. Credential vending removes
the need for catalog users to have direct access to Cloud Storage buckets. This
feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

You can now create BigQuery
[non-incremental materialized views over Spanner data](https://docs.cloud.google.com/bigquery/docs/materialized-views-create#spanner)
to improve query performance by periodically caching results.
This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

BigQuery data preparation supports unnesting arrays, which expands each
array element into its own row for easier analysis. For more information, see
[Unnest arrays](https://docs.cloud.google.com/bigquery/docs/data-prep-get-suggestions#unnest-arrays).
This feature is [generally
available](https://cloud.google.com/products#product-launch-stages) (GA).

### Announcement

[History-based query optimizations](https://docs.cloud.google.com/bigquery/docs/history-based-optimizations)
are now enabled by default. If history-based optimizations have been previously
disabled, you can [re-enable history-based optimizations](https://docs.cloud.google.com/bigquery/docs/history-based-optimizations#enable-history-based-optimization)
for your project or organization.

---
## 2025-09-25

### Feature

The
[`ARRAY_FIRST`](https://cloud.google.com/bigquery/docs/reference/standard-sql/array_functions#array_first),
[`ARRAY_LAST`](https://cloud.google.com/bigquery/docs/reference/standard-sql/array_functions#array_last),
and
[`ARRAY_SLICE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/array_functions#array_slice)
GoogleSQL functions are now
[generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

BigQuery [data
canvas](https://cloud.google.com/bigquery/docs/data-canvas#destination_node) now
supports destination table nodes. Destination table nodes let you persist query
results to a new or existing table. This feature is [generally
available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-09-24

### Feature

BigQuery ML now supports
[visualization of model monitoring metrics](https://cloud.google.com/bigquery/docs/model-monitoring-overview#monitoring_visualization).
This feature lets you use charts and graphs to
[analyze model monitoring function output](https://cloud.google.com/vertex-ai/docs/model-monitoring/run-monitoring-job#analyze_monitoring_job_results).
You can use metric visualization with the
[`ML.VALIDATE_DATA_SKEW`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-skew)
and
[`ML.VALIDATE_DATA_DRIFT`](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-validate-data-drift)
functions. This feature is
[generally available](https://cloud.google.com/products/#product-launch-stages)
(GA).

### Feature

For command-line users, BigQuery is now integrated with the Gemini CLI to provide an agentic CLI experience. Using the dedicated [Gemini CLI extensions for BigQuery](https://cloud.google.com/bigquery/docs/develop-with-gemini-cli), you can search, explore, analyze, and gain insights from your data by asking natural language questions, generating forecasts, and running contribution analysis directly from the command line. This feature is available in beta.

---
## 2025-09-22

### Feature

You can now run federated queries against [PostgreSQL dialect databases in Spanner](https://cloud.google.com/spanner/docs/reference/postgresql/overview) using [BigQuery external datasets](https://cloud.google.com/bigquery/docs/spanner-external-datasets) with GoogleSQL; this includes [cross-region federated queries](https://cloud.google.com/bigquery/docs/spanner-federated-queries#cross_region_queries). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

### Libraries

### Python

#### [3.38.0](https://github.com/googleapis/python-bigquery/compare/v3.37.0...v3.38.0) (2025-09-15)

##### Features

* Add additional query stats ([#2270](https://github.com/googleapis/python-bigquery/issues/2270)) ([7b1b718](https://github.com/googleapis/python-bigquery/commit/7b1b718123afd80c0f68212946e4179bcd6db67f))

---
## 2025-09-16

### Feature

You can now [access snapshots of Apache Iceberg external tables](https://cloud.google.com/bigquery/docs/iceberg-external-tables#query_historical_data) that are retained in your Iceberg metadata by using the `FOR SYSTEM_TIME AS OF` clause. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

You can use the [`JSON_KEYS` function](https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#json_keys) to extract unique JSON keys from a JSON expression, and you can specify a [mode](https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#JSONPath_mode) for some JSON functions that take a JSONPath to allow more flexibility in how the path matches the JSON structure. These features are [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

[SQL code completion](https://cloud.google.com/bigquery/docs/write-sql-gemini) is now available for all BigQuery projects. To learn how to enable and activate Gemini in BigQuery features, see [Set up Gemini in BigQuery](https://cloud.google.com/gemini/docs/bigquery/set-up-gemini). This feature is available in [preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-15

### Feature

In the BigQuery Studio, in the Explorer pane, you can now [open saved queries in Connected Sheets](https://cloud.google.com/bigquery/docs/manage-saved-queries#open-saved-queries-in-sheets). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

You can now enable the [BigQuery advanced runtime](https://cloud.google.com/bigquery/docs/advanced-runtime) to improve query execution time and slot usage. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).
Between September 15, 2025 and early 2026, the BigQuery advanced runtime will become the default runtime for all projects.

### Libraries

### Java

#### [2.55.0](https://github.com/googleapis/java-bigquery/compare/v2.54.2...v2.55.0) (2025-09-12)

##### Features

* **bigquery:** Add custom ExceptionHandler to BigQueryOptions ([#3937](https://github.com/googleapis/java-bigquery/issues/3937)) ([de0914d](https://github.com/googleapis/java-bigquery/commit/de0914ddbccf988294d50faf56a515e58ab3505d))

##### Dependencies

* Update dependency com.google.cloud:google-cloud-bigquerystorage-bom to v3.17.0 ([#3954](https://github.com/googleapis/java-bigquery/issues/3954)) ([e73deed](https://github.com/googleapis/java-bigquery/commit/e73deed9c68a45023d02b40144c304329d6b5829))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#3952](https://github.com/googleapis/java-bigquery/issues/3952)) ([79b7557](https://github.com/googleapis/java-bigquery/commit/79b7557501d318fd92b90a681036fe6a1aa1bac4))

### Libraries

### Python

#### [3.37.0](https://github.com/googleapis/python-bigquery/compare/v3.36.0...v3.37.0) (2025-09-08)

##### Features

* Updates to fastpath query execution ([#2268](https://github.com/googleapis/python-bigquery/issues/2268)) ([ef2740a](https://github.com/googleapis/python-bigquery/commit/ef2740a158199633b5543a7b6eb19587580792cd))

##### Bug Fixes

* Remove deepcopy while setting properties for \_QueryResults ([#2280](https://github.com/googleapis/python-bigquery/issues/2280)) ([33ea296](https://github.com/googleapis/python-bigquery/commit/33ea29616c06a2e2a106a785d216e784737ae386))

##### Documentation

* Clarify that the presence of `XyzJob.errors` doesn't necessarily mean that the job has not completed or was unsuccessful ([#2278](https://github.com/googleapis/python-bigquery/issues/2278)) ([6e88d7d](https://github.com/googleapis/python-bigquery/commit/6e88d7dbe42ebfc35986da665d656b49ac481db4))
* Clarify the api\_method arg for client.query() ([#2277](https://github.com/googleapis/python-bigquery/issues/2277)) ([8a13c12](https://github.com/googleapis/python-bigquery/commit/8a13c12905ffcb3dbb6086a61df37556f0c2cd31))

---
## 2025-09-11

### Feature

Use the [BigQuery migration assessment for Informatica](https://cloud.google.com/bigquery/docs/migration-assessment) to assess the complexity of migrating data from your Informatica platform to BigQuery. This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

Gemini now recommends natural language prompts for you in the [SQL generation tool](https://cloud.google.com/bigquery/docs/write-sql-gemini#generate_a_sql_query). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

When you use the [Data Science Agent](https://cloud.google.com/bigquery/docs/colab-data-science-agent) in BigQuery, you can now use the Apache Spark or PySpark keywords in your prompt. The Data Science Agent is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-10

### Feature

You can [load files from Cloud Storage in BigQuery data preparations](https://cloud.google.com/bigquery/docs/data-prep-get-suggestions#create-new-from-gcs). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-09

### Feature

The [batch](https://cloud.google.com/bigquery/docs/batch-sql-translator) and [interactive translators](https://cloud.google.com/bigquery/docs/interactive-sql-translator) now caches your metadata, which can improve latency when you run a SQL translation. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Changed

You can now perform [supervised tuning](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model#supervised_tuning) on a BigQuery ML [remote model](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model) based on a Vertex AI `gemini-2.5-pro` or `gemini-2.5-flash-lite` model.

### Feature

You can configure reusable, default Cloud resource connections in a project. [Default connections](https://cloud.google.com/bigquery/docs/default-connections) are [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-09-08

### Feature

You can now add tables and views as tasks to BigQuery pipelines. For more information, see [Add a pipeline task](https://cloud.google.com/bigquery/docs/create-pipelines#add_a_pipeline_task). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

When you use the [Data Science Agent](https://cloud.google.com/bigquery/docs/colab-data-science-agent) in BigQuery, you can now use the `@` symbol to search for BigQuery tables in your project, and you can use the `+` symbol to search for files to upload. The Data Science Agent is in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

You can now include [table parameters](https://cloud.google.com/bigquery/docs/table-functions#table_parameters) when you create a table-valued function (TVF). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-03

### Feature

BigQuery now supports [soft failover](https://cloud.google.com/bigquery/docs/managed-disaster-recovery) with managed disaster recovery. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

You can [flatten records](https://cloud.google.com/bigquery/docs/data-prep-get-suggestions#flatten-records) in [BigQuery data preparation](https://cloud.google.com/bigquery/docs/data-prep-introduction) with a single operation. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

The `INFORMATION_SCHEMA.RESERVATIONS_TIMELINE` view now includes the [`per_second_details` schema field](https://cloud.google.com/bigquery/docs/information-schema-reservation-timeline#schema). This new field provides information regarding reservation capacity and usage on a per-second basis, and also includes details on autoscale utilization. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-09-02

### Feature

You can now create a [remote model based on an open embedding model from Vertex Model Garden or Hugging Face that is deployed to Vertex AI](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model-open). Options include E5 Embedding and other leading open embedding generation models. You can then use the [`ML.GENERATE_EMBEDDING` function](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-embedding) with this remote model to generate embeddings.

Try this feature with the [Generate text embeddings by using an open model and the `ML.GENERATE_EMBEDDING` function](https://cloud.google.com/bigquery/docs/generate-text-embedding-tutorial-open-models) tutorial.

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

You can now create a [remote model](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model) based on the Vertex AI `gemini-embedding-001` model. You can then use the [`ML.GENERATE_EMBEDDING` function](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-embedding) with this remote model to generate embeddings. This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

You can now reference BigQuery ML and DataFrames in your [prompts](https://cloud.google.com/bigquery/docs/colab-data-science-agent#sample-prompts) when you use the [Data Science Agent](https://cloud.google.com/bigquery/docs/colab-data-science-agent) in a BigQuery notebook. The Data Science Agent is in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

You can now configure listings for multiple regions for shared datasets and linked dataset replicas in BigQuery sharing. For more information, see [Create a listing](https://cloud.google.com/bigquery/docs/analytics-hub-manage-listings#create_a_listing). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

### Feature

You can now enable the automatic selection of a processing location in your pipeline configurations. For more information, see [Create pipelines](https://cloud.google.com/bigquery/docs/create-pipelines). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-09-01

### Libraries

### Go

#### [1.70.0](https://github.com/googleapis/google-cloud-go/compare/bigquery/v1.69.0...bigquery/v1.70.0) (2025-08-28)

##### Features

* **bigquery/reservation:** Add Reservation.max\_slots field to Reservation proto, indicating the total max number of slots this reservation can use up to ([f1de706](https://github.com/googleapis/google-cloud-go/commit/f1de7062db662aa6dfbf1e8cd2f0ac5df678e76d))
* **bigquery/reservation:** Add Reservation.scaling\_mode field and its corresponding enum message ScalingMode. This field should be used together with Reservation.max\_slots ([f1de706](https://github.com/googleapis/google-cloud-go/commit/f1de7062db662aa6dfbf1e8cd2f0ac5df678e76d))
* **bigquery/storage/managedwriter:** Allow overriding proto conversion mapping ([#12579](https://github.com/googleapis/google-cloud-go/issues/12579)) ([ce9d29b](https://github.com/googleapis/google-cloud-go/commit/ce9d29bf2ca22877c64c9eea5b5c6489de141cc5)), refs [#12578](https://github.com/googleapis/google-cloud-go/issues/12578)
* **bigquery:** Add load/extract job completion ratio ([#12471](https://github.com/googleapis/google-cloud-go/issues/12471)) ([3dab483](https://github.com/googleapis/google-cloud-go/commit/3dab483ad579c65ce520d6d9a2f8ad738ad68c9c))
* **bigquery:** Load job and external table opts for custom time format, null markers and source column match ([#12470](https://github.com/googleapis/google-cloud-go/issues/12470)) ([67b0320](https://github.com/googleapis/google-cloud-go/commit/67b0320a54be1ba7bc64eeee47a9afff14faac5f))

### Libraries

### Java

#### [2.54.2](https://github.com/googleapis/java-bigquery/compare/v2.54.1...v2.54.2) (2025-08-26)

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#3939](https://github.com/googleapis/java-bigquery/issues/3939)) ([794bf83](https://github.com/googleapis/java-bigquery/commit/794bf83e84efc0712638bebde5158777b9c89397))

---
## 2025-08-28

### Feature

For additional layers of security and control, you can now use query templates to predefine and limit the queries that can be run in data clean rooms. For more information, see [Use query templates](https://cloud.google.com/bigquery/docs/query-templates). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-08-26

### Feature

You can [deduplicate table data](https://cloud.google.com/bigquery/docs/data-prep-get-suggestions#deduplicate) with Gemini assistance in your [BigQuery data preparations](https://cloud.google.com/bigquery/docs/data-prep-introduction). Deduplication is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-08-25

### Feature

You can use the [`ST_REGIONSTATS` geography function](https://cloud.google.com/bigquery/docs/reference/standard-sql/geography_functions#st_regionstats) to combine raster data using Earth Engine with your vector data stored in BigQuery. For more information, see [Work with raster data](https://cloud.google.com/bigquery/docs/raster-data) and try the tutorial that shows you how to [use raster data to analyze global temperature](https://cloud.google.com/bigquery/docs/raster-tutorial-weather). This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

### Feature

You can now use data insights to have Gemini [generate table and column descriptions from table metadata](https://cloud.google.com/bigquery/docs/data-insights). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Libraries

### Python

#### [3.36.0](https://github.com/googleapis/python-bigquery/compare/v3.35.1...v3.36.0) (2025-08-20)

##### Features

* Add created/started/ended properties to RowIterator. ([#2260](https://github.com/googleapis/python-bigquery/issues/2260)) ([0a95b24](https://github.com/googleapis/python-bigquery/commit/0a95b24192395cc3ccf801aa9bc318999873a2bf))
* Retry query jobs if `jobBackendError` or `jobInternalError` are encountered ([#2256](https://github.com/googleapis/python-bigquery/issues/2256)) ([3deff1d](https://github.com/googleapis/python-bigquery/commit/3deff1d963980800e8b79fa3aaf5b712d4fd5062))

##### Documentation

* Add a TROUBLESHOOTING.md file with tips for logging ([#2262](https://github.com/googleapis/python-bigquery/issues/2262)) ([b684832](https://github.com/googleapis/python-bigquery/commit/b68483227693ea68f6b12eacca2be1803cffb1d1))
* Update README to break infinite redirect loop ([#2254](https://github.com/googleapis/python-bigquery/issues/2254)) ([8f03166](https://github.com/googleapis/python-bigquery/commit/8f031666114a826da2ad965f8ecd4727466cb480))

---
## 2025-08-22

### Feature

Multi-statement transactions are now available for [BigLake Iceberg tables in BigQuery](https://cloud.google.com/bigquery/docs/iceberg-tables#use_multi-statement_transactions). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-08-21

### Announcement

Starting September 25, 2025, the BigQuery Data Transfer Service for third-party SAAS and database connectors will update to a consumption-based pricing model. With this new pricing model, you will be charged based on the compute resources consumed by your data transfers, measured in slot-hours. For more information, see [Data Transfer Service pricing](https://cloud.google.com/bigquery/pricing#section-5). This pricing update applies to the following third-party connectors when they are [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

* [Facebook Ads](https://cloud.google.com/bigquery/docs/facebook-ads-transfer)
* [MySQL](https://cloud.google.com/bigquery/docs/mysql-transfer)
* [Oracle](https://cloud.google.com/bigquery/docs/oracle-transfer)
* [PostgreSQL](https://cloud.google.com/bigquery/docs/postgresql-transfer)
* [Salesforce](https://cloud.google.com/bigquery/docs/salesforce-transfer)
* [Salesforce Marketing Cloud](https://cloud.google.com/bigquery/docs/sfmc-transfer)
* [ServiceNow](https://cloud.google.com/bigquery/docs/servicenow-transfer)
* Other third-party connectors planned for future releases

---
## 2025-08-18

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigquery](https://github.com/googleapis/java-bigquery)

#### [2.54.1](https://github.com/googleapis/java-bigquery/compare/v2.54.0...v2.54.1) (2025-08-13)

##### Bug Fixes

* Adapt graalvm config to arrow update ([#3928](https://github.com/googleapis/java-bigquery/issues/3928)) ([ecfabc4](https://github.com/googleapis/java-bigquery/commit/ecfabc4b70922d0e697699ec5508a7328cadacf8))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#3924](https://github.com/googleapis/java-bigquery/issues/3924)) ([cb66be5](https://github.com/googleapis/java-bigquery/commit/cb66be596d1bfd0a5aed75f5a0e36d80269c7f6a))

### Feature

In the BigQuery console, you can now use the **Reference** panel to do the following:

* In the query editor, you can use the [Reference panel](https://cloud.google.com/bigquery/docs/running-queries#use-reference-panel) to preview the schema details of tables, snapshots, views, and materialized views, or open these resources in a new tab. You can also use the panel to construct new queries or edit existing queries by inserting query snippets or field names.
* In the notebook editor, you can use the [Reference panel](https://cloud.google.com/bigquery/docs/create-notebooks#create-notebook-console) to preview the schema details of tables, snapshots, views, or materialized views, or open these resources in a new tab.

This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

When you use the Data Science Agent in BigQuery, you can now use the [table selector](https://cloud.google.com/bigquery/docs/colab-data-science-agent#analyze-table) to choose one or more BigQuery tables to analyze. The Data Science Agent is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
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
