# 592.0.0 (2026-11-03)

## 2026-11-03

### Breaking Changes

* **(Cloud Datastore Emulator)** Removed support for running the Datastore emulator
  (`gcloud beta emulators datastore start`) in environment with Java versions
  prior to 25. Users can upgrade to Java 25 or above to continue using the
  latest Datastore emulator. Alternatively, users can use previous `gcloud` CLI
  versions to continue using the Datastore emulator with Java 21 support.
* **(Cloud Firestore Emulator)** Removed support for running the Firestore emulator
  (`gcloud emulators firestore start`) in environment with Java versions prior
  to 25. Users can upgrade to Java 25 or above to continue using the latest
  Firestore emulator. Alternatively, users can use previous `gcloud` CLI
  versions to continue using the previous Firestore emulator with Java 21
  support.
* **(Docker)** Removed the system Python and C compiler from the Debian-based Docker images.
  gcloud, gsutil and bq now always run on the bundled Python, on both
  `linux/amd64` and `linux/arm64`. The removed packages differ by image:
  + `:latest`, `:slim`, `:debian_component_based`: `python3`, `python3-dev`,
    `python3-pip`, `python3-crcmod` and `gcc`.
  + `:emulators`: `python3` and `python3-crcmod`.
  + `:stable`: `python3-dev` and `python3-crcmod`, on `linux/arm64` only.
* **(Docker)** Setting `CLOUDSDK_PYTHON=python3` (or `CLOUDSDK_GSUTIL_PYTHON` /
  `CLOUDSDK_BQ_PYTHON`) in these images now makes every gcloud, gsutil or bq
  call fail, because there is no `python3` on `PATH`. Unset it to use the
  bundled Python.
* **(Docker)** If your workflow requires a system Python, install it on top of the image,
  for example with `apt-get install python3`. This does not change which
  Python gcloud uses. If you need to compile C extensions, also install
  `build-essential python3-dev`.

### Google Cloud CLI

* Changed the Java dependency of the `google-cloud-cli-datastore-emulator`,
  `google-cloud-cli-firestore-emulator`, `google-cloud-cli-pubsub-emulator`,
  `google-cloud-cli-app-engine-java`, and `google-cloud-cli-bqms` deb and rpm
  packages from a full JDK to a headless JRE, preferring Java 25. The Datastore
  and Firestore emulator packages now require Java 25 or later.

### Agent Registry

* Removed `--scanning-state` flag from `gcloud agent-registry skills create`
  and `gcloud agent-registry skills update`. Use `--scanning-policy` instead.

### AlloyDB

* Updated AlloyDB Auth Proxy installation instructions in `gcloud alloydb connect` to v1.17.2.
* Added `--connection-pooling-authproxy-pooler-scaling-type` flag to
  `gcloud beta alloydb instances create`,
  `gcloud beta alloydb instances create-secondary`, and
  `gcloud beta alloydb instances update`.
* Promoted the following flags to GA on `gcloud alloydb instances create` and
  `gcloud alloydb instances update`:
  + `--enable-autoscaler`
  + `--autoscaler-max-node-count`
  + `--autoscaler-cool-down-period-seconds`
  + `--autoscaler-target-cpu-usage`
  + `--autoscaler-set-schedule`
  + `--autoscaler-schedule-cron-exp`
  + `--autoscaler-schedule-duration-seconds`
  + `--autoscaler-schedule-time-zone`
  + `--autoscaler-schedule-min-node-count`
  + `--autoscaler-schedule-description`
* Promoted the following flags to GA on `gcloud alloydb instances update`:
  + `--autoscaler-delete-schedule`
  + `--autoscaler-disable-schedule`
  + `--autoscaler-enable-schedule`
* Added `--autoscaler-target-connections-count` flag to
  `gcloud alloydb instances create` and `gcloud alloydb instances update`.

### App Engine

