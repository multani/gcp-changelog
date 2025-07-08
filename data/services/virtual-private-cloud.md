# Virtual Private Cloud

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
