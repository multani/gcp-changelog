# Dataflow

## 2025-06-26 00:00:00-07:00

### Feature

Dataflow now supports an automated parallel update workflow for streaming jobs. This feature helps minimize disruption by launching a new replacement job that runs in parallel with the existing job. After a duration of time you specify, the old job is automatically drained.

For more information, see [Run parallel pipelines](https://cloud.google.com/dataflow/docs/guides/upgrade-guide#run-parallel-pipelines).## 2025-06-09 00:00:00-07:00

### Feature

Dataflow now supports right fitting for streaming jobs. *Right fitting* lets you specify resource requirements for an entire pipeline or for specific pipeline steps. Previously, right fitting was only supported for batch pipelines. For more information, see [Streaming right fitting](https://cloud.google.com/dataflow/docs/guides/right-fitting#streaming-right-fitting).