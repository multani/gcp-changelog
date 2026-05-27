# App Engine standard environment Go

## 2026-05-27

### Feature

Enable only needed legacy bundled services using the [`app_engine_bundled_services`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=go#app_engine_bundled_services) field for improved security and maintainability of your applications ([Preview](https://cloud.google.com/products/#product-launch-stages)).

---
## 2026-05-21

### Feature

The App Engine Migration hub lets you migrate services in the App Engine standard environment to Cloud Run, and also provides cost-saving recommendations. For more information, see [Deploy an App Engine app in the standard environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-to-run) ([Preview](https://cloud.google.com/products?e=48754805#product-launch-stages)).

---
## 2026-03-12

### Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2026-02-19

### Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2026-02-12

### Feature

Support for deploying your existing apps in the standard environment to Cloud Run using
the `gcloud beta app migrate-to-run` command is in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Deploy an App Engine app in the standard environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-to-run).

---
## 2026-01-31

### Deprecated

Go 1.11 is [deprecated](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#deprecated).
You won't be able to deploy Go 1.11 applications, even if your organization
previously used an organization policy to re-enable deployments of legacy
runtimes. Your existing Go 1.11 applications will continue to run and receive
traffic. We recommend that you [migrate to the latest supported version of
Go](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/go-differences).

---
## 2025-08-21

### Feature

Support for [Go 1.25 runtime](https://cloud.google.com/appengine/docs/standard/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-08-07

### Feature

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://cloud.google.com/appengine/docs/standard/secure-minimum-tls) in the App Engine standard environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

---
## 2025-07-30

### Feature

Support for [Go 1.24 runtime](https://cloud.google.com/appengine/docs/standard/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

### Feature

Support for [Go 1.25 runtime](https://cloud.google.com/appengine/docs/standard/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages). This runtime is available for early testers using existing [release candidates](https://go.dev/dl/#unstable).

---
## 2025-07-15

### Feature

Support for [Go 1.24 runtime](https://cloud.google.com/appengine/docs/standard/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
