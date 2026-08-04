# 579.0.0 (2026-08-04)

## 2026-08-04

### Breaking Changes

* **(API Registry)** Removed `gcloud api-registry mcp enable` and `gcloud api-registry mcp disable`. MCP server enablement is no longer required; enabling the underlying service is sufficient.
* **(Compute Engine)** Removed `PRESERVED_STATE` column from `gcloud compute instance-groups managed list-instances` output in beta.

### AI

* Route `gcloud ai` requests for the `us` multi-region to the Vertex AI multi-regional (REP) endpoint.

### Agent Identity

* Added `--three-legged-oauth-default-continue-uri` flag to `gcloud agent-identity auth-providers create` and `update` commands.

### Cloud Auth

* Enabled ECP HTTP Proxy support for external users (disabled by default).
* Added optional `--ecp-http-proxy` flag to `gcloud auth enterprise-certificate-config create` to support custom ECP HTTP proxy binary paths.

### Cloud Dataproc

* Promoted `--master-instance-selection`,
  `--master-instance-flexibility-policy-file`, `--worker-instance-selection`,
  `--worker-instance-flexibility-policy-file`,
  `--secondary-worker-instance-selection`, and
  `--secondary-worker-instance-flexibility-policy-file` flags to GA for
  `gcloud dataproc clusters create` and
  `gcloud dataproc workflow-templates set-managed-cluster`.

### Cloud Firestore Emulator

* Added support for `--require-indexes` and `--index-file` flags in `gcloud emulators firestore start` command.

### Cloud Functions

* Added `all-traffic` as an allowed value for `--direct-vpc-egress` flag in `gcloud functions deploy`.
* Promoted `gcloud functions upgrade` command to GA.

### Cloud NetApp

* Added `gcloud netapp volumes start-split` and `gcloud netapp volumes get-split-status` commands to GA track.

### Cloud Quotas

* Promoted `gcloud quotas` surface (info, preferences, and adjuster settings) to General Availability (GA).

### Cloud SQL

* Modified `gcloud sql instances reencrypt` to support zero-downtime
  re-encryption for most Cloud SQL instances, removing the previous downtime
  warning. Instances using C4, C4A, or N4 machine types are not yet supported for
  zero-downtime re-encryption; they will still restart during this operation and
  prompt a downtime warning.

### Cloud Services

* Updated `gcloud beta services mcp enable` command to be a no-op, as MCP enablement is no longer required.

### Cluster Director

* Fixed an issue where the default zone for cluster resources (storage, network, etc.) was always set to the location's "b" zone, overriding the user-specified zone in compute flags.
* Renamed `--blueprint` flag to `--reference-architecture` in `gcloud beta cluster-director clusters create`.

### Compute Engine

* Promoted `gcloud compute hosts` and `gcloud compute reservations hosts` to GA.
* Updated `gcloud compute reservations hosts list` and `gcloud compute reservations hosts describe` to require `--reservation` when `--reservation-block` is specified.
* Added support for 3500GB, and 7000GB partition sizes when creating
  local SSDs via `gcloud compute instances create` and
  `gcloud compute instance-templates create`.
* Promoted `--igmp-query` flag in `--network-interface` of `gcloud compute instance-templates create` to GA.
* Promoted `--igmp-query` flag in `gcloud compute instances network-interfaces add` to GA.
* Promoted `--igmp-query` flag in `--network-interface` of `gcloud compute instances bulk create` to GA.\* Added `gcloud compute http-health-checks test-iam-permissions` command.
* Added `--routing-mode` flag to `gcloud compute service-attachments create` and `update` commands in beta.
* Added `gcloud compute snapshot-groups test-iam-permissions` command in beta release track.
* Added `gcloud compute instances test-iam-permissions` command to test
  IAM permissions on a Compute Engine virtual machine instance in GA, beta,
  and preview.
* Added `gcloud compute interconnects groups set-iam-policy` command to set IAM policy on an interconnect group in beta, preview, and GA.
* Added `--exapool-capacity-optimized-capacity`,
  `--exapool-read-optimized-capacity`, and
  `--exapool-write-optimized-capacity` flags to
  `gcloud alpha compute storage-pools update` for Exapool storage pools.
* Added Arm `CCA` support to the `confidential-compute-type` option in `gcloud compute instance create`.
* Added `gcloud compute network-firewall-policies test-iam-permissions` command.
* Added `gcloud compute disks test-iam-permissions` command to test IAM permissions on a Compute Engine disk.
* Promoted `--ipv6-network-tier` flag of
  `gcloud compute networks subnets create` and
  `gcloud compute networks subnets update` to beta.
* Added `STANDARD` option to `--ipv6-network-tier` flag of
  `gcloud compute instances create`,
  `gcloud compute instance-templates create`,
  `gcloud compute instances network-interfaces add`, and
  `gcloud compute instances network-interfaces update` in beta.
* Added `gcloud compute routers test-iam-permissions` command to test specific IAM permissions on a Compute Engine router in beta.

### Compute Firewall Policies

* Promoted new ULL\_POLICY value for `--policy-type` flag of `gcloud compute network-firewall-policies create` to GA.

### Distributed Cloud Edge

* Promoted `gcloud edge-cloud zones list` to GA.

### GKE Hub

* Promoted
  `gcloud container fleet|hub config-management update` command to `beta`.

### Identity and Access Management

* Added `gcloud iam access-policies create|delete|describe|list|update|search-policy-bindings` commands to allow management of access policy resources.
* Added `--target-resource` flag to `gcloud iam policy-bindings create`.

### Kpt

* Updated kpt to v1.0.0-beta.67. See <https://github.com/kptdev/kpt/releases/tag/v1.0.0-beta.67> for more details.

### Kubernetes Engine

* Updated default kubectl to 1.35.6.
* Additional kubectl versions:
  + 1.30.14
  + 1.31.14
  + 1.32.13
  + 1.33.13
  + 1.34.10
  + 1.35.7
  + 1.36.3

### Network Services

* Deprecated `clientTlsPolicy` field in `gcloud network-services endpoint-policies`.
* Updated `gcloud network-services endpoint-policies` resource name pattern to support regional locations.

### Vmware Engine

* Added `--kms-key` flag to `gcloud vmware private-clouds create`. Specifying this flag with a valid KMS key resource name enables CMEK.
* Added `--encryption-type` and `--kms-key` flags to `gcloud vmware private-clouds update`. `--kms-key` (valid KMS key resource name) is required when `--encryption-type` is CMEK.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
