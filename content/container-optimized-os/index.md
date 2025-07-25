# Container Optimized OS

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
