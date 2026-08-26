# 582.0.0 (2026-08-25)

## 2026-08-25

### Breaking Changes

* **(Google Cloud CLI)** Removed the legacy Cloud SQL Proxy V1 component ('cloud\_sql\_proxy') from the Google Cloud CLI. All connect commands now rely exclusively on Cloud SQL Auth Proxy V2 ('cloud-sql-proxy').
* **(API Registry)** Removed `gcloud api-registry mcp servers list` and `gcloud api-registry
  mcp tools list`. For similar functionality, see Agent Registry at
  `<https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/mcp-servers>`.
* **(Cloud Services)** Removed `gcloud beta services mcp policies get`, `gcloud beta services mcp
  policies get-effective`, and `gcloud beta services mcp policies test-enabled`
  as MCP policies are not required and they have been functioning as no-ops.

### Anthos

* Updated anthos-cli with newer go version and library dependencies.

### App Engine

* Updated the Java SDK to version 5.1.0 build from the open source project
  <https://github.com/GoogleCloudPlatform/appengine-java-standard/releases/tag/v5.1.0>.
* Upgraded Jetty 12.0 to 12.0.38 and Jetty 12.1 to 12.1.12.
* Added gRPC support to the App Engine Images service for image transformations and composition.

### App Lifecycle Manager

* Added `--flags` flag to `gcloud beta app-lifecycle-manager flags releases create` to allow creating flag releases from a list of flag IDs.

### Cloud Composer

* Enabled Airflow CLI commands for Composer environments running new Airflow 3.3.x versions.

### Cloud Firestore

* Added support for search shorthands to `gcloud beta firestore indexes composite create`.

### Cloud Key Management Service

* Added `--protection-level` and `--crypto-key-backend` flags to `gcloud kms keys versions update` command.

### Cloud Managed Kafka

* Released 'broker-disk' flags to GA.

### Cloud Run

* Promote `gcloud run instances` commands to the beta track.
* Added `--delay-execution` flag to `gcloud beta run jobs` command groups to
  allow run job execution within a delay window.
* Added `--run-upload` flag to `gcloud beta run deploy` to specify that the source should be uploaded via the Cloud Run UploadSource API.

### Cloud SQL

* Updated 'cloud-sql-proxy' packaged component to use 2.25.2 of the Cloud SQL
  Proxy.

### Cloud Spanner Emulator

* Added `--remote_functions_host_port` flag to Spanner emulator start command.
  This flag allows Spanner emulator to connect to a Functions Framework
  instance that hosts implementation of Remote User Defined Functions.

### Cloud Workstations

* Changed the default value of `--pool-size` flag for `gcloud workstations
  configs create` and `gcloud beta workstations configs create` to 1. To
  explicitly create a configuration without a fast start pool, run with
  `--pool-size=0`.

### Compute Engine

* Added `gcloud compute composite-health-checks test-iam-permissions` command to test IAM permissions on a Compute Engine composite health check in `alpha`, `beta`, and `GA`.
* Added `--security-settings-client-tls-policy`, `--security-settings-subject-alt-names`, and `--security-settings-aws-v4-*` flags to `gcloud compute backend-services create` and `update` commands.
* Added allowed value `asn` to flags `--enforce-on-key` and `--enforce-on-key-configs` to `gcloud compute security-policies rules create` and `update` commands in alpha, beta, and GA.
* Added `gcloud beta compute service-attachments test-iam-permissions` command to test IAM permissions on a service attachment.
* Added `--consistent-hash-http-header-name` flag to
  `gcloud compute backend-services create` and `update` commands.
* Added `BMSAI` support to `--confidential-compute-type` option in `gcloud compute instances create` and `bulk create` commands.
* Promoted identity support for Backend Services to GA.

### Design Center

* Added `gcloud design-center spaces application-templates export` command to export IaC for an application template.
* Added `gcloud design-center spaces application-templates revisions export` command to export IaC for an application template revision.

### Developer Connect

* Promoted `gcloud developer-connect account-connectors` commands to GA.

### Orchestration Pipelines

* Added `gcloud beta orchestration-pipelines` command group to manage Orchestration Pipelines.

### Vmware Engine

* Added `gcloud vmware private-clouds migrate-management-vms` which migrates the management VMs of a private cloud from the current management cluster to a workload cluster.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
