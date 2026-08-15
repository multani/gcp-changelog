# App Engine standard environment Java

## 2026-08-14

### Feature

To improve security, starting in August 2026, App Engine opts your application into TLS version 1.2 and later. You can opt out until the end of August 2026. Starting in September 2026, App Engine might permanently block insecure traffic with TLS version 1.1 and earlier. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls).

---
## 2026-07-29

### Feature

Support for enabling only needed legacy bundled services using the
[`app_engine_bundled_services`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#app_engine_apis)
field is in [General Availability](https://cloud.google.com/products/#product-launch-stages).

---
## 2026-07-07

### Feature

To modernize image processing, [migrate from the App Engine Images service to
Cloud Run](https://docs.cloud.google.com/appengine/migration-center/standard/java/images-to-cloud-run) by
routing calls to a Cloud Run image transformation service while your app
continues to run on App Engine (Preview).

---
## 2026-06-03

### Feature

App Engine supports [Direct VPC egress](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc) in [Preview](https://cloud.google.com/products#product-launch-stages). Direct VPC egress lets your workloads access VPC network resources as a simpler, more cost-effective [alternative to Serverless VPC Access connectors](https://docs.cloud.google.com/appengine/docs/standard/compare-direct-vpc-egress-connectors).

---
## 2026-05-27

### Feature

Enable only needed legacy bundled services using the [`app_engine_bundled_services`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#app_engine_apis) field for improved security and maintainability of your applications ([Preview](https://cloud.google.com/products/#product-launch-stages)).

---
## 2026-05-21

### Feature

The App Engine Migration hub lets you migrate services in the App Engine standard environment to Cloud Run, and also provides cost-saving recommendations. For more information, see [Deploy an App Engine app in the standard environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-to-run) ([Preview](https://cloud.google.com/products?e=48754805#product-launch-stages)).

---
## 2026-03-02

### Feature

Support for [migrating from the legacy Mail API to an SMTP-based email service](https://docs.cloud.google.com/appengine/migration-center/standard/java/mail-to-smtp), such as SendGrid, Mailgun, or Mailjet is in [General Availability](https://cloud.google.com/products/#product-launch-stages).

---
## 2026-02-12

### Feature

Support for deploying your existing apps in the standard environment to Cloud Run using
the `gcloud beta app migrate-to-run` command is in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Deploy an App Engine app in the standard environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-standard-to-run).

---
## 2026-01-31

### Deprecated

Java 8 is [deprecated](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#deprecated).
You won't be able to deploy Java 8 applications, even if your organization
previously used an organization policy to re-enable deployments of legacy
runtimes. Your existing Java 8 applications will continue to run and receive
traffic. We recommend that you [migrate to the latest supported version of
Java](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/java-differences).

---
## 2025-12-22

### Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-31

### Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime) is in [Preview](https://cloud.google.com/products#product-launch-stages).

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
