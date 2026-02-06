# Google Distributed Cloud connected

## 2026-02-03

### Libraries

The following Google Distributed Cloud connected components have been updated:

* **GDC software-only has been updated** to version v1.33.300-gke.60.
  (This component was formerly known as GKE on Bare Metal and as Anthos Clusters on Bare Metal.)
* **Kubernetes** has been updated to version 1.33.5-gke.900.
* **EdgeOS kernel** has been updated to version
  [6.12.31](https://cos.googlesource.com/third_party/kernel/+/b7edc92b0ebd3782fb928e8401f55c5a9155269f).
* **Symcloud Storage** has been updated to version 5.4.18-278.

### Deprecated

The following functionality has been deprecated in this release of Google Distributed Cloud connected:

* **GDC connected racks form factor.** The Google Distributed Cloud connected racks form factor, also known
  as Config 1 and Config 2, has been deprecated and all documentation for Google Distributed Cloud connected
  features related to this form factor has been removed from product documentation. The last minor release
  of Google Distributed Cloud connected that supports the racks form factor is
  [Google Distributed Cloud connected 1.11](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/overview).

### Announcement

This is a minor release of Google Distributed Cloud connected (version 1.12.0). Google Distributed Cloud software updates
roll out gradually across regions. The latest version might not be immediately available on your Google Distributed Cloud
connected deployment.

### Fixed

The following issues have been resolved in this release of Google Distributed Cloud connected:

* **Virtual machines no longer intermittently freeze.** Through a combination of updates to Symcloud Storage and
  [new firmware for the integrated Dell Remote Access Controller (iDRAC)](https://www.dell.com/support/home/en-in/drivers/driversdetails?driverid=kywdc&oscode=ws19l&productcode=oth-xr11),
  we have improved the resilience of virtual machine workloads against unstable mains power and resolved freezes
  caused by storage snapshotting. For more information, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).
* **Auto-renewal of TLS certificates for Symcloud Storage no longer fails.** Symcloud Storage host services no longer
  report a `Critical` state if a Google Distributed Cloud connected node was restarted after the Symcloud Storage TLS
  certificate has expired. These certificates now renew automatically when the Google Distributed Cloud connected software
  on the cluster is upgraded.
* **Symcloud Storage volumes no longer intermittently enter `Degraded` state due to disk initialization failures.**
  Disk initialization jobs now automatically retry until they succeed if transient control plane instability causes them to fail.
* **Single-node cluster upgrades no longer fail due to race conditions.** A number of bugs in
  [`runc`](https://github.com/opencontainers/runc) have been resolved, eliminating
  race conditions that caused single-node cluster upgrade failures.

### Security

Security mitigations for the following vulnerabilities have been implemented in this release of Google Distributed Cloud connected:

* **OS layer security mitigations:** All CVEs that have been resolved up to the LTS kernel version 6.12.31 (inclusive).
* **GDC software-only security mitigations:** All mitigations listed in the [GDC software-only release notes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities) up to version [1.33.300-gke.60](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities#1.33) (inclusive).

### Feature

The following new functionality has been introduced in this release of Google Distributed Cloud connected:

* **Refreshed GDC connected servers G2 hardware.** We are now shipping refreshed Google Distributed Cloud connected
  servers G2 hardware based on the Dell XR8000 series platform. For more information, see
  [Plan the hardware configuration](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/requirements#hardware).
* **Virtual machine image download with Workload Identity.** You can now access Cloud Storage buckets that hold
  your virtual machine images using a Kubernetes service account impersonating a Google service account. For more
  information, see
  [Create a Cloud Storage bucket for virtual machine images](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/virtual-machines#create_a_bucket_for_vm_images).

### Issue

This release of Google Distributed Cloud connected contains the following known issues:

* **Symcloud Storage pods can enter a `CrashLoopBackOff` state due to bootstrapping failures.**. The Symcloud Storage
  worker pods can intermittently restart multiple times while bootstrapping, preventing the `config.ini` file from being
  generated, which causes the pods to fail repeatedly. To remedy this issue, contact
  [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).
* **Symcloud Storage jobs can stall due to thread lock contention.** A race condition caused by lock contention between
  multiple threads can prevent Symcloud Storage jobs, such as volume attachment, detachment, creation, or deletion to stall.
  To remedy this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).
* **Symcloud Storage activation can stall due to scheduling conflicts following transient pre-install job failures.**
  The pre-installation job does not tolerate transient failures, such as `containerd` issues. If a job pod fails but isn't
  automatically deleted, existing pod affinity constraints prevent a replacement pod from being scheduled. This leaves the
  job incomplete and stalls the Symcloud Storage activation process. To remedy this issue, contact
  [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).
* **`RobinCluster` status updates can be delayed after reconciliation.** The `RobinCluster` status may not immediately
  reflect a Ready state even after reconciliation has completed. This delay occurs because the Symcloud Storage Operator's
  back-off timer can increase to over 10 minutes during reconciliation, causing a lag in reporting the final status.
* **Network Operator metrics missing in Cloud Monitoring.** Metrics for Network Function operators are not reported in
  Cloud Monitoring if the Google Cloud project hosting the cluster exceeds its Cloud Monitoring API ingestion quota limits.
  To remedy this issue, review your Cloud Monitoring API quota usage. If you consistently reach the limits, request a quota
  increase through the Google Cloud Console.

### Libraries

The following Google Distributed Cloud connected components have been updated:

* **Symcloud Storage** has been updated to version 5.4.16-166.

### Fixed

The following issues have been resolved in this release of Google Distributed Cloud connected:

* **Single-node cluster upgrades no longer fail due to race conditions.** A number of bugs in
  [`runc`](https://github.com/opencontainers/runc) have been resolved, eliminating
  race conditions that caused single-node cluster upgrade failures.
* **Virtual machines no longer intermittently freeze.** Through a combination of updates to Symcloud Storage and
  [new firmware for the integrated Dell Remote Access Controller (iDRAC)](https://www.dell.com/support/home/en-in/drivers/driversdetails?driverid=kywdc&oscode=ws19l&productcode=oth-xr11),
  we have improved the resilience of virtual machine workloads against unstable mains power and resolved freezes
  caused by storage snapshotting. For more information, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/getting-support).
* **Improved reliability of virtual machine workloads.** This release addresses Symcloud Storage issues contributing to
  freezing and slow recovery of VM workloads: `iomgr` `bmap` cache assertion, `bmap` repopulation performance, and `bmap`
  garbage collection performance.
* **Virtual machine workloads no longer throw a `SyncFailed` error when reading large amounts of remote data.** A race
  condition was resolved that caused virtual machine workloads to stop responding to their clients if the network connection
  failed when reading large amounts of data remotely. The race condition caused the virtual machine to become unhealthy and
  report the following event: `SyncFailed virt-handler unknown error encountered sending command SyncVMI: rpc error: code = DeadlineExceeded desc = context deadline exceeded`.
* **Patroni cluster now synchronizes properly when restarted after an ungraceful shutdown.** If the Patroni cluster was not gracefully
  shut down, it could fail to synchronize correctly upon restart, leading to an outage of the Robin Service.
* **Symcloud Storage pods now start up properly even if some pods are not ready when a node is cordoned or terminated.** The Patroni
  `StatefulSet` used the `Ordered` pod management policy, which prevented remaining pods from starting up if the previous pod wasn't ready.
  The updated policy now allows each pod to recover regardless of the state of the other pods.

### Issue

This release of Google Distributed Cloud connected contains the following known issues:

* **Robin Service fails after restarting a worker node due to expired TLS certificates.** Symcloud Storage TLS certificates
  do not auto-renew. If a worker pod is restarted while the corresponding certificate is expired, all Robin host services report
  a `Critical` state. To remedy this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/getting-support).
* **Symcloud Storage jobs can stall due to thread lock contention.** A race condition caused by lock contention between multiple
  threads can cause Symcloud Storage jobs, such as volume creation, deletion, attachment, or detachment, to stall. To remedy this
  issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/getting-support).
* **Symcloud Storage pods can enter a `CrashLoopBackOff` state due to bootstrapping failures.** The Symcloud Storage worker pods
  can intermittently restart multiple times while bootstrapping, preventing the `config.ini` file from being generated, which causes
  the pods to fail repeatedly. To remedy this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/getting-support).
* **Symcloud Storage cluster in Degraded state after installation.** Transient control plane instability can cause the disk
  initialization job to fail and there is no automatic retry upon job failure. This results in the installation ending with
  the Symcloud Storage cluster in `Degraded` state. To remedy this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/getting-support).
* **Symcloud Storage activation can stall due to scheduling conflicts following transient pre-install job failures.** The pre-installation
  job does not tolerate transient failures, such as containerd issues. If a job pod fails but isn't automatically deleted, existing pod affinity constraints prevent a replacement pod from being scheduled. This leaves the job incomplete and stalls the Symcloud Storage activation process.
  To remedy this issue, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/getting-support).
