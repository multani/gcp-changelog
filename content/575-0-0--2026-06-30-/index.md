# 575.0.0 (2026-06-30)

## 2026-06-30

### Google Cloud CLI

* Added `any-reservation-then-fail` argument for flag `--reservation-affinity`
  in `gcloud container clusters node-pools create`.

### Agent Registry

* Added `gcloud agent-registry` command group to manage Agent Registry resources.

### AlloyDB

* Added `--failover` flag to `gcloud beta alloydb clusters promote` to support cross-region failover.

### Apigee

* Added `gcloud apigee apis import` which allows customers to upload API Proxy
  bundles in archive ZIP or feature template YAML format.

### Artifact Registry

* Expose the Registry URL in the output of `gcloud artifacts repositories describe` and in the output of `gcloud artifacts repositories create` (upon synchronous creation).

### Assured Workloads

* Added `SWITZERLAND_DATA_BOUNDARY_WITH_ACCESS_JUSTIFICATIONS` option to `--compliance-regime` flag of `gcloud assured workloads create`.

### BigLake

* Added `gcloud biglake hive tables create` to beta.

### Cloud Access Context Manager

* Exposed `--service-account` and `--service-account-project-number` for `gcloud access-context-manager cloud-bindings` commands in the GA track.

### Cloud Bigtable

* Added support for `--tags` flag to `gcloud bigtable instances create` to allow binding tags on instance creation.

### Cloud Data Lineage

* Added `gcloud datalineage processes` command group to manage data lineage processes.

### Cloud Dataproc

* Added `--master-machine-types` flag in `gcloud dataproc clusters create`.

### Cloud IAM

* Updated `gcloud iam service-accounts create` to print the created service account's email address.

### Cloud Run

* Made the `FILE` positional argument optional for all `gcloud run * replace` commands, defaulting to their respective standard filenames if not specified.
* Promoted regional inference to beta for Cloud Run services, jobs, and worker
  pools. When `--region` or the `run/region` property is not specified, the
  command line looks for a resource with that name in all regions.
* Added `--sandbox-launcher` flag to `gcloud beta run deploy` and
  `gcloud beta run services update` to allow setting a container as sandbox
  launcher.
* Promoted `--workdir` flag for `gcloud run` commands to GA.
* Promoted interactive project prompt when project is not specified in `gcloud run deploy` to GA.
* Promoted suggesting project and region from Artifact Registry URL in `gcloud run deploy` to GA.
* Added `--tail` flag to `gcloud beta run jobs execute` to tail logs
  of the running execution.
* Added `--dry-run` flag to `gcloud beta run deploy`,
  `gcloud beta run services update`, `gcloud beta run services delete`,
  `gcloud beta run worker-pools deploy`, `gcloud beta run worker-pools update`,
  and `gcloud beta run worker-pools delete` to validate configuration without
  persisting changes.
* Added `gcloud run jobs executions describe-latest` command to describe the latest execution of a job.
* Call out proxy when deploying or updating services with `gcloud run deploy` or `gcloud run services update` that require authentication in all tracks.

### Cloud SQL

* Added `--user` and `--password-secret-version` to `gcloud sql instances execute-sql`.

### Cloud Storage

* Added download validation via MD5 hash and checksumming for streaming downloads in `gcloud storage cp`, `gcloud storage mv` and `gcloud storage cat` commands, see <https://docs.cloud.google.com/storage/docs/streaming-downloads>.
* Updated `gcloud storage cp` command to support streaming uploads with objects in RAPID storage see <https://docs.cloud.google.com/storage/docs/streaming-uploads>.
* Updated `gcloud storage cp` and `gcloud storage mv` commands to support streaming downloads with objects in RAPID storage see <https://docs.cloud.google.com/storage/docs/streaming-downloads>.
* Updated `gcloud storage cat` to support Rapid Bucket see <https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket>.

### Cloud Workstations

* Promoted `--pd-disk-size` flag of `gcloud workstations update` to GA.

### Cluster Director

* Users must supply a staticNodeCount if they want one. This no longer defaults
  to 1.

### Compute Engine

* Added `gcloud alpha compute instance-groups managed configure-accelerator-topologies` command to configure accelerator topologies of a managed instance group.
* Added `gcloud compute instances set-machine-resources` command to allow setting machine resources for a virtual machine instances in alpha, beta, and GA.
* Added `test-iam-permissions` command to `gcloud compute storage-pools` to return permissions that a caller has on the specified storage pool.
* Added `gcloud compute reservations sub-blocks set-iam-policy` command to beta and GA release tracks.
* Added `gcloud compute reservations blocks set-iam-policy` command to set IAM policy on a reservation block in beta, preview, and GA.
* Promoted support for `gcloud compute instance-groups managed resize-requests create` for regional MIG to GA.
* Promoted support for `gcloud compute instance-groups managed resize-requests cancel` for regional MIG to GA.
* Promoted support for `gcloud compute instance-groups managed resize-requests delete` for regional MIG to GA.
* Promoted support for `gcloud compute instance-groups managed resize-requests describe` for regional MIG to GA.
* Promoted support for `gcloud compute instance-groups managed resize-requests list` for regional MIG to GA.
* Added `gcloud compute instance-templates test-iam-permissions` command to test IAM permissions on an instance template in alpha, beta, GA, and preview.
* Added `gcloud compute target-https-proxies set-quic-override` command in beta, preview, and GA.
* Added `gcloud compute reservations test-iam-permissions` to test IAM permissions on Compute Engine reservations.
* Added `gcloud compute network-attachments set-iam-policy` command to set IAM policy on a network attachment in alpha, beta, preview, and GA.
* Added `gcloud compute instances list-referrers` command to alpha, beta, and GA
  release tracks.
* Added `gcloud compute reservations blocks test-iam-permissions` command to test IAM permissions on a reservation block in beta.
* Added `gcloud compute interconnects attachments groups test-iam-permissions` command to test IAM permissions on an interconnect attachment group in beta, preview, and GA.
* Added support for displaying dynamic fields (such as `TERMINATION_TIMESTAMP`) to `gcloud compute instance-groups managed list-instances` in GA.

### Database Migration

* Added `--source-database-name-override` flag to
  `gcloud database-migration conversion-workspaces seed|update` to allow
  overriding the database name for the seed operation.

### GKE Hub

* Promoted `gcloud container fleet rollouts` to GA.
* Promoted `gcloud container fleet rolloutsequences` to GA.

### Kpt

* Updated kpt to v1.0.0-beta.64. See <https://github.com/kptdev/kpt/releases/tag/v1.0.0-beta.64> for more details.

### Kubernetes Engine

* Promoted GKE custom image flags (`--image` and `--image-project`)
  to GA, making them publicly visible in
  `gcloud container clusters create`,
  `gcloud container clusters create-auto`, and
  `gcloud container node-pools create` (and `--image`/`--image-project`
  in `gcloud container clusters upgrade`).
* Added `stack-type` option to `--additional-node-network` flag of
  `gcloud container node-pools create` to configure the stack type
  (`ipv4`, `ipv4-ipv6`, or `ipv6`) for additional network interfaces.

### Network Management

* Added `--source-cloud-run-job` flag to `gcloud network-management connectivity-tests`.

### Network Services

* Updated `gcloud edge-cache services` import schemas to support specifying up to 100 allowed origins in `CORSPolicy.allowOrigins` and a client TTL of `0s` in `CDNPolicy.clientTtl`.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
