# Cloud Load Balancing

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
