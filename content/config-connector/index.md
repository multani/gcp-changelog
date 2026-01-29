# Config Connector

## 2026-01-27

### Feature

[#6065](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/6065): Enabled Vertical Pod Autoscaler (VPA) support. You can enable VPA for Config Connector components via `ControllerResource` and `NamespacedControllerResource` to automatically adjust resource requests.

### Announcement

Config Connector version 1.134.4 is now available.

### Fixed

Bug Fixes:

* [#6035](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/6035): Fixed an issue where `managedFields` metadata could be incorrectly attributed to the `status` subresource during spec updates, causing "Location must be set" errors.

---
## 2026-01-23

### Feature

New Fields:

* `AlloyDBInstance`
  + Added `spec.connectionPoolConfig` field.
  + Added `status.connectionPoolConfig` field.

### Announcement

Config Connector version 1.143.0 is now available.

### Feature

New Beta Resources (Direct Reconciler):

* `ArtifactRegistryRepository`
* `LoggingLink`
* `MemorystoreInstance`
* `PrivateCACAPool`

### Feature

New Alpha Resources (Direct Reconciler):

* `ParameterManagerParameter`

### Feature

New Features:

* Set `GOMEMLIMIT` for KCC workloads to improve memory management and stability.

### Change

Reconciliation Improvements:

* `TagsTagBinding`

  + Added support for `organizations` in `parentRef`.
  + Added support for multiple targets in `parentRef`.
* Resource References (refs.Ref) support added for the following resources to improve reference resolution:

  + `BigQueryTable`
  + `BigQueryDataset`
  + `CloudRunService`
  + `CloudRunJob`
  + `ArtifactRegistryRepository`
  + `StorageBucket`

### Fixed

Bug Fixes:

* [Issue 6221](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/6221): `ComputeBackendService` can now correctly refer to `clientTLSPolicy`.
* [Issue 6156](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/6156): `BigQueryTable` now ignores `int64` to `int32` schema changes when configured.
* [Issue 6026](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/6026): Fixed identity parsing for `TagsTagValue`.

---
## 2026-01-09

### Change

Reconciliation Improvements:

Added support for direct reconciliation to more resources, with opt-in
behaviour. The API is unchanged. To use the direct reconciler, add the
`alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the corresponding
Config Connector object. The following resources now have direct reconciliation
support:

* `TagsLocationTagBinding`: Now supports direct reconciliation.

### Feature

New Features:

* IAM: Added support for `iam.cnrm.cloud.google.com/disable-dependent-services` annotation.
* Added support for Cilium cluster-wide network policy.

### Feature

New Fields:

* `AlloyDBInstance`
  + Added `spec.observabilityConfig` and `spec.queryInsightsConfig` fields.
* `ContainerNodePool`
  + Added `spec.nodeConfig.enableNestedVirtualization` field.
* `MonitoringDashboard`
  + Added support for `spec.charts[].dataSets[].timeSeriesQuery.opsAnalyticsQuery.sqlQueryRef`

### Fixed

Bug Fixes:

* `BatchJob`: Fixed a bug where the resource could not be created.
* `FirewallPolicyRule`: Fixed an issue with updating the resource.
* `IAMServiceAccountKey`: Fixed an issue causing unnecessary re-reconciliation.
* Fixed a bug where `ComputeBackendService` could not refer to `clientTLSPolicy` due to an invalid format.
* Fixed a bug where interconnect attachments were not ignored.
* Fixed a bug in the GitHub MCP server.
* Fixed a bug in the private cluster endpoint for `mockgcp`.

### Announcement

Config Connector version 1.142.0 is now available.

### Feature

New Beta Resources (Direct Reconciler):

* `AlloyDBBackup`
* `AccessContextManagerAccessLevel`

---
## 2025-12-19

### Announcement

Config Connector version 1.141.0 is now available.

### Feature

New Features:

* Enabled Vertical Pod Autoscaler (VPA) support for Config Connector controllers.
* Added `verticalPodAutoscalerMode` field to `ConfigConnector` and `ConfigConnectorContext` resources.

### Fixed

Bug Fixes:

* Fixed various issues in `observedState` handling for resources with reference fields.
* Fixed an issue where IAMPolicy and IAMPartialPolicy controllers would alphabetize the members field within the resource spec and write it back. This behavior can conflict with intent-based reconciliation from GitOps systems such as Config Sync, causing a loop of updates and potentially exhausting IAM read quotas.

### Feature

New Fields:

* RunJob

  + Added `spec.template.spec.containers[].port` field.
* DataplexTask

  + Replaced `project` with `projectRef`.
  + Replaced `serviceAccount` with `serviceAccountRef`.
  + Replaced `kmsKey` with `kmsKeyRef`.

---
## 2025-12-15

### Announcement

Config Connector version 1.140.2 is now available.

### Fixed

* Fixed a bug where the IAMPolicy and IAMPartialPolicy controllers would alphabetize the members field within the resource spec and write it back. This behavior can conflict with intent-based reconciliation from GitOps systems such as Config Sync, causing a loop of updates and potentially exhausting IAM read quotas. This issue affected versions 1.140.0 and has now been patched in version 1.140.2.

---
## 2025-12-04

### Announcement

Config Connector version 1.140.0 is now available.

### Change

New Alpha Resources (Direct Reconciler):

* `AssuredWorkloadsWorkload`
  + Manage Assured Workloads workloads to support compliance and security requirements.
* `ConfigDeliveryResourceBundle`
  + Manage Config Delivery resource bundles for Config Sync.

### Change

Reconciliation Improvements:

* Integrated Multi-Cluster Leader Election for improved reliability in multi-cluster setups.

### Feature

New Beta Resources (Direct Reconciler):

* `CertificateManagerCertificateIssuanceConfig`
  + Manage Certificate Manager certificate issuance configurations for automating certificate issuance.

### Feature

New Fields:

* `AlloyDBCluster`
  + Added `spec.restoreContinuousBackupSource` and `spec.restoreBackupSource` fields to support restoring from a backup.
* `BigQueryReservationAssignment`
  + Added `spec.jobType` field.
* `FirestoreDatabase`
  + Added `spec.deleteProtectionState` field.
* `FirestoreField`
  + Added `spec.ttlConfig` field.
* `RunJob`
  + Added `spec.template.template.containers.dependsOn` field.

### Fixed

* Fixed an issue where `BigQueryReservationAssignment` was not exposing `externalRef`.
* Fixed an issue with `CertificateManagerDNSAuthorization` API, Fuzzer and Mapper.
* Fixed an issue with `FirestoreDatabase` defaulting logic.

---
## 2025-11-20

### Announcement

Config Connector version 1.139.0 is now available.

### Change

Reconciliation Improvements:

* `IAM partial policy management`

### Feature

New Features:

* The controller type is now reported at the start and end of reconciliation.
* Mockgcp now supports `iap oauth brands` and `bigtable materializedview`.

### Fixed

* Reduced the memory footprint of the recorder.
* `SQLInstance`: Fixed an issue where empty `maintenanceVersion` patches were sent. The `settings` and `maintenanceVersion` fields are now unmanaged.
* `FirestoreDatabase`: Fixed boolean value exports.

### Change

New Alpha Resources (Direct Reconciler):

* `FirestoreField`

---
## 2025-11-14

### Announcement

Config Connector version 1.138.0 is now available.

### Feature

New Beta Resources (Direct Reconciler):

* `BackupDRBackupVault`
* `OrgPolicyCustomConstraint`

### Fixed

Bug Fixes:

* Fixed format validation issue in the `DataflowFlexTemplateJob` direct controller when the
  `spec.subnetworkRef.external` field contains full URL.
* Updated `status.observedGeneration` in `ConfigConnector` object.

### Feature

New Alpha Resources (Direct Reconciler):

* `FirestoreBackupSchedule`
* `FirestoreDocument`

### Changed

Reconciliation Improvements:

* Improved Normalization logic for `OrgPolicy`, `RunJob`, `TagsTagBinding`, and `VertexAIIndex` resources.

---
## 2025-10-16

### Announcement

Config Connector version 1.137.0 is now available.

### Feature

New Fields:

* `BigtableMaterializedView`: Added `spec.sourceTableRef` and `spec.definition`.
* `BackupDRBackupPlan`: Added `spec.backupConfig.retentionPeriodDays` and `spec.backupConfig.backupWindow`.
* `MemorystoreInstance`: Added support for `MEMCACHE` and `REDIS` instance types.

### Changed

Reconciliation Improvements:

* Enabled opt-in for IAM partial policy management.
* Enabled server-side apply for KMS resources.
* Improved reconciliation for `BigtableLogicalView` by using deep reflection.
* Improved reconciliation for `FirestoreDatabase` with identity pattern and export support.
* Improved reconciliation for `RunJob` with export support.
* Unified `ComputeTargetTCPProxy` direct API and controller.

### Fixed

Bug Fixes:

* Fixed an issue where `ComputeBackendService` backends were not sorted.
* Fixed an issue where `CloudFunctionsFunction` runtime was not a supported value.
* Fixed an issue with labels for `BackupDRBackupPlan`.
* Fixed an issue with labels for `RunJob`.
* Fixed a fuzzing issue for `FirestoreField`.
* Fixed an issue with `KMSCryptoKey` import.
* Fixed a flakiness issue in the `MonitoringDashboard` fuzzer.
* Fixed a flakiness issue in tests.
* Fixed an issue with bad labels in tests.
* Fixed an issue with `etag` in direct reconciliation.

### Changed

New Alpha Resources (Direct Reconciler):

* `BigtableMaterializedView`

### Changed

New Beta Resources (Direct Reconciler):

* `DocumentAIProcessorVersion`
* `EssentialContactsContact`
* `BigQueryBigLakeTable`
* `BackupDRBackupPlan`

---
## 2025-10-07

### Fixed

Bug Fixes:

* Added support for checking `etag` in spec for alpha resources.
* Fixed an issue where `CloudIdentityMembership` roles comparison would fail.
* Fixed a bug where the wrong GVK was reported in IAM controller.
* Fixed a bug where errors were swallowed when reading a Secret.
* Fixed an issue with LRO endTime in mockgcp.
* Fixed a bug in the `etag` mapper.
* Fixed a bug in the mapper generator for slice and single object map.
* Fixed a bug in the mapper generator for OneOf if the input is not proto.Message.
* Fixed an import for refs in the same package in `controllerbuilder`.

### Announcement

Config Connector version 1.136.1 is now available.

### Changed

New Beta Resources (Direct Reconciler):

* [`AssetFeed`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/asset/assetfeed)
* [`BigQueryReservationAssignment`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/bigqueryreservation/bigqueryreservationassignment)
* [`CloudDeployDeliveryPipeline`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/clouddeploy/clouddeploydeliverypipeline)
* [`ComposerEnvironment`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/composer/composerenvironment)

### Feature

New Fields:

* [`ComposerEnvironment`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/composer/composerenvironment)
  + Added `spec.storageConfig` field.
  + Added `spec.config.workloadsConfig.dagProcessor` field.
  + Added `spec.config.workloadsConfig.triggerer` field.
  + Added `spec.config.softwareConfig.webServerPluginsMode` field.
  + Added `spec.config.softwareConfig.cloudDataLineageIntegration` field.

### Changed

Reconciliation Improvements:

* Introduced [Stateful Reconciliation for Direct Controllers](https://github.com/GoogleCloudPlatform/k8s-config-connector/blob/master/docs/designs/stateful-reconciliation-with-cookie.md). With stateful reconciliation, the direct controller stores a hash of the last successfully applied `.spec` in the resource's `.status`. This provides a lightweight, GitOps-safe record when a user has modified the desired state of the resource.

---
## 2025-09-24

### Announcement

Config Connector version 1.134.1 is now available.

### Fixed

Bug Fixes:

* [#5230](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/5230): Fixed an issue that could lead to premature certificate rotation by ensuring errors are not swallowed when reading a Secret.
* [#5231](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/5231): Add more verbose logging during certificate validation to assist with debugging.

---
## 2025-09-22

### Announcement

Config Connector version 1.135.0 is now available.

### Changed

New Beta Resources (Direct Reconciler):

* `AssetSavedQuery`
* `PubSubSnapshot`

### Changed

Modified Beta Reconciliation:
We migrated the following resources from the Terraform-based or DCL-based controller to the new Direct Controller.

* `VMWareEngineExternalAddress`

### Feature

New Fields:

* `AlloyDBCluster`
  + Added `spec.databaseVersion` field

### Fixed

Bug Fixes:

* [PR#5009](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/5009)
  Fix the nil pointer dereference error in AlloyDB direct controller

---
## 2025-09-03

### Announcement

Config Connector version 1.134.0 is now available.

### Changed

Improved reconciliation by migrating the following resources from the Terraform-based or DCL-based controller to the new direct controller. These resources are migrated automatically and you no longer need to apply the `opt-in` annotation to enable the direct controller:

* [`CloudIdentityGroup`](https://cloud.google.com/config-connector/docs/reference/resource-docs/cloudidentity/cloudidentitygroup)
* [`CloudIdentityMembership`](https://cloud.google.com/config-connector/docs/reference/resource-docs/cloudidentity/cloudidentitymembership)

### Changed

New Fields:

* `ContainerCluster`: DNS endpoint is supported in ContainerCluster.

### Fixed

Bug Fixes:

* `ConfigConnectorContext`:
  + [PR#4995](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4995): `status.observedGeneration` is now being set on the ConfigConnectorContext.
  + [PR#4657](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4657): Added `spec.managerNamespace`.
* `SQLInstance`:
  + [PR#4838](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4838): Fixed bug in SQLInstance `maintenanceVersion` UPDATE operation
  + [PR#4843](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4843): Set status on acquisition for SQLInstance controller
  + [PR#4857](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4857): Support SQLInstance `maintenanceVersion` in CREATE operation

---
## 2025-07-30

### Announcement

Config Connector version 1.133.0 is now available.

### Feature

New Beta Resources (Direct Reconciler):

* [`APIGatewayAPI`](https://cloud.google.com/config-connector/docs/reference/docs/reference/resource-docs/apigateway/apigatewayapi.md)
* [`AppHubApplication`](https://cloud.google.com/config-connector/docs/reference/docs/reference/resource-docs/apphub/apphubapplication.md)
* `StorageAnywhereCache`

### Changed

New Alpha Resources (Direct Reconciler):

* `BigtableLogicalView`

### Changed

Reconciliation Improvements

Added support for direct reconciliation to more resources, with opt-in behaviour. The API is backward compatible. The following resources now have direct reconciliation support

* `BigQueryTable`
  + Use the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation on the `BigQueryTable` CR object to opt-in the direct controller.
  + The direct controller also supports adding BigQueryDataPolicies directly to BigQueryTable columns within `spec.schema`.

### Fixed

* [PR#4808](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4808)
  filtered out Kubernetes labels that are invalid for Google Cloud in the
  `ComputeForwardingRule` direct controller, ensuring backward compatibility
  after migrating to the direct controller.

---
## 2025-07-14

### Announcement

Config Connector version 1.132.1 is now available.

### Changed

Reconciliation Improvements:

* [SpannerInstance](https://cloud.google.com/config-connector/docs/reference/resource-docs/spanner/spannerinstance)
  + You can opt-in the direct controller by adding the
    `alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the
    `SpannerInstance` resource`.
  + Direct controller is opt-in if using the following fields:
    - `spec.labels`
    - `spec.defaultBackupScheduleType`
    - `spec.edition`
    - `spec.autoscalingConfig`

---
## 2025-06-10

### Announcement

Config Connector version 1.132.0 is now available.

### Feature

New Beta Resources (Direct Reconciler):

* [`SpeechCustomClass`](https://cloud.google.com/config-connector/docs/reference/resource-docs/speech/speechcustomclass)
* [`SpeechPhraseSet`](https://cloud.google.com/config-connector/docs/reference/resource-docs/speech/speechphraseset)
* [`SpeechRecognizer`](https://cloud.google.com/config-connector/docs/reference/resource-docs/speech/speechrecognizer)
* [`VertexAINotebooksInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/notebooks/notebookinstance)
* [`VertexAIMetadataStore`](https://cloud.google.com/config-connector/docs/reference/resource-docs/vertexai/vertexaimetadatastore)

### Changed

New Alpha Resources (Direct Reconciler):

* `OrgPolicyPolicy`
* `OrgPolicyCustomConstraint`
* `SpeechRecognizer`
* `StorageAnywhereCache`

### Feature

New Fields:

* [SpannerInstance](https://cloud.google.com/config-connector/docs/reference/resource-docs/spanner/spannerinstance)
  For opt-in direct controller,
  + Added `spec.labels` field.
  + Added `spec.defaultBackupScheduleType` field.
* [SecretManagerSecret](https://cloud.google.com/config-connector/docs/reference/resource-docs/secretmanager/secretmanagersecret)
  For opt-in direct controller,
  + Added `spec.labels` field.

---
