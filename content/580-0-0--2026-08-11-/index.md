# 580.0.0 (2026-08-11)

## 2026-08-11

### Breaking Changes

* **(Google Cloud CLI)** The `google-cloud-sdk` Snap package will be deprecated and removed on September 29th, 2026. Please migrate to the `google-cloud-cli` package. For more information, see <https://docs.cloud.google.com/sdk/docs/downloads-snap>.

### Google Cloud CLI

* Fixed Google Compute Engine residency detection to prevent authentication
  failures due to transient issues and command latency regressions in
  non-Google Cloud environments.

### Apihub

* Promoted `gcloud apihub locations configure-and-deploy-server` command to GA. This command configures and deploys an MCP (Model Context Protocol) server on Apigee X via API Hub.

### Certificate Authority Service

* Added first-party activation support to `gcloud privateca subordinates activate` via `--issuer-pool`, `--issuer-location`, and `--issuer-ca` flags.
* Added suggestion to use `gcloud privateca subordinates activate` when `gcloud privateca subordinates create` with issuer flags fails due to an already existing subordinate CA.

### Certificate Manager

* Added `--tags` flag to `gcloud certificate-manager` create commands (`certificates create`, `dns-authorizations create`, `issuance-configs create`, `maps create`, and `trust-configs create`).

### Cloud Backup DR

* Added selective disk backup properties (`boot-disk-only` and `disk-exclusion-labels`) under `--compute-instance-properties` in `gcloud backup-dr backup-plans create` and `update` commands.
* Added `--source-instance-boot-disk` and `--source-instance-disk-device-name` flags to `gcloud backup-dr backups restore disk` for individual disk restore from compute instance backup.

### Cloud Composer

* Enabled the 'backfill' Airflow CLI sub-command for Composer environments running Airflow 3.
* Enabled the 'config lint' Airflow CLI sub-command for Composer environments running Airflow 2.11.0 or higher.

### Cloud Dataflow

* Added `gcloud dataflow jobs pause` and `gcloud dataflow jobs resume` commands.
* Added `--enable-turnkey-alerts` flag to `gcloud dataflow jobs run` and `gcloud dataflow flex-template run`.

### Cloud IAM

* Added support for X.509 certificate-based credentials and locational mTLS endpoints to `gcloud iam workload-identity-pools create-cred-config`.

### Cloud Spanner

* Update `gcloud spanner backups list` command to display INSTANCE\_PARTITIONS column in GA track.

### Cloud Storage

* `gcloud storage rsync`:
  + Skipping syncing files which goes outside of destination directory.

### Cluster Director

* Updated `gcloud cluster-director clusters create` to default to dynamic nodes when using flex start.

### Compute Engine

* Added `gcloud compute resource-policies test-iam-permissions` command to test IAM permissions on a Compute Engine resource policy in GA, beta, preview, and alpha.
* Added `gcloud compute snapshot-groups set-iam-policy` command in beta.
* Added `--kms-key-service-account` to `gcloud compute disks create`,
  `gcloud compute images create`, `gcloud compute machine-images create` and
  `gcloud compute snapshots create` for beta track.
* Added `--boot-disk-kms-key-service-account` and
  `--instance-kms-key-service-account` to `gcloud compute instances create` and
  `gcloud compute instance-templates create` for beta track.
* Added `--consistent-hash-minimum-ring-size` flag to
  `gcloud compute backend-services create` and `update` commands.
* Added `--circuit-breakers-max-requests` flag to `gcloud compute backend-services create` and `update` commands.
* Added `gcloud compute backend-services test-iam-permissions` command to test IAM permissions on a Compute Engine backend service in beta, preview, and GA.
* Added `gcloud compute ssl-policies test-iam-permissions` command to test IAM permissions on a Compute Engine SSL policy in beta.
* Added `gcloud compute firewall-policies test-iam-permissions` command.
* Promoted `--graceful-shutdown`, `--graceful-shutdown-max-duration`, and
  `--no-graceful-shutdown` flags to the GA track for `gcloud compute instances`
  and `gcloud compute instance-templates` commands.
* Added `--identity-type` flag to `gcloud compute instances create`,
  `gcloud compute instances update`, and
  `gcloud compute instance-templates create` in alpha.
* Promoted exapool capacity flags to beta and GA tracks for
  `gcloud compute storage-pools update` command.
* Added `--maintenance-freeze-duration` and `--clear-maintenance-freeze-duration` flags to `gcloud compute instances set-scheduling` and `gcloud compute instances create` in beta.
* Added `gcloud compute images test-iam-permissions` command to test IAM permissions on a Compute Engine image in beta, preview, and GA.

### Device Run

* Promoted `gcloud device-run sessions wait` command to beta.
* Updated `--instrumentation-timeout` flag of `gcloud beta device-run sessions submit instrumentation` to allow a maximum duration of 3 hours.
* Updated `gcloud device-run devices describe` to display `hardware_type` instead of `form`.
* Updated `gcloud device-run devices list` to display `HARDWARE_TYPE` column instead of `FORM`.

### GKE Hub

* Promoted API field schema for `--fleet-default-member-config` flag on
  `gcloud container fleet|hub config-management enable` command to `beta`.

### Metastore

* Updated `gcloud beta metastore services migrations start` to support migrations to Lakehouse runtime catalog(s).
* Deprecated Cloud SQL migration arguments in `gcloud beta metastore services migrations start`.

### Network Connectivity

* Added `--export-psc-published-services-and-regional-google-apis` and
  `--export-psc-global-google-apis` flags to
  `gcloud beta network-connectivity hubs create` and
  `gcloud beta network-connectivity hubs update` commands.

### Network Security

* Promoted `mcp` and `policyProfile` fields to GA in `gcloud network-security authz-policies import` and `export` commands.
* Made `loadBalancingScheme` optional in `gcloud network-security authz-policies import` and `export` commands.

### Network Services

* Promoted `gcloud network-services telemetry-policies delete` command to BETA.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
