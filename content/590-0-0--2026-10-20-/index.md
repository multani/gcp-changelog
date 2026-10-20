# 590.0.0 (2026-10-20)

## 2026-10-20

### Breaking Changes

* **(Google Cloud CLI)** Removed the `gcloud-man-pages` component. Use `--help` for full command documentation.
* **(App Engine)** Removed the `app-engine-grpc` component from the Google Cloud CLI.
* **(Cloud Build)** Removed the Cloud Build Local Builder component (`cloud-build-local`) from the Google Cloud CLI.

### Google Cloud CLI

* Updated bundled Python on Linux and Windows, and in the Alpine-based Docker
  images, to pyOpenSSL 26.4.0 and cryptography 50.0.1. 32-bit Windows uses
  pyOpenSSL 26.2.0 and cryptography 48.0.1, the newest releases that support it.

### AI

* Updated `gcloud beta ai endpoints deploy-model` to request automatic resources for Gemini deployments on GDC connected endpoints.
  + If no replica counts are specified, the minimum replica count defaults to 1 only for `gemini-2.5-flash`.
  + Specifying flags that apply only to dedicated resources, such as `--machine-type` or `--accelerator`, now prints a warning and deploys with dedicated resources.

### Agent Identity

* Added `gcloud beta agent-identity auth-providers resolve-authorization`
  command.

### AlloyDB

* Added `--enable-public-dns` flag to `gcloud beta alloydb instances create|update`.

### Apigee

* Fixed an issue where `gcloud apigee` commands would fail with an
  `UnauthorizedRequestError` for users who authenticate using Mutual TLS (mTLS).

### App Engine

* Updated `gcloud beta app migrate-to-run` to default to the App Engine
  application's region instead of `us-central1` when neither `--region` nor
  the `run/region` property is set.

### BigLake

* Promoted `--federated-catalog-identity-mode` for `gcloud biglake iceberg
  catalogs create` to GA.
* Promoted `--federated-catalog-identity-mode` for `gcloud biglake iceberg
  catalogs update` to GA.
* Promoted `--metadata-service-directory-name` for `gcloud biglake iceberg
  catalogs create` to GA.
* Promoted `--metadata-service-directory-name` for `gcloud biglake iceberg
  catalogs update` to GA.
* `federated` value for `--catalog-type` flag of `gcloud biglake iceberg
  catalogs create` is now supported.

### Certificate Authority Service

* Added `--filter` flag to `gcloud privateca subordinates list`. The flag is
  able to allow filtering results based on specified boolean expression.

### Cloud Bigtable

* Build with 1.26.4 to resolve CVE-2026-39820.

### Cloud Bigtable Emulator

* Rebuild cbt-emulator for CVE-2026-39820.

### Cloud Dataflow

* Promoted `gcloud dataflow config-store-settings` to GA.

### Cloud Dataplex

* Fixed `gcloud dataplex dbt metadata-jobs create` so that dbt resources whose
  names contain a dot, such as tests on a model with a decimal version, are no
  longer rejected by the import job.
* Fixed `gcloud dataplex dbt metadata-jobs create` so that two dbt resources
  that map to the same Dataplex entry ID no longer fail the whole import job.
  The first is imported and a warning names the other.

### Cloud IAM

* Added `--vendor-type` flag to `gcloud iam workforce-pools providers create-oidc`, `create-saml`, `update-oidc`, and `update-saml` commands.

### Cloud Resource Manager

* Promoted `gcloud resource-manager capability-configs` to GA.
* Promoted `gcloud resource-manager boundary-configs` to GA.
* Promoted `gcloud resource-manager boundaries` to GA.

### Cloud Run

* Added `--dry-run` flag to `gcloud beta run domain-mappings create` to
  validate a domain mapping, including whether the domain is available,
  without creating it.

### Cloud SQL

* Added `POSTGRES_19` to `--database-version` flag of `gcloud sql instances create` and `gcloud sql instances patch`.
* Added `--no-replication-lag-max-seconds-for-recreate` flag to `gcloud beta sql instances patch` to disable recreating a lagging MySQL read replica.
* Updated 'cloud-sql-proxy' packaged component to use 2.26.2 of the Cloud SQL Proxy.

### Cloud Spanner

* Improved error output when `gcloud spanner cli` runs an incompatible
  `spanner-cli` binary found on `PATH` instead of the `spanner-cli`
  component; users are now directed to install the component.

### Cloud Workstations

* Added `enable-automatic-failover` to `--boost-config` flag in `gcloud beta workstations configs create` and `gcloud beta workstations configs update`.

### Compute Engine

* Added `compute instance-templates export` command to all release tracks.
* Removed WORKLOAD\_IDENTITY choise in `--identity-type` flag.
* Promoted `--instance-flexibility-policy` flag and min CPU platform and disk
  overrides to GA for `gcloud compute instance-groups managed create` and
  `update`.
* Added `compute instance-templates import` command to all release tracks.

### Database Migration

* Added `--failback` flag to `gcloud database-migration migration-jobs
  promote` command to promote a migration job from destination back to source
  during the FAILBACK phase.

### GKE Hub

* Promoted `--view`, `--memberships`, `--filter`, and `--sort-by` flags on
  `gcloud container fleet|hub config-management describe` command to `GA`.
* Updated `gcloud container fleet|hub memberships register` to allow skipping the Connect agent installation on non-GKE clusters via the `--no-install-connect-agent` flag.

### Kubernetes Engine

* Added the `reservedSystemCpus` kubelet config option to the `gcloud
  container clusters create`, `gcloud container node-pools create`, and
  `gcloud container node-pools update` commands. This option specifies the
  list of CPUs reserved for host system services.
* Added `ltsc2025` option to `--windows-os-version` flag of `gcloud container
  node-pools create` and `gcloud container node-pools update` to create or
  update Windows node pools using the Windows Server 2025 (LTSC2025) image.
* Updated default kubectl to 1.35.9.
* Additional kubectl versions:
  + 1.31.14
  + 1.32.13
  + 1.33.13
  + 1.34.12
  + 1.35.9
  + 1.36.5
  + 1.37.1
* Allowed `--num-nodes=0` for `gcloud container clusters create` to create
  a cluster without a default node pool on GKE versions that support it.
  Flags that only configure the default node pool, such as `--machine-type`
  and `--enable-autoscaling`, can't be used with `--num-nodes=0`.

### Network Connectivity

* Added `--purpose` flag to `gcloud network-connectivity internal-ranges
  create` to specify the purpose of the internal range.

### Network Security

* Promoted `--wildfire-analysis-profile` flag of
  `gcloud network-security security-profile-groups create` and
  `gcloud network-security security-profile-groups update` commands to GA.
* Promoted `gcloud network-security security-profiles wildfire-analysis`
  command group and its `create`, `delete`, `describe`, `list` and `update`
  commands to GA.
* Promoted `add-submission-rule`, `delete-submission-rule`,
  `add-inline-cloud-analysis-rule` and `delete-inline-cloud-analysis-rule`
  commands of `gcloud network-security security-profiles wildfire-analysis`
  to GA.

### Service Extensions

* Created a new set of commands for `gcloud service-extensions extension-bindings` (alpha and beta).
* Added `gcloud beta service-extensions cdn-edge-extensions` command group to manage `CdnEdgeExtension` resources.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
