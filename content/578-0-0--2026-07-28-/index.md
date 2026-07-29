# 578.0.0 (2026-07-28)

## 2026-07-28

### Breaking Changes

* **(Database Migration)** Made `--auto-commit` flag the default for `gcloud database-migration
  conversion-workspaces seed|convert|import-rules` operations. To disable
  auto-committing, use `--no-auto-commit` flag.

### Google Cloud CLI

* Fixed an issue where running `gcloud init` crashed when Enterprise Certificate Proxy (ECP) binaries were missing from configuration.
* Updated macOS Python Virtualenv for the `gcloud` CLI to 3.14.6.

### AlloyDB

* Promote AlloyDB Backup DR restore flags (`--backupdr-backup` and `--backupdr-data-source`) to the GA track.

### BigLake

* Fixed a bug where `gcloud biglake iceberg tables` commands failed to send the `X-Iceberg-Access-Delegation: vended-credentials` header.

### BigQuery

* Added `-f`/`--force` support to `bq rm --connection` to ignore NOT\_FOUND
  errors if the connection does not exist.
* Fixed reading configuration from `gcloud` CLI with `--nouse_google_auth` flag.
* Added a predefined label for jobs created in specific metrics environments.
* Updated the help text for several global flags.
* Updated command format in the user-agent HTTP header of API requests.

### Cloud Backup DR

* Added `--log-retention-days` flag across `gcloud backup-dr backup-plans create` and `update` across all release tracks to enable Point-in-Time Recovery (PITR) log retention configuration.

### Cloud Bigtable

* Added `--ignore-warnings` flag to `gcloud bigtable instances tables update` and `gcloud bigtable tables update`.
* Promoted `--ignore-warnings` flag of `gcloud bigtable materialized-views create` to GA.

### Cloud Composer

* Enabled Airflow CLI commands for Composer environments running Airflow 3.2.

### Cloud IAM

* Promoted `enabled-for-users-groups` option for `--scim-usage` flag to beta in `gcloud beta iam workforce-pools providers`.

### Cloud Run

* Added `--sandbox-launcher` flag to `gcloud beta run jobs` and
  `gcloud beta run worker-pools` command groups to allow setting a container as
  sandbox launcher when creating or updating a Cloud Run job or a worker pool.

### Cloud Workstations

* Added `--idle-action` flag to `gcloud alpha workstations configs create`,
  `gcloud alpha workstations configs update`, `gcloud beta workstations
  configs create`, and `gcloud beta workstations configs update` commands.

### Compute Engine

* Added `--network-tier` flag to `gcloud compute public-advertised-prefixes create` in beta.
* Added `--metadata-filter` flag to `gcloud compute forwarding-rules create` command across all release tracks.
* Added `--metadata-filter` flag to `gcloud compute forwarding-rules update` commands across all release tracks.
* Added `gcloud compute machine-images test-iam-permissions` command to test IAM permissions on a Compute Engine machine image in beta, preview, and GA.
* Promoted `regex_rewrite` support in `url_rewrite` block to beta for `gcloud compute url-maps`.
* Promoted the following `gcloud compute routers` command groups to GA:
  `add-named-set`, `add-named-set-element`, `download-named-set`,
  `get-named-set`, `list-named-sets`, `remove-named-set`,
  `remove-named-set-element`, and `upload-named-set`.
* Added `gcloud compute health-sources test-iam-permissions` command to test IAM permissions on a health source.
* Added `gcloud compute instant-snapshot-groups set-iam-policy` command to set the IAM policy for a Compute Engine instant snapshot group.
* Added `gcloud compute networks subnets test-iam-permissions` command in beta, preview, and GA.
* Added `gcloud compute image-views describe` command in beta.
* Added `gcloud compute snapshots test-iam-permissions` to test IAM permissions for Compute Engine snapshots.
* Added `gcloud compute interconnects attachments groups set-iam-policy` command to set IAM policy on an interconnect attachment group in beta, preview, and GA.
* Added `--internal-range` flag to `gcloud compute addresses create`
  to support allocating global internal IP addresses from an Internal Range
  for Private Service Connect.
* Updated `gcloud compute reservations hosts list` and `gcloud compute reservations hosts describe` to require `--reservation` when `--reservation-block` is specified.

### Developer Connect

* Updated `gcloud beta developer-connect account-connectors` commands to support Bring Your Own (BYO) and Bitbucket Cloud (BBC) connection types.

### GKE Hub

* Promoted `--view`, `--memberships`, `--filter`, and `--sort-by` flags on
  `gcloud container fleet|hub config-management describe` command to `beta`.

### Network Management

* Added `--source-dms-private-connection` flag to `gcloud network-management connectivity-tests`.

### Secret Manager

* Added the `--secret-type` flag to `gcloud secrets create` to support creating secrets of different types (e.g. Cloud SQL credentials).
* Added the `gcloud secrets enable-managed-rotation` command to enable managed rotation for a secret using Cloud SQL credentials.
* Added the `gcloud secrets rotate-secret` command to rotate a secret.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
