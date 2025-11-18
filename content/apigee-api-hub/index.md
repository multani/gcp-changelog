# Apigee API hub

## 2025-11-18

### Feature

**New API deployments view**

API deployment information is now available as a separate tab in the **API details** page. You can view your API deployment details, create new deployments, and manage existing deployments using the API deployments tab.

For more information, see [Manage deployments](https://docs.cloud.google.com/apigee/docs/apihub/manage-api-deployments).

### Fixed

The issue relating to [API hub provisioning failures in data residency enabled Apigee organizations](#November_03_2025) is now resolved. You can now provision API hub within an Apigee organization that has data residency enabled.

For information about provisioning API hub, see [Provision API hub in the Cloud console](https://docs.cloud.google.com/apigee/docs/apihub/provision).

### Changed

**New tutorial: Ingest Microsoft Azure API data into API hub**

A new tutorial is available for ingesting Microsoft Azure API data into API hub.

This tutorial shows you how to ingest API metadata from Azure API Management (APIM) into Apigee API hub. It uses a pre-built Application Integration template and a set of custom scripts on GitHub to perform a manual, on-demand ingestion of your API data.

For more information, see [Ingest Microsoft Azure API data into API hub](https://docs.cloud.google.com/apigee/docs/apihub/tutorials/ingest-azure-api-hub).

---
## 2025-11-04

### Feature

**Filter APIs by user-defined attributes**

You can now filter APIs using your custom, user-defined attributes from the **APIs** page in the Google Cloud console.

For more information, see [Filter resources based on attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources).

---
## 2025-11-03

### Issue

**API hub provisioning fails in data residency enabled Apigee organizations**

Currently, API hub can't be provisioned within an Apigee organization that has data residency enabled. Attempts to provision API hub in a data residency-enabled Apigee organization will result in a timeout error.

**Workaround:** There is no workaround available at this time. If your existing Apigee organization has data residency enabled, you will not be able to provision API hub until this limitation is resolved in a future release.

---
## 2025-10-28

### Feature

**API insights in API hub**

API insights is now available in API hub, providing a unified view of your API traffic and performance across all connected gateways. With API insights, you can gain a holistic understanding of your API ecosystem's health and quickly identify areas for optimization.

Currently, API insights supports data sources from Apigee, Apigee hybrid, Apigee Edge Public Cloud, and Apigee Edge Private Cloud (OPDK).

**Note:** Data residency (DRZ) and VPC-SC are not supported with API insights at this time.

For more information, see [API insights overview](https://cloud.google.com/apigee/docs/apihub/api-insights-overview).

### Feature

**Detailed API resource insights**

A new **Insights** tab is now available on the API details page, providing API-centric analytics to help you understand usage patterns and performance for each of your APIs.

You can now analyze key metrics such as total traffic, average TPS, request/response latencies, and more, directly from the API details page.

For more information, see [View API resource insights](https://cloud.google.com/apigee/docs/apihub/view-api-resource-insights).

---
## 2025-10-16

### Changed

**Create and manage API operations in the UI**

You can now create and manage API operations for your API versions from the **API details** page in the Google Cloud console.

For more information, see [Manage operations](https://cloud.google.com/apigee/docs/apihub/manage-operations).

---
## 2025-10-14

### Changed

**New MCP API style system attribute**

The system-defined API style attribute now includes a new value: **MCP**. This lets you classify and govern APIs based on the latest Model Context Protocol (MCP) standards.

For more information, see [System attributes](https://cloud.google.com/apigee/docs/apihub/manage-attributes#system-attributes).

---
## 2025-09-14

### Changed

**New MCP API style system attribute**

The system-defined API style attribute now includes a new value: **MCP**. This lets you classify and govern APIs based on the latest Model Context Protocol (MCP) standards.

For more information, see [System attributes](https://cloud.google.com/apigee/docs/apihub/manage-attributes#system-attributes).

---
## 2025-09-11

### Changed

**API hub navigation update**

The **API hub** section is now moved to the top level of the Apigee left navigation menu. This change improves discoverability and access to the API hub features.

### Libraries

Updated Go client library. For more information, see [apihub: v0.2.0](https://github.com/googleapis/google-cloud-go/releases/tag/apihub/v0.2.0).

---
## 2025-09-08

### Feature

**Enable and disable semantic search**

You can now enable and disable semantic search from the **API hub > Settings> Actions** page in the Google Cloud console.

For more information, see [Enable and disable semantic search](https://cloud.google.com/apigee/docs/apihub/search-apis#enable-semantic-search).

### Changed

**Automatic discovery of OpenAPI Spec from Apigee proxy resources**

API hub now automatically discovers and ingests valid OpenAPI specifications when they are included in an Apigee API proxy resource. This applies to all new and existing Apigee and Apigee hybrid runtime projects that are attached in API hub.

For more information, see [Auto-discovery of OpenAPI specs from Apigee proxies](https://cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#auto-oas-discovery).

### Deprecated

**Deprecation of Vertex AI Extensions in API hub**

The Vertex AI Extensions feature is no longer supported in API hub as of **September 8, 2025**.

---
## 2025-09-01

### Changed

**New API versions view**

API version information is now available as a separate tab in the **API details** page. You can view your API version details, copy API ID, create new API versions and more using the API versions tab.

For more information, see [Manage versions](https://cloud.google.com/apigee/docs/apihub/manage-versions).

---
## 2025-08-22

### Feature

**Deprovision API hub in the UI**

You can now deprovision an API hub instance from the **API hub > Settings > Actions** page in the Google Cloud console.

For more information, see [Deprovision Apigee API hub](https://cloud.google.com/apigee/docs/apihub/deprovision).

### Feature

**Create and delete custom plugins in the UI**

You can now create and delete custom plugins from the **API hub > Settings > Plugins** page in the Google Cloud console.

For more information, see [Create custom plugins](https://cloud.google.com/apigee/docs/apihub/create-custom-plugins) and [Manage custom plugins](https://cloud.google.com/apigee/docs/apihub/manage-custom-plugins).

---
## 2025-08-12

### Feature

**API observations in API hub ([Preview](https://cloud.google.com/products#product-launch-stages))**

API observations in API hub helps you tackle the challenges of undocumented and unmanaged APIs in your API infrastructure. It leverages Apigee [shadow API discovery](https://cloud.google.com/apigee/docs/api-observation/shadow-api-discovery) and uses automated discovery processes to bring all your APIs, **across Google Cloud projects**, into a unified, managed view.

For more information, see [API observations in API hub](https://cloud.google.com/apigee/docs/apihub/api-observation-overview).

**Note:** Rollouts of this feature will begin today, and may take five or more business days to be completed across all Google Cloud zones. You may not be able to view or use API observations until the rollout is complete. 

---
## 2025-07-31

### Feature

**New data source support for plugins**

API hub now supports importing API metadata through new dedicated plugins for the following data sources:

1. [Apigee Edge Public Cloud](https://docs.apigee.com/api-platform/get-started/apigee-edge-uapim)
2. [Apigee Edge Private Cloud (OPDK)](https://docs.apigee.com/private-cloud/v4.53.00/privatecloud-uapim-overview)

For more information, see [Plugins overview](https://cloud.google.com/apigee/docs/apihub/plugins).

### Feature

**Push-based plugin ingestion**

API hub now supports push-based plugin ingestion. This method allows for more real-time synchronization of API metadata. All new **Apigee, Apigee hybrid, Apigee Edge Public Cloud, and Apigee Edge Private Cloud (OPDK)** plugins are created with push-based ingestion by default.

For more information, see [Plugin data ingestion methods](https://cloud.google.com/apigee/docs/apihub/plugins#plugin-data-ingestion-methods).

**Note:** Rollouts of this feature will begin today, and may take five or more business days to be completed across all Google Cloud zones. You may not be able to create push-based plugins until the rollout is complete.

### Feature

**Create custom plugins [API only]**

You can now use the `Create Plugin` API to create custom plugins in API hub. Custom plugins are created manually to connect API hub to a specific API data source.

For more information, see [Create custom plugins](https://cloud.google.com/apigee/docs/apihub/create-custom-plugins).

### Issue

**Default Apigee plugin instance not auto-created during runtime attachment**

**Issue:** When provisioning API hub as part of Apigee provisioning, the default `Apigee X and hybrid` plugin instance is not automatically created. This prevents API proxies from being auto-registered.

**Workaround:** You can manually attach an Apigee runtime instance and import the Apigee assets. See [Attach a runtime project](https://cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#attach-a-runtime-project).

### Changed

**Delete plugin instance changes**

API hub no longer retains any ingested metadata from a plugin after its deletion. Deleting a plugin instance also permanently deletes all the associated API data from API hub.

For more information, see [Delete a plugin instance](https://cloud.google.com/apigee/docs/apihub/manage-plugin-instances#delete-plugin-instance).

### Changed

**Provisioning changes and Apigee API proxy registration**

API hub changed how it registers API proxies from Apigee and how it creates default plugin instances during provisioning.

API hub now automatically creates a default `Apigee X and hybrid` plugin instance and auto-registers API proxies only when you provision it as part of Apigee provisioning.

If you provision API hub directly from the API hub UI, API hub does not automatically create a default plugin instance, nor does it auto-register proxies.

For more information, see [Project attachments and plugins](https://cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#project-associations-and-plugins).

### Changed

**New tutorial: Enrich API data in API hub**

A new tutorial is available for enriching API data in Apigee API hub.

It shows you how to use API hub's custom curation features to automatically fetch OpenAPI specifications from a Cloud Storage bucket and associate them with their corresponding Apigee API proxies. The custom curation logic is defined using an integration in Application Integration.

For more information, see [Enrich API data with custom curation in API hub](https://cloud.google.com/apigee/docs/apihub/tutorials/enrich-api-data).

### Deprecated

**Deprecation of pull-based ingestion for Apigee plugins**

[Pull-based ingestion](https://cloud.google.com/apigee/docs/apihub/plugins#plugin-data-ingestion-methods) is no longer supported for `Apigee and Apigee hybrid` plugins as of **July 31, 2025**. For existing projects that have pull-based Apigee X and hybrid plugins configured, these plugins will continue to function and will be automatically migrated to the push-based type starting **August 2025**.

### Deprecated

**Deprecation of Apigee proxy deployment attributes**

As of **July 31st, 2025**, the `Apigee X and Hybrid Environment` and `Apigee X and Hybrid Organization` attributes will no longer be added to new Apigee proxy deployments. This change specifically applies when you import deployments into API hub by attaching a runtime project.

If your existing projects use these attributes in filtered search queries, we recommend updating them. To ensure your searches continue to work, use the `Source project` and `Source environment` fields as alternatives.

---
## 2025-07-22

### Changed

**API hub provisioning now enables Apigee API**

When you provision API hub, it now enables the Apigee API (`apigee.googleapis.com`) in your Google Cloud project. If Apigee isn't already provisioned, an Apigee organization is also automatically created in your project as part of the provisioning process.

API hub remains a free service. Enabling the Apigee API has no additional pricing or billing implications for your project.

For more information, see [Provision API hub in the Cloud console](https://cloud.google.com/apigee/docs/apihub/provision).

### Changed

**API hub deprovisioning changes**

Deprovisioning an API hub instance now also deletes any associated Apigee organizations from your Google Cloud project, provided those Apigee organizations have no Apigee instances.

If you deprovision an API hub instance, you can reprovision it later, but you'll need to wait 7 days before you can do so.

For more information, see [Deprovision Apigee API hub](https://cloud.google.com/apigee/docs/apihub/deprovision).

### Changed

**VPC Service Controls (VPC-SC) is GA**

VPC Service Controls in API hub is now [GA](https://cloud.google.com/products#product-launch-stages).

For more information, see [VPC Service Controls for API hub](https://cloud.google.com/apigee/docs/apihub/vpc-service-control).

---
## 2025-07-18

### Feature

**Apigee and hybrid plugin instance management**

You can now create and delete plugin instances for Apigee and Apigee Hybrid while associating the respective Apigee runtime projects to API hub.

For more information, see [Auto-register Apigee proxies](https://cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies).

### Breaking

**Apigee and Apigee hybrid plugin creation now requires source project ID**

When creating new instances of the **Apigee X and hybrid** plugin, you must now provide a source project ID. This source project ID is the Google Cloud project from which the plugin will import data.

This is a breaking change and will affect any existing API calls that create these plugins without explicitly providing this ID.

**Action Required:** Update your API calls to include the appropriate source project ID when creating new Apigee X and hybrid plugins. Failing to do so will result in creation errors.

### Changed

**Edit plugin instances changes**

You can now change or modify the name and curation logic of your plugin instance.

For more information, see [Edit a plugin instance](https://cloud.google.com/apigee/docs/apihub/manage-plugin-instances#edit-plugin-instance).

### Changed

**Resource URI format for Apigee deployments**

To ensure optimal functionality and consistency while creating or updating **Apigee** deployments, we now recommend that the **Resource URI** conforms to the following format:
`organizations/([^/]+)/environments/([^/]+)/apis/([^/]+)$`

For more information, see [Introduction to deployments](https://cloud.google.com/apigee/docs/apihub/deployments-intro).

---
## 2025-06-03

### Announcement

On June 3, 2025, we released an updated version of Apigee.

### Feature

**Apigee API hub is enabled for new Apigee organizations in supported regions.**

With this release, we are enabling [Apigee API hub](https://cloud.google.com/apigee/docs/apihub/what-is-api-hub) for new Apigee organizations [in regions where API hub is supported](https://cloud.google.com/apigee/docs/locations#available-apigee-api-analytics-regions). All new Apigee organizations, including hybrid organizations, that select an API hub-supported region *for their Apigee Analytics region* during provisioning will have access to API hub features at no additional cost.

API hub allows you to view, organize, and manage all of the APIs in your Apigee organization in one central location. To learn more, see [What is Apigee API hub?](https://cloud.google.com/apigee/docs/apihub/what-is-api-hub)

No action on your part is required to provision API hub for your organization, with the following exceptions:

* If your Apigee organization has Data Residency or VPC Service Controls enabled, you must configure your API hub instance manually to support these services. See [VPC Service Controls for API hub](https://cloud.google.com/apigee/docs/apihub/vpc-service-control) and [API hub and data residency](https://cloud.google.com/apigee/docs/apihub/locations#drz-api-hub) for more information.
* If your Apigee organization uses Customer-Managed Encryption Keys (CMEK), you must deprovision the Apigee API hub instance provided by default and recreate it to support CMEK. See [Deprovision Apigee API hub](https://cloud.google.com/apigee/docs/apihub/deprovision) and [Provision API hub in the Cloud console](https://cloud.google.com/apigee/docs/apihub/provision) for step-by-step instructions.

Contact [Google Cloud Support](https://cloud.google.com/apigee/docs/support/getting-started-with-support) for questions or assistance.

---
