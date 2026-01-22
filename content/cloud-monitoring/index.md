# Cloud Monitoring

## 2026-01-21

### Feature

Your Application Monitoring dashboards now display the trace spans that are
associated with your registered App Hub applications. The display
includes annotations that let you identify services and workloads. You can also
open the Trace Explorer page from your Application Monitoring dashboards.
To learn more, see the following documents:

* [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring).
* [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring).
* [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces) describes how to
  use the Trace Explorer page to filter and explore your trace data.

---
## 2025-12-16

### Other

On December 15, 2025, it was announced that your Application Monitoring
dashboards will display the trace spans that are associated with your
registered App Hub applications. Those dashboards don't display
trace data. To view your trace data, use the Trace Explorer page.

---
## 2025-12-15

### Feature

Your Application Monitoring dashboards now display the trace spans that are
associated with your registered App Hub applications. The display
includes annotations that let you identify services and workloads. You can also
open the Trace Explorer page from your Application Monitoring dashboards.
To learn more, see the following documents:

* [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring).
* [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring).
* [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces) describes how to
  use the Trace Explorer page to filter and explore your trace data.

---
## 2025-12-11

### Feature

You can now add a widget to a dashboard that lets you manage the settings for
a variable. To learn more, see the following documents:

* [Google Cloud console: Add widget to manage the value of a variable](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#add-filter-control-widget)
* [API: Dashboard with a FilterControl widget](https://docs.cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_filter_control)

### Feature

The Google Cloud CLI (`gcloud`) commands to manage
Cloud Monitoring alerting policies are now generally available.
For more information, see [`gcloud monitoring
policies`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies).

---
## 2025-12-08

### Feature

You can now install and manage the Ops Agent on virtual machines in
a specified zone by using VM Extension Manager extension policies.
You can use extension policies to keep the installed version of the agent
current, keep a specified version of the agent installed, and other tasks.
For more information, see [Install and manage the Ops Agent by using
VM Extension Manager policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies).

---
## 2025-11-04

### Feature

You can now view the topology for applications that you register with
App Hub. The topology map provides a graphical view of the
relationships between the services and workloads in your App Hub
application. The topology map also displays alerts and traffic latency,
which can help you understand how
your application is performing and diagnose issues.
This feature is in Public Preview.

To learn more, see the following:

* [View application topology](https://docs.cloud.google.com/monitoring/docs/application-topology)
* [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring)

---
## 2025-10-23

### Feature

You can now use the Google Cloud CLI and the Cloud Monitoring API to list
incidents and get incident details. This feature is in Public
Preview. For more information, see the following pages:

* [Incidents for metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/incidents-events)
* [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/alerts)
* [API documentation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts)

---
## 2025-10-02

### Feature

Application Monitoring is now
[generally available (GA)](https://cloud.google.com/products#product-launch-stages).
Application Monitoring lets you monitor the resources and infrastructure from
the perspective of an [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) application. The
out-of-the-box dashboards that Application Monitoring creates can help you
understand how your application's resources are performing, and they can help
you diagnose issues.

* [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring)
  provides a brief overview of this feature.
* [Set up application monitoring](https://docs.cloud.google.com/monitoring/docs/setup-application-monitoring)
  describes how to configure an observability scope so that you have an
  aggregated view of your log, metric, and trace data.
* [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring)
  describes the labels attached to your telemetry data and provides guidance
  about how to explore the OOTB dashboards.
* [Supported infrastructure](https://docs.cloud.google.com/monitoring/docs/application-monitoring-services).

---
## 2025-09-15

### Feature

When viewing a chart, you can now open a flyout that displays the chart and
related log entries. To explore your metric and log data in more detail,
you can then use the toolbars and menus in the flyout. To learn more,
see the following:

* [Correlate metric and log data](https://cloud.google.com/monitoring/charts/working-with-charts#correlate-telemetry)
* [Explore application telemetry](https://cloud.google.com/monitoring/docs/application-monitoring#explore-application)

---
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
