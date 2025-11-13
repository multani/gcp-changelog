# Batch

## 2025-10-30

### Changed

Documentation has been updated to clarify the
[machine types that jobs can use](https://docs.cloud.google.com/batch/docs/get-started#machine-types).

### Changed

Dynamic Workload Scheduler for Batch
([Preview](https://cloud.google.com/products#product-launch-stages)) has
been replaced with the following consumption options:

* **Flex-start VMs
  ([Preview](https://cloud.google.com/products#product-launch-stages))**: We
  recommend Flex-start VMs if your job can withstand best-effort
  availability in exchange for discounted pricing and up to 7 days to finish
  running.
* **Calendar-mode reservations
  ([Preview](https://cloud.google.com/products#product-launch-stages))**: We
  recommend calendar-mode reservations if your job needs a very high level of
  assurance of resource availability for at least 1 day and up to 90 days.

Both consumption options use
[Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing),
which offers discounts of up to 53% off of on-demand pricing.
For more information, see [Create and run a job that uses GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus).

---
## 2025-07-24

### Issue

Pub/Sub might not send notifications for all intermediate states when a job or task changes very quickly. You can mitigate this issue by viewing state history through status events. For more information, see
[Known issues](https://cloud.google.com/batch/docs/known-issues#pubsub-missing-quick-states).

---
