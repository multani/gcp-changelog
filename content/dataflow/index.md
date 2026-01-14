# Dataflow

## 2026-01-13

### Feature

Dataflow now serves a notice for when the Dataflow
[Runner v2](https://docs.cloud.google.com/dataflow/docs/runner-v2) container image of a streaming pipeline
will be upgraded. To use a new image and avoid the scheduled maintenance, launch
a replacement job before the upgrade. For more information, see
[Runner v2 harness update](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#runner_v2_harness_update).

---
## 2025-11-21

### Feature

Dataflow now supports speculative execution for batch pipelines. This feature mitigates the impact of slow-running tasks (*stragglers*) by launching a redundant execution of these tasks. The first task to finish is used, and the other is canceled, which can improve the overall completion time of your pipeline. This feature is generally available. For more information, see [Use speculative execution to avoid stragglers](https://docs.cloud.google.com/dataflow/docs/guides/large-pipeline-best-practices#backup-tasks).

---
## 2025-09-24

### Feature

For jobs that use GPUs, Dataflow now supports the flex-start provisioning model. This flex-start provisioning model can improve your ability to get access to constrained GPU resources for short-duration workloads. This feature is available in Preview and is for batch pipelines only. For more information, see [Configure a provisioning model](https://cloud.google.com/dataflow/docs/gpu/use-gpus#optional_configure_a_provisioning_model).

---
## 2025-09-08

### Feature

Dataflow now supports using [secure tags](https://cloud.google.com/firewall/docs/tags-firewalls-overview) to set firewall rules on worker VMs. For more information, see [Use secure tags with Dataflow](https://cloud.google.com/dataflow/docs/guides/routes-firewall#secure_tags).

---
## 2025-08-27

### Feature

Dataflow supports TPUs, Google's custom-designed AI accelerators that are optimized for large-scale AI/ML workloads. This feature lets you accelerate inference workloads on frameworks like PyTorch, JAX, and TensorFlow. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) with an allowlist. For more information, see [Dataflow support for TPUs](https://cloud.google.com/dataflow/docs/tpu/tpu-support).

### Feature

Dataflow supports [*specifically targeted* reservations](https://cloud.google.com/compute/docs/instances/reservations-overview#consumption-type) for pipelines using accelerators (GPUs or TPUs). This functionality is generally available with an allowlist. For more information, see [Use Compute Engine reservations with Dataflow](https://cloud.google.com/dataflow/docs/guides/compute-engine-reservations.md#reservations-accelerators).

### Changed

Dataflow supports NVIDIA® H100 and NVIDIA® H100 Mega GPU types. For more information, see [Dataflow support for GPUs](https://cloud.google.com/dataflow/docs/gpu/gpu-support).

---
## 2025-08-26

### Fixed

Dataflow [Runner v2](https://cloud.google.com/dataflow/docs/runner-v2) fixes an issue that could cause data discrepancies when using splittable DoFns, particularly when processing large datasets as side inputs. This fix ensures that all data is accurately processed and transmitted within the pipeline. This improvement is available in recent Dataflow service releases, and is automatically enabled when using Dataflow Runner v2.

**Note:** After this fix, pipelines that previously experienced data loss due to this issue might consume more resources (such as CPU, memory, and processing time) because more data is being processed. This increase in resource usage is expected and reflects the correct behavior of the pipeline.

---
## 2025-08-11

### Feature

Dataflow now automatically detects performance bottlenecks in streaming jobs. You can see the cause of the bottleneck in the **Step Info** panel to help with troubleshooting.

For more information, see [Troubleshoot bottlenecks](https://cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks).

---
## 2025-06-26

### Feature

Dataflow now supports an automated parallel update workflow for streaming jobs. This feature helps minimize disruption by launching a new replacement job that runs in parallel with the existing job. After a duration of time you specify, the old job is automatically drained.

For more information, see [Run parallel pipelines](https://cloud.google.com/dataflow/docs/guides/upgrade-guide#run-parallel-pipelines).

---
## 2025-06-09

### Feature

Dataflow now supports right fitting for streaming jobs. *Right fitting* lets you specify resource requirements for an entire pipeline or for specific pipeline steps. Previously, right fitting was only supported for batch pipelines. For more information, see [Streaming right fitting](https://cloud.google.com/dataflow/docs/guides/right-fitting#streaming-right-fitting).

---
