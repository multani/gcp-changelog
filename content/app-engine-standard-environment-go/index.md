# App Engine standard environment Go

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
