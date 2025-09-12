# Google Agentspace

## 2025-09-11

### Changed

**Google Agentspace: Interface updates**

* The LLM model selector has moved from the search bar to directly below the product logo in the top-left corner.
* The web grounding tool and source has been renamed *Google Search* and *Enterprise web search,* depending on the type of web grounding configured.
* The *Sources* button in the search bar has been renamed *Data.*
* The *Data* menu (formerly *Sources*) now shows which sources are selected.

---
## 2025-09-05

### Feature

**Google NotebookLM Enterprise: Notebook creation and management using the API (GA)**

Use standalone APIs to programmatically create and manage your notebooks. For more information, see [Create and manage notebooks using the API](https://cloud.google.com/agentspace/notebooklm-enterprise/docs/api-notebooks).

---
## 2025-08-28

### Feature

**Google NotebookLM Enterprise: Generate podcasts using the Podcast API (GA with allowlist)**

Use a standalone API to programmatically generate NotebookLM-style podcasts. No data store required; provide the source content directly to the [Podcast API](https://cloud.google.com/agentspace/docs/reference/rest/v1/projects.locations.podcasts.operations).

This feature is available to select Google Cloud customers (GA with allowlist). For more information, see [Generate podcasts (API method)](https://cloud.google.com/agentspace/notebooklm-enterprise/docs/podcast-api).

---
## 2025-08-21

### Breaking

**Full sync in SharePoint connector to avoid duplicate documents**

Because of a change that tries to optimize the sync performance, performing an incremental sync in a [SharePoint connector data store](https://cloud.google.com/agentspace/docs/connect-sharepoint-online) can cause duplicate documents for `file` entity types. This is applicable to all SharePoint connectors created before August 21, 2025, that contain `file` entity types.

As a one-time solution, you can avoid duplication by either running a full sync manually or waiting for the next scheduled full sync. After performing the full sync, you can perform incremental syncs without generating any duplicate documents.

---
## 2025-08-18

### Feature

**Google Agentspace: Export analytics**

Export metrics to a BigQuery table in your Google Cloud project using the `analytics:exportMetrics` method.

For more information, see [View and export analytics data](https://cloud.google.com/agentspace/docs/view-analytics#export_metrics).

---
## 2025-08-12

### Feature

**Google Agentspace: Custom starter prompts for no-code agents**

You can add starter prompts to no-code agents. Starter prompts guide users on how to interact with the agent. See [Create a no-code agent with Agent Designer](https://cloud.google.com/agentspace/docs/agent-designer).

---
