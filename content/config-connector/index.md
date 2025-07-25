# Config Connector

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
