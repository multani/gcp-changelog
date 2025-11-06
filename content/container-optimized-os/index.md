# Container Optimized OS

## 2025-11-05

### cos-117-18613-439-16

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.111](https://cos.googlesource.com/third_party/kernel/+/0ed8bd0d9c0b687b26f66a72743fa7f3f6f8088c ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.439.16/lakitu/gpu_driver_versions.textproto) |

### Fixed

Fixed bcache latency spikes.

### Security

Fixed CVE-2025-31133, CVE-2025-52565, and CVE-2025-52881 in
app-containers/runc. There are known reliability issues in these fixes that will be addressed in subsequent releases.

### Security

Fixed CVE-2025-40103 in the Linux kernel.

### Security

Fixed CVE-2025-40105 in the Linux kernel.

### Security

Fixed CVE-2025-40099 in the Linux kernel.

### Security

Fixed CVE-2025-40052 in the Linux kernel.

### Security

Fixed CVE-2025-40040 in the Linux kernel.

### Security

Fixed CVE-2025-40035 in the Linux kernel.

### Security

Fixed CVE-2025-40044 in the Linux kernel.

### Security

Fixed CVE-2025-40049 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811728 -> 811733

### cos-113-18244-521-11

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.155](https://cos.googlesource.com/third_party/kernel/+/75b1ce1ac39b0f103f0777f2199218595c927472 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.521.11/lakitu/gpu_driver_versions.textproto) |

### Security

Fixed CVE-2025-31133, CVE-2025-52565, and CVE-2025-52881 in
app-containers/runc. There are known reliability issues in these fixes that will be addressed in subsequent releases.

### Security

Fixed CVE-2025-40042 in the Linux kernel.

### Security

Fixed CVE-2025-40049 in the Linux kernel.

### Security

Fixed CVE-2025-40044 in the Linux kernel.

### Security

Fixed CVE-2025-40027 in the Linux kernel.

### Security

Fixed CVE-2025-40035 in the Linux kernel.

### Security

Fixed CVE-2025-40026 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812007 -> 812016

### cos-121-18867-294-12

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.113](https://cos.googlesource.com/third_party/kernel/+/10660c0131fbccaab609fca4aad9a134ebe20adc ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.294.12/lakitu/gpu_driver_versions.textproto) |

### Fixed

Fixed bcache latency spikes.

### Security

Fixed CVE-2025-31133, CVE-2025-52565, and CVE-2025-52881 in
app-containers/runc. There are known reliability issues in these fixes that will be addressed in subsequent releases.

### Security

Fixed CVE-2025-40103 in the Linux kernel.

### Security

Fixed CVE-2025-40105 in the Linux kernel.

### Security

Fixed CVE-2025-40099 in the Linux kernel.

### Security

Fixed CVE-2025-40040 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811785 -> 811792

### cos-125-19216-104-5

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.55](https://cos.googlesource.com/third_party/kernel/+/a87c94f53218718f1811c39c2e1a802d36f5e634 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.104.5/lakitu/gpu_driver_versions.textproto) |

### Fixed

Fixed bcache latency spikes.

### Security

Fixed CVE-2025-31133, CVE-2025-52565, and CVE-2025-52881 in
app-containers/runc. There are known reliability issues in these fixes that will be addressed in subsequent releases.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811499 -> 811455

---
## 2025-11-03

### cos-125-19216-104-3

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.55](https://cos.googlesource.com/third_party/kernel/+/1abebf8624cc7d4e8a9bb2bccff8f0dc031fd549 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.104.3/lakitu/gpu_driver_versions.textproto) |

### Announcement

This is an LTS refresh release.

### Feature

Fixed a bug in cos-extensions which would cause GB200 and GB300 devices not to be detected in one code path, which would result in Imex channels not being created by default.

### Fixed

Upgraded dev-lang/go to v1.23.12.

### Fixed

Fixed a TCPX bug which would sometimes incorrectly report devices as being missing when route cache entries were missing or invalidated.

### Security

Fixed CVE-2025-40006 in the Linux kernel.

### Security

Fixed CVE-2025-40009 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811500 -> 811499
* Changed: net.ipv4.udp\_mem: 188034 250715 376068 -> 188034 250714 376068

### cos-117-18613-439-12

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.111](https://cos.googlesource.com/third_party/kernel/+/027b2ab39b4dc72a0bdecc401f67fa816446d703 ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.439.12/lakitu/gpu_driver_versions.textproto) |

### Security

Fixed CVE-2025-40070 in the Linux kernel.

### Security

Fixed CVE-2025-40038 in the Linux kernel.

### Security

Fixed CVE-2025-40078 in the Linux kernel.

### Security

Fixed CVE-2025-38073 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811785 -> 811728

### cos-dev-129-19350-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.55](https://cos.googlesource.com/third_party/kernel/+/38ea339c697dd371bf1ca35bb23ca1bf49b19a82 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19350.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated the Linux kernel to v6.12.55.

### Feature

Fixed a bug in cos-extensions which would cause GB200 and GB300 devices not to be detected in one code path, which would result in Imex channels not being created by default.

### Fixed

Fixed a TCPX bug which would sometimes incorrectly report devices as being missing when route cache entries were missing or invalidated.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811495 -> 811384

### cos-121-18867-294-8

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.113](https://cos.googlesource.com/third_party/kernel/+/ff0e042c1b1498588b5d036a61f7d61af2c7bf48 ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.294.8/lakitu/gpu_driver_versions.textproto) |

### Fixed

Added support for NVIDIA driver v535.274.02 and v570.195.03.

### Security

Fixed CVE-2025-11413,11414 in binutils-libs.

### Security

Fixed CVE-2025-38073 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811835 -> 811785

### cos-113-18244-521-8

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.155](https://cos.googlesource.com/third_party/kernel/+/f6bca56e79efabbe59c0c87c7f5bffc7c98a8358 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.521.8/lakitu/gpu_driver_versions.textproto) |

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812040 -> 812007

---
## 2025-10-27

### cos-121-18867-294-2

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.113](https://cos.googlesource.com/third_party/kernel/+/51d5c624a0a37c8501fb3a2ed66f0a2dee6ac48a ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.294.2/lakitu/gpu_driver_versions.textproto) |

### Announcement

This is an [LTS Refresh release](https://cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases).

### Changed

Updated app-containers/runc to v1.2.7.

### Fixed

Reduced gcr\_wait\_online retry gap.

### Fixed

Upgraded sys-auth/pambase to v20250906.

### Fixed

Upgraded app-admin/google-guest-configs to v20250805.00.

### Fixed

Upgraded dev-lang/go to v1.23.12.

### Fixed

Upgraded sys-apps/hwdata to v0.400.

### Fixed

Upgraded sys-apps/pv to v1.9.42.

### Fixed

Upgraded sys-apps/less to v685.

### Fixed

Upgraded dev-libs/expat to v2.7.3.

### Fixed

Upgraded app-admin/sudo to v1.9.17\_p2.

### Fixed

Upgraded dev-db/sqlite to v3.50.3.

### Security

Fixed CVE-2025-11494 in binutils-libs.

### Security

Fixed CVE-2025-11495 in binutils-libs.

### Security

Fixed CVE-2025-11412 in binutils-libs.

### cos-113-18244-521-7

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.155](https://cos.googlesource.com/third_party/kernel/+/f6bca56e79efabbe59c0c87c7f5bffc7c98a8358 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.521.7/lakitu/gpu_driver_versions.textproto) |

### Announcement

This is an [LTS Refresh release](https://cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases).

### Changed

Updated app-containers/runc to v1.2.7.

### Fixed

Added support for NVIDIA driver v535.274.02 and v570.195.03. Updated default driver version to v535.274.02 for devices using 535 as the default driver. Updated the default driver version to v570.195.03 for NVIDIA\_H200.

### Fixed

Upgraded app-admin/google-guest-configs to v20250805.00.

### Fixed

Upgraded net-nds/rpcbind to v1.2.8.

### Fixed

Upgraded sys-apps/less to v685.

### Fixed

Upgraded sys-apps/hwdata to v0.400.

### Fixed

Upgraded dev-db/sqlite to v3.50.3.

### Fixed

Upgraded app-admin/sudo to v1.9.17\_p2.

### Security

Fixed CVE-2025-11413 and CVE-2025-11414 in binutils-libs.

### Security

Fixed CVE-2025-11494 in binutils-libs.

### Security

Fixed CVE-2025-11495 in binutils-libs.

### Security

Fixed CVE-2025-11412 in binutils-libs.

### Security

Fixed CVE-2025-39998 in the Linux kernel.

### Security

Fixed CVE-2025-39996 in the Linux kernel.

### cos-dev-129-19340-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.54](https://cos.googlesource.com/third_party/kernel/+/cfe88d85f71d7502f55ff3e7ceebcb6c65f8b5bb ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19340.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.9. This adds support for installing drivers for GB 300 devices.

### Changed

Updated the Linux kernel to v6.12.54.

### Feature

Added GB300 support to cos-extensions.

### Fixed

Added support for NVIDIA driver v535.274.02 and v570.195.03.

### Fixed

Upgraded chromeos-base/google-breakpad to v2025.10.16.221019-r255.

### Fixed

Upgraded sys-apps/less to v685.

### Fixed

Upgraded sys-apps/pv to v1.9.44.

### Security

Fixed CVE-2025-11413 and CVE-2025-11414 in binutils-libs.

### cos-117-18613-439-9

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.111](https://cos.googlesource.com/third_party/kernel/+/4c5be9a246727bd6ede85b46b5df0625cb5ee48e ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.439.9/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated app-containers/runc to v1.2.7.

### Fixed

Added support for NVIDIA driver v535.274.02 and v570.195.03.

### Fixed

Upgraded sys-apps/hwdata to v0.400.

### Fixed

Upgraded sys-apps/less to v685.

### Security

Fixed CVE-2025-11413 and CVE-2025-11414 in binutils-libs.

### Security

Fixed CVE-2025-11494 in binutils-libs.

### Security

Fixed CVE-2025-11495 in binutils-libs.

### Security

Fixed CVE-2025-11412 in binutils-libs.

### cos-125-19216-0-115

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.46](https://cos.googlesource.com/third_party/kernel/+/6bf8e7e2ed9d2fd0a8381ab1bd6e659b24b01807 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.115/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.9. This adds support for installing drivers for GB 300 devices.

### Feature

Added GB300 support to cos-extensions.

### Fixed

Added support for NVIDIA driver v535.274.02 and v570.195.03.

### Fixed

Upgraded sys-apps/pv to v1.9.44.

### Security

Fixed CVE-2025-11413, CVE-2025-11414 in binutils-libs.

---
## 2025-10-24

### cos-125-19216-0-110

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.46](https://cos.googlesource.com/third_party/kernel/+/6bf8e7e2ed9d2fd0a8381ab1bd6e659b24b01807 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.110/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.8.

### Changed

Added support for A4X-Max NICs.

### Changed

Updated app-containers/runc to v1.2.7.

### Feature

Added support for NVIDIA GB300 devices.

### Fixed

Reduced gcr\_wait\_online retry gap.

### Fixed

Upgraded sys-apps/less to v685.

### Fixed

Upgraded sys-apps/pv to v1.9.42.

### Fixed

Upgraded sys-apps/hwdata to v0.400.

### Security

Fixed CVE-2025-11494 in binutils-libs.

### Security

Fixed CVE-2025-11495 in binutils-libs.

### Security

Fixed CVE-2025-11412 in binutils-libs.

### Changed

Runtime sysctl changes:

* Changed: net.ipv4.udp\_mem: 188034 250714 376068 -> 188034 250715 376068

### cos-dev-129-19334-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.53](https://cos.googlesource.com/third_party/kernel/+/873f2db84b5c40b7a0efab7db35eff2471f51e16 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19334.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.8.

### Changed

Added support for A4X-Max NICs.

### Changed

Updated app-containers/runc to v1.2.7.

### Feature

Added support for NVIDIA GB300 devices.

### Fixed

Upgraded sys-auth/pambase to v20251013.

### Fixed

Upgraded app-admin/google-guest-configs to v20251014.00.

### Fixed

Upgraded sys-apps/hwdata to v0.400.

### Fixed

Upgraded sys-apps/pv to v1.9.42.

### Security

Fixed CVE-2025-11494 in binutils-libs.

### Security

Fixed CVE-2025-11495 in binutils-libs.

### Security

Fixed CVE-2025-11412 in binutils-libs.

---
## 2025-10-20

### cos-117-18613-439-2

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.111](https://cos.googlesource.com/third_party/kernel/+/4c5be9a246727bd6ede85b46b5df0625cb5ee48e ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.439.2/lakitu/gpu_driver_versions.textproto) |

### Announcement

This is an [LTS Refresh release](https://cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases).

### Fixed

Reduced gcr\_wait\_online retry gap.

### Fixed

Added task information collection to sosreports.

### Fixed

Updated golang.org/x/crypto, golang.org/x/net, and
golang.org/x/oauth2 in kubelet and kubectl.

### Fixed

Upgraded app-admin/google-guest-configs to v20250805.00.

### Fixed

Upgraded dev-lang/go to v1.23.12.

### Fixed

Upgraded sys-apps/gentoo-functions to v1.7.4.

### Fixed

Upgraded net-nds/rpcbind to v1.2.8.

### Fixed

Upgraded dev-libs/expat to v2.7.3.

### Fixed

Upgraded app-admin/sudo to v1.9.17\_p2.

### Fixed

Upgraded dev-db/sqlite to v3.50.3.

### Security

Fixed CVE-2025-41244 in app-emulation/open-vm-tools.

### Security

Fixed KCTF-6bb73db in the Linux Kernel.

### Security

Fixed KCTF-cd8ae32 in the Linux kernel.

### Security

Fixed CVE-2025-39961 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811830 -> 811764

### cos-121-18867-199-105

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.105](https://cos.googlesource.com/third_party/kernel/+/0fa56c0469c8f8bfc8ec24e71a3ae959d3b750d3 ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.105/lakitu/gpu_driver_versions.textproto) |

### Fixed

Added task information collection to sosreports.

### Fixed

Updated golang.org/x/crypto, golang.org/x/net, and
golang.org/x/oauth2 in kubelet and kubectl.

### Security

Fixed CVE-2025-39970 in the Linux kernel.

### Security

Fixed CVE-2025-39975 in the Linux kernel.

### Security

Fixed CVE-2025-39968 in the Linux kernel.

### Security

Fixed CVE-2025-39998 in the Linux kernel.

### Security

Fixed CVE-2025-39971 in the Linux kernel.

### Security

Fixed CVE-2025-39972 in the Linux kernel.

### Security

Fixed CVE-2025-39969 in the Linux kernel.

### Security

Fixed CVE-2025-39980 in the Linux kernel.

### Security

Fixed CVE-2025-39977 in the Linux kernel.

### Security

Fixed KCTF-6bb73db in the Linux Kernel.

### Security

Fixed CVE-2025-39961 in the Linux kernel.

### Security

Fixed KCTF-cd8ae32 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811792 -> 811798

### cos-125-19216-0-100

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.46](https://cos.googlesource.com/third_party/kernel/+/6bf8e7e2ed9d2fd0a8381ab1bd6e659b24b01807 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.100/lakitu/gpu_driver_versions.textproto) |

### Security

Fixed CVE-2025-39992 in the Linux kernel.

### Security

Fixed CVE-2025-39990 in the Linux kernel.

### Security

Fixed CVE-2025-39998 in the Linux kernel.

### Security

Fixed CVE-2025-38322 in the Linux kernel.

### Security

Fixed CVE-2025-39977 in the Linux kernel.

### Security

Fixed CVE-2025-39973 in the Linux kernel.

### Security

Fixed CVE-2025-39969 in the Linux kernel.

### Security

Fixed CVE-2025-39940 in the Linux kernel.

### Security

Fixed CVE-2025-39971 in the Linux kernel.

### Security

Fixed CVE-2025-39972 in the Linux kernel.

### Security

Fixed CVE-2025-39975 in the Linux kernel.

### Security

Fixed CVE-2025-39980 in the Linux kernel.

### Security

Fixed CVE-2025-39984 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811534 -> 811421
* Changed: net.ipv4.udp\_mem: 188034 250715 376068 -> 188034 250714 376068

### cos-dev-129-19326-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.53](https://cos.googlesource.com/third_party/kernel/+/873f2db84b5c40b7a0efab7db35eff2471f51e16 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19326.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated the Linux kernel to v6.12.53.

### Fixed

Reduced gcr\_wait\_online retry gap.

### Fixed

Updated the dump capture kernel to v6.12.52.

### Fixed

Updated golang.org/x/crypto, golang.org/x/net, and
golang.org/x/oauth2 in kubelet and kubectl.

### Security

Fixed KCTF-6bb73db in the Linux Kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811438 -> 811426

### cos-113-18244-448-79

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.151](https://cos.googlesource.com/third_party/kernel/+/231e818dc133cd66210c238e1b21898bf6ffc3c6 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.79/lakitu/gpu_driver_versions.textproto) |

### Fixed

Reduced gcr\_wait\_online retry gap.

### Fixed

Added task information collection to sosreports.

### Security

Fixed CVE-2025-41244 in app-emulation/open-vm-tools.

### Security

Fixed CVE-2025-39977 in the Linux kernel.

### Security

Fixed CVE-2025-39980 in the Linux kernel.

### Security

Fixed KCTF-6bb73db in the Linux Kernel.

---
## 2025-10-17

### cos-125-19216-0-94

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.46](https://cos.googlesource.com/third_party/kernel/+/50e2212a52072ff4b0d0c40457be44291865fa70 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.94/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated the dump capture kernel to v6.12.52.

### Fixed

Added task information collection to sosreports.

### Fixed

Updated golang.org/x/crypto, golang.org/x/net, and
golang.org/x/oauth2 in kubelet and kubectl.

### Security

Fixed CVE-2025-41244 in app-emulation/open-vm-tools.

### Security

Fixed KCTF-6bb73db in the Linux Kernel.

### Security

Fixed CVE-2025-39963 in the Linux kernel.

### Security

Fixed CVE-2025-39965 in the Linux kernel.

### Security

Fixed CVE-2025-39961 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811514 -> 811534
* Changed: net.ipv4.udp\_mem: 188034 250714 376068 -> 188034 250715 376068

---
## 2025-10-13

### cos-dev-129-19319-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.50](https://cos.googlesource.com/third_party/kernel/+/3c1532a68eb1ef3c5e11dc5b860713612086c4ce ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19319.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated the Linux kernel to v6.12.50.

### Feature

Added support for NVIDIA driver v580.95.05. Updated all latest driver version and default driver versions for NVIDIA\_GB200 and NVIDIA\_B200 to v580.95.05.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.4.

### Fixed

Updated toolbox container image tag to v20251002.

### Fixed

Upgraded chromeos-base/google-breakpad to v2025.10.06.205107-r254.

### Fixed

Upgraded dev-libs/expat to v2.7.3.

### Fixed

Upgraded sys-apps/hwdata to v0.399.

### Fixed

Upgraded net-libs/libtirpc to v1.3.7.

### Fixed

Partially fixed an issue where excessive contention among writeback kworkers when switching a large number of inodes between cgroups could lead to system unresponsiveness.

### Security

Upgraded open-vm-tools to 13.0.5. This fixes CVE-2025-41244 in anthos variant.

### Security

Fixed CVE-2025-11081, CVE-2025-11082 and CVE-2025-11083 in sys-libs/binutils-libs.

### Security

Updated dev-python/urllib3 to v2.5.0. This resolves
CVE-2025-50181.

### Security

Updated sys-apps/coreutils to v9.5. This resolves
CVE-2024-0684.

### Security

Fixed KCTF-134121b in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811493 -> 811438
* Changed: net.ipv4.udp\_mem: 188034 250714 376068 -> 188034 250715 376068

### cos-121-18867-199-98

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.105](https://cos.googlesource.com/third_party/kernel/+/45bce2b8e465ad477610e2c5d7562a63161c2e93 ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.98/lakitu/gpu_driver_versions.textproto) |

### Feature

Added support for NVIDIA driver v580.95.05. Updated all latest driver version and default driver versions for NVIDIA\_GB200 and NVIDIA\_B200 to v580.95.05.

### Fixed

Upgraded app-admin/node-problem-detector to v0.8.22.

### Fixed

Updated toolbox container image tag to v20251002.

### Fixed

Upgraded sys-apps/hwdata to v0.399.

### Fixed

Partially fixed an issue where excessive contention among writeback kworkers when switching a large number of inodes between cgroups could lead to system unresponsiveness.

### Security

Fixed CVE-2025-41244 in app-emulation/open-vm-tools in
anthos variant.

### Security

Fixed CVE-2025-11081, CVE-2025-11082 and CVE-2025-11083 in sys-libs/binutils-libs.

### Security

Fixed CVE-2025-23143 in the Linux kernel.

### Security

Fixed CVE-2025-39947 in the Linux kernel.

### Security

Fixed KCTF-134121b in the Linux kernel.

### Security

Fixed CVE-2025-39931 in the Linux kernel.

### Security

Fixed CVE-2025-39953 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811724 -> 811792

### cos-125-19216-0-87

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.46](https://cos.googlesource.com/third_party/kernel/+/5ee1685d45ceceb19bdc81e90ae4e54c24ab561a ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.87/lakitu/gpu_driver_versions.textproto) |

### Feature

Added support for NVIDIA driver v580.95.05. Updated all latest driver version and default driver versions for NVIDIA\_GB200 and NVIDIA\_B200 to v580.95.05.

### Fixed

Upgraded app-admin/node-problem-detector to v0.8.22.

### Fixed

Upgraded sys-apps/hwdata to v0.399.

### Fixed

Partially fixed an issue where excessive contention among writeback kworkers when switching a large number of inodes between cgroups could lead to system unresponsiveness.

### Security

Fixed CVE-2025-11081, CVE-2025-11082 and CVE-2025-11083 in sys-libs/binutils-libs.

### Security

Fixed CVE-2025-39931 in the Linux kernel.

### Security

Fixed CVE-2025-39953 in the Linux kernel.

### Security

Fixed CVE-2025-39947 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811500 -> 811514

### cos-113-18244-448-73

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.151](https://cos.googlesource.com/third_party/kernel/+/5d50d9defad33f7338599079ca039107113994b5 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.73/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated toolbox container image tag to v20251002.

### Fixed

Upgraded sys-apps/hwdata to v0.399.

### Security

Fixed CVE-2025-11081, CVE-2025-11082 and CVE-2025-11083 in sys-libs/binutils-libs.

### Security

Fixed CVE-2025-23143 in the Linux kernel.

### Security

Fixed KCTF-134121b in the Linux kernel.

### Security

Fixed CVE-2025-39931 in the Linux kernel.

### Security

Fixed CVE-2025-39953 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811950 -> 812035

### cos-117-18613-339-97

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.105](https://cos.googlesource.com/third_party/kernel/+/66eb292ddbb8ce45011021bc66763a342024033e ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.97/lakitu/gpu_driver_versions.textproto) |

### Feature

Added support for NVIDIA driver v580.95.05. Updated all latest driver version and default driver versions for NVIDIA\_GB200 and NVIDIA\_B200 to v580.95.05.

### Fixed

Upgraded app-admin/node-problem-detector to v0.8.22.

### Security

Fixed CVE-2025-11081, CVE-2025-11082 and CVE-2025-11083 in sys-libs/binutils-libs.

### Security

Fixed CVE-2025-23143 in the Linux kernel.

### Security

Fixed CVE-2025-39947 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811755 -> 811830

---
## 2025-10-09

### cos-117-18613-339-89

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.105](https://cos.googlesource.com/third_party/kernel/+/2ffcc1008ec07bc0d54abf1e34ffa84d16b697cb ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.89/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated toolbox container image tag to v20251002.

### Fixed

Upgraded sys-apps/hwdata to v0.399.

### Fixed

Partially fixed the system not responding caused by excessive contention among writeback kworkers when switching a large number of inodes between cgroups.

### Security

Fixed KCTF-134121b in the Linux kernel.

### Security

Fixed CVE-2025-39953 in the Linux kernel.

### Security

Fixed CVE-2025-39931 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811788 -> 811755

### cos-125-19216-0-80

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.46](https://cos.googlesource.com/third_party/kernel/+/499c3487fad22aa2a6160db596030afb3de49edd ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.80/lakitu/gpu_driver_versions.textproto) |

### Announcement

Promoted Milestone 125 to stable.

### Security

Fixed KCTF-134121b in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811450 -> 811500
* Changed: net.ipv4.udp\_mem: 188034 250715 376068 -> 188034 250714 376068

### Changed

Updated toolbox container image tag to v20251002.

---
## 2025-10-06

### cos-beta-125-19216-0-76

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.46](https://cos.googlesource.com/third_party/kernel/+/63e0810f15dbfa9fb8126501f54ab3cfb234ca55 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.76/lakitu/gpu_driver_versions.textproto) |

### Feature

Configured the cos-gpu-installer to use R580 drivers as the
default GPU drivers.

### Fixed

Add support for NVIDIA MFT Tools v4.33.0.

### Security

Updated dev-python/urllib3 to v1.26.18 and fixed CVE-2025-50181.

### Security

Updated dev-python/jinja to v3.1.6. This resolves
CVE-2024-56326, CVE-2024-56201 and CVE-2025-27516.

### Security

Fixed CVE-2025-39913 in the Linux kernel.

### Security

Fixed CVE-2025-39914 in the Linux kernel.

### Security

Fixed CVE-2025-39911 in the Linux kernel.

### Security

Fixed CVE-2025-39926 in the Linux kernel.

### Security

Fixed CVE-2025-39917 in the Linux kernel.

### Security

Fixed CVE-2025-22106 in the Linux kernel.

### Security

Fixed KCTF-1b34cbb in the Linux kernel.

### Security

Fixed CVE-2025-39886 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811504 -> 811450

### cos-121-18867-199-88

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.105](https://cos.googlesource.com/third_party/kernel/+/b1375912423c5d03f213ed57baff26d12a3d6d79 ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.88/lakitu/gpu_driver_versions.textproto) |

### Fixed

Add support for NVIDIA MFT Tools v4.33.0.

### Security

Fixed CVE-2025-50181 in dev-python/urllib3.

### Security

Fixed CVE-2025-39914 in the Linux kernel.

### Security

Fixed CVE-2025-39913 in the Linux kernel.

### Security

Fixed CVE-2025-39911 in the Linux kernel.

### Security

Fixed CVE-2025-22106 in the Linux kernel.

### Security

Fixed KCTF-1b34cbb in the Linux kernel.

### Security

Fixed CVE-2025-39882 in the Linux kernel.

### Security

Fixed CVE-2025-39886 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811826 -> 811724

### cos-117-18613-339-84

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.105](https://cos.googlesource.com/third_party/kernel/+/82b411b602e6c923c1828944e6d849ba41f1eaa1 ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.84/lakitu/gpu_driver_versions.textproto) |

### Fixed

Add support for NVIDIA MFT Tools v4.33.0.

### Security

Fixed CVE-2025-50181 in dev-python/urllib3.

### Security

Fixed CVE-2025-39914 in the Linux kernel.

### Security

Fixed CVE-2025-39913 in the Linux kernel.

### Security

Fixed CVE-2025-39911 in the Linux kernel.

### Security

Fixed CVE-2025-22106 in the Linux kernel.

### Security

Fixed KCTF-1b34cbb in the Linux kernel.

### Security

Fixed CVE-2025-39882 in the Linux kernel.

### Security

Fixed CVE-2025-39886 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811817 -> 811788

### cos-dev-129-19302-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.49](https://cos.googlesource.com/third_party/kernel/+/bca084acf36df7105bde6e24bdee99b4cc82df6b ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19302.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated the Linux kernel to v6.12.49.

### Feature

Configured the cos-gpu-installer to use R580 drivers as the
default GPU drivers.

### Fixed

Add support for NVIDIA MFT Tools v4.33.0.

### Security

Updated dev-python/jinja to v3.1.6. This resolves
CVE-2024-56326, CVE-2024-56201 and CVE-2025-27516.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811490 -> 811493
* Changed: net.ipv4.udp\_mem: 188034 250715 376068 -> 188034 250714 376068

### cos-113-18244-448-63

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.151](https://cos.googlesource.com/third_party/kernel/+/9264165a8b85e3d390b9b1627029eb486d0b5a77 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.63/lakitu/gpu_driver_versions.textproto) |

### Security

Fixed CVE-2025-50181 in dev-python/urllib3.

### Security

Fixed CVE-2025-39914 in the Linux kernel.

### Security

Fixed CVE-2025-39913 in the Linux kernel.

### Security

Fixed KCTF-1b34cbb in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812039 -> 811950

---
## 2025-09-29

### cos-beta-125-19216-0-62

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.46](https://cos.googlesource.com/third_party/kernel/+/96bbdbf724fadf236b71f17314bc6e716a7e2031 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.62/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated app-admin/node-problem-detector to v0.8.21.

### Fixed

Updated golang.org/x/oauth2, golang.org/x/net,
golang.org/x/crypto, and github.com/golang-jwt/jwt/v5 in Docker.

### Security

Fixed CVE-2025-39882 in the Linux kernel.

### Security

Fixed KCTF-0aeb54a in the Linux Kernel.

### Security

Fixed CVE-2025-39884 in the Linux kernel.

### Security

Fixed CVE-2025-40300 in the Linux kernel.

### Security

Fixed CVE-2025-39881 in the Linux kernel.

### Security

Fixed CVE-2025-39883 in the Linux kernel.

### cos-dev-129-19290-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.48](https://cos.googlesource.com/third_party/kernel/+/062ea04d39b48ae7b92268575cd91677e97dd59d ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19290.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated the Linux kernel to v6.12.48.

### Feature

Added CPU balloon support for ARM CPUs.

### Feature

Added support for the fwctl subsystem and the Mellanox fwctl driver for ARM64.

### Fixed

Upgraded sys-auth/pambase to v20250906.

### Fixed

Upgraded app-admin/google-guest-configs to v20250913.00.

### Fixed

Upgraded dev-libs/expat to v2.7.2.

### Fixed

Updated golang.org/x/oauth2, golang.org/x/net, golang.org/x/crypto, and github.com/golang-jwt/jwt/v5 in Docker.

### cos-117-18613-339-77

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.105](https://cos.googlesource.com/third_party/kernel/+/38b7911a3e469f3db4aeeb6e29daae6617e47384 ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.77/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated golang.org/x/crypto, golang.org/x/net,
golang.org/x/oauth2, and github.com/golang-jwt/jwt/v4 in Docker.

### Security

Updated dev-python/jinja to v3.1.6. This resolves
CVE-2024-56326, CVE-2024-56201 and CVE-2025-27516.

### Security

Fixed KCTF-0aeb54a in the Linux Kernel.

### Security

Fixed CVE-2025-39881 in the Linux kernel.

### Security

Fixed CVE-2025-39883 in the Linux kernel.

### Security

Fixed CVE-2025-40300 in the Linux kernel.

### cos-113-18244-448-58

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.151](https://cos.googlesource.com/third_party/kernel/+/cdea5873474cabb0b26402f65fdcc1df608af567 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.58/lakitu/gpu_driver_versions.textproto) |

### Fixed

Added support for NVIDIA driver v580.82.07.
Updated all latest driver version and default driver
versions for NVIDIA\_B200 to v580.82.07.

### Security

Updated dev-python/jinja to v3.1.6. This resolves
CVE-2024-56326, CVE-2024-56201 and CVE-2025-27516.

### Security

Fixed KCTF-0aeb54a in the Linux Kernel.

### Security

Fixed CVE-2025-39881 in the Linux kernel.

### Security

Fixed CVE-2025-39883 in the Linux kernel.

### Security

Fixed CVE-2025-40300 in the Linux kernel.

### cos-121-18867-199-80

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.105](https://cos.googlesource.com/third_party/kernel/+/0e0315b16868f789862900711ad3d92750ea17c5 ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.80/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated golang.org/x/oauth2, golang.org/x/net,
golang.org/x/crypto, and github.com/golang-jwt/jwt/v5 in Docker.

### Security

Updated dev-python/jinja to v3.1.6. This resolves
CVE-2024-56326, CVE-2024-56201 and CVE-2025-27516.

### Security

Fixed KCTF-0aeb54a in the Linux Kernel.

### Security

Fixed CVE-2025-39881 in the Linux kernel.

### Security

Fixed CVE-2025-39883 in the Linux kernel.

### Security

Fixed CVE-2025-40300 in the Linux kernel.

---
## 2025-09-24

### cos-beta-125-19216-0-53

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.46](https://cos.googlesource.com/third_party/kernel/+/6963667c07329fd67fdfa97b2c039c916e93a348 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.53/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.7.

### Feature

Added support for the fwctl subsystem and the Mellanox fwctl driver for ARM64.

### Fixed

Added support for NVIDIA driver v580.82.07.
Updated all latest driver version and default driver
versions for NVIDIA\_GB200 and NVIDIA\_B200 to v580.82.07.

### Fixed

Upgraded dev-libs/libxslt to version 1.1.43-r1.

### Fixed

Updated the Linux kernel to v6.12.46.

### Security

Upgraded dev-libs/libxml2 to version 2.13.9. This fixes
CVE-2025-9714.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811500 -> 811534

### Changed

Enabled Coherent Driver Memory Management by default when installing GPU drivers on GB2000.

### cos-117-18613-339-70

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.105](https://cos.googlesource.com/third_party/kernel/+/6132d6c35a2b10e178a2cc0eb1df4f55ed0bea3e ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.70/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.7.

### Fixed

Updated golang.org/x/crypto in google-osconfig-agent to v0.31.0.

### Fixed

Added support for NVIDIA driver v580.82.07.
Updated all latest driver version and default driver
versions for NVIDIA\_GB200 and NVIDIA\_B200 to v580.82.07.

### Fixed

Upgraded dev-libs/libxslt to version 1.1.43-r1.

### Fixed

Updated the Linux kernel to v6.6.105.

### Security

Upgraded dev-libs/libxml2 to version 2.13.9. This fixes
CVE-2025-9714.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811774 -> 811794

### Changed

Enabled Coherent Driver Memory Management by default when installing GPU drivers on GB2000.

### cos-113-18244-448-50

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.151](https://cos.googlesource.com/third_party/kernel/+/cf1698d307efdf83b0d49811c6702f5c476d3347 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.50/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.7.

### Fixed

Updated golang.org/x/crypto in google-guest-agent to v0.31.0.

### Fixed

Updated golang.org/x/crypto in google-osconfig-agent to v0.31.0.

### Fixed

Upgraded dev-libs/libxslt to version 1.1.43-r1.

### Fixed

Updated the Linux kernel to v6.1.151.

### Security

Upgraded dev-libs/libxml2 to version 2.13.9. This fixes
CVE-2025-9714.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811983 -> 812054

### Changed

Enabled Coherent Driver Memory Management by default when installing GPU drivers on GB2000.

### cos-dev-129-19284-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.47](https://cos.googlesource.com/third_party/kernel/+/cae186e568245769d61ab1cff0f14366822276c7 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19284.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.7.

### Changed

Updated the Linux kernel to v6.12.47.

### Fixed

Added support for NVIDIA driver v580.82.07.
Updated all latest driver version and default driver
versions for NVIDIA\_GB200 and NVIDIA\_B200 to v580.82.07.

### Fixed

Upgraded dev-libs/libxslt to version 1.1.43-r1.

### Security

Upgraded dev-libs/libxml2 to version 2.13.9. This fixes
CVE-2025-9714, CVE-2025-32415 and CVE-2025-32414.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811423 -> 811483
* Changed: net.ipv4.udp\_mem: 188034 250715 376068 -> 188034 250714 376068

### Changed

Enabled Coherent Driver Memory Management by default when installing GPU drivers on GB2000.

### cos-109-17800-570-50

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.151](https://cos.googlesource.com/third_party/kernel/+/a4114b18351d2a6e0d84a3c7b02e4513ced87fcf ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.50/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.7.

### Fixed

Updated golang.org/x/crypto in google-osconfig-agent to v0.31.0.

### Fixed

Upgraded dev-libs/libxslt to version 1.1.43-r1.

### Fixed

Updated the Linux kernel to v6.1.151.

### Security

Upgraded dev-libs/libxml2 to version 2.13.9. This fixes
CVE-2025-9714.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812272 -> 812258

### Changed

Enabled Coherent Driver Memory Management by default when installing GPU drivers on GB2000.

### cos-121-18867-199-73

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.105](https://cos.googlesource.com/third_party/kernel/+/6b5ca3235d0b2ee0728b27431e9c285a91583f4c ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.73/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.7.

### Fixed

Added support for NVIDIA driver v580.82.07. Updated all latest driver version and default driver versions for NVIDIA\_GB200 and NVIDIA\_B200 to v580.82.07.

### Fixed

Upgraded dev-libs/libxslt to version 1.1.43-r1.

### Security

Upgraded dev-libs/libxml2 to version 2.13.9. This fixes
CVE-2025-9714.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811710 -> 811752

### Changed

Enabled Coherent Driver Memory Management by default when installing GPU drivers on GB2000.

---
## 2025-09-16

### cos-121-18867-199-65

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.105](https://cos.googlesource.com/third_party/kernel/+/6b5ca3235d0b2ee0728b27431e9c285a91583f4c ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.65/lakitu/gpu_driver_versions.textproto) |

### Feature

Added GDRCopy kernel module for NVIDIA drivers.

### Feature

Added support for NVIDIA MFT Tools on arm64.

### Fixed

Updated the Linux kernel to v6.6.105.

### Security

Fixed CVE-2025-39782 in the Linux kernel.

### Security

Fixed CVE-2025-38608 in the Linux kernel.

### Security

Fixed CVE-2025-38622 in the Linux kernel.

### Security

Fixed CVE-2025-38639 in the Linux kernel.

### Security

Fixed CVE-2025-38572 in the Linux kernel.

### Security

Fixed CVE-2025-38588 in the Linux kernel.

### Security

Fixed CVE-2025-38349 in the Linux kernel.

### Security

Fixed CVE-2025-38550 in the Linux kernel.

### Security

Fixed CVE-2025-38568 in the Linux kernel.

### Security

Fixed CVE-2025-38645 in the Linux kernel.

### Security

Fixed CVE-2025-38640 in the Linux kernel.

### Security

Fixed CVE-2025-38528 in the Linux kernel.

### Security

Fixed CVE-2025-38563 in the Linux kernel.

### Security

Fixed CVE-2025-38539 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811788 -> 811710

### cos-117-18613-339-65

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/125bc228c1f1f826079ca5f36f78bb09932bb486 ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.65/lakitu/gpu_driver_versions.textproto) |

### Feature

Added GDRCopy kernel module for NVIDIA drivers.

### Feature

Added support for NVIDIA MFT Tools on arm64.

### Security

Fixed CVE-2025-38588 in the Linux kernel.

### Security

Fixed CVE-2025-38622 in the Linux kernel.

### Security

Fixed CVE-2025-38608 in the Linux kernel.

### Security

Fixed CVE-2025-38587 in the Linux kernel.

### Security

Fixed CVE-2025-38527 in the Linux kernel.

### Security

Fixed CVE-2025-38571 in the Linux kernel.

### Security

Fixed CVE-2025-38572 in the Linux kernel.

### Security

Fixed CVE-2025-38566 in the Linux kernel.

### Security

Fixed CVE-2025-38568 in the Linux kernel.

### Security

Fixed CVE-2025-38565 in the Linux kernel.

### Security

Fixed CVE-2025-38639 in the Linux kernel.

### Security

Fixed CVE-2025-38645 in the Linux kernel.

### Security

Fixed CVE-2025-38640 in the Linux kernel.

### Security

Fixed CVE-2025-38528 in the Linux kernel.

### Security

Fixed CVE-2025-38539 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811749 -> 811774

### cos-beta-125-19216-0-47

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.41](https://cos.googlesource.com/third_party/kernel/+/fcd7852f14840b42feeae954c5e2b8d5b3da6958 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.47/lakitu/gpu_driver_versions.textproto) |

### Fixed

Fixed a kernel bug which caused boot to fail for n4 machine types.

### Feature

Added GDRCopy kernel module for NVIDIA drivers.

### Feature

Added support for NVIDIA MFT Tools on arm64.

### Security

Fixed CVE-2025-38640 in the Linux kernel.

### Security

Fixed CVE-2025-38614 in the Linux kernel.

### Security

Fixed CVE-2025-38587 in the Linux kernel.

### Security

Fixed CVE-2025-38588 in the Linux kernel.

### Security

Fixed CVE-2025-38572 in the Linux kernel.

### Security

Fixed CVE-2025-38622 in the Linux kernel.

### Security

Fixed CVE-2025-38608 in the Linux kernel.

### Security

Fixed CVE-2025-38565 in the Linux kernel.

### Security

Fixed CVE-2025-38645 in the Linux kernel.

### Security

Fixed CVE-2025-38571 in the Linux kernel.

### Security

Fixed CVE-2025-38568 in the Linux kernel.

### Security

Fixed CVE-2025-38639 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811507 -> 811500

### cos-113-18244-448-43

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.144](https://cos.googlesource.com/third_party/kernel/+/e585ffc1d4d502fa00b73b252e2d9076f070513d ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.43/lakitu/gpu_driver_versions.textproto) |

### Feature

Added GDRCopy kernel module for NVIDIA drivers.

### Feature

Added IPv6 support for machines using the IDPF driver.

### Security

Fixed CVE-2025-38608 in the Linux kernel.

### Security

Fixed CVE-2025-38639 in the Linux kernel.

### Security

Fixed CVE-2025-38572 in the Linux kernel.

### Security

Fixed CVE-2025-38553 in the Linux kernel.

### Security

Fixed CVE-2025-38550 in the Linux kernel.

### Security

Fixed CVE-2025-38588 in the Linux kernel.

### Security

Fixed CVE-2025-38587 in the Linux kernel.

### Security

Fixed CVE-2025-38527 in the Linux kernel.

### Security

Fixed CVE-2025-38622 in the Linux kernel.

### Security

Fixed CVE-2025-38528 in the Linux kernel.

### Security

Fixed CVE-2025-38563 in the Linux kernel.

### Security

Fixed CVE-2025-38565 in the Linux kernel.

### Security

Fixed CVE-2025-38539 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812017 -> 811983

### cos-109-17800-570-46

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/21a09914420b38facc9d5d41d6790e66c9786c31 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.46/lakitu/gpu_driver_versions.textproto) |

### Feature

Added GDRCopy kernel module for NVIDIA drivers.

### Security

Fixed CVE-2025-38608 in the Linux kernel.

### Security

Fixed CVE-2025-38639 in the Linux kernel.

### Security

Fixed CVE-2025-38622 in the Linux kernel.

### Security

Fixed CVE-2025-38572 in the Linux kernel.

### Security

Fixed CVE-2025-38588 in the Linux kernel.

### Security

Fixed CVE-2025-38565 in the Linux kernel.

### Security

Fixed CVE-2025-38587 in the Linux kernel.

### Security

Fixed CVE-2025-38539 in the Linux kernel.

### Security

Fixed CVE-2025-38645 in the Linux kernel.

### Security

Fixed CVE-2025-38528 in the Linux kernel.

### Security

Fixed CVE-2025-38527 in the Linux kernel.

### Security

Fixed CVE-2025-38553 in the Linux kernel.

### Security

Fixed CVE-2025-38550 in the Linux kernel.

### Security

Fixed CVE-2025-38563 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812270 -> 812272

### cos-dev-129-19279-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.46](https://cos.googlesource.com/third_party/kernel/+/345ad6a408b0f8b808d2818aafac95e470de47c1 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19279.0.0/lakitu/gpu_driver_versions.textproto) |

### Fixed

Fixed a kernel bug which caused boot to fail for n4 machine types.

### Changed

Updated the Linux kernel to v6.12.46.

### Feature

Added GDRCopy kernel module for NVIDIA drivers.

### Feature

Added support for NVIDIA MFT Tools on arm64.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811510 -> 811423

---
## 2025-09-08

### cos-dev-129-19271-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.43](https://cos.googlesource.com/third_party/kernel/+/e342d60a146658d84ddceee66940ed6686f19d93 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19271.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Added kernel support for bare-metal on the NVIDIA Grace platform.

### Changed

Updated the Linux kernel to v6.12.43.

### Feature

Added iRDMA support in the Linux kernel.

### Feature

Enabled dynamic vlan configuration for non-primary NICs.

### Feature

Added TDX RTMR support.

### Feature

Disabled DNSSEC by default for COS TPU VMs.

### Feature

Added IPv6 support for machines using the IDPF driver.

### Fixed

Upgraded sys-auth/pambase to v20250826.

### Fixed

Upgraded app-admin/google-guest-configs to v20250826.00.

### Fixed

Upgraded app-admin/google-guest-configs to v20250818.00.

### Fixed

Installed app-misc/c\_rehash.

### Fixed

Upgraded chromeos-base/google-breakpad to v2025.08.18.161925-r245.

### Fixed

Upgraded sys-apps/file to v5.46-r3.

### Fixed

Upgraded sys-apps/hwdata to v0.398.

### Fixed

Fixed an issue where cpusets cgroups did not work with
cgroup v1 enabled.

### Security

Fixed CVE-2025-6052 in dev-libs/glib.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811419 -> 811510

### cos-beta-125-19216-0-38

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.41](https://cos.googlesource.com/third_party/kernel/+/15fd269cbaf8aa5f8f789db43e9a49c81fc9f3ab ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.38/lakitu/gpu_driver_versions.textproto) |

### Feature

Added NVIDIA GPU driver's R580 branch. Updated the LATEST GPU driver label to version 580.65.06.

### Fixed

Disabled network management by the google-guest-agent.

### Security

Fixed CVE-2025-38676 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811504 -> 811507

### cos-117-18613-339-56

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/834e8ff60aef5342c81ec8c298c3f054111c4988 ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.56/lakitu/gpu_driver_versions.textproto) |

### Security

Fixed CVE-2025-38351 in the Linux kernel.

### Security

Fixed CVE-2025-38676 in the Linux kernel.

### Security

Fixed CVE-2025-38322 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811812 -> 811749

### cos-113-18244-448-39

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.144](https://cos.googlesource.com/third_party/kernel/+/7415e491350efbbbae38329dd16ecd79204ebe04 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.39/lakitu/gpu_driver_versions.textproto) |

### Security

Fixed CVE-2025-38676 in the Linux kernel.

### Security

Fixed CVE-2025-38322 in the Linux kernel.

### Security

Fixed CVE-2024-58240 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812049 -> 812017

### cos-109-17800-570-43

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/251d4a8789b175c70dd0bc30d661571ca4535092 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.43/lakitu/gpu_driver_versions.textproto) |

