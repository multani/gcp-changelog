# Guest Environment

## 2025-11-13

### Feature

Version `20251107.01` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent)
is now available.

### Fixed

Version `20251107.01` includes a fix for the
[Startup script runner](compute/docs/instances/startup-scripts) component
that prevented it from writing status logs and script output to Cloud Logging.

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
