# AI Hypercomputer

## 2025-09-10

### Feature

**Generally available**: The [accelerator-optimized A4X machine type](https://cloud.google.com/ai-hypercomputer/docs/gpu#a4x), the first GPU VM to run on Arm, is available on AI Hypercomputer. The A4X machine series has the NVIDIA GB200 Grace Blackwell Superchips attached and runs on the NVIDIA GB200 NVL72 platform. Use this machine type to run your large artificial intelligence (AI) models and machine learning (ML) workloads. The A4X machine type is currently available in the `us-central1-a` zone.

### Feature

**Generally available**: You can receive a notification when maintenance for an A4X reservation sub-block is scheduled, starts, or is completed. Additionally, you can now view and trigger maintenance for an A4X reservation sub-block. These features give you more control over maintenance for your A4X reservations, helping you minimize downtimes for your workloads. For more information, see [Manage host events across reservations](https://cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations).

### Feature

You can receive at least seven days of advance notice for unplanned hardware maintenance for a reservation. This feature helps you more proactively control disruptions to your workloads when unplanned maintenance is scheduled after a host error or faulty host report. For more information, see [Manage hardware emergency maintenance notifications](https://cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#emergency-notifications).

### Feature

**Generally available**: You can use the following Cloud Monitoring metrics to monitor your A4X VMs, and help you identify and troubleshoot issues with your GPUs:

* NVLink runtime error
* Uncorrectable DRAM ECC errors
* Uncorrectable DRAM row remapping count
* Uncorrectable DRAM row remapping failed
* Uncorrectable PCIe errors
* Uncorrectable cache ECC errors

For more information, see [Monitor VMs and Slurm clusters](https://cloud.google.com/ai-hypercomputer/docs/monitor).

### Feature

**Generally available**: You can view and manage the topology of your A4X reservations, including sub-blocks. This feature helps you better understand the topology of the VMs in your workload to further minimize network latency, as well as understand the health of your reservation blocks or sub-blocks. For more information, see
[View reserved capacity](https://cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity).

### Feature

**Generally available**: When you reserve capacity for creating VMs, you can specify the reservation operational mode for your reserved capacity. A reservation operational mode defines how your VMs behave after a host error or faulty host report, and it determines your level of visibility and control over the reservation's infrastructure. For more information, see [Reservation operational mode](https://cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode).

### Feature

**Generally available**: When you reserve capacity for creating VMs, you can specify a maintenance scheduling type for your reservations. This feature helps you minimize downtimes by letting you specify whether you want to group VMs and have synchronized maintenance scheduling (*grouped*), or loosely couple VMs have independent maintenance scheduling (*independent*). For more information, see [Maintenance scheduling types](https://cloud.google.com/ai-hypercomputer/docs/create/review-configurations#maintenance-scheduling-types).

---
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
