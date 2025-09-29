# Cloud Data Fusion

## 2025-09-09

### Changed

The Salesforce plugin version 1.7.0 is available in Cloud Data Fusion version 6.8.0 and later. This release includes the following change:

* Upgrade of Salesforce Bulk API V1 version from 62.0 to 64.0 ([PLUGIN-1926](https://cdap.atlassian.net/browse/PLUGIN-1926)).

Salesforce has deprecated certain fields in the API version 64.0. Upgrading to Salesforce plugin version 1.7.0 might cause pipelines that use these fields, to fail. To ensure your pipelines continue to work, you must manually update your pipeline schema to either load a new schema or remove the deprecated fields. For more information, see [Prerequisites for upgrading to Salesforce plugin version 1.7.0](https://cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source#upgrade-prereq).

---
## 2025-08-28

### Changed

The ServiceNow plugin version 1.2.7 is available in Cloud Data Fusion version 6.10.1. This release includes the following change:

* Fixed an issue related to schema backward compatibility while upgrading from plugin version 1.1.0 ([PLUGIN-1902](https://cdap.atlassian.net/browse/PLUGIN-1902)).

---
## 2025-08-27

### Feature

Cloud Data Fusion version 6.11.1 is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). This release includes the following features:

* Added support for HTTP access tokens (Bearer authentication) in Bitbucket Server for [source control management](https://cloud.google.com/data-fusion/docs/how-to/source-control-management) ([CDAP-21049](https://cdap.atlassian.net/browse/CDAP-21049)).
* A new API is available to retrieve the application count for each namespace ([CDAP-21161](https://cdap.atlassian.net/browse/CDAP-21161)).

### Changed

Changes in Cloud Data Fusion 6.11.1:

* The Java runtime environment is upgraded from Java 8 to Java 11 ([CDAP-21184](https://cdap.atlassian.net/browse/CDAP-21184)).
* To create ephemeral Dataproc clusters, Cloud Data Fusion uses the Dataproc 2.3 image by default ([CDAP-21187](https://cdap.atlassian.net/browse/CDAP-21187)).
* The pipeline JSON size limit for creating new pipelines and importing pipelines as JSON is increased to 5MB (previously 2MB) (<CDAP-21194>).
* On the Pipeline details page, the inbound triggers sidebar features a paginated list of pipelines where you can select the pipelines you want to add to the trigger. Additionally, a refresh button is added to update the existing list of triggers and pipelines ([CDAP-21195](https://cdap.atlassian.net/browse/CDAP-21195)).

### Fixed

Fixed in Cloud Data Fusion 6.11.1:

* To prevent storage issues on static Dataproc clusters, temporary pipeline data is automatically deleted after a successful run ([CDAP-21076](https://cdap.atlassian.net/browse/CDAP-21076)).
* Fixed an issue that prevented [Expression Language (EL)](https://github.com/data-integrations/wrangler/blob/develop/wrangler-core/src/main/java/io/cdap/wrangler/expression/EL.java) from being used within user-defined directives ([CDAP-21204](https://cdap.atlassian.net/browse/CDAP-21204)).
* Fixed an issue where a pipeline would fail when reading an encrypted file from Cloud Storage using Tink ([PLUGIN-1717](https://cdap.atlassian.net/browse/PLUGIN-1717)).

### Deprecated

Dataproc 2.0 is no longer supported in Cloud Data Fusion version 6.11.1 and later.

---
## 2025-07-25

### Feature

You can now attach tags to Cloud Data Fusion instances during instance creation. This ensures immediate metadata for better organization, cost tracking, and policy automation. For more information, see [Attach tags during instance creation](https://cloud.google.com/data-fusion/docs/how-to/control-access-with-tags#add-tags).

---
## 2025-07-23

### Fixed

The Cloud Data Fusion version 6.10.1.5 patch revision is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). 6.10.1.5 includes reliability fixes.

---
## 2025-07-20

### Changed

The SAP ODP plugin version 0.12 is available in Cloud Data Fusion version 6.10 and later. This release includes the following changes:

* Support for old SAP ODP RFCs is removed to align with SAP Note 3255746.
* Messages have been updated when attempting to extract data from unsupported hierarchy data sources.

We recommend upgrading all your pipelines to the latest SAP ODP plugin version, as earlier versions are no longer compliant with SAP Guidelines.

**Note:** This release is backward compatible.

---
## 2025-07-16

### Changed

The Oracle plugin version 1.12.3 is available in Cloud Data Fusion (via Hub) versions 6.11.0 and later, and 1.11.8 is available in Cloud Data Fusion (via Hub) version 6.10.

This release provides backward compatibility for recent schema changes, including the following:

* [Precisionless numbers](https://cloud.google.com/data-fusion/docs/release-notes#March_14_2023): In version 1.10.0, precisionless numbers were handled as strings.
* [Improved timestamp handling](https://cloud.google.com/data-fusion/docs/release-notes#June_14_2023): Version 1.11.0 introduced improvements to timestamp handling.

To address backward compatibility for these changes, two new hidden fields are introduced in Oracle batch source configurations: `treatPrecisionlessNumAsDeci` and `treatAsOldTimestamp`. Both flags default to `false`. To enable these flags, edit the respective values in your exported connection JSON (if using connections) or pipeline JSON (if not using connections) before re-importing or re-deploying ([PLUGIN-1893](https://cdap.atlassian.net/browse/PLUGIN-1893)).

---
## 2025-06-12

### Changed

The Elasticsearch plugin version 1.11.0 is available in Cloud Data Fusion version 6.11.0. This release includes the following change:

* Upgraded Hadoop version for Elasticsearch plugin compatibility ([PLUGIN-1881](https://cdap.atlassian.net/browse/PLUGIN-1881)).

---
## 2025-06-11

### Changed

The HTTP plugin version 1.4.4 is available in Cloud Data Fusion version 6.10.1. This release includes the following changes:

* Implemented the Client Credentials Grant flow for HTTP OAuth2, enabling authorized clients to securely access data using the `client_credentials` grant type. Client credentials can be passed through Basic Authentication header, in the request body, or as query parameters ([PLUGIN-1872](https://cdap.atlassian.net/browse/PLUGIN-1872)).
* Fixed an issue causing the HTTP Source plugin to throw a `NullPointerException` when the `BasePageIterator` received a null response ([PLUGIN-1894](https://cdap.atlassian.net/browse/PLUGIN-1894)).

---
## 2025-06-09

### Changed

Cloud Data Fusion is available in the `northamerica-south1` (Mexico) region. For more information, see [Pricing](https://cloud.google.com/data-fusion/pricing).

---
## 2025-06-02

### Changed

The [Salesforce plugin](https://cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source) version 1.6.10 is available in Cloud Data Fusion versions 6.10.1 and 6.11.0. This release includes the following changes:

* Upgraded Salesforce API version from 53.0 to 62.0 ([PLUGIN-1891](https://cdap.atlassian.net/browse/PLUGIN-1891)).
* Added a retry mechanism for all Salesforce API calls from the Salesforce plugin ([PLUGIN-1892](https://cdap.atlassian.net/browse/PLUGIN-1892)).

---
