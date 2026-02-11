# Resource Manager

## 2026-02-09

### Feature

Organization Policy Service custom constraints are available for some
Network Connectivity resources. For more information, see
[Manage VPC resources by using custom organization policies](https://docs.cloud.google.com/vpc/docs/custom-constraints).

---
## 2026-02-02

### Feature

Organization Policy Service custom constraints are available for some
Artifact Analysis resources. For more information, see
[Use custom organization policies](https://docs.cloud.google.com/artifact-analysis/docs/custom-constraints).

Organization Policy Service custom constraints are available for some Storage Transfer Service
resources. For more information, see
[Custom organization policy constraints](https://docs.cloud.google.com/storage-transfer/docs/custom-constraints).

### Feature

**Access Resource Manager using our remote MCP server**

You can use the Resource Manager remote MCP server to search for and identify all
Google Cloud projects you have permission to access, so you have the correct
identifiers before configuring specific resources.

The [Resource Manager remote MCP server](https://docs.cloud.google.com/resource-manager/reference/mcp) is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-11-13

### Feature

You can use custom constraints with Organization Policy to provide more
granular control over specific fields for some Dataform resources. For more
information, see
[Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints).
This feature is
[generally available](https://cloud.google.com/products#product-launch-stages)
(GA).

---
## 2025-11-11

### Changed

The list of Organization Policy Service constraints that are enforced when an organization
resource is created has changed. The following Google Cloud security baseline
constraints are enforced for all organizations created on or after May 3, 2024:
\* `constraints/iam.managed.disableServiceAccountKeyCreation`
\* `constraints/iam.managed.disableServiceAccountKeyUpload`
\* `constraints/iam.automaticIamGrantsForDefaultServiceAccounts`
\* `constraints/iam.allowedPolicyMemberDomains`
\* `constraints/essentialcontacts.managed.allowedContactDomains`
\* `constraints/compute.managed.restrictProtocolForwardingCreationForTypes`
\* `constraints/storage.uniformBucketLevelAccess`

For more information, see [Google Cloud security baseline constraints](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations).

---
## 2025-11-05

### Feature

You can use custom constraints with Organization Policy to provide more granular
control over specific fields for some BigQuery resources. For more information,
see [Manage BigQuery resources using custom constraints](https://docs.cloud.google.com/bigquery/docs/custom-constraints).
This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-10-30

### Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some CA Service resources. For more information, see [Manage CA Service resources using custom constraints](https://docs.cloud.google.com/certificate-authority-service/docs/custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some BigQuery sharing resources. For more information, see [Manage Sharing data exchanges and listings using custom constraints](https://docs.cloud.google.com/bigquery/docs/analytics-hub-custom-constraints). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

### Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for managed workload identities. For more information, see [Use custom organization policies for Managed workload identities](https://docs.cloud.google.com/iam/docs/managed-workload-identity-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

### Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Datastream resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/datastream/docs/custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-10-14

### Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Datastream resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/datastream/docs/custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-10-10

### Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Application Integration resources. For more information, see [Manage Application Integration resources using custom constraints](https://docs.cloud.google.com/application-integration/docs/custom-constraints). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-06

### Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Dataform resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

---
## 2025-10-03

### Feature

Select Workload Identity Federation resources let you use custom constraints to define your own restrictions on Google Cloud services. To learn which Workload Identity Federation resources support custom constraints and to view sample use cases, see [Use custom organization policies for Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-custom-constraints).

This feature is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-18

### Feature

Select Cloud Load Balancing resources let you use custom constraints to define your own restrictions on Google Cloud services. To learn which load balancing resources support custom constraints and to view sample use cases, see [Manage Cloud Load Balancing resources using custom constraints](https://cloud.google.com/load-balancing/docs/custom-constraints).

This feature is available in **General Availability**.

---
## 2025-09-11

### Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Live Stream API resources. For more information, see [Use custom custom constraints](https://cloud.google.com/livestream/docs/custom-constraints).

---
## 2025-09-10

### Feature

**Designate project environments with tags**: You can now use tags to visually distinguish projects based on their environment—such as production, staging, or development—directly within the Google Cloud console. This new visual indicator helps prevent errors and improves awareness when you're working in sensitive environments. For information, see [Designate project environments with tags](https://cloud.google.com/resource-manager/docs/creating-managing-projects#designate_project_environments_with_tags).

---
## 2025-09-09

### Feature

**Preview:** Eight new organization policy constraints are available to help you
enforce security best practices for Compute Engine virtual machine (VM)
instances.

These [managed constraints](https://cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints)
simplify governance for common security scenarios and integrate with safe
rollout tools like
[dry-run](https://cloud.google.com/resource-manager/docs/organization-policy/dry-run-policy)
and
[simulation](https://cloud.google.com/policy-intelligence/docs/test-organization-policies),
letting you test their impact before enforcement.

The new constraints are as follows:

* `compute.managed.disableNestedVirtualization`
* `compute.managed.disableSerialPortAccess`
* `compute.managed.disableSerialPortLogging`
* `compute.managed.disallowGlobalDns`
* `compute.managed.requireOsConfig`
* `compute.managed.requireOsLogin`
* `compute.managed.vmCanIpForward`
* `compute.managed.vmExternalIpAccess`

These constraints can evaluate metadata values at the [VM instance, project, or
zonal level](https://cloud.google.com/compute/docs/metadata/overview#metadata-directories). For more information about these managed constraints, see [Managed
Constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#managed-constraints) in the Resource Manager documentation.

---
## 2025-09-08

### Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Cloud Deploy resources. For more information, see [Use custom organization policies](https://cloud.google.com/deploy/docs/custom-org-policy).

---
## 2025-08-28

### Fixed

Certain Organization Policy [managed constraints](https://cloud.google.com/resource-manager/docs/organization-policy/overview#managed-constraints) that were released on August 21, 2025 were not functioning as intended. The Organization Policy Service evaluated these constraints as if the `effectiveInstanceMetadata` field of the resources that they were enforced on was empty, causing them to always evaluate to either allow or deny access to the resource.

The following managed constraints were evaluated to always allow creation of resources where they were enforced:

* `constraints/compute.managed.disableGuestAttributesAccess`
* `constraints/compute.managed.disableSerialPortAccess`
* `constraints/compute.managed.disableSerialPortLogging`

The following managed constraints were evaluated to always block creation of resources where they were enforced:

* `constraints/compute.managed.disallowGlobalDns`
* `constraints/compute.managed.requireOsConfig`
* `constraints/compute.managed.requireOsLogin`

This issue has been corrected, and these constraints now properly evaluate the `effectiveInstanceMetadata` field to determine whether resource creation should be allowed or blocked.

---
## 2025-08-18

### Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Backup for GKE resources. For more information, see [Manage Backup for GKE resources using custom constraints](https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/create-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

### Feature

You can now use organization policy conditions to match a tag key. This lets you enable or
disable enforcement against all resources with that tag key, regardless of what
tag value is attached. For more information, see [Setting an organization policy with tags](https://cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy).

---
## 2025-07-25

### Issue

Organization policies in dry-run mode are reporting inconsistent results for the following [managed constraints](https://cloud.google.com/resource-manager/docs/organization-policy/overview#managed_constraints):

* `constraints/compute.managed.restrictProtocolForwardingCreationForTypes`
* `constraints/iam.managed.allowedPolicyMembers`
* `constraints/essentialcontacts.managed.allowedContactDomains`
* `constraints/compute.managed.blockPreviewFeatures`

If a resource inherited an organization policy in dry-run mode that uses any of these managed constraints, that dry-run policy was evaluated without using the parameters specified in the live policy. Normally, an organization policy in dry-run mode that's inherited on a resource is overridden by the live organization policy set directly on that same resource. Not evaluating the live organization policy parameters in the inherited organization policy in dry-run mode led to inconsistent results.

Our engineering team is working to resolve this issue.

---
## 2025-07-01

### Feature

[Policy Simulator for Organization Policy](https://cloud.google.com/policy-intelligence/docs/test-organization-policies) is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

---
## 2025-06-13

### Feature

Custom organization policies are now generally available for some API Keys. For more information, see [Creating and managing custom constraints](https://cloud.google.com/api-keys/docs/custom-constraints).

---
## 2025-06-10

### Changed

You can use custom constraints with Organization Policy to provide more granular control over specific fields for indexes and index endpoints in Vector Search. For more information, see [Create custom constraints for Vector Search](https://cloud.google.com/vertex-ai/docs/vector-search/custom-constraints).

---
