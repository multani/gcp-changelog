# Apigee APIM Operator

## 2025-10-16

### Announcement

On October 16, 2025, we released an updated version of Apigee (1-16-0-apigee-3).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Fixed

| Bug ID | Description |
| --- | --- |
| **442501403** | **Fixed an issue that caused incorrect target latency metrics in Apigee Analytics when a TargetEndpoint is configured with a <LoadBalancer>.** |
| **437999897** | **Reduced the log level for failed geo IP lookups to address excessive log messages for private IP addresses.** |
| **436323210** | **Fixed ingress cert keys to allow both `tls.key`/`key` and `tls.crt`/`cert`.** |
| **N/A** | **Updates to security infrastructure and libraries.** |

### Security

| Bug ID | Description |
| --- | --- |
| **440419558, 433759657** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:   * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868) * [CVE-2025-48924](https://nvd.nist.gov/vuln/detail/CVE-2025-48924) **Note**: This fix updates a Java library that is included in Apigee. Reliance on Java libraries that are included with Apigee is not supported. Those libraries are for Apigee product functionality only, and there's no guarantee that a library will be available from release to release. For more information, see [Restrictions](https://cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy#Restrictions). |

---
## 2025-10-14

### Deprecated

**Removal of deprecated Gemini Code Assist `@Apigee` tool.**

The Gemini Code Assist `@Apigee` tool is shut down as of October 14, 2025.

See [Gemini Code Assist @Apigee tool deprecation](https://cloud.google.com/apigee/docs/deprecations/apigee-tool) for information.

---
## 2025-10-09

### Deprecated

**Deprecation of the Gemini Code Assist `@Apigee` tool.**

The Gemini Code Assist `@Apigee` tool is deprecated and will be shut down as of October 14, 2025.

See [Gemini Code Assist @Apigee tool deprecation](https://cloud.google.com/apigee/docs/deprecations/apigee-tool) for information.

---
## 2025-10-07

### Breaking

**Previously unreported customer DNS misconfigurations now result in DNS errors**

Apigee removed the automatic DNS fallback functionality that was in 1-16-0-apigee-2. This removal surfaces customer DNS misconfigurations that previously did not show as DNS errors.

See [Known Issue 445936920](https://cloud.google.com/apigee/docs/release/known-issues#445936920).

---
## 2025-09-24

### Announcement

On September 24, 2025, we released an updated version of Apigee.

### Feature

**ApigeeBackendService for the Apigee Operator for Kubernetes (GA)**

The ApigeeBackendService resource for the Apigee Operator for Kubernetes is [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages).

This new resource enables the integration of the Apigee Operator for Kubernetes with the [Google Kubernetes Engine (GKE) Inference Gateway](https://cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway). The GKE Inference Gateway is an extension to the GKE Gateway that provides optimized routing and load balancing for serving generative Artificial Intelligence (AI) workloads. It simplifies the deployment, management, and observability of AI inference workloads.

With this new integration, GKE Inference Gateway users can now leverage Apigee's full suite of features to manage, govern and monetize their AI workload through APIs.

To learn more, see [Create an ApigeeBackendService](https://cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice).

---
## 2025-09-12

### Announcement

On September 12, 2025, we released an updated version of Apigee (1-16-0-apigee-2).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Security

| Bug ID | Description |
| --- | --- |
| **N/A** | **Security fix for `apigee-runtime`.** |

---
## 2025-09-11

### Changed

**API hub navigation update**

The **API hub** section is now moved to the top level of the Apigee left navigation menu. This change improves discoverability and access to the API hub features.

---
## 2025-09-09

### Announcement

On September 9, 2025, we released an updated version of Apigee (1-16-0-apigee-1).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Changed

| Bug ID | Description |
| --- | --- |
| **N/A** | **Updates to security infrastructure and libraries.** |

---
