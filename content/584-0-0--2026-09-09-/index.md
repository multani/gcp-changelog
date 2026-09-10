# 584.0.0 (2026-09-09)

## 2026-09-09

### Breaking Changes

* **(Cloud Storage)** Deprecated `gcloud storage buckets anywhere-caches pause` command.

### Google Cloud CLI

* Deprecated `minikube` component in Google Cloud CLI. The component will be removed after January 31, 2027. Existing local configurations and clusters in `~/.minikube` will be preserved. Minikube is an open-source project and continues to be actively maintained. To avoid disruptions, please migrate to standard OSS Minikube installations: <https://minikube.sigs.k8s.io/docs/start/>.
* Upgraded OpenSSL version to 3.5.8 in Linux bundled Python to resolve CVE-2026-42508.

### AlloyDB

* Added `--edition` flag in `gcloud alloydb clusters create|update` for alpha and beta tracks.

### Apigee

* Added `gcloud apigee apis delete` which deletes an API proxy and all of its
  revisions. Undeploy every deployed revision first with `gcloud apigee apis
  undeploy`.

### Artifact Registry

* Added `gcloud artifacts files upload` which allows user to upload
  Conda packages to a Conda repository.

### BigLake

* Added `--cross-cloud-cache` to `gcloud biglake iceberg catalogs create` and `update` commands to configure cross-cloud cache per catalog.
* Added `--kms-key` flag to `gcloud biglake iceberg catalogs create` and `update` commands.
* Added `--kms-key` flag to `gcloud biglake delta-sharing catalogs create` and `update` commands.

### Cloud Backup DR

* Added `gcloud backup-dr auto-protection-policies` command group in alpha and beta tracks.
* Added `gcloud backup-dr auto-protection-bindings` command group in alpha and beta tracks.
* Added `gcloud beta backup-dr binding-matching-resources` command group to manage Backup and DR BindingMatchingResources.

### Cloud Firestore

* Promoted `gcloud firestore change-streams` commands to beta.
* Promoted search configuration options to GA for `gcloud firestore indexes composite create`.

### Cloud Managed Kafka

* Promoted `--public-cluster` and `--allowed-source-ip-ranges` flags to GA for `gcloud managed-kafka clusters create` and `gcloud managed-kafka clusters update`.

### Cloud Memorystore

* Promoted `--tags` flag of `gcloud redis instance create`.

### Cloud SQL

* Updated 'cloud-sql-proxy' packaged component to use 2.25.4 of the Cloud SQL Proxy.

### Cloud Services

* **API Keys**: Added `--[no-]check-existing-usage` flag to `gcloud services
  api-keys update` and `gcloud services api-keys delete` to verify whether
  the key has recent incompatible traffic before updating or deleting the key
  (defaults to true).

### Cluster Director

* Fixed an issue in `gcloud cluster-director clusters update` help text and documentation where `--update-slurm-partitions` included an unsupported `exclusive` flag in examples.

### Compute Engine

* Promoted `regex_rewrite` support in `url_rewrite` block to GA for `gcloud compute url-maps`.
* Added `--network-endpoint-group` flag to `gcloud compute backend-services create` command.
* Added `--ha-policy-fast-ip-move` flag to `gcloud compute backend-services create` command.
* Added `--ha-policy-leader-backend-group` and `--ha-policy-leader-instance` flags to `gcloud compute backend-services update` command.
* Added `--no-graceful-shutdown` flag to `gcloud compute instance-groups managed stop-instances` command across all release tracks.
* Added `--no-graceful-shutdown` flag to `gcloud compute instance-groups managed delete-instances` command across all release tracks.
* Added `--outlier-detection-*` flags to `gcloud compute backend-services create` and `update` commands to configure outlier detection settings.
* Promoted `gcloud compute recoverable-snapshots recover` to beta.
* Promoted `gcloud compute recoverable-snapshots delete` to beta.
* Promoted `gcloud compute recoverable-snapshots describe` to beta.
* Promoted `gcloud compute recoverable-snapshots list` to beta.
* Promoted `gcloud compute recoverable-snapshots set-iam-policy` to beta.
* Promoted `gcloud compute recoverable-snapshots test-iam-permissions` to beta.
* Promoted `gcloud compute instances get-vm-extension-state` to beta.
* Promoted `gcloud compute instances list-vm-extension-states` to beta.
* Promoted `enable-vpc-scoped-dns` sub-argument of `--network-interface` flag in `gcloud compute instances create` to GA.
* Promoted `enable-vpc-scoped-dns` sub-argument of `--network-interface` flag in `gcloud compute instance-templates create` to GA.
* Promoted `--share-setting` flag in `gcloud compute reservations update` to GA.
* Promoted `gcloud compute project-views describe` command to GA.

### Database Migration

* Added support for updating connectivity options (`--private-connection`,
  `--psc-service-attachment`, `--static-ip-connectivity`, and forward SSH flags
  where supported) in `gcloud database-migration connection-profiles update`.
* Added `--mysql-is-primary-destination` flag to `gcloud database-migration migration-jobs create` command to specify whether the destination for the migration job is a primary instance.

### Dataproc Metastore

* Promoted `gcloud metastore services migrations start`, `describe`, `list`,
  and `delete` to GA for one-shot migrations (`mode:BACKFILL`).
* Added support for `INCREMENTAL_SYNC` mode in public preview for
  iceberg migrations.

### Design Center

* Added `gcloud design-center spaces application-templates export` command to export IaC for an application template.
* Added `gcloud design-center spaces application-templates revisions export` command to export IaC for an application template revision.
* Added `--input-variable-aliases`, `--add-input-variable-aliases`,
  `--clear-input-variable-aliases`, and `--remove-input-variable-aliases` flags
  to `gcloud design-center components update` to manage input variable aliases.

### Developer Knowledge

* # Release notes for developer\_knowledge component.

---
