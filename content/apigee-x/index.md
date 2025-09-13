# Apigee X

## 2025-09-12

### Announcement

On September 12, 2025, we released an updated version of Apigee (1-16-0-apigee-2).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Security

| Bug ID | Description |
| --- | --- |
| **N/A** | **Security fix for `apigee-runtime`.** |

---
## 2025-09-11

### Changed

**API hub navigation update**

The **API hub** section is now moved to the top level of the Apigee left navigation menu. This change improves discoverability and access to the API hub features.

---
## 2025-09-09

### Announcement

On September 9, 2025, we released an updated version of Apigee (1-16-0-apigee-1).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Changed

| Bug ID | Description |
| --- | --- |
| **N/A** | **Updates to security infrastructure and libraries.** |

---
## 2025-09-04

### Announcement

On September 4, 2025, we released an updated version of Apigee.

### Feature

**Apigee policies for LLM/GenAI workloads are Generally Available (GA)**

Four new Apigee policies supporting LLM/GenAI workloads are now [GA](https://cloud.google.com/products#product-launch-stages):

* [SemanticCacheLookup policy](https://cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy)
* [SemanticCachePopulate policy](https://cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy)
* [SanitizeUserPrompt](https://cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy)
* [SanitizeModelResponse](https://cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy)

The Apigee semantic caching policies enable intelligent response reuse based on semantic similarity. Using these policies in your Apigee API proxies can minimize redundant backend API calls, reduce latency, and lower operational costs. With this release, the semantic caching policies support URL templating, enabling the use of variables for AI model endpoint values.

The Model Armor policies protect your AI applications by sanitizing user prompts to and responses from large language models (LLMs). Using these policies in your Apigee API proxies can mitigate the risks associated with LLM usage by leveraging Model Armor to detect prompt injection, prevent jailbreak attacks, apply responsible AI filters, filter malicious URLs, and protect sensitive data.

For more information on using these policies in your Apigee API proxies, see:

* [Get started with semantic caching policies](https://cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies)
* [Get started with Apigee Model Armor policies](https://cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies)

---
## 2025-09-03

### Announcement

On September 3, 2025, we released an updated version of Apigee.

### Feature

**Apigee Server-Sent Events (SSE) and EventFlows are supported for use with the Apigee Extension Processor.**

The Apigee SSE feature enables continuous response streaming from server-sent event (SSE) endpoints to clients in real time. To learn more about this feature, see [Streaming server-sent events](https://cloud.google.com/apigee/docs/api-platform/develop/server-sent-events).

The Apigee Extension Processor is a [traffic extension](https://cloud.google.com/service-extensions/docs/overview#integration-lb) that lets you use Cloud Load Balancing to send callouts from the data processing path of the application load balancer to the Apigee Extension Processor. To learn more, see the [Apigee Extension Processor overview](https://cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-overview).

---
## 2025-08-27

### Announcement

On August 27, 2025, we released an updated version of Apigee (1-15-0-apigee-9).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Security

| Bug ID | Description |
| --- | --- |
| **427752569** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:  * [CVE-2025-22872](https://nvd.nist.gov/vuln/detail/CVE-2025-22872) * [CVE-2025-22870](https://nvd.nist.gov/vuln/detail/CVE-2025-22870) * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868) * [CVE-2025-22869](https://nvd.nist.gov/vuln/detail/CVE-2025-22869) |

### Fixed

| Bug ID | Description |
| --- | --- |
| **420901514** | **Enhanced WebSocket authentication.** |
| **429245088** | **Implemented option to override endpoints in the PublishMessage policy.** |
| **405039175** | **Resolved issue causing duplicate x-b3-\* headers when Distributed Trace is enabled.** |
| **378686709** | **Resolved issue causing unexpected `404` errors when using wildcards in proxy basepaths.** |
| **429245268** | **Implemented option to override endpoints in the MessageLogging policy.** |
| **N/A** | **Updates to security infrastructure and libraries.** |

---
## 2025-08-04

### Announcement

On August 4, 2025, we released an updated version of Apigee (1-15-0-apigee-8).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Feature

**Server-sent events and EventFlows are [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages)**

Apigee supports continuous response streaming from server-sent event (SSE) endpoints to clients in real time. The Apigee SSE feature is useful for handling large language model (LLM) APIs that operate most effectively by streaming their responses back to the client. SSE streaming reduces latency, and clients can receive response data as soon as it is generated by an LLM. This feature supports the use of AI agents that operate in real time environments, such as customer service bots or workflow orchestrators. For more information, see [Streaming server-sent events](https://cloud.google.com/apigee/docs/api-platform/develop/server-sent-events).

Streaming from SSE endpoints is available in Apigee and in Apigee hybrid v1.15.0 and newer.

### Fixed

| Bug ID | Description |
| --- | --- |
| **435620966** | **Fixed a regression that occurred when upgrading from ASM 1.22 to 1.23 that resulted in 503 errors.** |
| **422195061** | **Enhanced cache lookup performance.** |
| **269573358** | **Resolved issue with OASValidation policy schema references for parameters without body validation** The OASValidation policy correctly resolves and validates schemas passed by reference (`$ref`) for header, path, and query parameters, even when the <ValidateMessageBody> flag is set to `false`. |
| **421141062** | **Increased OAS validation limit to 20MB in JSON payloads to prevent validation failures.** |
| **417200603** | **Improved API connection stability to prevent premature timeouts for long-running requests.** |
| **423597917** | **`POST` operations for AppGroupApp keys updated** `POST` operations for AppGroup app keys now insert scopes and attributes instead of appending these values. This behavior is consistent with `POST` operations for companies in Apigee Edge for Public Cloud. |
| **390234048** | **Resolved issue resulting in missing fields in API responses for Monetization rate plans** The `createdAt` and `lastModifiedAt` fields are now present in responses from the `organizations.apiproducts.rateplans` API. |
| **422757662** | **Reverted problematic commit regarding X-b3 trace headers send when using distributed tracing.** |
| **409048431** | **Fixed a SAML signature verification bypass vulnerability.** |
| **N/A** | **Updates to security infrastructure and libraries.** |

---
## 2025-07-30

### Announcement

On July 30, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

* Develop > API Proxies
* Develop > Shared Flows
* Develop > Offline Debug

See [Apigee UI in Cloud console navigation](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

---
## 2025-07-28

### Announcement

On July 28, 2025, we released an updated version of Apigee (1-15-0-apigee-7).

**Note:** This release has been rolled back to address am issue. See entry for [August 4, 2025](https://cloud.google.com/apigee/docs/release-notes#August_04_2025) for the updated version number and payload.

### Feature

**Server-sent events and EventFlows are [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages)**

Apigee supports continuous response streaming from server-sent event (SSE) endpoints to clients in real time. The Apigee SSE feature is useful for handling large language model (LLM) APIs that operate most effectively by streaming their responses back to the client. SSE streaming reduces latency, and clients can receive response data as soon as it is generated by an LLM. This feature supports the use of AI agents that operate in real time environments, such as customer service bots or workflow orchestrators. For more information, see [Streaming server-sent events](https://cloud.google.com/apigee/docs/api-platform/develop/server-sent-events).

Streaming from SSE endpoints is available in Apigee and in Apigee hybrid v1.15.0 and newer.

### Fixed

| Bug ID | Description |
| --- | --- |
| **422195061** | **Enhanced cache lookup performance.** |
| **269573358** | **Resolved issue with OASValidation policy schema references for parameters without body validation** The OASValidation policy correctly resolves and validates schemas passed by reference (`$ref`) for header, path, and query parameters, even when the <ValidateMessageBody> flag is set to `false`. |
| **421141062** | **Increased OAS validation limit to 20MB in JSON payloads to prevent validation failures.** |
| **417200603** | **Improved API connection stability to prevent premature timeouts for long-running requests.** |
| **423597917** | **`POST` operations for AppGroupApp keys updated** `POST` operations for AppGroup app keys now insert scopes and attributes instead of appending these values. This behavior is consistent with `POST` operations for companies in Apigee Edge for Public Cloud. |
| **390234048** | **Resolved issue resulting in missing fields in API responses for Monetization rate plans** The `createdAt` and `lastModifiedAt` fields are now present in responses from the `organizations.apiproducts.rateplans` API. |
| **422757662** | **Reverted problematic commit regarding X-b3 trace headers send when using distributed tracing.** |
| **409048431** | **Fixed a SAML signature verification bypass vulnerability.** |
| **N/A** | **Updates to security infrastructure and libraries.** |

---
## 2025-07-24

### Announcement

On July 24, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

* Publish > Portals

See [Apigee UI in Cloud console navigation](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

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
## 2025-06-02

### Announcement

On June 2, 2025, we released an updated version of Apigee (1-15-0-apigee-5).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Feature

**New flow variables available for VerifyAPIKey policy**

Two new flow variables have been added to the [VerifyAPIKey](https://cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) policy.

* `app_group_app`
* `app_group_name`

To learn more, see [Using flow variables](https://cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables).

### Fixed

| Bug ID | Description |
| --- | --- |
| **410670597** | **Fixed the proxy response count metric (`proxy/response_count`) for EventFlow-enabled streaming proxies.** |
| **375360455** | **Resolved issues with connection termination when using HTTP streaming** Added automatic retries for connection reset due to upstream services. |
| **N/A** | **Updates to security infrastructure and libraries.** |
| **N/A** | **`x-b3` trace headers will be sent only when distributed tracing is enabled.** In previous releases Apigee was sending `x-b3` trace headers even when distributed tracing was disabled. This was an unexpected behavior which is fixed in this release. |

BigQuery
--------

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigquery](https://github.com/googleapis/nodejs-bigquery)

#### [8.1.0](https://github.com/googleapis/nodejs-bigquery/compare/v8.0.0...v8.1.0) (2025-05-29)

##### Features

* Job creation mode GA ([#1480](https://github.com/googleapis/nodejs-bigquery/issues/1480)) ([b51359a](https://github.com/googleapis/nodejs-bigquery/commit/b51359a61d93a5d9cff729221f457a50a5c7a52f))
* Support per-job reservation assignment ([#1477](https://github.com/googleapis/nodejs-bigquery/issues/1477)) ([8151e72](https://github.com/googleapis/nodejs-bigquery/commit/8151e72bb1e149f6f36f7acdba25629d208b1074))

### Go

### Changes for [bigquery/storage/apiv1beta1](https://github.com/googleapis/google-cloud-go/tree/main/bigquery/storage/apiv1beta1)

#### [1.69.0](https://github.com/googleapis/google-cloud-go/compare/bigquery/v1.68.0...bigquery/v1.69.0) (2025-05-27)

##### Features

* **bigquery/analyticshub:** Add support for Analytics Hub & Marketplace Integration ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery/analyticshub:** Adding allow\_only\_metadata\_sharing to Listing resource ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery/analyticshub:** Adding CommercialInfo message to the Listing and Subscription resources ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery/analyticshub:** Adding delete\_commercial and revoke\_commercial to DeleteListingRequest and RevokeSubscriptionRequest ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery/analyticshub:** Adding DestinationDataset to the Subscription resource ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery/analyticshub:** Adding routine field to the SharedResource message ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **bigquery:** Add support for dataset view and update modes ([#12290](https://github.com/googleapis/google-cloud-go/issues/12290)) ([7c1f961](https://github.com/googleapis/google-cloud-go/commit/7c1f9616b7ea95436582eb3c40c94e6bd9b48610))
* **bigquery:** Job creation mode GA ([#12225](https://github.com/googleapis/google-cloud-go/issues/12225)) ([1d8990d](https://github.com/googleapis/google-cloud-go/commit/1d8990dbf2563a5fbc96769ac9c6ea4ed06b239e))

### Python

### Changes for [google-cloud-bigquery](https://github.com/googleapis/python-bigquery)

#### [3.34.0](https://github.com/googleapis/python-bigquery/compare/v3.33.0...v3.34.0) (2025-05-27)

##### Features

* Job creation mode GA ([#2190](https://github.com/googleapis/python-bigquery/issues/2190)) ([64cd39f](https://github.com/googleapis/python-bigquery/commit/64cd39fb395c4a03ef6d2ec8261e1709477b2186))

##### Bug Fixes

* **deps:** Update all dependencies ([#2184](https://github.com/googleapis/python-bigquery/issues/2184)) ([12490f2](https://github.com/googleapis/python-bigquery/commit/12490f2f03681516465fc34217dcdf57000f6fdd))

##### Documentation

* Update query.py ([#2192](https://github.com/googleapis/python-bigquery/issues/2192)) ([9b5ee78](https://github.com/googleapis/python-bigquery/commit/9b5ee78f046d9ca3f758eeca6244b8485fe35875))
* Use query\_and\_wait in the array parameters sample ([#2202](https://github.com/googleapis/python-bigquery/issues/2202)) ([28a9994](https://github.com/googleapis/python-bigquery/commit/28a9994792ec90a6a4d16835faf2137c09c0fb02))

### Feature

In the navigation menu, you can now go to **Settings** and select **Configuration settings** to [customize the BigQuery Studio experience](https://cloud.google.com/bigquery/docs/bigquery-web-ui#navigation_menu) for users within the selected project or organization. This is achieved by showing or hiding user interface elements. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

### Feature

BigQuery now supports using [Spanner external datasets](https://cloud.google.com/bigquery/docs/spanner-external-datasets) with [authorized views](https://cloud.google.com/bigquery/docs/authorized-views), [authorized routines](https://cloud.google.com/bigquery/docs/authorized-routines), and [Cloud resource connections](https://cloud.google.com/bigquery/docs/create-cloud-resource-connection). This feature is [generally available](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages) (GA).

### Feature

The [`CREATE EXTERNAL TABLE`](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_external_table_statement) and [`LOAD DATA`](https://cloud.google.com/bigquery/docs/reference/standard-sql/load-statements) statements now support the following options in [preview](https://cloud.google.com/products/#product-launch-stages):

* `time_zone`: specify a time zone to use when loading data
* `date_format`, `datetime_format`, `time_format`, and `timestamp_format`: define how date and time values are formatted in your source files

### Feature

In the BigQuery console, in the **Welcome** tab, you can now try the [Apache Spark demo notebook](https://cloud.google.com/bigquery/docs/bigquery-web-ui#run_spark_notebook_demo_guide) that walks you through the basics of Spark notebook and showcases [serverless Spark in BigQuery](https://cloud.google.com/bigquery/docs/use-spark). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

Bigtable
--------

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [6.1.0](https://github.com/googleapis/nodejs-bigtable/compare/v6.0.0...v6.1.0) (2025-05-30)

##### Features

* Add full support for the universe domain ([#1604](https://github.com/googleapis/nodejs-bigtable/issues/1604)) ([4562e23](https://github.com/googleapis/nodejs-bigtable/commit/4562e2329e734c0c9d9f00cfa83aa2be13e9a7fe))

Cloud Composer
--------------

### Feature

Improved the startup times of Airflow workers for environments that have a large number of custom PyPI packages installed.

This change rolls out gradually. In this release, it's available in asia-east1, asia-northeast2, asia-south1, europe-north1, europe-west3, us-east1, us-south1, and us-west2 regions.

### Changed

*(Cloud Composer 3)* If a VPC network is attached to an environment, then all DNS addresses accessed by the Airflow components of the environment are resolved using the Cloud DNS configuration of the VPC network. In particular, Airflow workers that execute DAGs will resolve DNS addresses in this way.

### Changed

*(Cloud Composer 3)* All newly created private DNS zones are immediately visible to a Cloud Composer environment. Previously, re-attaching a VPC network was required.

### Fixed

*(Cloud Composer 3)* It's now possible to use [zones with cross-project binding](http://cloud.google.com/dns/docs/zones/cross-project-binding). Before this change, cross-project bound zones weren't supported in Cloud Composer 3.

### Changed

*(Cloud Composer 2)* In Cloud Composer versions 2.11.5 and later, log processing is switching to using OpenTelemetry instead of Fluentd.

This change was [announced previously](https://cloud.google.com/composer/docs/release-notes#May_14_2025) and is gradually rolling out over several releases. In this release, it's available in the following regions: asia-east1, asia-east2, asia-northeast2, asia-northeast3, asia-south2, asia-southeast2, australia-southeast1, australia-southeast2, europe-central2, europe-north1, europe-north2, europe-southwest1, europe-west, europe-west10, europe-west12, europe-west6, europe-west8, europe-west9, me-central1, me-central2, me-west1, northamerica-northeast2, northamerica-south1, southamerica-east1, southamerica-west1, us-east5, us-south1, us-west, and us-west3.

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.5](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-5) (default)
* [composer-3-airflow-2.9.3-build.25](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-25)

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

* [composer-2.13.3-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-3-airflow-2-10-5) (default)
* [composer-2.13.3-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-3-airflow-2-9-3)

### Deprecated

Cloud Composer version 2.8.1 has reached its [end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support).

Cloud Data Fusion
-----------------

### Changed

The [Salesforce plugin](https://cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source) version 1.6.10 is available in Cloud Data Fusion versions 6.10.1 and 6.11.0. This release includes the following changes:

* Upgraded Salesforce API version from 53.0 to 62.0 ([PLUGIN-1891](https://cdap.atlassian.net/browse/PLUGIN-1891)).
* Added a retry mechanism for all Salesforce API calls from the Salesforce plugin ([PLUGIN-1892](https://cdap.atlassian.net/browse/PLUGIN-1892)).

Cloud Monitoring
----------------

### Feature

You can now add treemap widgets to your custom dashboards. Treemaps display the
most recent value of aggregated data as a series of nested rectangles, the
color saturation of a rectangle is proportional to the represented value.
For more information, see the following:

* [Display the most recent value as a treemap](https://cloud.google.com/monitoring/charts#dashboard_with_a_treemap_widget)
* [API: Dashboard with a Treemap widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_treemap_widget)

Cloud Storage
-------------

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.55.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.54.0...storage/v1.55.0) (2025-05-29)

##### Features

* **storage/control:** Add Client Libraries Storage IntelligenceConfig ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **storage/internal:** Add IpFilter to Bucket ([#12309](https://github.com/googleapis/google-cloud-go/issues/12309)) ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))
* **storage/internal:** Add Object.Retention message ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))

##### Bug Fixes

* **storage:** Add EnableNewAuthLibrary internalOption to HTTP newClient ([#12320](https://github.com/googleapis/google-cloud-go/issues/12320)) ([0036073](https://github.com/googleapis/google-cloud-go/commit/0036073affee5451894654a983fba6b2638433cb))
* **storage:** Migrate oauth2/google usages to cloud.google.com/go/auth ([#11191](https://github.com/googleapis/google-cloud-go/issues/11191)) ([3a22349](https://github.com/googleapis/google-cloud-go/commit/3a22349c1ba6a192d70269f77e5804a9957aa572))
* **storage:** Omit check on MultiRangeDownloader ([#12342](https://github.com/googleapis/google-cloud-go/issues/12342)) ([774621c](https://github.com/googleapis/google-cloud-go/commit/774621c5baa5110f57fe79d817143416bd671d1e))
* **storage:** Retry url.Error and net.OpErrors when they wrap an io.EOF ([#12289](https://github.com/googleapis/google-cloud-go/issues/12289)) ([080f6b0](https://github.com/googleapis/google-cloud-go/commit/080f6b05c5e8bd5baaef71ed47f8d54c695f63d3))

##### Documentation

* **storage/internal:** Add explicit Optional annotations to fields that have always been treated as optional ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))
* **storage/internal:** Add note that Bucket.project output format is always project number format ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))
* **storage/internal:** Add note that managedFolders are supported for GetIamPolicy and SetIamPolicy ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))

Compute Engine
--------------

### Feature

**Preview**: The general-purpose C4D machine series offers bare metal (`-metal`) machine types with 384 vCPUs. Bare metal instances let you create an instance with direct access to the machine's CPU and memory, without a virtualization layer in the middle. To learn more, see [C4D machine series](https://cloud.google.com/compute/docs/general-purpose-machines#c4d_series). For information about bare metal instances, including regional availability, see [Bare metal instances on Compute Engine](https://cloud.google.com/compute/docs/instances/bare-metal-instances).

Container Optimized OS
----------------------

### Changed

### cos-dev-125-19071-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.92](https://cos.googlesource.com/third_party/kernel/+/1c5a7e09f4791a79a02ae7d83967cd3e13b12755 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19071.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Upgraded google-guest-agent to 20250327.00. This included
new services like `google-guest-compat-manager.service` and
`google-guest-agent-manager.service` and new binaries like
`google_guest_compat_manager`, `gce_metadata_script_runner`,
`google_guest_agent_manager`, `ggactl_plugin_cleanup` and
`gce_compat_metadata_script_runner`.

### Changed

Updated the Linux kernel to v6.6.92.

### Feature

Supported NVIDIA MFT Tools.

### Feature

Injected IMEX channel char device for GB200 GPUs.

### Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO\_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA\_GB200 machine.

### Fixed

Upgraded app-admin/google-guest-configs to v20250516.00.

### Fixed

Fixed docker MTU mismatch.

### Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r665.

### Fixed

Upgraded chromeos-base/google-breakpad to v2025.05.22.184901-r240.

### Fixed

Upgraded chromeos-base/session\_manager-client to v0.0.1-r2830.

### Fixed

Upgraded chromeos-base/power\_manager-client to v0.0.1-r2969.

### Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4866.

### Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2734.

### Fixed

Upgraded sys-apps/rootdev to v0.0.1-r51.

### Fixed

Upgraded dev-lang/go to v1.23.9.

### Fixed

Upgraded sys-apps/dbus to v1.16.2-r197.

### Fixed

Upgraded sys-apps/less to v678.

### Fixed

Upgraded dev-db/sqlite to v3.49.2.

### Security

Fixed CVE-2024-23337 in app-misc/jq.

### Security

Upgraded net-misc/curl to version 8.12.1. This fixes CVE-2025-0167.

### Security

Fixed CVE-2025-46836 in sys-apps/net-tools

### Security

Fixed CVE-20250-3198 in sys-libs/bintuils-libs.

### Security

Fixed KCTF-3f98113 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811729 -> 811798
* Changed: net.ipv6.conf.docker0.mtu: 1500 -> 1460

### Changed

### cos-117-18613-263-24

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/d7d9a34e59a967bd31420a1a629853632fc7d3a0 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.263.24/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO\_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA\_GB200 machine.

### Fixed

Upgraded sys-apps/less to v678.

### Security

Fixed CVE-2024-23337 in app-misc/jq.

### Security

Fixed CVE-2024-43840 in the Linux kernel.

### Security

Fixed KCTF-3f98113 in the Linux kernel.

### Security

Fixed KCTF-8478a72 in the Linux kernel.

### Changed

### cos-113-18244-382-29

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.134](https://cos.googlesource.com/third_party/kernel/+/e99d24367a9c6985bc9c997c6f3a053c2a7e2eff ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.382.29/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO\_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA\_GB200 machine.

### Fixed

Upgraded sys-apps/less to v678.

### Security

Fixed CVE-2024-23337 in app-misc/jq.

### Security

Fixed CVE-2024-36927 in the Linux kernel.

### Security

Fixed KCTF-3f98113 in the Linux kernel.

### Security

Fixed KCTF-8478a72 in the Linux kernel.

### Changed

### cos-121-18867-90-38

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/7217e46094ce6bf030248161190afe8b3d8678e8 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.90.38/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO\_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA\_GB200 machine.

### Fixed

Upgraded sys-apps/less to v678.

### Security

Fixed CVE-2024-23337 in app-misc/jq.

### Security

Fixed KCTF-3f98113 in the Linux kernel.

### Security

Fixed KCTF-8478a72 in the Linux kernel.

### Changed

### cos-109-17800-519-18

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.135](https://cos.googlesource.com/third_party/kernel/+/2e89dc9fc1cfcb0184104491d7f412eee640086b ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.18/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO\_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA\_GB200 machine.

### Fixed

Upgraded sys-apps/less to v678.

### Security

Fixed CVE-2024-26783 in the Linux kernel.

### Security

Fixed KCTF-3f98113 in the Linux kernel.

### Security

Fixed KCTF-8478a72 in the Linux kernel.

Google Cloud Architecture Center
--------------------------------

### Feature

(New guide) [Optimize AI and ML workloads with Google Cloud Managed Lustre](https://cloud.google.com/architecture/optimize-ai-ml-workloads-managed-lustre): Shows how to use Managed Lustre to optimize the performance of AI and ML workloads.

Policy Controller
-----------------

### Changed

Policy Controller version 1.20.4 is now available.

Pub/Sub
-------

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.29.1](https://github.com/googleapis/python-pubsub/compare/v2.29.0...v2.29.1) (2025-05-23)

##### Bug Fixes

* Remove setup.cfg configuration for creating universal wheels ([#1376](https://github.com/googleapis/python-pubsub/issues/1376)) ([60639c4](https://github.com/googleapis/python-pubsub/commit/60639c4928105ae8a72c8e37b1f48f75cc2ffcc3))

##### Documentation

* **sample:** Add samples for topic and subscription SMTs ([#1386](https://github.com/googleapis/python-pubsub/issues/1386)) ([4d072e0](https://github.com/googleapis/python-pubsub/commit/4d072e088b59f692dc3d59c3197a2993c125917e))
* Update documentation for JavaScriptUDF to indicate that the `message_id` metadata field is optional instead of required ([#1380](https://github.com/googleapis/python-pubsub/issues/1380)) ([be90054](https://github.com/googleapis/python-pubsub/commit/be9005412fea06bea917c8b6861546b7e6c62a1e))
* Update readme links ([#1409](https://github.com/googleapis/python-pubsub/issues/1409)) ([77ba05d](https://github.com/googleapis/python-pubsub/commit/77ba05d4ba5b84a25c1a07c5397bbc184fa6041d))

### Feature

General availability: Pub/Sub now offers Single Message Transforms (SMTs) that enable lightweight modifications to message data and attributes directly within Pub/Sub. SMTs can be set as properties of topics or subscriptions. The change is being rolled out in a phased manner over the rest of the week. For more information about SMTs, see [Single Message Transforms (SMTs) overview](https://cloud.google.com/pubsub/docs/smts/smts-overview).

Spanner
-------

### Feature

BigQuery now supports using [Spanner external datasets](https://cloud.google.com/bigquery/docs/spanner-external-datasets) with [authorized views](https://cloud.google.com/bigquery/docs/authorized-views), [authorized routines](https://cloud.google.com/bigquery/docs/authorized-routines), and [Cloud resource connections](https://cloud.google.com/bigquery/docs/create-cloud-resource-connection). This feature is [generally available](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages) (GA).

### Libraries

A monthly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [spanner/admin/database/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/spanner/admin/database/apiv1)

#### [1.81.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.80.0...spanner/v1.81.0) (2025-05-09)

##### Features

* **spanner/spansql:** Add support for DROP SEARCH INDEX and ALTER SEARCH INDEX ([#11961](https://github.com/googleapis/google-cloud-go/issues/11961)) ([952cd7f](https://github.com/googleapis/google-cloud-go/commit/952cd7fd419af9eb74f5d30a111ae936094b0645))

##### Bug Fixes

* **spanner:** Row mismatch in SelectAll using custom type ([#12222](https://github.com/googleapis/google-cloud-go/issues/12222)) ([ce6a23a](https://github.com/googleapis/google-cloud-go/commit/ce6a23a45fe66cc12e1b5014d2d45f1968ddc067))

#### [1.81.1](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.81.0...spanner/v1.81.1) (2025-05-15)

##### Features

* **spanner:** Add support of AFE and GRPC metrics in client-side metrics ([#12067](https://github.com/googleapis/google-cloud-go/issues/12067)) ([7b77038](https://github.com/googleapis/google-cloud-go/commit/7b77038eb4afe31b1a0d42f7c35aeabce0f48810))

#### [1.82.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.81.1...spanner/v1.82.0) (2025-05-20)

##### Features

* **spanner/admin/database:** Add throughput\_mode to UpdateDatabaseDdlRequest to be used by Spanner Migration Tool. See https ([#12287](https://github.com/googleapis/google-cloud-go/issues/12287)) ([2a9d8ee](https://github.com/googleapis/google-cloud-go/commit/2a9d8eec71a7e6803eb534287c8d2f64903dcddd))

### Java

### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)

#### [6.92.0](https://github.com/googleapis/java-spanner/compare/v6.91.1...v6.92.0) (2025-04-29)

* **spanner:** Do not export metrics during shutdown if prev export was less than 30 seconds ago ([#12266](https://github.com/googleapis/google-cloud-go/issues/12266)) ([8ad7511](https://github.com/googleapis/google-cloud-go/commit/8ad75111433be5424f9fff8aafd73463cb467734))
* **spanner:** Fix invalid trace in case of skipping trailers ([#12235](https://github.com/googleapis/google-cloud-go/issues/12235)) ([e54c439](https://github.com/googleapis/google-cloud-go/commit/e54c4398831b5a1c2998f9e8d159f0118aee1d0b))
  ### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)
  #### [6.94.0](https://github.com/googleapis/java-spanner/compare/v6.93.0...v6.94.0) (2025-05-21)

##### Features

* [Internal] client-side metrics for afe latency and connectivity error ([#3819](https://github.com/googleapis/java-spanner/issues/3819)) ([a8dba0a](https://github.com/googleapis/java-spanner/commit/a8dba0a83939fdbbc324f0a7aa6c44180462fa3a))
* Support begin with AbortedException for manager interface ([#3835](https://github.com/googleapis/java-spanner/issues/3835)) ([5783116](https://github.com/googleapis/java-spanner/commit/578311693bed836c8916f4b4ffa0782a468c1af3))
* Add throughput\_mode to UpdateDatabaseDdlRequest to be used by Spanner Migration Tool. See https://github.com/GoogleCloudPlatform/spanner-migration-tool ([3070f1d](https://github.com/googleapis/java-spanner/commit/3070f1db97788c2a55c553ab8a4de3419d1ccf5c))
* Enable AFE and gRPC metrics for DP ([#3852](https://github.com/googleapis/java-spanner/issues/3852)) ([203baae](https://github.com/googleapis/java-spanner/commit/203baae3996378435095cb90e3b2c7ee71a643cd))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.56.2 ([11bfd90](https://github.com/googleapis/java-spanner/commit/11bfd90daa244dbd31a76bc5a1d2e694e43fa292))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.58.0 ([3070f1d](https://github.com/googleapis/java-spanner/commit/3070f1db97788c2a55c553ab8a4de3419d1ccf5c))
* Remove trailing semicolons in DDL ([#3879](https://github.com/googleapis/java-spanner/issues/3879)) ([ca3a67d](https://github.com/googleapis/java-spanner/commit/ca3a67db715f398943382df1f8a9979905811ff8))
* Change server timing duration attribute to float as per w3c ([#3851](https://github.com/googleapis/java-spanner/issues/3851)) ([da8dd8d](https://github.com/googleapis/java-spanner/commit/da8dd8da3171a073d7b450d4413936351a4c1060))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.57.0 ([23b985c](https://github.com/googleapis/java-spanner/commit/23b985c9a04837b0b38f2cfc5d96469e1d664d67))
* Non-ASCII Unicode characters in code ([#3844](https://github.com/googleapis/java-spanner/issues/3844)) ([85a0820](https://github.com/googleapis/java-spanner/commit/85a0820505889ae6482a9e4f845cd53430dd6b44))
* Only close and return sessions once ([#3846](https://github.com/googleapis/java-spanner/issues/3846)) ([32b2373](https://github.com/googleapis/java-spanner/commit/32b2373d62cac3047d9686c56af278c706d7c488))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#3836](https://github.com/googleapis/java-spanner/issues/3836)) ([2ee7f97](https://github.com/googleapis/java-spanner/commit/2ee7f971f3374b01d22e5a7f8f2483cf60c3363d))

#### [6.93.0](https://github.com/googleapis/java-spanner/compare/v6.92.0...v6.93.0) (2025-05-09)

* Update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#3869](https://github.com/googleapis/java-spanner/issues/3869)) ([afa17f7](https://github.com/googleapis/java-spanner/commit/afa17f73beab80639467916bc73b5c96305093aa))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#3880](https://github.com/googleapis/java-spanner/issues/3880)) ([f3b00b6](https://github.com/googleapis/java-spanner/commit/f3b00b663aa897fda1bc21222d29726e6be630cb))
* Update dependency com.google.cloud.opentelemetry:exporter-metrics to v0.34.0 ([#3861](https://github.com/googleapis/java-spanner/issues/3861)) ([676b14f](https://github.com/googleapis/java-spanner/commit/676b14f916dea783b40ddec4061bd7af157b5d98))
* Update dependency commons-io:commons-io to v2.19.0 ([#3863](https://github.com/googleapis/java-spanner/issues/3863)) ([80a6af8](https://github.com/googleapis/java-spanner/commit/80a6af836ca29ec196a2f509831e1d36c557168f))
* Update dependency io.opentelemetry:opentelemetry-bom to v1.50.0 ([#3865](https://github.com/googleapis/java-spanner/issues/3865)) ([ae63050](https://github.com/googleapis/java-spanner/commit/ae6305089b394be0c1eaf8ff7e188711288d87ad))
* Update googleapis/sdk-platform-java action to v2.58.0 ([#3870](https://github.com/googleapis/java-spanner/issues/3870)) ([d1e45fa](https://github.com/googleapis/java-spanner/commit/d1e45fa88bb005529bcfb2a6ff2df44065be0fd2))
* Update opentelemetry.version to v1.50.0 ([#3866](https://github.com/googleapis/java-spanner/issues/3866)) ([f7e09b8](https://github.com/googleapis/java-spanner/commit/f7e09b8148c0e51503255694bd3347c637724b34))

##### Documentation

* Add samples for unnamed (positional) parameters ([#3849](https://github.com/googleapis/java-spanner/issues/3849)) ([035cadd](https://github.com/googleapis/java-spanner/commit/035cadd5bb77a8f9f6fb25ac8c8e5a3e186d9a22))

### Node.js

### Changes for [@google-cloud/spanner](https://github.com/googleapis/nodejs-spanner)

#### [8.0.0](https://github.com/googleapis/nodejs-spanner/compare/v7.21.0...v8.0.0) (2025-05-12)

##### ⚠ BREAKING CHANGES

* remove the arrify package ([#2292](https://github.com/googleapis/nodejs-spanner/issues/2292))
* migrate to Node 18 ([#2271](https://github.com/googleapis/nodejs-spanner/issues/2271))

##### Features

* Add promise based signatures for createQueryPartitions ([#2284](https://github.com/googleapis/nodejs-spanner/issues/2284)) ([255d8a6](https://github.com/googleapis/nodejs-spanner/commit/255d8a6a5749b6a05cd87dd7444cab7dd75d3e42))
* Add promise based signatures on createReadPartitions ([#2300](https://github.com/googleapis/nodejs-spanner/issues/2300)) ([7b8a1f7](https://github.com/googleapis/nodejs-spanner/commit/7b8a1f70f0de3aa5886a2cde9325c9a36222a311))
* Support promise based signatures for execute method ([#2301](https://github.com/googleapis/nodejs-spanner/issues/2301)) ([bb857e1](https://github.com/googleapis/nodejs-spanner/commit/bb857e18459f717d67b9b3d144c2b022178363cb))

##### Bug Fixes

* **deps:** Update dependency @google-cloud/kms to v5 ([#2289](https://github.com/googleapis/nodejs-spanner/issues/2289)) ([1ccb505](https://github.com/googleapis/nodejs-spanner/commit/1ccb505935e70b6f576f06e566325146ee68f3ff))
* **deps:** Update dependency @google-cloud/precise-date to v5 ([#2290](https://github.com/googleapis/nodejs-spanner/issues/2290)) ([44f7575](https://github.com/googleapis/nodejs-spanner/commit/44f7575efd3751d0595beef2ec4eb9f39bc426d7))
* **deps:** Update dependency big.js to v7 ([#2286](https://github.com/googleapis/nodejs-spanner/issues/2286)) ([0911297](https://github.com/googleapis/nodejs-spanner/commit/0911297cc33aec93c09ef2be42413f20c75fc2bf))

##### Miscellaneous Chores

* Migrate to Node 18 ([#2271](https://github.com/googleapis/nodejs-spanner/issues/2271)) ([cab3f22](https://github.com/googleapis/nodejs-spanner/commit/cab3f229ccb2189bd5af0c25a3006b553f8a5453))
* Remove the arrify package ([#2292](https://github.com/googleapis/nodejs-spanner/issues/2292)) ([e8f5ca1](https://github.com/googleapis/nodejs-spanner/commit/e8f5ca15125d570949769e6e66f0d911cb21f58d))

### Python

### Changes for [google-cloud-spanner](https://github.com/googleapis/python-spanner)

#### [3.54.0](https://github.com/googleapis/python-spanner/compare/v3.53.0...v3.54.0) (2025-04-28)

##### Features

* Add interval type support ([#1340](https://github.com/googleapis/python-spanner/issues/1340)) ([6ca9b43](https://github.com/googleapis/python-spanner/commit/6ca9b43c3038eca1317c7c9b7e3543b5f1bc68ad))
* Add sample for pre-split feature ([#1333](https://github.com/googleapis/python-spanner/issues/1333)) ([ca76108](https://github.com/googleapis/python-spanner/commit/ca76108809174e4f3eea38d7ac2463d9b4c73304))
* Add SQL statement for begin transaction isolation level ([#1331](https://github.com/googleapis/python-spanner/issues/1331)) ([3ac0f91](https://github.com/googleapis/python-spanner/commit/3ac0f9131b38e5cfb2b574d3d73b03736b871712))
* Support transaction isolation level in dbapi ([#1327](https://github.com/googleapis/python-spanner/issues/1327)) ([03400c4](https://github.com/googleapis/python-spanner/commit/03400c40f1c1cc73e51733f2a28910a8dd78e7d9))

##### Bug Fixes

* Improve client-side regex statement parser ([#1328](https://github.com/googleapis/python-spanner/issues/1328)) ([b3c259d](https://github.com/googleapis/python-spanner/commit/b3c259deec817812fd8e4940faacf4a927d0d69c))

#### [3.55.0](https://github.com/googleapis/python-spanner/compare/v3.54.0...v3.55.0) (2025-05-28)

##### Features

* Add a `last` field in the `PartialResultSet` ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* Add support for multiplexed sessions ([#1381](https://github.com/googleapis/python-spanner/issues/1381)) ([97d7268](https://github.com/googleapis/python-spanner/commit/97d7268ac12a57d9d116ee3d9475580e1e7e07ae))
* Add throughput\_mode to UpdateDatabaseDdlRequest to be used by Spanner Migration Tool. See https://github.com/GoogleCloudPlatform/spanner-migration-tool ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* Support fine-grained permissions database roles in connect ([#1338](https://github.com/googleapis/python-spanner/issues/1338)) ([064d9dc](https://github.com/googleapis/python-spanner/commit/064d9dc3441a617cbc80af6e16493bc42c89b3c9))

##### Bug Fixes

* E2E tracing metadata append issue ([#1357](https://github.com/googleapis/python-spanner/issues/1357)) ([3943885](https://github.com/googleapis/python-spanner/commit/394388595a312f60b423dfbfd7aaf2724cc4454f))
* Pass through kwargs in dbapi connect ([#1368](https://github.com/googleapis/python-spanner/issues/1368)) ([aae8d61](https://github.com/googleapis/python-spanner/commit/aae8d6161580c88354d813fe75a297c318f1c2c7))
* Remove setup.cfg configuration for creating universal wheels ([#1324](https://github.com/googleapis/python-spanner/issues/1324)) ([e064474](https://github.com/googleapis/python-spanner/commit/e0644744d7f3fcea42b461996fc0ee22d4218599))

##### Documentation

* A comment for field `chunked_value` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `precommit_token` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `precommit_token` in message `.google.spanner.v1.ResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `query_plan` in message `.google.spanner.v1.ResultSetStats` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `row_count_lower_bound` in message `.google.spanner.v1.ResultSetStats` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `row_type` in message `.google.spanner.v1.ResultSetMetadata` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `rows` in message `.google.spanner.v1.ResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `stats` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `stats` in message `.google.spanner.v1.ResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `values` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for message `ResultSetMetadata` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for message `ResultSetStats` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* Fix markdown formatting in transactions page ([#1377](https://github.com/googleapis/python-spanner/issues/1377)) ([de322f8](https://github.com/googleapis/python-spanner/commit/de322f89642a3c13b6b1d4b9b1a2cdf4c8f550fb))

---
## 2025-05-30

### Announcement

On May 30, 2025 we released an updated version of Apigee.

### Feature

**Announcing the general availability of Gemini Code Assist API development features in Apigee**

With this functionality, you can accelerate your API development lifecycle within VS Code using Gemini Code Assist in Apigee. This feature allows you to use natural language prompts to design, create, iterate, and manage OpenAPI specifications with the following capabilities:

* **AI-Powered API Design**: Generate high-quality OpenAPI specifications from natural language prompts to the Apigee tool in Gemini Code Assist Chat, leveraging the Gemini model and the enterprise context of your API hub.
* **Effortless Iteration**: Refine existing or newly generated specifications using the intuitive Gemini chat interface.
* **Integrated Testing**: Quickly validate your APIs by deploying them to a local or Google Cloud-hosted mock server.
* **Streamlined Workflow**: Publish your completed API specifications directly to Apigee API hub and kick-start proxy development by creating Apigee proxy bundles from your API specifications.
* **Duplicate Endpoint Detection**: Proactively identify and prevent the creation of duplicate API endpoints already registered in your API hub.

For more information and usage instructions, see [Designing and editing APIs](https://cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-design-edit-apis), [Tutorial: Use Gemini Code Assist to design, develop, and test APIs in Apigee](https://cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-gemini), and [Setting up Apigee API Management in Cloud Code for VS Code](https://cloud.google.com/apigee/docs/api-platform/local-development/setup).

---
## 2025-05-29

### Announcement

On May 29, 2025 we announced the shutdown schedule for the Apigee Classic UI.

### Announcement

On May 29, 2025, we released an updated version of Apigee.

### Feature

**Public Preview: Apigee Extension Processor support for request and response body processing**

When creating a load balancer service extension, you can customize the behavior of the extension processor proxy to support request body processing, response body processing, or a combination of the two.

For more information, see [Get started with the Apigee Extension Processor](https://cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart#create-lb-ext).

### Deprecated

The Apigee Classic UI will be shutdown as of August 29, 2025.

This is the final phase of moving Apigee to the Google Cloud console. Apigee in the Google Cloud console gives you the ability to manage all of your Apigee functionality in one place.

To prepare for the shutdown of the Apigee Classic UI, familiarize yourself with the new Apigee UI in Google Cloud console by reviewing [UI overview](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview).

See [Apigee Classic UI shutdown](https://cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates and exception request.

---
