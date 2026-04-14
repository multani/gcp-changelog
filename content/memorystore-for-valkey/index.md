# Memorystore for Valkey

## 2026-04-13

### Feature

Version 1.0 of [Bloom filters](https://docs.cloud.google.com/memorystore/docs/valkey/about-bloom-filters) and [JSON documents](https://docs.cloud.google.com/memorystore/docs/valkey/about-json) is [Generally Available](https://docs.cloud.google.com/products#product-launch-stages).

---
## 2026-04-06

### Feature

You can use the [Memorystore for Valkey remote MCP server](https://docs.cloud.google.com/memorystore/docs/valkey/use-memorystore-mcp).
This server lets you connect to Memorystore for Valkey instances from LLMs, AI
applications, and AI-enabled development platforms. This feature is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

---
## 2026-03-26

### Feature

In addition to the [per-instance CA mode](https://docs.cloud.google.com/memorystore/docs/valkey/manage-in-transit-encryption), Memorystore for Valkey offers the following new CA modes:

* [**Shared CA**](https://docs.cloud.google.com/memorystore/docs/valkey/use-shared-ca): a managed,
  regionalized CA infrastructure. For each region, you can download a single CA
  certificate bundle. This bundle is valid for all instances located in a region
  that you configure to use the shared CA. Using a shared CA reduces the number of
  certificates that clients need to manage. This CA mode is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).
* [**Customer-managed CA**](https://docs.cloud.google.com/memorystore/docs/valkey/use-customer-managed-ca):
  use your own CA pool that's hosted on [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs). If your client applications are configured to trust this CA, then your
  applications can connect to an instance without you having to download and
  install additional CA certificates. This gives you greater control and helps you
  meet compliance requirements. This CA mode is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

### Feature

Memorystore for Valkey supports version 1.0 of [Bloom filters](https://docs.cloud.google.com/memorystore/docs/valkey/about-bloom-filters) and [JSON documents](https://docs.cloud.google.com/memorystore/docs/valkey/about-json). This feature is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

---
## 2026-03-18

### Feature

You can use the Google Cloud console to [find and set maintenance windows](https://docs.cloud.google.com/memorystore/docs/valkey/find-and-set-maintenance-windows) and [perform self-service maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/self-service-maintenance) on instances. This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

---
## 2026-03-17

### Feature

The [simulate maintenance event](https://docs.cloud.google.com/memorystore/docs/valkey/simulate-maintenance) feature for Memorystore for Valkey is [Generally Available](https://docs.cloud.google.com/products#product-launch-stages).

### Feature

You can now deploy instances in the `asia-southeast3` (Bangkok), `europe-north2`
(Stockholm), and `northamerica-south1` (Mexico)
[regions](https://docs.cloud.google.com/memorystore/docs/valkey/locations).

---
## 2026-03-11

### Feature

[Support](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions) for version 9.0 of Valkey
is [Generally Available](https://cloud.google.com/products#product-launch-stages).

---
## 2026-02-10

### Feature

You can now use the Google Cloud console to [manage backups](https://docs.cloud.google.com/memorystore/docs/valkey/manage-backups).
This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

---
## 2026-01-23

### Feature

Added [support](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions) for Valkey version
9.0. As a result, you can now upgrade the version of your Memorystore for Valkey
instance to 9.0. For more information, see [About upgrading the Valkey version of an instance](https://docs.cloud.google.com/memorystore/docs/valkey/about-upgrading-version). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-12-18

### Feature

Memorystore for Valkey supports [organization policy constraints](https://docs.cloud.google.com/memorystore/docs/valkey/about-cmek#org-policy) for customer-managed encryption keys (CMEK). By using
these constraints, you can enforce CMEK protection for your instances and limit
which Cloud Key Management Service (KMS) keys you can use for this protection.
This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

---
## 2025-12-11

### Feature

You can now deploy instances in the [`africa-south1` (Johannesburg)](https://docs.cloud.google.com/memorystore/docs/valkey/locations) region.

---
## 2025-11-17

### Feature

The [`/node/server/healthy`](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#node-level_metrics)
metric is [Generally Available](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-22

### Feature

We have implemented a [security fix](https://docs.cloud.google.com/memorystore/docs/valkey/security-bulletins#gcp-2025-061) for [CVE-2025-49844](https://nvd.nist.gov/vuln/detail/CVE-2025-49844).

---
## 2025-10-21

### Feature

You can now use [self-service maintenance](https://docs.cloud.google.com/memorystore/docs/valkey/self-service-maintenance)
to update your instance to a newer version. This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-17

### Feature

You can now [create an instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances) in
Memorystore for Valkey, even if a zone of the region where you want the instance
to be created is unavailable. If this occurs, then Memorystore for Valkey creates
the instance in the available zones of the region. This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-10

### Feature

Memorystore for Valkey now supports maintenance changelogs. Maintenance
changelogs provide information about updates available in new maintenance
versions, such as patches for security vulnerabilities.

For links to current maintenance changelogs for each major version of
Memorystore for Valkey, see [Memorystore for Valkey maintenance changelogs](https://docs.cloud.google.com/memorystore/docs/valkey/maintenance-changelog). This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-06

### Feature

For each primary node of a Memorystore for Valkey instance, you can now have up to
five replica nodes. For more information, see [Memorystore for Valkey overview](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview). This feature is [Generally Available](https://cloud.google.com/products#product-launch-stages).

---
