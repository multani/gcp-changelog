# Batch

## 2026-07-20

### Breaking

Starting on the following dates, you can no longer create a job that locates
its Compute Engine resources outside of the job's location.

* For projects that have successfully submitted before July 31, 2026 at least
  one job that uses the `allowedLocations[]` field with any region or zones
  outside of the job's location, changes are starting on *June 30, 2027*.
* For all other projects, changes are starting on *July 31, 2026*.

If none of your jobs specify the `allowedLocations[]` field, then no action is
required. Otherwise, ensure that any region or zones specified in the
`allowedLocations[]` field are in the same region as the job's location
before these dates. For more information, see
[Batch locations](https://docs.cloud.google.com/batch/docs/locations).

---
## 2026-07-17

### Feature

[Instance flexibility](https://docs.cloud.google.com/batch/docs/create-run-job-instance-flexibility) is available in
[Preview](https://cloud.google.com/products#product-launch-stages).
Instance flexibility lets you allow a job to run on multiple machine types that
you specify and can optionally rank. Use instance flexibility to improve
*obtainability*—the probability that resources are available to run your
job. For example, by allowing multiple machine types, you can reduce the
probability of resource availability errors and try to obtain Spot VMs
that are less likely to be preempted.

To get started, see [Improve resource obtainability for jobs](https://docs.cloud.google.com/batch/docs/improve-obtainability-overview).

---
## 2026-03-20

### Feature

Flex-start VMs and calendar-mode reservations are generally available
([GA](https://cloud.google.com/products#product-launch-stages)).

Both consumption options use
[Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing),
which offers discounts of up to 53% off of on-demand pricing.
For more information, see [Create and run a job that uses GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus)
and [Ensure resource availability using VM reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation).

---
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
