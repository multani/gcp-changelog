# Virtual Private Cloud

## 2025-09-23

### Feature

Service producers can publish services that are hosted on [cross-region internal Application Load Balancers](https://cloud.google.com/load-balancing/docs/l7-internal). This feature is available in **General Availability**. For more information, see [Publish services by using Private Service Connect](https://cloud.google.com/vpc/docs/configure-private-service-connect-producer).

---
## 2025-09-12

### Feature

You can create a VPC network that supports RDMA over [Falcon transport](https://cloud.google.com/blog/topics/systems/introducing-falcon-a-reliable-low-latency-hardware-transport), which lets you run AI and high performance computing (HPC) workloads on VM instances that have the `IRDMA` network interface type in Google Cloud, such as H4D instances. This feature is available in **Preview**. For more information, see [RDMA network profiles](https://cloud.google.com/vpc/docs/rdma-network-profiles).

---
## 2025-08-26

### Feature

IPv6-only subnets and instances are available in **General Availability**. For more information, see the following:

* [Add an IPv6-only subnet](https://cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only)
* [Create an IPv6-only instance](https://cloud.google.com/compute/docs/instances/create-ipv6-instance#create-vm-ipv6-only)
* [Configure IPv6-only subnets and instances with DNS64 and NAT64](https://cloud.google.com/vpc/docs/connect-ipv6-to-ipv4)

You can also use an IPv6-only NAT subnet to [publish a service with Private Service Connect](https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service).

For information about which services support IPv6-only configurations, see [IPv6 support in Google Cloud](https://cloud.google.com/vpc/docs/ipv6-support).

### Feature

VPC Flow Logs supports logging for [RDMA flows over Converged Ethernet](https://cloud.google.com/vpc/docs/rdma-network-profiles#overview), such as GPU-to-GPU flows from A3 Ultra, A4, and A4X VMs. This feature is available in **General Availability**. For more information, see [About VPC Flow Logs records](https://cloud.google.com/vpc/docs/about-flow-logs-records).

---
## 2025-08-08

### Feature

VPC Flow Logs includes metadata annotations for Google services such as Google APIs and VPC-hosted services. The following annotations are available in **General Availability**:

* `service_name`
* `connectivity`
* `private_domain`

These annotations are supported for flows between VMs in VPC networks and Google services and for flows between on-premises endpoints and Google services (through Cloud Interconnect and Cloud VPN). For more information, see [GoogleServiceDetails field format](https://cloud.google.com/vpc/docs/about-flow-logs-records#google-service-details).

---
## 2025-08-04

### Feature

When you reserve an internal range with an automatically allocated IPv4 CIDR block, you can specify the [allocation strategy](https://cloud.google.com/vpc/docs/internal-ranges#allocation-strategies) that is used to select a free block. This feature is available in **General Availability**.

---
## 2025-07-09

### Feature

Dynamic Private Service Connect interfaces are available in **Preview**. You can update VM instances to add or remove dynamic Private Service Connect interfaces without restarting or recreating the instance.

For more information, see [Private Service Connect interface types](https://cloud.google.com/vpc/docs/about-private-service-connect-interfaces#types).

### Feature

VPC Network Peering supports peering connections in consensus mode. This feature is available in **Preview**. For more information, see [Update strategy](https://cloud.google.com/vpc/docs/using-vpc-peering#update-strategy).

---
## 2025-07-08

### Feature

The following features of policy-based routes are available in **General Availability**:

* Applying policy-based routes to IPv6 traffic
* Using a next hop that is in a peered VPC network

For more information, see [Create policy-based routes](https://cloud.google.com/vpc/docs/use-policy-based-routes#create).

---
## 2025-06-27

### Feature

Private Service Connect service connectivity automation periodically retries endpoint create or delete operations that fail due to errors. This feature is available in **General Availability**. For more information, see [Automatic retries for endpoint failures](https://cloud.google.com/vpc/docs/about-service-connectivity-automation#endpoint-automation).

---
## 2025-06-18

### Feature

The following features of VPC Flow Logs are available in **Preview** through the Network Management API:

* [Enabling VPC Flow Logs for an organization](https://cloud.google.com/vpc/docs/using-flow-logs#enable-organization)
* [Enabling VPC Flow Logs for a VPC network](https://cloud.google.com/vpc/docs/using-flow-logs#enable-network)
* [Enabling VPC Flow Logs for a subnet](https://cloud.google.com/vpc/docs/using-flow-logs#network-management)

For more information, see [Supported configurations](https://cloud.google.com/vpc/docs/flow-logs#configurations).

---
## 2025-06-16

### Feature

VPC Flow Logs annotates RDMA traffic that is reported from A3 Mega VMs. This feature is available in **General Availability**. For more information, see [About VPC Flow Logs records](https://cloud.google.com/vpc/docs/about-flow-logs-records).

---
## 2025-06-13

### Feature

Dynamic Network Interfaces (NICs) are available in **Preview**.

Dynamic NICs let you update an instance to add or remove network interfaces without having to restart or recreate the instance.

You can also use Dynamic NICs when you need more network interfaces. The maximum number of vNICs for most machine types in Google Cloud is 10; however, you can configure up to 16 total interfaces by using Dynamic NICs.

For more information, see the following:

* [Dynamic NICs](https://cloud.google.com/vpc/docs/multiple-interfaces-concepts#dynamic-nics)
* [Create a VM instance with Dynamic NICs](https://cloud.google.com/vpc/docs/create-use-multiple-interfaces)
* [Add Dynamic NICs to an existing instance](https://cloud.google.com/vpc/docs/add-dynamic-nics)

---
## 2025-06-05

### Feature

You can [publish a Secure Web Proxy instance](https://cloud.google.com/secure-web-proxy/docs/deploy-service-attachment) as a Private Service Connect service. Making Secure Web Proxy available as a published service lets you centralize egress traffic management across multiple VPC networks. This feature is available in **General Availability**.

---
## 2025-05-28

### Feature

You can assign IPv6 bring your own IP (BYOIP) addresses to a subnet's external address range. These subnet ranges can only be used by VM instances, either as ephemeral or reserved addresses. To reserve addresses from these ranges, create a static regional external IPv6 address with the VM endpoint type. This feature is available in **General Availability**.

For more information, see [Create and use IPv6 sub-prefixes](https://cloud.google.com/vpc/docs/create-ipv6-sub-prefixes).

---
