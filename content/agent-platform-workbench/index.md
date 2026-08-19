# Agent Platform Workbench

## 2026-08-16

### Security

Updated the bundled Ruby gems rexml and net-imap to patched versions, addressing known vulnerabilities.

### Change



### 20260816-2330-rc0 Release



### Security

Updated aiohttp, joblib and cryptography to patched versions, addressing known vulnerabilities including CVE-2022-21797 and CVE-2025-69223.

### Change

Installed latest packages from upstream dependencies.

### Change

Updated the CUDA base image from 12.8.1 to 12.9.2 (CUDA 12.9, cuDNN 9.10). This is a minor CUDA 12 update, binary compatible with the previous image, and also addresses known vulnerabilities in a bundled NVIDIA profiler component.

### Security

Updated the bundled Ruby gems rexml and net-imap to patched versions, addressing known vulnerabilities.

### Deprecated

Removed the JupyterLab 3 environment from the Python 3.12 custom container; JupyterLab 4 is now the only JupyterLab environment and is always used. The Python 3.10 images are unaffected.

### Change



### 20260816-2330-rc0 Release



### Security

Updated aiohttp, joblib and cryptography to patched versions, addressing known vulnerabilities including CVE-2022-21797 and CVE-2025-69223.

### Change

Installed latest packages from upstream dependencies.

### Change



### 20260816-2230-rc0 Release



### Change

Installed latest packages from upstream dependencies.

### Change



### 20260816-2230-rc0 Release



### Change

Installed latest packages from upstream dependencies.

### Change



### 20260816-2130-rc0 Release



### Change

Installed latest packages from upstream dependencies.

### Change

Installed latest packages from upstream dependencies.

### Fixed

Fixed the Git panel's grayed out buttons, which were disabled due to an issue with the Jupyter Lab's Git plugin introduced in version 0.54.0.

### Change



### 20260816-2030-rc0 Release



---
## 2026-08-09

### Change

Installed latest packages from upstream dependencies.

### Change



### 20260809-2330-rc0 Release



### Change

Installed latest packages from upstream dependencies.

### Change



### 20260809-2330-rc0 Release



### Fixed

Fixed the Git panel's grayed out buttons which were disabled due to an issue with the Jupyter Lab's Git plugin introduced in version 0.54.0.

### Change



### 20260809-2230-rc0 Release



### Change

Installed latest packages from upstream dependencies.

### Fixed

Fixed the Git panel's grayed out buttons which were disabled due to an issue with the Jupyter Lab's Git plugin introduced in version 0.54.0.

### Change



### 20260809-2230-rc0 Release



### Change

Installed latest packages from upstream dependencies.

### Change



### 20260809-2130-rc0 Release



### Change

Updated the NVIDIA GPU driver on Workbench Debian 12 images from 580.65.06 to 580.126.20 for compatibility with the Debian 12 6.1.0-52 kernel.

### Change

Installed latest packages from upstream dependencies.

### Fixed

Fixed the Git panel's grayed out buttons which were disabled due to an issue with the Jupyter Lab's Git plugin introduced in version 0.54.0.

---
## 2026-08-02

### Change



### 20260802-2330-rc0 Release



### Change



### 20260802-2330-rc0 Release



### Fixed

Fixed issue with JupyterLab UI silently reverting file changes and interrupting kernels due to Gemini CLI's auto reload extension.

### Change

The JupyterLab last-active and auto-reload extensions are now enabled only when Gemini CLI is configured, preventing them from affecting the native JupyterLab UI otherwise.

### Change

Installed latest packages from upstream dependencies.

### Fixed

Fixed issue with JupyterLab UI silently reverting file changes and interrupting kernels due to Gemini CLI's auto reload extension.

### Change

The JupyterLab last-active and auto-reload extensions are now enabled only when Gemini CLI is configured, preventing them from affecting the native JupyterLab UI otherwise.

### Change

Installed latest packages from upstream dependencies.

### Fixed

Fixed an error that could prevent creating new `micromamba` environments at runtime due to package cache permissions.

### Fixed

Fixed an error that could prevent creating new `micromamba` environments at runtime due to package cache permissions.

### Change



### 20260802-2230-rc0 Release



### Change



### 20260802-2230-rc0 Release



### Fixed

Fixed issue with JupyterLab UI silently reverting file changes and interrupting kernels due to Gemini CLI's auto reload extension.

### Change

The JupyterLab last-active and auto-reload extensions are now enabled only when Gemini CLI is configured, preventing them from affecting the native JupyterLab UI otherwise.

### Change

Installed latest packages from upstream dependencies.

### Fixed

Fixed issue with JupyterLab UI silently reverting file changes and interrupting kernels due to Gemini CLI's auto reload extension.

