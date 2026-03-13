# Guest Environment

## 2026-03-05

### Feature

Version `20260228.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is
now available for Debian 12, AlmaLinux 9, CentOS Stream 9, Oracle Linux 9,
Red Hat Enterprise Linux 9, and Rock Linux 9. To review the features and fixes
included in version `20260228.00` of the guest agent, see the
[March 2, 2026 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#March_02_2026).

---
## 2026-03-04

### Feature

Version `20260228.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is
now available for Windows. To review the features and fixes included in version
`20260228.00` of the guest agent, see the
[March 2, 2026 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#March_02_2026).

---
## 2026-03-03

### Feature

Version `20260228.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is
now available for Debian 11, AlmaLinux 8, CentOS Stream 8, Oracle Linux 8,
Red Hat Enterprise Linux 8, and Rock Linux 8. To review the features and fixes
included in version `20260228.00` of the guest agent, see the
[March 2, 2026 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#March_02_2026).

---
## 2026-03-02

### Fixed

Version `20260228.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent)
includes the following fixes:

* The guest agent is now able to add users to the Administrator group on
  different locales on Windows.
* The guest agent now signals itself ready only after the network setup
  has fully completed. This should prevent the guest agent from hitting race
  conditions with custom routing solutions that depend on the guest agent
  service.
* The guest agent no longer spams metadata SSH key errors when a key is
  incorrectly formatted.
* The guest agent now ensures proper reconnection of the primary NIC after a
  configuration rollback, specifically when `NetworkManager` is active. This
  resolves an issue where the NIC might not come back online in such
  scenarios.
* The guest agent now applies the value of the following configuration flags
  correctly: `Daemons.network_daemon` and
  `NetworkInterfaces.vlan_setup_enabled`.

### Feature

Version `20260228.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is
now available for Debian 13, AlmaLinux 10, CentOS Stream 10, Oracle Linux 10,
Red Hat Enterprise Linux 10, and Rock Linux 10. This version introduces the
following features:

* Supports bootstrapping credentials for the HTTPS endpoint for the metadata
  server by default. For more information about the HTTPS metadata server
  endpoint, see [HTTPS metadata server endpoints](https://docs.cloud.google.com/compute/docs/metadata/overview#https-mds).
* Includes a cleanup job that runs once a day and each time the guest agent manager
  service initializes. This cleanup job ensures that leftover plugin files and
  states are properly cleaned up.
* Supports dynamically starting locally installed extensions. This feature is
  disabled by default, but it can be toggled by setting the
  `enable_local_plugins` flag to `true` in the guest agent configuration file.

---
## 2025-12-18

### Fixed

Version `20251218.00` of the [guest agent](compute/docs/images/guest-agent) is
now available for Windows only. This version includes the following fixes:

* Fixes a crash loop in VM extensions due to a race condition where the guest
  agent manager service can sometimes try to connect to the extension before
  it is able to create and bind to its unix socket.
* Fixes an issue where the core plugin is not creating required registry keys
  before attempting to write to them.

---
## 2025-12-11

### Feature

Version `20251209.00` of the guest agent, which re-introduces the plugin-based
architecture to Windows, is now available.

For more information about the plugin-based architecture, see
[Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

The plugin-based architecture for Windows was previously rolled back due to a bug that prevented the correct setup of IP alias routes when used with the WSFC module, see [October 21, 2025 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#October_21_2025).

---
## 2025-12-08

### Fixed

Version `20251205.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is
available for Linux only. This version includes the following fixes:

* Fixes an issue where the metadata server would become inaccessible during
  the dynamic removal of multiple vLAN NICs.
* Fixes an issue where the metadata script runner failed to parse all
  supported URL patterns and formats.
* Rolls back multi-universe support for the Agent Communication Service (ACS)
  client due to issues in the default universe.

### Feature

Version `20251205.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is
available for Linux only. This version includes the following feature:

* Snapshot module now supports using NGUIDs to identify disks supporting a
  wider range of VM families.

---
## 2025-11-20

### Feature

Version `20251120.01` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is
now available for Windows only. This version includes the following fix:

* Changes the start mode guest agent from `auto` to `delayed-auto` on
  Windows Service Manager.

---
## 2025-11-17

### Feature

Version `20251115.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent)
is now available.

### Fixed

