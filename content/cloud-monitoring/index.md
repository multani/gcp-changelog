# Cloud Monitoring

## 2025-08-25

### Feature

Your Application Monitoring dashboards will display latency, error rates, and
traffic level for workloads deployed on Google Kubernetes Engine, when you
instrument your application with OpenTelemetry. To learn more, see
[Instrument an application for Application Monitoring](https://cloud.google.com/monitoring/docs/instrument-for-application-monitoring).

---
## 2025-08-21

### Feature

The following infrastructure is now integrated with Application Monitoring,
which is in public preview.

* AlloyDB for PostgreSQL clusters and services
* Bigtable clusters and services
* Dataproc Metastore services
* Cloud Deploy delivery pipelines
* Firestore databases
* Secret Manager secrets

To learn more, see
[Application Monitoring overview](https://cloud.google.com/monitoring/docs/about-application-monitoring)
and
[Supported infrastructure](https://cloud.google.com/monitoring/docs/application-monitoring-services).

---
## 2025-08-05

### Feature

You can now use the [`time_series_billed_for_queries_count`](https://cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/billing/time_series_billed_for_queries_count)
metric to estimate charges based on the number of time series that have been
queried. For more information, see [View the number of time series billed
for queries](https://cloud.google.com/stackdriver/estimating-bills#mon-billable-api-reads).

Billing by time series queried isn't enforced until October 2, 2025. For
more information, see [Cloud Monitoring pricing summary](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary).

---
## 2025-07-24

### Feature

You can now monitor and understand the costs and utilization of resources in
your Google Cloud project or App Hub application
by using the Cost Explorer. This feature is in Public Preview. For more
information, see [Optimize costs with the Cost Explorer](https://cloud.google.com//stackdriver/docs/costs/optimize-costs).

---
## 2025-07-17

### Feature

Application-specific resource attributes are attached to your trace data when
your App Hub applications use supported Google Cloud resources,
or when you instrument an application with OpenTelemetry and use the
Google Cloud Telemetry endpoint. To learn more, see the following:

* [Application Monitoring overview](https://cloud.google.com/monitoring/docs/about-application-monitoring)
* [View application telemetry](https://cloud.google.com/monitoring/docs/application-monitoring)
* [Find and explore traces](https://cloud.google.com/trace/docs/finding-traces)
* [Telemetry (OTLP) API overview](https://cloud.google.com/stackdriver/docs/reference/telemetry/overview)

---
## 2025-06-02

### Feature

You can now add treemap widgets to your custom dashboards. Treemaps display the
most recent value of aggregated data as a series of nested rectangles, the
color saturation of a rectangle is proportional to the represented value.
For more information, see the following:

* [Display the most recent value as a treemap](https://cloud.google.com/monitoring/charts#dashboard_with_a_treemap_widget)
* [API: Dashboard with a Treemap widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_a_treemap_widget)

---
