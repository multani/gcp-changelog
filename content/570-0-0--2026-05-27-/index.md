# 570.0.0 (2026-05-27)

## 2026-05-27

### Google Cloud CLI

* Rebuilt Windows bundled Python for the `gcloud` CLI with cryptography 46.0.7 and pyOpenSSL 26.0.0.
* Updated Linux bundled Python for the `gcloud` CLI to 3.14.5.
* Updated the `gcloud` CLI authentication caching logic to natively store and refresh Regional Access Boundary (RAB) data.
* Reverted Windows PuTTY executables to version 0.81 due to a breakage.

### AlloyDB

* Added flag `--labels` to `gcloud beta alloydb instances create|create-secondary` commands assign labels to an instance.
* Added flags `--update-labels`, `--remove-labels`, and `--clear-labels` to `gcloud beta alloydb instances update` commands to update, remove, or clear labels for an instance.

### Beyondcorp

* Enabled IAM conditions support for `add-iam-policy-binding` and
  `remove-iam-policy-binding` commands under
  `gcloud beyondcorp security-gateways` and
  `gcloud beyondcorp security-gateways applications`.
  Added sample values for conditions in command help text.

### BigLake

* Promoted `gcloud biglake hive catalogs` to beta.
* Promoted `gcloud biglake hive databases` to beta.
* Promoted federated unity catalog flags of `gcloud biglake iceberg catalogs` to beta.
* Promoted `--primary-location` flag of `gcloud biglake iceberg catalogs` to GA.

### BigQuery

* Remove `--alpha=reservation_groups` in `bq mk`, `show`, `ls` and `rm --reservation_group` operations.
* Added support for table identifiers in the form of
  `project.catalog.namespace.table`.
* Added support for dataset identifiers in the form of `catalog.namespace`.
* Added support for showing and removing row access policies using the `bq show` and `bq rm` commands.
* Fixed 'NoneType' error handling and short assignment ID parsing in `bq mk --reservation_assignment` when `reservation_id` is not specified.
* Added support for specifying a reservation assignment name in `bq mk --reservation_assignment`.
* Added support for `principal` field for the `bq mk`, `bq ls`, and `bq show` commands with the flag `--reservation_assignment`.
* Removed the frozen dependency on an old version of `absl`.

### Cloud Alerting

* Fixing List Alerts `gcloud` CLI example commands.

### Cloud Backup DR

* Added `--use-project-service-account` flag for `gcloud backup-dr backups restore compute` and `gcloud backup-dr backups restore disk`.

### Cloud Dataplex

* Added `--all-schema-fields` flag to `gcloud dataplex context lookup` to include all schema fields in the context.

### Cloud Key Management Service

* Added `--project` flag to `gcloud kms autokey-config describe` to support project-level Autokey configurations.
* Updated `gcloud kms autokey-config update` to support project-level Autokey configurations.
* Updated `gcloud kms autokey-config update` to support the `key-project-resolution-mode` field.

### Cloud Run

* Added interactive prompt instead of erroring out when project is not specified in `gcloud beta run deploy`.
* Added support for suggesting project and region from Artifact Registry URL in `gcloud beta run deploy`.
* Added `--[no]--ssh` flag to `gcloud beta run deploy` and `gcloud beta run services update` to enable or disable SSH access to the Cloud Run service's container instances.
* Added `--domain` flag to `gcloud beta run deploy` to create domain mappings on the fly during service deployment.

### Cloud Spanner

* Add `--labels` flag to `gcloud spanner instances create` command to support
  specifying labels during instance creation.
* Add `--update-labels`, `--clear-labels` and `--remove-labels` flags to
  `gcloud spanner instances update` command to support updating labels.

### Cloud Storage

* Added `--enable-ingest-on-write` flag to
  `gcloud storage buckets anywhere-caches update` to support enabling cache
  ingest on write, and enabled rendering of the parsed property in the
  `anywhere-caches describe` command output.
* Added `--enable-ingest-on-write` flag to
  `gcloud storage buckets anywhere-caches create` to support enabling cache ingest
  on write.

### Cloud Workstations

* Added `--disk-archive-timeout` flag to `gcloud workstations configs create` and `gcloud workstations configs update` commands.
* Added `--workstation-authorization-url` and `--workstation-launch-url` flags to `gcloud workstations clusters create` command.
* Added `--workstation-authorization-url` and `--workstation-launch-url` flags to `gcloud workstations clusters update` command.

### Cluster Director

* Added support for updating Slurm prolog, epilog, task prolog, and task epilog scripts.

### Compute Engine