### Security

Fixed CVE-2025-38676 in the Linux kernel.

### Security

Fixed CVE-2025-38322 in the Linux kernel.

### Security

Fixed CVE-2024-58240 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812262 -> 812270

### cos-121-18867-199-56

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/a87b591aba20e05799cce15bd37bcaeb7adc682e ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.56/lakitu/gpu_driver_versions.textproto) |

### Fixed

Upgraded sys-apps/file to v5.46-r3.

### Security

Fixed CVE-2025-38351 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811774 -> 811788

---
## 2025-09-02

### cos-beta-125-19216-0-33

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.41](https://cos.googlesource.com/third_party/kernel/+/63514cac0bb36911759fd907b87c654e5fed76d7 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.33/lakitu/gpu_driver_versions.textproto) |

### Feature

Added iRDMA support in the Linux kernel.

### Feature

Enabled dynamic vlan configuration for non-primary NICs.

### Fixed

Added support for the Lustre 2.14.0\_p216 drivers.

### Fixed

Upgraded sys-apps/file to v5.46-r3.

### Fixed

Upgraded sys-apps/hwdata to v0.398.

### Security

Fixed CVE-2025-6052 in dev-libs/glib.

### Security

Fixed KCTF-aba0c94 in the Linux kernel.

### Security

Fixed KCTF-62708b9 in the Linux kernel.

### Security

Fixed KCTF-6db015f in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811541 -> 811504

### cos-117-18613-339-52

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/8336c891d963e19a50f4bd8fc085852b3153ec4d ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.52/lakitu/gpu_driver_versions.textproto) |

