# Cloud Build

## 2026-02-12

### Change

Cloud Build is now available in the `asia-southeast3` region.

For more information, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

---
## 2026-01-20

### Change

Cloud Build is now available in the `asia-southeast3` region.

For more information, see [Cloud Build locations](https://docs.cloud.google.com/build/docs/locations).

---
## 2026-01-12

### Change

Cloud Build now supports OCI artifacts. OCI artifacts for a build
are shown in the following locations:

* The Artifacts column of Build history page
* The Execution details tab of the Build details page
* The Build Artifacts tab of the Build details page

For more information, see
[View build results](https://docs.cloud.google.com/build/docs/view-build-results).

---
## 2025-12-08

### Change

In build config files, the `mavenArtifacts` field now supports the
`deployFolder` field. You can use the `deployFolder` field to upload all Maven
files in a folder to a specific Artifact Registry repository. For more
information, see
[Upload all Maven files in a folder to an Artifact Registry repository](https://docs.cloud.google.com/build/docs/build-config-file-schema#upload-all-maven-files).

---
## 2025-10-09

### Changed

The Service Account User role has been removed from the Cloud Build Permissions page in the Google Cloud Console. Instead, when you enable certain roles on your Cloud Build service account, you can configure your Cloud Build Service account to impersonate the service account of the managed services related to those roles. This configuration lets you deploy builds using managed services while maintaining minimal permissions. For more information, see [Configure Cloud Build service account impersonation for managed services](https://docs.cloud.google.com/build/docs/deploying-builds/cb-sa-imp).

In addition, the Cloud Build Permissions page in the Google Cloud Console will only show the [legacy Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account#about_legacy) if your organization's policy allows it.

---
## 2025-09-29

### Feature

Developer Connect build triggers are now [generally available](https://cloud.google.com/products/#product-launch-stages).

You can now create build triggers that build from [repositories connected to Developer Connect](https://docs.cloud.google.com/build/docs/triggers#devcon-triggers) using the Google Cloud Console, `gcloud`, the Cloud Build API, and Terraform.

---
## 2025-09-02

### Feature

Dark theme is now available for Cloud Build. To enable the dark theme, in the Google Cloud console, click **Settings and utilities** > **Preferences**. In the navigation menu, click **Appearance**, and then select your color theme and click **Save**.

---
## 2025-08-15

### Feature

C3 and N2D machine families are now generally available in private pools. For a complete list of supported machines, see the [`machineType`](https://cloud.google.com/build/docs/private-pools/private-pool-config-file-schema#machinetype) entry in the private pool configuration file schema.

In addition, the **Create private pool** and **Edit private pool** pages now show a monthly estimate based on the pool's machine type configuration. For more information, see [View private pool price estimates](https://cloud.google.com/build/docs/private-pools/create-manage-private-pools#view-price).

---
## 2025-05-27

### Feature

You can now create build triggers that build from [repositories connected to Developer Connect](https://cloud.google.com/build/docs/triggers#devcon-triggers).

---
