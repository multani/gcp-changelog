# Knowledge Catalog

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

### Feature

Automated cataloging of Iceberg REST Catalog (IRC) for Google Cloud
Lakehouse runtime catalog is now generally available
([GA](https://cloud.google.com/products#product-launch-stages)). This includes support for
lineage, data profiling, data quality, and data insights.

Federated support for Databricks Unity IRC, AWS Glue Data Catalog IRC, and
Snowflake Horizon IRC is available in
[preview](https://cloud.google.com/products#product-launch-stages).

For more information, see
[About metadata management in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview#supported-sources).

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
