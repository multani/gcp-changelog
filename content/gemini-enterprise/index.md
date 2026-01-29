# Gemini Enterprise

## 2026-01-28

### Feature

**Gemini Enterprise: Support for new data stores and actions (Preview)**

The following data stores are now supported in Gemini Enterprise:

* [Confluence Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/confluence-dc)
* [Jira Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/jira-dc)
* [Zendesk](https://docs.cloud.google.com/gemini/enterprise/docs/zendesk)

**Download file** action has been added to [Dropbox](https://docs.cloud.google.com/gemini/enterprise/docs/dropbox). For a list of actions for all available data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

---
## 2026-01-27

### Change

**Gemini Enterprise: Autocomplete turned off in the chat box**

The autocomplete menu no longer appears as a user types in the chat box. Users
can still use the mentions feature by typing `@` in the chat box, followed by
the name of an agent, person, or file. For more information about mentions, see
[Add context with mentions](https://docs.cloud.google.com/gemini/enterprise/docs//assistant-chat#add_context_with_mentions).

---
## 2026-01-26

### Announcement

**Gemini Enterprise: Visual flow builder for existing agents**

The Agent Designer visual flow builder is now available for all agents created
before January 12, 2026. You can now manage these agents directly
from the [Agent Gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery) page, or edit their logic using the enhanced visual flow
builder from the **Agent Designer > Flow** tab.

For more information, see [Agent Designer overview](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer).

---
## 2026-01-23

### Change

**Gemini Enterprise: New actions in the unified view (Preview)**

New actions have been added to the following existing data stores:

* [Box](https://docs.cloud.google.com/gemini/enterprise/docs/box)
* [Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/confluence-cloud)
* [Dropbox](https://docs.cloud.google.com/gemini/enterprise/docs/dropbox)
* [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/jira-cloud)
* [Microsoft OneDrive](https://docs.cloud.google.com/gemini/enterprise/docs/ms-onedrive)
* [Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/ms-outlook)
* [Microsoft SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/ms-sharepoint)

---
## 2026-01-12

### Announcement

[Agent Designer](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer) is generally available ([GA](https://cloud.google.com/products?#product-launch-stages)).

---
## 2026-01-07

### Feature

**Semantic search in sessions**

Gemini Enterprise and Business have expanded search capabilities to include
semantic similarity, which lets you find relevant content in your chat history
based on meaning rather than just keywords.

---
## 2025-12-29

### Feature

**Semantic search in sessions**

Gemini Enterprise and Business have expanded search capabilities to include
semantic similarity, which lets you find relevant content in your chat history
based on meaning rather than just keywords.

---
## 2025-12-23

### Feature

**Gemini Enterprise: Manage actions using the updated flow (Public preview)**

Use the new capabilities on the **Actions** page to:

* Add new actions skipped during the data store creation process.
* Enable or disable the existing actions.
* Re-authenticate actions and verify authentication parameters.

For more information, see [Manage
actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).

---
## 2025-12-19

### Feature

**Gemini Enterprise: New actions available for data stores in the unified view (Public preview)**

New actions have been added for the following data stores:

* [Box](https://docs.cloud.google.com/gemini/enterprise/docs/box)
* [Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/confluence-cloud)
* [Microsoft Teams](https://docs.cloud.google.com/gemini/enterprise/docs/ms-teams)
* [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/jira-cloud)
* [Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/ms-outlook)

For a list of supported actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

### Feature

**Gemini Enterprise: Schedule agent executions for custom agents in Agent Designer (Preview)**

You can configure your custom agents, created using the Agent Designer, to execute predefined instructions and prompts on a set schedule.

Scheduled executions run automatically for personal tasks, but any action involving other people will be paused for your review and approval.

For more information, see [Schedule agent executions](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/schedule-agent).

---
## 2025-12-17

### Feature

**Gemini Enterprise: View the pooled quota usage (Public Preview)**

Admins can view the pooled quota usage of their licenses on the
**Manage users** page. This feature is in Public Preview. For more information,
see [View the pooled quota usage](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#view-quota-usage).

### Feature

**Gemini Enterprise: Use Gemini 3 Flash (Preview)**

You can use Gemini 3 Flash in Preview with Gemini Enterprise. To make
Gemini 3 Flash available to users in your
Gemini Enterprise app, a Gemini Enterprise admin must enable the
**Gemini 3 Flash (Preview)** toggle in the **Model availability**
feature control. For more information on feature controls, see
[Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

---
## 2025-12-15

### Feature

**Gemini Enterprise: Get user-level metrics (Preview)**

Admins can monitor user-level metrics in the **User Level** tab of the
**Analytics** page. This is a [Private preview](https://cloud.google.com/products#product-launch-stages)
feature. For more information, see
[Metrics definitions](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics#definitions).

---
## 2025-12-12

### Feature

**Gemini Enterprise: Unified data source creation and action flow**

The new unified process for creating a data store enables you to create the data store and the associated actions in a single, streamlined flow. This functionality allows Gemini Enterprise to perform tasks directly within the connected application.

The new **Actions** page shows you all the enabled actions for each data store. Actions are available in public preview and are enabled for Microsoft SharePoint, Microsoft Outlook, Microsoft OneDrive, Jira Cloud, Dropbox, and ServiceNow. For a list of supported actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

This launch includes support for the following data stores:

**Generally Available**

* [Microsoft SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/ms-sharepoint)
* [Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/ms-outlook)
* [Microsoft OneDrive](https://docs.cloud.google.com/gemini/enterprise/docs/ms-onedrive)
* [Google Drive](https://docs.cloud.google.com/gemini/enterprise/docs/gdrive)
* [Google Calendar](https://docs.cloud.google.com/gemini/enterprise/docs/gcal)
* [Gmail](https://docs.cloud.google.com/gemini/enterprise/docs/gmail)

**Public Preview**

* [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/jira-cloud)
* [Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/confluence-cloud)
* [Box](https://docs.cloud.google.com/gemini/enterprise/docs/box)
* [Microsoft Teams](https://docs.cloud.google.com/gemini/enterprise/docs/ms-teams)
* [Dropbox](https://docs.cloud.google.com/gemini/enterprise/docs/dropbox)
* [ServiceNow](https://docs.cloud.google.com/gemini/enterprise/docs/servicenow)

---
## 2025-12-11

### Feature

**Gemini Enterprise: Monitor metrics for NotebookLM Enterprise**

Admins can monitor NotebookLM Enterprise metrics in the **Agents**
tab of the **Analytics** page. For more information, see
[Metrics definitions](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics#definitions).

### Feature

**Google NotebookLM Enterprise: Gemini model upgrade (Preview)**

You can use Gemini 2.5 Flash with NotebookLM Enterprise.

---
## 2025-12-08

### Feature

**Gemini Enterprise: Share custom agents registered with Gemini Enterprise (Preview)**

Admins can share custom agents registered with Gemini Enterprise, including
Agent-to-Agent (A2A), Agent Development Kit (ADK), Dialogflow agents,
and agents added from Google Cloud Marketplace.
For more information, see
[Share custom agents](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents).

---
## 2025-12-05

### Feature

**Gemini Enterprise: Add agents from Google Cloud Marketplace (Preview)**

Admins can add agents from Google Cloud Marketplace that use the
Agent-to-Agent (A2A) protocol. After an agent is purchased and added to
Gemini Enterprise, end users can access the agent through the Gemini Enterprise
web app. For more information, see
[Add and manage agents from Google Cloud Marketplace](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-marketplace-agents).

---
## 2025-11-21

### Feature

**Gemini Enterprise: Use Nano Banana Pro for image generation (Preview)**

You can use Nano Banana Pro (Gemini 3 Pro Image) in Preview with
Gemini Enterprise for image generation. To make this available to users in your
Gemini Enterprise app, a Gemini Enterprise
admin must select **Gemini 3 Pro Image (Preview)** in the
**Enable image generation** feature control. For more information about feature
controls, see
[Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

### Feature

**Gemini Enterprise: Manage agents (Preview)**

Using the Agents page, admins can see all agents that are available to users in
the Gemini Enterprise web app. For more information, see
[Agents overview](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview).

### Feature

**Gemini Enterprise: Save information as memories**

You can ask the assistant to save and remember specific pieces of
information for reference in future conversations. For more information, see
[Save information as memories](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization#save-memories).

---
## 2025-11-19

### Feature

**Gemini Enterprise: Enhanced Agent Designer with visual flow builder (Preview)**

Agent Designer in Gemini Enterprise is enhanced with a new visual flow
builder, offering a more intuitive and powerful way to create and manage
complex, multi-step agents.

For more information, see [Agent Designer overview](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer).

To enable this feature for your users, a Gemini Enterprise administrator must
enable the corresponding toggle in your app's feature management settings. For
information about feature controls,
see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

**Note:** The visual flow builder is available for all new agents created after this release. Existing agents
will continue to use the familiar editor to ensure backward compatibility.

---
## 2025-11-18

### Feature

**Gemini Enterprise: Use Gemini 3 Pro (Preview)**

You can use Gemini 3 Pro in preview with Gemini Enterprise. To make
Gemini 3 Pro available to users in your
Gemini Enterprise app, a Gemini Enterprise admin must enable the
**Gemini 3 Pro (Preview)** toggle in the **Model availability**
feature control. For more information on feature controls, see
[Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

### Feature

**Gemini Enterprise: Sources from model**

In the Sources panel of an answer, Gemini Enterprise shows other sources used by the Gemini models.

### Feature

**Gemini Enterprise: Microsoft OneDrive @mentions**

You can use the @ symbol within your chats to mention and reference files in the connected Microsoft OneDrive data sources.

### Feature

**Gemini Enterprise: View generated images and videos**

You can view chats and download your generated images and videos using the Library. For more information, see
[View and download generated images and videos](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze#view_and_download_generated_images_and_videos).

---
## 2025-11-17

### Feature

**Gemini Enterprise: Register ADK and A2A agents**

You can register your ADK agents that are hosted on the Vertex AI Agent
Engine and your agents that were built using the Agent-to-Agent (A2A) protocol
with Gemini Enterprise. This makes the agents available to your users on the
Gemini Enterprise web app.

For more information, see:

* [Register and manage ADK agents hosted on the Vertex AI Agent Engine](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent)
* [Register and manage A2A agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent)

### Changed

**Gemini Enterprise: Authorize assistant actions from the chat box**

If actions are enabled for a data source, the user sees an **Enable Actions**
button next to the data source listing in the assistant chat box. The user must
click this button and complete authorization before they can use the assistant
actions associated with the data source.

---
## 2025-11-05

### Feature

**Gemini Enterprise: Layout parser support for DOCX, PPTX, and XLSX (GA)**

With the layout parser, support for parsing DOCX, PPTX, and XLSX file formats is
Generally Available (GA). Both the layout and digital parsers can parse PDF,
HTML, DOCX, PPTX, and XLSX files.
For more information about the parsers, see [Parse and chunk
documents](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents).

---
## 2025-10-31

### Feature

**Gemini Enterprise: Hidden model thinking details**

When generating an answer, the details of a model's thinking are always hidden
to protect sensitive information.

---
## 2025-10-21

### Changed

**Gemini Enterprise: Select individual connector instance**

Select or deselect specific connector instances, such as Jira or Confluence, using the 
database
 icon located in the chat box.

---
## 2025-10-02

### Feature

**Google Agentspace: Configure prompt chips**

You can create, delete, edit, and enable or disable Google-provided and custom prompts that provide better guidance to your users.

For more information, see [Configure prompt chips](https://cloud.google.com/agentspace/docs/configure-prompt-chips).

### Feature

**Google Agentspace: Generate images using Nano Banana (GA)**

Image generation and editing with Nano Banana (Gemini 2.5 Flash Image) is generally available (GA) in Google Agentspace across Global, EU, and US multi-regions.

For more information on generating images, see [Generate an image](https://cloud.google.com/agentspace/docs/assistant-analyze#generate_an_image).

---
## 2025-09-26

### Feature

**Google Agentspace: Manage image and video generation on the web app**

By default, image and video generation are enabled in the Agentspace web app. To turn off these features, admins must navigate to the **Configurations > Feature Management** tab, and turn off the **Enable video generation** and **Enable image generation** options.

---
## 2025-09-24

### Feature

**Google Agentspace: Knowledge base filter for catalog entities in ServiceNow connectors (GA)**

In your ServiceNow connectors, you can filter your knowledge base entities by catalog IDs. This lets you selectively ingest only those catalog entities whose `catalogSysId` matches the filter.
If no values are specified, then the connector ingests all catalog entities. This feature is Generally available (GA).

For information about ServiceNow connectors, see [Connect ServiceNow](https://cloud.google.com/agentspace/docs/connect-servicenow).

### Changed

**Google Agentspace: Interface updates**

* File uploads can be canceled at any time.
* The Star and Share buttons now appear after a user has initiated a session by submitting a prompt.

---
## 2025-09-23

### Breaking

**Google Agentspace: Change in ACLs for incidents in ServiceNow**

The access-control list (ACL) behavior for ServiceNow incidents has significantly changed, from too permissive to least-privilege behavior. This change drastically reduces the possibility of data leaks, but might be too restrictive for your needs.

For more information about ServiceNow, see [Connect ServiceNow](https://cloud.google.com/agentspace/docs/connect-servicenow) and [Add ServiceNow actions](https://cloud.google.com/agentspace/docs/assistant-actions-servicenow).

---
## 2025-09-15

### Feature

**Google Agentspace and Google NotebookLM Enterprise: Model Armor**

Model Armor helps proactively screen prompts and responses within Agentspace apps and NotebookLM Enterprise instances. For more information on how administrators can enable this feature, see:

* [Enable Model Armor in Google Agentspace](https://cloud.google.com/agentspace/docs/enable-model-armor)
* [Enable Model Armor in NotebookLM Enterprise](https://cloud.google.com/agentspace/notebooklm-enterprise/docs/enable-model-armor)

### Feature

**Google Agentspace: Real-time sync (Public preview)**

Real-time sync uses webhooks to receive notifications when data is created, updated, and deleted in a third-party data source. Notifications typically arrive within minutes of the event. The following data stores support real-time sync:

* [Jira Cloud](https://cloud.google.com/agentspace/agentspace-enterprise/docs/connect-jira-cloud#enable_real-time_sync)
* [Confluence Cloud](https://cloud.google.com/agentspace/agentspace-enterprise/docs/connect-confluence-cloud#enable_real-time_sync)
* [Microsoft OneDrive](https://cloud.google.com/agentspace/agentspace-enterprise/docs/connect-onedrive#real-time-sync)
* [Microsoft SharePoint Online](https://cloud.google.com/agentspace/agentspace-enterprise/docs/connect-sharepoint-online#real-time-sync)
* [ServiceNow](https://cloud.google.com/agentspace/agentspace-enterprise/docs/connect-servicenow#real-time-sync)

Support for real-time sync for these data stores is in Public preview.

---
## 2025-09-11

### Changed

**Google Agentspace: Interface updates**

* The LLM model selector has moved from the search bar to directly below the product logo in the top-left corner.
* The web grounding tool and source has been renamed *Google Search* and *Enterprise web search,* depending on the type of web grounding configured.
* The *Sources* button in the search bar has been renamed *Data.*
* The *Data* menu (formerly *Sources*) now shows which sources are selected.

---