Version `20251115.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent)
is now available and includes the following fixes:

* Fixes an issue in the dynamic vLAN subsystem where the `dhclient` backend
  attempted to remove `netplan`'s vLAN NICs.
* Fixes a crash loop in the plugin manager caused by its handling of plugin
  logs.

---
## 2025-11-13

### Fixed

Version `20251107.01` includes a fix for the
[Startup script runner](compute/docs/instances/startup-scripts) component
that prevented it from writing status logs and script output to Cloud Logging.

### Feature

Version `20251107.01` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent)
is now available.

---
## 2025-10-31

### Fixed

Version `20251030.02` includes fixes for the plugin-based architecture that is used by guest agent. For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

* The Clock Skew module no longer causes time inconsistencies on VMs. The agent no longer attempts to synchronize the hardware clock (`hwclock`) when the VM's Real-time Clock (RTC) isn't set to Coordinated Universal Time 0(UTC). For more information about how the guest agent handles clock synchronization, see [Clock Synchronization](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#clock-synchronization).
* The `vlan_setup_enabled` option now correctly sets up Dynamic Network Interfaces (NICs). [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics) now initialize reliably.
* The agent now prevents a race condition in network interface and route setup. Previously, routes were temporarily flushed if they were added before a DHCP lease was acquired. The agent now ensures routes persist correctly, preventing a brief period of missing routes. These routes were previously auto-corrected after approximately one minute.

---
## 2025-10-21

### Fixed

Version `20251009.01` of the guest agent, announced in the [October 20, 2025 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#October_20_2025), has been rolled back. This version introduced the plugin-based architecture to Windows but contained a bug in the [WSFC module](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#windows-failover).
To resolve this issue, guest agent version `20251011.00` is now available for Windows, which excludes the new plugin-based architecture.

---
## 2025-10-20

### Feature

Version `20251009.01` of the guest agent, which introduces the plugin-based
architecture to Windows, is now available.

For more information about the plugin-based architecture, see
[Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

---
## 2025-10-02

### Feature

Version `20250930.01` of the guest agent, which introduces the plugin-based
architecture to Debian 11, is now available.

For more information about the plugin-based architecture, see
[Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

---
## 2025-09-30

### Fixed

Version `20250930.01` includes the following fixes for issues found in the
plugin-based architecture. For more information about the plugin-based
architecture, see [Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

* Fixes an issue where the networking module incorrectly added routes when
  `ip_forwarding` and `target_instance_ips` settings were disabled in `/etc/default/instance_configs.cfg`.
* Prevents unnecessary error logs in the OS Login module caused by attempts to
  read a non-existent file.

---
## 2025-09-26

### Feature

Version `20250926.00` of the guest agent is now available. This guest agent
version introduces the plugin-based architecture to Debian 12.

For more information about the plugin-based architecture, see
[Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

---
## 2025-09-18

### Feature

Version `20250918.01` of the guest agent is now available. This guest agent
version introduces the plugin-based architecture to the following Debian and
Enterprise Linux 10 operating systems:

* Red Hat Enterprise Linux (RHEL) 10
* Rocky Linux 10
* CentOS Stream 10
* Debian 13

For more information about the plugin-based architecture, see
[Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

### Fixed

Version `20250918.01` includes the following fixes for issues found in
plugin-based architecture. For more information about the plugin-based
architecture, see [Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

* Corrects an issue in the OS Login module that was incorrectly writing `perm_denied=die`
  [PAM](https://en.wikipedia.org/wiki/Pluggable_Authentication_Module) module
  configuration when two-factor authentication isn't enabled.
* Fixes an issue in the metadata-based SSH module where re-adding a user didn't
  add the user to the sudoers group.

---
## 2025-09-09

### Feature

Version `20250907.00` of the guest agent, which introduces the plugin-based
architecture to Enterprise Linux 8 operating systems, is now available. For more
information about the plugin-based architecture, see [Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

With this version, the plugin-based guest agent is now also available for the
following operating systems:

* Red Hat Enterprise Linux (RHEL) 8
* Rocky Linux 8
* CentOS Stream 8
* Oracle Linux 8
* AlmaLinux 8

### Fixed

Version `20250907.00` includes the following fixes for issues found in guest
agent version `20250901.00`:

* Corrects an issue in the OS Login module that was incorrectly handling
  optional runtime systemd dependencies and causing an error log.
* Fixes a bug that could cause the metadata SSH key module to enter an infinite
  loop when setting up SSH keys. This occurred if an initial setup attempt failed
  and the metadata server returned the SSH keys in a different order on a
  subsequent retry.

---
## 2025-09-03

### Feature

With the introduction of the plugin-based architecture, the guest agent includes
the following updates:

* A new command-line tool, `ggactl_plugin`, is available to manage and restart
  the guest agent core plugin. To restart the agent, run:

  ```
  ggactl_plugin coreplugin restart

  ```

  For more information, see [Restarting the guest agent](https://cloud.google.com/compute/docs/images/manage-guest-agent#restart-guest-agent).
* All guest agent components now use a new logging framework. This framework
  lets you set the logging level in the
  [guest agent configuration file](https://cloud.google.com/compute/docs/images/manage-guest-agent#update-guest-agent-config).
  For more information about the logging options, see [core settings](https://cloud.google.com/compute/docs/images/manage-guest-agent#core)
  in the configuration options table.
* The workload refresh service `gce-workload-cert-refresher` is now part of the
  guest agent's core plugin. It is no longer a separate systemd service.
* The guest agent updates the metadata script runner and the Authorized Keys
  binary (Windows only) to use the new, configurable logging framework.
  Compatibility managers are included to facilitate the migration.

### Fixed

An issue is fixed where network routes were not consistently applied
([GitHub Issue #516](https://github.com/GoogleCloudPlatform/guest-agent/issues/516)).
The system now consistently applies network routes by monitoring the route table
and re-adding routes when they disappear.

---
