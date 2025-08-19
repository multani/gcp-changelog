# Organization Policy

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