### Fixed

Upgraded sys-apps/hwdata to v0.398.

### Fixed

Upgraded sys-apps/file to v5.46-r3.

### Security

Fixed CVE-2025-6052 in dev-libs/glib.

### Security

Fixed KCTF-aba0c94 in the Linux kernel.

### Security

Fixed KCTF-62708b9 in the Linux kernel.

### Security

Fixed KCTF-6db015f in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811728 -> 811812

### cos-121-18867-199-52

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/e6bcea4bc13acfe8bb9c88cc70784179495c68da ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.52/lakitu/gpu_driver_versions.textproto) |

### Fixed

Upgraded sys-apps/hwdata to v0.398.

### Security

Fixed CVE-2025-6052 in dev-libs/glib.

### Security

Fixed KCTF-aba0c94 in the Linux kernel.

### Security

Fixed KCTF-62708b9 in the Linux kernel.

### Security

Fixed KCTF-6db015f in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811817 -> 811774

### cos-113-18244-448-36

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.144](https://cos.googlesource.com/third_party/kernel/+/f3d65b53d35602dba107732c8ff74246ec37c54c ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.36/lakitu/gpu_driver_versions.textproto) |

### Fixed

Upgraded sys-apps/file to v5.46-r3.

### Fixed

Upgraded sys-apps/hwdata to v0.398.

### Security

Fixed KCTF-62708b9 in the Linux kernel.

### Security

Fixed KCTF-aba0c94 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812035 -> 812049

### cos-109-17800-570-40

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/7ee6ea59a506ec4129b6bd62e046f8d180705344 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.40/lakitu/gpu_driver_versions.textproto) |

