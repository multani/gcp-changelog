# Application Integration

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
