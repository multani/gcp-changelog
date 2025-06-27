# Cloud Data Fusion

## 2025-06-12 00:00:00-07:00

### Changed

The Elasticsearch plugin version 1.11.0 is available in Cloud Data Fusion version 6.11.0. This release includes the following change:

* Upgraded Hadoop version for Elasticsearch plugin compatibility ([PLUGIN-1881](https://cdap.atlassian.net/browse/PLUGIN-1881)).## 2025-06-11 00:00:00-07:00

### Changed

The HTTP plugin version 1.4.4 is available in Cloud Data Fusion version 6.10.1. This release includes the following changes:

* Implemented the Client Credentials Grant flow for HTTP OAuth2, enabling authorized clients to securely access data using the `client_credentials` grant type. Client credentials can be passed through Basic Authentication header, in the request body, or as query parameters ([PLUGIN-1872](https://cdap.atlassian.net/browse/PLUGIN-1872)).
* Fixed an issue causing the HTTP Source plugin to throw a `NullPointerException` when the `BasePageIterator` received a null response ([PLUGIN-1894](https://cdap.atlassian.net/browse/PLUGIN-1894)).## 2025-06-09 00:00:00-07:00

### Changed

Cloud Data Fusion is available in the `northamerica-south1` (Mexico) region. For more information, see [Pricing](https://cloud.google.com/data-fusion/pricing).## 2025-06-02 00:00:00-07:00

### Changed

The [Salesforce plugin](https://cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source) version 1.6.10 is available in Cloud Data Fusion versions 6.10.1 and 6.11.0. This release includes the following changes:

* Upgraded Salesforce API version from 53.0 to 62.0 ([PLUGIN-1891](https://cdap.atlassian.net/browse/PLUGIN-1891)).
* Added a retry mechanism for all Salesforce API calls from the Salesforce plugin ([PLUGIN-1892](https://cdap.atlassian.net/browse/PLUGIN-1892)).