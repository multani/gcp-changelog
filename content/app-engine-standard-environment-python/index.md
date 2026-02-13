# App Engine standard environment Python

## 2026-02-12

### Feature

Support for deploying your existing apps in the standard environment to Cloud Run using
the `gcloud beta app migrate-to-run` command is in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Deploy an App Engine app in the standard environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-gcloud).

---
## 2026-01-31

### Deprecated

Python 2.7 is [deprecated](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#deprecated).
You won't be able to deploy Python 2.7 applications, even if your
organization previously used an organization policy to re-enable
deployments of legacy runtimes. Your existing Python 2.7 applications
will continue to run and receive traffic. We recommend that you
[migrate to the latest supported version of Python](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/python-differences).

---
## 2025-12-19

### Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime) is in [General Availability](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-11-12

### Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-10-31

### Feature

To improve email security and ensure reliable, high-volume email delivery,
[migrate from the legacy Mail API to an SMTP-based email service](https://docs.cloud.google.com/appengine/migration-center/standard/python/mail-to-smtp), such as SendGrid, Mailgun, or Mailjet (Preview).

---
## 2025-08-07

### Feature

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://cloud.google.com/appengine/docs/standard/secure-minimum-tls) in the App Engine standard environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

---
## 2025-06-30

### Feature

For new deployments, the [URL Fetch API](https://cloud.google.com//appengine/docs/standard/services/urlfetch/issue-requests.md) validates the certificate of the host it contacts by default.

---