* Added `centos/rhel/rocky 10`, `debian 13`, `ubuntu 24.04/25.10` to allowed list of values for `osShortName` and `osVersion` of `gcloud compute instances ops-agents policies [create|update]`.
* Promoted the `--location` flag of `gcloud compute interconnects update` to beta.
* Promoted `--post-quantum-key-exchange` flag on `gcloud compute ssl-policies create` and `gcloud compute ssl-policies update` to GA.
* Promoted `gcloud compute advice capacity` to `beta`.
* Promoted `gcloud compute advice capacity-history` to `beta`.
* Promoted `--resource-manager-tags` flag for `gcloud compute commitments create` to beta and GA.
* Added `--stabilization-period` flag to
  `gcloud compute instance-groups managed <set-autoscaling|update-autoscaling>`
  to configure autoscaler load stabilization period before scale-in decisions.
* Added `--minimal-action` flag to `gcloud compute instances update`.
* Promoted `cachePolicy` support for `gcloud compute url-maps` to beta.
* Promoted `--resolve-subnet-mask` flag for `gcloud compute networks subnets create` to GA.
* Added `--resource-manager-tags` flag to `gcloud compute instant-snapshots create` in beta and GA.
* Added `--remove-obsolete-endpoint-accept-reject-entries` flag to
  `gcloud beta compute service-attachments update` to remove entries for
  Private Service Connect endpoints that are no longer connected.
* Promoted `--resource-manager-tags` flag for `gcloud compute external-vpn-gateways create` to beta.
* Promoted `--resource-manager-tags` flag for `gcloud compute target-vpn-gateways create` to beta.
* Promoted `--resource-manager-tags` flag for `gcloud compute vpn-gateways create` to beta.
* Promoted `--resource-manager-tags` flag for `gcloud compute vpn-tunnels create` to beta.
* Added `--instance-flexibility-policy` flag for `gcloud compute instance-groups managed create` and `gcloud compute instance-groups managed update` commands in beta.
* Added `CHIP_ERROR` as a valid value for `--fault-reasons` in `gcloud compute instances report-host-as-faulty` in alpha, beta, and GA.
* Promoted `--target-service` flag for `gcloud compute service-attachments update` to GA.
* Added `--resource-manager-tags` flag to `gcloud compute images create` in beta and GA.
* Promoted `--network-ddos-adaptive-protection`,
  `--network-ddos-impacted-baseline-threshold`, and
  `--clear-network-ddos-impacted-baseline-threshold` flags for
  `gcloud compute security-policies update` to beta.
* Added `--resource-manager-tags` flag to `gcloud compute disks create` in beta and GA.
* Added `--resource-manager-tags` flag to `gcloud compute snapshots create` in beta and GA.
* Promoted `--view` flag of `gcloud compute forwarding-rules describe` to GA.
* Promoted `gcloud compute org-rollouts cancel` to beta.
* Promoted `gcloud compute org-rollouts delete` to beta.
* Promoted `gcloud compute org-rollouts describe` to beta.
* Promoted `gcloud compute org-rollouts list` to beta.
* Promoted `gcloud compute org-rollout-plans create` to beta.
* Promoted `gcloud compute org-rollout-plans delete` to beta.
* Promoted `gcloud compute org-rollout-plans describe` to beta.
* Promoted `gcloud compute org-rollout-plans list` to beta.
* Removed validation on empty folder share list on `gcloud compute reservations create`.
* Promoted `--secondary-ipv6-range` flag on
  `gcloud compute networks subnets create`, and `--add-secondary-ipv6-range` and
  `--remove-secondary-ipv6-range` flags on
  `gcloud compute networks subnets update` to beta.
* Promoted `--ipv6-aliases` flag to `gcloud compute instances create`, `gcloud compute instances network-interfaces [add|update]`, and `gcloud compute instance-templates create` in beta.
* Added `--network-tier` flag to `gcloud compute public-advertised-prefixes create` in alpha.

### Kubernetes Engine

* Promoted `--enable-agent-sandbox` flag to GA for `gcloud container clusters create`, `gcloud container clusters create-auto`, and `gcloud container clusters update`.

### Network Connectivity

* Promoted `gcloud network-connectivity spokes gateways` command group to GA, including `create` and `update` commands.
* Added support for `HYBRID_INSPECTION` preset topology to `gcloud network-connectivity hubs create` in GA.

### Network Management

* Added `gcloud network-management network-monitoring-providers` command
  group which manages the enablement state of the Network Insights service.
* Added `gcloud network-management network-monitoring-providers
  monitoring-points` command group which manages agents within a network or
  application infrastructure that send probes.
* Added `gcloud network-management network-monitoring-providers
  network-paths` command group which manages the hop-by-hop route and active
  network delivery quality between a monitoring point and a target
  destination.
* Added `gcloud network-management network-monitoring-providers
  web-paths` command group which manages monitored web applications or URLs.

### Network Security

* Promoted `gcloud network-security secure-access-connect` command group
  to GA, including `attachments` and `realms` commands.
* Restricted Symantec integration and localization arguments (such as
  `--symantec-site` and `--country`) to `ALPHA` and `BETA` tracks only.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