### Security

Fixed KCTF-62708b9 in the Linux kernel.

### Security

Fixed KCTF-aba0c94 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812214 -> 812262

---
## 2025-08-25

### cos-beta-125-19216-0-24

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.41](https://cos.googlesource.com/third_party/kernel/+/02d39c3c0c9c42945d7d727b09fd66a344ac6fb8 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.24/lakitu/gpu_driver_versions.textproto) |

### Changed

Added kernel support for bare-metal on the NVIDIA Grace platform.

### Feature

Added TDX RTMR support.

### Feature

Removed the cloud-final.service dependency on multi-user.target which could delay cloud-init user-data scripts indefinitely when long-running startup scripts are used.

### Feature

Disabled DNSSEC by default for COS TPU VMs.

### Feature

Added IPv6 support for machines using the IDPF driver.

### Feature

Enabled the google-guest-agent's network management functionality.

### Feature

Added ConnectX-8 RDMA support.

### Fixed

Installed app-misc/c\_rehash.

### Fixed

Fixed an issue where cpusets cgroups did not work with
cgroup v1 enabled.

### Security

Fixed KCTF-abad3d0 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811484 -> 811541

### cos-121-18867-199-43

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/deeeb8e797576b7e1e58e75b8b6d20d26d3ea7ab ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.43/lakitu/gpu_driver_versions.textproto) |

### Feature

Disabled DNSSEC by default for COS TPU VMs.

### Feature

Added IPv6 support for machines using the IDPF driver.

### Fixed

Added support for the Lustre 2.14.0\_p216 drivers.

### Security

Fixed KCTF-abad3d0 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811736 -> 811817

### cos-117-18613-339-44

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/dbb5daa347de068ce303416670bb9f859074ea88 ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.44/lakitu/gpu_driver_versions.textproto) |

### Feature

Disabled DNSSEC by default for COS TPU VMs.

### Feature

Added IPv6 support for machines using the IDPF driver.

### Fixed

Added support for the Lustre 2.14.0\_p216 drivers.

### Security

Fixed KCTF-abad3d0 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811771 -> 811728

### cos-dev-129-19251-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.42](https://cos.googlesource.com/third_party/kernel/+/bb106cd2966ddeca447529bc878f7ec95ed4e9c2 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19251.0.0/lakitu/gpu_driver_versions.textproto) |

### Fixed

Added support for the Lustre 2.14.0\_p216 drivers.

### Security

Fixed KCTF-abad3d0 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811494 -> 811419

### cos-113-18244-448-33

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.144](https://cos.googlesource.com/third_party/kernel/+/be0696379db5a3b49f401e243d019e6df00a0504 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.33/lakitu/gpu_driver_versions.textproto) |

### Feature

Disabled DNSSEC by default for COS TPU VMs.

### Security

Fixed KCTF-abad3d0 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812040 -> 812035

### cos-109-17800-570-37

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/69a4dc1bdd77106e675905e62d935738f80567d2 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.37/lakitu/gpu_driver_versions.textproto) |

### Feature

Disabled DNSSEC by default for COS TPU VMs.

### Security

Fixed KCTF-abad3d0 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812258 -> 812214

---
## 2025-08-18

