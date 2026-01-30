# Dataplex

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
