# Network Security Integration

## 2026-01-14

### Feature

You can now integrate your network security appliances directly in the network traffic path for inspection and identify any threats before the traffic reaches its destination. For more information, see [In-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-integration-overview). This feature is available in **General Availability**.

---
## 2025-06-05

### Changed

Network Security integration now retains 396 bytes for the GENEVE encapsulation overhead. Consumer networks must use the maximum transmission unit (MTU) size of 8500 bytes or less. Producer networks must use an MTU at least 396 bytes more than the consumer network. For more information, see [GENEVE encapsulation and MTU requirements](https://cloud.google.com/network-security-integration/docs/understand-geneve#geneve-mtu).

---
