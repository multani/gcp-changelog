# Apigee Advanced API Security

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
