# Developer Connect

## 2026-08-14

### Announcement

[Developer Connect insights](https://cloud.google.com/developer-connect/docs/insights) is now [generally available](https://cloud.google.com/products#product-launch-stages).

### Feature

VPC Service Controls support for Developer Connect is
[generally available](https://cloud.google.com/products#product-launch-stages).
For instructions on using this feature, see
[Using VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).

---
## 2026-07-13

### Security

For GitLab Enterprise and Bitbucket Data Center connections, Developer Connect now
checks permissions on the calling principal.

When you create or update repository connections, Developer Connect uses Secret Manager
secrets to authenticate to third-party Git providers. Previously, these
referenced secrets were retrieved by the Developer Connect service agent (P4SA) on your
behalf, checking permissions only against the P4SA's credentials rather than
those of the calling principal. To adhere to the security principle of least
privilege, Developer Connect now checks permissions on both the calling principal
(using end-user credentials) and the P4SA, to ensure both have the
`secretmanager.versions.access` IAM permission on the referenced
secrets.

This check only affects GitLab Enterprise (GLE) and Bitbucket Data Center (BBDC)
connections.

For instructions and more details, see the
[Developer Connect security bulletin](https://cloud.google.com/developer-connect/docs/security-bulletins#gcp-2026-048).

---
## 2026-04-21

### Feature

You can now create an account connector [using a custom OAuth client](https://docs.cloud.google.com/developer-connect/docs/configure-connectors#configure-custom-oauth).

### Feature

You can now use Git proxy with [account connectors](https://docs.cloud.google.com/developer-connect/docs/configure-connectors).

---
## 2026-02-12

### Feature

Developer Connect now supports
[HTTP connections](https://docs.cloud.google.com/developer-connect/docs/http-connections), for access to
arbitrary HTTP endpoints.

---
## 2026-02-06

### Feature

You can now [connect to Secure Source Manager](https://docs.cloud.google.com/developer-connect/docs/connect-secure-source-manager) using Developer Connect.

---