* Updated the Java SDK to version 5.2.0 build from the open source project
  <https://github.com/GoogleCloudPlatform/appengine-java-standard/releases/tag/v5.2.0>.
* Added `--from-image` and `--destination-repository` flags to
  `gcloud beta app migrate-to-run` for App Engine Standard environment.
* Updated `gcloud beta app migrate-to-run --from-image` to show the reason
  returned by the App Engine Admin API when exporting the image fails.
* Added support for the `vpc_access` configuration in `app.yaml` to
  `gcloud app deploy`, enabling Direct VPC egress for App Engine standard
  environment.

### App Hub

* Added `MULTI_REGIONAL` choice to `--scope-type` flag of
  `gcloud apphub applications create`.

### Artifact Registry

* Fixed an issue in `gcloud artifacts attachments download` where attachment
  file names were not validated before writing to `--destination`.

### Beyondcorp

* Added `--dispatch-info-output-type` flag to
  `gcloud beyondcorp security-gateways create` and
  `gcloud beyondcorp security-gateways update`, and upstream
  `dispatchInfo` configuration to
  `gcloud beyondcorp security-gateways applications create` and
  `gcloud beyondcorp security-gateways applications update`
  to configure delegated dispatch info headers.
* Removed `gcloud beta beyondcorp app` and `gcloud beta beyondcorp
  client-connector` command groups.

### BigLake

* Added `--kms-key` flag to `gcloud beta biglake hive catalogs create`, and
  `--kms-key` and `--clear-kms-key` flags to
  `gcloud beta biglake hive catalogs update` to support customer-managed
  encryption keys (CMEK).
* Added `--workday-api-client-client-id` flag to
  `gcloud beta biglake iceberg catalogs create` and
  `gcloud beta biglake iceberg catalogs update` to support Workday OIDC
  authentication.

### Cloud Backup DR

* Removed default value (`-`) for `--location` flag in
  `gcloud beta backup-dr applied-auto-protection-policies list`. `--location`
  flag is now required.
* Promoted `gcloud backup-dr applied-auto-protection-policies` to GA.
* Fixed an issue where
  `gcloud backup-dr backup-plans update --backup-rules-from-file` failed with
  `update mask is required` when the file contained an empty `backup-rules`
  list.
* Fixed an issue where
  `gcloud backup-dr backup-plans update --backup-rules-from-file` cleared
  `--compute-instance-properties` and `--disk-properties` when they were
  specified in the same command.
* Promoted `gcloud backup-dr applied-auto-protection-policies` to GA.
* Promoted `gcloud backup-dr auto-protection-bindings` to GA.
* Promoted `gcloud backup-dr auto-protection-policies` commands to GA.
* Promoted `gcloud backup-dr binding-matching-resources` to GA.

### Cloud Bigtable

* Added `--automated-backup-keep-hot-duration` flag to
  `gcloud bigtable instances tables create`,
  `gcloud bigtable instances tables update`, `gcloud bigtable tables create`,
  and `gcloud bigtable tables update` to create hot automated backups that
  remain hot for the specified duration before transitioning to standard
  backups.
* Added `--clear-automated-backup-keep-hot-duration` flag to
  `gcloud bigtable instances tables update` and
  `gcloud bigtable tables update` to stop creating hot automated backups.
* Added `--avro-schema-path` flag to `gcloud bigtable schema-bundles create`
  and `gcloud bigtable schema-bundles update`.

### Cloud Dataplex

* Added `--custom-instructions` flag to
  `gcloud dataplex datascans create data-documentation` and
  `--custom-instructions` and `--clear-custom-instructions` flags to
  `gcloud dataplex datascans update data-documentation` to support specifying
  or clearing custom instructions that guide data documentation generation.
* Added `--sql-dialect` flag to
  `gcloud dataplex datascans create data-documentation` and
  `gcloud dataplex datascans update data-documentation` commands to specify
  the SQL dialect to use in generated SQL queries.

### Cloud Dataproc

