# AI Hypercomputer

## 2025-07-18

### Feature

**Generally available**: You can troubleshoot workloads with slow performance by using straggler detection metrics and logs.

*Stragglers* are single-point, non-crashing failures that eventually
slow down your entire workload. Large-scale ML workloads are very susceptible to stragglers, and VMs with stragglers are often very difficult to notice and pinpoint without straggler detection.

For more information, see [Monitor VMs and Slurm clusters](https://cloud.google.com/ai-hypercomputer/docs/monitor) and [Troubleshoot slow performance](https://cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance).

---
## 2025-07-10

### Feature

**Generally available**: You can now manage the [Collective Communication Analyzer (CoMMA)](https://cloud.google.com/ai-hypercomputer/docs/nccl/comma), a library that uses the NVIDIA Collective Communication Library (NCCL) profiler plugin to collect detailed NCCL telemetry for GPU machine types. The collected performance metrics and operational events are used for analyzing and optimizing large-scale AI and ML training workloads.

CoMMA is automatically installed and enabled on A4X, A4 High, and A3 Ultra machine types when using specific images. You can manage this data collection by disabling the plugin, adjusting its data granularity levels, or manually installing it on other GPU machine types. For more information, see [Enable, disable, and configure CoMMA](https://cloud.google.com/ai-hypercomputer/docs/nccl/configure-comma).

---
## 2025-07-07

### Feature

**Preview**: You can use future reservations in calendar mode to obtain resources for up to 90 days. By creating a request in calendar mode, you can reserve up to 80 GPU VMs for a future date and time. Then, you can use that capacity to run the following workloads:

* Model pre-training
* Model fine-tuning
* Simulations
* Inference

For more information, see [Choose a consumption option](https://cloud.google.com/ai-hypercomputer/docs/consumption-models).

---
## 2025-06-11

### Feature

**Generally available**: You can apply a workload policy in a managed instance group (MIG) to specify the type of the workload to run on the MIG. Workload policies help improve the workload performance by optimizing the underlying infrastructure. The supported type, `high-throughput`, is ideal for workloads that require high networking performance. For more information, see [Workload policy for MIGs](https://cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy#workload-policy).

---
