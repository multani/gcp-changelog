# 574.0.0 (2026-06-23)

## 2026-06-23

### AI Platform

* Added `gcloud beta ai semantic-governance-policy-engine deprovision`
  command to tear down a semantic governance policy engine, including its
  tenant project, GKE cluster, and PSC service attachments.

### Agent Identity

* Added `gcloud beta agent-identity auth-providers get-iam-policy|set-iam-policy|add-iam-policy-binding|remove-iam-policy-binding|test-iam-permissions` commands.

### Agent Registry

* Added `gcloud agent-registry` command group to manage Agent Registry resources.

### Backup For GKE

* Made `gcloud container backup-restore` command groups compatible with non-default universe domains.

### BigQuery

* Fixed a bug where `stderr` messages from `gcloud` CLI output would be printed to `stdout`.
* Added `--gcloud_config_cache` flag to enable caching data retrieved from the `gcloud` CLI.
* Added display of container request concurrency of BigQuery Python UDF in `bq show --routine`.
* Added information about AI Agent in the execution environment to the user-agent HTTP header in the API request.

### Cloud Datastream

* Added Regional Endpoints (REP) support for all Datastream commands.

### Cloud Memorystore

* Added `--zone-distribution-config-zones` flag to `gcloud memorystore instances create` command. This flag lets users specify multiple zones when they create a `MULTI_ZONE` cluster.
* Added `--zone-distribution-config-zones` flag to `gcloud redis clusters create` command. This flag lets users specify multiple zones when they create a `MULTI_ZONE` cluster.

### Cluster Director

* Added support for creating clusters using `--quickstart-cluster` in `gcloud beta cluster-director clusters create`.

### Colab

* Added Hyperdisk options to `--disk-type` of `gcloud colab runtime-templates create`: `HYPERDISK_BALANCED`.

### Compute Engine

* Fixed an issue where `gcloud compute url-maps import` reset custom `timeout` and `retryPolicy` (specifically `numRetries`) values to defaults when updating an existing URL map.
* Added `--vsock-mode` flag to `gcloud compute instances create`,
  `gcloud compute instance-templates create`, `gcloud compute instances bulk
  create`, and `gcloud compute queued-resources create` in ALPHA to support
  enabling/disabling VSOCK mode.
* Promoted `--purpose` flag to `gcloud compute public-delegated-prefixes create` in beta.

### Database Migration

* Added Regional Endpoints (REP) support for all Database Migration Service (DMS) commands.

### Kubernetes Engine

* Updated default kubectl from 1.35.3 to 1.35.6.
* Added new kubectl version 1.36.2 for the RAPID channel.
* Additional kubectl versions:
  + kubectl.1.30 (1.30.14)
  + kubectl.1.31 (1.31.14)
  + kubectl.1.32 (1.32.13)
  + kubectl.1.33 (1.33.13)
  + kubectl.1.34 (1.34.9)
  + kubectl.1.35 (1.35.6)
  + kubectl.1.36 (1.36.2)

### Network Security

* Promoted `gcloud network-security ull-mirroring-engines` and `gcloud network-security ull-mirroring-collectors` commands to beta.
* Promoted `gcloud network-security ull-mirroring-engines` and `gcloud network-security ull-mirroring-collectors` commands to GA.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
