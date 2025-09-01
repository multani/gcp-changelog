# Secret Manager

## 2025-09-01

### Feature

**Automatic secret rotation with the Secret Manager add-on for Google Kubernetes Engine (GKE)**: You can configure the Secret Manager add-on to automatically rotate secrets so that secrets updated in Secret Manager after initial pod deployment are automatically and periodically pushed to the pod. This feature is now Generally available (GA).

For more information, see [Configure automatic rotation of secrets](https://cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component#configure_automatic_rotation_of_secrets).

---
## 2025-07-09

### Feature

**Enhanced tagging capabilities for Secret Manager**: You can now add tags directly at the time of secret creation. This new feature lets you provide essential metadata for your resources and helps with better organization, cost tracking, and automated policy application from the time a secret is created. In addition to this, *tagging for regional secrets* is now fully supported, both during secret creation and for existing regional secrets. For more information, see the documentation on tags for [global secrets](https://cloud.google.com/secret-manager/docs/create-and-manage-tags) and [regional secrets](https://cloud.google.com/secret-manager/regional-secrets/create-manage-tags-regional-secrets).

**Soft-enforced rate limits for modifying secrets and secret versions**: We have introduced soft-enforced rate limits for the following operations in Secret Manager:

* `AddSecretVersion`
* `UpdateSecret`
* `EnableSecretVersion`
* `DisableSecretVersion`
* `DestroySecretVersion`

Soft enforcement lets us continue serving requests beyond the defined quota as long as our backend systems can comfortably handle the increased load. For details, see the [Quotas and limits](https://cloud.google.com/secret-manager/quotas) documentation.

---
## 2025-06-23

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [secretmanager/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)

#### [1.15.0](https://github.com/googleapis/google-cloud-go/compare/secretmanager/v1.14.7...secretmanager/v1.15.0) (2025-06-17)

##### Features

* **secretmanager:** Update secret manager protos for tags ([#12406](https://github.com/googleapis/google-cloud-go/issues/12406)) ([feb078b](https://github.com/googleapis/google-cloud-go/commit/feb078b04ab541dd3bdceb2ac1f24938bb0354a3))

---
