# Config Connector

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
