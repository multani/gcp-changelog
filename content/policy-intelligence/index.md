# Policy Intelligence

## 2026-06-03

### Feature

You can use Policy Analyzer to visualize allow policy queries. This
can help you understand the relationship between identities, roles, permissions,
and resources within your resource hierarchy.

Policy Analyzer supports queries about agent identities. You can see
who can access an agent or what resources and agents a specific agent can reach.

These features are available in in
[Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see
[Analyze allow policies](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies).

---
## 2026-05-08

### Feature

You can use the IAM recommender to remediate excessive
permissions for Google groups by transitioning from permanent role
bindings to temporary, on-demand entitlements in Privileged Access Manager (PAM). This
feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

To learn how to remediate excessive permissions, see [Remediate excessive
permissions with Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-remediate-iam-recommendations).

---
## 2025-11-24

### Feature

IAM administrators can review and manage identity risks
across their organization, folder, or project from the Google Cloud console
by using the **Security Insights** dashboard. For more information, see
[Review and manage identity risks](https://docs.cloud.google.com/policy-intelligence/docs/manage-identity-risks).

This feature is available in
[Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-11-13

### Changed

[Policy Simulator](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_iam_policy_simulator)
deny policy simulations on organization and folder resources are not protected
by VPC Service Controls. For more information, see
[Help secure Policy Intelligence APIs with VPC Service Controls](https://docs.cloud.google.com/policy-intelligence/docs/secure-apis-vpc-sc#simulator).

---
## 2025-11-04

### Feature

You can use Policy Troubleshooter to troubleshoot policies that include bindings
for [service account principal sets](https://docs.cloud.google.com/iam/docs/principal-identifiers#allow-service-account-principal-sets).
This feature is available in
[GA](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-22

### Fixed

The issue that caused IAM recommender role recommendations to be
inaccurate and out of date is fixed.

---
## 2025-10-16

### Feature

You can use Policy Troubleshooter to
[remediate access issues](https://docs.cloud.google.com/policy-intelligence/docs/remediate-requests). This
feature is available in
[Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-13

### Issue

Due to an ongoing issue, IAM recommender role recommendations
might be out of date and inaccurate. Removing roles or permissions can break
existing processes. Therefore, please validate usage before applying any changes.

---
## 2025-07-01

### Feature

[Policy Simulator for Organization Policy](https://cloud.google.com/policy-intelligence/docs/test-organization-policies) is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

---
