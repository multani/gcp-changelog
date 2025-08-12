# Dataflow

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
