# Cloud Load Balancing

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
