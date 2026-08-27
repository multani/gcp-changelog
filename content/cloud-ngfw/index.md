# Cloud NGFW

## 2026-08-17

### Feature

Support for the Advanced malware sandbox (WildFire) service is now restored.
You can now use Advanced malware sandbox to perform deep inspection of
network-routed file transfers and block zero-day malware before it reaches
your workloads. Advanced malware sandbox
is available in the Cloud Next Generation Firewall Enterprise tier.

For more information, see
[Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire) and
[Configure Advanced malware sandbox in your network](https://docs.cloud.google.com/firewall/docs/configure-wildfire).
This feature is available in **Preview**.

---
## 2026-07-30

### Announcement

The limits for the following Cloud NGFW resources have been updated:

* Security profile groups with threat prevention per project: 35
* Security profile groups with URL filtering per project: 35
* Firewall endpoint associations per organization-level firewall endpoint: 50
* Firewall endpoint associations per project-level firewall endpoint: 50

For more information, see [Quotas and limits](https://docs.cloud.google.com/firewall/docs/quotas).

---
## 2026-07-27

### Breaking

Enabling Advanced malware sandbox (WildFire) in an existing firewall
endpoint can cause a temporary data plane outage. As a result, the
Advanced malware sandbox feature is temporarily removed.

---
## 2026-07-20

### Feature

You can now use the Advanced malware sandbox (WildFire) service to protect
your network against unknown, novel malware, and file-based threats.
Advanced malware sandbox integrates dynamic machine learning (ML) and
cloud-based behavioral sandboxing to perform deep inspection of network-routed
file transfers and block zero-day malware before it reaches your workloads.
Advanced malware sandbox is available in the Cloud Firewall Enterprise tier.

For more information, see [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire) and
[Configure Advanced malware sandbox in your network](https://docs.cloud.google.com/firewall/docs/configure-wildfire). This
feature is available in **Preview**.

---
## 2026-06-30

### Feature

You can now create and configure project-level resources for application layer
inspection in Cloud NGFW, including project-level firewall endpoints, security
profile groups, and security profiles. For more information, see
[Organization-level and project-level
resources](https://docs.cloud.google.com/firewall/docs/about-app-layer-inspection#org-project-resources),
[Firewall endpoints overview](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints),
[Security profile groups overview](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups),
and [Security profiles overview](https://docs.cloud.google.com/firewall/docs/about-security-profiles). This
feature is available in **General Availability**.

### Feature

To restrict traffic to the managed Envoy proxies in a
[proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets), you can configure
global network firewall policies and regional network firewall policies to
protect internal Application Load Balancers and internal proxy Network Load
Balancers. For more information, see [Use global network firewall policies to
protect Envoy-based load balancers](https://docs.cloud.google.com/firewall/docs/global-network-app-lb) and
[Use regional network firewall policies to protect internal Application Load
Balancers and internal proxy Network Load
Balancers](https://docs.cloud.google.com/firewall/docs/regional-network-app-lb). This feature is available in
**General Availability**.

---
## 2026-05-04

### Feature

You can now create and configure the following organization-level Cloud NGFW
resources within a Google Cloud project:

* Security profiles
* Security profile groups
* Firewall endpoints
* Firewall endpoint associations

For more information, see [Security profile
overview](https://docs.cloud.google.com/firewall/docs/about-security-profiles), [Security profile group
overview](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups), and [Firewall endpoint
overview](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints). This feature is available in **Public preview**.

---
## 2026-03-24

### Feature

You can use the URL filtering service to filter your workload traffic by using
domain and Server Name Indication (SNI) information available in the egress
HTTP(S) messages. For more information, see
[URL filtering service overview](https://docs.cloud.google.com/firewall/docs/about-url-filtering). This
feature is available in **General Availability**.

---
## 2026-03-23

### Feature

Secure tags with a `purpose-data` attribute specifying a VPC network or an
organization now support VPC networks that are connected using VPC Network
Peering. For more information, see
[Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview).
This feature is available in **General Availability**.

---
## 2026-02-25

### Feature

You can use network contexts to meet your security goals by using fewer
firewall policy rules more efficiently. For more information, see
[Network contexts](https://docs.cloud.google.com/firewall/docs/understand-network-contexts). This feature
is available in **General Availability**.

---
## 2026-02-19

### Feature

Cloud NGFW now supports regional system firewall policies. Regional system
firewall policies are read-only policies that internal Google services, such as
Google Kubernetes Engine, use to secure their operations within a VPC network.
For more information, see [Regional system firewall
policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#regional-system-firewall-policies).
This feature is available in **General Availability**.

---
## 2026-01-13

### Feature

You can now create regional firewall policies that apply to managed Envoy proxies used by internal Application Load Balancers and internal proxy Network Load Balancers. For more information, see [Use regional network firewall policies to protect internal Application Load Balancers and internal proxy Network Load Balancers](https://docs.cloud.google.com/firewall/docs/regional-network-app-lb). This feature is available in **Preview**.

---
## 2025-11-17

### Feature

You can create a Remote Direct Memory Access (RDMA) over converged ethernet (RoCE) Virtual Private Cloud (VPC) network and configure firewall rules that apply to the network. For more information, see [Cloud NGFW for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/firewall-for-roce). This feature is available in **General Availability**.

---
## 2025-11-13

### Feature

You can create a firewall endpoint that supports jumbo frames up to 8,500 bytes in size. For more information, see [Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size). This feature is available in **General Availability**.

---
## 2025-09-23

### Feature

You can use the URL filtering service to filter your workload traffic by using domain and Server Name Indication (SNI) information available in the egress HTTP(S) messages. For more information, see [URL filtering service overview](https://cloud.google.com/firewall/docs/about-url-filtering). This feature is available in **Preview**.

---
## 2025-08-04

### Feature

You can create a secure tag at the organization level and bind its value to all virtual machine (VM) instances across that organization. For more information, see [Secure tags for firewalls](https://cloud.google.com/firewall/docs/tags-firewalls-overview). This feature is available in **General Availability**.

---
## 2025-07-25

### Feature

You can create a Remote Direct Memory Access (RDMA) over converged ethernet (RoCE) Virtual Private Cloud (VPC) network and configure firewall rules that apply to the network. For more information, see [Cloud NGFW for RoCE VPC networks](https://cloud.google.com/firewall/docs/firewall-for-roce). This feature is available in **Preview**.

---
## 2025-06-23

### Feature

You can create a secure tag at the organization level and bind its value to all virtual machine (VM) instances across that organization, instead of applying tags to instances within a specific network. For more information, see [Secure tags for firewalls](https://cloud.google.com/firewall/docs/tags-firewalls-overview). This feature is available in **Preview**.

---
