# Cloud Healthcare API

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
