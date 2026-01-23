# Cloud Run

## 2026-01-22

### Feature

The Python buildpack supports default entrypoint detection for the [Agent Development Kit (ADK) framework](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-adk-service) in [General Availability](https://cloud.google.com/products#product-launch-stages). For more information, see [Build a Python application](https://docs.cloud.google.com/docs/buildpacks/python#entrypoint).

---
## 2026-01-20

### Feature

The following new region is now available: `asia-southeast3`.

---
## 2026-01-13

### Feature

Cloud Run and Cloud Run functions source deployments support the `pyproject.toml`
file for managing dependencies. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages) for all
[supported Python versions](https://docs.cloud.google.com/run/docs/runtime-support#python).
For more information, see [Deploy Python applications with a `pyproject.toml`
file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml).

---
## 2025-12-22

### Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/run/docs/runtime-support#java) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

---
## 2025-12-19

### Feature

The Python buildpack supports default entrypoint detection for the [Agent Development Kit (ADK) framework](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-adk-service) (Preview). For more information, see [Build a Python application](https://docs.cloud.google.com/docs/buildpacks/python#entrypoint).

### Feature

Cloud Run and Cloud Run functions source deployments support `pyproject.toml`
file for managing dependencies. This feature is in General Availability for Python version 3.13 and later, and is in Preview for Python version 3.12 and earlier.
For more information, see [Deploy Python applications with a `pyproject.toml`
file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml).

### Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/run/docs/runtime-support#python) is in [General Availability](https://cloud.google.com/products?e=48754805#product-launch-stages). Starting from Python version 3.14 and later, the Python buildpack uses the uv package manager as the
default installer for the dependencies you specify in your `requirements.txt` file. You can also use pip as the default installer for these versions by setting the `GOOGLE_PYTHON_PACKAGE_MANAGER` environment variable to `pip`. For more information, see [Specify dependencies in Python](https://docs.cloud.google.com/run/docs/runtimes/python-dependencies.md#dependencies).

---
## 2025-12-18

### Feature

Support for [osonly24 runtime](https://docs.cloud.google.com/run/docs/runtime-support#osonly) is in [Preview](https://cloud.google.com/products?e=48754805#product-launch-stages). The OS only runtime lets you deploy Go applications from source, and binaries such as Dart and Go. For more information, see [Configure the OS only runtime](https://docs.cloud.google.com/docs/buildpacks/osonly).

---
## 2025-12-01

### Feature

You can use
[Developer Connect in the Cloud Run console](https://docs.cloud.google.com/run/docs/continuous-deployment)
to set up continuous deployments from GitHub, GitLab, and Bitbucket
repositories (Preview).

---
## 2025-11-21

### Feature

[Configure HTTP and gRPC readiness probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#readiness-probes)
for your Cloud Run services (Preview).

### Feature

Deploy a highly available, multi-region Cloud Run service with automated
failover and failback for internal traffic using [Cloud Run service health](https://docs.cloud.google.com/run/docs/multiple-regions#service-health)
(Preview).

---
## 2025-11-20

### Feature

Support for [Node.js 24 runtime](https://docs.cloud.google.com/run/docs/runtime-support#node.js) is in [General Availability](https://cloud.google.com/products?e=48754805#product-launch-stages).

---
## 2025-11-19

### Feature

You can [deploy source artifacts directly to
Cloud Run](https://docs.cloud.google.com/run/docs/deploying-source-code#deploy_from_source_without_build),
bypassing the Cloud Build step. (Preview)

---
## 2025-11-17

### Feature

The time it takes for initial deployments to Cloud Run in a new project has been reduced.
This change results in reduced latency and a faster getting started experience.

### Feature

Cloud Run and Cloud Run functions source deployments support `pyproject.toml`
file for managing dependencies. If you use a `pyproject.toml` file, source deployments
use one of the following to find and install dependencies:

* `pip`
* `uv`
* `poetry`

For more information, see [Deploy Python applications with a `pyproject.toml`
file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml) (Preview).

---
## 2025-11-13

### Feature

You can deploy services to Cloud Run [using a Compose file](https://docs.cloud.google.com/run/docs/deploy-run-compose)
(Preview).

---
## 2025-11-12

### Feature

Cloud Run [source deployment](https://docs.cloud.google.com/run/docs/deploying-source-code) supports Ubuntu 24
LTS base images (Preview). This builder is available under
`gcr.io/buildpacks/builder:google-24`. For more information, see
[Builders](https://docs.cloud.google.com/docs/buildpacks/builders).

### Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/run/docs/runtime-support#python) is in [Preview](https://cloud.google.com/products?e=48754805#product-launch-stages). Starting from Python version 3.14 and later, the Python buildpack uses the uv package manager as the
default installer for the dependencies you specify in your `requirements.txt` file. You can also use pip as the default installer for these versions by setting the `GOOGLE_PYTHON_PACKAGE_MANAGER` environment variable to `pip`. For more information, see [Specify dependencies in Python](https://docs.cloud.google.com/run/docs/runtimes/python-dependencies.md#dependencies).

---
## 2025-11-11

### Feature

You can set a [task timeout](https://docs.cloud.google.com/run/docs/configuring/task-timeout) up to 168 hours
(7 days) for Cloud Run jobs. (GA)

---
## 2025-11-06

### Feature

Use [dual-stack subnets with IPv6](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet)
to let your Cloud Run resources send IPv4 and internal IPv6 traffic to a VPC
network with Direct VPC egress, and send external IPv6 traffic to the public
internet. (GA)

---
## 2025-10-31

### Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/run/docs/runtime-support#java) is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-30

### Feature

For Cloud Run source deployed services and functions with [GPU enabled](https://docs.cloud.google.com/run/docs/configuring/services/gpu), Cloud Run defaults to using Cloud Build's `e2-highcpu-8 machine` type for
the build process when using the gcloud CLI or the Google Cloud console. This
change allows for higher CPU support and faster build times, and also leads to a
moderate increase in the overall cost of your service (GA).

---
## 2025-10-21

### Feature

Support for [configuring GPU](https://docs.cloud.google.com/run/docs/configuring/jobs/gpu)
for your Cloud Run job is in General Availability (GA).

### Feature

[Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) now supports [Private NAT](https://docs.cloud.google.com/nat/docs/private-nat) (GA).

---
## 2025-10-20

### Feature

Direct VPC egress now supports [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records) (Preview).

---
## 2025-10-06

### Feature

Support for [applying maximum instance configuration](https://docs.cloud.google.com/run/docs/configuring/max-instances#service-vs-revision-level) at the service level is in General Availability (GA).

---
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
