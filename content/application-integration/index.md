# Application Integration

## 2026-08-28

### Announcement

**Upcoming authorization changes for integration runs**

Application Integration is updating how identities are handled for integration runs. Every run will act as either the person who triggered it or a run-as service account that you configure, and running an integration will require permission to act as that service account. Integrations that run without a person, such as those started by a schedule or an event, will need an explicitly configured run-as service account.

Action might be required before the change takes effect. For guidance on identifying affected integrations and updating them, see [Prepare for upcoming authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes).

---
## 2026-08-21

### Security

**Missing authorization in QueryEngineTask (CVE-2026-12710)**

A missing authorization vulnerability ([CVE-2026-12710](https://nvd.nist.gov/vuln/detail/CVE-2026-12710)) in `QueryEngineTask` in [Application Integration](https://docs.cloud.google.com/application-integration/docs) was patched on April 4, 2026, and no customer action is needed.

---
## 2026-06-25

### Security

**Security bulletins page**

See the new security bulletins page for Application Integration. Use it to stay informed about related security updates, vulnerabilities, and remediations. For more information, see [Security bulletins](https://docs.cloud.google.com/application-integration/docs/security-bulletins).

---
## 2026-02-02

### Feature

**FIFO message processing with Pub/Sub ordering keys**

Application Integration now supports publishing messages to Google Cloud Pub/Sub topics using ordering keys, enabling First-In, First-Out (FIFO) message processing. By setting an ordering key in the Pub/Sub trigger's `Publish Message` action, you can ensure messages are received in the correct order, enhancing reliability for integrations requiring ordered message processing. For more information on how to use ordering keys to publish messages, see [Using ordering keys](https://cloud.google.com/pubsub/docs/publisher#using-ordering-keys).

---
## 2025-10-31

### Feature

**Troubleshoot failed execution logs using AI**

You can now use AI-powered troubleshooting with Google Gemini to analyze failed execution logs, identify root causes, and receive precise, actionable steps to resolve errors. To use this feature, you must enable AI capabilities in your Google Cloud region. For more information, see  [Troubleshoot failed execution logs using AI](https://cloud.google.com/application-integration/docs/troubleshoot-execution-logs-using-AI).

---
## 2025-10-10

### Feature

**Manage Application Integration resources using custom constraints**

You can now use custom constraints with Organization Policy to provide more granular control over specific fields for some Application Integration resources. For more information, see [Manage Application Integration resources using custom constraints](https://cloud.google.com/application-integration/docs/custom-constraints). This feature is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-16

### Changed

**Salesforce connected app requires installation for OAuth 2.0 authentication**

A new security requirement from Salesforce restricts the use of uninstalled connected apps. To ensure your Salesforce triggers remain functional, you must install the [connected app](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_create.htm&type=5) in your Salesforce account.

When establishing a new Salesforce trigger using OAuth 2.0 authentication, you are now required to install the connected app within your Salesforce account. This step is also necessary for existing triggers using OAuth 2.0 authentication if the connected app is not already installed, as failure to do so may cause them to stop working.

For more information, see [Install the OAuth 2.0 connected app](https://cloud.google.com/application-integration/docs/configure-salesforce-trigger#post-setup).

---
## 2025-09-10

### Changed

**Connected app requires installation for OAuth 2.0 authentication in Salesforce trigger**

To configure a Salesforce trigger that uses OAuth 2.0 authentication, you must install the relevant [connected app](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_create.htm&type=5) in your Salesforce account.

For more information, see [Install the OAuth connected app](https://cloud.google.com/application-integration/docs/configure-salesforce-trigger#post-setup).

---
## 2025-08-18

### Changed

**Standard canvas view**

The integration editor now features a single, standard [canvas view](https://cloud.google.com/application-integration/docs/canvas-view). The legacy canvas is no longer available.

---
