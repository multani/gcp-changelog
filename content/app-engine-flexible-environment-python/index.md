# App Engine flexible environment Python

## 2026-08-20

### Feature

Starting from August 2026, to provide modern security patches and support for MySQL 8.4 and later, the App Engine flexible environment uses Cloud SQL Auth Proxy v2 as the built-in sidecar container for connections to Cloud SQL. To use the latest Cloud SQL Auth Proxy container immediately, restart your VMs or deploy a new version of your application.

---
## 2026-08-14

### Feature

To improve security, starting in August 2026, App Engine opts your application into TLS version 1.2 and later. You can opt out until the end of August 2026. Starting in September 2026, App Engine might permanently block insecure traffic with TLS version 1.1 and earlier. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls).

---
## 2026-06-29

### Feature

Support for deploying your existing apps in the flexible environment to Cloud Run using
the `gcloud beta app migrate-to-run` command is in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Deploy an App Engine app in the flexible environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-flexible-to-run).

---
## 2025-12-19

### Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime) is in [General Availability](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-11-12

### Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-08-07

### Feature

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://cloud.google.com/appengine/docs/flexible/secure-minimum-tls) in the App Engine flexible environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

---
