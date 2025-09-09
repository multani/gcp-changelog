# Container Optimized OS

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
