# 572.0.0 (2026-06-09)

## 2026-06-09

### Google Cloud CLI

* Updated macOS Python Virtualenv for the `gcloud` CLI to 3.14.5 with pyOpenSSL 26.0.0 and cryptography 46.0.7.

### AI

* Fixed `gcloud ai endpoints deploy-model` to honor `--machine-type` for Gemini on GDC connected deployments. Previously the flag was silently ignored.

### App Engine

* Updated the Java SDK to version 5.0.3 build from the open source project
  <https://github.com/GoogleCloudPlatform/appengine-java-standard/releases/tag/v5.0.3>.
* Fixed for <https://github.com/GoogleCloudPlatform/appengine-java-standard/issues/503>.

### App Lifecycle Manager

* Added validation to enforce required sub-fields within arguments for releases,
  unit-kinds, and unit-operations commands.

### Cloud Access Context Manager

* Modified `--group-key` flag of `gcloud access-context-manager cloud-bindings create` to be optional.

### Cloud IAM

* Remove deprecated from Extended Attributes parameters.
  Extended Attributes are marked as restricted.

### Cloud Workstations

* Added `gcloud beta workstations update` command to update a workstation's properties, such as its persistent directory disk size.

### Cluster Director

* Added support for updating Slurm prolog, epilog, task prolog, and task epilog scripts.

### Compute Engine

* Added `EXTERNAL_PASSTHROUGH` option to `--load-balancing-scheme` flag of `gcloud compute forwarding-rules` in beta.
* Promoted `--ip_addresses` flag of `gcloud compute forwarding-rules` to beta.
* Added `EXTERNAL_PASSTHROUGH` option to `--load-balancing-scheme` flag of `gcloud compute backend-services` in beta.
* Added folder share support to `gcloud compute reservations update`.
* Promoted `--ncc-gateway` flag to GA.

### Database Migration

* Added support for seeding a conversion workspace from a Cloud Storage bucket
  via `--gcs-path` flag in `gcloud database-migration conversion-workspaces
  seed`.
* Added `--dry-run` flag to `gcloud database-migration conversion-workspaces
  apply` to allow validation of apply process by applying the draft version to
  a copy of the destination database.
* Decoupled `--host` and `--port` requirements in `gcloud database-migration
  connection-profiles create postgresql` for destination connection profiles
  leveraging Cloud SQL or AlloyDB.

### Kubernetes Engine

* Added `--maintenance-window-duration` flag to `gcloud container clusters create` command as an alternative to `--maintenance-window-end`.
* Added `--maintenance-window-duration` flag to `gcloud container clusters update` command as an alternative to `--maintenance-window-end`.

### Network Connectivity

* Promoted `gcloud network-connectivity spokes gateways advertised-routes`
  command group to GA, including `create`, `delete`, `describe`, and `list`
  commands.

### Network Security

* Promoted project scoping for
  `gcloud network-security firewall-endpoints` commands
  (`create`, `delete`, `describe`, `list`, `update`) to GA.

### Security Command Center

* Added `external-exposure` service to the `SUPPORTED_SERVICES` list.

### Service Extensions

* Updated import and export schemas for `gcloud service-extensions authz-extensions`.

### Workbench

* Added `--image-family` flag to `gcloud workbench instances upgrade`.
* Added `NVIDIA_RTX6000` to `--accelerator-type` choices on `gcloud workbench instances create` and `update`.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
