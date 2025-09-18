# Cloud Service Mesh

## 2025-09-17

### Announcement

The following rollouts have completed for managed Cloud Service Mesh:

* 1.21.5-asm.55 has rolled out to the rapid release channel.
* 1.20.8-asm.48 has rolled out to the regular release channel.
* 1.19.10-asm.48 has rolled out to the stable release channel.

While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.

---
## 2025-09-10

### Announcement

1.26.4-asm.1 in-cluster Cloud Service Mesh already includes the fixes for these CVEs.

### Announcement

**1.25.4-asm.0 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.25.4-asm.0 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.25.4](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.4/) subject to the list of [supported features](https://cloud.google.com/service-mesh/v1.25/docs/supported-features-in-cluster). Cloud Service Mesh version 1.25.4-asm.0 uses envoy v1.33.8-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade).

### Announcement

**1.24.6-asm.12 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.24.6-asm.12 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.24.6](https://istio.io/latest/news/releases/1.24.x/announcing-1.24.6/) subject to the list of [supported features](https://cloud.google.com/service-mesh/v1.24/docs/supported-features-in-cluster). Cloud Service Mesh version 1.24.6-asm.12 uses envoy v1.33.8-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.24/docs/upgrade/upgrade).

### Fixed

These patches address the following CVEs:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CVE | Proxy | Control Plane | CNI | Distroless |
| [CVE-2025-32990](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-32990) | Yes | Yes | Yes | - |
| [CVE-2025-32988](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-32988) | Yes | Yes | Yes | - |
| [CVE-2025-40909](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-40909) | Yes | Yes | Yes | - |
| [CVE-2025-32989](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-32989) | Yes | Yes | Yes | - |
| [CVE-2025-47268](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-47268) | Yes | Yes | Yes | - |
| [CVE-2025-5702](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-5702) | Yes | Yes | Yes | - |
| [CVE-2025-6395](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-6395) | Yes | Yes | Yes | - |
| [CVE-2025-48964](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-48964) | Yes | Yes | Yes | - |

---
## 2025-09-09

### Security

The managed Cloud Service Mesh rollouts [previously announced](https://cloud.google.com/service-mesh/docs/release-notes#August_12_2025) address the following vulnerabilities. While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.

**1.21.5-asm.55**

| Name | Envoy Proxy | Envoy Proxy distroless | Control plane |
| --- | --- | --- | --- |
| [CVE-2025-32462](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32462) | Yes | - | - |
| [CVE-2025-4877](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4877) | Yes | - | - |
| [CVE-2025-3576](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-3576) | Yes | - | - |
| [CVE-2025-4802](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4802) | Yes | - | - |
| [CVE-2025-4878](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4878) | Yes | - | - |
| [CVE-2025-5318](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5318) | Yes | - | - |
| [CVE-2025-6020](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6020) | Yes | - | - |
| [CVE-2025-46836](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-46836) | Yes | - | - |
| [CVE-2025-4598](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4598) | Yes | - | - |
| [CVE-2024-56406](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-56406) | Yes | - | - |
| [CVE-2025-30258](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-30258) | Yes | - | - |
| [CVE-2025-5372](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5372) | Yes | - | - |
| [CVE-2025-1372](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-1372) | Yes | - | - |
| [CVE-2025-1377](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-1377) | Yes | - | - |
| [CVE-2023-4039](https://security-tracker.debian.org/tracker/CVE-2023-4039) | - | Yes | - |

**1.20.8-asm.48**

| Name | Envoy Proxy | Envoy Proxy distroless | Control plane |
| --- | --- | --- | --- |
| [CVE-2025-32462](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32462) | Yes | - | - |
| [CVE-2025-4877](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4877) | Yes | - | - |
| [CVE-2025-3576](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-3576) | Yes | - | - |
| [CVE-2025-4802](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4802) | Yes | - | - |
| [CVE-2025-4878](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4878) | Yes | - | - |
| [CVE-2025-5318](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5318) | Yes | - | - |
| [CVE-2025-6020](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6020) | Yes | - | - |
| [CVE-2025-46836](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-46836) | Yes | - | - |
| [CVE-2025-4598](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4598) | Yes | - | - |
| [CVE-2024-56406](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-56406) | Yes | - | - |
| [CVE-2025-30258](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-30258) | Yes | - | - |
| [CVE-2025-5372](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5372) | Yes | - | - |
| [CVE-2025-1372](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-1372) | Yes | - | - |
| [CVE-2025-1377](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-1377) | Yes | - | - |

**1.19.10-asm.48**

| Name | Envoy Proxy | Envoy Proxy distroless | Control plane |
| --- | --- | --- | --- |
| [CVE-2025-32462](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32462) | Yes | - | - |
| [CVE-2025-22872](https://github.com/advisories/GHSA-vvgc-356p-c3xw) | Yes | Yes | Yes |
| [CVE-2025-4877](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4877) | Yes | - | - |
| [CVE-2025-3576](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-3576) | Yes | - | - |
| [CVE-2025-4802](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4802) | Yes | - | - |
| [CVE-2025-4878](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4878) | Yes | - | - |
| [CVE-2025-5318](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5318) | Yes | - | - |
| [CVE-2025-6020](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6020) | Yes | - | - |
| [CVE-2025-46836](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-46836) | Yes | - | - |
| [CVE-2025-4598](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-4598) | Yes | - | - |
| [CVE-2024-56406](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-56406) | Yes | - | - |
| [CVE-2025-30258](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-30258) | Yes | - | - |
| [CVE-2025-5372](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-5372) | Yes | - | - |

---
## 2025-09-02

### Security

**1.26.4-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains a fix for a [use-after-free (UAF) vulnerability in the DNS cache](https://www.cve.org/CVERecord?id=CVE-2025-54588). For more information, see the [security bulletin](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-048).

Only clusters running in-cluster Cloud Service Mesh version 1.26 are affected. If you are running an earlier in-cluster version or managed Cloud Service Mesh, you are not affected and do not need to take any action.

For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade).

---
## 2025-08-12

### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

* 1.21.5-asm.55 is rolling out to the rapid release channel.
* 1.20.8-asm.48 is rolling out to the regular release channel.
* 1.19.10-asm.48 is rolling out to the stable release channel.

---
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