### Change

The JupyterLab last-active and auto-reload extensions are now enabled only when Gemini CLI is configured, preventing them from affecting the native JupyterLab UI otherwise.

### Change

Installed latest packages from upstream dependencies.

---
## 2026-07-30

### Change



### M145 Release



### Change



### 20260730-2130-rc0 Release



### Change

Installed latest packages from upstream dependencies.

### Change

Installed latest packages from upstream dependencies.

### Fixed

Fixed issue with JupyterLab UI silently reverting file changes and interrupting kernels due to Gemini CLI's auto reload extension.

### Change

The JupyterLab last-active and auto-reload extensions are now enabled only when Gemini CLI is configured, preventing them from affecting the native JupyterLab UI otherwise.

### Fixed

Fixed the JupyterLab Git extension's Pull and Push buttons being disabled by pinning `jupyterlab-git` to 0.53.0.

### Fixed

Fixed the JupyterLab Git extension's Pull and Push buttons being disabled by pinning `jupyterlab-git` to 0.53.0.

### Fixed

Fixed an error that could prevent creating new `micromamba` environments at runtime due to package cache permissions.

### Fixed

Fixed an error that could prevent creating new `micromamba` environments at runtime due to package cache permissions.

### Fixed

Workbench internal agents now trust custom and enterprise CA certificates installed on the host operating system, fixing TLS certificate verification failures for connections routed through the instance proxy.

### Fixed

Workbench internal agents now trust custom and enterprise CA certificates installed on the host operating system, fixing TLS certificate verification failures for connections routed through the instance proxy.

### Fixed

Files created by the post-startup script are now owned by the `jupyter` user, and `git safe.directory` is configured so that root-owned repositories continue to work.

### Fixed

Files created by the post-startup script are now owned by the `jupyter` user, and `git safe.directory` is configured so that root-owned repositories continue to work.

### Fixed

Fixed issue with JupyterLab UI silently reverting file changes and interrupting kernels due to Gemini CLI's auto reload extension.

### Change

The JupyterLab last-active and auto-reload extensions are now enabled only when Gemini CLI is configured, preventing them from affecting the native JupyterLab UI otherwise.

### Change

The JupyterLab last-active and auto-reload extensions are now enabled only when Gemini CLI is configured, preventing them from affecting the native JupyterLab UI otherwise.

---
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

### Change



### M144 Release



### Change



### 20260712-2130-rc0 Release



### Change

Installed latest packages from upstream dependencies.

### Change

Installed latest packages from upstream dependencies.

### Fixed

Fixed a race condition that could cause JupyterLab to be unreachable (HTTP 524) on GPU instances.

### Fixed

Fixed broken cupy installation.

### Feature

**Secure Boot is compatible with GPUs**

You can now enable Secure Boot on Agent Platform Workbench instances that have a
GPU attached. Secure Boot with GPUs is supported on the `workbench-instances-2603`
VM image and the `workbench-container-2606` custom container, which include a
Secure Boot-signed NVIDIA GPU driver so the driver loads under Secure Boot. For
more information, see [Create an
instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create).

### Feature

**Secure Boot is compatible with GPUs**

You can now enable Secure Boot on Agent Platform Workbench instances that have a
GPU attached. Secure Boot with GPUs is supported on the `workbench-instances-2603`
VM image and the `workbench-container-2606` custom container, which include a
Secure Boot-signed NVIDIA GPU driver so the driver loads under Secure Boot. For
more information, see [Create an
instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create).

### Feature

**Secure Boot is compatible with GPUs**

You can now enable Secure Boot on Agent Platform Workbench instances that have a
GPU attached. Secure Boot with GPUs is supported on the `workbench-instances-2603`
VM image and the `workbench-container-2606` custom container, which include a
Secure Boot-signed NVIDIA GPU driver so the driver loads under Secure Boot. For
more information, see [Create an
instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create).

---
## 2026-07-06

### Feature

**Agent Platform Workbench image release**

The following Agent Platform Workbench instances image release is available:

* **20260701-2130-rc0 (`workbench-instances-2603` - Debian 12)**
  + Installed latest packages from upstream dependencies.
  + Fixed a race condition that could cause JupyterLab to be unreachable (HTTP 524) on GPU instances.
  + Fixed an issue where long-running requests (for example, streaming or long-poll connections) could be terminated after about 60 seconds.

### Change



### 20260701-2130-rc0 Release



### Change

Installed latest packages from upstream dependencies.

### Fixed

Fixed a race condition that could cause JupyterLab to be unreachable (HTTP 524) on GPU instances.

### Fixed

Fixed an issue where long-running requests (for example, streaming or long-poll connections) could be terminated after about 60 seconds.

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
