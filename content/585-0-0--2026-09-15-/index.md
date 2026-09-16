# 585.0.0 (2026-09-15)

## 2026-09-15

### Breaking Changes

* **(Cloud Storage)** Deprecated `ADMIT_ON_SECOND_MISS` choice for `--admission-policy` flag in `gcloud storage buckets anywhere-caches create` and `gcloud storage buckets anywhere-caches update`.

### Google Cloud CLI

* Removed the legacy `--tls-offload` flag from
  `gcloud auth enterprise-certificate-config create` and deprecated the legacy
  C++ ECP TLS Offload Engine. Certificate-Based Access (CBA) requests now
  exclusively use the ECP HTTP Proxy (`ecp_http_proxy`).
* Added support for ANSI escape sequences and colorization in `tmux` environments.

### App Topology

* Promoted `gcloud app-topology` to GA and beta.

### BigLake

* Added `--cross-cloud-cache` to `gcloud biglake delta-sharing catalogs create` and `update` commands to configure cross-cloud cache per catalog.

### Cloud API Gateway

* Added `--enable-streaming` to `gcloud api-gateway gateways create`, which
  creates a gateway that serves response streaming: server-sent events, HTTP
  chunked transfer, WebSockets, and gRPC/HTTP2 bidirectional streaming. The
  streaming mode can only be set when the gateway is created.

### Cloud Backup DR

* Added `gcloud backup-dr auto-protection-policies` command group in alpha and beta tracks.
* Added `gcloud backup-dr auto-protection-bindings` command group in alpha and beta tracks.
* Added `gcloud backup-dr applied-auto-protection-policies` command group in alpha and beta tracks.
* Added `gcloud backup-dr binding-matching-resources` command group to manage Backup and DR Binding Matching Resources in alpha and beta tracks.

### Cloud Dataflow

* Added support for `--additional-pipeline-options` flag to
  `gcloud dataflow jobs run` command to support common runtime pipeline
  option assignments for classic Dataflow Templates.

### Cloud Filestore

* Added `--psc-requested-ip-address` flag to `gcloud filestore instances create`
  to allow specifying a desired IP address.

### Cloud IAM

* Promoted `enabled-for-users-groups` option for `--scim-usage` flag to GA in `gcloud iam workforce-pools providers`.

### Cloud Memorystore

* Promoted `--tags` flag of `gcloud memcache instances create to GA`.
* Promote `gcloud memorystore instances` basic auth feature to the GA release track:
  + Promote `--authorization-mode=token-auth` flag in `gcloud memorystore instances create` and `update` commands.
  + Promote new command groups and commands:
  + `gcloud memorystore instances create-token-auth-user`
  + `gcloud memorystore instances token-auth-users` (commands: `create-auth-token`, `delete`, `describe`, `list`)
  + `gcloud memorystore instances token-auth-users auth-tokens` (commands: `delete`, `describe`, `list`)

### Cloud Workstations

* Added `--disk-provisioned-iops` and `--disk-provisioned-throughput` flags to `gcloud beta workstations configs create` and `gcloud beta workstations configs update` commands.
* Added `--console-base-url` flag to `gcloud beta workstations clusters create`
  and `gcloud beta workstations clusters update` commands.

### Compute Engine

* Fixed an issue where updating labels on Interconnect Attachments using `gcloud compute interconnects attachments [dedicated|partner|provider|l2-forwarding] update --update-labels` failed.
* Allowed using project numbers in command arguments.
* Promoted `gcloud compute image-views describe` command to GA.
* Promoted `gcloud compute image-views list` command to beta and GA.
* Added `--content-type`, `--http-status`, `--backend-bucket`, and `--backend-service` flags to `gcloud beta compute url-maps invalidate-cdn-cache` to support extended invalidation matchers.
* Added support for wildcard (`*`) matching in `--host` flag of `gcloud beta compute url-maps invalidate-cdn-cache` (e.g., `--host="*.example.com"`).

### Compute OS Config

* Added Regional Endpoints (REP) support for `gcloud compute os-config` commands via `--endpoint-mode`.

### GKE Hub

* Added `--ignore-maintenance-policies`, `--ignore-cluster-disruption-budgets`,
  `--patch-only`, `--soak-duration-overrides-per-stage`,
  and `--soak-duration-override-all-stages` flags
  to `gcloud container fleet rolloutsequences upgrade`.

### Kubernetes Engine

* Updated default kubectl from 1.35.7 to 1.35.8.
* Added kubectl version 1.37.0 for the RAPID channel.
* Additional kubectl versions:
  + 1.31.14
  + 1.32.13
  + 1.33.13
  + 1.34.11
  + 1.35.8
  + 1.36.4
  + 1.37.0

### Transfer

* Added `--include-storage-classes` flag to `gcloud transfer jobs create` and `gcloud transfer jobs update`, and `--clear-include-storage-classes` flag to `gcloud transfer jobs update`.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
