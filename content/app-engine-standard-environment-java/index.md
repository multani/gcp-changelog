# App Engine standard environment Java

## 2025-10-31

### Feature

To improve email security and ensure reliable, high-volume email delivery,
[migrate from the legacy Mail API to an SMTP-based email service](https://docs.cloud.google.com/appengine/migration-center/standard/java/mail-to-smtp), such as SendGrid, Mailgun, or Mailjet (Preview).

---
## 2025-08-07

### Feature

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://cloud.google.com/appengine/docs/standard/secure-minimum-tls) in the App Engine standard environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

---
## 2025-06-30

### Feature

For new deployments, the [URL Fetch API](https://cloud.google.com//appengine/docs/standard/services/urlfetch/issue-requests.md) validates the certificate of the host it contacts by default.

---
