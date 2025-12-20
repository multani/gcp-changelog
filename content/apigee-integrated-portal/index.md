# Apigee Integrated Portal

## 2025-12-17

### Announcement

On December 17, 2025 we released a new version of the Apigee integrated portal.

### Fixed

**Incorrect Cross-Origin-Opener-Policy header in developer portal**

A fix has been implemented to address an issue where the
`Cross-Origin-Opener-Policy` response header in the developer portal was
malformed with an extra colon. This change ensures the security header is
correctly formatted.

---
## 2025-09-08

### Announcement

On September 8, 2025 we released a new version of the Apigee integrated portal.

### Feature

Workforce Identity Federation users can now manage Integrated Portals using the Apigee Cloud console. This previous limitation has been removed from [Accessing features only available in the Classic Apigee UI](https://cloud.google.com/apigee/docs/api-platform/system-administration/workforce-identity-federation-apigee#accessing-features-only-available-in-the-classic-apigee-ui).

---
## 2025-08-25

### Announcement

On August 25, 2025 we released a new version of the Apigee integrated portal.

This release includes general improvements to performance and availability.

---
## 2025-07-24

### Announcement

On July 24, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

* Publish > Portals

See [Apigee UI in Cloud console navigation](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

---
## 2025-06-23

### Announcement

On June 23, 2025 we released a new version of the Apigee integrated portal.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

### Feature

This release adds the **Export** feature to the Apigee UI in the Cloud console. You can now export publishing data for developers, apps, or API products as a comma-separated values (CSV) file or JSON file.

**Documentation:** [Exporting publishing data](https://cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product#export)

---
## 2025-06-02

### Announcement

On June 2, 2025 we released a new version of the Apigee integrated portal.

### Fixed

| Bug ID | Description |
| --- | --- |
| 404509044 | When [configuring an SMTP server,](https://cloud.google.com/apigee/docs/api-platform/publish/portal/configure-email#cloud-console-ui-preview) and the portal is first provisioned, email notifications are sent to portal users from a generic sender address. This release updates that generic address to `noreply-apigee-portals@google.com`. |

This approach is suitable for evaluation, but you should configure your own SMTP server before launching your portal to users. When you configure the SMTP server, you can also configure the sender address, for example, `no-reply@mycompany.com`.

---
## 2025-05-29

### Announcement

On May 29, 2025 we released a new version of the Apigee integrated portal.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Feature

**GA: Apigee Integrated Developer Portal Admin UI in the Google Cloud console.**

This release adds the Apigee Integrated Developer Portal Admin UI from the Classic Apigee UI into the Google Cloud console.

Leveraging Google Cloud console components provides API providers and Portal Admins with a centralized platform to efficiently configure, publish, and manage your API consumer portals, eliminating the need to switch between different UIs.

No new APIs have been introduced in this release.

See [Publishing overview](https://cloud.google.com/apigee/docs/api-platform/publish/publishing-overview) to get started.

---
