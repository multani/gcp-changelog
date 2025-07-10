# Cloud Service Mesh

## 2025-07-09

### Announcement

**1.25.3-asm.8 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.25.3-asm.8 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.25.3](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.3/) subject to the list of [supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.25.3-asm.8 uses envoy v1.33.4-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade).

### Announcement

**1.24.6-asm.4 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.24.6-asm.4 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.24.6](https://istio.io/latest/news/releases/1.24.x/announcing-1.24.6/) subject to the list of [supported features](https://cloud.google.com/service-mesh/v1.24/docs/supported-features-in-cluster). Cloud Service Mesh version 1.24.6-asm.4 uses envoy v1.32.7-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.24/docs/upgrade/upgrade).

### Changed

**1.23.6-asm.11 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.23.6-asm.11 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.23.6](https://istio.io/latest/news/releases/1.23.x/announcing-1.23.6/) subject to the list of [supported features](https://cloud.google.com/service-mesh/v1.23/docs/supported-features-in-cluster). Cloud Service Mesh version 1.23.6-asm.11 uses envoy v1.31.9-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.23/docs/upgrade/upgrade).

---
## 2025-06-09

### Feature

You can now enforce cluster-local traffic for an individual service, all services in a particular namespace, or globally for all services in the mesh. For more information, see [Keeping traffic in-cluster](https://cloud.google.com/service-mesh/docs/operate-and-maintain/multi-cluster#keeping_traffic_in-cluster).

---
## 2025-06-06

### Feature

[DNS Proxy feature](https://cloud.google.com/service-mesh/docs/operate-and-maintain/dns-proxy) is now available in the Rapid release channel. This feature requires sidecar version `1.21.5-asm.39` or later.

### Changed

This change affects clusters using both the `TRAFFIC_DIRECTOR` and `ISTIOD` control plane implementations.

When using Cloud Service Mesh with Istio APIs, configuring an [unsupported field](https://cloud.google.com/service-mesh/docs/onboarding/unsupported-istio-apis) or value in an Istio Custom Resources will be reflected as an error in the Mesh status API.

In some cases, the validation webhook will also reject unsupported API usage with an error message indicating the specific unsupported API. For more information, see [Common webhook error messages](https://cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-webhook#common_webhook_error_messages). You can mitigate these issues by amending the Istio Custom Resource to remove the specified unsupported API configuration.

### Feature

Isolation support to prevent cross-region overflow is now available as a preview feature for `TRAFFIC_DIRECTOR` implementations of Cloud Service Mesh. For more information, see [Isolation for Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/service-routing/isolation).

---
