# 581.0.0 (2026-08-18)

## 2026-08-18

### Breaking Changes

* **(Cloud Services)** Removed `gcloud beta services mcp enable`, `gcloud beta services mcp disable`, and `gcloud beta services mcp list` as MCP enablement is no longer required and they have been functioning as no-ops.

### AI Platform

* Added `gcloud beta ai semantic-governance-policy-engine deprovision`
  command to tear down a semantic governance policy engine, including its
  tenant project, GKE cluster, and PSC service attachments.
* Promoted `gcloud ai semantic-governance-policies` (`create`, `describe`,
  `update`, `delete`, `list`) and `gcloud ai
  semantic-governance-policy-engine` (`describe`, `update`, `deprovision`)
  commands from beta to GA.

### BigQuery

* Added fields `precedence` and `condition` to the commands `bq ls
  --reservation_assignment` and `bq show --reservation_assignment` output.
* Added the new `AUTOMATIC_MATERIALIZED_VIEW_REFRESH` job type for users to create reservation assignments with.

### Cloud Auth

* Enabled Enterprise Certificate Proxy (ECP) HTTP Proxy by default for context-aware mTLS requests.

### Cloud Bigtable

* Rebuilt cbt cli with newer version of bigtable client for CVE-2026-39883.

### Cloud IAM

* Updated `gcloud iam workforce-pools create-cred-config` and `gcloud iam workforce-pools create-login-config` to accept short-format provider audiences (`<pool>/<provider>`).
* Added `gcloud beta iam workforce-pools providers create-saml` and `gcloud beta iam workforce-pools providers update-saml` commands.

### Cloud Services

* **API Keys**: Added `--append` flag to `gcloud services api-keys update`
  command to merge new application and API target restrictions with existing
  key restrictions instead of replacing them.

### Cluster Director

* Fixed `gcloud cluster-director clusters create` to not create default compute resources when they are overridden by the user.
* Updated `gcloud cluster-director clusters create` to default to `hyperdisk-balanced` boot disks and restrict persistent disks (PD) for non-N2 and non-CT5P machine types.
* Fixed a validation error during cluster updates that concurrently modified storage resources and Slurm node sets.

### Compute Engine

* Added `gcloud compute target-ssl-proxies test-iam-permissions` command to test IAM permissions on a Compute Engine target SSL proxy in `beta`, `preview`, and `GA`.
* Added `--max-stream-duration` flag to `gcloud compute backend-services create` and `update` commands in beta, preview, and GA.
* Added `gcloud compute packet-mirrorings test-iam-permissions` command for beta, preview and GA tracks.

### Container

* Fixed issue where `gcloud` CLI would crash on corrupted `~/.kube/config`.
  Now you will now get a more detailed explanation about which section and line
  is wrong, to make troubleshooting easier. Corrupted kubeconfig will be backed
  up for further troubleshooting.

### Database Migration

* Added `--reserved-public-ip` and `--reserved-public-ip-nat-ips-count` flags to `gcloud database-migration private-connections create`.
* Added `--fetch-reserved-public-ips` flag to `gcloud database-migration connection-profiles fetch-static-ips`.

### Kubernetes Engine

* Add `--enable-slice-controller` flag in `gcloud container clusters create` and `gcloud container clusters update`.

### Oracle Database

* Added `--total-vm-storage-size-gb` flag to
  `gcloud oracle-database cloud-exadata-infrastructures configure-exascale`
  and `--properties-vm-backup-storage-type`,
  `--properties-vm-file-system-storage-type` flags to
  `gcloud oracle-database cloud-vm-clusters create` to support Exascale VM
  storage options.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
