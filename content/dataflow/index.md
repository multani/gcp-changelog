# Dataflow

## 2025-08-27

### Feature

Dataflow supports Cloud TPUs, Google's custom-designed AI accelerators that are optimized for large-scale AI/ML workloads. This feature lets you accelerate inference workloads on frameworks like PyTorch, JAX, and TensorFlow. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) with an allowlist. For more information, see [Dataflow support for TPUs](https://cloud.google.com/dataflow/docs/tpu/tpu-support).

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