* Added `--scheduling-timeout` and `--requested-run-duration` flags to `gcloud
  dataproc clusters create` for creating Dynamic Workload Scheduler (DWS)
  scheduled clusters.

### Cloud Datastream

* Fixed an issue where `gcloud datastream private-connections create` silently
  dropped user-supplied `--labels`.

### Cloud Firestore Emulator

* Release Cloud Firestore emulator v1.23.0
  + Added support for Datastore merge join and multiple inequality index
    selection with `--require-indexes` in Datastore mode
  + Added support for the `add_window_fields` stage in the Firestore
    Pipelines API with the `sum`, `average`, `count`, `minimum`, `maximum`,
    `first`, `last`, `array_agg`, `array_agg_distinct`, and `rank` window
    functions
  + Allowed Enterprise data types for all database editions
  + Fixed transaction conflict detection for concurrent writes against
    transactional queries
  + Fixed `ArrayIndexOutOfBoundsException` on incomplete Firestore Rules
    permission traces
  + Populated accurate `MoreResultsType` for Datastore mode queries and
    fixed Pipeline DML edge cases
  + Updated minimum required Java JRE version to 25

### Cloud Infrastructure Manager

* Updated `gcloud infra-manager deployments apply` to display a warning when
  `--tf-version-constraint` or the deployment configuration specifies a paid
  Terraform version (1.6.0 or later).

### Cloud Key Management Service

* Added support for ECDH key encapsulation mechanism algorithms:
  `kem-ecdh-p256` and `kem-ecdh-p384`.

### Cloud Run

* Added `--public` flag for Cloud Run services, allowing users to make a
  service public by disabling invoker IAM checks and Identity-Aware Proxy
  (IAP). This flag is available in `gcloud beta run deploy`,
  `gcloud beta run services update`, and
  `gcloud beta run multi-region-services update`.

### Cloud SQL

* Added `gcloud sql instances reconcile-networking` to reconcile Private Service Connect (PSC) DNS networking configuration for a Cloud SQL instance.

### Cloud Shell

* Updated `gcloud cloud-shell scp` to support passwordless authentication over
  the Cloud Shell TCP tunnel.
* Updated `gcloud cloud-shell ssh` to skip uploading an SSH public key when
  connecting with passwordless authentication.

### Cloud Workstations

* Added `--direct-access-ports` flag to `gcloud beta workstations clusters create` command.
* Added `--direct-access-ports` flag to `gcloud beta workstations clusters update` command.

### Compute Engine

* Fixed an issue where `gcloud compute` commands omitted troubleshooting
  documentation links from operation error messages.
* Promoted `--reservation-subblock` flag of `gcloud compute hosts describe`,
  `gcloud compute hosts list`, `gcloud compute reservations hosts describe`,
  and `gcloud compute reservations hosts list` to GA and beta.

### Firebase Test Lab

* Deprecated `gcloud firebase test` command group. Firebase Test Lab is
  deprecated and will be fully shut down on September 30, 2027. To maintain
  your testing workflows, you can migrate to the Developer Device Platform on
  Google Cloud. See the Developer Device Platform Migration Guide
  (<https://docs.cloud.google.com/developer-device-platform/device-run/migrate>)
  and FAQ
  (<https://docs.cloud.google.com/developer-device-platform/troubleshooting>)
  for more details.

### Kubernetes Engine

* Added `--enable-dataplane-v2` flag to `gcloud container clusters update` to
  initiate GKE Dataplane V2 migration for clusters.
* Added `--datapath-provider` flag to `gcloud container node-pools update` to
  update the datapath provider for a node pool.
* Promoted `--enable-ambient-networking` flag to GA for `gcloud container
  clusters create`, `gcloud container clusters create-auto`, and `gcloud
  container clusters update`.

### Network Security

* Updated `SecurityProfile` and `SecurityProfileGroup` YAML schemas to
  support WildFire Analysis in beta and GA.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
