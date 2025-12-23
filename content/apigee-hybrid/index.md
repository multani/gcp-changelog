# Apigee hybrid

## 2025-12-19

### Change

**UDCA component removed**

In Apigee hybrid v1.16, the Unified Data Collection Agent (UDCA) component has been removed. The responsibilities of sending analytics, trace, and deployment status data to the Apigee control plane are now handled using a [Google Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs) based data pipeline. Using the Pub/Sub based data pipeline has been the default data collection mechanism since [Apigee hybrid v1.14.0](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1140).

### Feature

**`apigee-guardrails` service account**

In v1.16.0, Apigee Hybrid introduces an `apigee-guardrails` Google IAM service account. This is used by the `apigee-operator` chart during initial installation to check that all needed APIs are enabled in your project.

**Note:** The `apigee-guardrails` service account is required for both upgraded and new installations. See [Upgrading to Apigee hybrid to version 1.16: Set up the `apigee-guardrails` service account](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/upgrade#set-up-the-apigee-guardrails-service-account) for upgrade instructions.

See:

* [Diagnosing issues with guardrails](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/guardrails)
* [About service accounts: `apigee-guardrails`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about#apigee-guardrails)
* [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/create-service-account)
* [Upgrading to Apigee hybrid to version 1.16](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/upgrade#changes-from-previous-version)
* [Installation Part 2: Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts)
* [Installation Part 2: Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication)

### Change

**Support for cert-manager release 1.18 and 1.19**

Apigee hybrid v1.16 supports cert-manager release 1.18 and 1.19.

**Note:** cert-manager release 1.18 introduces a change to the default certificate `Spec.PrivateKey.RotationPolicy` value that can impact traffic on upgraded Apigee hybrid installations. This does not affect new installations of Apigee Hybrid. See [Known issue 465834046](https://docs.cloud.google.com/apigee/docs/release/known-issues#465834046).

### Fixed

#### Fixed in this release

| Bug ID | Description |
| --- | --- |
| **448647917** | **Fixed a issue where non-SSL connections through a forward proxy could be improperly shared.** (also fixed in [Apigee 1-16-0-apigee-4](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_31_2025)) |
| **442501403** | **Fixed an issue that caused incorrect target latency metrics in Apigee Analytics when a TargetEndpoint is configured with a <LoadBalancer>.** (also fixed in [Apigee 1-16-0-apigee-3](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)) |
| **438192028** | **Updated the geolocation database to mitigate stale IP-to-location mappings.** (also fixed in [Apigee 1-16-0-apigee-3](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)) |
| **437999897** | **Reduced the log level for failed geo IP lookups to address excessive log messages for private IP addresses.** (also fixed in [Apigee 1-16-0-apigee-3](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)) |
| **436323210** | **Fixed ingress cert keys to allow both `tls.key`/`key` and `tls.crt`/`cert`.** |
| **N/A** | **Updates to security, infrastructure, and libraries.** (also fixed in [Apigee 1-16-0-apigee-4](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_31_2025)) |

### hybrid v1.16.0

On December 19, 2025 we released an updated version of the Apigee hybrid software, 1.16.0.

* For information on upgrading, see [Upgrading Apigee hybrid to version v1.16](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/upgrade).
* For information on new installations, see [The big picture](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/big-picture).

**Note:** This is a minor release: The container images used in minor releases are integrated with the Apigee hybrid Helm charts. Upgrading to a minor via the Helm chart automatically updates the images. No manual image changes are typically needed. For information on container image support in Apigee hybrid releases, see [Apigee release process](https://docs.cloud.google.com/apigee/docs/release/apigee-release-process#apigee-hybrid-container-images).

### Security

#### Fixed in this release

| Bug ID | Description |
| --- | --- |
| **452621774, 452381632, 441266643, 448498138** | **Security fix for Apigee infrastructure.** (also fixed in [Apigee 1-16-0-apigee-4](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_31_2025))  This addresses the following vulnerabilities:  * [CVE-2025-53864](https://nvd.nist.gov/vuln/detail/CVE-2025-53864) Updated Nimbus JWT library from 9.37.2 to 9.37.4, which introduced changes in behavior including changes to error string verbiage. * [CVE-2025-8916](https://nvd.nist.gov/vuln/detail/CVE-2025-8916) * [CVE-2025-5115](https://nvd.nist.gov/vuln/detail/CVE-2025-5115) * [CVE-2024-40094](https://nvd.nist.gov/vuln/detail/CVE-2024-40094) |
| **440419558, 433759657** | **Security fix for Apigee infrastructure.** (also fixed in [Apigee 1-16-0-apigee-3](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)) This addresses the following vulnerabilities:   * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868) * [CVE-2025-48924](https://nvd.nist.gov/vuln/detail/CVE-2025-48924) **Note**: This fix updates a Java library that is included in Apigee. Reliance on Java libraries that are included with Apigee is not supported. Those libraries are for Apigee product functionality only, and there's no guarantee that a library will be available from release to release. For more information, see [Restrictions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy#Restrictions). |
| **443902061** | **Security fix for Apigee infrastructure** (also fixed in [Apigee 1-16-0-apigee-3](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)) This addresses the following vulnerability:   * [CVE-2025-13292](https://nvd.nist.gov/vuln/detail/CVE-2025-13292) Fixed an issue with improper access control that resulted in cross-tenant analytics modification and access to log data. |
| **N/A** | **Security fixes for `apigee-asm-ingress`.**  This addresses the following vulnerabilities:  * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) |
| **N/A** | **Security fixes for `apigee-asm-istiod`.**  This addresses the following vulnerabilities:  * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) |
| **N/A** | **Security fixes for `apigee-connect-agent`.**  This addresses the following vulnerabilities:  * [CVE-2025-61725](https://nvd.nist.gov/vuln/detail/CVE-2025-61725) * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723) * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) * [CVE-2025-47907](https://nvd.nist.gov/vuln/detail/CVE-2025-47907) |
| **N/A** | **Security fixes for `apigee-fluent-bit`.**  This addresses the following vulnerability:  * [CVE-2025-9230](https://nvd.nist.gov/vuln/detail/CVE-2025-9230) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra`.**  This addresses the following vulnerabilities:  * [CVE-2025-61725](https://nvd.nist.gov/vuln/detail/CVE-2025-61725) * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723) * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) * [CVE-2025-47913](https://nvd.nist.gov/vuln/detail/CVE-2025-47913) * [CVE-2025-47907](https://nvd.nist.gov/vuln/detail/CVE-2025-47907) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra-client`.**  This addresses the following vulnerabilities:  * [CVE-2025-61725](https://nvd.nist.gov/vuln/detail/CVE-2025-61725) * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723) * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) * [CVE-2025-47907](https://nvd.nist.gov/vuln/detail/CVE-2025-47907) |
| **N/A** | **Security fixes for `apigee-kube-rbac-proxy`.**  This addresses the following vulnerabilities:  * [CVE-2025-61725](https://nvd.nist.gov/vuln/detail/CVE-2025-61725) * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723) * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) |
| **N/A** | **Security fixes for `apigee-mart-server`.**  This addresses the following vulnerabilities:  * [CVE-2025-53066](https://nvd.nist.gov/vuln/detail/CVE-2025-53066) * [CVE-2025-50106](https://nvd.nist.gov/vuln/detail/CVE-2025-50106) * [CVE-2025-50059](https://nvd.nist.gov/vuln/detail/CVE-2025-50059) * [CVE-2025-48913](https://nvd.nist.gov/vuln/detail/CVE-2025-48913) * [CVE-2025-30749](https://nvd.nist.gov/vuln/detail/CVE-2025-30749) * [CVE-2024-13009](https://nvd.nist.gov/vuln/detail/CVE-2024-13009) |
| **N/A** | **Security fixes for `apigee-open-telemetry-collector`.**  This addresses the following vulnerabilities:  * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723) * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) * [CVE-2025-29786](https://nvd.nist.gov/vuln/detail/CVE-2025-29786) |
| **N/A** | **Security fixes for `apigee-operators`.**  This addresses the following vulnerabilities:  * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723) * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) * [CVE-2025-61725](https://nvd.nist.gov/vuln/detail/CVE-2025-61725) |
| **N/A** | **Security fixes for `apigee-prom-prometheus`.**  This addresses the following vulnerabilities:  * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723) * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) * [CVE-2022-48174](https://nvd.nist.gov/vuln/detail/CVE-2022-48174) |
| **N/A** | **Security fixes for `apigee-prometheus-adapter`.**  This addresses the following vulnerabilities:  * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723) * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) |
| **N/A** | **Security fixes for `apigee-redis`.**  This addresses the following vulnerabilities:  * [CVE-2025-61725](https://nvd.nist.gov/vuln/detail/CVE-2025-61725) * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723) * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) * [CVE-2025-47907](https://nvd.nist.gov/vuln/detail/CVE-2025-47907) |
| **N/A** | **Security fixes for `apigee-runtime`.**  This addresses the following vulnerabilities:  * [CVE-2025-50106](https://nvd.nist.gov/vuln/detail/CVE-2025-50106) * [CVE-2025-50059](https://nvd.nist.gov/vuln/detail/CVE-2025-50059) * [CVE-2025-48913](https://nvd.nist.gov/vuln/detail/CVE-2025-48913) * [CVE-2025-30749](https://nvd.nist.gov/vuln/detail/CVE-2025-30749) |
| **N/A** | **Security fixes for `apigee-stackdriver-logging-agent`.**  This addresses the following vulnerability:  * [CVE-2025-24294](https://nvd.nist.gov/vuln/detail/CVE-2025-24294) |
| **N/A** | **Security fixes for `apigee-synchronizer`.**  This addresses the following vulnerabilities:  * [CVE-2025-50106](https://nvd.nist.gov/vuln/detail/CVE-2025-50106) * [CVE-2025-50059](https://nvd.nist.gov/vuln/detail/CVE-2025-50059) * [CVE-2025-48913](https://nvd.nist.gov/vuln/detail/CVE-2025-48913) * [CVE-2025-30749](https://nvd.nist.gov/vuln/detail/CVE-2025-30749) |
| **N/A** | **Security fixes for `apigee-udca`.**  This addresses the following vulnerabilities:  * [CVE-2025-61725](https://nvd.nist.gov/vuln/detail/CVE-2025-61725) * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723) * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) * [CVE-2025-47913](https://nvd.nist.gov/vuln/detail/CVE-2025-47913) |
| **N/A** | **Security fixes for `apigee-watcher`.**  This addresses the following vulnerabilities:  * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723) * [CVE-2025-58188](https://nvd.nist.gov/vuln/detail/CVE-2025-58188) * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187) |

### Feature

**Seccomp Profiles**

Apigee Hybrid now offers the capability to apply Seccomp Profiles to your runtime components, significantly enhancing the security posture of your deployment.

This feature allows Apigee administrators and security teams to restrict the system calls (syscalls) a containerized process can make to the host's kernel. By limiting a container to only the necessary syscalls, you can:

* Enhance Security: Mitigate the risk of container breakouts and privilege escalation.
* Enforce Least Privilege: Ensure components only have access to the exact system calls required for their operation.
* Meet Compliance: Provide a critical control for meeting stringent security compliance requirements.

Seccomp profiles are not enabled by default. To enable the feature, see [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).

### Security

#### Fixed since last minor release

| Bug ID | Description |
| --- | --- |
| **448498138** | **Security fixes for `apigee-runtime`.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151))  This addresses the following vulnerability:  * [CVE-2024-40094](https://nvd.nist.gov/vuln/detail/CVE-2024-40094) |
| **447367372** | **Security fixes for `apigee-runtime`.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151))  This addresses the following vulnerability:  * [CVE-2025-58057](https://nvd.nist.gov/vuln/detail/CVE-2025-58057) |
| **433952146** | **Security fix.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143))  This addresses the following vulnerability:  * [CVE-2024-6763](https://nvd.nist.gov/vuln/detail/CVE-2024-6763) |
| **433951774** | **Security fix.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143))  This addresses the following vulnerability:  * [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254) |
| **433950558** | **Security fix.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143))  This addresses the following vulnerability:  * [CVE-2024-47554](https://nvd.nist.gov/vuln/detail/CVE-2024-47554) |
| **433950370** | **Security fix.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143))  This addresses the following vulnerability:  * [CVE-2025-25193](https://nvd.nist.gov/vuln/detail/CVE-2025-25193) |
| **418557195** | **Security fixes for `apigee-fluent-bit`.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151))  This addresses the following vulnerabilities:  * [CVE-2025-24528](https://nvd.nist.gov/vuln/detail/CVE-2025-24528) * [CVE-2025-4207](https://nvd.nist.gov/vuln/detail/CVE-2025-4207) * [CVE-2025-1390](https://nvd.nist.gov/vuln/detail/CVE-2025-1390) * [CVE-2024-26462](https://nvd.nist.gov/vuln/detail/CVE-2024-26462) * [CVE-2024-13176](https://nvd.nist.gov/vuln/detail/CVE-2024-13176) |
| **396944778** | **Security fixes for `apigee-synchronizer`.** (Fixed in [v1.13.4](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1134))  This addresses the following vulnerabilities:  * [CVE-2025-25193](https://nvd.nist.gov/vuln/detail/CVE-2025-25193) * [CVE-2025-24970](https://nvd.nist.gov/vuln/detail/CVE-2025-24970) * [CVE-2025-23184](https://nvd.nist.gov/vuln/detail/CVE-2025-23184) * [CVE-2024-47554](https://nvd.nist.gov/vuln/detail/CVE-2024-47554) |
| **392934392** | **Security fixes for `apigee-logger`.** |
| **N/A** | **Incorporated an updated base image for `stackdriver-logging-agent`, improving the overall security of the service.** (Fixed in [1.14.2-hotfix.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_1142-hotfix1))  This addresses the following vulnerabilities (among others and not limited to):  * [CVE-2022-32221](https://nvd.nist.gov/vuln/detail/CVE-2022-32221) * [GHSA-jvgm-pfqv-887x](https://osv.dev/vulnerability/GHSA-jvgm-pfqv-887x) |
| **N/A** | **Security fixes for `apigee-asm-ingress`.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143))  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-asm-istiod`.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143))  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-envoy`.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143))  This addresses the following vulnerability:  * [CVE-2025-0395](https://nvd.nist.gov/vuln/detail/CVE-2025-0395) |
| **N/A** | **Security fixes for `apigee-fluent-bit`.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143) & [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151))  This addresses the following vulnerabilities:  * [CVE-2025-32990](https://nvd.nist.gov/vuln/detail/CVE-2025-32990) * [CVE-2025-32988](https://nvd.nist.gov/vuln/detail/CVE-2025-32988) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra-client`.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143))  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra`.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143))  This addresses the following vulnerabilities:  * [CVE-2025-23015](https://nvd.nist.gov/vuln/detail/CVE-2025-23015) * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) * [CVE-2025-24970](https://nvd.nist.gov/vuln/detail/CVE-2025-24970) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra`.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151))  This addresses the following vulnerability:  * [CVE-2025-23015](https://nvd.nist.gov/vuln/detail/CVE-2025-23015) |
| **N/A** | **Security fixes for `apigee-kube-rbac-proxy`.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143))  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-mart-server`.** (Fixed in [v1.13.4](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1134))  This addresses the following vulnerability:  * [CVE-2024-20952](https://nvd.nist.gov/vuln/detail/CVE-2024-20952) |
| **N/A** | **Security fixes for `apigee-mart-server`.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143))  This addresses the following vulnerabilities:  * [CVE-2025-48924](https://nvd.nist.gov/vuln/detail/CVE-2025-48924) * [CVE-2025-48795](https://nvd.nist.gov/vuln/detail/CVE-2025-48795) * [CVE-2025-48734](https://nvd.nist.gov/vuln/detail/CVE-2025-48734) * [CVE-2025-24970](https://nvd.nist.gov/vuln/detail/CVE-2025-24970) * [CVE-2024-47554](https://nvd.nist.gov/vuln/detail/CVE-2024-47554) * [CVE-2024-47535](https://nvd.nist.gov/vuln/detail/CVE-2024-47535) * [CVE-2024-13009](https://nvd.nist.gov/vuln/detail/CVE-2024-13009) * [CVE-2024-8184](https://nvd.nist.gov/vuln/detail/CVE-2024-8184) * [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254) * [CVE-2024-6763](https://nvd.nist.gov/vuln/detail/CVE-2024-6763) |

### Fixed

#### Fixed since last minor release

| Bug ID | Description |
| --- | --- |
| **451841788** | **Apigee hybrid required the `mintTaskScheduler.serviceAccountPath` property even when Monetization was not enabled.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) & [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143)) |
| **451375397** | **The `apigee-pull-push.sh` script could return a No such image error message.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) & [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143)) |
| **445912919** | **Unused files and folders have been removed from the Apigee hybrid Helm charts to prevent potential security exposure and streamline the product installation and upgrade process.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151)) |
| **442501403** | **Fixed an issue that caused incorrect target latency metrics in Apigee Analytics when a `TargetEndpoint` is configured with a `<LoadBalancer>`.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151)) |
| **437999897** | **Reduced the log level for failed geo IP lookups to address excessive log messages for private IP addresses.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151)) |
| **431930277**, **395272878** | **When the configuration property [`envs.managementCallsSkipProxy`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#envs-managementcallsskipproxy) is set to `true` via helm for environment-level forward proxy, trace and analytics (which use `googleapis.com`) will skip forward proxy.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151)) |
| **423597917** | **Post of an [`AppGroupAppKey`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys/updateAppGroupAppKey) scopes should result in insert operation instead of update.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) & [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143)) |
| **420675540** | **Fixed Cassandra based replication for runtime contracts in synchronizer.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151), [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143) & [v1.13.4](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1134)) |
| **419578402** | **Mint-Mart forward proxy compatible.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) & [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143)) |
| **416634326** | **Presence of istio.io Custom Resource Definitions (CRDs) in an Apigee hybrid cluster could cause failure in apigee-ingressgateway-manager pods.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151), [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143) & [v1.13.4](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1134)) |
| **414499328** | **`ApigeeTelemetry` could become stuck in `creating` state** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143) & [v1.13.4](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1134)) |
| **412740465** | **Fixed issue where zipkin headers were not generated by Apigee Ingress Gateway.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) & [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143)) |
| **409048431** | **Fixes a vulnerability which could allow a SAML signature verification to be bypassed.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) & [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143)) |
| **401746333** | **Fixed a `java.lang.ClassCircularityError` that could occur in Java Callouts due to an issue with the class loading mechanism.**(Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) & [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143)) |
| **395272878** | **Separate Forward proxy support for `googleapis.com` and `non-googleapis.com` runtime traffic.** (Fixed in [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143)) |
| **393615439** | **OASValidation behavior for `allOf` with `additionalProperties: true`.** (Fixed in [1.14.2-hotfix.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_1142-hotfix1)) |
| **382565315** | **A memory leak within the Security Policy has been addressed, improving system stability.** (Fixed in [v1.13.4](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1134)) |
| **378686709** | **The use of wildcards (\*) in Apigee proxy basepaths would conflict with other explicit basepaths, resulting in a 404 error.** To apply this fix, follow the procedure in [Known issue 378686709](https://docs.cloud.google.com/apigee/docs/release/known-issues#378686709). (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) & [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143)) |
| **375360455** | **Updated apigee-runtime drain timeout to 300s to fix connection termination issue during pod termination.** (Fixed in [v1.13.4](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1134)) |
| **367815792** | **Two new Flow Variables: `app_group_app` and `app_group_name` have been added to VerifyApiKey and Access Token policy.** (Fixed in [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) & [v1.14.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143)) |

---
## 2025-10-12

### hybrid v1.15.1

On October 10, 2025 we released an updated version of the Apigee hybrid software, 1.15.1.

* For information on upgrading, see [Upgrading Apigee hybrid to version 1.15](https://cloud.google.com/apigee/docs/hybrid/v1.15/upgrade).
* For information on new installations, see [The big picture](https://cloud.google.com/apigee/docs/hybrid/v1.15/big-picture).

**Note:** This is a patch release: The container images used in patch releases are integrated with the Apigee hybrid Helm charts. Upgrading to a patch via the Helm chart automatically updates the images. No manual image changes are typically needed. For information on container image support in Apigee hybrid releases, see [Apigee release process](https://cloud.google.com/apigee/docs/release/apigee-release-process#apigee-hybrid-container-images).

### Feature

**Recurring, top-up, and setup fees for Apigee hybrid monetization**

Apigee hybrid now supports recurring, top-up, and setup fees for monetization. For information see [Enabling monetization for Apigee hybrid](https://cloud.google.com/apigee/docs/hybrid/v1.15/monetization-for-hybrid).

### Feature

**Apigee policies for LLM/GenAI workloads**

Apigee hybrid now supports the following Apigee policies with support for LLM/GenAI workloads.

* [SemanticCacheLookup policy](https://cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy)
* [SemanticCachePopulate policy](https://cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy)
* [SanitizeUserPrompt](https://cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy)
* [SanitizeModelResponse](https://cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy)

The Apigee semantic caching policies enable intelligent response reuse based on semantic similarity. Using these policies in your Apigee API proxies can minimize redundant backend API calls, reduce latency, and lower operational costs. With this release, the semantic caching policies support URL templating, enabling the use of variables for AI model endpoint values.

The Model Armor policies protect your AI applications by sanitizing user prompts to and responses from large language models (LLMs). Using these policies in your Apigee API proxies can mitigate the risks associated with LLM usage by leveraging Model Armor to detect prompt injection, prevent jailbreak attacks, apply responsible AI filters, filter malicious URLs, and protect sensitive data.

**Note:** In Apigee hybrid, this feature has the following limitations:

* Support for these policies is limited to installations on Google Cloud Platform.
* Apigee hybrid does not support forward proxy with these policies.

For more information on using these policies in your Apigee API proxies, see:

* [Get started with semantic caching policies](https://cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies)
* [Get started with Apigee Model Armor policies](https://cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies)

### Fixed

| Bug ID | Description |
| --- | --- |
| **451841788** | **Apigee hybrid required the `mintTaskScheduler.serviceAccountPath` property even when Monetization was not enabled.** |
| **451375397** | **The `apigee-pull-push.sh` script could return a "No such image error" message.** |
| **445912919** | **Unused files and folders have been removed from the Apigee hybrid Helm charts to prevent potential security exposure and streamline the product installation and upgrade process.** |
| **442501403** | **Fixed an issue that caused incorrect target latency metrics in Apigee Analytics when a `TargetEndpoint` is configured with a `<LoadBalancer>`.** |
| **437999897** | **Reduced the log level for failed geo IP lookups to address excessive log messages for private IP addresses.** |
| **431930277**, **395272878** | **When the configuration property [`envs.managementCallsSkipProxy`](https://cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#envs-managementcallsskipproxy) is set to `true` via helm for environment-level forward proxy, trace and analytics (which use `googleapis.com`) will skip forward proxy.** |
| **423597917** | **Post of an [`AppGroupAppKey`](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys/updateAppGroupAppKey) scopes should result in insert operation instead of update.** |
| **420675540** | **Fixed Cassandra based replication for runtime contracts in synchronizer.** |
| **419578402** | **Mint-Mart forward proxy compatible.** |
| **416634326** | **Presence of istio.io Custom Resource Definitions (CRDs) in an Apigee hybrid cluster could cause failure in apigee-ingressgateway-manager pods.** |
| **412740465** | **Fixed issue where zipkin headers were not generated by Apigee Ingress Gateway.** |
| **409048431** | **Fixes a vulnerability which could allow a SAML signature verification to be bypassed.** |
| **378686709** | **The use of wildcards (\*) in Apigee proxy basepaths would conflict with other explicit basepaths, resulting in a 404 error.** To apply this fix, follow the procedure in [Known issue 378686709](https://cloud.google.com/apigee/docs/release/known-issues#378686709). |
| **367815792** | **Two new Flow Variables: `app_group_app` and `app_group_name` have been added to VerifyApiKey and Access Token policy.** |

### Security

| Bug ID | Description |
| --- | --- |
| **448498138** | **Security fixes for `apigee-runtime`.**  This addresses the following vulnerability:  * [CVE-2024-40094](https://nvd.nist.gov/vuln/detail/CVE-2024-40094) |
| **447367372** | **Security fixes for `apigee-runtime`.**  This addresses the following vulnerability:  * [CVE-2025-58057](https://nvd.nist.gov/vuln/detail/CVE-2025-58057) |
| **418557195** | **Security fixes for `apigee-fluent-bit`.**  This addresses the following vulnerabilities:  * [CVE-2025-24528](https://nvd.nist.gov/vuln/detail/CVE-2025-24528) * [CVE-2025-4207](https://nvd.nist.gov/vuln/detail/CVE-2025-4207) * [CVE-2025-1390](https://nvd.nist.gov/vuln/detail/CVE-2025-1390) * [CVE-2024-26462](https://nvd.nist.gov/vuln/detail/CVE-2024-26462) * [CVE-2024-13176](https://nvd.nist.gov/vuln/detail/CVE-2024-13176) |
| **N/A** | **Security fixes for `apigee-fluent-bit`.**  This addresses the following vulnerabilities:  * [CVE-2025-32990](https://nvd.nist.gov/vuln/detail/CVE-2025-32990) * [CVE-2025-32988](https://nvd.nist.gov/vuln/detail/CVE-2025-32988) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra`.**  This addresses the following vulnerability:  * [CVE-2025-23015](https://nvd.nist.gov/vuln/detail/CVE-2025-23015) |
| **N/A** | **Security fixes for `apigee-mart-server`.**  This addresses the following vulnerabilities:  * [CVE-2025-58057](https://nvd.nist.gov/vuln/detail/CVE-2025-58057) * [CVE-2025-58056](https://nvd.nist.gov/vuln/detail/CVE-2025-58056) * [CVE-2025-55163](https://nvd.nist.gov/vuln/detail/CVE-2025-55163) * [CVE-2025-48924](https://nvd.nist.gov/vuln/detail/CVE-2025-48924) * [CVE-2025-48795](https://nvd.nist.gov/vuln/detail/CVE-2025-48795) * [CVE-2025-48734](https://nvd.nist.gov/vuln/detail/CVE-2025-48734) * [CVE-2025-24970](https://nvd.nist.gov/vuln/detail/CVE-2025-24970) * [CVE-2024-47554](https://nvd.nist.gov/vuln/detail/CVE-2024-47554) * [CVE-2024-47535](https://nvd.nist.gov/vuln/detail/CVE-2024-47535) * [CVE-2024-13009](https://nvd.nist.gov/vuln/detail/CVE-2024-13009) * [CVE-2024-8184](https://nvd.nist.gov/vuln/detail/CVE-2024-8184) * [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254) * [CVE-2024-6763](https://nvd.nist.gov/vuln/detail/CVE-2024-6763) |
| **N/A** | **Security fixes for `apigee-stackdriver-logging-agent`.**  This addresses the following vulnerabilities:  * [CVE-2025-58767](https://nvd.nist.gov/vuln/detail/CVE-2025-58767) * [CVE-2025-24294](https://nvd.nist.gov/vuln/detail/CVE-2025-24294) * [CVE-2023-33953](https://nvd.nist.gov/vuln/detail/CVE-2023-33953) * [CVE-2022-32511](https://nvd.nist.gov/vuln/detail/CVE-2022-32511) * [CVE-2022-29181](https://nvd.nist.gov/vuln/detail/CVE-2022-29181) * [CVE-2022-24839](https://nvd.nist.gov/vuln/detail/CVE-2022-24839) * [CVE-2022-24836](https://nvd.nist.gov/vuln/detail/CVE-2022-24836) * [CVE-2022-0759](https://nvd.nist.gov/vuln/detail/CVE-2022-0759) * [CVE-2021-41817](https://nvd.nist.gov/vuln/detail/CVE-2021-41817) * [CVE-2021-31799](https://nvd.nist.gov/vuln/detail/CVE-2021-31799) * [CVE-2021-30560](https://nvd.nist.gov/vuln/detail/CVE-2021-30560) * [CVE-2021-28965](https://nvd.nist.gov/vuln/detail/CVE-2021-28965) * [CVE-2021-23214](https://nvd.nist.gov/vuln/detail/CVE-2021-23214) * [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695) * [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694) * [CVE-2020-25613](https://nvd.nist.gov/vuln/detail/CVE-2020-25613) * [CVE-2019-3881](https://nvd.nist.gov/vuln/detail/CVE-2019-3881) * [CVE-2018-25032](https://nvd.nist.gov/vuln/detail/CVE-2018-25032) * [CVE-2018-1115](https://nvd.nist.gov/vuln/detail/CVE-2018-1115) * [CVE-2018-10915](https://nvd.nist.gov/vuln/detail/CVE-2018-10915) * [CVE-2018-1058](https://nvd.nist.gov/vuln/detail/CVE-2018-1058) * [CVE-2018-1053](https://nvd.nist.gov/vuln/detail/CVE-2018-1053) * [CVE-2017-7546](https://nvd.nist.gov/vuln/detail/CVE-2017-7546) * [CVE-2017-7484](https://nvd.nist.gov/vuln/detail/CVE-2017-7484) * [CVE-2017-15098](https://nvd.nist.gov/vuln/detail/CVE-2017-15098) * [CVE-2017-14798](https://nvd.nist.gov/vuln/detail/CVE-2017-14798) * [CVE-2016-7954](https://nvd.nist.gov/vuln/detail/CVE-2016-7954) * [CVE-2016-7048](https://nvd.nist.gov/vuln/detail/CVE-2016-7048) * [CVE-2016-5424](https://nvd.nist.gov/vuln/detail/CVE-2016-5424) * [CVE-2016-5423](https://nvd.nist.gov/vuln/detail/CVE-2016-5423) * [CVE-2016-0766](https://nvd.nist.gov/vuln/detail/CVE-2016-0766) * [CVE-2015-3167](https://nvd.nist.gov/vuln/detail/CVE-2015-3167) * [CVE-2015-3166](https://nvd.nist.gov/vuln/detail/CVE-2015-3166) * [CVE-2015-0244](https://nvd.nist.gov/vuln/detail/CVE-2015-0244) * [CVE-2015-0243](https://nvd.nist.gov/vuln/detail/CVE-2015-0243) * [CVE-2015-0241](https://nvd.nist.gov/vuln/detail/CVE-2015-0241) |

### Changed

**Documentation change**

The following documents have been changed or introduced to align the Apigee hybrid installation guides with the supported methods for service account authentication:

* [Service account authentication methods in Apigee hybrid](https://cloud.google.com/apigee/docs/hybrid/v1.15/sa-authentication-methods) - A new overview topic for service account authentication.
* [Storing service account keys in Kubernetes secrets](https://cloud.google.com/apigee/docs/hybrid/v1.15/storing-sa-keys-in-k8s-secrets) - A new topic.
* [Step 4: Create service accounts](https://cloud.google.com/apigee/docs/hybrid/v1.15/install-service-accounts) - Rewritten to accommodate all supported methods of service account authentication.
* [Step 5: Set up service account authentication](https://cloud.google.com/apigee/docs/hybrid/v1.15/install-sa-authentication) - A new topic on configuring authentication after creating service accounts.
* [Step 7: Create the overrides](https://cloud.google.com/apigee/docs/hybrid/v1.15/install-create-overrides) and [Step 11: Install Apigee hybrid Using Helm](https://cloud.google.com/apigee/docs/hybrid/v1.15/install-helm-charts) - Topics revised to provide templates, examples, and procedures for each supported type of service account authentication.
* **Step 11(Optional): Configure Workload Identity** - Topic removed. The procedures are included in [Step 11: Install Apigee hybrid Using Helm: WIF for GKE](https://cloud.google.com/apigee/docs/hybrid/v1.15/install-helm-charts.html#wif-for-gke)

---
## 2025-10-07

### hybrid v1.14.3

On October 7, 2025 we released an enhancement to Apigee hybrid version 1.14.3, recurring, top-up, and setup fees for Apigee hybrid monetization.

**Note:** This is an enhancement to an existing release.

* For complete information on the contents of the v1.14.3 release, see [Apigee hybrid v1.14.3 release notes](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1143).

### Feature

**Recurring, top-up, and setup fees for Apigee hybrid monetization**

Apigee hybrid now supports recurring, top-up, and setup fees for monetization. For information see [Enabling monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/monetization-for-hybrid).

### Fixed

| Bug ID | Description |
| --- | --- |
| **419578402** | **Mint-Mart forward proxy compatible.** |

---
## 2025-09-29

### hybrid v1.14.3

On September 29, 2025 we released an updated version of the Apigee hybrid software, 1.14.3.

* For information on upgrading, see [Upgrading Apigee hybrid to version 1.14](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/upgrade).
* For information on new installations, see [The big picture](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/big-picture).

**Note:** This is a patch release: The container images used in patch releases are integrated with the Apigee hybrid Helm charts. Upgrading to a patch via the Helm chart automatically updates the images. No manual image changes are typically needed. For information on container image support in Apigee hybrid releases, see [Apigee release process](https://docs.cloud.google.com/apigee/docs/release/apigee-release-process#apigee-hybrid-container-images).

### Fixed

| Bug ID | Description |
| --- | --- |
| **423597917** | **Post of an [`AppGroupAppKey`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys/updateAppGroupAppKey) scopes should result in insert operation instead of update.** |
| **420675540** | **Fixed Cassandra based replication for runtime contracts in synchronizer.** |
| **416634326** | **Presence of istio.io Custom Resource Definitions (CRDs) in an Apigee hybrid cluster could cause failure in apigee-ingressgateway-manager pods.** |
| **414499328** | **`ApigeeTelemetry` could become stuck in `creating` state** |
| **412740465** | **Fixed issue where zipkin headers were not generated by Apigee Ingress Gateway.** |
| **409048431** | **Fixes a vulnerability which could allow a SAML signature verification to be bypassed.** |
| **395272878** | **Separate Forward proxy support for `googleapis.com` and `non-googleapis.com` runtime traffic.** |
| **378686709** | **The use of wildcards (\*) in Apigee proxy basepaths would conflict with other explicit basepaths, resulting in a 404 error.** To apply this fix, follow the procedure in [Known issue 378686709](https://docs.cloud.google.com/apigee/docs/release/known-issues#378686709). |
| **367815792** | **Two new Flow Variables: `app_group_app` and `app_group_name` have been added to VerifyApiKey and Access Token policy.** |

### Security

| Bug ID | Description |
| --- | --- |
| **433952146** | **Security fix.**  This addresses the following vulnerability:  * [CVE-2024-6763](https://nvd.nist.gov/vuln/detail/CVE-2024-6763) |
| **433951774** | **Security fix.**  This addresses the following vulnerability:  * [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254) |
| **433950558** | **Security fix.**  This addresses the following vulnerability:  * [CVE-2024-47554](https://nvd.nist.gov/vuln/detail/CVE-2024-47554) |
| **433950370** | **Security fix.**  This addresses the following vulnerability:  * [CVE-2025-25193](https://nvd.nist.gov/vuln/detail/CVE-2025-25193) |
| **N/A** | **Security fixes for `apigee-asm-ingress`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-asm-istiod`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-envoy`.**  This addresses the following vulnerability:  * [CVE-2025-0395](https://nvd.nist.gov/vuln/detail/CVE-2025-0395) |
| **N/A** | **Security fixes for `apigee-fluent-bit`.**  This addresses the following vulnerabilities:  * [CVE-2025-32990](https://nvd.nist.gov/vuln/detail/CVE-2025-32990) * [CVE-2025-32988](https://nvd.nist.gov/vuln/detail/CVE-2025-32988) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra`.**  This addresses the following vulnerabilities:  * [CVE-2025-23015](https://nvd.nist.gov/vuln/detail/CVE-2025-23015) * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) * [CVE-2025-24970](https://nvd.nist.gov/vuln/detail/CVE-2025-24970) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra-client`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-kube-rbac-proxy`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-mart-server`.**  This addresses the following vulnerabilities:  * [CVE-2025-48924](https://nvd.nist.gov/vuln/detail/2025-48924) * [CVE-2025-48795](https://nvd.nist.gov/vuln/detail/2025-48795) * [CVE-2025-48734](https://nvd.nist.gov/vuln/detail/2025-48734) * [CVE-2025-24970](https://nvd.nist.gov/vuln/detail/2025-24970) * [CVE-2024-47554](https://nvd.nist.gov/vuln/detail/2024-47554) * [CVE-2024-47535](https://nvd.nist.gov/vuln/detail/2024-47535) * [CVE-2024-13009](https://nvd.nist.gov/vuln/detail/2024-13009) * [CVE-2024-8184](https://nvd.nist.gov/vuln/detail/2024-8184) * [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/2024-7254) * [CVE-2024-6763](https://nvd.nist.gov/vuln/detail/2024-6763) |
| **N/A** | **Security fixes for `apigee-operators`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-stackdriver-logging-agent`.**  This addresses the following vulnerabilities:  * [CVE-2025-43857](https://nvd.nist.gov/vuln/detail/CVE-2025-43857) * [CVE-2024-41946](https://nvd.nist.gov/vuln/detail/CVE-2024-41946) * [CVE-2024-41123](https://nvd.nist.gov/vuln/detail/CVE-2024-41123) * [CVE-2024-25062](https://nvd.nist.gov/vuln/detail/CVE-2024-25062) * [CVE-2023-42915](https://nvd.nist.gov/vuln/detail/CVE-2023-42915) * [CVE-2023-33953](https://nvd.nist.gov/vuln/detail/CVE-2023-33953) * [CVE-2022-34169](https://nvd.nist.gov/vuln/detail/CVE-2022-34169) * [CVE-2022-32511](https://nvd.nist.gov/vuln/detail/CVE-2022-32511) * [CVE-2022-32207](https://nvd.nist.gov/vuln/detail/CVE-2022-32207) * [CVE-2022-29181](https://nvd.nist.gov/vuln/detail/CVE-2022-29181) * [CVE-2022-28739](https://nvd.nist.gov/vuln/detail/CVE-2022-28739) * [CVE-2022-27782](https://nvd.nist.gov/vuln/detail/CVE-2022-27782) * [CVE-2022-24839](https://nvd.nist.gov/vuln/detail/CVE-2022-24839) * [CVE-2022-24836](https://nvd.nist.gov/vuln/detail/CVE-2022-24836) * [CVE-2022-23308](https://nvd.nist.gov/vuln/detail/CVE-2022-23308) * [CVE-2022-0759](https://nvd.nist.gov/vuln/detail/CVE-2022-0759) * [CVE-2021-41819](https://nvd.nist.gov/vuln/detail/CVE-2021-41819) * [CVE-2021-41817](https://nvd.nist.gov/vuln/detail/CVE-2021-41817) * [CVE-2021-4044](https://nvd.nist.gov/vuln/detail/CVE-2021-4044) * [CVE-2021-3518](https://nvd.nist.gov/vuln/detail/CVE-2021-3518) * [CVE-2021-3517](https://nvd.nist.gov/vuln/detail/CVE-2021-3517) * [CVE-2021-32740](https://nvd.nist.gov/vuln/detail/CVE-2021-32740) * [CVE-2021-32066](https://nvd.nist.gov/vuln/detail/CVE-2021-32066) * [CVE-2021-31799](https://nvd.nist.gov/vuln/detail/CVE-2021-31799) * [CVE-2021-30560](https://nvd.nist.gov/vuln/detail/CVE-2021-30560) * [CVE-2021-28966](https://nvd.nist.gov/vuln/detail/CVE-2021-28966) * [CVE-2021-28965](https://nvd.nist.gov/vuln/detail/CVE-2021-28965) * [CVE-2021-23214](https://nvd.nist.gov/vuln/detail/CVE-2021-23214) * [CVE-2021-22926](https://nvd.nist.gov/vuln/detail/CVE-2021-22926) * [CVE-2020-7595](https://nvd.nist.gov/vuln/detail/CVE-2020-7595) * [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695) * [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694) * [CVE-2020-25613](https://nvd.nist.gov/vuln/detail/CVE-2020-25613) * [CVE-2019-9193](https://nvd.nist.gov/vuln/detail/CVE-2019-9193) * [CVE-2019-3881](https://nvd.nist.gov/vuln/detail/CVE-2019-3881) * [CVE-2019-20388](https://nvd.nist.gov/vuln/detail/CVE-2019-20388) * [CVE-2019-10211](https://nvd.nist.gov/vuln/detail/CVE-2019-10211) * [CVE-2019-10210](https://nvd.nist.gov/vuln/detail/CVE-2019-10210) * [CVE-2019-10128](https://nvd.nist.gov/vuln/detail/CVE-2019-10128) * [CVE-2019-10127](https://nvd.nist.gov/vuln/detail/CVE-2019-10127) * [CVE-2018-25032](https://nvd.nist.gov/vuln/detail/CVE-2018-25032) * [CVE-2018-1115](https://nvd.nist.gov/vuln/detail/CVE-2018-1115) * [CVE-2018-10915](https://nvd.nist.gov/vuln/detail/CVE-2018-10915) * [CVE-2018-1058](https://nvd.nist.gov/vuln/detail/CVE-2018-1058) * [CVE-2018-1053](https://nvd.nist.gov/vuln/detail/CVE-2018-1053) * [CVE-2017-7546](https://nvd.nist.gov/vuln/detail/CVE-2017-7546) * [CVE-2017-7486](https://nvd.nist.gov/vuln/detail/CVE-2017-7486) * [CVE-2017-7484](https://nvd.nist.gov/vuln/detail/CVE-2017-7484) * [CVE-2017-17405](https://nvd.nist.gov/vuln/detail/CVE-2017-17405) * [CVE-2017-15098](https://nvd.nist.gov/vuln/detail/CVE-2017-15098) * [CVE-2017-14798](https://nvd.nist.gov/vuln/detail/CVE-2017-14798) * [CVE-2016-7954](https://nvd.nist.gov/vuln/detail/CVE-2016-7954) * [CVE-2016-7048](https://nvd.nist.gov/vuln/detail/CVE-2016-7048) * [CVE-2016-5424](https://nvd.nist.gov/vuln/detail/CVE-2016-5424) * [CVE-2016-5423](https://nvd.nist.gov/vuln/detail/CVE-2016-5423) * [CVE-2016-0766](https://nvd.nist.gov/vuln/detail/CVE-2016-0766) * [CVE-2015-3167](https://nvd.nist.gov/vuln/detail/CVE-2015-3167) * [CVE-2015-3166](https://nvd.nist.gov/vuln/detail/CVE-2015-3166) * [CVE-2015-0244](https://nvd.nist.gov/vuln/detail/CVE-2015-0244) * [CVE-2015-0243](https://nvd.nist.gov/vuln/detail/CVE-2015-0243) * [CVE-2015-0242](https://nvd.nist.gov/vuln/detail/CVE-2015-0242) * [CVE-2015-0241](https://nvd.nist.gov/vuln/detail/CVE-2015-0241) |
| **N/A** | **Security fixes for `apigee-watcher`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |

---
## 2025-09-24

### Apigee Operator for Kubernetes for Apigee Hybrid (Preview)

On September 24, 2025 we released the Apigee Operator for Kubernetes for Apigee Hybrid 1.15.0 and newer.

The Apigee Operator for Kubernetes allows you to perform API management tasks, such as defining API products and operations, using Kubernetes tools. This preview release allows you to integrate this capability with your Apigee hybrid (v1.15.0 or newer) installation.

For more information, see:

* [Apigee Operator for Kubernetes overview](https://cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-overview)
* [Install the Apigee Operator for Kubernetes for Apigee hybrid](https://cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install-hybrid)

---
## 2025-07-09

### hybrid v1.13.4

On July 9, 2025 we released an updated version of the Apigee hybrid software, 1.13.4.

* For information on upgrading, see [Upgrading Apigee hybrid to version 1.13](https://cloud.google.com/apigee/docs/hybrid/v1.13/upgrade).
* For information on new installations, see [The big picture](https://cloud.google.com/apigee/docs/hybrid/v1.13/big-picture).

**Note:** if you are upgrading to Apigee hybrid version 1.13.4 from version 1.13.2 or earlier, see [APPENDIX: Validate policies after upgrade to 1.13.3 or later](https://cloud.google.com/apigee/docs/hybrid/v1.13/upgrade#recommended-actions-upgrade-1133) for steps to address stricter class instantiation checks introduced in [version 1.13.3](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1133).
**Note:** This is a patch release: The container images used in patch releases are integrated with the Apigee hybrid Helm charts. Upgrading to a patch via the Helm chart automatically updates the images. No manual image changes are typically needed. For information on container image support in Apigee hybrid releases, see [Apigee release process](https://cloud.google.com/apigee/docs/release/apigee-release-process#apigee-hybrid-container-images).

### Fixed

| Bug ID | Description |
| --- | --- |
| **420675540** | **Fixed Cassandra based replication for runtime contracts in synchronizer.** |
| **401746333** | **Fixed a `java.lang.ClassCircularityError` that could occur in Java Callouts due to an issue with the class loading mechanism.** |
| **382565315** | **A memory leak within the Security Policy has been addressed, improving system stability.** |
| **375360455** | **Updated apigee-runtime drain timeout to 300s to fix connection termination issue during pod termination.** |

### Security

| Bug ID | Description |
| --- | --- |
| **396944778** | **Security fixes for `apigee-synchronizer`.**  This addresses the following vulnerabilities:  * [CVE-2025-25193](https://nvd.nist.gov/vuln/detail/CVE-2025-25193) * [CVE-2025-24970](https://nvd.nist.gov/vuln/detail/CVE-2025-24970) * [CVE-2025-23184](https://nvd.nist.gov/vuln/detail/CVE-2025-23184) * [CVE-2024-47554](https://nvd.nist.gov/vuln/detail/CVE-2024-47554) |
| **392934392** | **Security fixes for `apigee-logger`.** |
| **N/A** | **Security fixes for `apigee-mart-server`.**  This addresses the following vulnerability:  * [CVE-2024-20952](https://nvd.nist.gov/vuln/detail/CVE-2024-20952) |
| **N/A** | **Security fixes for `apigee-mint-task-scheduler`.**  This addresses the following vulnerability:  * [CVE-2024-20952](https://nvd.nist.gov/vuln/detail/CVE-2024-20952) |
| **N/A** | **Security fixes for `apigee-redis`.**  This addresses the following vulnerabilities:  * [CVE-2022-24834](https://nvd.nist.gov/vuln/detail/CVE-2022-24834) * [CVE-2022-24735](https://nvd.nist.gov/vuln/detail/CVE-2022-24735) |
| **N/A** | **Security fixes for `apigee-runtime`.**  This addresses the following vulnerability:  * [CVE-2024-20952](https://nvd.nist.gov/vuln/detail/CVE-2024-20952) |
| **N/A** | **Security fixes for `apigee-synchronizer`.**  This addresses the following vulnerability:  * [CVE-2024-20952](https://nvd.nist.gov/vuln/detail/CVE-2024-20952) |
| **N/A** | **Security fixes for `vault`.**  This addresses the following vulnerability:  * [CVE-2025-0377](https://nvd.nist.gov/vuln/detail/CVE-2025-0377) |

---
## 2025-06-04

### Announcement



### hybrid v1.15.0

On June 4, 2025 we released an updated version of the Apigee hybrid software, 1.15.0.

* For information on upgrading, see [Upgrading Apigee hybrid to version 1.15](https://cloud.google.com/apigee/docs/hybrid/v1.15/upgrade).
* For information on new installations, see [The big picture](https://cloud.google.com/apigee/docs/hybrid/v1.15/big-picture).

**Note:** This is a minor release: The container images used in minor releases are integrated with the Apigee hybrid Helm charts. Upgrading to a minor via the Helm chart automatically updates the images. No manual image changes are typically needed. For information on container image support in Apigee hybrid releases, see [Apigee release process](https://cloud.google.com/apigee/docs/release/apigee-release-process#apigee-hybrid-container-images).

### Feature

**Large message payload support in Apigee hybrid**

Apigee now supports message payloads up to 30MB. You configure support for large message payloads in Apigee hybrid for individual environments or for your whole installation. See [Configure large message payload support in Apigee hybrid](https://cloud.google.com/apigee/docs/hybrid/v1.15/configure-large-payload-support).

### Fixed

| Bug ID | Description |
| --- | --- |
| **412324617** | **Fixed issue where Runtime container could spin at 100% cpu limit.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142)) |
| **399447688** | **API proxy deployment could become stuck in `PROGRESSING` state.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142)) |
| **396886110** | **Fixed a bug where the HPA max replicas could be lower than min.** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141)) |
| **413708061**, **396571537** | **Rotating Cassandra credentials in Kubernetes secrets fixed for Multi-region deployments.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142)) |
| **392547038** | **Add Helm chart template checks for non-existent environments and virtualhosts.** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141)) |
| **391861216** | **Restore for Google Cloud Platform and HYBRID Cloud Providers no longer affects system keyspaces. This fixes [Known Issue 391861216](https://cloud.google.com/apigee/docs/release/known-issues#391861216).** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141)) |
| **390258745**, **388608440** | **Any left over Cassandra snapshots are automatically removed. This fixes [known issue 388608440](https://cloud.google.com/apigee/docs/release/known-issues#388608440).** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141)) |
| **384937220** | **Fixed `ApigeeRoute` name collision on internal chaining gateway for Enhanced Proxy Limits.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142)) |
| **383441226** | **Added the following `metrics` configuration properties:**  * [metrics.adapter.resources.limits.cpu](https://cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#metrics-adapter-resources-limits-cpu) * [metrics.adapter.resources.limits.memory](https://cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#metrics-adapter-resources-limits-memory) * [metrics.adapter.resources.requests.cpu](https://cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#metrics-adapter-resources-requests-cpu) * [metrics.adapter.resources.requests.memory](https://cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#metrics-adapter-resources-requests-memory) * [metrics.prometheus.resources.limits.cpu](https://cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#metrics-prometheus-resources-limits-cpu) * [metrics.prometheus.resources.limits.memory](https://cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#metrics-prometheus-resources-limits-memory) * [metrics.prometheus.resources.requests.cpu](https://cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#metrics-prometheus-resources-requests-cpu) * [metrics.prometheus.resources.requests.memory](https://cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref#metrics-prometheus-resources-requests-memory)  (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141)) |
| **368155212** | **Auto Cassandra secret rotation could fail when [Enhanced per-environment proxy limits](https://cloud.google.com/apigee/docs/hybrid/v1.15/enhanced-proxy-limits) are enabled.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142)) |
| **367681534** | **Tagging [`apigee-stackdriver-prometheus-sidecar`](http://gcr.io/apigee-release/hybrid/apigee-stackdriver-prometheus-sidecar:0.10.0) to prevent removal from customer repos after 2 years due to infrequent updates.** (Fixed in [1.14.0-hotfix.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_1140-hotfix1)) |

### Security

**Fixed in this release**

| Bug ID | Description |
| --- | --- |
| **N/A** | **Security fixes for `apigee-asm-ingress`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-asm-istiod`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-connect-agent`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-envoy`.**  This addresses the following vulnerabilities:  * [CVE-2025-4802](https://nvd.nist.gov/vuln/detail/CVE-2025-4802) * [CVE-2025-0395](https://nvd.nist.gov/vuln/detail/CVE-2025-0395) |
| **N/A** | **Security fixes for `apigee-fluent-bit`.**  This addresses the following vulnerability:  * [CVE-2025-4802](https://nvd.nist.gov/vuln/detail/CVE-2025-4802) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra`.**  This addresses the following vulnerabilities:  * [CVE-2025-23015](https://nvd.nist.gov/vuln/detail/CVE-2025-23015) * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra-client`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-kube-rbac-proxy`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-mart-server`.**  This addresses the following vulnerability:  * [CVE-2022-3715](https://nvd.nist.gov/vuln/detail/CVE-2022-3715) |
| **N/A** | **Security fixes for `apigee-operators`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-prom-prometheus`.**  This addresses the following vulnerabilities:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) * [CVE-2025-22869](https://nvd.nist.gov/vuln/detail/CVE-2025-22869) |
| **N/A** | **Security fixes for `apigee-prometheus-adapter`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `apigee-redis`.**  This addresses the following vulnerabilities:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) * [CVE-2024-24791](https://nvd.nist.gov/vuln/detail/CVE-2024-24791) |
| **N/A** | **Security fixes for `apigee-runtime`.**  This addresses the following vulnerabilities:  * [CVE-2025-0725](https://nvd.nist.gov/vuln/detail/CVE-2025-0725) * [CVE-2022-3715](https://nvd.nist.gov/vuln/detail/CVE-2022-3715) |
| **N/A** | **Security fixes for `apigee-stackdriver-logging-agent`.**  This addresses the following vulnerabilities:  * [CVE-2025-43857](https://nvd.nist.gov/vuln/detail/CVE-2025-43857) * [CVE-2025-32415](https://nvd.nist.gov/vuln/detail/CVE-2025-32415) * [CVE-2025-32414](https://nvd.nist.gov/vuln/detail/CVE-2025-32414) * [CVE-2025-27788](https://nvd.nist.gov/vuln/detail/CVE-2025-27788) * [CVE-2025-27113](https://nvd.nist.gov/vuln/detail/CVE-2025-27113) * [CVE-2024-49761](https://nvd.nist.gov/vuln/detail/CVE-2024-49761) * [CVE-2024-41946](https://nvd.nist.gov/vuln/detail/CVE-2024-41946) * [CVE-2024-41123](https://nvd.nist.gov/vuln/detail/CVE-2024-41123) * [CVE-2024-25062](https://nvd.nist.gov/vuln/detail/CVE-2024-25062) * [CVE-2023-42915](https://nvd.nist.gov/vuln/detail/CVE-2023-42915) * [CVE-2023-33953](https://nvd.nist.gov/vuln/detail/CVE-2023-33953) * [CVE-2022-34169](https://nvd.nist.gov/vuln/detail/CVE-2022-34169) * [CVE-2022-32511](https://nvd.nist.gov/vuln/detail/CVE-2022-32511) * [CVE-2022-32207](https://nvd.nist.gov/vuln/detail/CVE-2022-32207) * [CVE-2022-29181](https://nvd.nist.gov/vuln/detail/CVE-2022-29181) * [CVE-2022-28739](https://nvd.nist.gov/vuln/detail/CVE-2022-28739) * [CVE-2022-27782](https://nvd.nist.gov/vuln/detail/CVE-2022-27782) * [CVE-2022-24839](https://nvd.nist.gov/vuln/detail/CVE-2022-24839) * [CVE-2022-24836](https://nvd.nist.gov/vuln/detail/CVE-2022-24836) * [CVE-2022-23308](https://nvd.nist.gov/vuln/detail/CVE-2022-23308) * [CVE-2022-0759](https://nvd.nist.gov/vuln/detail/CVE-2022-0759) * [CVE-2021-41819](https://nvd.nist.gov/vuln/detail/CVE-2021-41819) * [CVE-2021-41817](https://nvd.nist.gov/vuln/detail/CVE-2021-41817) * [CVE-2021-4044](https://nvd.nist.gov/vuln/detail/CVE-2021-4044) * [CVE-2021-3518](https://nvd.nist.gov/vuln/detail/CVE-2021-3518) * [CVE-2021-3517](https://nvd.nist.gov/vuln/detail/CVE-2021-3517) * [CVE-2021-32740](https://nvd.nist.gov/vuln/detail/CVE-2021-32740) * [CVE-2021-32066](https://nvd.nist.gov/vuln/detail/CVE-2021-32066) * [CVE-2021-31799](https://nvd.nist.gov/vuln/detail/CVE-2021-31799) * [CVE-2021-30560](https://nvd.nist.gov/vuln/detail/CVE-2021-30560) * [CVE-2021-28966](https://nvd.nist.gov/vuln/detail/CVE-2021-28966) * [CVE-2021-28965](https://nvd.nist.gov/vuln/detail/CVE-2021-28965) * [CVE-2021-23214](https://nvd.nist.gov/vuln/detail/CVE-2021-23214) * [CVE-2021-22926](https://nvd.nist.gov/vuln/detail/CVE-2021-22926) * [CVE-2020-7595](https://nvd.nist.gov/vuln/detail/CVE-2020-7595) * [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695) * [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694) * [CVE-2020-25613](https://nvd.nist.gov/vuln/detail/CVE-2020-25613) * [CVE-2019-9193](https://nvd.nist.gov/vuln/detail/CVE-2019-9193) * [CVE-2019-3881](https://nvd.nist.gov/vuln/detail/CVE-2019-3881) * [CVE-2019-20388](https://nvd.nist.gov/vuln/detail/CVE-2019-20388) * [CVE-2019-10211](https://nvd.nist.gov/vuln/detail/CVE-2019-10211) * [CVE-2019-10210](https://nvd.nist.gov/vuln/detail/CVE-2019-10210) * [CVE-2019-10128](https://nvd.nist.gov/vuln/detail/CVE-2019-10128) * [CVE-2019-10127](https://nvd.nist.gov/vuln/detail/CVE-2019-10127) * [CVE-2018-25032](https://nvd.nist.gov/vuln/detail/CVE-2018-25032) * [CVE-2018-1115](https://nvd.nist.gov/vuln/detail/CVE-2018-1115) * [CVE-2018-10915](https://nvd.nist.gov/vuln/detail/CVE-2018-10915) * [CVE-2018-1058](https://nvd.nist.gov/vuln/detail/CVE-2018-1058) * [CVE-2018-1053](https://nvd.nist.gov/vuln/detail/CVE-2018-1053) * [CVE-2017-7546](https://nvd.nist.gov/vuln/detail/CVE-2017-7546) * [CVE-2017-7486](https://nvd.nist.gov/vuln/detail/CVE-2017-7486) * [CVE-2017-7484](https://nvd.nist.gov/vuln/detail/CVE-2017-7484) * [CVE-2017-17405](https://nvd.nist.gov/vuln/detail/CVE-2017-17405) * [CVE-2017-15098](https://nvd.nist.gov/vuln/detail/CVE-2017-15098) * [CVE-2017-14798](https://nvd.nist.gov/vuln/detail/CVE-2017-14798) * [CVE-2016-7954](https://nvd.nist.gov/vuln/detail/CVE-2016-7954) * [CVE-2016-7048](https://nvd.nist.gov/vuln/detail/CVE-2016-7048) * [CVE-2016-5424](https://nvd.nist.gov/vuln/detail/CVE-2016-5424) * [CVE-2016-5423](https://nvd.nist.gov/vuln/detail/CVE-2016-5423) * [CVE-2016-0766](https://nvd.nist.gov/vuln/detail/CVE-2016-0766) * [CVE-2015-3167](https://nvd.nist.gov/vuln/detail/CVE-2015-3167) * [CVE-2015-3166](https://nvd.nist.gov/vuln/detail/CVE-2015-3166) * [CVE-2015-0244](https://nvd.nist.gov/vuln/detail/CVE-2015-0244) * [CVE-2015-0243](https://nvd.nist.gov/vuln/detail/CVE-2015-0243) * [CVE-2015-0242](https://nvd.nist.gov/vuln/detail/CVE-2015-0242) * [CVE-2015-0241](https://nvd.nist.gov/vuln/detail/CVE-2015-0241) |
| **N/A** | **Security fixes for `apigee-synchronizer`.**  This addresses the following vulnerabilities:  * [CVE-2025-0725](https://nvd.nist.gov/vuln/detail/CVE-2025-0725) * [CVE-2022-3715](https://nvd.nist.gov/vuln/detail/CVE-2022-3715) |
| **N/A** | **Security fixes for `apigee-watcher`.**  This addresses the following vulnerability:  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871) |
| **N/A** | **Security fixes for `cert-manager-cainjector`.**  This addresses the following vulnerabilities:  * [CVE-2023-45287](https://nvd.nist.gov/vuln/detail/CVE-2023-45287) * [CVE-2023-45285](https://nvd.nist.gov/vuln/detail/CVE-2023-45285) * [CVE-2023-44487](https://nvd.nist.gov/vuln/detail/CVE-2023-44487) * [CVE-2023-39325](https://nvd.nist.gov/vuln/detail/CVE-2023-39325) * [CVE-2023-39323](https://nvd.nist.gov/vuln/detail/CVE-2023-39323) * [CVE-2023-29405](https://nvd.nist.gov/vuln/detail/CVE-2023-29405) * [CVE-2023-29404](https://nvd.nist.gov/vuln/detail/CVE-2023-29404) * [CVE-2023-29403](https://nvd.nist.gov/vuln/detail/CVE-2023-29403) * [CVE-2023-29402](https://nvd.nist.gov/vuln/detail/CVE-2023-29402) * [CVE-2023-29400](https://nvd.nist.gov/vuln/detail/CVE-2023-29400) * [CVE-2023-24540](https://nvd.nist.gov/vuln/detail/CVE-2023-24540) * [CVE-2023-24539](https://nvd.nist.gov/vuln/detail/CVE-2023-24539) * [CVE-2023-24538](https://nvd.nist.gov/vuln/detail/CVE-2023-24538) * [CVE-2023-24537](https://nvd.nist.gov/vuln/detail/CVE-2023-24537) * [CVE-2023-24536](https://nvd.nist.gov/vuln/detail/CVE-2023-24536) * [CVE-2023-24534](https://nvd.nist.gov/vuln/detail/CVE-2023-24534) * [CVE-2022-41725](https://nvd.nist.gov/vuln/detail/CVE-2022-41725) * [CVE-2022-41724](https://nvd.nist.gov/vuln/detail/CVE-2022-41724) * [CVE-2022-41723](https://nvd.nist.gov/vuln/detail/CVE-2022-41723) * [CVE-2022-41715](https://nvd.nist.gov/vuln/detail/CVE-2022-41715) * [CVE-2022-32189](https://nvd.nist.gov/vuln/detail/CVE-2022-32189) * [CVE-2022-30635](https://nvd.nist.gov/vuln/detail/CVE-2022-30635) * [CVE-2022-30633](https://nvd.nist.gov/vuln/detail/CVE-2022-30633) * [CVE-2022-30632](https://nvd.nist.gov/vuln/detail/CVE-2022-30632) * [CVE-2022-30631](https://nvd.nist.gov/vuln/detail/CVE-2022-30631) * [CVE-2022-30630](https://nvd.nist.gov/vuln/detail/CVE-2022-30630) * [CVE-2022-30580](https://nvd.nist.gov/vuln/detail/CVE-2022-30580) * [CVE-2022-2880](https://nvd.nist.gov/vuln/detail/CVE-2022-2880) * [CVE-2022-2879](https://nvd.nist.gov/vuln/detail/CVE-2022-2879) * [CVE-2022-28327](https://nvd.nist.gov/vuln/detail/CVE-2022-28327) * [CVE-2022-28131](https://nvd.nist.gov/vuln/detail/CVE-2022-28131) * [CVE-2022-27664](https://nvd.nist.gov/vuln/detail/CVE-2022-27664) * [CVE-2022-24921](https://nvd.nist.gov/vuln/detail/CVE-2022-24921) * [CVE-2022-24675](https://nvd.nist.gov/vuln/detail/CVE-2022-24675) * [CVE-2022-23806](https://nvd.nist.gov/vuln/detail/CVE-2022-23806) * [CVE-2022-23773](https://nvd.nist.gov/vuln/detail/CVE-2022-23773) * [CVE-2022-23772](https://nvd.nist.gov/vuln/detail/CVE-2022-23772) * [CVE-2021-44716](https://nvd.nist.gov/vuln/detail/CVE-2021-44716) * [CVE-2021-41772](https://nvd.nist.gov/vuln/detail/CVE-2021-41772) * [CVE-2021-41771](https://nvd.nist.gov/vuln/detail/CVE-2021-41771) * [CVE-2021-39293](https://nvd.nist.gov/vuln/detail/CVE-2021-39293) * [CVE-2021-38297](https://nvd.nist.gov/vuln/detail/CVE-2021-38297) * [CVE-2021-33198](https://nvd.nist.gov/vuln/detail/CVE-2021-33198) * [CVE-2021-33196](https://nvd.nist.gov/vuln/detail/CVE-2021-33196) * [CVE-2021-33195](https://nvd.nist.gov/vuln/detail/CVE-2021-33195) * [CVE-2021-33194](https://nvd.nist.gov/vuln/detail/CVE-2021-33194) * [CVE-2021-29923](https://nvd.nist.gov/vuln/detail/CVE-2021-29923) * [CVE-2021-27918](https://nvd.nist.gov/vuln/detail/CVE-2021-27918) * [CVE-2020-28367](https://nvd.nist.gov/vuln/detail/CVE-2020-28367) * [CVE-2020-28366](https://nvd.nist.gov/vuln/detail/CVE-2020-28366) * [CVE-2020-28362](https://nvd.nist.gov/vuln/detail/CVE-2020-28362) * [CVE-2020-16845](https://nvd.nist.gov/vuln/detail/CVE-2020-16845) |
| **N/A** | **Security fixes for `cert-manager-controller`.**  This addresses the following vulnerabilities:  * [CVE-2023-45287](https://nvd.nist.gov/vuln/detail/CVE-2023-45287) * [CVE-2023-45285](https://nvd.nist.gov/vuln/detail/CVE-2023-45285) * [CVE-2023-44487](https://nvd.nist.gov/vuln/detail/CVE-2023-44487) * [CVE-2023-39325](https://nvd.nist.gov/vuln/detail/CVE-2023-39325) * [CVE-2023-39323](https://nvd.nist.gov/vuln/detail/CVE-2023-39323) * [CVE-2023-29405](https://nvd.nist.gov/vuln/detail/CVE-2023-29405) * [CVE-2023-29404](https://nvd.nist.gov/vuln/detail/CVE-2023-29404) * [CVE-2023-29403](https://nvd.nist.gov/vuln/detail/CVE-2023-29403) * [CVE-2023-29402](https://nvd.nist.gov/vuln/detail/CVE-2023-29402) * [CVE-2023-29400](https://nvd.nist.gov/vuln/detail/CVE-2023-29400) * [CVE-2023-24540](https://nvd.nist.gov/vuln/detail/CVE-2023-24540) * [CVE-2023-24539](https://nvd.nist.gov/vuln/detail/CVE-2023-24539) * [CVE-2023-24538](https://nvd.nist.gov/vuln/detail/CVE-2023-24538) * [CVE-2023-24537](https://nvd.nist.gov/vuln/detail/CVE-2023-24537) * [CVE-2023-24536](https://nvd.nist.gov/vuln/detail/CVE-2023-24536) * [CVE-2023-24534](https://nvd.nist.gov/vuln/detail/CVE-2023-24534) * [CVE-2022-41725](https://nvd.nist.gov/vuln/detail/CVE-2022-41725) * [CVE-2022-41724](https://nvd.nist.gov/vuln/detail/CVE-2022-41724) * [CVE-2022-41723](https://nvd.nist.gov/vuln/detail/CVE-2022-41723) * [CVE-2022-41715](https://nvd.nist.gov/vuln/detail/CVE-2022-41715) * [CVE-2022-32189](https://nvd.nist.gov/vuln/detail/CVE-2022-32189) * [CVE-2022-30635](https://nvd.nist.gov/vuln/detail/CVE-2022-30635) * [CVE-2022-30633](https://nvd.nist.gov/vuln/detail/CVE-2022-30633) * [CVE-2022-30632](https://nvd.nist.gov/vuln/detail/CVE-2022-30632) * [CVE-2022-30631](https://nvd.nist.gov/vuln/detail/CVE-2022-30631) * [CVE-2022-30630](https://nvd.nist.gov/vuln/detail/CVE-2022-30630) * [CVE-2022-30580](https://nvd.nist.gov/vuln/detail/CVE-2022-30580) * [CVE-2022-2880](https://nvd.nist.gov/vuln/detail/CVE-2022-2880) * [CVE-2022-2879](https://nvd.nist.gov/vuln/detail/CVE-2022-2879) * [CVE-2022-28327](https://nvd.nist.gov/vuln/detail/CVE-2022-28327) * [CVE-2022-28131](https://nvd.nist.gov/vuln/detail/CVE-2022-28131) * [CVE-2022-27664](https://nvd.nist.gov/vuln/detail/CVE-2022-27664) * [CVE-2022-24921](https://nvd.nist.gov/vuln/detail/CVE-2022-24921) * [CVE-2022-24675](https://nvd.nist.gov/vuln/detail/CVE-2022-24675) * [CVE-2022-23806](https://nvd.nist.gov/vuln/detail/CVE-2022-23806) * [CVE-2022-23773](https://nvd.nist.gov/vuln/detail/CVE-2022-23773) * [CVE-2022-23772](https://nvd.nist.gov/vuln/detail/CVE-2022-23772) * [CVE-2021-44716](https://nvd.nist.gov/vuln/detail/CVE-2021-44716) * [CVE-2021-41772](https://nvd.nist.gov/vuln/detail/CVE-2021-41772) * [CVE-2021-41771](https://nvd.nist.gov/vuln/detail/CVE-2021-41771) * [CVE-2021-39293](https://nvd.nist.gov/vuln/detail/CVE-2021-39293) * [CVE-2021-38297](https://nvd.nist.gov/vuln/detail/CVE-2021-38297) * [CVE-2021-33198](https://nvd.nist.gov/vuln/detail/CVE-2021-33198) * [CVE-2021-33196](https://nvd.nist.gov/vuln/detail/CVE-2021-33196) * [CVE-2021-33195](https://nvd.nist.gov/vuln/detail/CVE-2021-33195) * [CVE-2021-33194](https://nvd.nist.gov/vuln/detail/CVE-2021-33194) * [CVE-2021-29923](https://nvd.nist.gov/vuln/detail/CVE-2021-29923) * [CVE-2021-27918](https://nvd.nist.gov/vuln/detail/CVE-2021-27918) * [CVE-2020-28367](https://nvd.nist.gov/vuln/detail/CVE-2020-28367) * [CVE-2020-28366](https://nvd.nist.gov/vuln/detail/CVE-2020-28366) * [CVE-2020-28362](https://nvd.nist.gov/vuln/detail/CVE-2020-28362) * [CVE-2020-16845](https://nvd.nist.gov/vuln/detail/CVE-2020-16845) |
| **N/A** | **Security fixes for `cert-manager-webhook`.**  This addresses the following vulnerabilities:  * [CVE-2023-45287](https://nvd.nist.gov/vuln/detail/CVE-2023-45287) * [CVE-2023-45285](https://nvd.nist.gov/vuln/detail/CVE-2023-45285) * [CVE-2023-44487](https://nvd.nist.gov/vuln/detail/CVE-2023-44487) * [CVE-2023-39325](https://nvd.nist.gov/vuln/detail/CVE-2023-39325) * [CVE-2023-39323](https://nvd.nist.gov/vuln/detail/CVE-2023-39323) * [CVE-2023-29405](https://nvd.nist.gov/vuln/detail/CVE-2023-29405) * [CVE-2023-29404](https://nvd.nist.gov/vuln/detail/CVE-2023-29404) * [CVE-2023-29403](https://nvd.nist.gov/vuln/detail/CVE-2023-29403) * [CVE-2023-29402](https://nvd.nist.gov/vuln/detail/CVE-2023-29402) * [CVE-2023-29400](https://nvd.nist.gov/vuln/detail/CVE-2023-29400) * [CVE-2023-24540](https://nvd.nist.gov/vuln/detail/CVE-2023-24540) * [CVE-2023-24539](https://nvd.nist.gov/vuln/detail/CVE-2023-24539) * [CVE-2023-24538](https://nvd.nist.gov/vuln/detail/CVE-2023-24538) * [CVE-2023-24537](https://nvd.nist.gov/vuln/detail/CVE-2023-24537) * [CVE-2023-24536](https://nvd.nist.gov/vuln/detail/CVE-2023-24536) * [CVE-2023-24534](https://nvd.nist.gov/vuln/detail/CVE-2023-24534) * [CVE-2022-41725](https://nvd.nist.gov/vuln/detail/CVE-2022-41725) * [CVE-2022-41724](https://nvd.nist.gov/vuln/detail/CVE-2022-41724) * [CVE-2022-41723](https://nvd.nist.gov/vuln/detail/CVE-2022-41723) * [CVE-2022-41715](https://nvd.nist.gov/vuln/detail/CVE-2022-41715) * [CVE-2022-32189](https://nvd.nist.gov/vuln/detail/CVE-2022-32189) * [CVE-2022-30635](https://nvd.nist.gov/vuln/detail/CVE-2022-30635) * [CVE-2022-30633](https://nvd.nist.gov/vuln/detail/CVE-2022-30633) * [CVE-2022-30632](https://nvd.nist.gov/vuln/detail/CVE-2022-30632) * [CVE-2022-30631](https://nvd.nist.gov/vuln/detail/CVE-2022-30631) * [CVE-2022-30630](https://nvd.nist.gov/vuln/detail/CVE-2022-30630) * [CVE-2022-30580](https://nvd.nist.gov/vuln/detail/CVE-2022-30580) * [CVE-2022-2880](https://nvd.nist.gov/vuln/detail/CVE-2022-2880) * [CVE-2022-2879](https://nvd.nist.gov/vuln/detail/CVE-2022-2879) * [CVE-2022-28327](https://nvd.nist.gov/vuln/detail/CVE-2022-28327) * [CVE-2022-28131](https://nvd.nist.gov/vuln/detail/CVE-2022-28131) * [CVE-2022-27664](https://nvd.nist.gov/vuln/detail/CVE-2022-27664) * [CVE-2022-24921](https://nvd.nist.gov/vuln/detail/CVE-2022-24921) * [CVE-2022-24675](https://nvd.nist.gov/vuln/detail/CVE-2022-24675) * [CVE-2022-23806](https://nvd.nist.gov/vuln/detail/CVE-2022-23806) * [CVE-2022-23773](https://nvd.nist.gov/vuln/detail/CVE-2022-23773) * [CVE-2022-23772](https://nvd.nist.gov/vuln/detail/CVE-2022-23772) * [CVE-2021-44716](https://nvd.nist.gov/vuln/detail/CVE-2021-44716) * [CVE-2021-41772](https://nvd.nist.gov/vuln/detail/CVE-2021-41772) * [CVE-2021-41771](https://nvd.nist.gov/vuln/detail/CVE-2021-41771) * [CVE-2021-39293](https://nvd.nist.gov/vuln/detail/CVE-2021-39293) * [CVE-2021-38297](https://nvd.nist.gov/vuln/detail/CVE-2021-38297) * [CVE-2021-33198](https://nvd.nist.gov/vuln/detail/CVE-2021-33198) * [CVE-2021-33196](https://nvd.nist.gov/vuln/detail/CVE-2021-33196) * [CVE-2021-33195](https://nvd.nist.gov/vuln/detail/CVE-2021-33195) * [CVE-2021-33194](https://nvd.nist.gov/vuln/detail/CVE-2021-33194) * [CVE-2021-29923](https://nvd.nist.gov/vuln/detail/CVE-2021-29923) * [CVE-2021-27918](https://nvd.nist.gov/vuln/detail/CVE-2021-27918) * [CVE-2020-28367](https://nvd.nist.gov/vuln/detail/CVE-2020-28367) * [CVE-2020-28366](https://nvd.nist.gov/vuln/detail/CVE-2020-28366) * [CVE-2020-28362](https://nvd.nist.gov/vuln/detail/CVE-2020-28362) * [CVE-2020-16845](https://nvd.nist.gov/vuln/detail/CVE-2020-16845) |
| **N/A** | **Security fixes for `vault`.**  This addresses the following vulnerability:  * [CVE-2025-0377](https://nvd.nist.gov/vuln/detail/CVE-2025-0377) |

### Security

**Fixed since last minor release**

| Bug ID | Description |
| --- | --- |
| **391923260** | **Security fixes for `apigee-watcher`.** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141))  This addresses the following vulnerabilities:  * [CVE-2024-24789](https://nvd.nist.gov/vuln/detail/CVE-2024-24789) * [CVE-2024-45337](https://nvd.nist.gov/vuln/detail/CVE-2024-45337) * [CVE-2024-45338](https://nvd.nist.gov/vuln/detail/CVE-2024-45338) * [CVE-2024-24790](https://nvd.nist.gov/vuln/detail/CVE-2024-24790) * [CVE-2022-23635](https://nvd.nist.gov/vuln/detail/CVE-2022-23635) * [CVE-2022-31045](https://nvd.nist.gov/vuln/detail/CVE-2022-31045) * [CVE-2021-39156](https://nvd.nist.gov/vuln/detail/CVE-2021-39156) * [CVE-2021-39155](https://nvd.nist.gov/vuln/detail/CVE-2021-39155) * [CVE-2019-14993](https://nvd.nist.gov/vuln/detail/CVE-2019-14993) |
| **391923260** | **Security fixes for `apigee-udca`.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142))  This addresses the following vulnerabilities:  * [CVE-2025-27788](https://nvd.nist.gov/vuln/detail/CVE-2025-27788) * [CVE-2025-22869](https://nvd.nist.gov/vuln/detail/CVE-2025-22869) * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868) * [CVE-2024-45337](https://nvd.nist.gov/vuln/detail/CVE-2024-45337) * [CVE-2024-34158](https://nvd.nist.gov/vuln/detail/CVE-CVE-2024-34158) * [CVE-2024-34156](https://nvd.nist.gov/vuln/detail/CVE-CVE-2024-34156) * [CVE-2023-6481](https://nvd.nist.gov/vuln/detail/CVE-2023-6481) |
| **385394193**, **383850393**, **383778273** | **Security fixes for `apigee-cassandra-backup-utility`, `apigee-cassandra-client`, and `apigee-hybrid-cassandra`.** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141))  This addresses the following vulnerabilities:  * [CVE-2024-0727](https://nvd.nist.gov/vuln/detail/CVE-2024-0727) * [CVE-2023-5678](https://nvd.nist.gov/vuln/detail/CVE-2023-5678) * [CVE-2022-3715](https://nvd.nist.gov/vuln/detail/CVE-2022-3715) |
| **385394193**, **383850393**, **383778273** | **Security fixes for `apigee-cassandra-backup-utility`, `apigee-cassandra-client`, and `apigee-hybrid-cassandra`.** (Fixed in [v1.13.3](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1133))  This addresses the following vulnerabilities:  * [CVE-2022-3715](https://nvd.nist.gov/vuln/detail/CVE-2022-3715) * [CVE-2024-0727](https://nvd.nist.gov/vuln/detail/CVE-2024-0727) * [CVE-2023-5678](https://nvd.nist.gov/vuln/detail/CVE-2023-5678) |
| **383113773, 382967738** | **Fixed a vulnerability in PythonScript policy.** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141)) |
| **365178914** | **Security fixes for `apigee-cassandra-backup-utility` and `apigee-hybrid-cassandra`.** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141))  This addresses the following vulnerability:  * [CVE-2023-37920](https://nvd.nist.gov/vuln/detail/CVE-2023-37920) |
| **N/A** | **Security fixes for `apigee-watcher`.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142))  This addresses the following vulnerabilities:  * [CVE-2025-22869](https://nvd.nist.gov/vuln/detail/CVE-2025-22869) * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868) |
| **N/A** | **Security fixes for `apigee-udca`.** (Fixed in [v1.13.3](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1133))  This addresses the following vulnerability:  * [CVE-2024-24790](https://nvd.nist.gov/vuln/detail/CVE-2024-24790) |
| **N/A** | **Security fixes for `apigee-stackdriver-logging-agent`.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142))  This addresses the following vulnerabilities:  * [CVE-2025-24928](https://nvd.nist.gov/vuln/detail/CVE-2025-24928) * [CVE-2025-24855](https://nvd.nist.gov/vuln/detail/CVE-2025-24855) * [CVE-2025-0306](https://nvd.nist.gov/vuln/detail/CVE-2025-0306) * [CVE-2024-56171](https://nvd.nist.gov/vuln/detail/CVE-2024-56171) * [CVE-2024-55549](https://nvd.nist.gov/vuln/detail/CVE-2024-55549) |
| **N/A** | **Security fixes for `apigee-redis`.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142))  This addresses the following vulnerabilities:  * [CVE-2025-22869](https://nvd.nist.gov/vuln/detail/CVE-2025-22869) * [CVE-2024-56171](https://nvd.nist.gov/vuln/detail/CVE-2024-56171) * [CVE-2024-24791](https://nvd.nist.gov/vuln/detail/CVE-2024-24791) |
| **N/A** | **Security fixes for `apigee-prometheus-adapter`.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142))  This addresses the following vulnerability:  * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868) |
| **N/A** | **Security fixes for `apigee-prometheus-adapter`.** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141))  This addresses the following vulnerabilities:  * [CVE-2024-45338](https://nvd.nist.gov/vuln/detail/CVE-2024-45338) * [CVE-2024-45337](https://nvd.nist.gov/vuln/detail/CVE-2024-45337) |
| **N/A** | **Security fixes for `apigee-operators`.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142))  This addresses the following vulnerabilities:  * [CVE-2025-22869](https://nvd.nist.gov/vuln/detail/CVE-2025-22869) * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868) |
| **N/A** | **Security fixes for `apigee-open-telemetry-collector`.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142))  This addresses the following vulnerabilities:  * [CVE-2025-29786](https://nvd.nist.gov/vuln/detail/CVE-2025-29786) * [CVE-2025-22869](https://nvd.nist.gov/vuln/detail/CVE-2025-22869) * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868) |
| **N/A** | **Security fixes for `apigee-open-telemetry-collector`.** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141))  This addresses the following vulnerability:  * [CVE-2024-45338](https://nvd.nist.gov/vuln/detail/CVE-2024-45338) |
| **N/A** | **Security fixes for `apigee-mint-task-scheduler`.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142))  This addresses the following vulnerability:  * [CVE-2025-21587](https://nvd.nist.gov/vuln/detail/CVE-2025-21587) |
| **N/A** | **Security fixes for `apigee-mint-task-scheduler`.** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141))  This addresses the following vulnerabilities:  * [CVE-2025-24970](https://nvd.nist.gov/vuln/detail/CVE-2025-24970) * [CVE-2024-47535](https://nvd.nist.gov/vuln/detail/CVE-2024-47535) |
| **N/A** | **Security fixes for `apigee-mint-task-scheduler`.** (Fixed in [v1.13.3](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1133))  This addresses the following vulnerability:  * [CVE-2024-47535](https://nvd.nist.gov/vuln/detail/CVE-2024-47535) |
| **N/A** | **Security fixes for `apigee-kube-rbac-proxy`.** (Fixed in [v1.13.3](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1133))  This addresses the following vulnerabilities:  * [CVE-2024-24790](https://nvd.nist.gov/vuln/detail/CVE-2024-24790) * [CVE-2019-9192](https://nvd.nist.gov/vuln/detail/CVE-2019-9192) * [CVE-2019-1010023](https://nvd.nist.gov/vuln/detail/CVE-2019-1010023) * [CVE-2019-1010022](https://nvd.nist.gov/vuln/detail/CVE-2019-1010022) * [CVE-2018-20796](https://nvd.nist.gov/vuln/detail/CVE-2018-20796) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra`.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142))  This addresses the following vulnerability:  * [CVE-2025-23015](https://nvd.nist.gov/vuln/detail/CVE-2025-23015) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra`.** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141))  This addresses the following vulnerability:  * [CVE-2023-37920](https://nvd.nist.gov/vuln/detail/CVE-2023-37920) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra`.** (Fixed in [v1.13.3](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1133))  This addresses the following vulnerability:  * [CVE-2024-9287](https://nvd.nist.gov/vuln/detail/CVE-2024-9287) |
| **N/A** | **Security fixes for `apigee-hybrid-cassandra-client`.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142))  This addresses the following vulnerability:  * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868) |
| **N/A** | **Security fixes for `apigee-fluent-bit`.** (Fixed in [v1.14.2](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1142))  This addresses the following vulnerabilities:  * [CVE-2025-1094](https://nvd.nist.gov/vuln/detail/CVE-2025-1094) * [CVE-2025-0395](https://nvd.nist.gov/vuln/detail/CVE-2025-0395) |
| **N/A** | **Security fixes for `apigee-fluent-bit`.** (Fixed in [v1.13.3](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1133))  This addresses the following vulnerability:  * [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979) |
| **N/A** | **Security fixes for `apigee-asm-istiod`.** (Fixed in [v1.14.1](https://cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141))  This addresses the following vulnerability:  * [CVE-2024-45338](https://nvd.nist.gov/vuln/detail/CVE-2024-45338) |

---
## 2025-05-29

### Announcement

On May 29, 2025 we announced the shutdown schedule for the Apigee Classic UI.

### Deprecated

The Apigee Classic UI will be shutdown as of August 29, 2025.

This is the final phase of moving Apigee to the Google Cloud console. Apigee in the Google Cloud console gives you the ability to manage all of your Apigee functionality in one place.

To prepare for the shutdown of the Apigee Classic UI, familiarize yourself with the new Apigee UI in Google Cloud console by reviewing [UI overview](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview).

See [Apigee Classic UI shutdown](https://cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates and exception request.

---
