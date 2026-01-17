# Carbon Footprint

## 2026-01-01

### Issue

We have identified an issue resulting in incomplete Cloud Run emissions data for
November and December 2025. Customers may observe lower than actual emissions
for Cloud Run during this period. We are actively working on a fix and will
provide an update when the data correction is available.

---
## 2025-10-01

### Feature

Cloud Carbon Footprint launched an improved data export experience in the Cloud Carbon console, now available in Experimental Preview.

When you click **Data export** on the Cloud Carbon console Ul for a given billing account, you can now see Carbon Footprint exports that you have access to for that billing account, in addition to the ability to create a new data export. This feature helps you better manage your Carbon Footprint exports in BigQuery. [Read more](https://cloud.google.com/carbon-footprint/docs/export#manage) for details.

In some cases, the list of exports may not be complete for the following reasons:

* **Permissions**: The export was configured in a project that you don't have permission to view.
* **Performance Optimization**: To optimize performance and prevent latency when you have access to a very large number of projects, the search may not display exports in all projects.

---
## 2025-09-12

### Fixed

We have corrected an issue affecting the market-based Scope 2 emissions for the europe-west2 (London) region in the July 2025 Carbon Footprint data.

In the [July 2025 methodology update](https://cloud.google.com/carbon-footprint/docs/release-notes#August_14_2025), renewable energy coverage was misapplied to the Scope 2 market-based emissions in the europe-west2 (London) region. This resulted in non-zero Scope 2 market-based emissions for europe-west2. This inconsistency arose from evolving RE100 market-boundary guidance following Brexit. While RE100 guidance excludes the UK from the EU market-boundary post-Brexit, it allows for the use of previously purchased EU energy attribute certificates (EACs) with sufficiently close vintages to be applied against UK consumption in 2024. Google's application of these EACs to UK consumption results in zero Scope 2 market-based emissions in the europe-west2 (London).

We have corrected our data to align with the RE100 market boundaries guidance and our corporate environmental reporting of matched renewable energy. Scope 2 market-based emissions for europe-west2 are now correctly reported as zero for July 2025, using 2024 renewable energy coverage consistent with Google's environmental report.

* To correct your historical data, please [run a backfill](https://cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer_or_backfill) for July 2025 in your carbon footprint export. Due to a half-month lag in our data release, you will need to backfill the data for August 15, 2025, which will then update the July 2025 data in your BigQuery table.

Data for August 2025, available on September 15, 2025, will automatically reflect this correction. Data for all previous periods remains unaffected.

---
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
