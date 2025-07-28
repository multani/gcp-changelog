# Cloud Service Mesh

## 2025-07-25

### Feature

[Advanced load balancing](https://cloud.google.com/service-mesh/docs/operate-and-maintain/advanced-load-balancing-istio) for managed Cloud Service Mesh (TD) now generally available (GA).

---
## 2025-07-21

### Changed

Managed Cloud Service Mesh will start using proxy version `csm_mesh_proxy.20250623b_RC00` for Gateway API on GKE clusters. This proxy version maps closest to Envoy version 1.35. This change is rolling out to all release channels.

---
## 2025-07-16

### Announcement

**1.26.0-asm.11 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.26.0-asm.11 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.26.0](https://istio.io/latest/news/releases/1.26.x/announcing-1.26/) subject to the list of [supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster).

The following environment variables and annotations are not supported:

* `ENABLE_GATEWAY_API_MANUAL_DEPLOYMENT`
* `RETRY_IGNORE_PREVIOUS_HOSTS`
* `ENABLE_CLUSTER_TRUST_BUNDLE_API`
* `OMIT_EMPTY_VALUES`
* `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`
* `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP` with the value 1
* Referencing ConfigMaps in a DestinationRule with TLS mode set to SIMPLE mode is not supported

The `ENABLE_AUTO_SNI` flag is still supported to stay aligned with the legacy behavior.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.26.0-asm.11 uses Envoy v1.34.2-dev.

### Announcement

In-cluster Cloud Service Mesh 1.23 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions).

### Announcement

**1.25.3-asm.11 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.25.3-asm.11 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.25.3](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.3/) subject to the list of [supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster). Cloud Service Mesh version 1.25.3-asm.11 uses envoy v1.33.4-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade).

### Announcement

**1.24.6-asm.9 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.24.6-asm.9 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.24.6](https://istio.io/latest/news/releases/1.24.x/announcing-1.24.6/) subject to the list of [supported features](https://cloud.google.com/service-mesh/v1.24/docs/supported-features-in-cluster). Cloud Service Mesh version 1.24.6-asm.9 uses envoy v1.32.7-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.24/docs/upgrade/upgrade).

---
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