* **`RobinCluster` status updates can be delayed after reconciliation.** The `RobinCluster` status may not immediately reflect
  a `Ready` state even after reconciliation has completed. This delay occurs because the Symcloud Storage Operator's back-off
  timer can increase to over 10 minutes during reconciliation, causing a lag in reporting the final status.

### Announcement

This is a patch release of Google Distributed Cloud connected (version 1.11.1). Google Distributed Cloud software updates
roll out gradually across regions. The latest version might not be immediately available on your Google Distributed Cloud
connected deployment.

---
## 2025-09-15

### Announcement

This is a minor release of Google Distributed Cloud connected (version 1.11.0). Google Distributed Cloud software updates
roll out gradually across regions. The latest version might not be immediately available on your Google Distributed Cloud
connected deployment.

### Feature

The following new functionality has been introduced in this release of Google Distributed Cloud connected:

* **Backup for VM workloads on GDC connected servers.** You can now backup and restore virtual machine workloads on your Google Distributed Cloud connected servers deployment, including scheduling. For more information, see [Back up a virtual machine](https://cloud.google.com/distributed-cloud/edge/latest/docs/vm-servers#back_up_a_virtual_machine).
* **Configurable runtime class for container workloads.** As part of gVisor integration in Google Distributed Cloud connected, you can now specify the default runtime class for container workloads at both Pod and cluster level. Cluster-level runtime class selection is a preview-level feature. For more information, see [Configure the runtime class for a Pod](https://cloud.google.com/distributed-cloud/edge/latest/docs/deploy#runtime-class).
* **Island mode networking.** Google Distributed Cloud connected now supports [island mode networking](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/flat-vs-island-network) on secondary network interfaces. For more information, see [(Optional) Configure island mode](https://cloud.google.com/distributed-cloud/edge/latest/docs/networking#island-mode).
* **`AppArmor` sandboxing audit logs for VM workloads.** Google Distributed Cloud connected now lets you enable audit logs for virtual machine workloads sandboxed using `AppArmor` policies. To enable audit log emission on an existing virtual machine workload, restart the corresponding virtual machine. For more information, see [View AppArmor sandboxing audit logs](https://cloud.google.com/distributed-cloud/edge/latest/docs/vm-servers#view_apparmor_sandboxing_audit_logs).
* **CoreDNS resolution for secondary networks.** Google Distributed Cloud connected now supports specifying a CIDR block for use with secondary networks at both Pod and cluster level. This allows for CoreDNS resolution on secondary network interfaces. For more information, see [`Network` resource](https://cloud.google.com/distributed-cloud/edge/latest/docs/network-function#Network).
* **Access clusters through Connect Gateway.** You can now access your Google Distributed Cloud connected clusters through Connect Gateway. For more information, see [Obtain cluster credentials through Connect Gateway](https://cloud.google.com/distributed-cloud/edge/latest/docs/clusters#gateway).
* **VNC support for accessing VM workloads through Connect Gateway.** You can now use VNC to access your virtual machine workloads through Connect Gateway.

### Security

Security mitigations for the following vulnerabilities have been implemented in this release of Google Distributed Cloud connected:

* **OS layer security mitigations:** CVE-2025-31498, CVE-2024-48615, CVE-2016-1585.
* **GDC software-only security mitigations:** All mitigations listed in the [GDC software-only release notes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities) up to version [1.32.100](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities#1.32) (inclusive).

### Libraries

The following Google Distributed Cloud connected components have been updated:

* **GDC software-only has been updated** to version 1.32.100. (This component was formerly known as GKE on Bare Metal and as Anthos Clusters on Bare Metal.)
* **Kubernetes** has been updated to version 1.32.4-gke.200.

### Fixed

The following issues have been resolved in this release of Google Distributed Cloud connected:

* **Machines no longer experience intermittent connectivity loss.** Google Distributed Cloud connected machines no longer experience intermittent connectivity loss; the underlying rare condition that can occur with fleet credential management has been resolved.
* **VNC sessions through Connect Gateway are now more resilient.** The stability of VNC sessions to virtual machine workloads through Connect Gateway has been improved.

### Issue

This release of Google Distributed Cloud connected contains the following known issues:

* **The `gvisor` runtime class is incompatible with Symcloud Storage persistent volumes in block mode.** If you set a workload that uses Symcloud Storage persistent volumes in block mode to use the `gvisor` runtime class, the workload fails. Symcloud Storage persistent volumes in filesystem mode are not affected.
* **Cilium does not differentiate between TCP and UDP protocols.** Cilium does not differentiate between TCP and UDP protocols for services that use both protocols on the same port number and routes traffic for both protocols to the same backend pods. This can render such services non-functional. To work around this issue, use a different port for each protocol.
* **Overlapping the Pod and cluster CIDR blocks for secondary networks causes network failure.** If you specify overlapping CIDR blocks for Pods and clusters using the `annotations.networking.gke.io/gdce-pod-cidr` and `annotations.networking.gke.io/gke-gateway-clusterip-cidr` annotations in the `Network` resource, the Google Distributed Cloud connected virtual networking subsystem might behave erratically, including loss of connectivity. Follow the guidelines in [(Optional) Configure island mode](https://cloud.google.com/distributed-cloud/edge/latest/docs/networking#island-mode) to prevent this issue.
* **The `anthos-multinet` container might take up to two hours to fully start.** You might intermittently experience a slower than normal startup for the `anthos-multinet` container (up to two hours). To remedy this issue, contact [Google Support](https://cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).

---
## 2025-08-15

### Libraries

The following Google Distributed Cloud connected components have been updated:

* **EdgeOS kernel** has been updated to version 5.15.177.
* **GDC software-only has been updated** from version 1.30.500 to version 1.31.400. (This component was formerly known as GKE on Bare Metal and as Anthos Clusters on Bare Metal.)
* **Kubernetes** has been updated from version 1.30 to version 1.31.
* **Symcloud Storage** has been updated from version 5.4.14 to version 5.4.16.

### Fixed

The following issues have been resolved in this release of Google Distributed Cloud connected:

* **Storage is now freed immediately upon cluster deletion.** After deleting a cluster, the storage used by that cluster is now freed up immediately. You no longer have to manually delete all persistent volumes in a cluster before deleting the cluster itself.
* **Virtual machine workloads no longer fail to restart or migrate if DHCP server address changes.** If you are using DHCP to assign IP addresses to your virtual machine workloads and the IP address of your DHCP server changes, your virtual machine workloads now automatically restart and successfully complete migration.

### Issue

This release of Google Distributed Cloud connected contains the following known issues:

* **Machines can experience intermittent connectivity loss.** Google Distributed Cloud connected machines can experience intermittent connectivity loss due to a rare condition that can occur with fleet credential management. To remedy this issue, contact [Google Support](https://cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).
* **The `anthos-multinet` container might take up to two hours to fully start.** You might intermittently experience a slower than normal startup for the `anthos-multinet` container (up to two hours). To remedy this issue, contact [Google Support](https://cloud.google.com/distributed-cloud/edge/latest/docs/getting-support).
* **Virtual machine workloads cannot coexist on the same virtual network with Pods that use DHCP for IP address assignment.** This is because virtual machine workloads need the `IPAMMode` parameter set to `external` to use DHCP, while Pods need the `IPAMMode` parameter set to `internal` to use DHCP. Pods with static IP address are not affected by this. This behavior is by design.

### Announcement

This is a minor release of Google Distributed Cloud connected (version 1.10.0).

### Feature

The following new functionality has been introduced in this release of Google Distributed Cloud connected:

* **Pause and resume cluster software upgrades.** Software upgrades for your Google Distributed Cloud connected clusters now automatically pause when a maintenance window ends and automatically resume when the next maintenance window starts. For more information, see [Availability best practices](https://cloud.google.com/distributed-cloud/edge/latest/docs/availability).
* **VM management in Cloud Console for GDCc servers.** You can now manage virtual machine workloads running on your Google Distributed Cloud connected servers deployments through the Cloud Console. For more information, see [Manage virtual machines on Distributed Cloud connected servers](https://cloud.google.com/distributed-cloud/edge/latest/docs/vm-servers).
* **Kernel memory accounting control.** You can now configure the `NodeSystemConfigUpdate` Network Function operator resource to exclude kernel-space memory from Pod memory usage calculation. For more information, see [`NodeSystemConfigUpdate` resource](https://cloud.google.com/distributed-cloud/edge/latest/docs/network-function#NodeSystemConfigUpdate).
* **Configurable per-node subnet mask size.** The `Network` Network Function operator resource now allows you to configure the subnet mask size for each node. For more information, see [`Network` resource](https://cloud.google.com/distributed-cloud/edge/latest/docs/network-function#Network).
* **Raw workload log export.** You can now access raw (unprocessed and untagged) workload logs for your Pods for export to your own log processor. For more information, see [Collect raw workload logs for external processing](https://cloud.google.com/distributed-cloud/edge/latest/docs/logs-metrics#collect_raw_workload_logs_for_external_processing).

### Changed

The following changes to existing functionality have been introduced in this release of Google Distributed Cloud connected:

* **Reduced minimum internet connection bandwidth requirement.** The minimum internet connection bandwidth required by Google Distributed Cloud connected to function reliably has been reduced. For more information, see [Internet connection bandwidth](https://cloud.google.com/distributed-cloud/edge/latest/docs/requirements#internet-bandwidth).

### Security

Security mitigations for the following vulnerabilities have been implemented in this release of Google Distributed Cloud connected:

* **OS layer security mitigations:** CVE-2024-56664, CVE-2024-56658, CVE-2023-52664, CVE-2024-27010, CVE-2024-56647, CVE-2024-53091.
* **GDC software-only security mitigations:** All mitigations listed in the [GDC software-only release notes](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities) from version [1.30.500](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities#1.30) up to version [1.31.400](https://cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vulnerabilities#1.31) (inclusive).

---
