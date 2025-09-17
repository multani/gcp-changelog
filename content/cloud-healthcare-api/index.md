# Cloud Healthcare API

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
