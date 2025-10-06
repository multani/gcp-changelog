# Dataform

## 2025-10-06

### Feature

You can now set the priority of BigQuery jobs in Dataform
to run queries as interactive jobs that start running as quickly as possible
or as batch jobs with lower priority. For more information, see
[Create a workflow configuration](https://cloud.google.com/dataform/docs/schedule-runs#create-workflow-configuration)
and
[InvocationConfig](https://cloud.google.com/dataform/reference/rest/v1/InvocationConfig).
This feature is
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

---
## 2025-09-08

### Feature

You can now [update an incremental table schema without a full table refresh](https://cloud.google.com/dataform/docs/#change-schema-without-refresh). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-02

### Feature

Dataform now automatically selects a processing location based on the datasets referenced in your SQL queries. This makes setting the default location optional in your workflow configurations. For more information, see [About repository settings](https://cloud.google.com/dataform/docs/manage-repository#repository-settings). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-08-21

### Security

A security vulnerability was discovered in the Dataform API. This vulnerability could potentially allow unauthorized access to customer code repositories and data. For more information, see
[GCP-2025-045 security bulletin](https://cloud.google.com/dataform/docs/security-bulletins#gcp-2025-045).

---
## 2025-07-14

### Feature

Updates to the automatic cataloging of Dataform metadata in Dataplex improve the near real-time [management](https://cloud.google.com/dataplex/docs/catalog-overview) and [search](https://cloud.google.com/dataplex/docs/search-assets) capabilities for repository metadata. These features are [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-06-12

### Announcement

Dark theme is now available for BigQuery and Dataform. To turn on the dark theme, go to the Console, open the **Settings and utilities** menu next to your avatar, and select **Preferences**. On the **User preferences** page, select **Appearance** in the navigation, select your color theme, and save your selection.

---
## 2025-05-29

### Feature

You can now use your Google Account user credentials to authorize the creation, scheduling, and running of pipelines, the scheduling of notebooks and data preparations, and the creation of workflow configurations. For more information, see [Schedule runs](https://cloud.google.com/dataform/docs/schedule-runs). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-05-28

### Feature

You can now use strict act-as mode to enable an additional security check for certain user actions in Dataform. For more information, see [Use strict act-as mode](https://cloud.google.com/dataform/docs/strict-act-as-mode). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

---
