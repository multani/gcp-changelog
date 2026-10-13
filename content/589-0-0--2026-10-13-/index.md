# 589.0.0 (2026-10-13)

## 2026-10-13

### Breaking Changes

* **(Google Cloud CLI)** Deprecated the `skaffold` component in Google Cloud CLI. The component will be removed from Google Cloud CLI releases after January 15, 2027. A portion of `gcloud components install skaffold` attempts now return an error. Please install Skaffold following the instructions at <https://skaffold.dev/docs/install/>.

### Google Cloud CLI

* Updated Linux and Windows bundled Python to install `cryptography` 46.0.7 from the official PyPI wheels instead of custom builds.
* Updated the Alpine-based Docker images (`:alpine`, `:VERSION-alpine`) to use a bundled Python and no longer include a system `python3`.
* Updated bundled Python to 3.14.8 on Linux and Windows, and in the Alpine-based Docker images. This updates the OpenSSL that Python uses for TLS to 3.5.9.

### AlloyDB

* Added `--enable-express` flag to `gcloud beta alloydb clusters create|update`.

### Apigee

* Promoted `gcloud apigee apis delete` to GA. The command deletes an API proxy
  and all of its revisions. Every command in `gcloud apigee apis` now serves
  GA.
* Fixed an issue where `gcloud apigee apis import --from-template` discarded a
  template's `endpoints` and `targets` whenever the template referenced a
  feature. A template that declared its own topology and used features only for
  policies compiled to a proxy with no `ProxyEndpoint`, and the import failed.
  A template's `endpoints` and `targets` now seed the proxy, and features are
  applied on top of them.

### App Engine

* Fixed an issue where `gcloud beta app migrate-to-run` dropped the Serverless
  VPC Access connector for deployed versions.
* Fixed an issue where `gcloud beta app migrate-to-run` mapped App Engine
  Flexible `instance_ip_mode` to Cloud Run ingress.
* Fixed an issue where `gcloud beta app migrate-to-run` did not route all
  egress through Direct VPC for internal-only App Engine Flexible apps.

### App Lifecycle Manager

* Hid the deprecated `gcloud beta saas-runtime` command group. Existing
  commands continue to work and print a deprecation warning. Use `gcloud beta
  app-lifecycle-manager` instead.

### Beyondcorp

* Deprecated `gcloud beta beyondcorp app` command group.

### BigLake

* Added `--service-directory-name` flag to `gcloud biglake delta-sharing catalogs update`.

### BigQuery

* Added support for Azure Data Lake Storage URIs (`abfs://` and `abfss://`) in
  inline external table definitions (`--external_table_definition`).
* Added `--dataplex_entry_group` flag to `bq mk --transfer_config` and
  `bq update --transfer_config` to allow integration with Dataplex Entry
  Groups.
* Added support to filter Transfer Configs by Dataplex Entry Group using
  `--filter="metadata_destination.dataplex_configuration:*"` for
  `bq ls --transfer_config`.

### Cloud Alerting

* Promoted `gcloud monitoring alerts` command group to GA.

### Cloud Composer

* Updated `gcloud composer environments storage dags export`,
  `gcloud composer environments storage data export`,
  `gcloud composer environments storage plugins export`,
  `gcloud beta composer environments storage dags export`,
  `gcloud beta composer environments storage data export`, and
  `gcloud beta composer environments storage plugins export` to skip, with a
  warning, objects that would be written outside of the local `--destination`
  directory.

### Cloud DNS

* Added `gcloud beta dns outbound-endpoints` command group.
* Added `--outbound-endpoints` flag to `gcloud beta dns managed-zones` and `gcloud beta dns policies`.

### Cloud Firestore

* Promoted `gcloud firestore change-streams` commands to GA.

### Cloud Storage

* Added server-side hash validation by default for resumable uploads in
  `gcloud storage cp`, `gcloud storage mv`, and `gcloud storage rsync`. To
  disable this behavior, run `gcloud config set
  storage/enable_server_side_hash_validation False`.

### Compute Engine

* Optimized `gcloud compute instance-groups managed list-instances` by
  passing `--limit` and `--page-size` to the backend API and terminating page
  fetching early when the limit is reached.
* Added `CMEK_ENCRYPTION` option to `--local-ssd-encryption-mode` flag of
  `gcloud beta compute instances create` to encrypt Local SSDs with
  customer-managed encryption keys.
* Fixed `gcloud beta compute disk-types list` returning no results when
  `--zones` or `--regions` is specified. Deprecated `NAME` positional
  argument and `--regexp` flag of this command. Use `--filter` instead.
* Promoted `loadBalancingScheme` value `EXTERNAL_PASSTHROUGH` to GA in import
  and export schemas for `gcloud compute backend-services`.
* Promoted `IPAddresses` and `loadBalancingScheme` value
  `EXTERNAL_PASSTHROUGH` to GA in import and export schemas for `gcloud
  compute forwarding-rules`.
* Promoted `gcloud compute advice capacity` to GA.
* Promoted `gcloud compute advice capacity-history` to GA.

### Database Migration

* Updated `--ssl-flags` flag documentation and parsing for `gcloud
  database-migration connection-profiles` commands to support custom
  delimiter syntax (`^DELIM^`) for values containing commas (e.g.
  `server_certificate_dn`).
* Added `--dbm-port` flag to
  `gcloud database-migration connection-profiles create sqlserver` and
  `gcloud database-migration connection-profiles update` commands to specify
  the Database Mirroring (DBM) port for SQL Server Distributed Availability
  Group (DAG) migrations.
* Added `--sqlserver-dag-source-ag` and `--sqlserver-dag-linked-server` flags
  to `gcloud database-migration migration-jobs create` and
  `gcloud database-migration migration-jobs update` commands to configure SQL
  Server Distributed Availability Group (DAG) migrations.

### Device Run

* Removed `gcloud beta device-run sessions submit xctest`. The command remains available in the alpha release track.

### GKE Hub

* Added `--prioritized` flag to `gcloud beta container fleet rolloutsequences
  upgrade` and `gcloud beta container hub rolloutsequences upgrade`.

### Kubernetes Engine

* Added `--wiz-sensor-api-key-secret-uri`, `--wiz-sensor-proxy-secret-uri`,
  and `--wiz-sensor-registry-secret-uri` flags to `gcloud container clusters
  create`, `create-auto`, and `update` commands to configure Wiz Sensor.

### Looker

* Fixed `gcloud looker instances update --linked-lsp-project-number` sending
  an empty update mask and failing.

### Oracle Database

* Added `update` command to the following `gcloud oracle-database` command
  groups to support adding, updating, removing, and clearing labels using
  `--update-labels`, `--remove-labels`, and `--clear-labels` flags:
  + `gcloud oracle-database cloud-exadata-infrastructures update`
  + `gcloud oracle-database cloud-vm-clusters update`
  + `gcloud oracle-database db-systems update`
  + `gcloud oracle-database exascale-db-storage-vaults update`
  + `gcloud oracle-database goldengate-connections update`
  + `gcloud oracle-database goldengate-connection-assignments update`
  + `gcloud oracle-database goldengate-deployments update`
  + `gcloud oracle-database odb-networks odb-subnets update`

### Workbench

* Fixed `--nic-type` flag choices in `gcloud workbench instances create` to
  use `VIRTIO_NET` instead of `VIRTIGO_NET`.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
