# Infrastructure Manager

## 2026-09-15

### Feature

Infrastructure Manager now supports the `us` multi-regional location in
General Availability (GA).

You can now create and manage deployments, revisions, and previews in the
`us` multi-region (`projects/PROJECT_ID/locations/us`). Deployments in the
`us` multi-region benefit from metadata and state file redundancy across data
centers in the United States.

For more information, see
[Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations).

---
## 2026-01-12

### Change

Infrastructure Manager is available in the following regions:

* `me-central2`

For more information about regions, see [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations).

---
## 2026-01-05

### Announcement

Infrastructure Manager will deprecate support for Terraform version `1.2.3` on
**January 8, 2026**.

If you have [enabled auto-migration](https://docs.cloud.google.com/infrastructure-manager/docs/terraform-version-deprecation#auto-migration),
your deployments using Terraform version `1.2.3` will be migrated automatically to
Terraform version `1.5.7`.

We recommend that you upgrade your deployment Terraform version from `1.2.3`
to version `1.5.7` before the version `1.2.3.` end of support date on
**February 8, 2026**.

For more information, see [Terraform version management policy](https://docs.cloud.google.com/infrastructure-manager/docs/terraform-version-deprecation)
documentation.

---
