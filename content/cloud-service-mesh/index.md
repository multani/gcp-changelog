# Cloud Service Mesh

## 2026-02-09

### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

* 1.21.6-asm.10 is rolling out to the rapid release channel.
* 1.20.8-asm.63 is rolling out to the regular release channel.
* 1.19.10-asm.57 is rolling out to the stable release channel.

These patch releases contain the fixes for the following managed Cloud Service Mesh CVEs:

| CVE | Proxy | Control Plane | CNI | Distroless | Severity |
| --- | --- | --- | --- | --- | --- |
| [CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729) | Yes | Yes | - | Yes | High (7.5) |
| [CVE-2025-61727](https://pkg.go.dev/vuln/GO-2025-4175) | Yes | Yes | - | Yes | Medium (6.5) |
| [CVE-2024-41996](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-41996) | Yes | Yes | - | Yes | High (7.5) |
| [CVE-2025-9086](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-9086) | Yes | Yes | - | Yes | High (7.5) |
| [CVE-2021-46848](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2021-46848) | Yes | Yes | - | Yes | Critical (9.1) |
| [CVE-2025-13151](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-13151) | Yes | Yes | - | Yes | High (7.5) |
| [CVE-2025-68973](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-68973) | Yes | Yes | - | Yes | High (7.8) |

---
## 2026-01-20

### Announcement

**1.27.5-asm.0 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.27.5-asm.0 for in-cluster Cloud Service Mesh. It includes
the features of
[Istio 1.27.5](https://istio.io/latest/news/releases/1.27.x/announcing-1.27.5/)
subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.27/docs/supported-features-in-cluster).
Cloud Service Mesh version 1.27.5-asm.0 uses envoy v1.35.9-dev.

For details on upgrading Cloud Service Mesh, see
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade).

### Announcement

**1.28.2-asm.4 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.28.2-asm.4 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.28.0](https://istio.io/latest/news/releases/1.28.x/announcing-1.28/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster).

The following environment variables, fields, and annotations are not supported:

* `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`
* Additional attributes for `HTTPCookie` in the DestinationRule API
* `caCertCredentialName` field in ServerTLSSettings API
* Optional `NetworkPolicy` for Istiod deployment
* Disable shadow host suffix
* `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP`

Istio dual stack is not supported

Istio's experimental feature to enable lazy subset creation of envoy statistics
is not supported.

The `ENABLE_AUTO_SNI` flag is still supported to stay aligned with legacy
behavior.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.28.2-asm.4 uses Envoy v1.36.5-dev.

### Announcement

In-cluster Cloud Service Mesh 1.25 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions).

### Announcement

**1.26.8-asm.1 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.26.8-asm.1 for in-cluster Cloud Service Mesh. It includes
the features of
[Istio 1.26.8](https://istio.io/latest/news/releases/1.26.x/announcing-1.26.8/)
subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.26/docs/supported-features-in-cluster).
Cloud Service Mesh version 1.26.8-asm.1 uses envoy v1.34.11.

For details on upgrading Cloud Service Mesh, see
[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade).

---
## 2026-01-15

### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

* 1.21.6-asm.8 is rolling out to the rapid release channel.
* 1.20.8-asm.60 is rolling out to the regular release channel.
* 1.19.10-asm.55 is rolling out to the stable release channel.

These patch releases contain the fixes for the following managed Cloud Service Mesh CVEs:

