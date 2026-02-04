# Apigee Advanced API Security

## 2026-02-03

### Feature

**Support for configuring two condition types within a single security action**

Announcing the availability of support for two condition types
in a single security action. For example, you can include both IP addresses and
ASN numbers in the same security action.

This feature is available in Apigee and Apigee hybrid 1.16.0 and later.

**Note:** This feature is available when configuring the security action
via the API, not the UI, at this time.

For usage information, see [Configure multiple condition types](https://docs.cloud.google.com/apigee/docs/api-security/security-actions-api#configure-multiple-condition-types) in the documentation.

### Announcement

On February 3, 2026 we released an updated version of Advanced API Security
security actions

---
## 2026-01-12

### Announcement

On January 12, 2026 we released an updated version of Advanced API Security Abuse Detection

### Feature

**Introduction of Terraform support for managing Advanced API Security abuse detection exclusion lists**

You can now use Terraform to manage Advanced API Security abuse detection
exclusion lists. The feedback feature allows you to specify CIDR ranges and IP
addresses to exclude from future incident reports, and is used to exclude
traffic known to be safe, such as requests related to automated testing.

**Note:** Exclusion lists are not available for VPC-SC customers at this time.

For usage information, see
[Exclude traffic from abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#exclude-traffic-from-abuse-detection)
and [Use Terraform in Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/terraform-overview)
in the Apigee documentation and the
[Terraform abuse detection feedback (exclusion lists) instructions](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_feedback).

---
## 2025-12-17

### Feature

**General availability of Risk Assessment v2 and support for assessments using additional policies**

Announcing the
[general availability](https://cloud.google.com/products#product-launch-stages)
of Risk Assessment v2 and support for assessments using the VerifyIAM policy and
these three AI policies: SanitizeUserPrompt, SanitizeModelResponse, and
SemanticCacheLookup.

**Note:** The Risk Assessment v2 monitoring conditions feature remains in preview.

For usage information, see [Risk Assessment overview and UI](https://docs.cloud.google.com/apigee/docs/api-security/security-scores) in the documentation.

### Announcement

On December 17, 2025 we released an updated version of Advanced API Security
Risk Assessment

**Note:** Rollouts of this release to production instances will begin within two
business days and may take four or more business days to complete across all
Google Cloud zones. Your instances may not have the feature available until the
rollout is complete.

### Feature

**New risk assessment type field when creating or updating a risk assessment version 2 custom security profile**

The API for creating and updating a version 2 risk assessment custom security
profile now includes a `risk_assessment_type` field to specify
whether the custom security profile applies to an Apigee/Apigee hybrid instance
or to API hub multi-gateway.

This field is optional and defaults to `APIGEE`; this is not a
breaking change for existing risk assessment users.

See [REST Resource: organizations.securityProfilesV2](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2) for information on the new functionality.

---
## 2025-10-02

### Announcement

On October 2, 2025 we released an updated version of Advanced API Security Abuse Detection

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

### Feature

**Introduction of exclusion lists for Abuse Detection and incidents**

You can now specify CIDR ranges and IP addresses to exclude from future incident reports. Use this feature to exclude traffic known to be safe, such as requests related to automated testing.

The new functionality includes the ability to create and manage multiple "exclusion lists" which define traffic to exclude and the reasons it is excluded.

**Note:** Exclusion lists are not available for VPC-SC customers at this time.

For usage information, see [Exclude traffic from abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#exclude-traffic-from-abuse-detection) in the documentation.

---
## 2025-09-19

### Announcement

On September 19, 2025 we released an updated version of Advanced API Security

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

### Feature

**New security actions status icons and "expired" note in the security actions UI**

This release adds security status icons to the Apigee UI to make it easier to see, at a glance, whether a security action is enabled, disabled, or paused, and an "expired" note when an action is expired.

The status icons display next to the action's status in the security actions list and in the security action details page.

For information on security actions and security action statuses, see the [Security Actions customer documentation](https://cloud.google.com/apigee/docs/api-security/security-actions).

---
## 2025-09-18

### Announcement

On September 18, 2025 we released an updated version of Advanced API Security

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

### Feature

**Improvements to the Abuse Detection incident model**

This release includes improvements to the incident model, including lower noise and higher accuracy for abuse detection incidents.

**Note: This feature is not currently available to customers with VPC-SC enabled.**

For information on abuse detection incidents, see the [Abuse Detection customer documentation](https://cloud.google.com/apigee/docs/api-security/abuse-detection#incidents).

---
## 2025-08-25

### Announcement

On August 25, 2025 we released an updated version of Advanced API Security

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

### Feature

**Additional details and explanations for incidents and traffic identified as anomalous in Abuse Detection Advanced Anomaly Detection**

Starting with this release, additional details are available for anomalies detected in incidents and detected traffic, including details on why traffic was flagged as anomalous, the days and times it triggered, time series charts showing anomalous traffic spikes, and direct links to the Google Cloud Logging for events.

See the [Abuse detection "Details view"](https://cloud.google.com/apigee/docs/api-security/abuse-detection#details-view) for more information.

---
## 2025-08-11

### Announcement

On August 11, 2025 we released an updated version of Advanced API Security Abuse Detection

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

### Feature

**Improved performance when viewing IP address-specific details for abuse detection incidents**

With this release, the IP address detail information for abuse incidents displays more quickly for IP addresses with high traffic volumes, potentially reducing load times from minutes to seconds.

For usage information, see the [Abuse Detection incident detail documentation](https://cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details).

---
## 2025-08-06

### Announcement

On August 6, 2025 we released an updated version of Advanced API Security

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

### Feature

**Availability of Shadow API Discovery for APIs in any Google Cloud project**

Using Shadow API Discovery, you can find undocumented/shadow APIs in your existing cloud infrastructure. Shadow APIs pose a security risk to your system, since they might be unsecured, unmonitored, and unmaintained.

With this release, you can configure and run API observation jobs in any Google Cloud project, without needing to provision Apigee in that project. You can also centrally view the results of API observation jobs and compare discovered API endpoints and operations to APIs cataloged in API hub to identify shadow APIs.

See the [Shadow API Discovery overview](https://cloud.google.com/apigee/docs/api-observation/shadow-api-discovery) for information on Shadow API Discovery and how to add it to projects.

**Note:** Data residency is not currently supported for Shadow API Discovery. See [data residency compatibility](https://cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#data-residency-compatibility).

---
## 2025-08-04

### Announcement

On August 4, 2025 we announced new functionality in Advanced API Security Abuse Detection.

### Feature

**Terraform support for configuring Advanced API Security**

We have expanded our Terraform support for Advanced API Security, enabling you to automate the management of your security posture. You can now use Terraform to manage add-on enablement for [Subscription](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_addons_config) and [PAYG](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_environment_addons_config) environments, create [Risk Assessment security profiles](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_profile_v2) and [monitoring conditions](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_monitoring_condition), [configure IP address resolution](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_environment#client_ip_resolution_config-1), and [create security actions](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_security_action).

For information, see [Configure Advanced API Security using Terraform](https://cloud.google.com/apigee/docs/api-security/enable-security#configure-advanced-api-security-using-terraform).

---
## 2025-07-14

### Announcement

On July 14, 2025 we released an updated version of Advanced API Security

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

### Feature

**Support for editing and deleting security actions**

With this release you can edit and delete existing security actions using either the UI or the Apigee Management APIs.

For usage information, see the [security actions documentation](https://cloud.google.com/apigee/docs/api-security/security-actions).

---
## 2025-07-01

### Announcement

On July 1, 2025 we released a new version of Advanced API Security Abuse Detection.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

### Feature

**Support for AppGroups in Abuse Detection attributes**

Abuse Detection incidents and detected traffic now show information on AppGroups and AppGroup apps when the AppGroup is part of the request or traffic.

**Note:** This functionality is not available in Apigee hybrid at this time.

For usage information, see the [Abuse Detection documentation](https://cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details).

---
## 2025-06-16

### Announcement

On June 16, 2025 we released a new version of Advanced API Security Abuse Detection.

### Feature

**API address drill down details are now available in the preview release of Advanced API Security Abuse Detection incidents in the detected traffic tab.**

This new functionality shows details related to specific API addresses when viewing detected abuse in detected traffic.

For usage information, see the [Abuse Detection customer documentation](https://cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details) for incident details.

---
## 2025-06-04

### Announcement

On June 4, 2025 we released an update to the Anomaly Detection model in Advanced API Security Abuse Detection.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

### Feature

**New model for Abuse Detection's Advanced Anomaly Detection rule**

With this release, we introduced a new and improved machine learning model for anomaly detection in Advanced API Security. This new model includes the following improvements:

* **Trained on customer-specific traffic patterns.** The new model is trained exclusively on your organization's historical API traffic data. It continues to learn from your API traffic patterns over time to increase accuracy.
* **Engineered by Google for anomaly detection.** The new model is a custom Vertex AI-based machine learning model, engineered and also used internally by Google specifically to detect anomalies in traffic patterns.

Usage requirements:

* In order to use this new model, you must explicitly opt in to allow the model to use your traffic and other data to train for anomaly detection. Note that your data is never shared with other customers for training purposes.
* The new model is not available for VPC-SC customers at this time.

The new anomaly detection model replaces the old model, with no customer-facing changes to the API or UI. Upon opting in for model training, you can expect to start seeing detected anomalies within 6 hours. If you have already opted in to allow the older version of our anomaly detection model to use your traffic data for training, you will not need to opt in again.

For more information on this model and on Abuse Detection, see [Abuse Detection customer documentation](https://cloud.google.com/apigee/docs/api-security/abuse-detection), including [Detection rules](https://cloud.google.com/apigee/docs/api-security/detection-rules).

---
## 2025-05-27

### Announcement

On May 27, 2025 we released an updated version of Apigee Advanced API Security.

### Feature

With this release, Advanced API Security expands its runtime region support to include `africa-south1` (Johannesburg).

For a list of supported regions, see [Apigee locations](https://cloud.google.com/apigee/docs/locations).

---
