# App Engine flexible environment Go

## 2026-08-20

### Feature

Starting from August 2026, to provide modern security patches and support for MySQL 8.4 and later, the App Engine flexible environment uses Cloud SQL Auth Proxy v2 as the built-in sidecar container for connections to Cloud SQL. To use the latest Cloud SQL Auth Proxy container immediately, restart your VMs or deploy a new version of your application.

---
## 2026-08-19

### Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in
[Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

Starting from Go runtime version 1.26 and later, the lifecycle support dates
align more closely with the
[Go community release cycle](https://go.dev/wiki/Go-Release-Cycle). For more
information, see
[Runtime support schedule](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go).

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
## 2026-03-12

### Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2026-02-19

### Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-10-20

### Feature

[Support for TLS version 1.2 and later](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls),
along with a corresponding secure set of cipher suites, is in General Availability (GA).

---
## 2025-08-21

### Feature

Support for [Go 1.25 runtime](https://cloud.google.com/appengine/docs/flexible/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-08-07

### Feature

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://cloud.google.com/appengine/docs/flexible/secure-minimum-tls) in the App Engine flexible environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

---
## 2025-07-30

### Feature

Support for [Go 1.24 runtime](https://cloud.google.com/appengine/docs/flexible/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

### Feature

Support for [Go 1.25 runtime](https://cloud.google.com/appengine/docs/flexible/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages). This runtime is available for early testers using existing [release candidates](https://go.dev/dl/#unstable).

---
## 2025-07-15

### Feature

Support for [Go 1.24 runtime](https://cloud.google.com/appengine/docs/flexible/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
