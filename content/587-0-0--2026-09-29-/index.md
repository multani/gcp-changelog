# 587.0.0 (2026-09-29)

## 2026-09-29

### Breaking Changes

* **(Cloud Storage)** Removed `gcloud storage buckets anywhere-caches pause` command.
* **(Distributed Cloud Edge)** Removed deprecated `gcloud edge-cloud container vpn-connections` command group.

### Google Cloud CLI

* Updated `gcloud` CLI to support Python v3.15.
* Updated Linux and Windows bundled Python to upgrade `grpcio` to 1.84.0 and remove `setuptools`.

### AI Platform

* Added `--agent-response-denial-message` flag to `gcloud ai
  semantic-governance-policies create` and `gcloud ai
  semantic-governance-policies update` (and their `beta` equivalents) to set a
  custom message that is shown to end users when a policy denies a request.

### Agent Registry

* Updated `gcloud agent-registry bindings create` to make `--source-identifier` optional.

### AlloyDB

* Promoted IAM Group user types to GA.

### Artifact Registry

* Updated help text for `gcloud artifacts repositories create` to clarify that
  custom remote repository URIs must use HTTPS.

### BigQuery

* Modified `bq update --connection` to allow clearing
  `serviceDirectoryService` on AWS and Azure cross-cloud connections by
  passing `--service_directory_service=''` (when this flag value is empty,
  BigQuery uses the public internet to query the data instead of Cross-Cloud
  Interconnect).
* Updated `bq mk --migration_workflow`, `bq show --migration_workflow`, `bq rm
  --migration_workflow`, and `bq ls --migration_workflow` to skip unnecessary
  setup steps.

### Cloud Build

* Added `--worker-release` flag to `gcloud builds submit`, `gcloud builds
  worker-pools create`, and `gcloud builds worker-pools update` to
  [specify the worker release channel or version](https://docs.cloud.google.com/build/docs/release-channels).

### Cloud Dataplex

* Promoted `gcloud dataplex dbt` to GA.

### Cloud Dataproc

* Added `--multizone` flag to `gcloud dataproc clusters create` and `gcloud
  dataproc workflow-templates set-managed-cluster` to allow creating a
  multi-zonal cluster where instances can be created across multiple zones
  within the region.

### Cloud Filestore

* Made `--network` flag optional on `gcloud beta filestore instances create`
  to support Private Service Connect (PSC) with user-created-endpoint.

### Cloud Identity-Aware Proxy

* Added `gcloud beta iap tcp add-iam-policy-binding` which adds an IAM policy
  binding to an Identity-Aware Proxy TCP IAM resource, including Cloud Run
  tunnel resources.
* Added `gcloud beta iap tcp remove-iam-policy-binding` which removes an IAM
  policy binding from an Identity-Aware Proxy TCP IAM resource, including
  Cloud Run tunnel resources.
* Added `gcloud beta iap tcp get-iam-policy` which displays the IAM policy for
  an Identity-Aware Proxy TCP IAM resource, including Cloud Run tunnel
  resources.
* Added `gcloud beta iap tcp set-iam-policy` which replaces the IAM policy for
  an Identity-Aware Proxy TCP IAM resource, including Cloud Run tunnel
  resources.

### Cloud Managed Lustre

* Promoted `gcloud lustre instances directory-policies` command group to GA.
* Added `--target-version` flag to GA `gcloud lustre instances create` and `gcloud lustre instances update`.

### Cloud Run

* Added `--[no-]use-http2` flag to `gcloud run instances deploy` to configure
  whether to use HTTP/2 for connections to the instance.
* Added support for custom URLs with `--domain` flag in `gcloud beta run
  deploy`.
* Added `gcloud beta run services ssh` which starts a secure, interactive
  shell session with an instance of a Cloud Run service.
* Added `gcloud beta run instances ssh` which starts a secure, interactive
  shell session with a Cloud Run instance.
* Promoted `type=ephemeral-disk` in `--add-volume` flag to GA for `gcloud run
  deploy`, `gcloud run jobs deploy`, `gcloud run worker-pools deploy`,
  '`gcloud run jobs create`, `gcloud run jobs update`, `gcloud run services
  create`, `gcloud run worker-pools create`, and `gcloud run worker-pools
  update`.
* Promoted `--scaling-cpu-target` and `--scaling-concurrency-target` flags to
  the GA track for `gcloud run deploy` and `gcloud run services update`.
* Changed the maximum accepted value of the `--scaling-cpu-target` flag from
  `0.95` to `0.90` to match the Cloud Run API.

### Cloud Tasks

* Added `gcloud alpha|beta tasks batch-create` command, which creates multiple
  tasks from a JSON or YAML file in a single batch operation.
* Added `--from-file` and `--failed-tasks-file` to
  `gcloud alpha|beta tasks delete`, which delete multiple tasks in a single
  batch operation.
* Added the task-level retry flags `--max-attempts`, `--max-retry-duration`,
  `--min-backoff`, `--max-backoff`, and `--max-doublings` to
  `gcloud alpha|beta tasks create-http-task` and
  `gcloud alpha|beta tasks create-app-engine-task`. These flags override the
  queue-level retry configuration for an individual task.

### Cloud Workstations

* Added regional endpoint support for `gcloud workstations`.

### Compute Engine

* Added `<get|set>-iam-policy` and `<add|remove>-iam-policy-binding` to
  `gcloud beta compute ssl-policies`.
* Promote `--kms-key` flag for `gcloud compute snapshots create` to v1.
* Promoted `gcloud compute interconnects set-name` to GA.
* Added `--instance-flexibility-policy` flag for `gcloud compute instances
  bulk create` command in beta.
* Added `min-cpu-platform` field in `--instance-selection` flag of `gcloud
  compute instances bulk create` in beta.
* Updated `gcloud compute image-views list` to query public image projects by default and filter out deprecated images.
* Added `--standard-images`, `--preview-images`, and `--show-deprecated` flags to `gcloud compute image-views list`.

### Compute Firewall Policies

* Promoted `--priority` and `--associated-policy-to-be-replaced` flags of
  `gcloud compute network-firewall-policies associations create` to GA.
* Promoted `gcloud compute network-firewall-policies associations update`
  command to GA.

### Device Run

* Added `--locale` flag to `gcloud device-run sessions submit xctest` to switch the application locale before running tests.
* Promoted `gcloud device-run sessions submit android-executable` to beta.

### Network Security

* Promoted `gcloud network-security rate-limit-policies` to beta.

### Security Command Center

* Added `--[no-]deletion-notifications-enabled` flag to `gcloud scc bqexports
  create`, `gcloud scc bqexports update`, `gcloud scc notifications create`,
  and `gcloud scc notifications update` to configure whether notifications are
  sent for deleted findings.

### Vector Search

* Added `--dense-scann-target-recall` to `gcloud vector-search collections
  data-objects search` to accept a query-time target recall (a value in `[0,
  1]`) for dense index search.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