| CVE | Proxy | Control Plane | CNI | Distroless |
| --- | --- | --- | --- | --- |
| [CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729) | Yes | Yes | - | Yes |
| [CVE-2025-61727](https://security-tracker.debian.org/tracker/CVE-2025-61727) | Yes | Yes | - | Yes |

---
## 2025-12-15

### Announcement

Regional Cloud Service Mesh is now available as a public preview feature. See
[Regional Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/regional-cloud-service-mesh)
for more information.

### Announcement

Regional Cloud Service Mesh is now available as a public preview feature. See
[Regional Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/regional-cloud-service-mesh)
for more information.

---
## 2025-12-04

### Announcement

Managed Cloud Service Mesh will start using proxy version
`csm_mesh_proxy.20251121c_RC00` for Gateway API on GKE clusters. This proxy
version maps closest to Envoy version 1.37. This change is rolling out to all
release channels and contains the fix for the managed Cloud Service Mesh
security vulnerability listed in [GCP-2025-073](/service-mesh/docs/security-bulletins#gcp-2025-073.

---
## 2025-12-03

### Security

The following images are now rolling out for managed Cloud Service Mesh:

* 1.21.6-asm.7 is rolling out to the rapid release channel.
* 1.20.8-asm.59 is rolling out to the regular release channel.
* 1.19.10-asm.54 is rolling out to the stable release channel.

These patch releases contain the fix for the managed Cloud Service Mesh security vulnerability listed in
[GCP-2025-073](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-073).

### Security

**1.27.4-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2025-073](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-073). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.27.4-asm.1 uses Envoy v1.35.7.

### Security

**1.25.6-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2025-073](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-073). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade). Cloud Service Mesh v1.25.6-asm.1 uses Envoy v1.33.13.

### Security

**1.26.7-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2025-073](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-073). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh v1.26.7-asm.1 uses Envoy v1.34.11.

---
## 2025-11-18

### Announcement

The following rollouts have completed for managed Cloud Service Mesh:

* 1.21.6-asm.4 has rolled out to the rapid release channel.
* 1.20.8-asm.56 has rolled out to the regular release channel.
* 1.19.10-asm.52 has rolled out to the stable release channel.
* CNI and MDPC version 1.20.8-asm.56 has rolled out to all release channels.

While the managed data plane automatically updates Envoy Proxies by restarting
workloads, you must manually restart any StatefulSets and Jobs.

---
## 2025-11-17

### Announcement

The following rollouts have completed for managed Cloud Service Mesh:

* 1.21.6-asm.4 has rolled out to the rapid release channel.
* 1.20.8-asm.56 has rolled out to the regular release channel.
* 1.19.10-asm.52 has rolled out to the stable release channel.
* CNI and MDPC version 1.20.8-asm.56 has rolled out to all release channels.

While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.

---
## 2025-10-28

### Security

**1.25.5-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2025-064](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-064). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade). Cloud Service Mesh v1.25.5-asm.9 uses Envoy v1.33.12.

### Security

**1.26.5-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2025-064](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-064). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh v1.26.5-asm.1 uses Envoy v1.34.10.

### Security