### cos-beta-125-19216-0-12

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.41](https://cos.googlesource.com/third_party/kernel/+/cb97b1d56434861bfcd63c64497d0b8580f58508 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19216.0.12/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated containerd to v2.1.3.

### Changed

Updated the NVIDIA GPU driver policy for New Feature Branch (NFB) drivers. The LATEST tag has been updated to point to the stable 570.133.20 Production Branch. The 575.57.08 NFB driver remains available for development and testing but must now be selected by its specific version number.Removed 575.57.08 NFB driver support for NVIDIA\_GB200 machine.

### Changed

Upgraded nvidia-container-toolkit to v1.17.8. This fixes CVE-2025-23266.

### Changed

Updated cos-gpu-installer to v2.5.5.

### Changed

Upgraded the Linux kernel to version 6.12.

### Changed

Upgrade dpdk-kmods to 9b182be2ee4b.

### Changed

Added support for 7th generation TPU devices.

### Changed

Patched a null ptr exception bug in NVIDIA 570.124.06 OSS driver.

### Changed

iptables-restore.service to start after ipset.service.

### Changed

Fixed an issue that resulted in missing grub boot measurements in some machine configurations.

### Changed

Updated Python to v3.11.

### Changed

Upgraded app-containers/docker to v27.5.1, Upgraded app-containers/docker-test to v27.5.1, Upgraded app-containers/docker-cli to v27.5.1.

### Changed

Updated the default tag of the GPU driver supporting the NVIDIA H200 GPU device to 570.86.15.

### Changed

Upgrade cloud-init to v24.4.1.

### Feature

Backported support for AMD SEV-SNP SVSM vTPM driver and
configfs-tsm addition for extended attestation protocol.

### Feature

Added ARM support for the Lustre v2.14.0 drivers.

### Feature

Added NVIDIA 570.133.20 vGPU driver.

### Feature

Added support for Nvidia driver version 575.57.08. Added support for NVIDIA\_RTX\_PRO\_6000 devices.

### Feature

Supported NVIDIA MFT Tools on COS.

### Feature

Injected IMEX channel char device for GB200 GPUs.

### Feature

Fixed an issue in containerd that potentially breaks metric collection.

### Feature

Fixed an issue in containerd that prevented some v2 shims from shutting down properly.

### Feature

Added support for NVIDIA GB200 GPU with 570.124.06 GPU driver. This driver version has been assigned the latest, default, and R570 tags for this GPU type.

### Feature

Add support for iRDMA devices.

### Feature

Updated cos-gpu-installer to v2.4.8: Add the -skip-nvidia-smi flag to disable the execution of nvidia-smi verification during gpu driver installation.

### Feature

Applied Intel patches to add iRDMA support in the Linux kernel.

### Fixed

Removed an artifact registry ping that would delay multi-user.target indefinitely for machines with no external IP address.

### Fixed

Reverted a containerd change which reduced the default soft file descriptor limit for processes in containers to 1024.

### Fixed

Upgraded app-admin/google-guest-configs to v20250718.00.

### Fixed

Added support for the Lustre 2.14.0\_p212 drivers.

### Fixed

Fixed docker MTU mismatch.

### Fixed

Increased kdump memory reservation.

### Fixed

Fixed issue where modinfo could not display module signatures.

### Fixed

Upgraded app-admin/google-guest-agent to v20250418.00.

### Fixed

Upgraded sys-apps/makedumpfile to v1.7.7.

### Fixed

Modified toolbox to use unified cgroup hierarchy mode instead of hybrid mode when possible.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.3.

### Fixed

Fixed EINTR error in app-container/cni-plugins.

### Fixed

Upgraded sys-auth/pambase to v20250228.

### Fixed

Disabled martian logging for ConnectX-7 network cards. These cards only communicate locally, but martian logging during communications with the host can lead to a race condition which causes GID table construction to sometimes fail.

### Fixed

Upgraded app-containers/runc to v1.2.5, Upgraded app-containers/runc-test to v1.2.5.

### Fixed

Upgraded app-admin/node-problem-detector to v0.8.20.

### Fixed

Upgraded app-admin/fluent-bit to v3.2.5.

### Fixed

Upgraded chromeos-base/google-breakpad to v2025.07.23.214511-r244.

### Fixed

Upgraded chromeos-base/minijail to v18-r168.

### Fixed

Upgraded dev-libs/openssl to 3.5.1.

### Fixed

Upgraded dev-lang/go to v1.23.11.

### Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4879.

### Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r667.

### Fixed

Upgraded chromeos-base/session\_manager-client to v0.0.1-r2830.

### Fixed

Upgraded chromeos-base/power\_manager-client to v0.0.1-r2969.

### Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2734.

### Fixed

Upgraded sys-apps/rootdev to v0.0.1-r51.

### Fixed

Upgraded sys-apps/dbus to v1.16.2-r197.

### Fixed

Upgraded app-benchmarks/microbenchmarks to v0.0.1-r20.

### Fixed

Upgraded chromeos-base/update\_engine-client to v0.0.1-r2480.

### Fixed

Updated dev-python/requests to v2.32.4.

### Fixed

Upgraded net-misc/openssh to 10.0\_p1.

### Fixed

Upgraded dev-db/sqlite to v3.50.3.

### Fixed

Upgraded virtual/logger to v0-r2.

### Fixed

Upgraded sys-apps/pv to v1.9.34.

### Fixed

Upgraded app-admin/sudo to v1.9.17\_p2.

### Fixed

Upgraded sys-process/lsof to v4.99.5.

### Fixed

Updated app-misc/jq to v1.8.1.

### Fixed

Upgraded sys-apps/less to v679.

### Fixed

Upgraded sys-process/procps to v4.0.5-r2.

### Fixed

Upgraded sys-libs/libcap to v2.76.

### Fixed

Upgraded sys-apps/ethtool to version 6.11.

### Fixed

Upgraded app-arch/gzip to v1.14.

### Fixed

Upgraded net-dns/libidn2 to v2.3.8.

### Fixed

Upgraded sys-apps/grep to v3.12.

### Fixed

Upgraded sys-apps/diffutils to v3.11-r2.

### Fixed

Upgraded net-nds/rpcbind to v1.2.7.

### Fixed

Upgraded net-misc/rsync to v3.4.1.

### Fixed

Upgraded dev-libs/nss to v3.110.

### Fixed

Upgraded sys-libs/libseccomp to v2.6.0-r2.

### Fixed

Upgraded dev-libs/expat to v2.7.1.

### Fixed

Upgraded app-arch/unzip to v6.0\_p29.

### Fixed

Upgraded sys-apps/acl to v2.3.2-r2.

### Fixed

Updated dev-python/s3transfer to v0.11.4.

### Fixed

Updated dev-python/botocore to v1.37.9.

### Fixed

Updated dev-python/python-dateutil to v2.9.0.

### Fixed

Upgraded sys-apps/which to v2.23.

### Fixed

Upgraded dev-libs/double-conversion to v3.3.1.

### Fixed

Upgraded net-misc/socat to v1.8.0.3.

### Fixed

Upgraded sys-apps/hwdata to v0.391.

### Fixed

Upgraded sysram to version 6.12-0.

### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Security

Upgraded net-misc/netplan to v1.1.2. This fixes
CVE-2022-4968.

### Security

Fixed CVE-2024-6174 and CVE-2024-11584 in cloud-init.

### Security

Fixed CVE-2025-47273 in dev-python/setuptools.

### Security

Updated systemd to v254.26. This resolves CVE-2025-4598.

### Security

Updated apparmor to v3.1.6. This fixes CVE-2016-1585.

### Security

Update NVIDIA GPU drivers to v535.247.01 for default/ R535
and v570.133.20 for latest/R570. This resolves CVE‑2025‑23244.

### Security

Fixed CVE-2025-8058 in glibc.

### Security

Upgraded dev-libs/glib to 2.82.5. This resolves
CVE-2024-52533.

### Security

Patched openssl to fix CVE-2023-50782 affecting
dev-python/crytography.

### Security

Updated dev-go/net in policy manager to v0.39.0. This fixes CVE-2025-22870.

### Security

Upgraded dev-go/crypto to v0.35.0. This fixes CVE-2025-22869.

### Security

Updated dev-go/oauth2 to v0.27.0. Fixes CVE-2025-22868.

### Security

Fixed CVE-2024-13176 in dev-libs/openssl.

### Security

Fixed CVE-2025-0395 in sys-libs/glibc.

### Security

Fixed CVE-2024-9287 in dev-lang/python.

### Security

Fixed CVE-2025-0840 in binutils.

### Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Security

Fixed CVE-2024-26130 in dev-python/cryptography.

### Security

Updated app-editors/nano to v8.5. This resolves
CVE-2024-5742.

### Security

Upgraded vim, vim-core to
version 9.1.1500. This fixes CVE-2025-26603, CVE-2025-27423,
CVE-2025-29768, CVE-2025-1215, CVE-2025-24014, CVE-2025-22134.

### Security

Upgrade libarchive to v3.8.1. This fixes CVE-2025-5914.

### Security

Upgraded elfutils to v0.193. This fixes CVE-2025-1365, CVE-2025-1371, CVE-2025-1372, and CVE-2025-1377.

### Security

Fixed CVE-2024-23337 in app-misc/jq.

### Security

Upgraded net-misc/curl to v8.12.1. This fixes CVE-2025-0167.

### Security

Fixed CVE-2025-46836 in sys-apps/net-tools

### Security

Fixed CVE-20250-3198 in sys-libs/bintuils-libs.

### Security

Fix CVE-2025-32414, CVE-2025-32415 in dev-libs/libxml2.

### Security

Fixed CVE-2025-32728 in net-misc/openssh.

### Security

Fixed CVE-2024-53427 in app-misc/jq.

### Security

Fixed CVE-2025-31498 in net-dns/c-ares.

### Security

Fixed CVE-2024-48615 in app-arch/libarchive.

### Security

Upgraded net-misc/wget to v1.25.0. This fixes CVE-2024-10524.

### Security

Upgraded dev-libs/libxml2 to v1.12.10. Fixes CVE-2025-27113.

### Changed

Runtime sysctl changes:

* Added: kernel.apparmor\_restrict\_unprivileged\_unconfined: 0
* Added: kernel.core\_file\_note\_size\_limit: 4194304
* Added: kernel.core\_sort\_vma: 0
* Added: net.ipv4.fib\_multipath\_hash\_seed: 0
* Added: net.ipv4.tcp\_pingpong\_thresh: 1
* Added: net.ipv6.conf.all.ra\_honor\_pio\_life: 0
* Added: net.ipv6.conf.all.ra\_honor\_pio\_pflag: 0
* Added: net.ipv6.conf.all.regen\_min\_advance: 2
* Added: net.ipv6.conf.default.ra\_honor\_pio\_life: 0
* Added: net.ipv6.conf.default.ra\_honor\_pio\_pflag: 0
* Added: net.ipv6.conf.default.regen\_min\_advance: 2
* Added: net.ipv6.conf.docker0.ra\_honor\_pio\_life: 0
* Added: net.ipv6.conf.docker0.ra\_honor\_pio\_pflag: 0
* Added: net.ipv6.conf.docker0.regen\_min\_advance: 2
* Added: net.ipv6.conf.eth0.ra\_honor\_pio\_life: 0
* Added: net.ipv6.conf.eth0.ra\_honor\_pio\_pflag: 0
* Added: net.ipv6.conf.eth0.regen\_min\_advance: 2
* Added: net.ipv6.conf.lo.ra\_honor\_pio\_life: 0
* Added: net.ipv6.conf.lo.ra\_honor\_pio\_pflag: 0
* Added: net.ipv6.conf.lo.regen\_min\_advance: 2
* Added: vm.enable\_soft\_offline: 1
* Changed: fs.epoll.max\_user\_watches: 1809007 -> 1808517
* Changed: fs.fanotify.max\_user\_marks: 67544 -> 68412
* Changed: fs.file-max: 811774 -> 811484
* Changed: fs.inotify.max\_user\_watches: 63425 -> 64189
* Changed: kernel.threads-max: 63487 -> 63178
* Changed: net.ipv4.tcp\_mem: 94041 125391 188082 -> 94017 125357 188034
* Changed: net.ipv4.udp\_mem: 188085 250783 376170 -> 188034 250715 376068
* Changed: user.max\_cgroup\_namespaces: 31743 -> 31589
* Changed: user.max\_fanotify\_marks: 67544 -> 68412
* Changed: user.max\_inotify\_watches: 63425 -> 64189
* Changed: user.max\_ipc\_namespaces: 31743 -> 31589
* Changed: user.max\_mnt\_namespaces: 31743 -> 31589
* Changed: user.max\_net\_namespaces: 31743 -> 31589
* Changed: user.max\_pid\_namespaces: 31743 -> 31589
* Changed: user.max\_time\_namespaces: 31743 -> 31589
* Changed: user.max\_user\_namespaces: 31743 -> 31589
* Changed: user.max\_uts\_namespaces: 31743 -> 31589
* Changed: vm.lowmem\_reserve\_ratio: 256 256 32 0 0 -> 256 256 32 0
* Deleted: kernel.sched\_child\_runs\_first: 0

### Feature

Enabled the Btrfs kernel module.

### cos-dev-129-19246-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.41](https://cos.googlesource.com/third_party/kernel/+/ef55a40bd2b3af2acd1197d83f203f892d717819 ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19246.0.0/lakitu/gpu_driver_versions.textproto) |

### Feature

Backported support for AMD SEV-SNP SVSM vTPM driver and
configfs-tsm addition for extended attestation protocol.

### Feature

Enabled the google-guest-agent's network management functionality.

### Feature

Added ConnectX-8 RDMA support.

### Fixed

Upgraded app-admin/google-guest-configs to v20250807.00.

### Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r668.

### Fixed

Upgraded dev-lang/go to v1.23.12.

### Fixed

Upgraded dev-db/sqlite to v3.50.4.

### Fixed

Upgraded net-nds/rpcbind to v1.2.8.

### Fixed

Upgraded sys-apps/gentoo-functions to v1.7.4.

### Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

### Security

Fixed KCTF-01d3c84 in the Linux kernel.

### cos-113-18244-448-29

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.144](https://cos.googlesource.com/third_party/kernel/+/4a14d0356f04e4dc9ad84328ced11962da997611 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.29/lakitu/gpu_driver_versions.textproto) |

### Feature

Added NVIDIA GPU driver's R580 branch. Updated the LATEST GPU driver label to version 580.65.06.

### Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

### Security

Fixed KCTF-01d3c84 in the Linux kernel.

### Security

Fixed CVE-2025-38499 in the linux kernel.

### Feature

Added NVIDIA GPU driver's R580 branch. Updated the LATEST GPU driver label to version 580.65.06.

### Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

### Security

Fixed KCTF-01d3c84 in the Linux kernel.

### Security

Fixed CVE-2025-38499 in the linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812031 -> 812040

### cos-109-17800-570-33

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/32eebab8d4fc97eb69fe095c4737e578f395ea56 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.33/lakitu/gpu_driver_versions.textproto) |

### Feature

Added NVIDIA GPU driver's R580 branch. Updated the LATEST GPU driver label to version 580.65.06.

### Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

### Security

Fixed KCTF-01d3c84 in the Linux kernel.

### Security

Fixed CVE-2025-38499 in the Linux kernel.

### Feature

Added NVIDIA GPU driver's R580 branch. Updated the LATEST GPU driver label to version 580.65.06.

### Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

### Security

Fixed KCTF-01d3c84 in the Linux kernel.

### Security

Fixed CVE-2025-38499 in the linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812266 -> 812258

### cos-121-18867-199-38

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/503b48dcd05d72cc3993836ba04c998694445289 ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.38/lakitu/gpu_driver_versions.textproto) |

### Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

### Security

Fixed KCTF-01d3c84 in the Linux kernel.

### Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

### Security

Fixed KCTF-01d3c84 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811774 -> 811736

### cos-117-18613-339-39

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/4388aee252f712d6c58566a5e41a11c7e938827e ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.39/lakitu/gpu_driver_versions.textproto) |

### Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

### Security

Fixed KCTF-01d3c84 in the Linux kernel.

### Security

Upgraded sys-libs/binutils-libs to version 2.45. This fixes CVE-2025-8224,CVE-2025-8225 and CVE-2025-1153.

### Security

Fixed KCTF-01d3c84 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811830 -> 811771

---
## 2025-08-14

### cos-121-18867-199-34

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/bfd3481379d56d24f2ab0fa617f940470828d303 ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.34/lakitu/gpu_driver_versions.textproto) |

### Security

Fixed CVE-2025-38499 in the linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811817 -> 811774

### cos-117-18613-339-36

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/466a913740c9a1e7249f9f8efda9f3c9b32367b2 ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.36/lakitu/gpu_driver_versions.textproto) |

### Security

Fixed CVE-2025-38499 in the linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811765 -> 811830

---
## 2025-08-12

### cos-121-18867-199-28

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/0eae577cf6b3f6844e1328ed3d4643f7f44dfc19 ) | v27.5.1 | v2.0.6 | [See List](https://storage.googleapis.com/cos-tools/18867.199.28/lakitu/gpu_driver_versions.textproto) |

### Feature

Added NVIDIA GPU driver's R580 branch. Updated the LATEST GPU driver label to version 580.65.06.

### Feature

Removed the cloud-final.service dependency on multi-user.target which could delay cloud-init user-data scripts indefinitely when long-running startup scripts are used.

### Fixed

Updated app-admin/node-problem-detector to 0.8.21.

### Fixed

Updated app-containers/cni-plugins to 1.7.1.

### Fixed

Updated containerd to v2.0.6.

### Fixed

Removed an artifact registry ping that would delay multi-user.target indefinitely for machines with no external IP address.

### Fixed

Reverted a containerd change which reduced the default soft file descriptor limit for processes in containers to 1024.

### Fixed

LTS Refresh from main-R121 to release-R121

### Fixed

kubernetes 1.32.4-gke.200

### Fixed

Upgraded app-admin/google-guest-configs to v20250516.00.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.3.

### Fixed

LTS Refresh from main-R121 to release-R121

### Fixed

Upgraded dev-lang/go to v1.23.9.

### Fixed

Upgraded sys-apps/pv to v1.9.34.

### Fixed

Updated dev-python/requests to v2.32.4.

### Fixed

Upgraded virtual/logger to v0-r2.

### Fixed

LTS Refresh from main-R121 to release-R121

### Fixed

Upgraded sys-libs/libcap to v2.76.

### Fixed

Upgraded sys-process/procps to v4.0.5-r2.

### Fixed

Upgraded dev-db/sqlite to v3.50.1.

### Fixed

Upgraded sys-libs/libseccomp to v2.6.0-r2.

### Fixed

Upgraded app-arch/unzip to v6.0\_p29.

### Fixed

Upgraded dev-libs/expat to v2.7.1.

### Fixed

Upgraded net-nds/rpcbind to v1.2.7.

### Fixed

Upgraded app-arch/gzip to v1.14.

### Fixed

Fixed an issue where the cpuidle driver selected for some
machine types would cause inflated reports of high CPU usage.

### Fixed

LTS Refresh from main-R121-cos-6.6 to release-R121-cos-6.6

### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Security

Upgraded net-misc/netplan to 1.1.2. This fixes
CVE-2022-4968.

### Security

Fixed CVE-2025-8058 in glibc.

### Security

Upgraded dev-libs/glib to 2.82.5. This resolves
CVE-2024-52533.

### Security

Upgraded urllib3 to version 1.26.18. This fixes CVE-2021-33503, CVE-2023-43804, and CVE-2023-45803.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Security

Upgraded sqlite to v3.50.2. This resolves CVE-2025-6965.

### Security

Fixed KCTF-bfebdb8 in the kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811826 -> 811817

### cos-dev-129-19226-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.41](https://cos.googlesource.com/third_party/kernel/+/0c333f6a7b49b4a001ab23fca27c39d4f694ebcd ) | v27.5.1 | v2.1.3 | [See List](https://storage.googleapis.com/cos-tools/19226.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated containerd to v2.1.3.

### Feature

Added NVIDIA GPU driver's R580 branch. Updated the LATEST GPU driver label to version 580.65.06.

### Feature

Removed the cloud-final.service dependency on multi-user.target which could delay cloud-init user-data scripts indefinitely when long-running startup scripts are used.

### Feature

Enabled hardware optimized SHA256 algorithms for x86 machines with SSSE3 and AVX/AVX2 instructions and ARM64 machines with SHA-NI and ARMv8 Crypto Extensions.

### Fixed

Updated app-admin/node-problem-detector to 0.8.21.

### Fixed

Updated app-containers/cni-plugins to 1.7.1.

### Fixed

Removed an artifact registry ping that would delay multi-user.target indefinitely for machines with no external IP address.

### Fixed

Reverted a containerd change which reduced the default soft file descriptor limit for processes in containers to 1024.

### Fixed

Upgraded app-admin/google-guest-configs to v20250718.00.

### Fixed

Upgraded chromeos-base/google-breakpad to v2025.07.23.214511-r244.

### Fixed

Upgraded chromeos-base/minijail to v18-r168.

### Fixed

Upgraded dev-libs/openssl to 3.5.1.

### Fixed

Upgraded dev-lang/go to v1.23.11.

### Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4879.

### Fixed

Updated dev-python/requests to v2.32.4.

### Fixed

Upgraded net-misc/openssh to 10.0\_p1.

### Fixed

Upgraded dev-db/sqlite to v3.50.3.

### Fixed

Upgraded virtual/logger to v0-r2.

### Fixed

Upgraded sys-apps/pv to v1.9.34.

### Fixed

Upgraded app-admin/sudo to v1.9.17\_p2.

### Fixed

Upgraded sys-process/lsof to v4.99.5.

### Fixed

Reverted a containerd change which reduced the default soft file descriptor limit for processes in containers to 1024.

### Fixed

Fixed an issue where the cpuidle driver selected for some
machine types would cause inflated reports of high CPU usage.

### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Security

Upgraded net-misc/netplan to 1.1.2. This fixes
CVE-2022-4968.

### Security

Fixed CVE-2025-8058 in glibc.

### Security

Upgraded dev-libs/glib to 2.82.5. This resolves
CVE-2024-52533.

### Security

Upgraded urllib3 to version 1.26.18. This fixes CVE-2021-33503, CVE-2023-43804, and CVE-2023-45803.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811510 -> 811531

### Feature

Enabled the Btrfs kernel module.

### cos-117-18613-339-32

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/e7e2af87d8c4a74a002a0fe2313d4ce03aab53a2 ) | v24.0.9 | v1.7.28 | [See List](https://storage.googleapis.com/cos-tools/18613.339.32/lakitu/gpu_driver_versions.textproto) |

### Feature

Added NVIDIA GPU driver's R580 branch. Updated the LATEST GPU driver label to version 580.65.06.

### Fixed

Updated app-admin/node-problem-detector to 0.8.21.

### Fixed

Updated containerd to v1.7.28.

### Fixed

Updated dev-python/requests to v2.32.4.

### Fixed

Upgraded virtual/logger to v0-r2.

### Fixed

Fixed an issue where the cpuidle driver selected for some
machine types would cause inflated reports of high CPU usage.

### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Security

Upgraded net-misc/netplan to 1.1.2. This fixes
CVE-2022-4968.

### Security

Fixed CVE-2024-11584 in cloud-init.

### Security

Fixed CVE-2024-6174 in cloud-init.

### Security

Fixed CVE-2025-8058 in glibc.

### Security

Patched openssl to fix CVE-2023-50782 affecting
dev-python/crytography.

### Security

Upgraded dev-libs/glib to 2.82.5. This resolves
CVE-2024-52533.

### Security

Upgraded urllib3 to version 1.26.18. This fixes CVE-2021-33503, CVE-2023-43804, and CVE-2023-45803.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Security

Fixed KCTF-bfebdb8 in the kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811775 -> 811765

### cos-109-17800-570-26

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/81651b50f5aebbcc9a6cd461d69c2acaf246cbdc ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.26/lakitu/gpu_driver_versions.textproto) |

