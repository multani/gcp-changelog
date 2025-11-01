# Cloud Load Balancing

## 2025-10-31

### Changed

The global and classic external Application Load Balancers implemented on
Google Front-Ends (GFEs) now reject TLS connections when the client and the load
balancer support ALPN (Application-Layer Protocol Negotiation), but don't share
common ALPN protocols.

Previously, if a client proposed a list of application protocols during the TLS
handshake using the ALPN extension and none were supported by the load balancer,
ALPN would be deactivated and the connection would default to using HTTP/1 as
the default application protocol. After this update, the GFE instead returns
an `SSL_TLSEXT_ERR_ALERT_FATAL` response which causes the load balancer to
terminate the TLS handshake, and the connection to close. This change ensures
that an application-layer protocol is always explicitly negotiated between the
clients and the load balancers that support ALPN.

---
## 2025-10-29

### Feature

You can specify a custom ephemeral `/96` IPv6 address range when creating a
regional IPv6 forwarding rule. For more information, see the following:

* [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal)
* [Backend service-based external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
* [Protocol forwarding overview](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding)

This feature is in **General availability**.

---
## 2025-10-28

### Feature

Application Load Balancers support authorization policies that let you
establish access control checks for incoming traffic.

For details, see
[Authorization policy overview](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview).

This feature is in **General availability**.

### Feature

Application Load Balancers support authorization policies that let you
establish access control checks for incoming traffic.

For details, see
[Authorization policy overview](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview).

This feature is in **General availability**.

### Feature

Both internal passthrough Network Load Balancers and external passthrough Network Load Balancers support load balancing to managed
instance groups (MIGs) comprised of IPv6-only VM instances.

For more details, see the following pages:

* [Set up an external passthrough Network Load Balancer with a backend service](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service)
* [Set up an internal passthrough Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal)

This feature is in **General availability**.

---
## 2025-10-06

### Feature

Percentage-based request mirroring is now supported for the global and regional external Application Load Balancers (classic is not supported). By default, the mirrored backend service receives all requests, even if the original traffic is being split between multiple weighted backend services. You
can now configure the mirrored backend service to receive only a percentage of the
requests by using the `mirrorPercent` flag to specify the percentage of
requests to be mirrored, expressed as a value between 0 and 100.0.

For an example, see [Set up traffic management for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#mirror_traffic).

This feature is available in **General availability**.

---
## 2025-09-17

### Security

A security fix was made which changes the behavior of requests and responses sent with the `Transfer-Encoding: Chunked` header to be more RFC 9112 compliant. The [RFC states](https://datatracker.ietf.org/doc/html/rfc9112#name-chunked-transfer-coding) that both the `chunked_body` and the `last-chunk` fields must end in `CRLF`. This is now enforced.

---
## 2025-09-12

### Changed

The global and classic external Application Load Balancers implemented on Google Front-Ends (GFEs) now support HTTP/1.0 explicitly as a protocol during ALPN (Application-Layer Protocol Negotiation) negotiation.

Previously, when the GFEs didn't support HTTP/1.0 explicitly, the GFE would return an `SSL_TLSEXT_ERR_NOACK` response, disable ALPN, and fall back to using HTTP/1 (which includes HTTP/1.0 and HTTP/1.1) as the default application protocol. After this change, GFEs will instead return `HTTP/1.0`, which provides clients with positive confirmation that their advertised `HTTP/1.0` was accepted.

You are not expected to make any changes with this update. If a TLS handshake with HTTP/1.0 is unsuccessful, please contact [support](https://cloud.google.com/load-balancing/docs/getting-support).

---
## 2025-08-26

### Feature

The internal and external passthrough Network Load Balancers now support load balancing to unmanaged instance groups comprised of IPv6-only VM instances.

Protocol forwarding also supports IPv6-only target instances.

For more details, see the following pages:

* [Protocol forwarding overview](https://cloud.google.com/load-balancing/docs/protocol-forwarding)
* [Backend service-based external passthrough Network Load Balancer overview](https://cloud.google.com/load-balancing/docs/network/networklb-backend-service)
* [Internal passthrough Network Load Balancer overview](https://cloud.google.com/load-balancing/docs/internal)
* [Set up an internal passthrough Network Load Balancer with IPv6-only subnets and backends](https://cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure-ipv6-only)

This feature is available in **General Availability**.

---
## 2025-08-05

### Feature

Cross-region internal Application Load Balancers can now route requests for static content to Cloud Storage buckets.

For more information, see [Set up a cross-region internal Application Load Balancer with Cloud Storage buckets](https://cloud.google.com/load-balancing/docs/l7-internal/setup-cross-region-internal-https-buckets).

This capability is now in **General Availability**.

---
## 2025-07-30

### Changed

**Starting October 15, 2025, the global and classic external Application Load Balancers are improving HTTP header handling for headers with obs-fold values to comply with the [RFC 9112](https://www.rfc-editor.org/rfc/rfc9112.html#section-5.2) standard**

Previously, these load balancers would forward HTTP headers with obs-fold values (those split across multiple lines, with subsequent lines starting with a space or a tab) without any changes. Starting October 15, 2025, each obs-fold will be replaced with one or more space characters (SP octets) before forwarding the message upstream. This ensures that the header is correctly interpreted as a single line, as required by the HTTP specification.

**What you need to do**

Review your current client applications and backend services before October 15, 2025 and ensure that they generate HTTP headers with obs-fold values in a single-line format when communicating with these load balancers.

Because the obs-fold header fields have been deprecated in RFC 9112, compliant clients and servers should already avoid using this format. However, there is a possibility that services that specifically rely on the old, non-compliant multi-line format of headers with obs-fold values might experience unexpected behavior. You should proactively check your backend service logs for any errors originating from your services due to the modified obs-fold headers.

For more information on the HTTP specification regarding headers with obs-fold values, review [RFC 9112, Section 5.2: Obsolete Line Folding](https://www.rfc-editor.org/rfc/rfc9112.html#section-5.2).

---
## 2025-07-28

### Feature

Global external Application Load Balancers now support the [JA4 fingerprint](https://github.com/FoxIO-LLC/ja4/blob/main/technical_details/JA4.md). The JA4 fingerprint can be added to a [custom request header](https://cloud.google.com/load-balancing/docs/https/custom-headers-global?variables#variables) using the `tls_ja4_fingerprint` variable.

This capability is now in **General Availability**.

---
## 2025-07-09

### Feature

Application Load Balancers and Proxy Network Load Balancers now support TLS certificates with large key sizes. Previously, these load balancers supported only certificates with RSA-2048 or ECDSA P-256 key types. With this update, you can now use self-managed certificates with RSA-3072, RSA-4096, and ECDSA P-384 keys.

**Key details**:

* Supported key types (for self-managed certificates): RSA-2048, RSA-3072, RSA-4096, ECDSA P-256, and ECDSA P-384
* Load balancing coverage for self managed certificates:

  + Certificate Manager SSL certificates: Global and regional load balancing
  + Compute Engine SSL Certificates: Regional load balancing
* Pricing: An additional charge of $0.45 per 1 million connections applies with certificates that use RSA-3072 and RSA-4096 key types. There are no per-connection charges for certificates that use RSA-2048, ECDSA P-256, or ECDSA P-384 key types.

For more information, see the documentation for [Supported key types](https://cloud.google.com/load-balancing/docs/ssl-certificates#key-types).

This capability is now in **General Availability**.

---
## 2025-07-08

### Feature

Zonal affinity, configured on the backend service of an internal passthrough Network Load Balancer, lets you limit cross-zone traffic, reduce latency, and improve performance, all while maintaining the benefits of a multi-zonal architecture.

Internal passthrough Network Load Balancers support three zonal affinity options that offer varying degrees of preference for routing new connections to eligible backends that are in the same zone as a supported client.

For more information, see [Zonal affinity for internal passthrough Network Load Balancers](https://cloud.google.com/load-balancing/docs/internal/zonal-affinity).

This feature is in **Preview**.

---
## 2025-06-26

### Feature

In typical HTTPS communication, neither the load balancer nor the backend verify each other's identity, assuming that they are within a secure perimeter and can be trusted. However, when perimeter security needs reinforcement or communication extends beyond the perimeter, backend mTLS becomes essential. Backend mTLS ensures secure communication by requiring both the load balancer and the backend to mutually verify their identities.

With *backend authenticated TLS*, the load balancer verifies the backend server's certificate by checking its chain of trust, thereby confirming the backend's identity. Conversely, with *backend mTLS*, the backend server verifies the client certificate presented by the load balancer. Together, these mechanisms enable backend mTLS, ensuring that both parties validate each other's identity.

Backend mTLS complements frontend mTLS, which is already generally available (GA).

For details, see the following:

* [Backend mTLS overview](https://cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls)
* [Set up backend authenticated TLS](https://cloud.google.com/load-balancing/docs/backend-authenticated-tls-setup)
* [Set up backend mTLS](https://cloud.google.com/load-balancing/docs/backend-mtls-setup)

This capability is in **General Availability** for global external Application Load Balancers.

---
## 2025-06-13

### Feature

Cloud Load Balancing supports load balancing to multi-NIC instances that use [Dynamic NICs](https://cloud.google.com/vpc/docs/multiple-interfaces-concepts).

This capability is in **Preview**.

---
## 2025-06-03

### Feature

Application Load Balancers now support the use of *custom metrics* that let you configure your load balancer's traffic distribution behavior to be based on metrics specific to your application or infrastructure requirements, rather than Google Cloud's standard utilization or rate-based metrics. Defining custom metrics for your load balancer gives you the flexibility to route application requests to the backend instances and endpoints that are most optimal for your workload.

For more information, see [Custom metrics for Application Load Balancers](https://cloud.google.com/load-balancing/docs/https/applb-custom-metrics).

This capability is in **General availability**.

### Feature

Cleartext HTTP/2 over TCP, also known as H2C, lets you use HTTP/2 without TLS. H2C is supported by internal and external Application Load Balancers for both of the following connections:

* Connections between clients and the load balancer. No special configuration is required. Support for this capability is already in **General Availability**.
* Connections between the load balancer and its backends. Support for this capability is now in **General Availability**.

  To configure H2C for connections between the load balancer and its backends, you set the backend service protocol to `H2C`.

---
