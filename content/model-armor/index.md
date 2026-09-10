# Model Armor

## 2026-09-04

### Feature

**Clarification: August 5, 2026 release note for Melbourne and Seoul**

In Melbourne (`australia-southeast2`) and Seoul (`asia-northeast3`), only the
Sensitive Data Protection filter is supported when data residency is
enforced. To use other Model Armor features in these regions,
[disable data residency enforcement in the
template](https://docs.cloud.google.com/model-armor/manage-templates#set-data-residency-compliance).

For information about available Model Armor features for each
region, see [Supported features by
region](https://docs.cloud.google.com/model-armor/feature-availability-by-region#supported-by-region).

---
## 2026-09-02

### Feature

Filter version `v3` will be promoted to the `Stable` alias on or before
September 25, 2026. On the same date, filter versions `v1` and `v2` transition
to `Legacy` status and retire on November 29, 2026.

If your templates use the `Stable` alias, they will automatically upgrade to
`v3` when it is promoted. If your templates use explicit version numbers (`v1`
or `v2`), migrate them to `v3` or the `Stable` alias before November 29, 2026.

For more information, see [Set the filter version for a
template](https://docs.cloud.google.com/model-armor/set-filter-version#release-timeline).

---
## 2026-08-27

### Feature

You can disable data residency enforcement for in-use and in-transit data in
Model Armor templates. Disabling data residency enforcement
allows cross-jurisdictional routing to enable Model Armor
features that are otherwise unavailable in [limited-support
regions](https://docs.cloud.google.com/model-armor/feature-availability-by-region#limited-support). Data at
rest remains compliant with data residency requirements.

For more information, see [Set data residency
compliance](https://docs.cloud.google.com/model-armor/manage-templates#set-data-residency-compliance) and
[Data residency and endpoints](https://docs.cloud.google.com/model-armor/data-residency).

---
## 2026-08-25

### Feature

Model Armor supports screening prompts and responses up to
65,536 tokens (262,144 characters) for prompt injection and
jailbreak detection, responsible AI, and child sexual abuse material (CSAM)
filters. Model Armor scans only the first 256 URLs found in prompts
and responses.

For more information, see [Token system limits](https://docs.cloud.google.com/model-armor/quotas#token-limits).

---
## 2026-01-30

### Change

The [prompt injection and jailbreak detection](https://docs.cloud.google.com/model-armor/overview#ma-prompt-injection)
filter for the Mumbai (`asia-south1`) and Singapore (`asia-southeast1`) regions
is upgraded to improve detection accuracy and reduce the rate of false positives.

---
## 2025-09-16

### Feature

Model Armor is integrated with Google Agentspace to provide greater insights and enhanced security of your agent interactions by default. For more information, see [Integration with Google Agentspace](https://cloud.google.com/security-command-center/docs/model-armor-agentspace-integration).

---
## 2025-09-15

### Feature

[Model Armor integration with Google Kubernetes Engine](https://cloud.google.com/security-command-center/docs/model-armor-gke-integration) is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-08

### Feature

The Model Armor monitoring dashboard provides a centralized view to track interactions and violations within your projects. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [View the monitoring dashboard](https://cloud.google.com/security-command-center/docs/model-armor-monitoring-dashboard).

---
## 2025-08-04

### Changed

Model Armor supports the `asia-southeast1` location. For information about supported locations, see [Locations for the Model Armor API](https://cloud.google.com/security-command-center/docs/regional-endpoints#locations-model-armor).

---
## 2025-07-29

### Feature

You can use Terraform to manage Model Armor floor settings and templates. This helps reduce manual overhead with Model Armor deployments. For more information, see [Terraform resources for Security Command Center](https://cloud.google.com/security-command-center/docs/terraform#resources).

---
