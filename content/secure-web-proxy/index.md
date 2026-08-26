# Secure Web Proxy

## 2026-08-20

### Feature

Secure Web Proxy now supports the [local intermediate CA
signing](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection#ca-pool-intermediate-ca-config)
certificate issuance mode for TLS inspection. By using this mode,
Secure Web Proxy caches a single intermediate certificate authority (CA)
certificate from your CA pool to sign leaf certificates locally for requested
domains, reducing certificate issuance requests and transaction costs. To use
this certificate issuance mode, you must make sure that your CA pool is
configured to issue intermediate CA certificates.

For more information, see [Certificate issuance
modes](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview#certificate_issuance_modes)
and [Configure a local intermediate CA
signing](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection#ca-pool-intermediate-ca-config).
This feature is [generally
available (GA)](https://cloud.google.com/products#product-launch-stages).

---
## 2026-06-16

### Feature

You can now use [authorization
policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies)
to perform identity-based and content-based access control checks when
processing outbound traffic requests through Secure Web Proxy.

By [configuring authorization
policies](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies), you can set rules for
your workloads to access external destinations. You can also use these
authorization policies to delegate complex authorization decisions to identity
and content-scanning services like Service Extensions. This feature is
supported in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

You can [integrate frontend mutual TLS (mTLS) with
Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp) to boost
the security of your applications and workloads.

With this integration, you can use validated client identities in
Secure Web Proxy [authorization
policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies)
to enforce granular access control for outbound traffic. This feature is
supported in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-05-21

### Feature

When deploying your Secure Web Proxy instance as [next
hop](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop), you can now configure the gateway
to listen on all ports (from `1` to `65535`). By using this feature, your proxy
can automatically intercept and enforce security policies and rules to all
outbound traffic, removing the need to manage specific port lists.

This feature is supported in
[Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-08-18

### Feature

Support for [VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_swp) is [generally available](https://cloud.google.com/products/#general-availability) (GA).

---
