# Cloud Deploy

## 2026-01-23

### Change

The limit on deployment minutes per delivery pipeline has been removed. The only
quota now enforced in Cloud Deploy is the system limit of 18,000 API
requests per minute per region. [Learn more](https://docs.cloud.google.com/deploy/quotas).

---
## 2025-12-12

### Change

We now [upgrade the tools used for deployments more frequently](https://docs.cloud.google.com/deploy/docs/select-tool-version).
This includes tools like Skaffold, Kubectl, and Helm. You can also
[select specific versions](https://docs.cloud.google.com/deploy/docs/select-tool-version#how_select) of these
tools when you create a release.

---
## 2025-09-02

### Feature

You can now use custom constraints with Organization Policy to provide more granular control over specific fields for some Cloud Deploy resources. For more information, see [Use custom organization policies](https://cloud.google.com/deploy/docs/custom-org-policy).

---
