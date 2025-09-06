# Gemini on GDC API on GDC connected

## 2025-09-03

### Announcement

This is the Public Preview release of Gemini on Google Distributed Cloud connected API.

### Issue

This release of Gemini on GDC connected API contains the following known issues:

* **Servo metrics not captured by Cloud Monitoring.** Servo metrics for Gemini on GDC connected API are not captured by Cloud Monitoring. Other supported metrics are captured as expected.
* **User identity is not supported.** To successfully deploy a Gemini on GDC connected API endpoint, you must use a service account to generate the access credentials.
* **Service account keys expire after 14 days.** If you use a service account key older than 14 days, you can't use it to generate endpoint access credentials. In such situations, you must generate a fresh service account key.
* **Disabling Cloud projects or Cloud services is not supported.** To disable a Cloud project or a Cloud service on your Gemini on GDC connected API deployment, contact your Google representative.
* **Model deployment might intermittently fail**. If you encounter a model deployment failure, contact your Google representative to resolve this issue.

---