### Fixed

Upgraded virtual/logger to v0-r2.

### Fixed

Updated dev-python/requests to v2.32.4.

### Fixed

Upgraded sys-process/lsof to v4.99.5.

### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Security

Upgraded net-misc/netplan to 1.1.2. This fixes
CVE-2022-4968.

### Security

Fixed CVE-2024-11584 in cloud-init.

### Security

Fixed CVE-2024-6174 in cloud-init.

### Security

Fixed CVE-2024-52533 in dev-libs/glib.

### Security

Patched openssl to fix CVE-2023-50782 affecting
dev-python/crytography.

### Security

Fixed CVE-2025-8058 in glibc.

### Security

Upgraded urllib3 to version 1.26.18. This fixes CVE-2021-33503, CVE-2023-43804, and CVE-2023-45803.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Security

Fixed KCTF-bfebdb8 in the kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812262 -> 812266

### cos-113-18244-448-22

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.144](https://cos.googlesource.com/third_party/kernel/+/e127a59f9a0efe8569de3ebdd6f9149a89b5a076 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.22/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated dev-python/requests to v2.32.4.

### Fixed

Upgraded virtual/logger to v0-r2.

### Fixed

Upgraded sys-process/lsof to v4.99.5.

### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Security

Upgraded net-misc/netplan to 1.1.2. This fixes
CVE-2022-4968.

### Security

Fixed CVE-2024-11584 in cloud-init.

### Security

Fixed CVE-2024-6174 in cloud-init.

### Security

Fixed CVE-2024-52533 in dev-libs/glib.

### Security

Fixed CVE-2025-8058 in glibc.

### Security

Upgraded urllib3 to version 1.26.18. This fixes CVE-2021-33503, CVE-2023-43804, and CVE-2023-45803.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Security

Fixed KCTF-bfebdb8 in the kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812027 -> 812031

---
## 2025-08-06

### cos-121-18867-199-19

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/18df8a39e6aba5e6b90c546050f17ccbe17296ef ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.199.19/lakitu/gpu_driver_versions.textproto) |

### Announcement

This is an LTS Refresh release.

### Fixed

Removed an artifact registry ping that would delay multi-user.target indefinitely for machines with no external IP address.

### Fixed

Reverted a containerd change which reduced the default soft file descriptor limit for processes in containers to 1024.

### Fixed

Upgraded kubernetes to v1.32.4-gke.200.

### Fixed

Upgraded app-admin/google-guest-configs to v20250516.00.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.3.

### Fixed

Upgraded dev-lang/go to v1.23.9.

### Fixed

Updated dev-python/requests to v2.32.4.

### Fixed

Upgraded virtual/logger to v0-r2.

### Fixed

Upgraded sys-libs/libcap to v2.76.

### Fixed

Upgraded sys-process/procps to v4.0.5-r2.

### Fixed

Upgraded dev-db/sqlite to v3.50.1.

### Fixed

Upgraded sys-libs/libseccomp to v2.6.0-r2.

### Fixed

Upgraded app-arch/unzip to v6.0\_p29.

### Fixed

Upgraded dev-libs/expat to v2.7.1.

### Fixed

Upgraded net-nds/rpcbind to v1.2.7.

### Fixed

Upgraded app-arch/gzip to v1.14.

### Fixed

Fixed an issue where the cpuidle driver selected for some
machine types would cause inflated reports of high CPU usage.

### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Security

Upgraded net-misc/netplan to 1.1.2. This fixes
CVE-2022-4968.

### Security

Upgraded dev-libs/glib to 2.82.5. This resolves
CVE-2024-52533.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Security

Upgraded sqlite to v3.50.2. This resolves CVE-2025-6965.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811826 -> 811817

### cos-117-18613-339-26

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/63cd753c2414d04f689ed02a0630d569b6acf634 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.339.26/lakitu/gpu_driver_versions.textproto) |

### Fixed

Fixed an issue where the cpuidle driver selected for some
machine types would cause inflated reports of high CPU usage.

### Fixed

Updated dev-python/requests to v2.32.4.

### Fixed

Upgraded virtual/logger to v0-r2.

### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Security

Upgraded net-misc/netplan to 1.1.2. This fixes
CVE-2022-4968.

### Security

Fixed CVE-2024-11584 in cloud-init.

### Security

Fixed CVE-2024-6174 in cloud-init.

### Security

Patched openssl to fix CVE-2023-50782 affecting
dev-python/cryptography.

### Security

Upgraded dev-libs/glib to 2.82.5. This resolves
CVE-2024-52533.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811775 -> 811788

