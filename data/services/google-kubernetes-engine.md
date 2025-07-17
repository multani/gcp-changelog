# Google Kubernetes Engine

## 2025-07-16

### Changed

To enable upcoming support for mTLS and client certificates, Google Front Ends
(GFEs) that power GKE DNS-based control plane public endpoints will add client
certificate requests during the TLS handshake. Requests are already incorporated
into GKE DNS-based control plane public endpoints where hostnames end with
`us-central1.gke.goog`. For all other GKE DNS-based control plane public
endpoints, this will roll out between August 18, 2025 and August 22, 2025.

Until mTLS and client certificate configuration options are available, the
following details apply:

* A client certificate request in a TLS handshake *doesn't* mean that `kubectl`
  (or other compatible clients) must provide a client certificate. Client
  certificates are neither mandatory nor configurable.
* TLS libraries in current operating systems send a "no client certificate"
  response to the public endpoint's client certificate request.
* GKE DNS-based control plane public endpoints will **not** enforce client
  certificates or mTLS requirements until a future announcement about
  configuration options.

If you use an intermediate proxy between `kubectl` (or other compatible
clients) and a GKE DNS-based control plane public endpoint, ensure that it fully
adheres to
[Section 7.4.4 of RFC 5246](https://datatracker.ietf.org/doc/html/rfc5246#section-7.4.4),
[Section 4.4.2 of RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446#section-4.4.2),
or
[Section 4.4.2.4 of RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446#section-4.4.2.4).

Vertex AI
---------

### Feature

Added [Gemma 3](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_axolotl_gemma3_finetuning.ipynb) fine-tuning notebook using Axolotl docker with support for 1b, 4b, 12b, and 27b variants.

---
## 2025-07-14

### Fixed

Windows NVMe attached disks are supported only in GKE version
1.33.2-gke.1240000 and later. In earlier GKE versions, creating
PersistentVolumeClaims on Windows nodes that use NVMe volumes results in errors.
For more information about the disk interface types that are used by machine
families, see the Compute Engine
[Machine series comparison](https://cloud.google.com/compute/docs/machine-resource#machine_type_comparison).

If you have Windows workloads that use machine families that support only NVMe,
upgrade your clusters to version 1.33.2-gke.1240000 or later.

Pub/Sub
-------

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.31.0](https://github.com/googleapis/python-pubsub/compare/v2.30.0...v2.31.0) (2025-06-26)

##### Features

* Add MessageTransformationFailureReason to IngestionFailureEvent ([#1427](https://github.com/googleapis/python-pubsub/issues/1427)) ([8ab13e1](https://github.com/googleapis/python-pubsub/commit/8ab13e1b71c151f0146548e7224dd38c9d719a88))

##### Bug Fixes

* Surface Fatal Stream Errors to Future; Adjust Retryable Error Codes ([#1422](https://github.com/googleapis/python-pubsub/issues/1422)) ([e081beb](https://github.com/googleapis/python-pubsub/commit/e081beb29056035304d365ec9c50fa7ffbac6886))

Security Command Center
-----------------------

### Changed

In the [Google Kubernetes Engine (GKE) security posture dashboard](https://cloud.google.com/security-command-center/docs/concepts-security-sources#gke-security-posture-dashboard), the software vulnerabilities pane is available in [Preview](https://cloud.google.com/products#product-launch-stages), not General Availability.

Spanner
-------

### Feature

[Spanner Data Boost](https://cloud.google.com/spanner/docs/databoost/databoost-overview) supports data stored on hard disk drives (HDD). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

VPC Service Controls
--------------------

### Feature

[Preview stage](https://cloud.google.com/products#product-launch-stages) support for the following integration:

* [Address Validation API](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_address_validation)
* [Places (New) API](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_places_new)

Vertex AI
---------

### Feature

[Multimodal MedGemma 27B IT](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/medgemma;publisherModelVersion=medgemma-27b-it), [MedSigLIP](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/medsiglip), and [T5Gemma](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/t5gemma) models are available through Model Garden.

---
## 2025-07-11

### Changed

#### (2025-R29) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are
already in progress when we publish the release notes, and can take multiple
days to complete across all Google Cloud zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2461000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1614000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

    Security Command Center
    -----------------------

    ### Feature

    [Notebook Security Scanner](https://cloud.google.com/security-command-center/docs/concepts-security-sources#notebook-security-scanner) is a built-in package vulnerability detection service of Security Command Center. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages) to the Security Command Center Premium or Enterprise tier.

    You can enable and use Notebook Security Scanner to detect vulnerabilities in Python packages that are used in Colab Enterprise notebooks (files with the `ipynb` filename extension) and resolve those package vulnerability findings.

    Vertex AI
    ---------

    ### Feature

    To reduce the cost of running your inference jobs, you can now use flex-start VMs, which are powered by [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler). Flex-start VMs offer significant discounts and are well-suited for
    short-duration workloads. This feature is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

    For more information, see [Use DWS flex-start VMs with inference](https://cloud.google.com/vertex-ai/docs/predictions/use-flex-start-vms).

---
## 2025-07-02

### Changed

#### (2025-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1607000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)

---
## 2025-06-27

### Changed

#### (2025-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2445000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1594000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Extended channel:
  + 1.27.16-gke.2820000
  + 1.27.16-gke.2853000
  + 1.27.16-gke.2894000

---
## 2025-06-25

### Feature

The C4D machine series is generally available in GKE. The following version requirements apply:

* Standard clusters:
  + Manual node creation: GKE version 1.30 and later.
  + Node auto-provisioning and cluster autoscaler with Confidential GKE Nodes and compact placement: GKE version 1.32.3-gke.1717000 and later.
* Autopilot clusters, including compact placement:
  + C4D machine types without Titanium SSD: GKE version 1.33.0-gke.1439000 and later.
  + C4D machine types with Titanium SSD: GKE version 1.33.1-gke.1171000 and later.

You can use the C4D machine series with Confidential GKE Nodes and in compact placement policies in Autopilot and Standard clusters.

For more information, see [C4D machine series](https://cloud.google.com/compute/docs/general-purpose-machines#c4d_series).

---
## 2025-06-24

### Changed

Starting on September 1, 2025, GKE version upgrades can proceed even if existing resources violate custom organization policy constraints. GKE allows upgrade-only operations to occur as long as the operation doesn't introduce new policy violations.

---
## 2025-06-18

### Changed

#### (2025-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.27.16-gke.2853000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.27.16-gke.2894000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2380000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2428000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1493000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1549000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Extended channel:
  + 1.27.16-gke.2810000
  + 1.27.16-gke.2874000
  + 1.28.15-gke.2287000
  + 1.28.15-gke.2403000
  + 1.29.15-gke.1395000
  + 1.29.15-gke.1523000
  + 1.30.12-gke.1151000
  + 1.31.9-gke.1005000
  + 1.32.4-gke.1353003
  + 1.33.0-gke.2248000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2303000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.27.16-gke.2820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2303000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.

---
## 2025-06-16

### Feature

For clusters running GKE version 1.32.4-gke.1236000 or later, the cluster autoscaler can scale down nodes by evicting Pods in the kube-system namespace that have no Pod Disruption Budget (PDB) set and have been running for at least one hour.

### Feature

For clusters running GKE version 1.32.4-gke.1236000 or later, the cluster autoscaler can scale down nodes by evicting Pods in the kube-system namespace that have no Pod Disruption Budget (PDB) set and have been running for at least one hour.

---
## 2025-06-12

### Changed

#### (2025-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.27.16-gke.2820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.27.16-gke.2874000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2303000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2403000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1523000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Extended channel:
  + 1.27.16-gke.2771000
  + 1.27.16-gke.2853000
  + 1.28.15-gke.2239000
  + 1.28.15-gke.2380000
  + 1.29.15-gke.1325000
  + 1.29.15-gke.1493000
  + 1.30.12-gke.1086000
  + 1.31.8-gke.1113000
  + 1.32.4-gke.1236007
  + 1.32.4-gke.1353001
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.27.16-gke.2810000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1395000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Changed

#### (2025-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1545000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following node versions are now available:
  + [1.27.16-gke.2874000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2403000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1523000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1545000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available:
  + 1.30.11-gke.1217000
  + 1.31.7-gke.1390000
  + 1.32.4-gke.1106006
  + 1.32.4-gke.1353001
  + 1.32.4-gke.1415001
  + 1.32.4-gke.1533000
  + 1.33.1-gke.1375000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Changed

#### (2025-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1545000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1151000
  + 1.31.9-gke.1005000
  + 1.32.4-gke.1353001
  + 1.32.4-gke.1415001
  + 1.32.4-gke.1533000
  + 1.33.0-gke.2248000
  + 1.33.1-gke.1107000
  + 1.33.1-gke.1375000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.

### Changed

#### (2025-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1086000
  + 1.31.8-gke.1113000
  + 1.32.4-gke.1236007
  + 1.32.4-gke.1353001
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Changed

#### (2025-R25) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
* The following versions are no longer available in the Stable channel:
  + 1.30.11-gke.1217000
  + 1.31.7-gke.1390000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.

### Changed

#### (2025-R25) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
and [Upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1545000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1151000
  + 1.31.9-gke.1005000
  + 1.32.4-gke.1353001
  + 1.32.4-gke.1415001
  + 1.32.4-gke.1533000
  + 1.33.0-gke.2248000
  + 1.33.1-gke.1107000
  + 1.33.1-gke.1375000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.

### Regular channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1086000
  + 1.31.8-gke.1113000
  + 1.32.4-gke.1236007
  + 1.32.4-gke.1353001
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Stable channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
* The following versions are no longer available in the Stable channel:
  + 1.30.11-gke.1217000
  + 1.31.7-gke.1390000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.

### Extended channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.27.16-gke.2820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.27.16-gke.2874000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2303000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2403000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1523000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Extended channel:
  + 1.27.16-gke.2771000
  + 1.27.16-gke.2853000
  + 1.28.15-gke.2239000
  + 1.28.15-gke.2380000
  + 1.29.15-gke.1325000
  + 1.29.15-gke.1493000
  + 1.30.12-gke.1086000
  + 1.31.8-gke.1113000
  + 1.32.4-gke.1236007
  + 1.32.4-gke.1353001
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.27.16-gke.2810000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1395000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### No channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1545000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following node versions are now available:
  + [1.27.16-gke.2874000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2403000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1523000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1545000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available:
  + 1.30.11-gke.1217000
  + 1.31.7-gke.1390000
  + 1.32.4-gke.1106006
  + 1.32.4-gke.1353001
  + 1.32.4-gke.1415001
  + 1.32.4-gke.1533000
  + 1.33.1-gke.1375000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1353003](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

---
## 2025-06-10

### Feature

GKE now reports CPU and memory requests and limits [metrics](https://cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes-kubernetes) for Kubernetes-native [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) starting from GKE version 1.32.4-gke.1106006.

### Feature

Flex-start provisioning mode on GKE now supports TPUs in single-host node pools. Flex-start makes accessing highly-demanded accelerators, like TPU v5e, v5p, and Trillium easier while optimizing their utilization. To learn more, see [About GPU and TPU provisioning with flex-start provisioning mode](https://cloud.google.com/kubernetes-engine/docs/concepts/dws).

### Feature

GKE now reports CPU and memory requests and limits [metrics](https://cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes-kubernetes) for Kubernetes-native [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) starting from GKE version 1.32.4-gke.1106006.

### Feature

Flex-start provisioning mode on GKE now supports TPUs in single-host node pools. Flex-start makes accessing highly-demanded accelerators, like TPU v5e, v5p, and Trillium easier while optimizing their utilization. To learn more, see [About GPU and TPU provisioning with flex-start provisioning mode](https://cloud.google.com/kubernetes-engine/docs/concepts/dws).

---
## 2025-06-05

### Changed

#### (2025-R24) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
and [Upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1533000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1375000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Rapid channel:
  + 1.31.8-gke.1113000
  + 1.31.9-gke.1044000
  + 1.32.4-gke.1236006
  + 1.32.4-gke.1353000
  + 1.32.4-gke.1415000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Regular channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1033000
  + 1.31.8-gke.1045000
  + 1.32.4-gke.1106006
  + 1.32.4-gke.1236006
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.

### Stable channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
* The following versions are no longer available in the Stable channel:
  + 1.30.11-gke.1157000
  + 1.31.7-gke.1265000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.

### Extended channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.27.16-gke.2810000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.27.16-gke.2853000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2380000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1395000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1493000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
* The following versions are no longer available in the Extended channel:
  + 1.27.16-gke.2732000
  + 1.27.16-gke.2820000
  + 1.28.15-gke.2192000
  + 1.28.15-gke.2303000
  + 1.29.15-gke.1274000
  + 1.29.15-gke.1415000
  + 1.30.12-gke.1033000
  + 1.31.8-gke.1045000
  + 1.32.4-gke.1106006
  + 1.32.4-gke.1236006
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.27.16-gke.2771000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.

### No channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1533000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
  + [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1375000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following node versions are now available:
  + [1.27.16-gke.2853000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2380000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1493000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1533000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
  + [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1375000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available:
  + 1.30.11-gke.1157000
  + 1.31.7-gke.1265000
  + 1.31.9-gke.1044000
  + 1.32.3-gke.1927009
  + 1.32.4-gke.1236006
  + 1.32.4-gke.1353000
  + 1.32.4-gke.1415000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.

### Changed

#### (2025-R23) Version updates

There are no version updates for 2025-R23.

### Changed

#### (2025-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1533000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1375000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Rapid channel:
  + 1.31.8-gke.1113000
  + 1.31.9-gke.1044000
  + 1.32.4-gke.1236006
  + 1.32.4-gke.1353000
  + 1.32.4-gke.1415000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Changed

#### (2025-R23) Version updates

There are no version updates for 2025-R23.

### Changed

#### (2025-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1033000
  + 1.31.8-gke.1045000
  + 1.32.4-gke.1106006
  + 1.32.4-gke.1236006
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.

### Changed

#### (2025-R23) Version updates

There are no version updates for 2025-R23.

### Changed

#### (2025-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
* The following versions are no longer available in the Stable channel:
  + 1.30.11-gke.1157000
  + 1.31.7-gke.1265000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.

### Changed

#### (2025-R23) Version updates

There are no version updates for 2025-R23.

### Changed

#### (2025-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.27.16-gke.2810000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.27.16-gke.2853000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2380000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1395000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1493000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
* The following versions are no longer available in the Extended channel:
  + 1.27.16-gke.2732000
  + 1.27.16-gke.2820000
  + 1.28.15-gke.2192000
  + 1.28.15-gke.2303000
  + 1.29.15-gke.1274000
  + 1.29.15-gke.1415000
  + 1.30.12-gke.1033000
  + 1.31.8-gke.1045000
  + 1.32.4-gke.1106006
  + 1.32.4-gke.1236006
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.27.16-gke.2771000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.

### Changed

#### (2025-R23) Version updates

There are no version updates for 2025-R23.

### Changed

#### (2025-R24) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1533000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
  + [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1375000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following node versions are now available:
  + [1.27.16-gke.2853000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2380000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1493000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1353001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1415001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.32.4-gke.1533000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330)
  + [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1375000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available:
  + 1.30.11-gke.1157000
  + 1.31.7-gke.1265000
  + 1.31.9-gke.1044000
  + 1.32.3-gke.1927009
  + 1.32.4-gke.1236006
  + 1.32.4-gke.1353000
  + 1.32.4-gke.1415000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1236007](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.

### Changed

#### (2025-R23) Version updates

There are no version updates for 2025-R23.

---
## 2025-05-30

### Changed

#### (2025-R22) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
and [Upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1086000
  + 1.31.9-gke.1005000
  + 1.33.0-gke.1868000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.

### Regular channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
  + [1.32.4-gke.1236006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
* The following versions are no longer available in the Regular channel:
  + 1.30.11-gke.1217000
  + 1.31.7-gke.1390000
  + 1.32.3-gke.1927009
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Stable channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
  + [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
* The following versions are no longer available in the Stable channel:
  + 1.30.11-gke.1131000
  + 1.31.7-gke.1212000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.

### Extended channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.27.16-gke.2771000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.27.16-gke.2820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2303000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
  + [1.32.4-gke.1236006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
* The following versions are no longer available in the Extended channel:
  + 1.27.16-gke.2703000
  + 1.27.16-gke.2810000
  + 1.28.15-gke.2169000
  + 1.28.15-gke.2287000
  + 1.29.15-gke.1240000
  + 1.29.15-gke.1395000
  + 1.30.11-gke.1217000
  + 1.31.7-gke.1390000
  + 1.32.3-gke.1927009
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2192000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.27.16-gke.2732000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2192000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### No channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
* The following node versions are now available:
  + [1.27.16-gke.2820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2303000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
* The following versions are no longer available:
  + 1.30.11-gke.1131000
  + 1.31.7-gke.1212000
  + 1.31.9-gke.1005000
  + 1.32.3-gke.1785003
  + 1.32.4-gke.1106000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Changed

The insecure kubelet read-only port (`10255`) is disabled by default in all new clusters that run GKE version 1.32 and later. If you created your cluster using a GKE version earlier than 1.32, we recommend that you disable the insecure kubelet read-only port. For more information see [Disable the kubelet read-only port in GKE clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port).

### Changed

#### (2025-R21) Version updates

There are no version updates for 2025-R21.

### Changed

#### (2025-R22) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.11-gke.1217000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011)
  + [1.31.7-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317)
* The following versions are no longer available in the Stable channel:
  + 1.30.11-gke.1131000
  + 1.31.7-gke.1212000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.11-gke.1157000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13011) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.

### Changed

#### (2025-R22) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
  + [1.32.4-gke.1236006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
* The following versions are no longer available in the Regular channel:
  + 1.30.11-gke.1217000
  + 1.31.7-gke.1390000
  + 1.32.3-gke.1927009
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Changed

#### (2025-R22) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1086000
  + 1.31.9-gke.1005000
  + 1.33.0-gke.1868000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.0-gke.2248000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1330) with this release.

### Changed

#### (2025-R22) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
* The following node versions are now available:
  + [1.27.16-gke.2820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2303000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
* The following versions are no longer available:
  + 1.30.11-gke.1131000
  + 1.31.7-gke.1212000
  + 1.31.9-gke.1005000
  + 1.32.3-gke.1785003
  + 1.32.4-gke.1106000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.7-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1317) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Changed

#### (2025-R22) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.27.16-gke.2771000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.27.16-gke.2820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2303000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318)
  + [1.32.4-gke.1236006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
* The following versions are no longer available in the Extended channel:
  + 1.27.16-gke.2703000
  + 1.27.16-gke.2810000
  + 1.28.15-gke.2169000
  + 1.28.15-gke.2287000
  + 1.29.15-gke.1240000
  + 1.29.15-gke.1395000
  + 1.30.11-gke.1217000
  + 1.31.7-gke.1390000
  + 1.32.3-gke.1927009
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2192000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.27.16-gke.2732000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2192000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1274000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.8-gke.1045000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.4-gke.1106006](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Feature

GKE now provides insights and recommendations that help you to [identify and remediate](https://cloud.google.com/kubernetes-engine/docs/troubleshooting/scalability#identify-fix-etcd-usage) clusters where the etcd cluster state database size is approaching the limit. Implementing the recommendation helps you to keep your clusters stable and performant.

---
## 2025-05-27

### Feature

In GKE version 1.32.2-gke.1297000 and later, you can run GPU workloads on Confidential GKE Nodes with the [A3 High machine type](https://cloud.google.com/compute/docs/accelerator-optimized-machines#a3-standard-vms) and NVIDIA H100 GPUs. This enables stronger data protection and integrity for GPU-accelerated computations running within GKE clusters and nodes. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Encrypt GPU workload data in use with Confidential GKE Nodes](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes).

### Feature

In GKE version 1.32.2-gke.1297000 and later, you can use the Intel TDX and AMD SEV-SNP [Confidential Computing technologies](https://cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with Confidential GKE Nodes. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages). Use Confidential GKE Nodes to encrypt your workload data in-use through Compute Engine Confidential VMs for data and code confidentiality and integrity. For more information, see [Encrypt workload data in-use with Confidential GKE Nodes](https://cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes).

---
