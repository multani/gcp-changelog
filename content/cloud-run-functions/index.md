# Cloud Run functions

## 2026-10-24

### Security

The following runtime languages contain important security updates:

* [Go 1.24 and later](https://docs.cloud.google.com/functions/docs/runtime-support#go): `1.24.13`, `1.25.14`, `1.26.10`, `1.27.3`
* [Node.js 22 and later](https://docs.cloud.google.com/functions/docs/runtime-support#node.js): `22.23.4`, `24.22.1`, `26.12.1`
* [Java 17 and later](https://docs.cloud.google.com/functions/docs/runtime-support#java): `17.0.20_101`, `21.0.12_101.0.LTS`, `25.0.5_8.0.LTS`
* [PHP 8.2 and later](https://docs.cloud.google.com/functions/docs/runtime-support#php): `8.2.35`, `8.3.36`, `8.4.27`, `8.5.12`
* [Python 3.10 and later](https://docs.cloud.google.com/functions/docs/runtime-support#python): `3.10.22`, `3.11.17`, `3.12.15`, `3.13.15`, `3.14.6`
* [Ruby 3.3 and later](https://docs.cloud.google.com/functions/docs/runtime-support#ruby): `3.3.12`, `3.4.11`, `4.0.7`
* [.NET 6 and later](https://docs.cloud.google.com/functions/docs/runtime-support#.net): `6.0.428`, `8.0.415`, `10.0.100`

The following stacks and their underlying operating system packages have also been updated:

* `google-22`, `google-22-full`
* `google-24`, `google-24-full`

Take immediate protective action by rebuilding and redeploying your resources with updated dependencies.

See [Security bulletins for Google Cloud](https://docs.cloud.google.com/support/bulletins) for more information.

---
## 2026-10-22

### Security

All supported versions of [PHP 8.2](https://docs.cloud.google.com/functions/docs/runtime-support#php) and later are patched. Take immediate protective action by redeploying your resources with updated dependencies.

See [Responding to core PHP vulnerabilities](https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619) for more information.

---
## 2026-10-21

### Security

This note is incorrect; follow guidance in the entry for [October 22, 2026](#October_22_2026).

Patch updates to [supported PHP runtimes](https://docs.cloud.google.com/functions/docs/runtime-support#php) are available with deployments from source: `8.5.12`, `8.4.27`, `8.3.36`, and `8.2.35`. Functions with automatic base image updates enabled have already been patched. If you have disabled automatic base image updates, take immediate action to protect your workloads by redeploying your workloads with updated dependencies and redeploying. See [Responding to core PHP vulnerabilities](https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619) for more information.

---
## 2026-09-01

### Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in
[General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

---
## 2026-08-19

### Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in
[Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

Starting from Go runtime version 1.26 and later, the lifecycle support dates
align more closely with the
[Go community release cycle](https://go.dev/wiki/Go-Release-Cycle). For more
information, see
[Runtime support schedule](https://docs.cloud.google.com/functions/docs/runtime-support#go).

---
## 2026-08-10

### Feature

The [Cloud Run functions upgrade tool](https://docs.cloud.google.com/functions/1stgendocs/migrating/upgrade-gen1-functions) is in [General Availability](https://cloud.google.com/products#product-launch-stages). Use this tool to upgrade 1st gen functions to Cloud Run functions.

---
## 2026-07-27

### Feature

Support for the [Node.js 26 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#node.js) is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-03-17

### Feature

Support for [Ruby 4.0 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#ruby) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2026-03-12

### Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2026-03-03

### Feature

Support for [Ruby 4.0 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#ruby) is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-02-27

### Feature

Support for [PHP 8.5 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#php) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2026-02-24

### Feature

Support for the ability to configure [Direct VPC egress for 2nd gen functions](https://docs.cloud.google.com/functions/docs/running/direct-vpc) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2026-02-19

### Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#go) is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-02-18

### Feature

Support for [.NET 10 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#.net) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2026-02-02

### Feature

Support for [PHP 8.5 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#php) is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-01-27

### Feature

Support for [.NET 10 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#.net) is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-01-06

### Feature

You can now configure [Direct VPC egress for 2nd gen functions](https://docs.cloud.google.com/functions/docs/running/direct-vpc). This support is at the [Preview release level](https://cloud.google.com/products#product-launch-stages).

---
## 2025-12-22

### Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#java) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-12-19

### Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#python) is in [General Availability](https://cloud.google.com/products#product-launch-stages). Starting from Python version 3.14 and later, the Python Buildpack uses the uv package manager as the
default installer for the dependencies you specify in your `requirements.txt` file. You can also use pip as the default installer for these versions by setting the `GOOGLE_PYTHON_PACKAGE_MANAGER` environment variable to `pip`. For more information, see [Specify dependencies in Python](https://docs.cloud.google.com/run/docs/runtimes/python-dependencies.md#dependencies).

---
## 2025-11-20

### Feature

Support for [Node.js 24 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#node.js) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-11-12

### Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#python) is in [Preview](https://cloud.google.com/products#product-launch-stages). Starting from Python version 3.14 and later, the Python Buildpack uses the UV package manager as the
default installer for the dependencies you specify in your `requirements.txt` file. You can also use pip as the default installer for these versions by setting the `GOOGLE_PYTHON_PACKAGE_MANAGER` environment variable to `pip`. For more information, see [Specify dependencies in Python](https://docs.cloud.google.com/run/docs/runtimes/python-dependencies.md#dependencies).

---
## 2025-10-31

### Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#java) is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-07

### Feature

Cloud Run functions (1st gen) supports the [Node.js 22 runtime](https://docs.cloud.google.com/functions/docs/runtime-support#node.js) at the [General Availability release level](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-10-01

### Feature

Cloud Run functions now provides an [upgrade tool](https://docs.cloud.google.com/functions/1stgendocs/migrating/upgrade-gen1-functions) for upgrading 1st gen functions to Cloud Run. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-08-21

### Feature

Support for [Go 1.25 runtime](https://cloud.google.com/functions/docs/concepts/execution-environment#go) is in [General Availability (GA)](https://cloud.google.com/products/?_gl=1*dplot*_ga*MTM2MDk5MzEzMi4xNzQ1ODg0OTY5*_ga_4LYFWVHBEB*MTc0NjE0MTA3Ny4yMi4xLjE3NDYxNDEwOTYuMC4wLjA.#product-launch-stages).

---
## 2025-07-30

### Feature

Support for [Go 1.24 runtime](https://cloud.google.com/functions/docs/concepts/execution-environment#go) is in [General Availability (GA)](https://cloud.google.com/products/?_gl=1*dplot*_ga*MTM2MDk5MzEzMi4xNzQ1ODg0OTY5*_ga_4LYFWVHBEB*MTc0NjE0MTA3Ny4yMi4xLjE3NDYxNDEwOTYuMC4wLjA.#product-launch-stages).

### Feature

Support for [Go 1.25 runtime](https://cloud.google.com/functions/docs/concepts/execution-environment#go) is in [Preview](https://cloud.google.com/products/?_gl=1*dplot*_ga*MTM2MDk5MzEzMi4xNzQ1ODg0OTY5*_ga_4LYFWVHBEB*MTc0NjE0MTA3Ny4yMi4xLjE3NDYxNDEwOTYuMC4wLjA.#product-launch-stages). This runtime is available for early testers using existing [release candidates](https://go.dev/dl/#unstable).

### Feature

Support for [Node.js 24 runtime](https://cloud.google.com/functions/docs/concepts/execution-environment#node.js) is in [Preview](https://cloud.google.com/products/?_gl=1*dplot*_ga*MTM2MDk5MzEzMi4xNzQ1ODg0OTY5*_ga_4LYFWVHBEB*MTc0NjE0MTA3Ny4yMi4xLjE3NDYxNDEwOTYuMC4wLjA.#product-launch-stages). Node.js 24 is in the Current release state and enters long-term support (LTS) in October 2025. For more information, see [Node.js v24.0.0 (Current)](https://nodejs.org/en/blog/release/v24.0.0) in the Node.js website.

---
## 2025-07-15

### Feature

Support for the [Go 1.24 runtime](https://cloud.google.com/functions/docs/concepts/execution-environment#go) is in [Preview](https://cloud.google.com/products/?_gl=1*dplot*_ga*MTM2MDk5MzEzMi4xNzQ1ODg0OTY5*_ga_4LYFWVHBEB*MTc0NjE0MTA3Ny4yMi4xLjE3NDYxNDEwOTYuMC4wLjA.#product-launch-stages).

---
## 2025-06-17

### Feature

Support for the [Ruby 3.4 runtime](https://cloud.google.com/functions/docs/concepts/execution-environment#ruby) is in [General Availability (GA)](https://cloud.google.com/products/?_gl=1*dplot*_ga*MTM2MDk5MzEzMi4xNzQ1ODg0OTY5*_ga_4LYFWVHBEB*MTc0NjE0MTA3Ny4yMi4xLjE3NDYxNDEwOTYuMC4wLjA.#product-launch-stages).

### Feature

Support for the [PHP 8.4 runtime](https://cloud.google.com/functions/docs/concepts/execution-environment#php) is in [General Availability (GA)](https://cloud.google.com/products/?_gl=1*dplot*_ga*MTM2MDk5MzEzMi4xNzQ1ODg0OTY5*_ga_4LYFWVHBEB*MTc0NjE0MTA3Ny4yMi4xLjE3NDYxNDEwOTYuMC4wLjA.#product-launch-stages).

---
## 2025-05-30

### Feature

For Java functions that use `functions-framework` version 1.4.0 or later, you
can now use the logging class `java.util.logging.Logger` to add a [unique execution
ID](https://cloud.google.com/run/docs/runtimes/java#execution_id) to log outputs.

---
