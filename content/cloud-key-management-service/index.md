# Cloud Key Management Service

## 2026-08-24

### Feature

Cloud KMS supports deleting key rings in General Availability.

For more information about deleting Cloud KMS resources, see [Delete Cloud KMS
resources](https://docs.cloud.google.com/kms/docs/delete-kms-resources).

---
## 2026-08-06

### Feature

**Preview:** Cloud KMS supports quantum-safe key import. You can use the
following quantum-safe import methods:

* `HPKE_KEM_XWING_HKDF_SHA256_AES_256_GCM`
* `HPKE_KEM_ML_KEM_768_HKDF_SHA256_AES_256_GCM`
* `HPKE_KEM_ML_KEM_1024_HKDF_SHA256_AES_256_GCM`

For more information about quantum-safe key import, see [Quantum-safe key
import](https://docs.cloud.google.com/kms/docs/quantum-safe-key-import).

---
## 2026-07-29

### Feature

Cloud KMS Autokey with same-project key storage (formerly known as Autokey for
delegated key management) is generally available. Autokey with same-project key
storage can be used on its own or alongside Autokey with dedicated-project key
storage (formerly known as Autokey for centralized key management).

For more information, see [Enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey).
To learn how to set guardrails to constrain how Autokey is used in your
organization, see [Control Autokey usage](https://docs.cloud.google.com/kms/docs/control-autokey-usage).

---
## 2026-07-16

### Feature

Cloud KMS supports the following post-quantum computing (PQC) signing algorithms
in General Availability:

* `PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256`
* `PQ_SIGN_ML_DSA_44`
* `PQ_SIGN_ML_DSA_44_EXTERNAL_MU`
* `PQ_SIGN_ML_DSA_65`
* `PQ_SIGN_ML_DSA_65_EXTERNAL_MU`
* `PQ_SIGN_ML_DSA_87`
* `PQ_SIGN_ML_DSA_87_EXTERNAL_MU`
* `PQ_SIGN_SLH_DSA_SHA2_128S`

For more information about supported algorithms, see [PQC signing
algorithms](https://docs.cloud.google.com/kms/docs/algorithms#pqc_signing_algorithms). For more information
about PQC signing, see [Post-quantum cryptography (PQC) digital
signature](https://docs.cloud.google.com/kms/docs/digital-signatures#pqc).

---
## 2026-07-07

### Feature

The Cloud KMS overview dashboard **Asymmetric PQC insights** chart is generally
available. You can use the **Asymmetric PQC insights** chart and details view to identify how many and which of your asymmetric keys are susceptible to attacks
from future quantum computers. This information is an important input into your
quantum computing modernization planning and process.

For more information about the **Asymmetric PQC insights** chart, see [View
asymmetric post-quantum cryptography (PQC)
insights](https://docs.cloud.google.com/kms/docs/view-pqc-insights).

---
## 2026-05-14

### Feature

The Cloud KMS **Encryption metrics** dashboard and project-level key tracking
are generally available. You can use the **Encryption metrics** dashboard to
review summaries and details of your keys used in customer-managed encryption
key (CMEK) integrations and the resources that they protect. The **Encryption
metrics** dashboard and the key **Usage tracking** tab support both centralized
key management using a dedicated key project and delegated key management using
keys stored in the same projects as the resources that they protect.

For more information about the **Encryption metrics** dashboard, see [View
encryption metrics](https://docs.cloud.google.com/kms/docs/view-encryption-metrics). For more information
about project-level key tracking, see [View key
usage](https://docs.cloud.google.com/kms/docs/view-key-usage).

---
## 2026-03-02

### Feature

Cloud KMS deletion of keys and key versions is generally available. Keys and key
versions must meet deletion criteria before they can be deleted. Names of
deleted keys can't be reused.

For more information, including deletion criteria, see [Delete Cloud KMS
resources](https://docs.cloud.google.com/kms/docs/delete-kms-resources).

---
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
