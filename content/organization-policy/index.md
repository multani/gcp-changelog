# Organization Policy

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
