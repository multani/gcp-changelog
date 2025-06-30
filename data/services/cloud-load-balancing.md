# Cloud Load Balancing

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
