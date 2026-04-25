# Gemini Enterprise Agent Platform

## 2026-04-22

### Change



### Initial release of Gemini Enterprise Agent Platform

This initial release includes (but is not limited to) the following releases or
changes:

* Change **Vertex
  AI** is now part of Gemini Enterprise Agent Platform. Information on model
  support for Vertex AI is now under [Gemini Enterprise Agent Platform >
  Models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/overview).
* Change **Agent
  Builder** is now part of Gemini Enterprise Agent Platform. Features have
  been renamed as follows:
  + **Agent Engine** is now [**Agent Runtime**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime).
  + **Agent Builder Sessions** is [**Agent Platform Sessions**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions).
  + **Memory Bank** is now [**Agent Platform Memory Bank**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank).
* Change **Agent
  Runtime** now supports long-running operations (up to 7 days).
* Change **Agent
  Runtime** now supports sub-second cold starts.
* Change
  Provisioning for **Agent Runtime** has been reduced to less than 1 minute.
* Release You can now use your own
  [custom-built
  containers](gemini-enterprise-agent-platform/build/runtime/setup#byoc) when
  you deploy agents with **Agent Runtime**.
* Change When
  [creating a
  Session](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-api),
  you can specify your own session ID.
* Release Memory Bank now enables
  continuous event streaming with automated memory generation triggered by
  configurable criteria like event count or idle time. For more information,
  see [Ingest
  events](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/ingest-events).
* Release Memory Bank now automatically
  maintains an immutable version history of memories through revision
  resources. For more information, see [Memory
  revisions](gemini-enterprise-agent-platform/scale/memory-bank/revisions).
* Release [**Agent
  Identity**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview)
  for General Availability. Agent Identity helps let your agent securely
  authenticate to MCP servers, cloud resources, endpoints, and other agents,
  either acting as itself or acting on behalf of the end user.
* Release [**Agent Gateway**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)
  for Private Preview. Agent Gateway is the networking component of the Gemini
  Enterprise Agent Platform ecosystem. It secures and governs connectivity for
  all agentic interactions, whether they occur between users and agents,
  agents and tools, or among agents themselves.
* Release [**Agent
  Registry**](https://docs.cloud.google.com/agent-registry/overview) for Public Preview. Agent Registry is
  a centralized, unified catalog that lets you store, discover, and govern
  Model Context Protocol (MCP) servers, tools, and AI agents within Google
  Cloud.
* Release New [**IAM governance
  policies**](gemini-enterprise-agent-platform/govern/policies/overview) are
  available in Private Preview.
* Release [**Agent
  Observability**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview)
  for Preview. Agent Observability in Gemini Enterprise Agent Platform
  provides comprehensive visibility into the performance, behavior, and health
  of your deployed agents and Model Context Protocol (MCP) servers. By
  monitoring key metrics, tracing execution paths, and observing your
  multi-agent system as a whole, you can diagnose issues, optimize resource
  consumption, and improve the reliability of your agents.
* Release [**Gemini Embedding
  2**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/embedding-2)
  (`gemini-embedding-2`) for General Availability.
* Release The [**Gemini Deep Research
  Agent**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/deep-research), a
  pre-built agent designed to help you plan, execute, and synthesize
  multi-step research tasks. It uses Gemini 3.1 Pro to bridge the gap between
  public web data and private enterprise context by simultaneously grounding
  research across three distinct, high-fidelity data streams.
* Release [**Agent Platform remote MCP
  server**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/use-agent-platform-mcp)
  for General Availability. Support for Model Context Protocol (MCP) use is
  available for Agent Platform.
* Change
  **Google Cloud console navigation**: The navigation menus under Agent
  Platform (formerly Vertex AI) and Data Analytics have been updated to
  centralize agentic products and features. Bookmarked links will continue to
  work via automatic redirects.

### Change



### Vertex AI to Gemini Enterprise Agent Platform naming changes

The table below lists all of the features that have been transitioned from Vertex AI and what their new names are in Agent Platform.

#### Click to expand naming changes list

| Vertex AI name | Agent Platform name |
| --- | --- |
| Vertex AI Platform | Agent Platform |
| Generative AI on Vertex AI | Generative AI |
| Vertex AI Studio | Agent Studio |
| Vertex AI API | Agent Platform API |
| Vertex AI Model Garden | Model Garden |
| Vertex AI Models as a Service (MaaS) | MaaS |
| (Gemini/Veo) on Vertex AI | (Gemini/Veo) on Agent Platform |
| (Claude/Llama/DeepSeek/etc.) on Vertex AI | (Claude/Llama/DeepSeek/etc.), available on Agent Platform |
| Pre-trained APIs on Vertex AI | Pre-trained APIs on Agent Platform |
| (Provisioned Throughput/Pay-as-you-go/etc.) on Vertex AI | (Provisioned Throughput/Pay-as-you-go/etc.) on Agent Platform |
| Gemini Live API on Vertex AI | Gemini Live API on Agent Platform |
| Vertex AI Search | Agent Search |
| Vertex AI Search for Industry | Agent Search for Industry |
| Vertex AI Search for Commerce | Agent Search for Commerce |
| Recommendations from Vertex AI Search | Recommendations |
| Vertex AI Conversation | Agent Conversation |
| Vertex AI RAG Engine | RAG Engine |
| Vertex AI Vector Search | Vector Search |
| Vertex AI Vector Search 2.0 | Agent Retrieval |
| Vertex AI Agent Engine | Agent Runtime |
| Vertex AI Studio App Builder | App Builder in Agent Studio |
| Vertex AI Agent Engine Memory Bank | Agent Platform Memory Bank |
| Vertex AI Agent Engine Sessions | Agent Platform Sessions |
| Vertex AI Agent Engine Code Execution | Agent Platform Code Execution |
| Grounding with Google [...] in Vertex AI | Grounding with Google [...] in Agent Platform |
| Grounding with Google [...] in Vertex AI Search | Grounding with Google [...] in Agent Search |
| Grounding with Google [...] in Vertex AI Studio | Grounding with Google [...] in Agent Studio |
| Vertex AI Training | Agent Platform Managed Training |
| Vertex AI Serverless Training | Agent Platform Serverless Training |
| Vertex AI Training Clusters (VTC) | Managed Training Clusters |
| Ray on Vertex AI | Ray on Agent Platform |
| Reinforcement Learning from Human Feedback (RLHF)/Reinforcement Learning (RL) on Vertex AI | Reinforcement Learning on Agent Platform |
| Vertex AI Neural Architecture Search | Neural Architecture Search on Agent Platform |
| Vertex AI Prediction/Vertex AI Inference | Agent Platform Inference |
| Vertex AI Vision | Agent Platform Vision |
| Vertex AI Batch Inference | Agent Platform Batch Inference |
| Vertex AI Online Inference | Agent Platform Online Inference |
| Vertex AI Endpoints | Agent Platform Endpoints |
| Vertex AI Forecasting/Forecasting with AutoML | Forecasting on Agent Platform |
| Vertex AI Pipelines | Agent Platform Pipelines |
| Vertex AI Notebooks | Agent Platform Notebooks |
| Vertex AI Colab Enterprise | Agent Platform Colab Enterprise |
| Vertex AI Workbench | Agent Platform Workbench |
| Vertex AI Workbench Instances | Agent Platform Workbench Instances |
| Vertex AI Feature Store | Agent Platform Feature Store |
| Vertex AI Model Registry | Agent Platform Model Registry |
| Vertex AI Model Evaluation | Agent Platform Model Evaluation |
| Gen AI evaluation service on Vertex AI | Gen AI evals |
| Vertex AI AutoML (Vision/Video/Tables) | Agent Platform AutoML |
| Data Labeling on Vertex AI | Data Labeling |
| Vertex AI on GDC | Agent Platform on GDC |
| Vertex AI Experiments | Experiments on Agent Platform |
| Vertex AI Model Monitoring | Model Monitoring on Agent Platform |
| Vertex AI Media Studio | Agent Media Studio |
| Vertex AI | Agent Platform |
| Vertex AI Generative AI | Agent Platform Generative AI |

### Issue

The following known issues affect Gemini Enterprise Agent Platform:

* **Audio track extraction (Gemini Embedding 2 only):** The `audio_track_extraction` feature does not work. For more information, see [Issue #504505771](https://issuetracker.google.com/504505771).

---