### cos-113-18244-448-20

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.144](https://cos.googlesource.com/third_party/kernel/+/b1a3d1b003be6fec7ba7dea5a6b70bf397c567aa ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.20/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated dev-python/requests to v2.32.4.

### Fixed

Upgraded virtual/logger to v0-r2.

### Fixed

Upgraded sys-process/lsof to v4.99.5.

### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Security

Upgraded net-misc/netplan to 1.1.2. This fixes
CVE-2022-4968.

### Security

Fixed CVE-2024-11584 in cloud-init.

### Security

Fixed CVE-2024-6174 in cloud-init.

### Security

Fixed CVE-2024-52533 in dev-libs/glib.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812027 -> 812046

### cos-109-17800-570-23

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/66208798dd21d4ee2d28f8ea8b9b3a2df63e3f42 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.23/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated dev-python/requests to v2.32.4.

### Fixed

Upgraded sys-process/lsof to v4.99.5.

### Security

Added support for Nvidia driver version 535.261.03. This fixes CVE-2025-23286 and CVE-2025-23279.

### Security

Added support for Nvidia driver version 570.172.08. This fixes CVE-2025-23279.

### Security

Upgraded net-misc/netplan to 1.1.2. This fixes
CVE-2022-4968.

### Security

Fixed CVE-2024-11584 in cloud-init.

### Security

Fixed CVE-2024-6174 in cloud-init.

### Security

Patched openssl to fix CVE-2023-50782 affecting
dev-python/cryptography.

### Security

Upgraded dev-vcs/git to version 2.49.1. This fixes CVE-2025-48385, CVE-2025-27613, CVE-2025-27614, CVE-2025-48384, CVE-2025-46835.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812262 -> 812283

---
## 2025-07-30

### cos-dev-125-19175-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.37](https://cos.googlesource.com/third_party/kernel/+/dfb6569157e957816a33d329705284d2ef5a390e ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19175.0.0/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated app-misc/jq to v1.8.1.

### Fixed

The NFS access cache is no longer cleared on login by default. To use the old behavior, load the NFS module with the `nfs_fasc=1` module parameter.

### Security

Patched openssl to fix CVE-2023-50782 affecting
dev-python/crytography.

### Security

Upgraded sqlite to v3.50.2. This resolves CVE-2025-6965.

### Security

Fixed CVE-2024-26130 in dev-python/cryptography.

### Security

Fixed KCTF-5e28d5a in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811539 -> 811510

---
## 2025-07-28

### cos-117-18613-339-11

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.97](https://cos.googlesource.com/third_party/kernel/+/28b7c5a22b76c6b3f6ee318b28af04c6270cdd0c ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.339.11/lakitu/gpu_driver_versions.textproto) |

### Announcement

This is an [LTS Refresh release](https://cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases).

### Fixed

Upgraded app-admin/google-guest-configs to v20250516.00.

### Fixed

Upgraded app-containers/cni-plugins to v1.7.1.

### Fixed

Upgraded dev-lang/go to v1.23.9.

### Fixed

Upgraded sys-process/lsof to v4.99.5.

### Fixed

Updated app-misc/jq to v1.8.1.

### Fixed

Upgraded dev-db/sqlite to v3.50.1.

### Fixed

Upgraded sys-libs/libcap to v2.76.

### Fixed

Upgraded net-fs/cifs-utils to v7.4.

### Fixed

Upgraded sys-process/procps to v4.0.5-r2.

### Fixed

Upgraded app-arch/gzip to v1.14.

### Fixed

Fixed a kernel bug which caused some NVME disk IO errors to be ignored, potentially resulting in dropped writes.

### Fixed

The NFS access cache is no longer cleared on login by default. To use the old behavior, load the NFS module with the `nfs_fasc=1` module parameter.

### Security

Fixed CVE-2024-26130 in dev-python/cryptography.

### Security

Upgraded sqlite to v3.50.2. This resolves CVE-2025-6965.

### Fixed

Upgraded sys-libs/talloc to v2.4.3.

### Security

Fixed KCTF-5e28d5a in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811820 -> 811775

### cos-113-18244-448-6

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.144](https://cos.googlesource.com/third_party/kernel/+/b1a3d1b003be6fec7ba7dea5a6b70bf397c567aa ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.448.6/lakitu/gpu_driver_versions.textproto) |

### Announcement

This is an [LTS Refresh release](https://cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases).

### Fixed

Upgraded app-admin/google-guest-configs to v20250501.00.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.3.

### Fixed

Updated app-misc/jq to v1.8.1.

### Fixed

Upgraded sys-libs/libcap to v2.76.

### Fixed

Upgraded net-fs/cifs-utils to v7.4.

### Fixed

Upgraded sys-process/procps to v4.0.5-r2.

### Fixed

Upgraded dev-db/sqlite to v3.50.1.

### Fixed

Upgraded app-arch/gzip to v1.14.

### Security

Fixed KCTF-5e28d5a in the Linux kernel.

### Security

Patched openssl to fix CVE-2023-50782 affecting
dev-python/crytography.

### Security

Upgraded sqlite to v3.50.2. This resolves CVE-2025-6965.

### Security

Fixed CVE-2024-26130 in dev-python/cryptography.

### Fixed

Upgraded sys-libs/talloc to v2.4.3.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811983 -> 812027

### cos-121-18867-90-106

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/386b92953069741a6a583dd4abce71d299fafa55 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.90.106/lakitu/gpu_driver_versions.textproto) |

### Fixed

Upgraded sys-process/lsof to v4.99.5.

### Fixed

Updated app-misc/jq to v1.8.1.

### Fixed

Fixed a kernel bug which caused some NVME disk IO errors to be ignored, potentially resulting in dropped writes.

### Fixed

The NFS access cache is no longer cleared on login by default. To use the old behavior, load the NFS module with the `nfs_fasc=1` module parameter.

### Security

Patched openssl to fix CVE-2023-50782 affecting
dev-python/crytography.

### Security

Fixed CVE-2024-26130 in dev-python/cryptography.

### Security

Fixed KCTF-5e28d5a in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811784 -> 811826

### cos-109-17800-570-8

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/66208798dd21d4ee2d28f8ea8b9b3a2df63e3f42 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.8/lakitu/gpu_driver_versions.textproto) |

### Security

Fixed KCTF-5e28d5a in the Linux kernel.

### Security

Upgraded sqlite to v3.50.2. This resolves CVE-2025-6965.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812234 -> 812262

---
## 2025-07-24

### cos-dev-125-19165-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.12.37](https://cos.googlesource.com/third_party/kernel/+/0ce36d1d9a8a3cab6816b03d67f80f64e582deb7 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19165.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated the NVIDIA GPU driver policy for New Feature Branch (NFB) drivers. The LATEST tag has been updated to point to the stable 570.133.20 Production Branch. The 575.57.08 NFB driver remains available for development and testing but must now be selected by its specific version number.Removed 575.57.08 NFB driver support for NVIDIA\_GB200 machine.

### Changed

Upgraded nvidia-container-toolkit to v1.17.8. This fixes CVE-2025-23266.

### Changed

Updated cos-gpu-installer to v2.5.5.

### Changed

Updated the Linux kernel to v6.12.37.

### Feature

Added ARM support for the Lustre 2.14.0 drivers.

### Feature

Remove support for the v2.14.0\_p184 and v2.14.0\_p198 Lustre client drivers.

### Fixed

Upgraded app-admin/google-guest-configs to v20250627.00.

### Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4875.

### Fixed

Upgraded chromeos-base/google-breakpad to v2025.07.01.161305-r243.

### Fixed

Upgraded uhaul to version 6.12-0.

### Fixed

Upgraded sysram to version 6.12-0.

### Fixed

Fixed an issue where some workloads could cause a full
system hang when running close to their memory limit.

### Security

Fixed CVE-2024-6174 and CVE-2024-11584 in cloud-init.

### Security

Updated app-editors/nano to v8.5. This resolves
CVE-2024-5742.

### Security

Upgraded vim, vim-core to
version 9.1.1500. This fixes CVE-2025-26603, CVE-2025-27423,
CVE-2025-29768, CVE-2025-1215, CVE-2025-24014, CVE-2025-22134.

### Security

Upgraded app-admin/sudo to v1.9.17\_p1. This resolves
CVE-2025-32462 and CVE-2025-32463.

### Changed

Runtime sysctl changes:

* Added: kernel.apparmor\_restrict\_unprivileged\_unconfined: 0
* Added: kernel.core\_file\_note\_size\_limit: 4194304
* Added: kernel.core\_sort\_vma: 0
* Added: net.ipv4.fib\_multipath\_hash\_seed: 0
* Added: net.ipv4.tcp\_pingpong\_thresh: 1
* Added: net.ipv6.conf.all.ra\_honor\_pio\_life: 0
* Added: net.ipv6.conf.all.ra\_honor\_pio\_pflag: 0
* Added: net.ipv6.conf.all.regen\_min\_advance: 2
* Added: net.ipv6.conf.default.ra\_honor\_pio\_life: 0
* Added: net.ipv6.conf.default.ra\_honor\_pio\_pflag: 0
* Added: net.ipv6.conf.default.regen\_min\_advance: 2
* Added: net.ipv6.conf.docker0.ra\_honor\_pio\_life: 0
* Added: net.ipv6.conf.docker0.ra\_honor\_pio\_pflag: 0
* Added: net.ipv6.conf.docker0.regen\_min\_advance: 2
* Added: net.ipv6.conf.eth0.ra\_honor\_pio\_life: 0
* Added: net.ipv6.conf.eth0.ra\_honor\_pio\_pflag: 0
* Added: net.ipv6.conf.eth0.regen\_min\_advance: 2
* Added: net.ipv6.conf.lo.ra\_honor\_pio\_life: 0
* Added: net.ipv6.conf.lo.ra\_honor\_pio\_pflag: 0
* Added: net.ipv6.conf.lo.regen\_min\_advance: 2
* Added: vm.enable\_soft\_offline: 1
* Changed: fs.epoll.max\_user\_watches: 1809007 -> 1808517
* Changed: fs.fanotify.max\_user\_marks: 67544 -> 68412
* Changed: fs.file-max: 811755 -> 811539
* Changed: fs.inotify.max\_user\_watches: 63425 -> 64189
* Changed: kernel.threads-max: 63487 -> 63178
* Changed: net.ipv4.tcp\_mem: 94041 125391 188082 -> 94017 125357 188034
* Changed: net.ipv4.udp\_mem: 188085 250783 376170 -> 188034 250715 376068
* Changed: user.max\_cgroup\_namespaces: 31743 -> 31589
* Changed: user.max\_fanotify\_marks: 67544 -> 68412
* Changed: user.max\_inotify\_watches: 63425 -> 64189
* Changed: user.max\_ipc\_namespaces: 31743 -> 31589
* Changed: user.max\_mnt\_namespaces: 31743 -> 31589
* Changed: user.max\_net\_namespaces: 31743 -> 31589
* Changed: user.max\_pid\_namespaces: 31743 -> 31589
* Changed: user.max\_time\_namespaces: 31743 -> 31589
* Changed: user.max\_user\_namespaces: 31743 -> 31589
* Changed: user.max\_uts\_namespaces: 31743 -> 31589
* Changed: vm.lowmem\_reserve\_ratio: 256 256 32 0 0 -> 256 256 32 0
* Deleted: kernel.sched\_child\_runs\_first: 0

---
## 2025-07-21

### cos-109-17800-570-5

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.143](https://cos.googlesource.com/third_party/kernel/+/934359bdc0f1081eed66a6db8dba3ea7c2948d3c ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.570.5/lakitu/gpu_driver_versions.textproto) |

### Announcement

This is an [LTS Refresh release](https://cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_refresh_releases).

### Changed

Updated the NVIDIA GPU driver policy for New Feature Branch (NFB) drivers. The LATEST tag has been updated to point to the stable 570.133.20 Production Branch. The 575.57.08 NFB driver remains available for development and testing but must now be selected by its specific version number.

### Fixed

Upgraded app-admin/google-guest-configs to v20250516.00.

### Fixed

Upgraded app-containers/docker-credential-helpers to v0.9.3.

### Fixed

Updated app-misc/jq to v1.8.1.

### Fixed

Upgraded net-fs/cifs-utils to v7.4.

### Fixed

Upgraded sys-libs/libcap to v2.76.

### Fixed

Upgraded dev-db/sqlite to v3.50.1.

### Fixed

Upgraded app-arch/unzip to v6.0\_p29.

### Fixed

Upgraded app-arch/gzip to v1.14.

### Fixed

Fixed an issue where some workloads could cause a full
system hang when running close to their memory limit.

### Fixed

Upgraded sys-libs/talloc to v2.4.3.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812258 -> 812234

### Security

Fixed KCTF-103406b in the Linux kernel

### cos-121-18867-90-97

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/24fc21afff6a88ece2f6e5e3163e54e15fb554b5 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.90.97/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated the NVIDIA GPU driver policy for New Feature Branch (NFB) drivers. The LATEST tag has been updated to point to the stable 570.133.20 Production Branch. The 575.57.08 NFB driver remains available for development and testing but must now be selected by its specific version number. Removed 575.57.08 NFB driver support for NVIDIA\_GB200 machine.

### Feature

Added ARM support for the Lustre 2.14.0 drivers.

### Fixed

Fixed an issue where some workloads could cause a full
system hang when running close to their memory limit.

### Security

Fixed CVE-2024-6174 and CVE-2024-11584 in cloud-init.

### Security

Fixed KCTF-103406b in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811807 -> 811784

### cos-117-18613-263-75

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/00c059b5e633ba65a380fed13ae9d1d3503be953 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.263.75/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated the NVIDIA GPU driver policy for New Feature Branch (NFB) drivers. The LATEST tag has been updated to point to the stable 570.133.20 Production Branch. The 575.57.08 NFB driver remains available for development and testing but must now be selected by its specific version number. Removed 575.57.08 NFB driver support for NVIDIA\_GB200 machine.

### Feature

Added ARM support for the Lustre 2.14.0 drivers.

### Fixed

Fixed an issue where some workloads could cause a full
system hang when running close to their memory limit.

### Security

Fixed KCTF-103406b in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811784 -> 811820

### cos-113-18244-382-65

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/9fee4f41d85c4575865445d7411310b7f9959ab4 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.382.65/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated the NVIDIA GPU driver policy for New Feature Branch (NFB) drivers. The LATEST tag has been updated to point to the stable 570.133.20 Production Branch. The 575.57.08 NFB driver remains available for development and testing but must now be selected by its specific version number.

### Fixed

Fixed an issue where some workloads could cause a full
system hang when running close to their memory limit.

### Security

Fixed KCTF-103406b in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812031 -> 811983

---
## 2025-07-14

### cos-117-18613-263-66

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/12c0014075ea8438afd8396c473a3895a9c9dc5a ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.263.66/lakitu/gpu_driver_versions.textproto) |

### Changed

Upgraded nvidia-container-toolkit to v1.17.8.

### Fixed

Updated google-guest-agent to v20250701.01.

### Security

Updated app-editors/nano to v8.5. This resolves
CVE-2024-5742.

### Security

Upgraded vim, vim-core to
version 9.1.1500. This fixes CVE-2025-26603, CVE-2025-27423,
CVE-2025-29768, CVE-2025-1215, CVE-2025-24014, CVE-2025-22134.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811799 -> 811784

### cos-109-17800-519-47

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/80aa802c8b1dacdfd244bb9931499a2fa4fcd118 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.47/lakitu/gpu_driver_versions.textproto) |

### Changed

Upgraded nvidia-container-toolkit to v1.17.8.

### Fixed

Upgraded sys-apps/less to v679.

### Security

Updated app-editors/nano to v8.5. This resolves
CVE-2024-5742.

### Security

Upgraded vim, vim-core to
version 9.1.1500. This fixes CVE-2025-26603, CVE-2025-27423,
CVE-2025-29768, CVE-2025-1215, CVE-2025-24014, CVE-2025-22134.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812201 -> 812258

### cos-121-18867-90-85

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/25875e54e8fcc5831f6572e7bd367a70ef85b37c ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.90.85/lakitu/gpu_driver_versions.textproto) |

### Changed

Upgraded nvidia-container-toolkit to v1.17.8.

### Fixed

Updated google-guest-agent to v20250701.01.

### Security

Updated app-editors/nano to v8.5. This resolves
CVE-2024-5742.

### Security

Upgraded vim, vim-core to
version 9.1.1500. This fixes CVE-2025-26603, CVE-2025-27423,
CVE-2025-29768, CVE-2025-1215, CVE-2025-24014, CVE-2025-22134.

### cos-113-18244-382-60

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/436274a3803b4d919d23b19b266c7e95ccdb4e09 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.382.60/lakitu/gpu_driver_versions.textproto) |

### Changed

Upgraded nvidia-container-toolkit to v1.17.8.

### Fixed

Upgraded sys-apps/less to v679.

### Security

Updated app-editors/nano to v8.5. This resolves
CVE-2024-5742.

### Security

Upgraded vim, vim-core to
version 9.1.1500. This fixes CVE-2025-26603, CVE-2025-27423,
CVE-2025-29768, CVE-2025-1215, CVE-2025-24014, CVE-2025-22134.

---
## 2025-07-07

### cos-121-18867-90-77

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/25875e54e8fcc5831f6572e7bd367a70ef85b37c ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.90.77/lakitu/gpu_driver_versions.textproto) |

### Security

Upgraded app-admin/sudo to v1.9.17\_p1. This resolves
CVE-2025-32462 and CVE-2025-32463.

### cos-117-18613-263-58

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/12c0014075ea8438afd8396c473a3895a9c9dc5a ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.263.58/lakitu/gpu_driver_versions.textproto) |

### Security

Upgraded app-admin/sudo to v1.9.17\_p1. This resolves
CVE-2025-32462 and CVE-2025-32463.

### cos-113-18244-382-54

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/436274a3803b4d919d23b19b266c7e95ccdb4e09 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.382.54/lakitu/gpu_driver_versions.textproto) |

### Security

Upgraded app-admin/sudo to v1.9.17\_p1. This resolves
CVE-2025-32462 and CVE-2025-32463.

### cos-109-17800-519-41

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/80aa802c8b1dacdfd244bb9931499a2fa4fcd118 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.41/lakitu/gpu_driver_versions.textproto) |

### Security

Upgraded app-admin/sudo to v1.9.17\_p1. This resolves
CVE-2025-32462 and CVE-2025-32463.

---
## 2025-06-30

### cos-dev-125-19126-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.94](https://cos.googlesource.com/third_party/kernel/+/ffa537805d6bb853cb6baacb2d70fb7fadba42e0 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19126.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated nvidia-container-toolkit to v1.17.7.

### Changed

Upgraded sys-apps/ethtool to version 6.11.

### Fixed

Upgraded app-admin/google-guest-configs to v20250605.00.

### Fixed

Added support for the Lustre 2.14.0\_p212 drivers.

### Fixed

drop marvell-pcie-ep-octeon driver

### Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4872.

### Fixed

Upgraded chromeos-base/google-breakpad to v2025.06.12.121629-r242.

### Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4871.

### Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r667.

### Fixed

Upgraded dev-lang/go to v1.23.10.

### Fixed

Upgraded app-admin/sudo to v1.9.17.

### Fixed

Upgraded sys-apps/less to v679.

### Fixed

Upgraded dev-db/sqlite to v3.50.1.

### Fixed

Upgraded sys-process/procps to v4.0.5-r2.

### Fixed

Upgraded sys-libs/libcap to v2.76.

### Security

Upgrade libarchive to version 3.8.1. This fixes CVE-2025-5914.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811773 -> 811755

### cos-117-18613-263-56

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/12c0014075ea8438afd8396c473a3895a9c9dc5a ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.263.56/lakitu/gpu_driver_versions.textproto) |

### Fixed

Added support for the Lustre 2.14.0\_p212 drivers.

### Fixed

Upgraded sys-apps/less to v679.

### Fixed

Upgraded dev-libs/libusb to v1.0.29.

### Security

Upgrade libarchive to version 3.8.1. This fixes CVE-2025-5914.

### Security

Upgraded elfutils to version 0.193. This fixes CVE-2025-1365, CVE-2025-1371, CVE-2025-1372, and CVE-2025-1377.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811785 -> 811719

### cos-121-18867-90-75

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/25875e54e8fcc5831f6572e7bd367a70ef85b37c ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.90.75/lakitu/gpu_driver_versions.textproto) |

### Fixed

Added support for the Lustre 2.14.0\_p212 drivers.

### Fixed

Upgraded sys-apps/less to v679.

### Security

Upgrade libarchive to version 3.8.1. This fixes CVE-2025-5914.

### Security

Upgraded elfutils to version 0.193. This fixes CVE-2025-1365, CVE-2025-1371, CVE-2025-1372, and CVE-2025-1377.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811798 -> 811807

### cos-113-18244-382-53

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/436274a3803b4d919d23b19b266c7e95ccdb4e09 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.382.53/lakitu/gpu_driver_versions.textproto) |

### Fixed

Upgraded dev-libs/libusb to v1.0.29.

### Security

Upgrade libarchive to version 3.8.1. This fixes CVE-2025-5914.

### Security

Upgraded elfutils to version 0.193. This fixes CVE-2025-1365, CVE-2025-1371, CVE-2025-1372, and CVE-2025-1377.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812041 -> 812035

### cos-109-17800-519-40

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/80aa802c8b1dacdfd244bb9931499a2fa4fcd118 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.40/lakitu/gpu_driver_versions.textproto) |

### Fixed

Upgraded dev-libs/libusb to v1.0.29.

### Security

Upgrade libarchive to version 3.8.1. This fixes CVE-2025-5914.

### Security

Upgraded elfutils to version 0.193. This fixes CVE-2025-1365, CVE-2025-1371, CVE-2025-1372, and CVE-2025-1377.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812288 -> 812258

---
## 2025-06-23

### Changed



### cos-125-19115-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.94](https://cos.googlesource.com/third_party/kernel/+/ffa537805d6bb853cb6baacb2d70fb7fadba42e0 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19115.0.0/csql-arm64-gcp/gpu_driver_versions.textproto) |

### Changed

