# Dataform

## 2026-01-28

### Feature

You can
[organize your code assets into a hierarchical structure](https://docs.cloud.google.com/dataform/docs/organize-code-assets)
with folders and repositories using the Dataform API. This feature is in
[preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-01-19

### Breaking

[Dataform workflows](https://docs.cloud.google.com/dataform/docs/sql-workflows),
[BigQuery notebooks](https://docs.cloud.google.com/bigquery/docs/orchestrate-notebooks),
[pipelines](https://docs.cloud.google.com/bigquery/docs/schedule-pipelines),
and
[data preparations](https://docs.cloud.google.com/bigquery/docs/orchestrate-data-preparations)
are enforcing strict act-as mode at the project level. To avoid failures and
maintain automatic releases, you must use custom service accounts instead of the
default Dataform service agent across all repositories. You must also grant the
Service Account User role (`roles/iam.serviceAccountUser`) to the default
Dataform service agent and relevant principals. For more information and to
verify act-as permissions, see
[Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode).

---
## 2025-12-16

### Feature

[Strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode)
for Dataform is now
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA). This feature enhances security by requiring users to have the
`iam.serviceAccounts.actAs` permission on the service account used to run
workflows, ensuring a more secure and predictable permissions model for your
Dataform projects.

---
## 2025-12-15

### Feature

You can verify and resolve `iam.serviceAccounts.actAs` permission issues in
Dataform by checking Cloud Logging, interpreting log entries, and granting the
necessary IAM roles. For more information, see
[Verify act-as permissions for the effective service account](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode#verify-permissions).
This feature is in
[preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-12-09

### Feature

Dataform offers
[enhanced IAM permissions](https://docs.cloud.google.com/dataform/docs/access-control#use-config-api),
providing more granular control over resource creation and scheduling.
Administrators can also
[enable private workspaces](https://docs.cloud.google.com/dataform/docs/access-control#enable-private-workspaces)
to restrict access to the workspace creator. These features are in
[preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-11-18

### Feature

Dataform now lets you automate the creation of
[BigLake tables for Apache Iceberg in BigQuery](https://docs.cloud.google.com/dataform/docs/create-tables#create-iceberg-table).
This feature is
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

---
## 2025-11-13

### Feature

You can use custom constraints with Organization Policy to provide more
granular control over specific fields for the `CompilationResult`,
`ReleaseConfig`, `WorkflowConfig`, `WorkflowInvocation`, and `Workspace`
resources. For more information, see
[Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints).
This feature is
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

---
## 2025-10-06

### Feature

You can now use custom constraints with Organization Policy to provide more
granular control over specific fields for some Dataform
resources. For more information, see
[Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints).
This feature is
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

### Feature

You can now set the priority of BigQuery jobs in Dataform
to run queries as interactive jobs that start running as quickly as possible
or as batch jobs with lower priority. For more information, see
[Create a workflow configuration](https://docs.cloud.google.com/dataform/docs/schedule-runs#create-workflow-configuration)
and
[InvocationConfig](https://docs.cloud.google.com/dataform/reference/rest/v1/InvocationConfig).
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
