# Cloud Billing

## 2025-07-16

### Feature

**Spend-based committed use discount (CUD) metadata export to BigQuery (public preview)**

You can now access spend-based CUD metadata programmatically through a BigQuery export. This data provides a comprehensive, daily snapshot of spend-based CUDs, which you can join with other billing data exports for improved CUD reporting and management.

[Learn more about the CUD metadata export](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export).

---
## 2025-07-07

### Feature

**Tags data for *regional* Secret Manager secret usage is available in both the [Standard usage cost export](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) and the [Detailed usage cost export](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).**

Tags for Global secrets have been available since [August 8, 2024](https://cloud.google.com/billing/docs/release-notes#August_08_2024). With this update, you can now tag *Regional secrets* as well.

To learn more about Tags, see [Tags overview](https://cloud.google.com/resource-manager/docs/tags/tags-overview). To learn about using Tags in your cost data exported to BigQuery, see [about tags](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and [query examples with tags](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags).

---
## 2025-06-27

### Changed

**New fields added to Cloud Billing data exports to BigQuery**

To prepare for expanding the spend-based committed use discounts (CUD)s program, we added new data fields to the schema for Cloud Billing standard and detailed data exports to BigQuery. These new fields add more information about the prices charged for your Google Cloud usage and consumption models.

To learn more, see [Billing data and SKU updates for spend-based CUDs](https://cloud.google.com/billing/docs/resources/multiprice-cuds).

---
## 2025-06-24

### Feature

**New, enhanced forecasting model for increased accuracy in cost reports**

Cloud Billing forecasts now better account for seasonality trends, data irregularities, and missing data, using an enhanced forecasting model that leverages AI to factor in various scenarios, such as the following:

* Intelligent handling of transient effects caused by known business events - for example, a new workload migration causing a usage spike.
* Deeper understanding of seasonality - for example, various recurring patterns, such as daily, weekly and monthly cycles in your cloud spend; or for retailers, increases in usage during holiday seasons.
* Adapting to trends to remain relevant in changing environments - for example, new AI spend.

These enhancements, powered by our new machine learning engine, translate to increased forecasting accuracy. By capturing complex trends, multiple seasonalities, and handling data anomalies more intelligently, you'll see a marked improvement in the precision of your cost forecasts.

For more information about the forecasted costs in reports, see
[View you forecasted costs](https://cloud.google.com/billing/docs/how-to/reports#cost-forecast).

---
