# Cloud Healthcare API

## 2025-12-22

### Feature

* The Cloud Healthcare API now supports transcoding DICOM data with the
  following transfer syntaxes:
* `1.2.840.10008.1.2.1.99` (Deflated Explicit VR Little Endian)
* `1.2.840.10008.1.2.4.51` (JPEG Extended)
* `1.2.840.10008.1.2.4.80` (JPEG-LS Lossless)
* `1.2.840.10008.1.2.4.81` (JPEG-LS Near-Lossless)
* `1.2.840.10008.1.2.4.110` (JPEG XL Lossless)
* `1.2.840.10008.1.2.4.111` (JPEG XL JPEG Recompression)
* `1.2.840.10008.1.2.4.112` (JPEG XL)
* `1.2.840.10008.1.2.4.201` (HTJ2K Lossless Only)
* `1.2.840.10008.1.2.4.202` (HTJ2K Lossless Only with RPCL Options)
* `1.2.840.10008.1.2.4.203` (HTJ2K)
* `1.2.840.10008.1.2.8.1` (Deflated Image Frame Compression)

---
## 2025-12-02

### Feature

* DICOM exports to BigQuery now support a new JSON schema option
* DICOM streaming to BigQuery now supports a new JSON schema option
* The new JSON schema option contains fewer columns and works more gracefully with the
  33,000 public tags defined in the DICOM standard. For more information on the new schema,
  see the [`BigQueryDestination`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores#BigQueryDestination)
  field.

### Feature

* DICOM streaming to BigQuery using the new JSON schema now supports [Change Data Capture](https://docs.cloud.google.com/bigquery/docs/change-data-capture)
* For more information on enabling change data capture, see the
  [`BigQueryDestination`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores#BigQueryDestination)
  field.

---
## 2025-11-03

### Feature

`VersionedStorageSizeBytes` was added to the output of
[`GetFhirStoreMetrics`](https://cloud.google.com/healthcare-api/docs/fhir-store-metrics).

---
## 2025-10-25

### Feature

* The Cloud Healthcare API is now available in the `me-central1` (Qatar) and `me-central2` (KSA) regions.

---
## 2025-10-23

### Feature

* A new application has been added to the Cloud Console under "Healthcare",
  called "DICOM Studio"
* This new application provides a web interface for exploring DICOM Stores
  in the Cloud Healthcare API similar to "FHIR Viewer".
  + Search and find studies, series, and instances in any DICOM Store using our DICOM Web API
  + View studies, series and instance metadata
  + Edit studies, series and instance metadata
  + Perform CRUD operations (Delete) on studies, series and instances
  + View studies, series and instance images via a transcoded image preview

---
## 2025-10-09

### Feature

* A new application has been added to the Cloud Console under "Healthcare",
  called "DICOM Studio"
* This new application provides a web interface for exploring DICOM Stores
  in the Cloud Healthcare API similar to "FHIR Viewer".
  + Search and find studies, series, and instances in any DICOM Store using our DICOM Web API
  + View studies, series and instance metadata
  + Edit studies, series and instance metadata
  + Perform CRUD operations (Delete) on studies, series and instances
  + View studies, series and instance images via a transcoded image preview

---
## 2025-09-12

### Feature

* `Accept-Encoding` compression headers on DICOM frame requests that contain
  uncompressed pixel data (as defined by the DICOM transfer syntax) are now
  supported and can return compressed results

**Note**: For very large downlinks and very large files where downlink vastly
outpaces compression speed, latency may slightly increase. Compression can be
disabled by not including the header in these cases.

---
## 2025-08-26

### Feature

**Preview:** Cloud Healthcare API has launched DICOM Updates and Patches. This
allows customers to update their DICOM data in-place. For more information, see
[Update and patch DICOM studies, series, and instances](https://cloud.google.com/healthcare-api/docs/how-tos/dicom-update-patch).

---
## 2025-05-27

### Deprecated

The Healthcare Natural Language API is deprecated and will be shut down
on May 27, 2026. For more information, see
[Deprecations](https://cloud.google.com/healthcare-api/docs/deprecations/).

---
