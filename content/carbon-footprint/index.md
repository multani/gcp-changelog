# Carbon Footprint

## 2025-09-03

### Announcement

We recently released a new technical paper, ["Measuring the Environmental Impact of Delivering AI at Google Scale"](https://arxiv.org/abs/2508.15734) and [blogpost](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference). This research establishes a more comprehensive methodology for measuring the energy, emissions, and water consumption of AI inference in a live production environment. Our goal is to promote greater transparency and encourage the industry to align on more standardized, comprehensive measurement frameworks.

Currently, the data in Google Cloud Carbon Footprint for AI services does not fully reflect this comprehensive approach, which we believe is the most transparent environmental impact assessment from AI labs today. To better align with this new, more detailed methodology, we will be updating our carbon accounting pipeline for services that use AI, such as Vertex AI.

The new methodology provides a more accurate and complete picture of the environmental impact of AI services. We anticipate that this change, which will be implemented during our next semi-annual methodology refresh, may result in an increase in the emissions data for some of our Cloud AI services. However, we believe this move to more actionable data will enable us to more readily incentivize and track optimizations for these AI services.

The updated data will be released with the January 2026 methodology refresh, which is expected to be available in mid-February 2026. We believe this is an important step toward providing you with the most accurate and actionable data possible to manage your cloud usage more sustainably.

---
## 2025-08-14

### Changed

For the July 2025 semi-annual methodology refresh (released in mid-August 2025), we implemented the following improvements and updated the carbon model to version 14:

**Updating Scope 1 & 3 emissions from Google's corporate footprint**:

* Updated Scope 1 & 3 allocation factors using latest Google company-wide data from [2025 Google Environmental Report](https://www.sustainability.google/reports/google-2025-environmental-report/). See the [non-electricity emission sources section of methodology documentation](https://cloud.google.com/carbon-footprint/docs/methodology#non-electricity-allocation) on how we apply these Scope 1 & 3 emissions across Google products and services.

**Updating inputs for Scope 2 market-based emissions calculation from Google's corporate footprint**:

* Updated **annual** renewable electricity percentage from Google's clean energy procurement, in accordance with [2025 Google Environmental Report](https://www.sustainability.google/reports/google-2025-environmental-report/), as an input for Scope 2 market-based emissions.
* Updated annual emissions factors from latest government sources, in accordance with [2025 Google Environmental Report](https://www.sustainability.google/reports/google-2025-environmental-report/), as an input for Scope 2 market-based emissions. Note that Scope 2 location-based emissions are estimated using **hourly** greenhouse gas emissions factors. Read more about the difference in methodology between Scope 2 location-based and market-based emissions in the [methodology document](https://cloud.google.com/carbon-footprint/docs/methodology#market-based-allocation).

**Improving data accuracy**:

* A data issue impacting Cloud Run emissions calculations for March 2025 has been resolved. Incorrect carbon footprint data were generated for some Cloud Run SKUs due to a bug in our data processing logic, resulting in inflated carbon emission figures for affected users.
  + To correct your historical data, please [run a backfill](https://cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer_or_backfill) for March 2025 in your carbon footprint export. Due to a half-month lag in our data release, you will need to backfill the data for April 15, 2025, which will then update the March 2025 data in your BigQuery table. Data for all other periods remains unaffected.

**Updating service coverage**:

* Integration Connectors and Application Integration were removed from [covered services](https://cloud.google.com/carbon-footprint/docs/covered-services) of Carbon Footprint, due to potential mis-attribution of carbon to these services. We are actively investigating and working on the improvements. Once internal data mapping improves for a service, we plan to add it back.

**Deprecating carbon offsets fields from schema**:

* The `carbon_offsets_kgCO2e` and `carbon_footprint_total_kgCO2e.after_offsets` fields have been deprecated in the Carbon Footprint [schema](https://cloud.google.com/carbon-footprint/docs/data-schema) due to Google's strategic shift from traditional carbon offsets to a direct focus on carbon removal technologies and projects. If you have already set up an [export](https://cloud.google.com/carbon-footprint/docs/export), these two fields have been set to NULL and will not be updated.
* This change is in line with Google's evolving strategy for achieving its net-zero climate goals with more robust and impactful climate solutions such as carbon removal technologies. Read more about [Google's progress to accelerate carbon removal solutions](https://blog.google/outreach-initiatives/sustainability/our-progress-to-accelerate-carbon-removal-solutions/).

---
