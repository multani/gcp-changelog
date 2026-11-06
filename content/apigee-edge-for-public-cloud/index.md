# Apigee Edge for Public Cloud

## 2026-11-05

### Announcement

**Scheduled maintenance of Management/Control Plane for the Apigee Edge for Public Cloud on November 6, 2026.**

Scheduled maintenance of Management/Control Plane for the Apigee Edge for Public Cloud production will take place on Friday, November 6, 2026, from 9:00 PM PT to
10:00 PM PT (Saturday, November 7, 2026, from 5:00 AM UTC to 6:00 AM UTC). This
maintenance follows the monthly maintenance window schedule documented in the
[Apigee Edge release notes archive](https://docs.apigee.com/release/notes/apigee-release-notes).

During the scheduled maintenance window, the following services will be
temporarily unavailable, and attempts to access them will return a `4xx` status
code:

* Management Services UI
* Management Services APIs
* Monetization Management APIs
* New proxy deployments
* DevPortal Service
* Microgateway Services
* Edge Query (Analytics Stats APIs)

Runtime API calls to deployed API proxies are unaffected. While access to
analytics queries may be temporarily unavailable during the maintenance window, all
analytics and metrics data from this period will be available once maintenance
ends.

---
## 2026-10-15

### Announcement

On October 15, 2026, we began releasing Single Sign-On (SSO) updates for Apigee
Edge for Public Cloud.

### Fixed

| Bug ID | Component | Description |
| --- | --- | --- |
| **560310696** | SSO | Fixed an issue where the Portal SSO endpoint inadvertently accepted deprecated TLS 1.1 connections. The endpoint now strictly enforces TLS 1.2+. |

---
## 2026-10-05

### Security

**Security fixes for the integrated portal and API specs in the Apigee Edge
management UIs.**

The Apigee Edge UIs for managing integrated portals and API specs were updated
to patch vulnerabilities in underlying libraries and serving components.
Functionality is unchanged, but some pages might show minor styling differences.

---
## 2026-09-02

### Announcement

Apigee Edge for Public Cloud release notes are now published on Google Cloud
documentation.

Release notes for Apigee Edge for Public Cloud, including its Edge UI, SSO,
Message Processor, and integrated portal components, are published on the
[Apigee Edge for Public Cloud release notes](https://docs.cloud.google.com/apigee/docs/edge-public-cloud/release-notes)
page from September 2026 onward. You can
[subscribe](https://docs.cloud.google.com/apigee/docs/edge-public-cloud/release-notes#sub) to that page with
a feed reader to be notified when a new release is published.

Release notes published before September 2026 remain available in the
[Apigee Edge release notes archive](https://docs.apigee.com/release/notes/apigee-release-notes).

---
