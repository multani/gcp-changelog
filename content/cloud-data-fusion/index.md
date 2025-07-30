# Cloud Data Fusion

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
