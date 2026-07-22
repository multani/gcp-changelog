# 577.0.0 (2026-07-21)

## 2026-07-21

### Agent Identity

* Promoted `gcloud agent-identity auth-providers` and `gcloud agent-identity access-summaries` to GA.

### AlloyDB

* Modify flag `--no-enable-autoscaler` of `gcloud beta alloydb instances create|update` commands to only set the `enabled` field to `false` and not clear autoscaling config.
* Modify `gcloud beta alloydb instances update` command to only allow one of
  `--autoscaler-delete-schedule`, `--autoscaler-disable-schedule`,
  `--autoscaler-enable-schedule`, or `--autoscaler-set-schedule` to be
  specified.

### Artifact Registry

* Added `connector-repository` mode to `gcloud artifacts repositories create`.

### BigQuery

* Added support for `--s3_service_directory_service` flag to pass custom
  Service Directory endpoints for AWS connection make and update operations.
  This is used for routing traffic over a private network connection through
  Cross-Cloud Interconnect.
* Updated the data source of agent name value set in the user agent HTTP
  header.
* Stopped enforcing `bq init` when `--oauth_access_token` is provided.

### Cloud Bigtable

* fix: cbt cli escape row keys and column qualifiers in printRow.

### Cloud Firestore Emulator

* Release Cloud Firestore emulator v1.22.0
  + Added DML support for the Firestore Pipelines API
  + Added ability to model when composite indexes are required in Datastore mode using new `--require-indexes` and `--index-file` flags
  + Added depreciation warning for JRE versions <25

### Cloud Key Management Service

* (GA) Added `--folder` flag to
  `gcloud kms autokey-config show-effective-config` to retrieve the effective
  Cloud KMS Autokey configuration for folders. The `--project` and `--folder`
  flags are now optional, defaulting to the current project.

### Cloud Workstations

* Added `gcloud beta workstations suspend` and `gcloud alpha workstations suspend` commands.

### Compute Engine

* Added `gcloud compute machine-images test-iam-permissions` command to test IAM permissions on a Compute Engine machine image in beta, preview, and GA.
* Promoted `regex_rewrite` support in `url_rewrite` block to beta for `gcloud compute url-maps`.
* Promoted the following `gcloud compute routers` command groups to GA:
  `add-named-set`, `add-named-set-element`, `download-named-set`,
  `get-named-set`, `list-named-sets`, `remove-named-set`,
  `remove-named-set-element`, and `upload-named-set`.
* Added `gcloud compute health-sources test-iam-permissions` command to test IAM permissions on a health source.
* Added `--logging-http-request-headers` and `--logging-http-response-headers`
  flags to `gcloud compute backend-services create` and `update` commands to
  configure Cloud Logging HTTP headers for external L7 load balancers.
* Added `--local-ssd-encryption-mode` flag to `gcloud compute instances create` to specify the encryption mode for Local SSDs.
* Deprecated customer-supplied encryption keys (CSEK) flags
  `--csek-key-file`, `--require-csek-key-create`,
  `--source-machine-image-csek-key-file`, `--source-disk-csek-key`,
  `--source-disk-key-file`, and `--source-instant-snapshot-key-file` for
  `gcloud compute` commands.

### GKE Hub

* Changed both `--config` flag on
  `gcloud beta container fleet|hub config-management apply` command and
  `--fleet-default-member-config` flag on
  `gcloud beta container fleet|hub config-management enable` command to no
  longer default `spec.upgrades: manual` population since auto-upgrades is no
  longer supported from Config Sync version 1.21.0 and `spec.upgrades: manual`
  is behaviorally equivalent to not setting this field.

### Kubernetes Engine

* Fix overwriting autoscaling settings in `gcloud container clusters update`.

### Network Security

* Updated `gcloud beta network-security authz-policies import` to support `networkRules` and `snis` fields.

### Recaptcha

* Added `--universal` option to `gcloud recaptcha keys create` and
  `gcloud recaptcha keys update`.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
