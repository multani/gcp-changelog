# 586.0.0 (2026-09-22)

## 2026-09-22

### Breaking Changes

* **(Google Cloud CLI)** The `google-cloud-sdk` Snap package will be deprecated and removed on September 29th, 2026. Please migrate to the `google-cloud-cli` package. For more information, see <https://docs.cloud.google.com/sdk/docs/downloads-snap>.
* **(Google Cloud CLI)** Deprecated and removed the bundled Kustomize component ('kustomize') from the Google Cloud CLI. Kustomize is an open-source project and continues to be maintained.
  + To avoid disruptions, please migrate to standard OSS kustomize installation: <https://kubectl.docs.kubernetes.io/installation/kustomize/> or use the built-in 'kubectl kustomize ...'.
* **(Google Cloud CLI)** The `gcloud` CLI man pages component (`gcloud-man-pages`) is deprecated and
  will be removed in release version 590.0.0 on October 20th, 2026. Please use
  the built-in `--help` flag for full command documentation.
* **(Cloud Services)** Updated `gcloud services api-keys create` and
  `gcloud services api-keys update` to require `--api-target` restrictions
  across GA and beta.
* **(Cloud Services)** Removed `--clear-restrictions` flag from `gcloud services api-keys update`.
* **(Kpt)** Removed `kpt` component from the Google Cloud CLI. Kpt is an open-source project and continues to be actively maintained. To avoid disruptions, please migrate to the standard OSS kpt installation: <https://kpt.dev/installation/kpt-cli/>.

### Apigee

* Added support for DRZ endpoints for CH region.

### Artifact Registry

* Fixed an issue where Artifact Registry Docker commands failed to parse
  domain-scoped project URIs.

### Audit Manager

* Added the `gcloud audit-manager audit-schedules` command group, supporting `create`, `list`, and `update` commands.

### BigLake

* Promoted to GA `gcloud biglake iceberg catalogs create
  --[federated-catalog-type, glue-aws-region, glue-aws-role-arn,
  glue-warehouse, namespace-filters, refresh-interval, secret-name,
  service-directory-name, snowflake-account-identifier, snowflake-role,
  snowflake-warehouse, unity-catalog-name, unity-instance-name,
  unity-service-principal-application-id, workday-base-url, workday-tenant]`.
* Promoted to beta `gcloud beta biglake iceberg catalogs create
  --[service-directory-name, snowflake-account-identifier, snowflake-role,
  snowflake-warehouse, workday-base-url, workday-tenant]`.
* Promoted to beta `gcloud beta biglake iceberg catalogs update
  --[service-directory-name, snowflake-role]`.
* Promoted to GA `gcloud biglake iceberg catalogs update --[glue-aws-role-arn,
  namespace-filters, refresh-interval, secret-name, service-directory-name,
  snowflake-role, unity-service-principal-application-id]`.

### Cloud Observability

* Added `create` and `update` methods to `gcloud observability buckets`
  command group.
* Promoted Observability commands from `BETA` to `GA`.

### Cloud Run

* Added Custom URL support on `gcloud domain mappings create`, allowing users
  to create easy to remember and shareable subdomains of the format
  `<user-chosen>`.cloud.run
* Added `--clear-key` flag to `gcloud beta run instances deploy` and `gcloud
  beta run instances update` to remove a previously set CMEK key reference.

### Cluster Director

* Added `networkTags` property to instance configuration flags in `gcloud beta
  cluster-director clusters create`.
* Added existing NFS storage support (`--nfs`, `--add-nfs`, `--remove-nfs`,
  and `existingNfs` in `--config`) in `gcloud beta cluster-director clusters
  create/update`.

### Compliance Manager

* Added `gcloud compliance-manager framework-deployments update` to update framework deployments across organization and project scopes.

### Compute Engine

* Added `gcloud compute url-maps test-iam-permissions` command to test IAM permissions on a URL map in beta, preview, and GA.
* Promoted `--request-body-to-exclude` flag of `gcloud compute security-policies rules add-preconfig-waf-exclusion` and `gcloud compute security-policies rules remove-preconfig-waf-exclusion` to GA.
* Promoted `--request-body-to-exclude` flag of
  `gcloud compute org-security-policies rules add-preconfig-waf-exclusion`
  and `gcloud compute org-security-policies rules
  remove-preconfig-waf-exclusion` to GA.
* Promoted `--preemption-notice-duration` flag to `gcloud compute instances`
  in GA.
* Promoted `gcloud compute interconnects set-name` to beta.

### Database Migration

* Added `--load-parallel-level` flag to `gcloud database-migration
  migration-jobs create` and `gcloud database-migration migration-jobs update`
  commands to specify the parallelism level during initial load for MySQL
  migrations.

### Design Center

* Added `gcloud design-center spaces applications recommend-iam-roles` command to get recommended IAM roles for a Design Center application.

### Developer Knowledge

* Promoted `gcloud developer-knowledge` commands to GA.

### Device Run

* Promoted `gcloud device-run sessions submit xctest` to beta.
* Added `gcloud device-run software-versions list` command to list available test software versions.
* Added `gcloud device-run software-versions describe` command to describe a specific software version.

### Network Connectivity

* Promoted `--hub`, `--auto-accept`, and `--psc-routing-enabled` flags of `gcloud network-connectivity transports create` to GA.

### Network Security

* Updated `gcloud network-security authz-policies import` to support `DENY_BY_DEFAULT` action.
* Added `gcloud network-security firewall-endpoints wildfire-verdict-change-requests` commands to the ALPHA and BETA release tracks.

### Orchestration Pipelines

* Added `gcloud beta orchestration-pipelines info` command to display information about the orchestration pipelines library and supported model version.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
