# Vertex AI Workbench

## 2026-01-16

### Feature

[Preview](https://cloud.google.com/products#product-launch-stages):
The Gemini CLI is available in Vertex AI Workbench instances.
The Gemini CLI is an open source AI agent that provides access to
Gemini directly in a terminal. You can use the Gemini CLI
to do tasks like the following:

* Create a new notebook.
* Run notebook cells.
* Write and edit a notebook's code and text cells.
* Explain code and technical concepts.
* Interact with a Vertex AI Workbench instance's local file system,
  including performing complex file operations that span multiple files
  based on a single, high-level instruction.
* Run basic shell commands.
* Run commands to interact with other Google Cloud services, such as
  Vertex AI and BigQuery.

To get started, see
[Use the Gemini CLI](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/gemini-cli).

---
## 2025-12-12

### Feature

* The following features are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages):

  + [Create new Vertex AI Workbench instances](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/create#create) with JupyterLab 4+.
  + [Create an instance with managed user credential access.](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/create-euc-instance)
* Using post-startup scripts for new instances with user credential access is now available in private GA. For information about access to this release, see the [access request page](https://docs.google.com/forms/d/e/1FAIpQLSdzNZUFsRRbB0KaMCObGUYzIo6lK3X2tO7JZOm_DZrUhBYw5Q/viewform). For more information, see [Create instances with post-startup scripts](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/create-euc-instance#post-startup-scripts).

---
## 2025-12-10

### Feature

**M137 release**

The M137 release of Vertex AI Workbench instances includes the following:

* Patched an issue where `sudo` prompts for a password when a custom Jupyter user
  name is specified.

---
## 2025-12-09

### Feature

[Generally available (GA)](https://cloud.google.com/products#product-launch-stages):
Encrypt your data-in-use by using
[Confidential Computing](https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-overview).
You can enable the Confidential VM service when you create
a Vertex AI Workbench instance. To get started, see [Create an instance with
Confidential Computing](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/create-confidential-computing).

---
## 2025-11-21

### Feature

**M136 release**

The M136 release of Vertex AI Workbench instances includes the following:

* Patched an issue where image outputs aren't displayed properly.

---
## 2025-11-17

### Feature

**M135 release**

The M135 release of Vertex AI Workbench instances includes the following:

* Patched an issue where user-triggered OS shutdowns aren't reported to
  the Notebooks API.

---
## 2025-10-09

### Feature

**M134 release**

The M134 release of Vertex AI Workbench instances includes the following:

* Patched a regression with custom notebook metrics reporting (for example,
  `jupyterlab_kernels` and `docker_status metrics`).
* Updated the Dataproc JupyterLab plugin (`dataproc-jupyter-plugin`) to
  version 0.1.92.
* When using Google Cloud CLI commands, the `project` and `region` properties
  are preset.

---
## 2025-10-01

### Feature

[Generally available (GA)](https://cloud.google.com/products/#product-launch-stages):
You can use [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation)
with Vertex AI Workbench instances. Workforce Identity Federation lets
you create and manage Vertex AI Workbench instances with credentials
provided by an external identity provider (IdP). For more information, see
[Create an instance with third party credentials](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/create-third-party-instance).

---
## 2025-09-17

### Feature

**M133 release**

The M133 release of Vertex AI Workbench instances includes the following:

* Patched an incompatibility with the Dataproc JupyterLab plugin (`dataproc-jupyter-plugin`) and instances with end-user credentials enabled.

---
## 2025-08-29

### Feature

**M132 release**

The M132 release of Vertex AI Workbench instances includes the following:

* The new scheduler Jupyter plugin (`scheduler-jupyter-plugin`) is now preinstalled in the Jupyterlab 4 environment, with support for both the Cloud Composer and Vertex AI notebook schedulers.
* Updated the Dataproc JupyterLab plugin (`dataproc-jupyter-plugin`) to version 0.1.90.
* Patched bugs related to the managed end user credentials feature (Preview), resolving an incompatibility with listing Dataproc remote kernels.
* Patched a bug that caused instances with disabled proxy access to get stuck in provisioning.
* Removed the archived Debian 11 backports repository, resolving an issue with running `apt update` within the instance.

---
## 2025-08-05

### Feature

[Generally available](https://cloud.google.com/products#product-launch-stages): You can consume reservations with Vertex AI Workbench instances. Reservations of Compute Engine zonal resources help you gain a high level of assurance that your jobs have the necessary resources to run. For more information, see [Use reservations with Vertex AI Workbench instances](https://cloud.google.com/vertex-ai/docs/workbench/instances/reservations).

---
## 2025-07-10

### Feature

**M131 release**

The M131 release of Vertex AI Workbench instances includes the following:

* Updated the Dataproc JupyterLab plugin to version 0.1.89.

---
## 2025-06-26

### Feature

**M130 release**

The M130 release of Vertex AI Workbench instances includes the following:

* Updated the Dataproc JupyterLab plugin to version 0.1.87.
* Added the BigQuery JupyterLab plugin, version 0.0.1.
* The `GOOGLE_CLOUD_REGION` environment variable is now set by default.

---
## 2025-06-10

### Feature

Available in [Preview](https://cloud.google.com/products#product-launch-stages): You can consume reservations with Vertex AI Workbench instances. Reservations of Compute Engine zonal resources help you gain a high level of assurance that your jobs have the necessary resources to run. For more information, see [Use reservations with Vertex AI Workbench instances](https://cloud.google.com/vertex-ai/docs/workbench/instances/reservations).

---
