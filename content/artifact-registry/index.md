# Artifact Registry

## 2025-09-23

### Feature

Layer-based scanning for Artifact Analysis is in [Preview](https://cloud.google.com/products#product-launch-stages). You can view vulnerability metadata for a specific layer of your image digest in the Google Cloud Console and in the GCloud CLI. For more information, see the following topics:

**Google Cloud Console**:

* [View layer metadata for Go images](https://cloud.google.com/artifact-analysis/docs/scan-go-automatically#layer)
* [View layer metadata for Java images](https://cloud.google.com/artifact-analysis/docs/scan-java-automatically#layer)
* [View layer metadata for Node.js images](https://cloud.google.com/artifact-analysis/docs/scan-nodejs-automatically#layer)
* [View layer metadata for Python images](https://cloud.google.com/artifact-analysis/docs/scan-python-automatically#layer)

**GCloud CLI**

* [View layer metadata for Go images](https://cloud.google.com/artifact-analysis/docs/scan-go-automatically#layer-gcloud)
* [View layer metadata for Java images](https://cloud.google.com/artifact-analysis/docs/scan-java-automatically#layer-gcloud)
* [View layer metadata for Node.js images](https://cloud.google.com/artifact-analysis/docs/scan-nodejs-automatically#layer-gcloud)
* [View layer metadata for Python images](https://cloud.google.com/artifact-analysis/docs/scan-python-automatically#layer-gcloud)

---
## 2025-08-29

### Changed

The Container Analysis API now supports the option of returning partial results during region-down failure conditions when listing notes, listing occurrences, or generating vulnerability summaries. For more information, view the `returnPartialSuccess` parameter for the following requests:

* [v1.projects.locations.notes.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.locations.notes/list)
* [v1.projects.locations.occurrences.getVulnerabilitySummary](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.locations.occurrences/getVulnerabilitySummary)
* [v1.projects.locations.occurrences.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.locations.occurrences/list)
* [v1.projects.notes.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.notes/list)
* [v1.projects.occurrences.getVulnerabilitySummary](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences/getVulnerabilitySummary)
* [v1.projects.occurrences.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.occurrences/list)
* [v1beta1.projects.locations.notes.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.notes/list)
* [v1beta1.projects.locations.occurrences.getVulnerabilitySummary](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/getVulnerabilitySummary)
* [v1beta1.projects.locations.occurrences.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences/list)
* [v1beta1.projects.notes.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.notes/list)
* [v1beta1.projects.occurrences.getVulnerabilitySummary](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.occurrences/getVulnerabilitySummary)
* [v1beta1.projects.occurrences.list](https://cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.occurrences/list)

---
## 2025-06-25

### Announcement

Artifact Registry generic repositories are now [generally available](https://cloud.google.com/products?#product-launch-stages).

Generic repositories store versioned, immutable artifacts that don't have to adhere to any specific package format in Artifact Registry. You can store and manage arbitrary files such as archives, binaries, and media files with no package specifications or management clients.

To get started with generic repositories, see the [quickstart](https://cloud.google.com/artifact-registry/docs/generic/store-generic).

---
