# Dataplex

## 2026-04-28

### Announcement

Cloud Composer is now called [Managed Service for Apache Airflow](https://docs.cloud.google.com//composer/docs). The names for associated APIs, client libraries, CLI commands, and Identity and Access Management (IAM) remain unchanged and still
reference Composer.

### Announcement

**Dataproc** and **Google Cloud Serverless for Apache Spark** are now unified
under the [**Managed Service for Apache Spark**](https://docs.cloud.google.com/dataproc/docs)
brand. This change consolidates our managed Spark deployment options into a
single umbrella brand that includes the full breadth of our Spark capabilities.
No existing functionality is being removed as part of this change, and there
is no impact to the Dataproc API, metastore, client library, CLI, or IAM names.

---
## 2026-04-24

### Announcement

BigLake is now called [Google Cloud Lakehouse](https://docs.cloud.google.com/biglake/docs/introduction). BigLake metastore is now called the
[Lakehouse runtime catalog](https://docs.cloud.google.com/biglake/docs/about-blms).
The names for associated APIs, client libraries, CLI commands, and Identity and
Access Management (IAM) remain unchanged and still reference BigLake.

---
## 2026-04-20

### Feature

Knowledge Catalog discovers links between data assets, helping you understand how they connect and the nature of their relationships.
This feature is available in [preview](https://cloud.google.com/products#product-launch-stages).
For more information, see [View data relationships in Knowledge Catalog](https://cloud.google.com/dataplex/docs/data-relationships).

---
## 2026-04-17

### Feature

Data quality now supports rule reusability. You can now define data quality
rules as templates and reuse them across multiple catalog entries to standardize
your data quality processes. You can also use a shared library of
[system rule templates](https://docs.cloud.google.com/dataplex/docs/reuse-data-quality-rules#system-templates)
for common data validation scenarios. For more information, see
[Reuse data quality rules](https://docs.cloud.google.com/dataplex/docs/reuse-data-quality-rules).

### Feature

You can now build and run a Knowledge Catalog discovery agent to get more relevant search results for complex natural language queries.

For more information, see [Build an agent to discover your data](https://cloud.google.com/dataplex/docs/use-discovery-agent).

### Feature

To further refine lineage graphs, Knowledge Catalog lineage views include new
highlight and filter modes. This feature is available in
[preview](https://cloud.google.com/products#product-launch-stages).
For more information, see
[Apply filters and highlighting for a focused view](https://cloud.google.com/dataplex/docs/lineage-views#lineage-filtered-view).

---
## 2026-04-16

### Feature

Data insights for unstructured data transforms dark data or
unstructured files in the form of PDFs in Cloud Storage into structured,
queryable assets. This feature is now available in
[preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [About data insights for unstructured
data](https://docs.cloud.google.com/dataplex/docs/data-insights-unstructured-data).

---
## 2026-04-10

### Announcement

Dataplex Universal Catalog is now called Knowledge Catalog. The API, client
library, CLI, and Identity and Access Management (IAM) names remain unchanged.

### Feature

The lightweight profiling mode for data profile scans is available in
[preview](https://cloud.google.com/products#product-launch-stages).

The lightweight mode provides low-latency profile scans that return results in
seconds, making it ideal for grounding AI agent responses and interactive data
exploration. For more information, see [Profiling modes](https://cloud.google.com/dataplex/docs/data-profiling-overview#profiling_modes).

---
## 2026-04-09

### Feature

You can now specify a custom execution identity for data quality and
data profile scans. By default, scans are executed using the Service
Agent. You can now use a custom service account (Bring Your Own Service Account)
or End-User Credentials (EUC). Using a custom execution identity lets you
enforce the principle of least privilege, use fine-grained BigQuery access
controls, and unify scan processing costs directly under BigQuery.

For more information, see [Configure execution identity for data quality scans](https://cloud.google.com/dataplex/docs/use-auto-data-quality#configure-execution-identity) and [Configure execution identity for data profile scans](https://cloud.google.com/dataplex/docs/use-data-profiling#configure-execution-identity).

---
## 2026-03-30

### Feature

Automated cataloging of Looker (Google Cloud core) metadata as well as data
lineage ingestion from BigQuery sources are now available in
[preview](https://cloud.google.com/products#product-launch-stages). For more
information, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dataplex).

---
## 2026-03-23

### Feature

You can now specify a custom execution identity for data quality and
data profile scans. By default, scans are executed using the Service
Agent. You can now use a custom service account (Bring Your Own Service Account)
or End-User Credentials (EUC). Using a custom execution identity lets you
enforce the principle of least privilege, use fine-grained BigQuery access
controls, and unify scan processing costs directly under BigQuery.

For more information, see [Configure execution identity for data quality scans](https://cloud.google.com/dataplex/docs/use-auto-data-quality#configure-execution-identity) and [Configure execution identity for data profile scans](https://cloud.google.com/dataplex/docs/use-data-profiling#configure-execution-identity).

---
## 2026-02-24

### Feature

You can now save data profile aspects in Dataplex Universal Catalog up to 1 MB in size.
For more information, see
[Quotas and limits](https://cloud.google.com/dataplex/docs/quotas).

---
## 2026-02-19

### Feature

When you create a [data quality rule](https://cloud.google.com/dataplex/docs/auto-data-quality-overview#rule-definition),
you can now optionally include a
[debug query](https://cloud.google.com/dataplex/docs/auto-data-quality-overview#debug-queries)
to run alongside the rule. A debug query is a SQL statement that returns up to
10 scalar values to help diagnose rule failures. This feature is available in
[preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-02-11

### Feature

You can now use metadata change feeds to receive near real-time notifications
about metadata changes in Dataplex. Dataplex publishes notifications to a
Pub/Sub topic of your choice, letting you build event-driven workflows,
sync metadata to external catalogs, or trigger data quality checks.
For more information, see
[About metadata change feeds](https://cloud.google.com/dataplex/docs/metadata-change-feeds-overview).

---
## 2026-01-29

### Feature

You can control data lineage ingestion for Dataproc
at the organization, folder, or project level. This feature is in
[Preview](https://cloud.google.com/products#product-launch-stages).
For more information, see
[Control lineage ingestion](https://cloud.google.com/dataplex/docs/about-data-lineage#control-lineage-ingestion).

---
## 2026-01-12

### Breaking

Some of the metadata that is stored in Dataplex Universal Catalog is changing.
This change brings the metadata stored in Dataplex into consistency with
metadata from the original source systems such as Vertex AI, Bigtable, Spanner,
Pub/Sub, Dataform, and Dataproc Metastore. If you have workloads that depend on
such Dataplex metadata, you must adjust them to preserve continuity. For more
information about the scope of this change and what you need to do, see
[Changes to metadata stored in Dataplex Universal Catalog](https://cloud.google.com/dataplex/docs/metadata-changes).

---
## 2025-12-08

### Feature

[Natural language search](https://docs.cloud.google.com/dataplex/docs/search-assets) in Dataplex Universal
Catalog is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Natural language search extends keyword search to support natural language
queries. It lets you find resources using everyday language, eliminating the
need for complex syntax.

---
## 2025-11-21

### Feature

Data products in Dataplex Universal Catalog is now available in
[preview](https://cloud.google.com/products#product-launch-stages).

A data product serves as a logical, curated package of data assets designed to
solve a specific business problem. It enables faster time to insights and
provides trust, context, and self-service access request mechanisms for data
consumers. For more information, see
[About data products](https://docs.cloud.google.com/dataplex/docs/data-products-overview).

---
## 2025-11-17

### Feature

Previously, data profile scan results were published only to the Google Cloud console. You can now publish the results of a data profile scan as Dataplex Universal Catalog metadata. The latest results are saved to the entry that represents the source table. You can view the results in the Google Cloud console.

If you want to enable catalog publishing for an existing data profile scan, you must edit the scan and re-enable the publishing option.

For more information, see [Use data profiling](https://docs.cloud.google.com/dataplex/docs/use-data-profiling).

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-29

### Feature

Column-level lineage is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).
The feature provides a granular view of your data by tracking the flow between individual columns within tables. You can perform functions such as root cause analysis, impact analysis, and data source verification for specific columns. Column-level lineage is only supported for BigQuery jobs. For more information about column-level lineage, see [Column-level lineage](https://docs.cloud.google.com/dataplex/docs/lineage-views#column-level-lineage).

---
## 2025-09-23

### Feature

You can now connect your Dataplex Universal Catalog instance to your favorite developer tools, such as the Gemini CLI and other IDEs. This integration enables AI-driven data discovery and asset management directly within your development environment. For more information, see [Use Dataplex Universal Catalog with MCP, Gemini, and other agents](https://cloud.google.com/dataplex/docs/pre-built-tools-with-mcp-toolbox).

---
## 2025-09-03

### Feature

[Natural language search](https://cloud.google.com/dataplex/docs/search-assets) in Dataplex Universal Catalog is available in [preview](https://cloud.google.com/products#product-launch-stages).

Natural language search extends keyword search to support natural language queries. It lets you find resources using everyday language, eliminating the need for complex syntax.

---
## 2025-06-18

### Feature

Previously, data quality scan results were published only to the Google Cloud console. You can now publish the results of a data quality scan as Dataplex Universal Catalog metadata. The latest results are saved to the entry that represents the source table. You can view the results in the Google Cloud console.

If you want to enable catalog publishing for an existing data quality scan, you must edit the scan and re-enable the publishing option.

For more information, see [Use auto data quality](https://cloud.google.com/dataplex/docs/use-auto-data-quality).

This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

---
