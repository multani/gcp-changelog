# Config Connector

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
