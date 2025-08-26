# Sensitive Data Protection

## 2025-08-25

### Feature

The `DOCUMENT_TYPE/FINANCE/INVOICE` and `DOCUMENT_TYPE/MEDICAL/RECORD` infoType detectors are available in `global` and the `asia`, `europe`, and `us` multi-regions. For more information about all infoTypes, see [InfoType detector reference](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

---
## 2025-08-15

### Feature

The `AUSTRIA_SOCIAL_SECURITY_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see the [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

### Feature

During discovery operations, Sensitive Data Protection scans the contents of various archive files. For a list of supported file types, see [Supported file clusters in discovery operations](https://cloud.google.com/sensitive-data-protection/docs/supported-file-types#file_clusters).

---
## 2025-08-13

### Feature

You can configure Sensitive Data Protection to save the findings from an inspection job to a Cloud Storage bucket or folder. For more information, see [Save findings to Cloud Storage](https://cloud.google.com/sensitive-data-protection/docs/concepts-actions#save-findings-cloud-storage).

---
## 2025-08-04

### Feature

Sensitive Data Protection provides recommendations to optimize your infoType selections. In the Google Cloud console, if you select a specific infoType that is covered by a general infoType, Sensitive Data Protection recommends general infoTypes that you can use instead.

For information about the benefits of using general infoTypes, see [General and specific infoType detectors](https://cloud.google.com/sensitive-data-protection/docs/concepts-infotypes#general-specific-infotypes).

---
## 2025-08-01

### Feature

The following infoType detectors are available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

* `DOCUMENT_TYPE/R&D/SOURCE_CODE/C`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/CPP`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/CS`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/GO`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/HTML`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/JAVA`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/JAVASCRIPT`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/JSON`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/PHP`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/POWERSHELL`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/PYTHON`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/RUST`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/SHELL`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/SQL`
* `DOCUMENT_TYPE/R&D/SOURCE_CODE/TYPESCRIPT`

---
## 2025-07-04

### Feature

Sensitive Data Protection can detect and redact the following object infoTypes in images:

* `OBJECT_TYPE/BARCODE`
* `OBJECT_TYPE/LICENSE_PLATE`
* `OBJECT_TYPE/PERSON`
* `OBJECT_TYPE/WHITEBOARD`

For more information, see the following:

* [Inspect an image for sensitive objects](https://cloud.google.com/sensitive-data-protection/docs/inspecting-images#inspect_an_image_for_sensitive_objects)
* [Object redaction](https://cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images#object-redaction)

---
## 2025-06-25

### Feature

The `CZECHIA_PERSONAL_ID_NUMBER` infoType detector is available in all regions. For more information about all built-in infoTypes, see [InfoType detector reference](https://cloud.google.com/dlp/docs/infotypes-reference).

---
