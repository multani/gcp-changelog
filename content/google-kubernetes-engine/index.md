# Google Kubernetes Engine

## 2025-08-14

### Feature

You can now configure GKE clusters to have a default compute
class in GKE versions 1.33.1-gke.1744000 or later. For more
details, see the
[default custom compute class documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes).

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
