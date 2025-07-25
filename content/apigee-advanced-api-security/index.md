# Apigee Advanced API Security

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
