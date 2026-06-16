# 573.0.0 (2026-06-16)

## 2026-06-16

### Breaking Changes

* **(Anthos Multi-Cloud)** Deprecated `gcloud container attached clusters get-credentials`.
  Use `gcloud container fleet memberships get-credentials` to get credentials
  for a running Attached cluster.

### Google Cloud CLI

* Updated Windows bundled Python for the `gcloud` CLI to 3.14.5.

### AI

* Added `gcloud ai tuning-jobs` command group to manage Vertex AI supervised fine-tuning jobs.

### App Engine

* Updated the Java SDK to version 5.0.4 build from the open source project
  <https://github.com/GoogleCloudPlatform/appengine-java-standard/releases/tag/v5.0.4>.
* fixed <https://github.com/GoogleCloudPlatform/appengine-java-standard/issues/506>.

### Artifact Registry

* Added `gcloud artifacts image-streaming-cache` command group to manage
  image streaming caches per region. This group includes `create`,
  `describe`, `delete`, and `list` commands.

### BigLake

* Promoted `--unity-service-principal-application-id` flag for `gcloud biglake iceberg catalogs create` and `update` to BETA, making it publicly visible.
* Promoted BigLake catalogs and arguments for `gcloud biglake iceberg catalogs` to GA.

### Cloud Data Lineage

* Added `gcloud datalineage` command group to manage Cloud Data Lineage resources.
* Added `gcloud datalineage config describe` and `gcloud datalineage config update` commands to manage Data Lineage configurations.

### Cloud Datastream

* Added support for Dataverse, Salesforce Marketing Cloud, and ServiceNow connection profiles to `gcloud datastream connection-profiles create` and `update` commands.
* Added support for Dataverse, Salesforce Marketing Cloud, and ServiceNow streams to `gcloud datastream streams create` and `update` commands.

### Cloud Run

* Promoted `--readiness_probe` in `gcloud run deploy` and `gcloud run services update` to GA.

### Cloud Services

* **API Keys**: Updated `gcloud services api-keys` `create` and `update`
  commands' `--api-target` flag to accept a colon-separated list of `methods`
  inline (e.g. `--api-target="service=foo,methods=m1:m2"`).

### Cloud Storage

* Promoted `gcloud storage batch-operations bucket-operations` commands to GA.

### Cluster Director

* Added support for creating clusters using blueprints in `gcloud beta cluster-director clusters create`.

### Compute Engine

* Promoted `--action-on-vm-failed-health-check` flag to GA for `gcloud compute instance-groups managed create` and `gcloud compute instance-groups managed update`.
* Fixed an issue where waiting for asynchronous operations would fail for certain global nested resources (like `cross-site-networks wire-groups`).
* Added `any-reservation-then-fail` choice to `--reservation-affinity` flag in
  beta for `gcloud compute instances create`,
  `gcloud compute instances bulk create`,
  `gcloud compute instance-templates create`,
  `gcloud compute instances create-with-container`, and
  `gcloud compute instance-templates create-with-container` commands.
* Promoted `--include-disks` and `--exclude-disks` flags for `gcloud compute machine-images create` to the BETA release track.

### Kubernetes Engine

* Added `--dataplane-optimization-mode` flag to `gcloud container clusters create` to select scalability mode for Dataplane V2.
* Deprecated None value of --release-channel flag from gcloud container clusters create and update command. Use RAPID, REGULAR, STABLE or EXTENDED instead.

### Network Connectivity

* Updated help text for `--region` flag in `gcloud network-connectivity transports create` to include supported regions list.

### Network Security

* Added `gcloud network-security operations` command group (`describe`, `wait`, `list`, `cancel`).
* Promoted project scoping for
  `gcloud network-security firewall-endpoints` commands
  (`create`, `delete`, `describe`, `list`, `update`) to GA.
* Promoted `gcloud network-security security-profiles wildfire-analysis`
  commands to BETA.
* Promoted
  `gcloud network-security firewall-endpoints wildfire-verdict-change-requests`
  commands to beta.
* Promoted WildFire-related flags in
  `gcloud network-security firewall-endpoints create` command to
  BETA.
* Promoted WildFire-related flags in
  `gcloud network-security firewall-endpoints update` command to
  BETA.

### Recaptcha

* Fixed an issue where `gcloud recaptcha keys create` ignored `--testing-score` when creating Android or iOS keys.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
