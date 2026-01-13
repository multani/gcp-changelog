# API Gateway

## 2026-01-12

### Feature

**Centralize API Gateway API management using Apigee API hub**

Connect API Gateway to Apigee API hub to enable seamless publishing of API metadata
from your API Gateway project to API hub. This integration provides a
centralized, unified view of your APIs across different gateways,
simplifying API discovery, governance, and management.

Key benefits include:

* **Centralized API discovery**: All your API Gateway APIs are discoverable in API hub alongside APIs from other sources
* **Enhanced visibility**: Gain insights into your API landscape with consolidated metadata
* **Streamlined management**: Simplify API governance and lifecycle management across your diverse API ecosystem

For more detail, see [Centralize API management using API hub](https://docs.cloud.google.com/api-gateway/docs/api-hub-overview).

**Note**: Rollouts of this release to production instances might take up to 5 business days to complete
across all Google Cloud zones. Your instances might not have the feature
available until the rollout is complete.

---
## 2025-11-12

### Announcement

On November 12, 2025, we released a new version of API Gateway.

### Feature

**API Gateway now supports OpenAPI version 3.0.**

With this release, API Gateway now supports OpenAPI version 3.0, including all patch versions (3.0.x).

Key Benefits:

* Simplified Deployment: Directly upload and deploy OpenAPI version 3.0.x specifications without prior conversion to 2.0.
* Enhanced Compatibility: Seamlessly integrate your OpenAPI version 3.0.x definitions with API Gateway.

For more detail, see [OpenAPI overview](https://docs.cloud.google.com/api-gateway/docs/openapi-overview).

---
## 2025-07-23

### Announcement

On July 23, 2025, we released an updated version of API Gateway.

### Deprecated

**Deprecation of Transport Layer Security (TLS) v1.0 and v1.1 protocols**

API Gateway now enforces TLS v1.2+. You can opt out of enforcing TLS v1.2+ for your API Gateway's new security settings by reaching out to [Google Cloud Support](https://cloud.google.com/support) to continue using your current protocol.

---
## 2025-06-09

### Announcement

On June 9, 2025, we released an updated version of API Gateway.

### Feature

With this release, the limit on the number of API gateways that can be created per region is increased to **50**.

For more information, see [Quotas and limits](https://cloud.google.com/api-gateway/docs/quotas)

---
