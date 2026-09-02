# 583.0.0 (2026-09-01)

## 2026-09-01

### AlloyDB

* Added support for `POSTGRES_19` as a version in `alloydb clusters create` for alpha and beta tracks.
* Added support for `POSTGRES_19` as a version in `alloydb clusters migrate-cloud-sql` for alpha and beta tracks.

### Apigee

* Fixed an issue where `gcloud apigee apis import --from-template` nested
  `<FaultRule>` and `<DefaultFaultRule>` steps inside a `<Request>` element,
  which caused the generated fault rules to run no steps. Steps are now
  emitted as direct children, and fault rules are read correctly in either
  form when importing a bundle.
* Modified `gcloud apigee apis import --from-template` to ignore the `mode`
  field when it is set on a fault rule and to log a warning. The field applies
  only to flows.

### BigQuery

* Added support for `--service_directory_service` flag for `bq mk --connection`
  and `bq update --connection` commands for Azure connections.
* Deprecated `--s3_service_directory_service` flag. Use
  `--service_directory_service` instead for `bq mk --connection` and
  `bq update --connection` commands for AWS connections.
* Added `creationTime` and `updateTime` to be displayed in `bq show` for
  reservation group.
* Added `--precedence` and `--condition` flags to `bq mk` and `bq update` for
  reservation assignments.

### Cloud Access Context Manager

* Promoted `gcloud access-context-manager lookup-configured-perimeter` to beta and GA.

### Cloud Bigtable Emulator

* Rebuilding cbt emulator with go version 1.25.9 which fixed CVE-2026-27140.

### Cloud Composer

* Added `gcloud beta composer environments hibernate` command to hibernate a Cloud Composer environment.
* Added `gcloud beta composer environments resume` command to resume a Cloud Composer environment.
* Added `--enable-development-mode` flag to `gcloud beta composer environments create` to enable development mode for environments.

### Cloud Run

* Added an interactive prompt when creating or updating Cloud Run jobs
  configured with GPUs and task timeouts greater than 1 hour in
  `gcloud beta run jobs` command group.
* Added `--identity-certificate`, `--identity-type`, and `--functional-type`
  flags to the beta track for `gcloud run deploy` and
  `gcloud run services update` to configure workloads with Agent Registry and
  Agent Identity.
* Added `--identity-certificate`, `--identity-type`, and `--functional-type`
  flags to `gcloud beta run jobs` command groups to configure workloads with
  Agent Registry and Agent Identity.

### Cloud SQL

* Updated 'cloud-sql-proxy' packaged component to use 2.25.3 of the Cloud SQL Proxy.

### Cloud Storage

* Tuned download performance for gRPC bidi streaming used by RAPID storage in `gcloud storage`.

### Cluster Director

* Fixed an issue where creating a cluster using `--quickstart-cluster` (or
  any other reference architecture) would automatically inject default storage
  resources (such as managed Lustre) even when custom storage configurations
  (e.g. `--filestores`) were explicitly specified.
* Promoted `gcloud cluster-director` to GA.

### Compute Engine

* Added `--no-graceful-shutdown` flag to `gcloud compute instance-groups managed stop-instances` command across all release tracks.
* Added `--no-graceful-shutdown` flag to `gcloud compute instance-groups managed delete-instances` command across all release tracks.
* Added `--no-graceful-shutdown` flag to `gcloud compute instance-groups managed recreate-instances` command across all release tracks.
* Added `--no-graceful-shutdown` flag to `gcloud compute instance-groups managed delete` command across all release tracks.
* Added `--outlier-detection-*` flags to `gcloud compute backend-services create` and `update` commands to configure outlier detection settings.
* Promoted `gcloud compute recoverable-snapshots recover` to beta.
* Promoted `gcloud compute recoverable-snapshots delete` to beta.
* Promoted `gcloud compute recoverable-snapshots describe` to beta.
* Promoted `gcloud compute recoverable-snapshots list` to beta.
* Promoted `gcloud compute recoverable-snapshots set-iam-policy` to beta.
* Promoted `gcloud compute recoverable-snapshots test-iam-permissions` to beta.
* Promoted `gcloud compute snapshot-recycle-bin-policy describe` to beta.
* Promoted `gcloud compute snapshot-recycle-bin-policy patch` to beta.
* Promoted `gcloud compute snapshots get-effective-recycle-bin-rule` to beta.

### Database Migration

* Added support for homogeneous MySQL destination connection profiles for
  quickstart migrations in `gcloud database-migration connection-profiles create
  mysql` and `gcloud database-migration connection-profiles update`.

### Distributed Cloud Edge

* Promoted `gcloud edge-cloud zones describe`, `get-iam-policy`, `list`, `roles list`, and `set-iam-policy` to GA.
* Promoted `gcloud edge-cloud services describe`, `enable`, and `list` to GA.
* Promoted `gcloud edge-cloud projects describe`, `enable`, and `list` to GA.
* Promoted `gcloud edge-cloud service-accounts create`, `delete`, `describe`, and `list` to GA.
* Promoted `gcloud edge-cloud service-accounts keys create`, `describe`, `disable`, and `list` to GA.
* Promoted `gcloud edge-cloud api-keys create`, `delete`, `describe`, and `list` to GA.
* Promoted `--control-plane-node-system-partition-size-gib` flag from alpha to GA for `edge-cloud container clusters create`.

### GKE Hub

* Added `--ignore-maintenance-policies`, `--ignore-cluster-disruption-budgets`,
  `--soak-duration-overrides-per-stage` and `--soak-duration-override-all-stages`
  flags to `gcloud beta container fleet rolloutsequences upgrade`.
* Added `--patch-only` flag to `gcloud beta container fleet rolloutsequences upgrade`.

### Kubernetes Engine

* Updated default kubectl from 1.35.6 to 1.35.7.
* Additional kubectl versions:
  + 1.31.14
  + 1.32.13
  + 1.33.13
  + 1.34.11
  + 1.35.8
  + 1.36.4

### Network Services

* Promoted `gcloud network-services telemetry-policies delete` to beta.
* Promoted `gcloud network-services telemetry-policies describe` and
  `gcloud network-services telemetry-policies list` to beta.
* Promoted `gcloud network-services telemetry-policies export` and
  `gcloud network-services telemetry-policies import` to beta.

### Orchestration Pipelines

* Added BUNDLE\_ID as a default variable to allow dynamic referencing
  in pipeline configurations. BUNDLE\_ID resolves to the Git repository name,
  auto-generated local bundle name, or the current working directory name as
  a fallback. Used in `gcloud orchestration-pipelines deploy` command.

### Transfer

* Promoted `--match-glob` flag in `transfer jobs create` to GA.
* Promoted `--match-glob` flag in `transfer jobs update` to GA.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
