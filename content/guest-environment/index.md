# Guest Environment

## 2025-09-03

### Announcement

Starting with version `20250901.00`, the guest agent is migrated to a new
plugin-based architecture to improve modularity. You can revert to the previous
version by setting the metadata attribute `enable-guest-agent-core-plugin` to
`FALSE`. For more information about the plugin-based architecture, see
[Guest agent](https://cloud.google.com/compute/docs/images/guest-agent).

This plugin-based guest agent is available for the following operating systems:

* Red Hat Enterprise Linux (RHEL) 9
* Rocky Linux 9
* CentOS Stream 9
* Oracle Linux 9
* AlmaLinux 9

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
