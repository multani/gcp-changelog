# Cloud Trace

## 2026-01-05

### Feature

You can now collect, view, and analyze multimodal prompts and responses from
your agentic applications that use the LangGraph or Agent Development Kit (ADK)
frameworks. This feature is in [Public Preview](https://cloud.google.com/products#product-launch-stages).

To learn more, see the following documents:

* [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/trace/docs/collect-view-multimodal-prompts-responses)
* [Instrument generative AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview)

---
## 2025-12-15

### Feature

The Trace Explorer has been updated to include annotations that let you
identify App Hub-registered services and workloads. The link provided
with a service or workload lets you open the corresponding
Application Monitoring dashboard. To learn more, see the following documents:

* [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces) describes how to
  use the Trace Explorer page to filter and explore your trace data.
* [Application Monitoring overview](https://docs.cloud.google.com/monitoring/docs/about-application-monitoring).
* [View application telemetry](https://docs.cloud.google.com/monitoring/docs/application-monitoring)
  describes how to view the telemetry for a registered application.

---
## 2025-11-06

### Feature

You can now collect, view, and analyze prompts and responses from your agentic
applications when they are built with the Agent Development Kit (ADK).
This feature is in Public Preview.

[Collect and view multimodal prompts and responses](https://docs.cloud.google.com/trace/docs/collect-view-multimodal-prompts-responses)
describes how to do the following:

* Configure your project and ADK to collect multimodal data.
* View a conversation and the multimodal data by using the Trace Explorer.
* Find log entries that contain references to multimodal data.
* Query your prompts and responses by using BigQuery.
* Evaluate your prompts and responses by using the Vertex AI SDK for Python.

---
## 2025-08-27

### Feature

You can now create and manage the trace scope programmatically. This feature
is in Public Preview. For more information, see the following documents:

* [Create and manage trace scopes](https://cloud.google.com/trace/docs/trace-scope/create-and-manage)
* [Trace scopes API overview](https://cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.traceScopes)

---
## 2025-07-17

### Feature

Application-specific resource attributes are attached to your trace data when
your App Hub applications use supported Google Cloud resources,
or when you instrument an application with OpenTelemetry and use the
Google Cloud Telemetry endpoint. You can use the Trace Explorer to filter
by your application, your service, or your workload. To learn more, see the
following:

* [Find and explore traces](https://cloud.google.com/trace/docs/finding-traces)
* [Application Monitoring overview](https://cloud.google.com/monitoring/docs/about-application-monitoring)
* [View application telemetry](https://cloud.google.com/monitoring/docs/application-monitoring)
* [Telemetry (OTLP) API overview](https://cloud.google.com/stackdriver/docs/reference/telemetry/overview)

---
## 2025-06-13

### Changed

The **Analysis reports** page has been removed.
To analyze your trace data, use the **Trace explorer** page.
You can use filters and the time-range selector to view
and analyze historical data.

---
## 2025-05-27

### Feature

Learn how to instrument your generative AI applications by using OpenTelemetry
and the LangGraph framework to collect information about the actions taken by
your AI agent. You can view generative AI events by using the
**Trace Explorer**:

* [Instrument generative AI applications](https://cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview)
* [Instrument a LangGraph ReAct Agent with OpenTelemetry](https://cloud.google.com/stackdriver/docs/instrumentation/ai-agent-langgraph)
* [View generative AI events](https://cloud.google.com/trace/docs/finding-traces#view_generative_ai_events)

---