**1.27.2-asm.1 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2025-064](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2025-064). For details on upgrading Cloud Service Mesh, refer to [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh v1.27.2-asm.1 uses Envoy v1.35.6.

---
## 2025-10-27

### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

* 1.21.6-asm.4 is rolling out to the rapid release channel.
* 1.20.8-asm.56 is rolling out to the regular release channel.
* 1.19.10-asm.52 is rolling out to the stable release channel.

CNI/managed data plane controller version 1.20.8-asm.56 is rolling out to all release channels.

### Fixed

These patches contain fixes for the following CVEs:

**1.21.6-asm.4**

| Name | Envoy Proxy | Envoy Proxy Distroless | Control plane |
| --- | --- | --- | --- |
| [CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802) | - | Yes | - |
| [CVE-2025-8058](https://security-tracker.debian.org/tracker/CVE-2025-8058) | - | Yes | - |
| [CVE-2023-4039](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-4039) | Yes | - | - |
| [CVE-2024-10041](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-10041) | Yes | - | - |
| [CVE-2025-32988](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32988) | Yes | - | - |
| [CVE-2025-6395](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6395) | Yes | - | - |
| [CVE-2025-48964](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-48964) | Yes | - | - |
| [CVE-2025-32989](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32989) | Yes | - | - |
| [CVE-2025-47268](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-47268) | Yes | - | - |
| [CVE-2025-40909](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-40909) | Yes | - | - |
| [CVE-2025-32990](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32990) | Yes | - | - |

**1.20.8-asm.55**

| Name | Envoy Proxy | Envoy Proxy Distroless | Control plane |
| --- | --- | --- | --- |
| [CVE-2023-4813](https://security-tracker.debian.org/tracker/CVE-2023-4813) | - | Yes | - |
| [CVE-2025-8058](https://security-tracker.debian.org/tracker/CVE-2025-8058) | - | Yes | - |
| [CVE-2023-4806](https://security-tracker.debian.org/tracker/CVE-2023-4806) | - | Yes | - |
| [CVE-2025-32989](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32989) | Yes | - | - |
| [CVE-2025-32988](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32988) | Yes | - | - |
| [CVE-2025-48964](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-48964) | Yes | - | - |
| [CVE-2024-10041](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-10041) | Yes | - | - |
| [CVE-2025-40909](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-40909) | Yes | - | - |
| [CVE-2025-32990](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32990) | Yes | - | - |
| [CVE-2025-47268](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-47268) | Yes | - | - |
| [CVE-2025-6395](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6395) | Yes | - | - |
| [CVE-2023-4039](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-4039) | Yes | - | - |

**1.19.10-asm.52**

| Name | Envoy Proxy | Envoy Proxy Distroless | Control plane |
| --- | --- | --- | --- |
| [CVE-2023-4813](https://security-tracker.debian.org/tracker/CVE-2023-4813) | - | Yes | - |
| [CVE-2025-8058](https://security-tracker.debian.org/tracker/CVE-2025-8058) | - | Yes | - |
| [CVE-2023-4806](https://security-tracker.debian.org/tracker/CVE-2023-4806) | - | Yes | - |
| [CVE-2025-32989](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32989) | Yes | - | - |
| [CVE-2025-48964](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-48964) | Yes | - | - |
| [CVE-2024-10041](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-10041) | Yes | - | - |
| [CVE-2025-32988](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32988) | Yes | - | - |
| [CVE-2025-40909](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-40909) | Yes | - | - |
| [CVE-2025-32990](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-32990) | Yes | - | - |
| [CVE-2025-47268](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-47268) | Yes | - | - |
| [CVE-2025-6395](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-6395) | Yes | - | - |
| [CVE-2023-4039](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-4039) | Yes | - | - |

**CNI & MDPC**

| Name | CNI | MDPC |
| --- | --- | --- |
| [CVE-2024-56406](https://ubuntu.com/security/CVE-2024-56406) | Yes | Yes |
| [CVE-2025-1372](https://ubuntu.com/security/CVE-2025-1372) | Yes | Yes |
| [CVE-2025-46836](https://ubuntu.com/security/CVE-2025-46836) | Yes | Yes |
| [CVE-2025-30258](https://ubuntu.com/security/CVE-2025-30258) | Yes | Yes |
| [CVE-2023-4039](https://ubuntu.com/security/CVE-2023-4039) | Yes | Yes |
| [CVE-2025-4802](https://ubuntu.com/security/CVE-2025-4802) | Yes | Yes |
| [CVE-2025-1377](https://ubuntu.com/security/CVE-2025-1377) | Yes | Yes |
| [CVE-2025-4598](https://ubuntu.com/security/CVE-2025-4598) | Yes | Yes |
| [CVE-2025-3576](https://ubuntu.com/security/CVE-2025-3576) | Yes | Yes |

---
## 2025-10-16

### Announcement

The promotion of [1.21 to the Rapid release channel](https://cloud.google.com/service-mesh/docs/release-notes#May_06_2025) included upstream breaking changes to [ExternalName](https://istio.io/latest/news/releases/1.21.x/announcing-1.21/upgrade-notes/#externalname-support-changes) and [auto-sni](https://istio.io/latest/news/releases/1.21.x/announcing-1.21/upgrade-notes/#default-value-of-the-feature-flag-enable_auto_sni-to-true) when using the `ISTIOD` [implementation](https://cloud.google.com/service-mesh/docs/check-control-plane-implementation). After considering the impact on customers, we have decided to restore the previous behavior from 1.20 and earlier for managed Cloud Service Mesh clusters using the `ISTIOD` implementation to match Rapid clusters using the `TRAFFIC_DIRECTOR` implementation. These changes are rolling out to the Rapid release channel in version 1.21.5-asm.55 or later.

* If you are using an `ExternalName` service in the Rapid channel without a port description, the `ExternalName` service will not be translated into `Cluster` in the Envoy configuration. If the `ExternalName` service is a destination of `VirtualService` or `ExternalName` service is used with `REGISTRY_ONLY` mode, you must specify the port in the service like in 1.20 and earlier.
* If you have an external service multiplexing traffic based on SNI but the corresponding `DestinationRule` doesn't have an explicit SNI, you must [set SNI properly](https://cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-security#explicit_sni_setup).

---
## 2025-10-15

### Announcement

**1.25.5-asm.7 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.25.5-asm.7 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.25.5](https://istio.io/latest/news/releases/1.25.x/announcing-1.25.5/) subject to the list of [supported features](https://cloud.google.com/service-mesh/v1.25/docs/supported-features-in-cluster). Cloud Service Mesh version 1.25.5-asm.7 uses envoy v1.33.10-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/v1.25/docs/upgrade/upgrade).

### Fixed

1.25.5-asm.7 includes the fixes for the following CVEs:

| CVE | Proxy | Control Plane | CNI | Distroless |
| --- | --- | --- | --- | --- |
| [CVE-2025-6297](https://ubuntu.com/security/CVE-2025-6297) | Yes | Yes | Yes | - |
| [CVE-2024-10963](https://ubuntu.com/security/CVE-2024-10963) | Yes | Yes | Yes | - |
| [CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802) | - | - | - | Yes |
| [CVE-2025-8058](https://ubuntu.com/security/CVE-2025-8058) | Yes | Yes | Yes | Yes |

### Announcement

**1.26.4-asm.7 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.26.4-asm.7 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.26.4](https://istio.io/latest/news/releases/1.26.x/announcing-1.26.4/) subject to the list of [supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.26.4-asm.7 uses Envoy v1.34.8-dev.

### Fixed

1.26.4-asm.7 includes the fixes for the following CVEs:

| CVE | Proxy | Control Plane | CNI | Distroless |
| --- | --- | --- | --- | --- |
| [CVE-2024-10963](https://ubuntu.com/security/CVE-2024-10963) | Yes | Yes | Yes | - |
| [CVE-2025-8058](https://ubuntu.com/security/CVE-2025-8058) | Yes | Yes | Yes | Yes |
| [CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802) | - | - | - | Yes |

### Announcement

**1.27.1-asm.5 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.27.1-asm.5 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.27.1](https://istio.io/latest/news/releases/1.27.x/announcing-1.27/) subject to the list of [supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.27.1-asm.5 uses Envoy v1.35.4-dev.

### Fixed

1.27.1-asm.5 includes the fixes for the following CVEs:

| CVE | Proxy | Control Plane | CNI | Distroless |
| --- | --- | --- | --- | --- |
| [CVE-2025-6297](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-6297) | Yes | Yes | Yes | - |
| [CVE-2024-10963](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2024-10963) | Yes | Yes | Yes | - |
| [CVE-2025-9230](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-9230 ) | Yes | Yes | Yes | - |
| [CVE-2025-8058](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-8058) | Yes | Yes | Yes | Yes |
| [CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802 ) | - | - | - | Yes |

### Announcement

In-cluster Cloud Service Mesh 1.24 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions).

---
## 2025-09-30

### Feature

You can now configure traffic routing using [Cloud Service Mesh service routing APIs](https://cloud.google.com/service-mesh/docs/configure-cloud-service-mesh-for-cloud-run#service_to_service) between Cloud Run and Cloud Run, Google Kubernetes Engine, and Google Compute Engine services. (GA).

### Changed

Managed Cloud Service Mesh with a TD control plane in the Rapid release channel will start using proxy images with an [internal envoy version](https://cloud.google.com/service-mesh/docs/supported-features-managed#base_images).

All features supported by Managed (TD) control planes are supported by this proxy. To identify which proxy version is used in a cluster, see [Identify the proxy versions used in the cluster](https://cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-proxy#identify_the_proxy_version_used_in_the_cluster).

This release uses the version `csm_istio_proxy_20250611.00_p0`. More details about the proxy version can be found on the [Versions](https://cloud.google.com/service-mesh/versions) page.

---
## 2025-09-29

### Announcement

CNI/managed data plane controller version 1.23.6-asm.15 is rolling out to all release channels.

### Fixed

|  |  |  |
| --- | --- | --- |
| **CVE** | **CNI** | **MDP Controller** |
| [CVE-2025-4802](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-4802) | Yes | Yes |
| [CVE-2023-29383](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-29383) | Yes | Yes |
| [CVE-2024-56406](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2024-56406) | Yes | Yes |
| [CVE-2023-7008](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-7008) | Yes | Yes |
| [CVE-2025-1377](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-1377) | Yes | Yes |
| [CVE-2023-4039](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-4039) | Yes | Yes |
| [CVE-2025-46836](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-46836) | Yes | Yes |
| [CVE-2023-50495]( http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-50495) | Yes | Yes |
| [CVE-2025-4598](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-4598) | Yes | Yes |
| [CVE-2025-3576](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-3576) | Yes | Yes |
| [CVE-2025-30258](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-30258) | Yes | Yes |
| [CVE-2017-11164](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-11164) | Yes | Yes |
| [CVE-2022-41409](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2022-41409) | Yes | Yes |
| [CVE-2025-1372](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2025-1372) | Yes | Yes |
| [CVE-2022-27943]( http://people.ubuntu.com/~ubuntu-security/cve/CVE-2022-27943) | Yes | Yes |
| [CVE-2022-4899](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2022-4899) | Yes | Yes |
| [CVE-2023-34969](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-34969) | Yes | Yes |
| [CVE-2023-45918](http://people.ubuntu.com/~ubuntu-security/cve/CVE-2023-45918) | Yes | Yes |

---
## 2025-09-25

### Deprecated

Support for the following features will end on **March 17, 2027**:

* [GKE on AWS](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement)
* [GKE on Azure](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement)
* EKS Attached Clusters on AWS
* Azure Attached Clusters with AKS

Note that there are no changes to the other features of GKE attached clusters or Google Distributed Cloud (software only or air-gapped),

You must migrate to an alternative service mesh solution or an alternative Istio-based solution using your existing CSM configuration files by March 17, 2027.

---
## 2025-09-23

### Announcement

**1.27.1-asm.2 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.27.1-asm.2 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.27.1](https://istio.io/latest/news/releases/1.27.x/announcing-1.27/) subject to the list of [supported features](https://cloud.google.com/service-mesh/docs/supported-features-in-cluster).

The following environment variables and annotations are not supported:

* `ENVOY_STATUS_PORT_ENABLE_PROXY_PROTOCOL`
* `PILOT_DNS_CARES_UDP_MAX_QUERIES`
* `PILOT_IP_AUTOALLOCATE_IPV4_PREFIX` and `PILOT_IP_AUTOALLOCATE_IPV6_PREFIX`
* `sidecar.istio.io/bootstrapOverride`

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.27.1-asm.2 uses Envoy v 1.35.3-dev.

---
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
