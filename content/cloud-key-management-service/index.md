# Cloud Key Management Service

## 2026-02-11

### Feature

Cloud KMS Autokey for projects is available in Public Preview. Autokey for
projects lets you enable Cloud KMS Autokey for delegated key management. In
delegated key management, keys created by Autokey are created in the same
project as the resources they protect. This option is suitable for your
organization if project administrators are in charge of key management for the
projects they manage.

You can still use Cloud KMS Autokey for centralized key management in a folder,
where all keys that protect resources in that folder are created in a dedicated
key project. You can also use centralized key management in a folder, with
certain projects within that folder configured to use delegated key management
and same-project keys instead of creating keys in the dedicated key project.

You can enable Autokey for projects on individual projects or on all projects
within a folder. For more information, see
[Enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey).

---
## 2026-01-20

### Feature

Cloud KMS is available in the following region:

* `asia-southeast3`

For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

---
## 2025-12-17

### Feature

Single-tenant Cloud HSM is now generally available. With
Single-tenant Cloud HSM, you can create and manage dedicated single-tenant
instances. Each instance is a cluster of partitions on HSMs in a single
Cloud KMS region. Google manages the HSMs, but you have administrative
control over your instance.

Single-tenant Cloud HSM is available in the following locations:

* `us-central1`
* `us-east4`
* `europe-west1`
* `europe-west4`

Creating a managing an instance requires quorum approval with two-factor
authentication using keys that you create and secure outside of
Google Cloud. Single-tenant Cloud HSM instances incur additional costs.

For more information about Single-tenant Cloud HSM, see
[Single-tenant Cloud HSM](https://docs.cloud.google.com/kms/docs/single-tenant-hsm). To learn how to
create and maintain a Single-tenant Cloud HSM instance, see [Create and
manage a Single-tenant Cloud HSM
instance](https://docs.cloud.google.com/kms/docs/create-manage-single-tenant-hsm). To see pricing details for
Single-tenant Cloud HSM, see [Pricing for
Single-tenant Cloud HSM](https://docs.cloud.google.com/kms/pricing#single-tenant).

---
## 2025-11-13

### Feature

The Cloud KMS **Encryption metrics** dashboard is available in Preview. The
dashboard shows the following metrics for the selected project to help you
understand your CMEK usage:

* Resources in this project by protection type
* Alignment to key usage recommended practices
* Resource protection type by service

To learn more about the **Encryption metrics** dashboard, including its
limitations, see [View encryption metrics](https://docs.cloud.google.com/kms/docs/view-encryption-metrics).

---
## 2025-09-23

### Feature

Cloud KMS now supports key encapsulation mechanisms (KEMs) for sharing secrets in Preview. KEMs are designed to be resistant to post-quantum attacks. You can use the following KEM algorithms:

* `ML_KEM_768`
* `ML_KEM_1024`
* `KEM_XWING`

For more information about key encapsulation mechanisms, see [Key encapsulation mechanisms](https://cloud.google.com/kms/docs/key-encapsulation-mechanisms). To learn how to use key encapsulation mechanisms to share secrets, see [Encapsulate and decapsulate using KEMs](https://cloud.google.com/kms/docs/encapsulate-decapsulate).

---
## 2025-06-30

### Feature

Cloud HSM for Google Workspace now lets you use Cloud HSM keys for client-side encryption (CSE) to protect sensitive workloads in Google Workspace. For more information about Cloud HSM for Google Workspace, including how to get started, see [Onboard to Cloud HSM for Google Workspace](https://cloud.google.com/kms/docs/onboard-hsm-workspace).

---
