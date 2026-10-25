# App Engine flexible environment Java

## 2026-10-24

### Security

The following runtime language contains important security updates:

* [Java 17 and later](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#java): `17.0.20_101`, `21.0.12_101.0.LTS`, `25.0.5_8.0.LTS`

The following stacks and their underlying operating system packages have also been updated:

* `google-22`, `google-22-full`
* `google-24`, `google-24-full`

Take immediate protective action by rebuilding and redeploying your resources with updated dependencies.

See [Security bulletins for Google Cloud](https://docs.cloud.google.com/support/bulletins) for more information.

---
## 2026-09-29

### Feature

App Engine permanently blocks insecure traffic with TLS version 1.1 and earlier.
For `appspot.com` domains, this block occurs at the connection level. For custom
domains, the connection might succeed, but the requests are blocked. For more
information, see
[Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls).

---
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
## 2025-12-22

### Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/appengine/docs/flexible/java/runtime) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-31

### Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/appengine/docs/flexible/java/runtime) is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-08-07

### Feature

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://cloud.google.com/appengine/docs/flexible/secure-minimum-tls) in the App Engine flexible environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

---
