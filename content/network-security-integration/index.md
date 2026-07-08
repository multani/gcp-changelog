# Network Security Integration

## 2026-06-30

### Feature

The broker mode for out-of-band Network Security Integration (also known as
packet broker) is now available in **General Availability (GA) with allowlist**.
Broker mode lets you mirror GENEVE-encapsulated network packets from a consumer
network to multiple producer networks for analysis, and adds additional GENEVE
metadata (such as timestamp and network stable ID).
This feature is not available to all users. To access this feature, contact your
Google account team.

For more information, see [Out-of-band integration
overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview#oob-modes)
and [Understand GENEVE
format](https://docs.cloud.google.com/network-security-integration/docs/understand-geneve).

### Feature

Project-level security profiles and security profile groups for Network Security
Integration are now available in **General Availability (GA)**.

For more information, see [Security profiles
overview](https://docs.cloud.google.com/network-security-integration/docs/security-profiles-overview) and
[Security profile groups
overview](https://docs.cloud.google.com/network-security-integration/docs/security-profile-groups-overview).

---
## 2026-05-04

### Feature

You can now enable zonal affinity for your Network Security Integration in-band
integration deployments and configure zonal interception with regional backends.
For more information, see [Zonal
affinity](https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-integration-overview#zonal-affinity).

---
## 2026-01-14

### Feature

You can now integrate your network security appliances directly in the network traffic path for inspection and identify any threats before the traffic reaches its destination. For more information, see [In-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-integration-overview). This feature is available in **General Availability**.

---
## 2025-06-05

### Changed

Network Security integration now retains 396 bytes for the GENEVE encapsulation overhead. Consumer networks must use the maximum transmission unit (MTU) size of 8500 bytes or less. Producer networks must use an MTU at least 396 bytes more than the consumer network. For more information, see [GENEVE encapsulation and MTU requirements](https://cloud.google.com/network-security-integration/docs/understand-geneve#geneve-mtu).

---
