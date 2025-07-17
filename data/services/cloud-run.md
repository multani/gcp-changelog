# Cloud Run

## 2025-07-16

### Feature

You can [disable the built-in `run.app` URL](https://cloud.google.com/run/docs/securing/ingress) of a Cloud Run service to ensure that traffic can only ingress through paths that you've explicitly configured ([GA](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-07-15

### Feature

Compute flexible committed use discounts (CUDs) have expanded to also cover your Cloud Billing account's spend across Cloud Run services with request-based billing and Cloud Run functions.

The [improved spend-based CUD experience](https://cloud.google.com/docs/cuds-multiprice) is available without requiring an opt-in for new users or users who don't have an active spend-based CUD.

To learn more about how opting into the new model affects your flexible CUDs, see [Committed use discounts](https://cloud.google.com/run/cud).

### Feature

Support for the [Go 1.24 runtime](https://cloud.google.com/run/docs/runtime-support#go) is in [Preview](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages).

---
## 2025-06-30

### Feature

You can [apply maximum instance configuration](https://cloud.google.com/run/docs/configuring/max-instances#service-vs-revision-level) at the service level (in Preview).

---
## 2025-06-25

### Feature

Cloud Run [worker pools](https://cloud.google.com/run/docs/deploy-worker-pools) are now available (Preview). Worker pools are specifically designed for non-request workloads.

---
## 2025-06-24

### Feature

A new region is now available for [Cloud Run GPUs](https://cloud.google.com/run/docs/configuring/services/gpu#supported-regions): `us-east4`.

---
## 2025-06-17

### Feature

Support for the [PHP 8.4 runtime](https://cloud.google.com/run/docs/runtime-support#php) is in [General Availability (GA)](https://cloud.google.com/products/?_gl=1*dplot*_ga*MTM2MDk5MzEzMi4xNzQ1ODg0OTY5*_ga_4LYFWVHBEB*MTc0NjE0MTA3Ny4yMi4xLjE3NDYxNDEwOTYuMC4wLjA.#product-launch-stages).

### Feature

Support for the [Ruby 3.4 runtime](https://cloud.google.com/run/docs/runtime-support#ruby) is in [General Availability (GA)](https://cloud.google.com/products/?_gl=1*dplot*_ga*MTM2MDk5MzEzMi4xNzQ1ODg0OTY5*_ga_4LYFWVHBEB*MTc0NjE0MTA3Ny4yMi4xLjE3NDYxNDEwOTYuMC4wLjA.#product-launch-stages).

---
## 2025-06-16

### Feature

You can [configure GPU](https://cloud.google.com/run/docs/configuring/jobs/gpu) in your Cloud Run job (Preview).

---
## 2025-06-09

### Feature

You can [use request host and request path in IAM Conditions](https://cloud.google.com/run/docs/securing/managing-access#conditions) when defining access control for invoking Cloud Run services.

---
## 2025-05-30

### Feature

For Java Cloud Run functions that use `functions-framework` version 1.4.0 or later, you
can now use the logging class `java.util.logging.Logger` to add a [unique execution
ID](https://cloud.google.com/run/docs/runtimes/java#execution_id) to log outputs.

---
## 2025-05-28

### Feature

Multiple regions now benefit from enhanced responsiveness for latency-sensitive applications for [Cloud Run service URLs](https://cloud.google.com/run/docs/triggering/https-request#url).

---
