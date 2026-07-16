# Agent Platform Workbench

## 2026-07-13

### Feature

**Agent Platform Workbench image release**

The following Agent Platform Workbench instances image releases are available:

* **20260712-2130-rc0 (`workbench-instances-2603` - Debian 12)**
  + Installed latest packages from upstream dependencies.
  + Fixed broken cupy installation.
* **M144 (`workbench-instances` - Debian 11)**
  + Installed latest packages from upstream dependencies.
  + Fixed a race condition that could cause JupyterLab to be unreachable (HTTP 524) on GPU instances.

---
## 2026-07-06

### Feature

**Agent Platform Workbench image release**

The following Agent Platform Workbench instances image release is available:

* **20260701-2130-rc0 (`workbench-instances-2603` - Debian 12)**
  + Installed latest packages from upstream dependencies.
  + Fixed a race condition that could cause JupyterLab to be unreachable (HTTP 524) on GPU instances.
  + Fixed an issue where long-running requests (for example, streaming or long-poll connections) could be terminated after about 60 seconds.

---
## 2026-06-30

### Feature

**Python 3.12 base containers for Agent Platform Workbench custom containers**

You can build [custom containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-custom-container)
for Agent Platform Workbench instances using Python 3.12 base containers, in addition
to the default Python 3.10 base containers. The Python 3.12 standard and slim
base containers are available at the following URIs:

* `us-docker.pkg.dev/workbench-images/gcr.io/workbench-container-2606:latest`
* `us-docker.pkg.dev/workbench-images/gcr.io/workbench-container-slim-2606:latest`

---
## 2026-06-29

### Feature

**Agent Platform Workbench image release**

The following Agent Platform Workbench instances image release is available:

* **20260628-2130-rc0 (`workbench-instances-2603` - Debian 12)**
  + Installed latest packages from upstream dependencies.
  + Installed TensorFlow and PyTorch packages to the default kernel.

---
## 2026-06-24

### Feature

**Agent Platform Workbench image release**

The following Agent Platform Workbench instances image release is available:

* **20260624-1604-rc0 (`workbench-instances-2603` - Debian 12)**
  + Installed latest packages from upstream dependencies.
  + Fixed an issue where notebook kernels could become unavailable if the Dataproc plugin failed to load.

---
## 2026-06-23

### Feature

**Agent Platform Workbench image release**

The following Agent Platform Workbench instances image releases are available:

* **20260622-2130-rc0 (`workbench-instances-2603` - Debian 12)**
  + Installed latest packages from upstream dependencies.
  + Fixed a duplicate "Python 3 (ipykernel)" kernel appearing in the launcher.
* **M143 (`workbench-instances` - Debian 11)**
  + Installed latest packages from upstream dependencies.

---