Updated the Linux kernel to v6.6.94.

### Feature

Added NVIDIA 570.133.20 vGPU driver.

### Feature

Added a kernel patch to address bcache latency.

### Security

Upgraded elfutils to version 0.193. This fixes CVE-2025-1365, CVE-2025-1371, CVE-2025-1372, and CVE-2025-1377.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811736 -> 811773

### Changed



### cos-121-18867-90-67

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/25875e54e8fcc5831f6572e7bd367a70ef85b37c ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.90.67/lakitu/gpu_driver_versions.textproto) |

### Security

Updated the Linux kernel to v6.6.93. This includes
mitigations for CVE-2024-28956, which may negatively impact the
performance of Intel machine types.

### Security

Fixed KCTF-d35acc1 in the Linux kernel.

### Feature

Added a kernel patch to address bcache latency.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811824 -> 811798

### Changed



### cos-117-18613-263-49

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/12c0014075ea8438afd8396c473a3895a9c9dc5a ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.263.49/lakitu/gpu_driver_versions.textproto) |

### Security

Updated the Linux kernel to v6.6.93. This includes
mitigations for CVE-2024-28956, which may negatively impact the
performance of Intel machine types.

### Security

Fixed KCTF-d35acc1 in the Linux kernel.

### Feature

Added a kernel patch to address bcache latency.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811766 -> 811785

### Changed



### cos-113-18244-382-49

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/436274a3803b4d919d23b19b266c7e95ccdb4e09 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.382.49/lakitu/gpu_driver_versions.textproto) |

### Security

Updated the Linux kernel to v6.1.141. This includes
mitigations for CVE-2024-28956, which may negatively impact the
performance of Intel machine types.

### Security

Fixed KCTF-d35acc1 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812035 -> 812041

### Changed



### cos-109-17800-519-36

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.141](https://cos.googlesource.com/third_party/kernel/+/80aa802c8b1dacdfd244bb9931499a2fa4fcd118 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.36/lakitu/gpu_driver_versions.textproto) |

### Security

Updated the Linux kernel to v6.1.141. This includes
mitigations for CVE-2024-28956, which may negatively impact the
performance of Intel machine types.

### Security

Fixed KCTF-d35acc1 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812276 -> 812288

---
## 2025-06-18

### Changed



### cos-dev-125-19104-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.93](https://cos.googlesource.com/third_party/kernel/+/8f1ed7554eff45bf08c26fd7f15bc57a7ffac0b0 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19104.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Upgraded dpdk-kmods to 9b182be2ee4b

### Changed

Updated the Linux kernel to v6.6.93.

### Security

Upgraded app-misc/jq to v1.8.0. This fixes CVE-2025-48060.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811779 -> 811736

### Changed



### cos-121-18867-90-62

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/2b6148ec22df8bd88c829407078577aecc9c764a ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.90.62/lakitu/gpu_driver_versions.textproto) |

### Security

Upgraded app-misc/jq to v1.8.0. This fixes CVE-2025-48060.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811798 -> 811824

### Changed



### cos-117-18613-263-45

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/90daf444819d8b8478e6285bdafc25f1fa953e04 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.263.45/lakitu/gpu_driver_versions.textproto) |

### Security

Upgraded app-misc/jq to v1.8.0. This fixes CVE-2025-48060.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811775 -> 811766

### Changed



### cos-113-18244-382-47

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.134](https://cos.googlesource.com/third_party/kernel/+/cbd62176e17d3c4d02a624ad951c16f9e6c8d5a4 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.382.47/lakitu/gpu_driver_versions.textproto) |

### Security

Upgraded app-misc/jq to v1.8.0. This fixes CVE-2025-48060.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812031 -> 812035

### Changed



### cos-109-17800-519-32

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.135](https://cos.googlesource.com/third_party/kernel/+/269aea26c0f2e9675236f141e0a182b8c58e8e52 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.32/lakitu/gpu_driver_versions.textproto) |

### Security

Upgraded app-misc/jq to v1.8.0. This fixes CVE-2025-48060.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812266 -> 812276

---
## 2025-06-17

### Changed



### cos-117-18613-263-42

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/90daf444819d8b8478e6285bdafc25f1fa953e04 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.263.42/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.3.

### Changed

Added support for the Lustre 2.14.0\_p198 drivers.

### Feature

Added support for Nvidia driver version 575.57.08.

### Feature

Fixed CVE-2024-41110 in Docker.

### Security

Fixed CVE-2025-47273 in dev-python/setuptools.

### Security

Updated systemd to v254.26. This resolves CVE-2025-4598.

### Security

Fixed CVE-2025-37800 in the Linux kernel.

### Security

Fixed CVE-2025-37800 in the Linux kernel.

### Security

Fixed CVE-2025-37803 in the Linux kernel.

### Security

Fixed KCTF-ac9fe7d in the kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811818 -> 811775

### Changed



### cos-121-18867-90-59

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/2b6148ec22df8bd88c829407078577aecc9c764a ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.90.59/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.3.

### Changed

Added support for the Lustre 2.14.0\_p198 drivers.

### Feature

Added support for Nvidia driver version 575.57.08.

### Security

Fixed CVE-2025-47273 in dev-python/setuptools.

### Security

Updated systemd to v254.26. This resolves CVE-2025-4598.

### Security

Fixed CVE-2025-37800 in the Linux kernel.

### Security

Fixed CVE-2025-37803 in the Linux kernel.

### Security

Fixed KCTF-ac9fe7d in the kernel.

### Security

Fixed CVE-2024-43840 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811741 -> 811798

### Changed



### cos-113-18244-382-43

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.134](https://cos.googlesource.com/third_party/kernel/+/cbd62176e17d3c4d02a624ad951c16f9e6c8d5a4 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.382.43/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.3.

### Feature

Added support for Nvidia driver version 575.57.08.

### Feature

Fixed CVE-2024-41110 in Docker.

### Security

Fixed CVE-2025-47273 in dev-python/setuptools.

### Security

Updated systemd to v254.26. This resolves CVE-2025-4598.

### Security

Fixed KCTF-ac9fe7d in the kernel.

### Security

Fixed CVE-2024-26783 in the Linux kernel.

### Security

Fixed CVE-2024-36903 in the Linux kernel.

### Security

Fixed CVE-2024-43840 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812017 -> 812031

### Changed



### cos-109-17800-519-30

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.135](https://cos.googlesource.com/third_party/kernel/+/269aea26c0f2e9675236f141e0a182b8c58e8e52 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.30/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.3.

### Feature

Added support for Nvidia driver version 575.57.08.

### Feature

Fixed CVE-2024-41110 in Docker.

### Security

Updated systemd to v253.33. This resolves CVE-2025-4598.

### Security

Fixed CVE-2025-47273 in dev-python/setuptools.

### Security

Fixed KCTF-ac9fe7d in the kernel.

### Security

Fixed CVE-2024-36927 in the Linux kernel.

### Security

Fixed CVE-2024-43840 in the Linux kernel.

### Security

Fixed CVE-2024-36903 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812283 -> 812266

### Changed



### cos-dev-125-19094-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.92](https://cos.googlesource.com/third_party/kernel/+/8ff56aa9d000fc42d1198f5e46504f60c75f29b2 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19094.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Updated cos-gpu-installer to v2.5.3.

### Changed

Added support for the Lustre 2.14.0\_p198 drivers.

### Feature

Added support for Nvidia driver version 575.57.08.

### Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4869.

### Fixed

Upgraded dev-db/sqlite to v3.50.0.

### Security

Fixed CVE-2025-47273 in dev-python/setuptools.

### Security

Updated systemd to v254.26. This resolves CVE-2025-4598.

### Security

Fixed KCTF-ac9fe7d in the kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811798 -> 811779

---
## 2025-06-02

### Changed



### cos-dev-125-19071-0-0

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.92](https://cos.googlesource.com/third_party/kernel/+/1c5a7e09f4791a79a02ae7d83967cd3e13b12755 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/19071.0.0/lakitu/gpu_driver_versions.textproto) |

### Changed

Upgraded google-guest-agent to 20250327.00. This included
new services like `google-guest-compat-manager.service` and
`google-guest-agent-manager.service` and new binaries like
`google_guest_compat_manager`, `gce_metadata_script_runner`,
`google_guest_agent_manager`, `ggactl_plugin_cleanup` and
`gce_compat_metadata_script_runner`.

### Changed

Updated the Linux kernel to v6.6.92.

### Feature

Supported NVIDIA MFT Tools.

### Feature

Injected IMEX channel char device for GB200 GPUs.

### Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO\_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA\_GB200 machine.

### Fixed

Upgraded app-admin/google-guest-configs to v20250516.00.

### Fixed

Fixed docker MTU mismatch.

### Fixed

Upgraded chromeos-base/chromeos-common-script to v0.0.1-r665.

### Fixed

Upgraded chromeos-base/google-breakpad to v2025.05.22.184901-r240.

### Fixed

Upgraded chromeos-base/session\_manager-client to v0.0.1-r2830.

### Fixed

Upgraded chromeos-base/power\_manager-client to v0.0.1-r2969.

### Fixed

Upgraded chromeos-base/shill-client to v0.0.1-r4866.

### Fixed

Upgraded chromeos-base/debugd-client to v0.0.1-r2734.

### Fixed

Upgraded sys-apps/rootdev to v0.0.1-r51.

### Fixed

Upgraded dev-lang/go to v1.23.9.

### Fixed

Upgraded sys-apps/dbus to v1.16.2-r197.

### Fixed

Upgraded sys-apps/less to v678.

### Fixed

Upgraded dev-db/sqlite to v3.49.2.

### Security

Fixed CVE-2024-23337 in app-misc/jq.

### Security

Upgraded net-misc/curl to version 8.12.1. This fixes CVE-2025-0167.

### Security

Fixed CVE-2025-46836 in sys-apps/net-tools

### Security

Fixed CVE-20250-3198 in sys-libs/bintuils-libs.

### Security

Fixed KCTF-3f98113 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811729 -> 811798
* Changed: net.ipv6.conf.docker0.mtu: 1500 -> 1460

### Changed



### cos-117-18613-263-24

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/d7d9a34e59a967bd31420a1a629853632fc7d3a0 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.263.24/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO\_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA\_GB200 machine.

### Fixed

Upgraded sys-apps/less to v678.

### Security

Fixed CVE-2024-23337 in app-misc/jq.

### Security

Fixed CVE-2024-43840 in the Linux kernel.

### Security

Fixed KCTF-3f98113 in the Linux kernel.

### Security

Fixed KCTF-8478a72 in the Linux kernel.

### Changed



### cos-113-18244-382-29

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.134](https://cos.googlesource.com/third_party/kernel/+/e99d24367a9c6985bc9c997c6f3a053c2a7e2eff ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.382.29/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO\_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA\_GB200 machine.

### Fixed

Upgraded sys-apps/less to v678.

### Security

Fixed CVE-2024-23337 in app-misc/jq.

### Security

Fixed CVE-2024-36927 in the Linux kernel.

### Security

Fixed KCTF-3f98113 in the Linux kernel.

### Security

Fixed KCTF-8478a72 in the Linux kernel.

### Changed



### cos-121-18867-90-38

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/7217e46094ce6bf030248161190afe8b3d8678e8 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.90.38/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO\_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA\_GB200 machine.

### Fixed

Upgraded sys-apps/less to v678.

### Security

Fixed CVE-2024-23337 in app-misc/jq.

### Security

Fixed KCTF-3f98113 in the Linux kernel.

### Security

Fixed KCTF-8478a72 in the Linux kernel.

### Changed



### cos-109-17800-519-18

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.135](https://cos.googlesource.com/third_party/kernel/+/2e89dc9fc1cfcb0184104491d7f412eee640086b ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.18/lakitu/gpu_driver_versions.textproto) |

### Fixed

Updated cos-gpu-installer to v2.5.2: Added support for OTHER/NO\_GPU cases to enable GPU driver preloading on the ARM64 architecture and added support for IMEX Driver configuration installation for NVIDIA\_GB200 machine.

### Fixed

Upgraded sys-apps/less to v678.

### Security

Fixed CVE-2024-26783 in the Linux kernel.

### Security

Fixed KCTF-3f98113 in the Linux kernel.

### Security

Fixed KCTF-8478a72 in the Linux kernel.

---
## 2025-05-27

### Changed



### cos-121-18867-90-32

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/b4264a6c074cc123d9f043b10a6e2653952fdae2 ) | v27.5.1 | v2.0.4 | [See List](https://storage.googleapis.com/cos-tools/18867.90.32/lakitu/gpu_driver_versions.textproto) |

### Feature

Support NVIDIA MFT Tools on COS.

### Feature

Inject IMEX channel char device for GB200 GPUs.

### Security

Fixed CVE-2025-46836 in sys-apps/net-tools.

### Security

Fixed CVE-20250-3198 in sys-libs/bintuils-libs.

### Security

Fixed KCTF-b3bf8f6 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811834 -> 811792

### Changed



### cos-117-18613-263-19

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.6.87](https://cos.googlesource.com/third_party/kernel/+/e736bf1d9149d0c78e366c270fb44502fca96e9f ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18613.263.19/lakitu/gpu_driver_versions.textproto) |

### Feature

Support NVIDIA MFT Tools on COS.

### Feature

Inject IMEX channel char device for GB200 GPUs.

### Security

Fixed CVE-2025-46836 in sys-apps/net-tools.

### Security

Fixed CVE-20250-3198 in sys-libs/bintuils-libs.

### Security

Fixed KCTF-b3bf8f6 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 811793 -> 811830

### Changed



### cos-113-18244-382-22

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.134](https://cos.googlesource.com/third_party/kernel/+/418e1a7f94faec8f2e29f8e2202b06212ad9910b ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/18244.382.22/lakitu/gpu_driver_versions.textproto) |

### Feature

Support NVIDIA MFT Tools on COS.

### Security

Fixed CVE-2025-46836 in sys-apps/net-tools.

### Security

Fixed CVE-20250-3198 in sys-libs/bintuils-libs.

### Security

Fixed KCTF-b3bf8f6 in the Linux kernel.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812054 -> 812045

### Changed



### cos-109-17800-519-12

|  |  |  |  |
| --- | --- | --- | --- |
| Kernel | Docker | Containerd | [GPU Drivers](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) |
| [COS-6.1.135](https://cos.googlesource.com/third_party/kernel/+/8f41e7ee6fe9b8eb00f95b8b56858a7594b466b7 ) | v24.0.9 | v1.7.27 | [See List](https://storage.googleapis.com/cos-tools/17800.519.12/lakitu/gpu_driver_versions.textproto) |

### Feature

Support NVIDIA MFT Tools on COS.

### Security

Fixed CVE-2025-46836 in sys-apps/net-tools.

### Security

Fixed CVE-20250-3198 in sys-libs/bintuils-libs.

### Changed

Runtime sysctl changes:

* Changed: fs.file-max: 812270 -> 812274

---
