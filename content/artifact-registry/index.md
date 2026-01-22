# Artifact Registry

## 2026-01-21

### Feature

Artifact Registry is available in the `asia-southeast3` region (Bangkok).
For more information, see [Global locations](https://cloud.google.com/about/locations).

---
## 2026-01-20

### Feature

Artifact Registry now calculates fingerprints for each version of a package
pushed to the Artifact Registry repository. You can use the fingerprint to
validate that the package wasn't modified when moving between Google Cloud
systems, such as Compute Engine and Cloud Build.
This feature is in
[public preview](https://cloud.google.com/products/#product-launch-stages).
For more information,
see [Use fingerprints to verify package version identities](https://docs.cloud.google.com/artifact-registry/docs/fingerprint).

---
## 2025-11-24

### Feature

You can now use
[`ExportArtifact()`](https://cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/exportArtifact)
to export an artifact to a Cloud Storage bucket.

---
## 2025-11-04

### Feature

Artifact Registry support for managing Ruby gems with Artifact Registry
repositories is in
[Preview](https://cloud.google.com/products#product-launch-stages). For
more information, see the following topics:

* [Get started with Ruby gems](https://cloud.google.com/artifact-registry/docs/ruby)
* [Store Ruby gems in Artifact Registry (Quickstart)](https://cloud.google.com/artifact-registry/docs/ruby/store-ruby)

---
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
