# Google Kubernetes Engine

## 2025-10-29

### Changed

#### (2025-R45) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.1-gke.2037000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
* The following versions are no longer available in the Rapid channel:
  + 1.31.13-gke.1040000
  + 1.32.9-gke.1130000
  + 1.33.5-gke.1201000
  + 1.34.0-gke.2201000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    - 1.33 to [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    - 1.34 to [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Regular channel:
  + 1.31.13-gke.1008000
  + 1.32.9-gke.1092000
  + 1.33.5-gke.1125000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Stable channel:
  + 1.31.12-gke.1220000
  + 1.32.9-gke.1010000
  + 1.33.4-gke.1350000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2857000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.2002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.2109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1349000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.30.14-gke.1426000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2740000
  + 1.28.15-gke.2793000
  + 1.29.15-gke.1979000
  + 1.29.15-gke.2085000
  + 1.30.14-gke.1267000
  + 1.30.14-gke.1408000
  + 1.31.13-gke.1008000
  + 1.32.9-gke.1092000
  + 1.33.5-gke.1125000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.27 to [1.28.15-gke.2751000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.28 to [1.28.15-gke.2751000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    - 1.29 to [1.29.15-gke.1989000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    - 1.30 to [1.30.14-gke.1336000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    - 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
* The following versions are now available:
  + [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2857000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.2109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1426000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.31.12-gke.1220000
  + 1.32.9-gke.1010000
  + 1.33.4-gke.1245000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Security

#### (2025-R45) Security updates

This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:

| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.33.5-gke.1350000 | cos-121-18867-199-105 | [cos-121-18867-199-105 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-199-105_) |
| 1.34.1-gke.2037000 | cos-125-19216-0-94 | [cos-125-19216-0-94 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-0-94_) |

### Changed

#### (2025-R45) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2857000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.2002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.2109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1349000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.30.14-gke.1426000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2740000
  + 1.28.15-gke.2793000
  + 1.29.15-gke.1979000
  + 1.29.15-gke.2085000
  + 1.30.14-gke.1267000
  + 1.30.14-gke.1408000
  + 1.31.13-gke.1008000
  + 1.32.9-gke.1092000
  + 1.33.5-gke.1125000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.27 to [1.28.15-gke.2751000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.28 to [1.28.15-gke.2751000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    - 1.29 to [1.29.15-gke.1989000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    - 1.30 to [1.30.14-gke.1336000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    - 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Changed

#### (2025-R45) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
* The following versions are now available:
  + [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2857000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.2109000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1426000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.31.12-gke.1220000
  + 1.32.9-gke.1010000
  + 1.33.4-gke.1245000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Changed

#### (2025-R45) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.31.13-gke.1139000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1239000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.1-gke.2037000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
* The following versions are no longer available in the Rapid channel:
  + 1.31.13-gke.1040000
  + 1.32.9-gke.1130000
  + 1.33.5-gke.1201000
  + 1.34.0-gke.2201000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    - 1.33 to [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    - 1.34 to [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)

### Changed

#### (2025-R45) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Regular channel:
  + 1.31.13-gke.1008000
  + 1.32.9-gke.1092000
  + 1.33.5-gke.1125000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Changed

#### (2025-R45) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Stable channel:
  + 1.31.12-gke.1220000
  + 1.32.9-gke.1010000
  + 1.33.4-gke.1350000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

---
## 2025-10-28

### Feature

Autoscaled blue-green upgrades are a type of node upgrade strategy that
maximizes the amount of time before disruption-intolerant workloads are evicted,
while minimizing cost. This feature is available in Preview for
GKE Standard node pools. For more information, see
[Autoscaled blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#autoscaled-blue-green-upgrade-strategy).

### Feature

You can use the G4 VM, powered by NVIDIA's RTX PRO 6000 GPUs, with
GKE Autopilot in version 1.34.1-gke.1829001 or later. To
get started, see [Deploy GPU workloads in
Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).

---
## 2025-10-22

### Changed

#### (2025-R44) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
  + [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
* The following versions are no longer available in the Rapid channel:
  + 1.31.13-gke.1023000
  + 1.32.9-gke.1108000
  + 1.33.5-gke.1162000
  + 1.34.1-gke.1293000
  + 1.34.1-gke.1431000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    - 1.34 to [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Regular channel:
  + 1.31.12-gke.1265000
  + 1.32.9-gke.1072000
  + 1.33.5-gke.1080000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Stable channel:
  + 1.31.11-gke.1036000
  + 1.32.8-gke.1170000
  + 1.33.4-gke.1245000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2751000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2793000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1989000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.2085000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1336000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.30.14-gke.1408000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2730000
  + 1.28.15-gke.2767000
  + 1.29.15-gke.1971000
  + 1.29.15-gke.2002000
  + 1.30.14-gke.1150000
  + 1.30.14-gke.1349000
  + 1.31.12-gke.1265000
  + 1.32.9-gke.1072000
  + 1.33.5-gke.1080000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.27 to [1.28.15-gke.2740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.28 to [1.28.15-gke.2740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    - 1.29 to [1.29.15-gke.1979000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    - 1.30 to [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    - 1.31 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
* The following versions are now available:
  + [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2793000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.2085000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1408000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.31.11-gke.1036000
  + 1.32.8-gke.1170000
  + 1.33.4-gke.1172000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Security

#### (2025-R44) Security updates

This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:

| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.28.15-gke.2793000 | cos-113-18244-448-63 | [cos-113-18244-448-63 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113#cos-113-18244-448-63_) |
| 1.29.15-gke.2085000 | cos-113-18244-448-63 | [cos-113-18244-448-63 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113#cos-113-18244-448-63_) |
| 1.30.14-gke.1408000 | cos-113-18244-448-63 | [cos-113-18244-448-63 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113#cos-113-18244-448-63_) |
| 1.31.13-gke.1123000 | cos-117-18613-339-84 | [cos-117-18613-339-84 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-339-84_) |
| 1.32.9-gke.1207000 | cos-117-18613-339-84 | [cos-117-18613-339-84 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-339-84_) |
| 1.33.5-gke.1308000 | cos-121-18867-199-88 | [cos-121-18867-199-88 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-199-88_) |
| 1.34.0-gke.2201000 | cos-121-18867-199-28 | [cos-121-18867-199-28 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-199-28_) |
| 1.34.1-gke.1829001 | cos-125-19216-0-94 | [cos-125-19216-0-94 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-125-19216-0-94_) |

### Changed

#### (2025-R44) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2751000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2793000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1989000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.2085000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1336000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.30.14-gke.1408000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2730000
  + 1.28.15-gke.2767000
  + 1.29.15-gke.1971000
  + 1.29.15-gke.2002000
  + 1.30.14-gke.1150000
  + 1.30.14-gke.1349000
  + 1.31.12-gke.1265000
  + 1.32.9-gke.1072000
  + 1.33.5-gke.1080000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.27 to [1.28.15-gke.2740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.28 to [1.28.15-gke.2740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    - 1.29 to [1.29.15-gke.1979000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    - 1.30 to [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
    - 1.31 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Changed

#### (2025-R44) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
* The following versions are now available:
  + [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2793000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.2085000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1408000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.31.11-gke.1036000
  + 1.32.8-gke.1170000
  + 1.33.4-gke.1172000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Changed

#### (2025-R44) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.31.13-gke.1123000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1207000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1308000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
  + [1.34.1-gke.1829001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
* The following versions are no longer available in the Rapid channel:
  + 1.31.13-gke.1023000
  + 1.32.9-gke.1108000
  + 1.33.5-gke.1162000
  + 1.34.1-gke.1293000
  + 1.34.1-gke.1431000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    - 1.34 to [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)

### Changed

#### (2025-R44) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Regular channel:
  + 1.31.12-gke.1265000
  + 1.32.9-gke.1072000
  + 1.33.5-gke.1080000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Changed

#### (2025-R44) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Stable channel:
  + 1.31.11-gke.1036000
  + 1.32.8-gke.1170000
  + 1.33.4-gke.1245000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

---
## 2025-10-21

### Feature

The G4 VM, powered by NVIDIA's RTX PRO 6000 Blackwell Server Edition GPUs with
the AMD EPYC Turin CPU platform, is generally available on GKE.
G4 instances have up to 384 vCPUs, 1,440 GB of memory, 12 TiB of Titanium SSD
disks attached, and up to 400 Gbps of standard network performance. The G4 VM
offers a leap in performance with up to 9 times the throughput of G2 instances
for workloads such as AI development, and graphics rendering. G4 VMs are
currently available with 1, 2, 4, or 8 GPUs.

* For GKE Standard, use GKE version
  1.34.0-gke.1662000 or later. To get started, see [Run GPUs in
  GKE Standard node
  pools](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus).

---
## 2025-10-17

### Issue

Don't use GKE version 1.34.1-gke.1431000 or later when creating
or upgrading node pools with the
[`a3-highgpu-8g`](https://cloud.google.com/compute/docs/gpus#h100-gpus) machine
type. GKE nodes with these versions include COS Milestone 125,
which has an updated Linux kernel version that is incompatible with
[GPUDirect-TCPX](https://cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx).

---
## 2025-10-15

### Changed

#### (2025-R43) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.34.1-gke.1293000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.1-gke.1431000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
* The following versions are no longer available in the Rapid channel:
  + 1.31.12-gke.1265000
  + 1.31.13-gke.1008000
  + 1.32.9-gke.1072000
  + 1.32.9-gke.1092000
  + 1.33.5-gke.1080000
  + 1.33.5-gke.1125000
  + 1.34.0-gke.2201000
  + 1.34.1-gke.1127000
  + 1.34.1-gke.1279000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    - 1.34 to [1.34.1-gke.1293000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Regular channel:
  + 1.31.12-gke.1220000
  + 1.32.9-gke.1010000
  + 1.33.4-gke.1350000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Stable channel:
  + 1.32.8-gke.1134000
  + 1.33.4-gke.1172000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.31 to [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    - 1.32 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.32 to [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    - 1.33 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1979000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.2002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1349000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2697000
  + 1.28.15-gke.2751000
  + 1.29.15-gke.1936000
  + 1.29.15-gke.1989000
  + 1.30.14-gke.1336000
  + 1.31.12-gke.1220000
  + 1.32.9-gke.1010000
  + 1.33.4-gke.1350000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.27 to [1.28.15-gke.2730000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.28 to [1.28.15-gke.2730000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    - 1.29 to [1.29.15-gke.1971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    - 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
* The following versions are now available:
  + [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.2002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1349000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.32.8-gke.1134000
  + 1.33.4-gke.1134000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Security

#### (2025-R43) Security updates

This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:

| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.34.1-gke.1431000 | cos-beta-125-19216-0-76 | [cos-beta-125-19216-0-76 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125#cos-beta-125-19216-0-76_) |

### Changed

#### (2025-R43) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1979000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.2002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1349000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2697000
  + 1.28.15-gke.2751000
  + 1.29.15-gke.1936000
  + 1.29.15-gke.1989000
  + 1.30.14-gke.1336000
  + 1.31.12-gke.1220000
  + 1.32.9-gke.1010000
  + 1.33.4-gke.1350000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.27 to [1.28.15-gke.2730000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.28 to [1.28.15-gke.2730000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    - 1.29 to [1.29.15-gke.1971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    - 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Changed

#### (2025-R43) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation.
* The following versions are now available:
  + [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.2002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1349000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.32.8-gke.1134000
  + 1.33.4-gke.1134000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Changed

#### (2025-R43) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.34.1-gke.1293000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.31.13-gke.1040000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.1-gke.1431000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
* The following versions are no longer available in the Rapid channel:
  + 1.31.12-gke.1265000
  + 1.31.13-gke.1008000
  + 1.32.9-gke.1072000
  + 1.32.9-gke.1092000
  + 1.33.5-gke.1080000
  + 1.33.5-gke.1125000
  + 1.34.0-gke.2201000
  + 1.34.1-gke.1127000
  + 1.34.1-gke.1279000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.31 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
    - 1.32 to [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
    - 1.34 to [1.34.1-gke.1293000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)

### Changed

#### (2025-R43) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Regular channel:
  + 1.31.12-gke.1220000
  + 1.32.9-gke.1010000
  + 1.33.4-gke.1350000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Changed

#### (2025-R43) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Stable channel:
  + 1.32.8-gke.1134000
  + 1.33.4-gke.1172000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.31 to [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    - 1.32 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.32 to [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    - 1.33 to [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

---
## 2025-10-14

### Issue

In GKE versions 1.32.4-gke.1029000 and later, MountVolume calls
for network file system (NFS) volumes might fail with the following error:
`mount.nfs:rpc.statd is not running but is required for remote locking`.

This failure can occur if a Pod mounting an NFS volume runs on the same node as
an NFS server Pod, and the NFS server Pod starts before the client Pod attempts
to mount the volume. This scenario causes a conflict over the `rpcbind` service,
which prevents the service from starting correctly on the node for the client
Pod, leading to the mount failure.

As a workaround, deploy [this
DaemonSet](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/troubleshooting/nfs-mount-workaround/daemonset.yaml)
on all nodes where you mount the NFS volumes. The DaemonSet ensures that
the required services start correctly.

---
## 2025-10-09

### Feature

For AI models deployed on a GKE cluster, you can view details
about these deployments in the Google Cloud console. The pages include deployment
details, logs, and [observability
dashboards](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring#aiml-dashboard).

### Feature

The following networking features are available:

* In GKE version 1.33.4-gke.1055000 or later, you can control
  how external traffic reaches your Services on GKE clusters by
  using Network Service Tiers. You can configure the network tier to use either
  Standard Tier or Premium Tier when you create or update clusters or when you
  update LoadBalancer Services. For more information, see [Configure external
  traffic with Network Service Tiers](https://cloud.google.com/kubernetes-engine/docs/how-to/network-tiers).
* Starting with GKE versions 1.33 and later, you can enable
  automatic IP address management (auto IPAM) on GKE clusters. Auto
  IPAM dynamically adds or removes additional IP address ranges for nodes and Pods
  as the cluster scales up or down. This feature eliminates the need for large,
  potentially wasteful, upfront IP reservations and manual intervention during
  cluster scaling. For more information, see [Use auto IP address
  management](https://cloud.google.com/kubernetes-engine/docs/how-to/enable-auto-ipam).
* In GKE version 1.30.3-gke.1211000 and later, you can assign
  additional subnets to a VPC-native cluster. Additional subnets
  assigned to a cluster let you create new node pools where IPv4 addresses for
  both nodes and Pods come from the additional subnet ranges. This enhancement
  removes single-subnet limitations, increases scalability, and enhances the
  flexibility of your GKE clusters. For more information, see [Add subnets to
  clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/multi-subnet-cluster).

---
## 2025-10-08

### Changed

#### (2025-R42) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.1-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  + [1.34.1-gke.1293000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1267000
  + 1.30.14-gke.1316000
  + 1.30.14-gke.1325000
  + 1.31.12-gke.1220000
  + 1.32.9-gke.1010000
  + 1.33.4-gke.1350000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1150000
  + 1.30.14-gke.1267000
  + 1.31.11-gke.1036000
  + 1.32.8-gke.1170000
  + 1.33.4-gke.1245000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Stable channel:
  + 1.30.14-gke.1108000
  + 1.30.14-gke.1130000
  + 1.32.8-gke.1108000
  + 1.33.4-gke.1134000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.31 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.32 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    - 1.33 to [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2730000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2751000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1989000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1336000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2630000
  + 1.28.15-gke.2740000
  + 1.29.15-gke.1851000
  + 1.29.15-gke.1979000
  + 1.31.11-gke.1036000
  + 1.32.8-gke.1170000
  + 1.33.4-gke.1245000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.27 to [1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.28 to [1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    - 1.29 to [1.29.15-gke.1936000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    - 1.31 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
* The following versions are now available:
  + [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2751000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1989000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1336000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.30.14-gke.1108000
  + 1.30.14-gke.1130000
  + 1.30.14-gke.1150000
  + 1.30.14-gke.1267000
  + 1.30.14-gke.1316000
  + 1.30.14-gke.1325000
  + 1.32.6-gke.1060000
  + 1.32.8-gke.1108000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    - 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Security

#### (2025-R42) Security updates

This release includes new GKE versions that use updated
Container-Optimized OS images. These updated images are cumulative,
incorporating security fixes from all Container-Optimized OS
versions released since the previous GKE release.

To identify the specific vulnerabilities that were resolved in each updated
Container-Optimized OS image, see the **Security** release notes
for that image. The following table includes links to the release notes for
each updated Container-Optimized OS image:

| GKE version | Container-Optimized OS version | Details |
| --- | --- | --- |
| 1.33.5-gke.1162000 | cos-121-18867-199-80 | [cos-121-18867-199-80 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-199-80_) |
| 1.34.1-gke.1279000 | cos-121-18867-199-80 | [cos-121-18867-199-80 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-199-80_) |
| 1.28.15-gke.2751000 | cos-113-18244-448-58 | [cos-113-18244-448-58 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113#cos-113-18244-448-58_) |
| 1.29.15-gke.1989000 | cos-113-18244-448-58 | [cos-113-18244-448-58 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113#cos-113-18244-448-58_) |
| 1.30.14-gke.1336000 | cos-113-18244-448-58 | [cos-113-18244-448-58 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113#cos-113-18244-448-58_) |
| 1.31.13-gke.1023000 | cos-117-18613-339-77 | [cos-117-18613-339-77 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-339-77_) |
| 1.32.9-gke.1108000 | cos-117-18613-339-77 | [cos-117-18613-339-77 release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-339-77_) |

### Changed

#### (2025-R42) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2730000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2751000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1989000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1336000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2630000
  + 1.28.15-gke.2740000
  + 1.29.15-gke.1851000
  + 1.29.15-gke.1979000
  + 1.31.11-gke.1036000
  + 1.32.8-gke.1170000
  + 1.33.4-gke.1245000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.27 to [1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.28 to [1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
    - 1.29 to [1.29.15-gke.1936000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
    - 1.31 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Changed

#### (2025-R42) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
* The following versions are now available:
  + [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2751000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1989000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1336000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.30.14-gke.1108000
  + 1.30.14-gke.1130000
  + 1.30.14-gke.1150000
  + 1.30.14-gke.1267000
  + 1.30.14-gke.1316000
  + 1.30.14-gke.1325000
  + 1.32.6-gke.1060000
  + 1.32.8-gke.1108000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    - 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Changed

#### (2025-R42) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.31.13-gke.1023000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1162000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.1-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
  + [1.34.1-gke.1293000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1267000
  + 1.30.14-gke.1316000
  + 1.30.14-gke.1325000
  + 1.31.12-gke.1220000
  + 1.32.9-gke.1010000
  + 1.33.4-gke.1350000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)

### Changed

#### (2025-R42) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1150000
  + 1.30.14-gke.1267000
  + 1.31.11-gke.1036000
  + 1.32.8-gke.1170000
  + 1.33.4-gke.1245000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.30 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.31 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.32 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.31 to [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
    - 1.32 to [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
    - 1.33 to [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

### Changed

#### (2025-R42) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Stable channel:
  + 1.30.14-gke.1108000
  + 1.30.14-gke.1130000
  + 1.32.8-gke.1108000
  + 1.33.4-gke.1134000
* Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:
  + GKE upgrades clusters to the following new minor versions if there are no factors, such as [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or deprecated APIs, preventing upgrades:
    - 1.31 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
    - 1.32 to [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
    - 1.33 to [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)

---
## 2025-10-07

### Feature

Starting with GKE version 1.33.2-gke.1240000 and later, you can specify the
network tier (Standard or Premium) for ephemeral IP addresses used by
the `gke-l7-regional-external-managed-mc` GatewayClass. For more information,
see [Configure Network
Tier](https://cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure-network-tier).

---
## 2025-10-02

### Changed

#### (2025-R41) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1936000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1979000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2610000
  + 1.28.15-gke.2730000
  + 1.29.15-gke.1835000
  + 1.29.15-gke.1971000
  + 1.30.14-gke.1130000
  + 1.31.12-gke.1110000
  + 1.32.8-gke.1134000
  + 1.33.4-gke.1172000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1851000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R41) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.14-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1979000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.30.14-gke.1059000
  + 1.31.12-gke.1110000
  + 1.32.6-gke.1025000
  + 1.33.3-gke.1136000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R41) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.1-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
* The following versions are no longer available in the Rapid channel:
  + 1.31.12-gke.1110000
  + 1.32.8-gke.1170000
  + 1.34.0-gke.1662000
  + 1.34.0-gke.2011000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.34 to version [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) with this release.

### Changed

#### (2025-R41) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1130000
  + 1.31.12-gke.1110000
  + 1.32.8-gke.1134000
  + 1.33.4-gke.1172000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R41) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Stable channel:
  + 1.30.14-gke.1059000
  + 1.32.6-gke.1060000
  + 1.33.3-gke.1136000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.33 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R41) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.1-gke.1127000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
* The following versions are no longer available in the Rapid channel:
  + 1.31.12-gke.1110000
  + 1.32.8-gke.1170000
  + 1.34.0-gke.1662000
  + 1.34.0-gke.2011000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.34 to version [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) with this release.

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1130000
  + 1.31.12-gke.1110000
  + 1.32.8-gke.1134000
  + 1.33.4-gke.1172000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Stable channel:
  + 1.30.14-gke.1059000
  + 1.32.6-gke.1060000
  + 1.33.3-gke.1136000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.33 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1936000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1979000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2610000
  + 1.28.15-gke.2730000
  + 1.29.15-gke.1835000
  + 1.29.15-gke.1971000
  + 1.30.14-gke.1130000
  + 1.31.12-gke.1110000
  + 1.32.8-gke.1134000
  + 1.33.4-gke.1172000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1851000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.14-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2740000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1979000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1325000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.13-gke.1008000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13113)
  + [1.32.9-gke.1092000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.30.14-gke.1059000
  + 1.31.12-gke.1110000
  + 1.32.6-gke.1025000
  + 1.33.3-gke.1136000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

---
## 2025-10-01

### Feature

The GKE cluster autoscaler now allows for a significantly longer node drain time. From GKE version 1.32.7-gke.1079000 and later, the graceful node drain timeout has been increased from 10 minutes to 1 hour. For more information, see [How cluster autoscaler works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#how_cluster_autoscaler_works).

### Feature

The [`InPlaceOrRecreate`](https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler#inplaceorrecreate_mode) mode for Vertical Pod Autoscaler (VPA) is now available for Public Preview in GKE.

This mode uses [In-Place Pod Resize (IPPR/IPPU)](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler/enhancements/4016-in-place-updates-support), which allows VPA to automatically adjust workload resources, without requiring Pod recreation. This seamless rightsizing capability helps ensure better service continuity and helps minimize costs by optimizing resource allocation, particularly during idle periods.

VPA is enabled by default in Autopilot clusters. For Standard clusters, you must first enable VPA. For more information on configuring a VPA object, see
[Set Pod resource requests automatically](https://cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#gcloud).

---
## 2025-09-29

### Changed

#### (2025-R40) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2730000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1851000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2599000
  + 1.28.15-gke.2697000
  + 1.29.15-gke.1820000
  + 1.29.15-gke.1936000
  + 1.30.14-gke.1108000
  + 1.31.12-gke.1083000
  + 1.32.8-gke.1108000
  + 1.33.4-gke.1134000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1835000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Feature

To improve security and workload isolation, GKE has introduced a new, dedicated service agent for logging and monitoring of GKE nodes on clusters running version 1.33 and later. For more information, see [GKE service agents](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#gke-service-agents).

#### What's changing?

GKE will now use the following service agent for logging and monitoring on your nodes:

`service-{PROJECT_NUMBER}@gcp-sa-gkenode.iam.gserviceaccount.com`

This service agent has the minimal permissions GKE needs to operate nodes, which are included in the [`role/container.defaultNodeServiceAgent` IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAgent).

Using a dedicated service agent helps to isolate the requirements of GKE-managed workloads from your own workloads.

#### What's the impact?

* This change affects only *GKE system workloads*, which will now use the new service agent for their logging and monitoring capabilities. Your own workloads are not impacted.
* You might notice missing logs or metrics for your nodes if the new service agent doesn't have the necessary permissions.

#### What do I need to do?

In the vast majority of cases, no action is needed, as the role `role/container.defaultNodeServiceAgent` has been automatically granted to the new GKE Node Service Agent on your cluster project.

However, you will need to re-apply the role `role/container.defaultNodeServiceAgent` to the new service agent in the following scenarios:

* You have automation that might have removed this role.
* You notice missing logs or metrics for your nodes.

You can find the full list of permissions for this role in the [IAM documentation](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAgent).

### Changed

#### (2025-R40) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.14-gke.1316000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2730000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1316000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.30.14-gke.1036000
  + 1.31.12-gke.1083000
  + 1.32.8-gke.1026000
  + 1.33.4-gke.1036000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R40) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1316000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1150000
  + 1.33.4-gke.1245000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R40) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1108000
  + 1.31.12-gke.1083000
  + 1.32.8-gke.1108000
  + 1.33.4-gke.1134000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R40) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Stable channel:
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Stable channel:
  + 1.30.14-gke.1036000
  + 1.32.8-gke.1026000
  + 1.33.4-gke.1036000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.

### Changed

#### (2025-R40) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1316000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
  + [1.34.0-gke.2201000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1150000
  + 1.33.4-gke.1245000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1108000
  + 1.31.12-gke.1083000
  + 1.32.8-gke.1108000
  + 1.33.4-gke.1134000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Stable channel:
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Stable channel:
  + 1.30.14-gke.1036000
  + 1.32.8-gke.1026000
  + 1.33.4-gke.1036000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2730000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1851000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2599000
  + 1.28.15-gke.2697000
  + 1.29.15-gke.1820000
  + 1.29.15-gke.1936000
  + 1.30.14-gke.1108000
  + 1.31.12-gke.1083000
  + 1.32.8-gke.1108000
  + 1.33.4-gke.1134000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1835000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.14-gke.1316000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following node versions are now available:
  + [1.28.15-gke.2730000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1971000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1316000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1265000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1072000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.5-gke.1080000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
* The following versions are no longer available:
  + 1.30.14-gke.1036000
  + 1.31.12-gke.1083000
  + 1.32.8-gke.1026000
  + 1.33.4-gke.1036000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

---
## 2025-09-25

### Feature

You can now let GKE auto-create node pools with ComputeClasses without having to enable node auto-provisioning for the entire cluster. This provides more granular control over auto-created node pools, enabling you to target specific workloads and optimize resource usage. For more information, see
[Node auto-provisioning and ComputeClasses](https://cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#autoprovisioning-and-compute-classes).

To use this feature, your cluster must meet both of the following requirements:

* Enrolled in the Rapid release channel.
* Running GKE version 1.33.3-gke.1136000 or later.

### Feature

GKE Standard clusters now support Autopilot features, including the container-optimized compute platform and fully managed nodes, letting you use Autopilot's advantages without migrating to a dedicated Autopilot cluster. For more information, see [Run Autopilot workloads in GKE Standard clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/autopilot-classes-standard-clusters).

To use these features, your cluster must meet the following requirements:

* Enrolled in the Rapid release channel.
* Running GKE version 1.33.1-gke.1107000 or later.

### Issue

**Issue with A4X machine type compatibility on certain GKE versions**

Certain GKE versions are not compatible with the A4X machine type. The issue is that a Container-Optimized OS (COS) image that these GKE versions depend on was not built as a multi-architecture image. This incompatibility causes an `exec format` error on the Arm-based A4X machines. The issue affects GKE versions 1.33.2-gke.1377000 or later, and any versions earlier than 1.33.4-gke.1036000.

---
## 2025-09-23

### Changed

The following metrics are now only billed through Cloud Monitoring. If you were using any of these features through GKE Enterprise, your billing is automatically transitioned to the Cloud Monitoring SKU.

These metrics use [Google Cloud Managed Service for Prometheus](https://cloud.google.com/stackdriver/docs/managed-prometheus) to load metrics into Cloud Monitoring. The Cloud Monitoring charges for the ingestion of these metrics are based on the number of samples ingested. For more information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary).

* [Control Plane Metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics)
* [Kube State Metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics)
* [cAdvisor/Kubelet Metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics)
* [Config Sync Metrics](https://cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/monitoring-config-sync)
* [Policy Controller Metrics](https://cloud.google.com/kubernetes-engine/enterprise/policy-controller/docs/how-to/policy-controller-metrics)

---
## 2025-09-18

### Changed

#### (2025-R39) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1835000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1936000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2564000
  + 1.28.15-gke.2630000
  + 1.29.15-gke.1773000
  + 1.29.15-gke.1851000
  + 1.30.14-gke.1059000
  + 1.31.12-gke.1060000
  + 1.32.8-gke.1026000
  + 1.33.4-gke.1036000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R39) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following node versions are now available:
  + [1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1936000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available:
  + 1.30.14-gke.1011000
  + 1.31.12-gke.1060000
  + 1.32.7-gke.1079000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R39) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.34.0-gke.1662000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + [1.34.0-gke.2011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1130000
  + 1.31.12-gke.1060000
  + 1.31.12-gke.1083000
  + 1.32.8-gke.1108000
  + 1.32.8-gke.1134000
  + 1.33.4-gke.1172000
  + 1.34.0-gke.1477000
  + 1.34.0-gke.1497000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.34 to version [1.34.0-gke.1662000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) with this release.

### Changed

#### (2025-R39) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1059000
  + 1.31.12-gke.1060000
  + 1.32.8-gke.1026000
  + 1.33.4-gke.1036000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R39) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Stable channel:
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Stable channel:
  + 1.30.14-gke.1011000
  + 1.32.7-gke.1079000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.

### Changed

#### (2025-R39) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.34.0-gke.1662000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + [1.34.0-gke.2011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1130000
  + 1.31.12-gke.1060000
  + 1.31.12-gke.1083000
  + 1.32.8-gke.1108000
  + 1.32.8-gke.1134000
  + 1.33.4-gke.1172000
  + 1.34.0-gke.1477000
  + 1.34.0-gke.1497000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.34 to version [1.34.0-gke.1662000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) with this release.

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1059000
  + 1.31.12-gke.1060000
  + 1.32.8-gke.1026000
  + 1.33.4-gke.1036000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Stable channel:
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Stable channel:
  + 1.30.14-gke.1011000
  + 1.32.7-gke.1079000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1835000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1936000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2564000
  + 1.28.15-gke.2630000
  + 1.29.15-gke.1773000
  + 1.29.15-gke.1851000
  + 1.30.14-gke.1059000
  + 1.31.12-gke.1060000
  + 1.32.8-gke.1026000
  + 1.33.4-gke.1036000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following node versions are now available:
  + [1.28.15-gke.2697000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1936000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1267000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1220000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.9-gke.1010000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
  + [1.33.4-gke.1350000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available:
  + 1.30.14-gke.1011000
  + 1.31.12-gke.1060000
  + 1.32.7-gke.1079000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

---
## 2025-09-11

### Feature

GKE now provisions fast-starting nodes, which have significantly lower startup time, in Autopilot mode for G2 nodes with NVIDIA L4 GPUs. Fast-starting nodes are in Public Preview for clusters in the Rapid channel, and are available on a best-effort basis when workloads use compatible configurations. For more information, see [About quicker workload startup with fast-starting nodes](https://cloud.google.com/kubernetes-engine/docs/concepts/fast-starting-nodes).

### Feature

The accelerator-optimized A4X VM, an exascale platform based on [NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), is now Generally Available on GKE. A4X is the first GPU VM to run on Arm with the NVIDIA GB200 Grace Blackwell Superchips. You can use A4X to run your large artificial intelligence (AI) models, machine learning (ML), and high performance computing (HPC) workloads.

**Important:** Updated on September 25, 2025. The GKE version support for the A4X machine series in this feature note was listed incorrectly. For more information, see the **Issue** published on [September 25, 2025](https://cloud.google.com/kubernetes-engine/docs/release-notes#September_25_2025). The correct versions are now listed as follows.

The A4X machine type is available as `a4x-highgpu-4g` in the us-central1-a zone with the following GKE versions:

* For GKE Standard 1.32, use 1.32.8-gke.1108000 or later.
* For GKE Autopilot 1.33, use 1.33.4-gke.1036000 or later.

To create GKE clusters with A4X, see the following instructions:

* To quickly deploy production-ready clusters, see [Create an AI-optimized GKE cluster with default configuration](https://cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute).
* For precise customization or expansion of existing production GKE environments, see [Create a custom AI-optimized GKE cluster which uses A4X](https://cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute-custom-a4x).

### Changed

#### (2025-R38) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1851000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2547000
  + 1.28.15-gke.2610000
  + 1.29.15-gke.1756000
  + 1.29.15-gke.1835000
  + 1.30.14-gke.1036000
  + 1.31.12-gke.1014000
  + 1.32.7-gke.1079000
  + 1.33.3-gke.1136000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2564000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2564000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1773000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R38) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following node versions are now available:
  + [1.28.15-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1851000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available:
  + 1.30.12-gke.1414000
  + 1.31.12-gke.1014000
  + 1.32.7-gke.1016000
  + 1.33.2-gke.1043000
  + 1.33.2-gke.1240000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R38) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + [1.34.0-gke.1662000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1059000
  + 1.30.14-gke.1108000
  + 1.31.12-gke.1014000
  + 1.32.8-gke.1026000
  + 1.33.4-gke.1036000
  + 1.33.4-gke.1134000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R38) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1036000
  + 1.31.12-gke.1014000
  + 1.32.7-gke.1079000
  + 1.33.3-gke.1136000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Changed

#### (2025-R38) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Stable channel:
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1414000
  + 1.32.7-gke.1016000
  + 1.33.2-gke.1043000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.

### Changed

#### (2025-R38) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following versions are now available for new GKE clusters, and for
manual control plane upgrades and node upgrades for existing clusters. For more
information about versioning and upgrades, see [GKE versioning and
support](https://cloud.google.com/kubernetes-engine/versioning) and [About GKE
cluster upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + [1.34.0-gke.1662000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1059000
  + 1.30.14-gke.1108000
  + 1.31.12-gke.1014000
  + 1.32.8-gke.1026000
  + 1.33.4-gke.1036000
  + 1.33.4-gke.1134000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1036000
  + 1.31.12-gke.1014000
  + 1.32.7-gke.1079000
  + 1.33.3-gke.1136000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Stable channel:
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1414000
  + 1.32.7-gke.1016000
  + 1.33.2-gke.1043000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1851000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2547000
  + 1.28.15-gke.2610000
  + 1.29.15-gke.1756000
  + 1.29.15-gke.1835000
  + 1.30.14-gke.1036000
  + 1.31.12-gke.1014000
  + 1.32.7-gke.1079000
  + 1.33.3-gke.1136000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2564000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2564000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1773000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following node versions are now available:
  + [1.28.15-gke.2630000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1851000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1150000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1110000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1170000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1245000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available:
  + 1.30.12-gke.1414000
  + 1.31.12-gke.1014000
  + 1.32.7-gke.1016000
  + 1.33.2-gke.1043000
  + 1.33.2-gke.1240000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.

---
## 2025-09-08

### Feature

Starting with GKE version 1.33.4-gke.1036000, `ComputeClass` supports the following new `sysctls` configurations:

* kernel.shmmni
* kernel.shmmax
* kernel.shmall
* net.core.rmem\_default
* net.netfilter.nf\_conntrack\_max
* net.netfilter.nf\_conntrack\_buckets
* net.netfilter.nf\_conntrack\_tcp\_timeout\_close\_wait
* net.netfilter.nf\_conntrack\_tcp\_timeout\_time\_wait
* net.netfilter.nf\_conntrack\_tcp\_timeout\_time\_wait
* net.netfilter.nf\_conntrack\_acct
* vm.dirty\_background\_ratio
* vm.dirty\_writeback\_centisecs
* vm.overcommit\_memory
* vm.overcommit\_ratio
* vm.vfs\_cache\_pressure
* fs.aio-max-nr
* fs.file-max
* fs.inotify.max\_user\_instances
* fs.inotify.max\_user\_watches
* fs.nr\_open

For more information, see the [ComputeClass CRD reference](https://cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#sysctls).

---
## 2025-09-04

### Announcement

**Kubernetes 1.34 is now available in the Rapid channel**

Kubernetes 1.34 is now available in the Rapid channel. For more information about the content of Kubernetes 1.34, read the [Kubernetes 1.34 Release Notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#changelog-since-v1330).

### Changed

**Other changes in 1.34**

* **containerd 2.1:** GKE nodes are now upgraded to containerd 2.1. This release includes performance improvements such as faster image downloads. For a complete list of changes, see the official [containerd 2.1 release notes](https://github.com/containerd/containerd/releases/tag/v2.1.0).
* **VPA InPlaceOrRecreate**: This version introduces a [new InPlaceOrRecreate mode in Vertical Pod Autoscaler (VPA)](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler/enhancements/4016-in-place-updates-support) (Public Preview) powered by In-Place Pod Resize (IPPR/IPPU) that allows automatically rightsizing workloads often without recreating the Pod. This mode ensures seamless service continuity while minimizing costs during idle periods. If you haven't used VPA with your workloads before, enable Vertical Pod Autoscaler on your cluster and then create a VPA Object for a workload.

### Deprecated

**Deprecated in 1.34**

The [v1beta1](https://github.com/kubernetes/kubelet/tree/v0.34.0/pkg/apis/dra/v1beta1) gRPC API between the Kubelet and DRA drivers is deprecated in this release in favor of the [v1](https://github.com/kubernetes/kubelet/tree/v0.34.0/pkg/apis/dra/v1) API. This API will continue to function but we recommend that all drivers move to the v1 API to prepare for the eventual removal of the v1beta1 API.

### Changed

**CNI spec version for GKE Dataplane V2 updated to v1.1.0**

Starting with GKE patch version 1.34, clusters using [GKE Dataplane V2](https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) are being updated from [CNI spec](https://www.cni.dev/docs/spec/) v0.3.1 to v1.1.0.

Action required: If you use your own CNI plugins in your GKE cluster (such as self-managed open-source Istio), you must upgrade them
to a version compatible with CNI spec v1.1.0 to prevent errors.

### Feature

GKE alpha clusters enable all alpha and the default beta feature gates, which help you to test and validate upcoming Kubernetes capabilities. You can now modify the feature gates to enable or disable differently from the default values, which provides more granular control when leveraging these experimental features. Note that alpha clusters shouldn't be used for production workloads to ensure that your workloads remain stable and performant. For more information, see [Alpha clusters](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).

### Feature

**New features in Kubernetes 1.34**

* The [Kubernetes Dynamic Resource Allocation (DRA) APIs](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#api) are now generally available. For more information about using DRA in GKE, see [About dynamic resource allocation in GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation). The Prioritized list and Admin access features have been promoted to beta and will be enabled by default. The kubelet API has been updated to report status on resources allocated through DRA.
* [The Sleep Action for Pod prestop lifecycle hook](https://github.com/kubernetes/enhancements/issues/3960) is now GA. This can be used to delay Pod termination for graceful shutdown.
* [Streaming List Response Encoding](https://github.com/kubernetes/enhancements/issues/5116) is now GA. It enables efficient handling of requests for large object collections, improving API server reliability and performance.
* [In-Place Pod Resize](https://github.com/kubernetes/enhancements/issues/1287), which was in beta, is now improved by adding support for decreasing memory limits with best-effort OOM protection. Improved deferred resize retries are also added, which are now prioritized and more responsive to resources becoming available. A new `ResizeCompleted` event records when a resize is completed.

### Feature

On clusters with GKE Dataplane V2 that are on GKE version 1.34 and later, the [ptp plugin](https://www.cni.dev/plugins/current/main/ptp) is removed from the Container Network Interface (CNI) path. Pods that are created on new nodes have interfaces named `lxc[INTERFACE_HASH]` instead of `gke[INTERFACE_HASH]`. Additionally, the CNI configuration is moving from the `netd` DaemonSet to the `cni-writer` container in the `anetd` DaemonSet. For more information, see [Overview of GKE Dataplane V2](https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2#introduction).

---
## 2025-09-03

### Changed

#### (2025-R37) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2564000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1773000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1835000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2527000
  + 1.28.15-gke.2599000
  + 1.29.15-gke.1713000
  + 1.29.15-gke.1820000
  + 1.30.14-gke.1011000
  + 1.31.11-gke.1101000
  + 1.32.7-gke.1016000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1756000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.

### Feature

In GKE version 1.33.3-gke.1392000 or later, you can use ComputeClasses to provision Confidential GKE Nodes with any supported Confidential Computing type. This feature is now generally available. For more information, see [Confidential GKE Nodes](https://cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes).

### Changed

#### (2025-R37) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available:
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following node versions are now available:
  + [1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1835000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available:
  + 1.30.12-gke.1390000
  + 1.31.11-gke.1002000
  + 1.31.11-gke.1101000
  + 1.32.6-gke.1125000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.

### Changed

#### (2025-R37) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + [1.34.0-gke.1477000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
  + [1.34.0-gke.1497000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1036000
  + 1.31.11-gke.1101000
  + 1.32.7-gke.1079000
  + 1.33.3-gke.1136000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.34 to version [1.34.0-gke.1477000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) with this release.

### Changed

#### (2025-R37) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1011000
  + 1.31.11-gke.1101000
  + 1.32.7-gke.1016000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.

### Changed

#### (2025-R37) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Stable channel:
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1390000
  + 1.31.11-gke.1002000
  + 1.32.6-gke.1125000
  + 1.33.2-gke.1240000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.

### Changed

#### (2025-R37) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
and [Upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
  + [1.34.0-gke.1477000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
  + [1.34.0-gke.1497000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1036000
  + 1.31.11-gke.1101000
  + 1.32.7-gke.1079000
  + 1.33.3-gke.1136000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.34 to version [1.34.0-gke.1477000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1340) with this release.

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Regular channel:
  + 1.30.14-gke.1011000
  + 1.31.11-gke.1101000
  + 1.32.7-gke.1016000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Stable channel:
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1390000
  + 1.31.11-gke.1002000
  + 1.32.6-gke.1125000
  + 1.33.2-gke.1240000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2564000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1773000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1835000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2527000
  + 1.28.15-gke.2599000
  + 1.29.15-gke.1713000
  + 1.29.15-gke.1820000
  + 1.30.14-gke.1011000
  + 1.31.11-gke.1101000
  + 1.32.7-gke.1016000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1756000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available:
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following node versions are now available:
  + [1.28.15-gke.2610000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1835000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1130000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1083000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1172000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available:
  + 1.30.12-gke.1390000
  + 1.31.11-gke.1002000
  + 1.31.11-gke.1101000
  + 1.32.6-gke.1125000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.

---
## 2025-09-02

### Announcement

Features that were part of GKE Enterprise are now available as part of the standard GKE offering, or offered as standalone SKUs.

The following advanced multi-cluster management and networking features are included in the GKE offering at no additional cost:

* Fleet dashboard
* Multi-team Management
* Config Sync
* Config Controller
* Managed Policy Controller
* Connect Gateway
* Network Function Optimizer
* Fully Qualified Domain Name (FQDN) Network Policy
* Inter-node Transparent Encryption

The following GKE Enterprise features continue to be available using their current standalone SKUs. If you are using any of these features, your billing is automatically transitioned to the corresponding standalone SKU.

* Managed Cloud Service Mesh
* Multicluster Gateways; Multicluster Ingress
* Binary Authorization
* Advanced Vulnerability Scanning
* GKE Extended Support (LTS)

---
## 2025-08-29

### Fixed

A fix is available for an issue with Cloud Storage FUSE CSI driver that could
cause Pod to be stuck during startup after a node restart event.
Cloud Storage FUSE CSI driver now gracefully handles a node restart behavior.

The fix is available in the following GKE versions:

* 1.32.6-gke.1125000 and later
* 1.33.1-gke.1959000 and later

---
## 2025-08-28

### Feature

You can now run GPU workloads on Confidential GKE Nodes with the A3 High
machine type and NVIDIA H100 GPUs. This feature is available in
GKE version 1.32.2-gke.1297000 and later for manual GPU driver
installation, and in version 1.33.3-gke.1392000 and later for automatic driver
installation. This enables stronger data protection and integrity for
GPU-accelerated computations running within GKE clusters and
nodes. This feature is in General Availability.

For more information, see [Encrypt GPU workload data in use with Confidential GKE Nodes](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes).

### Security

GKE version 1.33.0-gke.1276000 and later remediate a low severity
vulnerability, in which an attacker with the ability to patch Node resources by
using the Kubernetes API could change specific node labels in clusters that use
Workload Identity Federation for GKE. This could result in the attacker gaining
access to node metadata, such as the IAM service account.
To remediate this
vulnerability, a validation policy is enforced that prevents unauthorized
modifications to the node labels that control metadata protection.

---
## 2025-08-27

### Changed

#### (2025-R36) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1756000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2507000
  + 1.28.15-gke.2564000
  + 1.29.15-gke.1686000
  + 1.29.15-gke.1773000
  + 1.30.12-gke.1414000
  + 1.31.11-gke.1064000
  + 1.32.6-gke.1125000
  + 1.33.2-gke.1240000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.

### Changed

#### (2025-R36) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following node versions are now available:
  + [1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available:
  + 1.30.12-gke.1372000
  + 1.31.10-gke.1067000
  + 1.31.11-gke.1064000
  + 1.31.11-gke.1135000
  + 1.32.6-gke.1096000
  + 1.32.8-gke.1005000
  + 1.33.2-gke.1111000
  + 1.33.3-gke.1392000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.

### Changed

#### (2025-R36) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1011000
  + 1.31.11-gke.1064000
  + 1.31.11-gke.1135000
  + 1.32.7-gke.1016000
  + 1.32.8-gke.1005000
  + 1.33.3-gke.1392000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.

### Changed

#### (2025-R36) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1414000
  + 1.31.11-gke.1064000
  + 1.32.6-gke.1125000
  + 1.33.2-gke.1240000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.

### Changed

#### (2025-R36) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1372000
  + 1.31.10-gke.1067000
  + 1.32.6-gke.1096000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.

### Changed

#### (2025-R36) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
and [Upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Rapid channel:
  + 1.30.14-gke.1011000
  + 1.31.11-gke.1064000
  + 1.31.11-gke.1135000
  + 1.32.7-gke.1016000
  + 1.32.8-gke.1005000
  + 1.33.3-gke.1392000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1414000
  + 1.31.11-gke.1064000
  + 1.32.6-gke.1125000
  + 1.33.2-gke.1240000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1372000
  + 1.31.10-gke.1067000
  + 1.32.6-gke.1096000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1756000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2507000
  + 1.28.15-gke.2564000
  + 1.29.15-gke.1686000
  + 1.29.15-gke.1773000
  + 1.30.12-gke.1414000
  + 1.31.11-gke.1064000
  + 1.32.6-gke.1125000
  + 1.33.2-gke.1240000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following node versions are now available:
  + [1.28.15-gke.2599000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1820000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.12-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1108000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.4-gke.1134000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available:
  + 1.30.12-gke.1372000
  + 1.31.10-gke.1067000
  + 1.31.11-gke.1064000
  + 1.31.11-gke.1135000
  + 1.32.6-gke.1096000
  + 1.32.8-gke.1005000
  + 1.33.2-gke.1111000
  + 1.33.3-gke.1392000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.

---
## 2025-08-25

### Feature

In GKE version 1.33 and later, the Horizontal Pod Autoscaler
has been re-architected for improved performance and scalability. This update
enables a consistent 15-second recalculation period and supports up to 5,000 HPA
objects per cluster.

For more information see, [Horizontal Pod autoscaling](https://cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler#scalability).

---
## 2025-08-21

### Feature

Starting with GKE version 1.33.2-gke.1240000 and later, you can
now specify the network service tier (Standard or Premium) for ephemeral IP
addresses used by the `gke-l7-regional-external-managed` GatewayClass. This
GatewayClass configures Regional External Application Load Balancers for single
clusters.

For more information, see [Configure network tier for Gateway IP addresses](https://cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure-network-tier).

### Feature

The [M4 machine series](https://cloud.google.com/compute/docs/memory-optimized-machines#m4_series)
is generally available in GKE Autopilot clusters with
version 1.33.4-gke.1013000 or later. For more information, see M4 in
[Resource requests in Autopilot](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests).

### Changed

Starting in GKE 1.33.3-gke.1136000, the validation of the
HealthCheckPolicy CRD is now performed earlier by GKE Gateway.
Hence, certain invalid policies are now rejected by `kubectl`. The resulting
error message will specify why the policy is invalid.

### Changed

#### (2025-R35) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
and [Upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1135000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.3-gke.1392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1414000
  + 1.31.11-gke.1036000
  + 1.32.6-gke.1125000
  + 1.33.2-gke.1240000
  + 1.33.3-gke.1250000
  + 1.33.3-gke.1266000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1390000
  + 1.31.11-gke.1002000
  + 1.32.6-gke.1096000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1340000
  + 1.31.10-gke.1034000
  + 1.32.6-gke.1025000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2564000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1773000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2488000
  + 1.28.15-gke.2547000
  + 1.29.15-gke.1656000
  + 1.29.15-gke.1756000
  + 1.30.12-gke.1390000
  + 1.31.11-gke.1002000
  + 1.32.6-gke.1096000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1686000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available:
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1135000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.3-gke.1392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following node versions are now available:
  + [1.28.15-gke.2564000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1773000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1135000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.3-gke.1392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available:
  + 1.30.12-gke.1340000
  + 1.31.10-gke.1034000
  + 1.32.6-gke.1013000
  + 1.33.1-gke.1584000
  + 1.33.3-gke.1250000
  + 1.33.3-gke.1266000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R35) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2564000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1773000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2488000
  + 1.28.15-gke.2547000
  + 1.29.15-gke.1656000
  + 1.29.15-gke.1756000
  + 1.30.12-gke.1390000
  + 1.31.11-gke.1002000
  + 1.32.6-gke.1096000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1686000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R35) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available:
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1135000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.3-gke.1392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following node versions are now available:
  + [1.28.15-gke.2564000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1773000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1135000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.3-gke.1392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available:
  + 1.30.12-gke.1340000
  + 1.31.10-gke.1034000
  + 1.32.6-gke.1013000
  + 1.33.1-gke.1584000
  + 1.33.3-gke.1250000
  + 1.33.3-gke.1266000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R35) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1059000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1135000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.31.12-gke.1014000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13112)
  + [1.32.8-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.32.8-gke.1026000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1328)
  + [1.33.3-gke.1392000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.4-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1334)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1414000
  + 1.31.11-gke.1036000
  + 1.32.6-gke.1125000
  + 1.33.2-gke.1240000
  + 1.33.3-gke.1250000
  + 1.33.3-gke.1266000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333) with this release.

### Changed

#### (2025-R35) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Regular channel:
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1390000
  + 1.31.11-gke.1002000
  + 1.32.6-gke.1096000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R35) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1340000
  + 1.31.10-gke.1034000
  + 1.32.6-gke.1025000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

---
## 2025-08-20

### Fixed

A fix is available for an issue where the `device-fs-monitor` component in the
Node Problem Detector generated false `ReadOnlyLocalSSDDetected` warnings on
nodes that did not have local SSDs. This could cause customer confusion and
distracting warnings.

The fix is available in the following GKE versions:

* 1.32.6-gke.1096000 and later
* 1.33.0-gke.1712000 and later

---
## 2025-08-15

### Feature

For clusters enrolled in the Extended channel, you can now use
[Gateway](https://cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)
with GKE version 1.30 or later, or
[customized sysctl configuration options](https://cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#sysctl-options).

### Feature

You can now receive a patch version in a release channel as soon as the version
is available and before GKE sets the version as an auto-upgrade
target in the channel by using *accelerated patch auto-upgrades*. Receiving
patch versions earlier can help accelerate auto-upgrade timelines for patches,
especially for use cases such as accelerating your compliance with security
requirements.

For more information, see
[Accelerated patch auto-upgrades](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels#accelerated-patch).

---
## 2025-08-14

### Changed

#### (2025-R34) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1686000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1756000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2475000
  + 1.28.15-gke.2527000
  + 1.29.15-gke.1639000
  + 1.29.15-gke.1713000
  + 1.30.12-gke.1372000
  + 1.31.10-gke.1067000
  + 1.32.6-gke.1060000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1656000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Feature

You can now configure GKE clusters to have a default compute
class in GKE versions 1.33.1-gke.1744000 or later. For more
details, see the
[default custom compute class documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes).

### Changed

#### (2025-R34) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available:
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.3-gke.1266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following node versions are now available:
  + [1.28.15-gke.2547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1756000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.3-gke.1266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available:
  + 1.30.12-gke.1333000
  + 1.31.10-gke.1021000
  + 1.32.4-gke.1767000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R34) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.3-gke.1266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1390000
  + 1.31.11-gke.1002000
  + 1.32.6-gke.1096000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R34) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1372000
  + 1.31.10-gke.1067000
  + 1.32.6-gke.1060000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R34) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1333000
  + 1.31.10-gke.1021000
  + 1.32.6-gke.1013000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R34) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
and [Upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.3-gke.1266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1390000
  + 1.31.11-gke.1002000
  + 1.32.6-gke.1096000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1372000
  + 1.31.10-gke.1067000
  + 1.32.6-gke.1060000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1333000
  + 1.31.10-gke.1021000
  + 1.32.6-gke.1013000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1686000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1756000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2475000
  + 1.28.15-gke.2527000
  + 1.29.15-gke.1639000
  + 1.29.15-gke.1713000
  + 1.30.12-gke.1372000
  + 1.31.10-gke.1067000
  + 1.32.6-gke.1060000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1656000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available:
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.3-gke.1266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following node versions are now available:
  + [1.28.15-gke.2547000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1756000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1101000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1079000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1250000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
  + [1.33.3-gke.1266000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available:
  + 1.30.12-gke.1333000
  + 1.31.10-gke.1021000
  + 1.32.4-gke.1767000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

---
## 2025-08-12

### Feature

Starting with GKE version 1.33.1-gke.1231000, you can view
KubeRay Operator addon logs. These logs are available by default in
Cloud Logging when the Ray operator addon is enabled in GKE.
This integration helps you to monitor and debug the Ray Operator. Previously,
accessing these logs required more complex steps. To view the logs, navigate to
Cloud Logging Logs Explorer in the Google Cloud console and run a query to filter
for the Ray Operator logs for your specific cluster.

For more information, see [View Ray Operator logs on GKE](https://cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/view-ray-operator-logs).

### Feature

Starting on August 1, 2025, the Performance HorizontalPodAutoscaler profile is
enabled by default for GKE Standard clusters that run
GKE version 1.33.2-gke.4605000 and later and meet all of the
[Performance profile requirements](https://cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#requirements_2).
The Performance profile improves the reaction time, speed, and scalability of
the Horizontal Pod Autoscaler. You can optionally
[disable the Performance profile](https://cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#disable_the_performance_hpa_profile).

---
## 2025-08-08

### Feature

You can now [customize a node system configuration](https://cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#kubelet-options) with the following new Kubelet, Sysctl, and Linux config options:

* kubeletConfig flags:

  + topologyManager (on GKE versions 1.32.3-gke.1785000 and later)
  + memoryManager (on GKE versions 1.32.3-gke.1785000 and later)
  + maxParallelImagePulls (on GKE versions 1.33.1-gke.1918000 and later)
  + singleProcessOomKill (on GKE versions 1.32.4-gke.1132000, 1.33.0-gke.1748000 and later)
  + evictionSoft
  + evictionSoftGracePeriod
  + evictionMinimumReclaim
  + evictionMaxPodGracePeriodSeconds
* sysctl flags:

  + vm.overcommit\_memory
  + vm.overcommit\_ratio
  + vm.vfs\_cache\_pressure
  + vm.dirty\_ratio
  + vm.dirty\_background\_ratio
  + vm.dirty\_expire\_centisecs
  + vm.dirty\_writeback\_centisecs
  + vm.watermark\_scale\_factor
  + vm.min\_free\_kbytes
  + vm.swappiness
  + fs.nr\_open
  + fs.file-max
  + fs.inotify.max\_user\_watches
  + fs.inotify.max\_user\_instances
  + fs.aio-max-nr
  + net.ipv4.tcp\_max\_orphans
* linuxConfig flags:

  + transparentHugepageEnabled (on GKE versions 1.33.2-gke.4655000 and later)
  + transparentHugepageDefrag (on GKE versions 1.33.2-gke.4655000 and later)

### Feature

The C4 machine series now has General Availability machine types that support Local SSD storage options. These machine types are available in all GKE versions for Standard mode, and in GKE version 1.33.1-gke.1545000 and later for Autopilot mode. For more information about these machine types, see the "C4 standard with Local SSD" and "C4 highmem with Local SSD" tabs in [C4 machine types](https://cloud.google.com/compute/docs/general-purpose-machines#c4_machine_types).

---
## 2025-08-06

### Changed

#### (2025-R33) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1656000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2461000
  + 1.28.15-gke.2507000
  + 1.29.15-gke.1614000
  + 1.29.15-gke.1686000
  + 1.30.12-gke.1340000
  + 1.31.10-gke.1034000
  + 1.32.6-gke.1025000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R33) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available:
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following node versions are now available:
  + [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available:
  + 1.30.12-gke.1320000
  + 1.31.9-gke.1287000
  + 1.32.4-gke.1698000
  + 1.33.2-gke.4780000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R33) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1372000
  + 1.31.10-gke.1067000
  + 1.32.6-gke.1060000
  + 1.33.2-gke.4780000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R33) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1340000
  + 1.31.10-gke.1034000
  + 1.32.6-gke.1025000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R33) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1320000
  + 1.31.9-gke.1287000
  + 1.32.4-gke.1767000
  + 1.33.2-gke.1111000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R33) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
and [Upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1372000
  + 1.31.10-gke.1067000
  + 1.32.6-gke.1060000
  + 1.33.2-gke.4780000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1340000
  + 1.31.10-gke.1034000
  + 1.32.6-gke.1025000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1320000
  + 1.31.9-gke.1287000
  + 1.32.4-gke.1767000
  + 1.33.2-gke.1111000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1656000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2461000
  + 1.28.15-gke.2507000
  + 1.29.15-gke.1614000
  + 1.29.15-gke.1686000
  + 1.30.12-gke.1340000
  + 1.31.10-gke.1034000
  + 1.32.6-gke.1025000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available:
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following node versions are now available:
  + [1.28.15-gke.2527000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1713000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.14-gke.1011000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
  + [1.31.11-gke.1064000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.7-gke.1016000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1327)
  + [1.33.3-gke.1136000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1333)
* The following versions are no longer available:
  + 1.30.12-gke.1320000
  + 1.31.9-gke.1287000
  + 1.32.4-gke.1698000
  + 1.33.2-gke.4780000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

---
## 2025-08-05

### Feature

The [M4 machine series](https://cloud.google.com/compute/docs/memory-optimized-machines#m4_series) is generally available in GKE Standard clusters.

### Fixed

A fix is available for an issue in which the Compute Engine Persistent Disk CSI
driver failed with an `invalid cpuString` error on GKE nodes that used custom
machine types. This issue prevented successful attachment and mounting of
Persistent Disk volumes on affected nodes. The fix is available in the following
GKE versions:

* 1.31.10-gke.1034000 and later
* 1.32.4-gke.1698000 and later
* 1.33.1-gke.1386000 and later

---
## 2025-08-01

### Changed

#### (2025-R32) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1686000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2456000
  + 1.28.15-gke.2488000
  + 1.29.15-gke.1607000
  + 1.29.15-gke.1656000
  + 1.30.12-gke.1333000
  + 1.31.10-gke.1021000
  + 1.32.6-gke.1013000
  + 1.33.2-gke.1111000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2461000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2461000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1614000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Changed

#### (2025-R32) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4780000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following node versions are now available:
  + [1.28.15-gke.2507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1686000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4780000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available:
  + 1.30.12-gke.1279000
  + 1.31.9-gke.1218000
  + 1.32.2-gke.1297002
  + 1.32.4-gke.1415000
  + 1.33.2-gke.4655000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Changed

#### (2025-R32) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4780000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1340000
  + 1.31.10-gke.1034000
  + 1.32.6-gke.1025000
  + 1.33.2-gke.4655000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Changed

#### (2025-R32) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1333000
  + 1.31.10-gke.1021000
  + 1.32.6-gke.1013000
  + 1.33.2-gke.1111000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Changed

#### (2025-R32) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1279000
  + 1.31.9-gke.1218000
  + 1.32.4-gke.1698000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Changed

#### (2025-R32) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
and [Upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4780000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1340000
  + 1.31.10-gke.1034000
  + 1.32.6-gke.1025000
  + 1.33.2-gke.4655000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1333000
  + 1.31.10-gke.1021000
  + 1.32.6-gke.1013000
  + 1.33.2-gke.1111000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1279000
  + 1.31.9-gke.1218000
  + 1.32.4-gke.1698000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.28.15-gke.2507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.29.15-gke.1686000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2456000
  + 1.28.15-gke.2488000
  + 1.29.15-gke.1607000
  + 1.29.15-gke.1656000
  + 1.30.12-gke.1333000
  + 1.31.10-gke.1021000
  + 1.32.6-gke.1013000
  + 1.33.2-gke.1111000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2461000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2461000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1614000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4780000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following node versions are now available:
  + [1.28.15-gke.2507000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1686000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1414000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1036000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1125000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4780000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available:
  + 1.30.12-gke.1279000
  + 1.31.9-gke.1218000
  + 1.32.2-gke.1297002
  + 1.32.4-gke.1415000
  + 1.33.2-gke.4655000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

---
## 2025-07-28

### Feature

In GKE version 1.33.2-gke.1335000 and later, the
[GKE Gateway controller](https://cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller)
supports
[Gateway API v1.3 CRDs](https://gateway-api.sigs.k8s.io/implementations/v1.3/).

### Feature

In GKE version 1.33.1-gke.1788000 and later, you can target specific reservation
sub-blocks in a reservation block by using the
[`reservationSubBlock` field in compute classes](https://cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#reservationSubBlock).

### Feature

In GKE version 1.32.2-gke.1359000 and later, you can now configure
[collection scheduling](https://cloud.google.com/kubernetes-engine/docs/concepts/tpus#collection-scheduling)
for single-host and multi-host TPU node pools by using
[compute classes](https://cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).
Collection scheduling lets you set a Service Level Objective (SLO) for your TPU
workloads.

### Feature

In GKE version 1.33.2-gke.1335000 and later, the
[GKE Gateway controller](https://cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller)
supports
[Gateway API v1.3 CRDs](https://gateway-api.sigs.k8s.io/implementations/v1.3/).

### Feature

In GKE version 1.33.1-gke.1788000 and later, you can target specific reservation
sub-blocks in a reservation block by using the
[`reservationSubBlock` field in compute classes](https://cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#reservationSubBlock).

### Feature

In GKE version 1.32.2-gke.1359000 and later, you can now configure
[collection scheduling](https://cloud.google.com/kubernetes-engine/docs/concepts/tpus#collection-scheduling)
for single-host and multi-host TPU node pools by using
[compute classes](https://cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).
Collection scheduling lets you set a Service Level Objective (SLO) for your TPU
workloads.

### Announcement

#### Control plane datastore maintenance

Starting in May, 2025, Google is performing maintenance on the internal control
plane datastore for all GKE clusters to improve scalability and
reliability. We expect to complete these improvements across GKE
by October, 2025.

This maintenance is happening gradually across all GKE clusters,
and will occur in your clusters only during configured maintenance windows. The
maintenance process is expected to take approximately 15 minutes to complete
during your cluster's maintenance window.

**Expected impact**

During the internal control plane datastore maintenance, the
**Kubernetes API server will be unavailable for 15 minutes**, regardless of
whether you use a regional cluster or a zonal cluster. During this 15-minute
period, you won't be able to interact with the Kubernetes API server for your
cluster.

Consider the following potential disruptions to your normal workflows during the
maintenance window for your cluster:

* **Kubernetes API unavailability**: you can't use the `kubectl` tool or any
  other Kubernetes API client to issue commands to the control plane,
  regardless of whether the cluster is regional or zonal. Attempts to deploy,
  modify, or query resources by using the Kubernetes API will fail during this
  period.
* **Halted deployments:** automated deployment pipelines (CI/CD) that interact
  with the Kubernetes API will fail to complete tasks such as deploying or
  updating applications in the cluster.
* **Google Cloud console limitations**: operations for the cluster in the
  Google Cloud console that communicate with the Kubernetes API might fail
  during the maintenance period.
* **Delayed control plane automation**: features that are managed by the
  control plane, such as the cluster autoscaler, Horizontal or Vertical
  Pod Autoscaling adjustments, or some node auto-repair operations might be
  paused until the API server is online.

The following resources have no expected impact during the maintenance period:

* **Running applications**: any running applications and services on your
  nodes should continue to function without interruptions.
* **Node pool operations**: existing nodes should remain connected and
  operational.
* **Network traffic**: traffic in the data plane, such as traffic to and from
  your running workloads, shouldn't be affected.

**What you need to do**

No action is required from you for the maintenance to occur. To plan for this
maintenance, we recommend that you do the following:

* **Review maintenance windows**: review your cluster's
  [maintenance window and exclusions settings](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions)
  and schedule maintenance windows during periods that minimize disruptions to
  your normal workflows.
* **Plan for Kubernetes API unavailability**: if you run critical operations
  in your cluster that require access to the Kubernetes API, avoid scheduling
  these operations during maintenance windows.

### Fixed

**Important:** This note is incorrect. For the correct note, see the entry for
[August 5, 2025](#csi-fix-20250805).

A fix is available for an issue in which the Compute Engine Persistent Disk CSI
driver failed with an `invalid cpuString` error on GKE nodes that used custom
machine types. This issue prevented successful attachment and mounting of
Persistent Disk volumes on affected nodes. The fix is available in the following
GKE versions:

* 1.31.10-gke.1021000 and later
* 1.32.4-gke.1698000 and later
* 1.33.1-gke.1386000 and later

---
## 2025-07-25

### Changed

#### (2025-R31) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1656000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2303000
  + 1.28.15-gke.2380000
  + 1.28.15-gke.2428000
  + 1.28.15-gke.2445000
  + 1.28.15-gke.2475000
  + 1.29.15-gke.1415000
  + 1.29.15-gke.1493000
  + 1.29.15-gke.1549000
  + 1.29.15-gke.1594000
  + 1.29.15-gke.1639000
  + 1.30.12-gke.1168000
  + 1.30.12-gke.1208000
  + 1.30.12-gke.1246000
  + 1.30.12-gke.1279000
  + 1.30.12-gke.1320000
  + 1.31.9-gke.1044001
  + 1.31.9-gke.1119000
  + 1.31.9-gke.1176000
  + 1.31.9-gke.1218000
  + 1.31.9-gke.1287000
  + 1.32.4-gke.1415000
  + 1.32.4-gke.1603000
  + 1.32.4-gke.1698000
  + 1.32.4-gke.1767000
  + 1.33.1-gke.1107000
  + 1.33.1-gke.1386000
  + 1.33.1-gke.1584000
  + 1.33.1-gke.1744000
  + 1.33.2-gke.1043000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1607000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Changed

#### (2025-R31) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following node versions are now available:
  + [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1656000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available:
  + 1.30.12-gke.1086000
  + 1.30.12-gke.1151000
  + 1.30.12-gke.1168000
  + 1.30.12-gke.1208000
  + 1.30.12-gke.1246000
  + 1.31.8-gke.1113000
  + 1.31.9-gke.1005000
  + 1.31.9-gke.1044001
  + 1.31.9-gke.1119000
  + 1.31.9-gke.1176000
  + 1.32.2-gke.1182003
  + 1.32.4-gke.1353003
  + 1.32.4-gke.1603000
  + 1.33.1-gke.1107000
  + 1.33.1-gke.1386000
  + 1.33.1-gke.1744000
  + 1.33.1-gke.1959000
  + 1.33.2-gke.1384000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Changed

#### (2025-R31) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1208000
  + 1.30.12-gke.1246000
  + 1.30.12-gke.1279000
  + 1.30.12-gke.1320000
  + 1.30.12-gke.1333000
  + 1.31.9-gke.1119000
  + 1.31.9-gke.1176000
  + 1.31.9-gke.1218000
  + 1.31.9-gke.1287000
  + 1.31.10-gke.1021000
  + 1.32.4-gke.1415000
  + 1.32.4-gke.1603000
  + 1.32.4-gke.1698000
  + 1.32.4-gke.1767000
  + 1.32.6-gke.1013000
  + 1.33.1-gke.1584000
  + 1.33.1-gke.1744000
  + 1.33.1-gke.1959000
  + 1.33.2-gke.1043000
  + 1.33.2-gke.1111000
  + 1.33.2-gke.1384000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Changed

#### (2025-R31) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1168000
  + 1.30.12-gke.1208000
  + 1.30.12-gke.1246000
  + 1.30.12-gke.1279000
  + 1.30.12-gke.1320000
  + 1.31.9-gke.1044001
  + 1.31.9-gke.1119000
  + 1.31.9-gke.1176000
  + 1.31.9-gke.1218000
  + 1.31.9-gke.1287000
  + 1.32.4-gke.1415000
  + 1.32.4-gke.1603000
  + 1.32.4-gke.1698000
  + 1.32.4-gke.1767000
  + 1.33.1-gke.1107000
  + 1.33.1-gke.1386000
  + 1.33.1-gke.1584000
  + 1.33.1-gke.1744000
  + 1.33.2-gke.1043000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Changed

#### (2025-R31) Version updates

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1086000
  + 1.30.12-gke.1151000
  + 1.30.12-gke.1168000
  + 1.30.12-gke.1208000
  + 1.30.12-gke.1246000
  + 1.31.8-gke.1113000
  + 1.31.9-gke.1005000
  + 1.31.9-gke.1044001
  + 1.31.9-gke.1119000
  + 1.31.9-gke.1176000
  + 1.32.2-gke.1297002
  + 1.32.4-gke.1415000
  + 1.32.4-gke.1603000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.33 to version [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Changed

#### (2025-R31) Version updates

GKE cluster versions have been updated.

**New versions available for upgrades and new clusters.**

The following Kubernetes versions are now available for new clusters and for
opt-in control plane upgrades and node upgrades for existing clusters. For more
information on versioning and upgrades, see [GKE versioning and support](https://cloud.google.com/kubernetes-engine/versioning)
and [Upgrades](https://cloud.google.com/kubernetes-engine/upgrades).

### Rapid channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1208000
  + 1.30.12-gke.1246000
  + 1.30.12-gke.1279000
  + 1.30.12-gke.1320000
  + 1.30.12-gke.1333000
  + 1.31.9-gke.1119000
  + 1.31.9-gke.1176000
  + 1.31.9-gke.1218000
  + 1.31.9-gke.1287000
  + 1.31.10-gke.1021000
  + 1.32.4-gke.1415000
  + 1.32.4-gke.1603000
  + 1.32.4-gke.1698000
  + 1.32.4-gke.1767000
  + 1.32.6-gke.1013000
  + 1.33.1-gke.1584000
  + 1.33.1-gke.1744000
  + 1.33.1-gke.1959000
  + 1.33.2-gke.1043000
  + 1.33.2-gke.1111000
  + 1.33.2-gke.1384000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Regular channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1168000
  + 1.30.12-gke.1208000
  + 1.30.12-gke.1246000
  + 1.30.12-gke.1279000
  + 1.30.12-gke.1320000
  + 1.31.9-gke.1044001
  + 1.31.9-gke.1119000
  + 1.31.9-gke.1176000
  + 1.31.9-gke.1218000
  + 1.31.9-gke.1287000
  + 1.32.4-gke.1415000
  + 1.32.4-gke.1603000
  + 1.32.4-gke.1698000
  + 1.32.4-gke.1767000
  + 1.33.1-gke.1107000
  + 1.33.1-gke.1386000
  + 1.33.1-gke.1584000
  + 1.33.1-gke.1744000
  + 1.33.2-gke.1043000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Stable channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Stable channel.
* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1086000
  + 1.30.12-gke.1151000
  + 1.30.12-gke.1168000
  + 1.30.12-gke.1208000
  + 1.30.12-gke.1246000
  + 1.31.8-gke.1113000
  + 1.31.9-gke.1005000
  + 1.31.9-gke.1044001
  + 1.31.9-gke.1119000
  + 1.31.9-gke.1176000
  + 1.32.2-gke.1297002
  + 1.32.4-gke.1415000
  + 1.32.4-gke.1603000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.32 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.33 to version [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### Extended channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation in the Extended channel.
* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1656000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available in the Extended channel:
  + 1.28.15-gke.2303000
  + 1.28.15-gke.2380000
  + 1.28.15-gke.2428000
  + 1.28.15-gke.2445000
  + 1.28.15-gke.2475000
  + 1.29.15-gke.1415000
  + 1.29.15-gke.1493000
  + 1.29.15-gke.1549000
  + 1.29.15-gke.1594000
  + 1.29.15-gke.1639000
  + 1.30.12-gke.1168000
  + 1.30.12-gke.1208000
  + 1.30.12-gke.1246000
  + 1.30.12-gke.1279000
  + 1.30.12-gke.1320000
  + 1.31.9-gke.1044001
  + 1.31.9-gke.1119000
  + 1.31.9-gke.1176000
  + 1.31.9-gke.1218000
  + 1.31.9-gke.1287000
  + 1.32.4-gke.1415000
  + 1.32.4-gke.1603000
  + 1.32.4-gke.1698000
  + 1.32.4-gke.1767000
  + 1.33.1-gke.1107000
  + 1.33.1-gke.1386000
  + 1.33.1-gke.1584000
  + 1.33.1-gke.1744000
  + 1.33.2-gke.1043000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.27 to version [1.28.15-gke.2456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.28 to version [1.28.15-gke.2456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.29 to version [1.29.15-gke.1607000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.30 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.31 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.32 to version [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Extended channel will be upgraded from version 1.33 to version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

### No channel

**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

* Version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following node versions are now available:
  + [1.28.15-gke.2488000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1656000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1390000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.11-gke.1002000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13111)
  + [1.32.6-gke.1096000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.4655000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following versions are no longer available:
  + 1.30.12-gke.1086000
  + 1.30.12-gke.1151000
  + 1.30.12-gke.1168000
  + 1.30.12-gke.1208000
  + 1.30.12-gke.1246000
  + 1.31.8-gke.1113000
  + 1.31.9-gke.1005000
  + 1.31.9-gke.1044001
  + 1.31.9-gke.1119000
  + 1.31.9-gke.1176000
  + 1.32.2-gke.1182003
  + 1.32.4-gke.1353003
  + 1.32.4-gke.1603000
  + 1.33.1-gke.1107000
  + 1.33.1-gke.1386000
  + 1.33.1-gke.1744000
  + 1.33.1-gke.1959000
  + 1.33.2-gke.1384000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332) with this release.

---
## 2025-07-22

### Announcement

Google Distributed Cloud for bare metal 1.31.700-gke.72 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.31.700-gke.72 runs on Kubernetes v1.31.10-gke.200.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

### Announcement

Google Distributed Cloud (software only) for VMware 1.31.700-gke.72 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.31.700-gke.72 runs on Kubernetes v1.31.10-gke.200.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Changed

The following functional changes were made in 1.31.700-gke.72:

* Updated the validation checks for cluster upgrades to enforce the [cluster version skew rules](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_skew) for user clusters.

### Fixed

The following issues were fixed in 1.31.700-gke.72:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

### Fixed

The following issues were fixed in 1.31.700-gke.72:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

---
## 2025-07-21

### Feature

In GKE version 1.33.2-gke.1111000 and later, you can use compute classes to set
[Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
on all nodes that are created for that compute class. These labels are applied
to the corresponding `Node` objects in the Kubernetes API. For more information
about setting node labels in compute classes, see the
[ComputeClass custom resource definition](https://cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodepoolconfig).

### Feature

In GKE version 1.33.2-gke.1111000 and later, you can use compute classes to set
[Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
on all nodes that are created for that compute class. These labels are applied
to the corresponding `Node` objects in the Kubernetes API. For more information
about setting node labels in compute classes, see the
[ComputeClass custom resource definition](https://cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodepoolconfig).

---
## 2025-07-17

### Announcement

Google Distributed Cloud for bare metal 1.32.200-gke.104 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads). To upgrade, see [Upgrade clusters](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). Google Distributed Cloud for bare metal 1.32.200-gke.104 runs on Kubernetes v1.32.4-gke.1000.

After a release, it takes approximately 7 to 14 days for the version to become available for installations or upgrades with the [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

If you use a third-party storage vendor, check the [Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release of Google Distributed Cloud for bare metal.

### Announcement

Google Distributed Cloud (software only) for VMware 1.32.200-gke.104 is now available for [download](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads). To upgrade, see [Upgrade a cluster](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading). Google Distributed Cloud 1.32.200-gke.104 runs on Kubernetes v1.32.4-gke.1000.

If you are using a third-party storage vendor, check the [GDC Ready storage partners](https://cloud.google.com/anthos/docs/resources/partner-storage) document to make sure the storage vendor has already passed the qualification for this release.

After a release, it takes approximately 7 to 14 days for the version to become available for use with [GKE On-Prem API clients](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools): the Google Cloud console, the gcloud CLI, and Terraform.

### Fixed

The following issues were fixed in 1.32.200-gke.104:

* Fixed a [known issue](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#keepalived-config-issue) where Keepalived failover is blocked when the corresponding HAProxy instance is unreachable. This issue prevented the control plane VIP from being made available on a new, healthy node.
* Fixed an issue that caused nodes to get stuck in maintenance mode. Health checks have been updated so that the network check job skips connectivity checks for nodes that are in maintenance mode.
* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities).

### Fixed

The following issues were fixed in 1.32.200-gke.104:

* Fixed vulnerabilities listed in [Vulnerability fixes](https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/vulnerabilities).

### Issue

For information about the latest known issues, see [Google Distributed Cloud for bare metal known issues](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues) in the Troubleshooting section.

---
## 2025-07-16

### Changed

#### (2025-R30) Version updates

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

* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Regular channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Stable channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)

### Extended channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### No channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available:
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following node versions are now available:
  + [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

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

### Changed

#### (2025-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are
already in progress when we publish the release notes, and can take multiple
days to complete across all Google Cloud zones.

* The following versions are now available in the Extended channel:
  + [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Changed

#### (2025-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are
already in progress when we publish the release notes, and can take multiple
days to complete across all Google Cloud zones.

* The following versions are now available:
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following node versions are now available:
  + [1.28.15-gke.2475000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1639000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Changed

#### (2025-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are
already in progress when we publish the release notes, and can take multiple
days to complete across all Google Cloud zones.

* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1372000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1067000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1060000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1384000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Changed

#### (2025-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are
already in progress when we publish the release notes, and can take multiple
days to complete across all Google Cloud zones.

* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Changed

#### (2025-R30) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are
already in progress when we publish the release notes, and can take multiple
days to complete across all Google Cloud zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)

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

    ### Changed

    #### (2025-R29) Version updates

    **Note:** Your clusters might not have these versions available. Rollouts are
    already in progress when we publish the release notes, and can take multiple
    days to complete across all Google Cloud zones.
    - The following versions are now available:
      * [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
      * [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
      * [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
      * [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
    - The following node versions are now available:
      * [1.28.15-gke.2461000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
      * [1.29.15-gke.1614000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
      * [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
      * [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
      * [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
      * [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

        ### Changed

        #### (2025-R29) Version updates

        **Note:** Your clusters might not have these versions available. Rollouts are
        already in progress when we publish the release notes, and can take multiple
        days to complete across all Google Cloud zones.
        + The following versions are now available in the Rapid channel:
          - [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
          - [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
          - [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
          - [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

            ### Changed

            #### (2025-R29) Version updates

            **Note:** Your clusters might not have these versions available. Rollouts are
            already in progress when we publish the release notes, and can take multiple
            days to complete across all Google Cloud zones.
            * The following versions are now available in the Regular channel:
              + [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
              + [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
              + [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
              + [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

                ### Changed

                #### (2025-R29) Version updates

                **Note:** Your clusters might not have these versions available. Rollouts are
                already in progress when we publish the release notes, and can take multiple
                days to complete across all Google Cloud zones.
                - The following versions are now available in the Stable channel:
                  * [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
                  * [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
                  * [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)

                    ### Changed

                    #### (2025-R29) Version updates

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
                    + The following versions are now available in the Rapid channel:
                      - [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
                      - [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
                      - [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
                      - [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

                    ### Regular channel

                    **Note:** Your clusters might not have these versions available. Rollouts are already in progress
                    when we publish the release notes, and can take multiple days to complete across all Google Cloud
                    zones.
                    + The following versions are now available in the Regular channel:
                      - [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
                      - [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
                      - [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
                      - [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

                    ### Stable channel

                    **Note:** Your clusters might not have these versions available. Rollouts are already in progress
                    when we publish the release notes, and can take multiple days to complete across all Google Cloud
                    zones.
                    + The following versions are now available in the Stable channel:
                      - [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
                      - [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
                      - [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)

                    ### Extended channel

                    **Note:** Your clusters might not have these versions available. Rollouts are already in progress
                    when we publish the release notes, and can take multiple days to complete across all Google Cloud
                    zones.
                    + The following versions are now available in the Extended channel:
                      - [1.28.15-gke.2461000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
                      - [1.29.15-gke.1614000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
                      - [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
                      - [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
                      - [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
                      - [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

                    ### No channel

                    **Note:** Your clusters might not have these versions available. Rollouts are already in progress
                    when we publish the release notes, and can take multiple days to complete across all Google Cloud
                    zones.
                    + The following versions are now available:
                      - [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
                      - [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
                      - [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
                      - [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
                    + The following node versions are now available:
                      - [1.28.15-gke.2461000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
                      - [1.29.15-gke.1614000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
                      - [1.30.12-gke.1340000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
                      - [1.31.10-gke.1034000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
                      - [1.32.6-gke.1025000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
                      - [1.33.2-gke.1240000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

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

### Changed

#### (2025-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available:
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following node versions are now available:
  + [1.28.15-gke.2456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1607000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Changed

#### (2025-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Changed

#### (2025-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)

### Changed

#### (2025-R28) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)

### Changed

#### (2025-R28) Version updates

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

* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Regular channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)

### Stable channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)

### Extended channel

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

### No channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available:
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)
* The following node versions are now available:
  + [1.28.15-gke.2456000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1607000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1333000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.10-gke.1021000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13110)
  + [1.32.6-gke.1013000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1326)
  + [1.33.2-gke.1111000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

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

### Changed

#### (2025-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available:
  + [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1959000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following node versions are now available:
  + [1.28.15-gke.2445000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1594000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1959000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Changed

#### (2025-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1959000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Changed

#### (2025-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)

### Changed

#### (2025-R27) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)

### Changed

#### (2025-R27) Version updates

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

* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1959000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

### Regular channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1246000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1176000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1603000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)

### Stable channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)

### Extended channel

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

### No channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available:
  + [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1959000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following node versions are now available:
  + [1.28.15-gke.2445000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1594000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1320000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1287000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1767000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1959000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
  + [1.33.2-gke.1043000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1332)

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

### Changed

#### (2025-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following node versions are now available:
  + [1.27.16-gke.2894000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2428000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1549000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available:
  + 1.30.12-gke.1033000
  + 1.31.8-gke.1045000
  + 1.32.4-gke.1236007
  + 1.33.0-gke.2248000
  + 1.33.1-gke.1545000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.

### Changed

#### (2025-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1168000
  + 1.31.9-gke.1044001
  + 1.33.1-gke.1386000
  + 1.33.1-gke.1545000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.

### Changed

#### (2025-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1151000
  + 1.31.9-gke.1005000
  + 1.32.4-gke.1353003
  + 1.33.0-gke.2248000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.

### Changed

#### (2025-R26) Version updates

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1033000
  + 1.31.8-gke.1045000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.

### Changed

#### (2025-R26) Version updates

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

* Version [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) is now the default version for cluster creation in the Rapid channel.
* The following versions are now available in the Rapid channel:
  + [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Rapid channel:
  + 1.30.12-gke.1168000
  + 1.31.9-gke.1044001
  + 1.33.1-gke.1386000
  + 1.33.1-gke.1545000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.29 to version [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.32 to version [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.30 to version [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.31 to version [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Rapid channel will be upgraded from version 1.33 to version [1.33.1-gke.1584000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.

### Regular channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation in the Regular channel.
* The following versions are now available in the Regular channel:
  + [1.30.12-gke.1208000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1119000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.33.1-gke.1386000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available in the Regular channel:
  + 1.30.12-gke.1151000
  + 1.31.9-gke.1005000
  + 1.32.4-gke.1353003
  + 1.33.0-gke.2248000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.29 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.30 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.31 to version [1.31.9-gke.1044001](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.32 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Regular channel will be upgraded from version 1.33 to version [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.

### Stable channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* The following versions are now available in the Stable channel:
  + [1.30.12-gke.1151000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1005000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
* The following versions are no longer available in the Stable channel:
  + 1.30.12-gke.1033000
  + 1.31.8-gke.1045000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.29 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.30 to version [1.30.12-gke.1086000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled in the Stable channel will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.

### Extended channel

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

### No channel

**Note:** Your clusters might not have these versions available. Rollouts are already in progress
when we publish the release notes, and can take multiple days to complete across all Google Cloud
zones.

* Version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) is now the default version for cluster creation.
* The following versions are now available:
  + [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following node versions are now available:
  + [1.27.16-gke.2894000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#v12716)
  + [1.28.15-gke.2428000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
  + [1.29.15-gke.1549000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
  + [1.30.12-gke.1279000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012)
  + [1.31.9-gke.1218000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1319)
  + [1.32.4-gke.1698000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324)
  + [1.33.1-gke.1744000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331)
* The following versions are no longer available:
  + 1.30.12-gke.1033000
  + 1.31.8-gke.1045000
  + 1.32.4-gke.1236007
  + 1.33.0-gke.2248000
  + 1.33.1-gke.1545000
* Auto-upgrade targets are now available for the following minor versions:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.29 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
* The following patch-only version auto-upgrade targets are now available for clusters with [maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or other factors preventing minor version upgrades:
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.30 to version [1.30.12-gke.1168000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13012) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.31 to version [1.31.8-gke.1113000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v1318) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.32 to version [1.32.4-gke.1415000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1324) with this release.
  + Control planes and nodes with auto-upgrade enabled will be upgraded from version 1.33 to version [1.33.1-gke.1107000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1331) with this release.

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
