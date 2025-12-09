# Cloud Run functions

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
