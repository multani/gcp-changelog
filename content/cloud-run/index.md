# Cloud Run

## 2025-09-24

### Feature

Support for setting multiple environment variables using the `.env` file is in General Availability (GA). For more information, see [Configure environment variables for services](https://cloud.google.com/run/docs/configuring/services/environment-variables.md#set_multiple_environment_variables), [jobs](https://cloud.google.com/run/docs/configuring/jobs/environment-variables.md#set_multiple_environment_variables), and [worker pools](https://cloud.google.com/run/docs/configuring/workerpools/environment-variables.md#set_multiple_environment_variables).

---
## 2025-09-23

### Feature

You can specify mount options when you configure Cloud Storage volume mounts for Cloud Run [services](https://cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts), [jobs](https://cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts), and [worker pools](https://cloud.google.com/run/docs/configuring/workerpools/cloud-storage-volume-mounts). (GA)

---
## 2025-09-10

### Feature

You can deploy and configure a [multi-region service](https://cloud.google.com/run/docs/multiple-regions#deploy) from a single gcloud CLI command or by using a YAML or Terraform file (GA).

### Feature

[Cloud Run Threat Detection](https://cloud.google.com/run/docs/securing/cloud-run-threat-detection) is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-03

### Feature

You can [configure GPU](https://cloud.google.com/run/docs/configuring/workerpools/gpu) in your Cloud Run worker pool (Preview).

---
## 2025-08-21

### Feature

Support for [Go 1.25 runtime](https://cloud.google.com/run/docs/runtime-support#go) is in [General Availability (GA)](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages).

---
## 2025-08-20

### Feature

For Cloud Run source deployed services and functions with [GPU enabled](https://cloud.google.com/run/docs/configuring/services/gpu), Cloud Run defaults to using Cloud Build's `e2-highcpu-8` machine type for the build process when you use the `gcloud beta run` command (Preview). This change allows for higher CPU support and faster build times, and also leads to a moderate increase in the overall cost of your service.

---
## 2025-08-14

### Feature

The Python buildpack supports Cloud Run source deployments for modern web frameworks such as [FastAPI](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-fastapi-service.md), [Gradio](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-gradio-service), and [Streamlit](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-streamlit-service).

For Python version 3.13 and later, the Python buildpack sets the default entrypoint for [Cloud Run source deployments](https://cloud.google.com/run/docs/deploying-source-code) based on the web server or framework configuration in your `requirements.txt` file. For more information, see [Build a Python application](https://cloud.google.com/docs/buildpacks/python#entrypoint).

---
## 2025-08-13

### Feature

You can set multiple environment variables using the `.env` file (Preview). For more information, see [Configure environment variables for services](https://cloud.google.com/run/docs/configuring/services/environment-variables.md#set_multiple_environment_variables), [jobs](https://cloud.google.com/run/docs/configuring/jobs/environment-variables.md#set_multiple_environment_variables), and [worker pools](https://cloud.google.com/run/docs/configuring/workerpools/environment-variables.md#set_multiple_environment_variables).

---
## 2025-08-05

### Feature

Support for [manually scaling your Cloud Run service](https://cloud.google.com/run/docs/configuring/services/manual-scaling) is now at General Availability (GA).

---
## 2025-07-30

### Feature

Support for [Go 1.24 runtime](https://cloud.google.com/run/docs/runtime-support#go) is in [General Availability (GA)](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages).

### Feature

Support for [Go 1.25 runtime](https://cloud.google.com/run/docs/runtime-support#go) is in [Preview](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages). This runtime is available for early testers using existing [release candidates](https://go.dev/dl/#unstable).

### Feature

Support for [Node.js 24 runtime](https://cloud.google.com/run/docs/runtime-support#node.js) is in [Preview](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages). Node.js 24 is in the Current release state and enters long-term support (LTS) in October 2025. For more information, see [Node.js v24.0.0 (Current)](https://nodejs.org/en/blog/release/v24.0.0) in the Node.js website.

---
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
