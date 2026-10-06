# 588.0.0 (2026-10-06)

## 2026-10-06

### Breaking Changes

* **(Cloud Managed Flink)** Removed the Managed Flink Client component (`managed-flink-client`) from the Google Cloud CLI.

### Agent Identity

* Added `gcloud alpha|beta agent-identity auth-providers authorizations get-iam-policy|set-iam-policy|add-iam-policy-binding|remove-iam-policy-binding|test-iam-permissions` commands.

### Anthos

* Updated anthos-cli with newer go version and library dependencies.

### Apigee

* Promoted `gcloud apigee apis import` to GA. The command imports an API proxy
  from a YAML template (`--from-template`) or from a proxy bundle ZIP
  (`--from-bundle`).
* Fixed an issue where `gcloud apigee apis import --from-template` emitted an
  `EventFlow` inside the generic `<Flows>` container, where Apigee treats it as
  an ordinary conditional flow instead of running it on each streamed event.
  `EventFlow` is now emitted as a top-level element carrying a `content-type`
  attribute, which defaults to `text/event-stream`, and is preserved when
  importing a bundle.
* Fixed an issue where `gcloud apigee apis import --from-template` applied only
  part of a feature's `defaultEndpoint`. Its `routes` and `faultRules` were
  dropped, and a flow step contributed by two features was emitted twice, which
  made Apigee run the policy twice. Contributions are now merged, so a repeated
  step overrides instead of duplicating.
* Fixed an issue where `gcloud apigee apis import --from-template` ignored a
  feature's `defaultTarget`, so generated target endpoints were missing the
  `PostFlow`, `EventFlow` and `DefaultFaultRule` it declared. Features that
  attach to the outbound side of a proxy, such as analytics and failover, now
  apply to every target. This can make the generated API proxy an Extensible
  API proxy, which can't be deployed to a Base environment.
* Fixed an issue where `gcloud apigee apis import --from-template` prefixed a
  feature's policy and resource names even when the feature declared no `uid`.
  A feature with no `name` produced an empty prefix and names that collided
  with every other unnamed feature. Names are now prefixed only for features
  that declare a `uid`, and policies or resources contributed by more than one
  feature are merged instead of listed twice. This changes the policy names
  generated for features without a `uid`.
* Fixed an issue where `gcloud apigee apis import --from-template` combined a
  template's own `endpoints` and `targets` with the ones its features supply,
  which could leave some targets unreachable because no route referenced them.
  A template's `endpoints` and `targets` are now used only when it supplies no
  features, and a warning is logged when they are ignored.
* Fixed an issue where `gcloud apigee apis import --from-template` did not
  generate `apiproxy/resources/jsc/metadata.js`, so feature JavaScript that
  read the proxy's name, description or parameter defaults failed at runtime.
  The resource is now generated into the bundle and listed in `<Resources>`.
* Fixed an issue where `gcloud apigee apis import --from-template` emitted the
  children of a policy in alphabetical order rather than the order the template
  declared them, which is not valid for policies whose schema is
  sequence-typed. `<HTTPTargetConnection>` is now also emitted before the
  flows, regardless of how the target was declared.
* Fixed an issue where `gcloud apigee apis import --from-template` would
  incorrectly reject templates that populate the `displayName` field.
* Added `--service-account` flag to `gcloud beta apigee apis deploy` to give a
  deployed proxy permission to act as a service account.

### Apihub

* Added `--service-type-enum-values` and related flags to `gcloud apihub apis update`, allowing the service type of an API to be set. Valid values are `code`, `model`, `agent` and `skill`.

### BigLake

* Promoted `gcloud biglake hive catalogs` to GA.
* Promoted `gcloud biglake hive databases` to GA.
* Promoted `gcloud biglake hive tables` to GA.

### Certificate Authority Service

* Added `--key-algorithm` flag to `gcloud privateca certificates create` to
  allow specifying a custom public key algorithm when creating certificates
  with `--generate-key`.

### Cloud Bigtable

* Update go version and rebuild for CVE-2026-33818.

### Cloud Bigtable Emulator

* Update go version and rebuild for CVE-2026-33818.
* Micro-precision timestamp support.

### Cloud Dataplex

* Promoted `gcloud dataplex data-products` to GA.

### Cloud IAM

* Added `gcloud iam workforce-pools subjects revoke-sessions` command to
  revoke all sessions for a workforce pool subject.

### Cloud On Demand Scanning

* Migrate extraction library to osv-scalibr and enable dynamic linking support
  (2026-09).

### Cloud Resource Manager

* The `--recommend` flag of `gcloud beta projects delete` and
  `gcloud beta projects remove-iam-policy-binding` no longer has any effect; the
  change-risk recommendations it showed have been retired.

### Cloud SQL

* Added routing parameters to instance creation requests in Cloud SQL.
* Updated 'cloud-sql-proxy' packaged component to use 2.26.0 of the Cloud SQL Proxy.

### Cluster Director

* Added `networkTags` property to `--slurm-login-node` flag in `gcloud beta cluster-director clusters create`.

### Compute Engine

* Added support for reading a metadata value from standard input by
  specifying `-` as the file path in `--metadata-from-file` flag of
  `gcloud compute instances create`, `gcloud compute instances
  add-metadata`, `gcloud compute instance-templates create`, and `gcloud
  compute project-info add-metadata`.
* Froze development of the `alpha` and `beta` Compute Engine release tracks.
  Existing commands in these release tracks remain supported and functional.
  Most previous alpha and beta features have graduated to general availability
  in `gcloud compute`, and new Compute Engine preview features will launch in
  `gcloud preview compute` going forward.

### Compute OS Config

* Added `--description` flag to `gcloud compute os-config policy-orchestrators
  create` and `gcloud compute os-config policy-orchestrators update`.

### Database Migration

* Added `--ssl-flags` flag to `gcloud database-migration connection-profiles
  create postgresql` and `update` commands to configure SSL connection flags.
* Added `--asm-host`, `--asm-port`, `--asm-user`, `--asm-password`, and
  `--asm-service-name` flags to `gcloud database-migration connection-profiles
  create oracle` command to configure Oracle Automatic Storage Management
  (ASM).
* Added `--machine-type` flag to
  `gcloud database-migration connection-profiles create alloydb` command to
  configure the primary instance machine type.

### Identity and Access Management

* The `--recommend` flag of `gcloud beta iam service-accounts delete` no longer
  has any effect; the change-risk recommendations it showed have been retired.

### Kubernetes Engine

* Updated default kubectl from 1.35.8 to 1.35.9.
* Additional kubectl versions:
  + 1.31.14
  + 1.32.13
  + 1.33.13
  + 1.34.12
  + 1.35.9
  + 1.36.5
  + 1.37.1

### Looker

* Added regional endpoint support for `gcloud looker`.

### Network Management

* Updated examples of `gcloud network-management connectivity-tests`.

### Network Security

* Added command `gcloud beta network-security server-tls-policies create`.
* Added command `gcloud beta network-security server-tls-policies update`.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
