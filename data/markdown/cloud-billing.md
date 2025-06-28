# Cloud Billing

## 2025-06-27

### Changed

**New fields added to Cloud Billing data exports to BigQuery**

To prepare for expanding the spend-based committed use discounts (CUD)s program, we added new data fields to the schema for Cloud Billing standard and detailed data exports to BigQuery. These new fields add more information about the prices charged for your Google Cloud usage and consumption models.

To learn more, see [Billing data and SKU updates for spend-based CUDs](https://cloud.google.com/billing/docs/resources/multiprice-cuds).

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

