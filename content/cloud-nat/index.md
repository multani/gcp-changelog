# Cloud NAT

## 2026-03-31

### Announcement

The default TCP [`TIME_WAIT`](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts)
timeout for Cloud NAT is scheduled to decrease from 120 seconds to 30 seconds,
across all regions, as follows:

* **From June 30 to September 29, 2026**: new Cloud NAT gateways will use either
  the 120-second or 30-second default, depending on when the update is
  deployed in a specific region.
* **On or after September 30, 2026**: all new Cloud NAT gateways in all regions
  will use the 30-second default.

**Impact on gateways**

* **New gateways**: after the update is deployed in a region, all new Cloud NAT
  gateways created in that region will use the 30-second default.
  This change also applies if a pre-update gateway is deleted and then recreated.
* **Existing gateways**: Cloud NAT gateways created before the regional update
  will retain the 120-second default. You can adjust this value by using the
  [--tcp-time-wait-timeout](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#change-conn-timeouts)
  flag at any time.

  Cloud NAT gateways configured with a custom `TIME_WAIT` value
  aren't affected and will continue to use your configured custom value.

The following table outlines the applicable default timeout for new gateways throughout the deployment timeline.

| Gateway type | Default timeout (before June 30) | Default timeout (June 30—September 29) | Default timeout (on or after September 30) |
| --- | --- | --- | --- |
| New | 120 seconds | 30 or 120 seconds | 30 seconds |

---
## 2025-10-21

### Feature

Private NAT supports Cloud Run in **General Availability**. For more
information, see [Supported resources](https://docs.cloud.google.com/nat/docs/overview#supported-resources).

---
## 2025-09-23

### Feature

Cloud NAT gateways for Public NAT support [source-based NAT rules](https://cloud.google.com/nat/docs/nat-rules-overview) for IPv4 addresses. This feature is available in **Preview**.

---
## 2025-08-26

### Feature

Cloud NAT gateways for Public NAT support IPv6 to IPv4 network address translation in **General Availability**. For more information, see [NAT64 in Public NAT](https://cloud.google.com/nat/docs/public-nat#nat64).

---
