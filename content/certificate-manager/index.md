# Certificate Manager

## 2026-10-14

### Change

Google-managed public SSL certificates signed by [Google Public
CA](https://docs.cloud.google.com/certificate-manager/docs/public-ca) (pki.goog) are gradually transitioning from a
90-day validity period to a 45-day validity period to improve security.

To align with modern industry-wide security standards and promote shorter
certificate lifespans, Google-managed public certificates now rotate more
frequently. This proactive rotation enhances the overall security posture of
load balancers. The transition requires no manual intervention or configuration
changes as Certificate Manager automatically manages both issuance and renewal.

For more information, see [Google-managed
certificates](https://docs.cloud.google.com/certificate-manager/docs/core-components#google-managed-certificates)
and [Use Google-managed
certificates](https://docs.cloud.google.com/certificate-manager/docs/certificate-manager-best-practices#use_google_managed_certificates).

---
## 2026-09-24

### Feature

You can now attach tags to Certificate Manager resources during creation. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Create and manage tags for Certificate Manager resources](https://docs.cloud.google.com/certificate-manager/docs/create-manage-tags).

---
## 2026-05-19

### Feature

Certificate Manager (2nd gen) is available in [Preview](https://cloud.google.com/products#product-launch-stages). Certificate Manager (2nd gen) offers a unified control plane to observe, manage, and automate certificates across your organization.

For more information, see [Certificate Manager (2nd gen) overview](https://docs.cloud.google.com/certificate-manager/docs/v2/overview).

---
