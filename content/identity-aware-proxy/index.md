# Identity-Aware Proxy

## 2026-08-31

### Feature

**IAM Unified Access Policies for Agent Gateway are generally available (GA)**

IAM Unified Access Policies (Access policies) for Agent Gateway and
Identity-Aware Proxy (IAP) are [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
Identity-Aware Proxy integrates with Agent Gateway and uses Access policies to
help secure and govern agentic egress communication between agent principals
and destination resources, such as Model Context Protocol (MCP) servers,
other agents, and registered or unregistered endpoints.

Key capabilities include:

* Multiple allow and deny rules within a single Access policy to establish
  fine-grained behavioral guardrails for egress traffic.
* Common Expression Language (CEL) condition evaluation in rules to enforce
  egress access criteria based on tool names, read-only constraints, HTTP
  methods, and URL paths.
* Dry-run and enforcement modes to validate and audit policy evaluation
  before blocking egress traffic.
* End-to-end agent identity authentication and authorization using mutual TLS
  (mTLS) and Context-Aware Access (CAA) with Demonstrating Proof of Possession
  (DPoP).

For more information, see [IAM access policies overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/iam-overview-uap).

---
## 2026-06-24

### Feature

Identity-Aware Proxy (IAP) supports securing agent-to-anywhere egress for Agent Gateway. The feature generally available [GA](https://cloud.google.com/products#product-launch-stages). To learn more about IAP support for Agent Gateway, see [IAP for agents overview](https://docs.cloud.google.com/iap/docs/agent-overview).

---
## 2026-03-13

### Feature

You can configure custom OAuth clients in Identity-Aware Proxy by using the
Google Cloud console; the feature is generally available [(GA)](https://cloud.google.com/products#product-launch-stages).
You must use custom OAuth clients to do the following:

* Configure IAP for users who are outside of an organization.
* Customize the OAuth consent screen with custom branding.
* Provide default OAuth clients for inherited applications across all
  IAP-protected resources at the organization
  or project level.

For more information, see [Use custom OAuth clients with IAP](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration).

---
## 2025-10-28

### Feature

The ability to use a path wildcard in the `aud` (audience) field when using a
service account JWT to authenticate with an IAP-secured resource
is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see
[Authenticate with a service account JWT](https://docs.cloud.google.com/iap/docs/authentication-howto#create_the_jwt).

---
## 2025-09-23

### Feature

The ability to use a path wildcard in the `aud` (audience) field when using a service account JWT to authenticate with an IAP-secured resource is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Authenticate with a service account JWT](https://cloud.google.com/iap/docs/authentication-howto#create_the_jwt)

---
