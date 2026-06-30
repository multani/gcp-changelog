# Gemini Enterprise

## 2026-06-29

### Feature

**Gemini Enterprise: Jira Data Center federated data store**

The Jira Data Center federated data store is generally available (GA) in
Gemini Enterprise.

For more information, see
[Jira Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc).

### Feature

**Gemini Enterprise: Action-filtering support for Microsoft SharePoint and OneDrive data stores (Preview)**

Filters configured on Microsoft SharePoint and Microsoft OneDrive federated data stores apply to both search queries and action execution. These filters let you specify which SharePoint sites and OneDrive paths are accessible to the Assistant; mutations or retrievals on out-of-scope data fail or return no results.

This feature is in Public Preview. For more information, see:

* [Set up a Microsoft SharePoint data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/set-up-data-store) and [Add filters to a Microsoft SharePoint data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/add-filters-to-sharepoint-data-store)
* [Set up a Microsoft OneDrive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/set-up-data-store) and [Add filters to a Microsoft OneDrive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/add-filters-to-onedrive-data-store)

### Feature

**Gemini Enterprise: HubSpot federated data store**

The HubSpot federated data store is generally available (GA) in Gemini
Enterprise.

For more information, see [Set up a HubSpot data
store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/hubspot/set-up-data-store).

---
## 2026-06-26

### Feature

**Gemini Enterprise: Confluence Data Center federated data store**

The Confluence Data Center federated data store is generally available
(GA) in Gemini Enterprise.

For more information, see
[Confluence Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc).

---
## 2026-06-25

### Feature

**Gemini Enterprise: Governance for agents and MCP servers**

You can access Agent Registry from within Gemini Enterprise. Agent Registry
provides a catalog of agents and custom Model Context Protocol (MCP) servers.
From the catalog, you can select A2A agents or MCP servers to add to your Gemini
Enterprise apps.

Furthermore, through egress policies managed by Agent Gateway, you can set
allow and deny permissions on traffic going to these agents or these MCP
servers.

This feature is generally available (GA). For more information, see:

* [Import agents from Agent Registry](https://docs.cloud.google.com/gemini/enterprise/docs/import-govern-agent-registry) and
* [Import custom MCP servers from Agent
  Registry](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/import-govern-mcp-server-agent-registry).

### Feature

**Gemini Enterprise: New data store and support for new actions (Public Preview)**

The Lovable data store is available in Public Preview in Gemini Enterprise. End
users can search and read projects, and use natural language commands to perform
actions, including adding connectors, remixing projects, and setting project
knowledge and visibility. For more information, see
[Connect Lovable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/lovable).

Additionally, support for new actions is available in Public Preview for the
following data stores:

* [Airtable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airtable): Create bases, fields, tables, and
  record comments; update tables.
* [Freshservice](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice): Create tickets; place
  service catalog item requests.
* [Google Stitch](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/googlestitch): Create and apply design
  systems.
* [Zoho Desk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohodesk): Create and update calls; send
  replies; update tasks.
* [Zoho Projects](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohoprojects): Create projects and
  tasks; update task lists.

For more information, see
[Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

### Feature

**Gemini Enterprise: View agent identity**

This feature is generally available (GA).
As a Gemini Enterprise administrator, you can view an agent's identity on the
Agent details page. This is typically the agent's SPIFFE ID.

If the SPIFFE ID is not published, the Agent Registry resource ID is displayed
as a fallback. For more information, see [Agent
identity](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview#agent-identity).

---
## 2026-06-24

### Feature

**Gemini Enterprise: Observability for agents (GA)**

Observability for Gemini Enterprise is now generally available (GA). This
includes:

* Configuring observability settings at the app level and for individual
  agents.
* Viewing metric dashboards in Metrics Explorer and on the agent's
  **Metrics** tab.
* Viewing trace spans in Trace Explorer and on the agent's **Traces** tab.

For more information, see:

* [Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings)
* [Access metrics](https://docs.cloud.google.com/gemini/enterprise/docs/access-metrics)
* [Access traces and spans](https://docs.cloud.google.com/gemini/enterprise/docs/access-traces-and-spans)

---
## 2026-06-23

### Feature

**Gemini Enterprise: Observability settings for Deep Research agents (Preview)**

You can now configure observability settings for individual Deep Research
agents, the same way as for Agent Designer employee-made agents. This allows
you to monitor metrics in Metrics Explorer and view trace results in
Trace Explorer for specific Deep Research agents.

Observability for Deep Research agents is enabled via the agent-level
**Observability** toggle, not the app-level toggle used for the Core Assistant
agent.

This feature is in Public Preview. For more information, see
[Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings).

---
## 2026-06-18

### Feature

**Gemini Enterprise: Workflow agents (GA with allowlist)**

You can create, import, update, and use workflow agents in the Gemini Enterprise
web app. These agents are designed to execute a sequence of
steps or actions, which can include a mix of AI automation and human intervention, based on a
configured trigger.

This feature is available as a GA with allowlist. To access this feature,
contact your Google account manager. After your Google Cloud project is added to
the allowlist, a Gemini Enterprise administrator must turn on the **Enable agent designer**
toggle in the web app feature management settings to let users use it.

For more information, see:

* [Manage web app
  features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features)
* [Workflow agents](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer-eap/workflow-agents)
  (You need to be on the allowlist to access the page.)

---
## 2026-06-17

### Feature

**Gemini Enterprise: Create and manage skills (GA with allowlist)**

You can create, import, update, and use skills in the Gemini Enterprise
web app. Skills are reusable custom instructions that help the assistant
perform specific tasks.

This feature is available as a GA with allowlist. To access this feature,
contact your Google account manager. After your Google Cloud project is added to
the allowlist, a Gemini Enterprise administrator must turn on the **Enable skills**
toggle in the web app feature management settings to let users use it.

For more information, see:

* [Manage web app
  features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).
* [Create and manage
  skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills) (You need to be on the allowlist to access the page.)

### Feature

**Gemini Enterprise: Gemini Enterprise app for Slack**

Gemini Enterprise administrators can integrate Gemini Enterprise with Slack to
deliver AI-powered answers and search directly to users in their Slack
workspace. Once integrated, users can interact with Gemini Enterprise through
direct messages and slash commands to receive answers that
incorporate data from all connected data stores.

This feature is generally available (GA). For more information, see
[Configure the Gemini Enterprise app for
Slack](https://docs.cloud.google.com/gemini/enterprise/docs/configure-slack-app).

---
## 2026-06-16

### Feature

**Gemini Enterprise: ServiceNow data store actions and federation**

The ServiceNow data store supports federation and assistant actions in
Gemini Enterprise.

You can connect a ServiceNow site to search and read incidents, change
requests, tasks, and knowledge base articles using natural language. You
can also perform actions, such as creating and updating incidents,
directly from the Gemini Enterprise app.

This feature is generally available (GA). For more information, see
[Connect ServiceNow](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow).

---
## 2026-06-15

### Feature

**Gemini Enterprise: New data stores and support for new actions (Public Preview)**

The following data stores are available in Public Preview:

* [AirOps](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airops)
* [Airtable](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/airtable)
* [Calendly](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/calendly)
* [Dynamics 365](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365)
* [Freshservice](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/freshservice)
* [Google Stitch](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/googlestitch)
* [Intercom](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/intercom)
* [MailerLite](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/mailerlite)
* [Zoho CRM](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohocrm)

Additionally, support for new actions is available for the following data
stores:

* [Smartsheet](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/smartsheet)
* [Wrike](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/wrike)
* [Zoho Projects](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohoprojects)

For more information, see
[Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

### Feature

**Gemini Enterprise: Observability settings for individual agents (Preview)**

You can now configure observability settings for individual agents in
Agent Designer employee-made agents. This allows you to monitor metrics in
Metrics Explorer and view trace results in Trace Explorer for specific
agents.

Observability settings for individual agents are configured inside the
agent-level settings. Previously, observability was only available at the
application level, which applies to the Core Assistant agent.

This feature is in Public Preview. For more information, see
[Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings).

---
## 2026-06-12

### Feature

**Gemini Enterprise mobile app: General availability (GA) for Google Identity users**

The Gemini Enterprise mobile app is generally available (GA) for organizations using Google Identity as their identity provider. Users can access their agents, search enterprise data, utilize voice features, and perform interactive actions from iOS and Android devices.

With this release, administrators can display a configuration QR code on the web app homepage to enable user access by scanning the QR code. For organizations using Microsoft Entra ID, access to the mobile app is in GA with allowlist.

To learn more, see [Configure the mobile app](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app) and [Use the mobile app](https://docs.cloud.google.com/gemini/enterprise/docs/use-the-mobile-app).

---
## 2026-06-09

### Feature

**Gemini Enterprise: Share agents with Google Groups**

End users can share agents created using Agent Designer with Google Identity
groups, provided an administrator has enabled this feature for the
Gemini Enterprise app.

This feature is generally available (GA). For more information, see
[Share an agent](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/share-agent).

---
## 2026-06-08

### Announcement

**Gemini Enterprise: Gemini 3.5 Flash feature management toggle is no longer available after June 16, 2026**

Starting June 16, 2026, the Gemini 3.5 Flash feature management toggle is no longer available. This
change applies to the Global, US, and EU multi-regions.

**Note:** This is a correction to the date mentioned previously in the [June 05,
2026 release note](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes#June_05_2026).

---
## 2026-06-05

### Feature

**Gemini Enterprise: Asana data store (Preview)**

The Asana data store is available in Public Preview in Gemini Enterprise.

You can connect an Asana account to search and read projects, workspaces,
teams, and tasks using natural language. You can also perform actions,
such as creating projects and tasks, directly from the Gemini Enterprise app.

For more information, see [Connect Asana](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/asana).

### Announcement

**Gemini Enterprise: Administrator control for Gemini 3.5 Flash**

As a reminder, effective June 9, 2026, the feature management toggle for
Gemini 3.5 Flash is no longer available. Gemini 3.5 Flash
is enabled by default for all users in the Gemini Enterprise app and cannot
be disabled.

This change applies to the Global, US, and EU multi-regions.

**Note:** The effective date has been extended by one day from the [originally
announced schedule](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes#May_26_2026).

---
## 2026-06-03

### Feature

**Gemini Enterprise: DRZ and MLP compliance in the EU for Google NotebookLM Enterprise**

Gemini Enterprise is compliant with data residency (DRZ) and machine learning
processing (MLP) requirements in the EU for Google NotebookLM Enterprise
for adding sources and interacting with the sources (chat). However, the
Discover Sources feature and Studio features, such as audio overview, slide
deck, infographic, video overview, mind map, and reports, are not MLP
compliant.

For more information on location limitations, see [NotebookLM
limitations](https://docs.cloud.google.com/gemini/enterprise/docs/locations#notebooklm-limitations).

---
## 2026-06-02

### Feature

**Gemini Enterprise: Gemini 3 pro image (Nano Banana Pro) and Gemini 3.1 flash image (Nano Banana 2) for image generation**

Gemini 3.1 flash image (Nano Banana 2) and Gemini 3 pro image
(gemini-3.0-pro-image) are generally available (GA) in Gemini Enterprise app.

To make these models available to users in your Gemini Enterprise app, a
Gemini Enterprise administrator can manage them in the feature controls:

* **Gemini 3 pro image (Nano Banana Pro)**: Turned off by default and is only available in the
  Global region.
* **Gemini 3.1 flash image (Nano Banana 2)**: Turned off by default and is only available in the
  Global region. If an administrator turned on this model during
  its Public Preview, it remains turned on in GA in the
  Gemini Enterprise app.

For more information about feature controls, see
[Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

---
## 2026-06-01

### Announcement

**Gemini Enterprise: Agent Designer migration to Gemini 3.5 Flash**

Agent Designer agents in the US and Global regions that previously migrated
from Gemini 2.5 Flash and Gemini 2.5 Pro to
Gemini 3.1 Pro have been migrated to Gemini 3.5 Flash. This
migration is automatic and requires no action.

To use a different model, edit your agent's settings using either
[conversational chat](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/edit-agent#edit-using-chat)
or the [flow builder](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/edit-agent#edit-using-flow).

### Feature

**Gemini Enterprise: Create and edit documents and slides in Canvas**

Canvas is a dedicated, interactive tool within the Gemini Enterprise
web app. It allows you to create and edit AI-generated documents and
presentations directly from your chats. You can then export these to Google
Workspace, Microsoft Office formats, and PDF.

A Gemini Enterprise administrator must turn on the feature so that users can
use it in the Gemini Enterprise app. For more information about feature
controls, see [Manage features on the web
app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

For more information, see
[Create and edit documents and slides in Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas).

---
## 2026-05-28

### Feature

**Gemini Enterprise: Release of Core Assistant (General Availability) and new Trace and Metrics information for Core Assistant (Preview)**

This release includes Core Assistant, a Google-provided ("Made by Google") root
agent that handles interactions when users talk to the Gemini Enterprise app
without specifying any other agent.

Core Assistant is
[Generally Available](https://cloud.google.com/products#product-launch-stages).

Core Assistant includes new observability and monitoring functionality:

* **Traces**: A chronological summary and visualization of trace spans showing execution flow, duration, inputs, outputs, and precise details if OpenTelemetry trace and logging instrumentation is enabled.
* **Metrics**: A default-on dashboard displaying session counts, latency, agent invocations, tool call counts, and error rates without any extra billing costs.

The Trace and Metrics tabs are in
[Public Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Observe and trace agent behavior with Core Assistant](https://docs.cloud.google.com/gemini/enterprise/docs/core-assistant).

---
## 2026-05-27

### Feature

**Gemini Enterprise: Slack data store**

The Slack data store is generally available (GA) in Gemini Enterprise.

You can connect a Slack Workspace to search and read conversations,
files, and messages using natural language. You can also perform actions,
such as sending and scheduling messages, directly from the
Gemini Enterprise app chat box.

For more information, see [Connect Slack](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/slack).

---
## 2026-05-26

### Feature

**Gemini Enterprise: Filter support for Google Sites data stores (Preview)**

You can add Site URL prefix filters to Google Sites data stores in
Gemini Enterprise to include or exclude specific sites from search results.

This feature is in Public Preview. For more information, see
[Add filters to a Google Sites data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gsites/add-filters-to-gsites-data-store).

### Deprecated

**Gemini Enterprise: Gemini Enterprise assist is deprecated**

The Gemini Enterprise assist feature is deprecated and shut down.
Users can now find comprehensive and relevant answers directly in the
Gemini Enterprise documentation.

### Feature

**Gemini Enterprise: Data store for PagerDuty (Preview)**

You can connect PagerDuty data stores to Gemini Enterprise.

Support for PagerDuty data stores is in Public Preview. For more information,
see [Connect PagerDuty](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pagerduty).

### Announcement

**Gemini Enterprise: Administrator control for Gemini 3.5 Flash**

Gemini Enterprise administrators can use the feature management toggle to turn on
or turn off Gemini 3.5 Flash, controlling its visibility in the
Gemini Enterprise app chat box.

The feature management toggle for Gemini 3.5 Flash will not be
available after June 8, 2026. Starting June 8, 2026, Gemini 3.5 Flash
is enabled by default and cannot be turned off for users in the Gemini Enterprise
app.

For more information about feature controls, see
[Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

---
## 2026-05-21

### Feature

**Gemini Enterprise: Create and edit documents and slides in Canvas (Preview)**

Canvas is a dedicated, interactive tool within the Gemini Enterprise
web app. It allows you to create and edit AI-generated documents and
presentations directly from your chats. You can then export these to Google
Workspace, Microsoft Office formats, and PDF.

This feature is in Public Preview. For more information, see
[Create and edit documents and slides in Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas).

---
## 2026-05-20

### Deprecated

**NotebookLM Enterprise: The Podcast API is deprecated**

The [Podcast API](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api) is
deprecated. Google isn't allowlisting new customers.

This feature was available as GA with allowlist.

---
## 2026-05-19

### Feature

**Gemini Enterprise: Data store for Crossbeam (Preview)**

You can now connect Crossbeam data stores to Gemini Enterprise.

Support for Crossbeam data stores is in Public Preview. For more information, see [Connect Crossbeam](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/crossbeam).

### Feature

**Gemini Enterprise: Use Gemini 3.5 Flash (GA)**

Gemini 3.5 Flash is generally available (GA) in the Global, US, and
EU regions with Gemini Enterprise. Users can select it in the model selector
dropdown within the Gemini Enterprise app assistant and in Agent Designer.

As Gemini 3.5 Flash is the current GA Flash model, Gemini 2.5
Flash is removed from the model selector. Administrators can't toggle
Gemini 3.5 Flash off.

For more information about feature controls, see
[Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

### Feature

**NotebookLM Enterprise: Create slide decks and infographics**

You can create slide decks and infographics using
NotebookLM Enterprise. This feature is generally available (GA).
For more information on the usage limits, see [Usage limits](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits).

---
## 2026-05-17

### Feature

**Gemini Enterprise: Agent Designer defaults to Gemini 3.1 Pro for US
and Global regions**

New agents created in Agent Designer use Gemini 3.1 Pro by default
in the US and Global regions. Gemini Enterprise app users can select
Gemini 2.5 Pro or Gemini 2.5 Flash in the agent settings
after creation. Default configurations in other regions where
Gemini 3.1 Pro is not available remain unchanged.

Existing Agent Designer agents in US and Global regions that previously used
Gemini 2.5 Pro or Gemini 2.5 Flash have been migrated to
Gemini 3.1 Pro to provide improved performance. This version of
Gemini 3.1 Pro is in Limited Availability and includes General
Availability (GA) Service Level Objectives (SLOs).
Gemini Enterprise app users can manually revert their agents to
Gemini 2.5 Pro or Gemini 2.5 Flash in the agent settings
if preferred.

For more information on creating agents in Agent Designer, see
[Create an agent](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/create-agent).

---
## 2026-05-15

### Feature

**Gemini Enterprise: New data stores (Public Preview)**

The following data stores are available in Gemini Enterprise:

* [Dice](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dice)
* [Midpage](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/midpage)
* [PandaDoc](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/pandadoc)
* [Smartsheet](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/smartsheet)
* [Wrike](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/wrike)
* [Zoho Books](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohobooks)
* [Zoho Desk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohodesk)
* [Zoho Projects](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zohoprojects)

These data stores are in Public Preview. For more information, see
[Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

---
## 2026-05-13

### Announcement

Correction: **Gemini Enterprise: EU region for Gemini 3 models is coming soon**

The availability of Gemini 3.1 Pro and 3 Flash in the EU region has
been updated to "coming soon". Previously, it was listed as currently available.

For more information, see: [Using Gemini 3.1 Pro and 3 Flash in Limited Availability](https://docs.cloud.google.com/gemini/enterprise/docs/known-limitations#using-gemini-3-preview).

---
## 2026-05-12

### Feature

**Gemini Enterprise: Data store for GitLab (Preview)**

You can now connect GitLab data stores to Gemini Enterprise.

Support for GitLab data stores is in Public Preview. For more information, see [Connect GitLab](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gitlab).

---
## 2026-05-08

### Feature

**Gemini Enterprise: Box data store using data federation**

Connecting a Box data source with Gemini Enterprise using data federation is
generally available (GA).

For more information, see
[Set up a Box data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box/set-up-data-store).

---
## 2026-05-07

### Feature

**Gemini Enterprise: Data store for Google Sites (Preview)**

You can connect Google Sites data stores to Gemini Enterprise.

Support for Google Sites data stores is in Public Preview. For more
information, see [Sync from Google Sites](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-sites).

### Security

**Gemini Enterprise: Multiple API endpoints for the Integration Platform were inadvertently exposed.**

This issue has been resolved, and access has been restricted. No action is required from external customers.

---
## 2026-05-06

### Feature

**Gemini Enterprise: New data stores (Public Preview)**

The following data stores are available in Gemini Enterprise:

* [Mermaid Chart](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/mermaid_chart)
* [Blockscout](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/blockscout)
* [Open Targets](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/open_targets)
* [Apollo GraphOS MCP Tools](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/apollo-graphos)

These data stores are in Public Preview. For more information, see
[Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

---
## 2026-05-05

### Feature

**Gemini Enterprise: New data stores (Public Preview)**

The following data stores are available in Gemini Enterprise:

* [Clinical Trials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/clinicaltrials)
* [Crypto](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/crypto)
* [Excalidraw](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/excalidraw)
* [GoDaddy](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/godaddy)
* [Granted](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/granted)
* [Hugging Face](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/huggingface)
* [Invideo](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/invideo)
* [Kiwi](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/kiwi)
* [LastMinute](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/lastminute)
* [Microsoft Learn](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/microsoft-learn)
* [Trivago](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/trivago)

These data stores are in Public Preview. For more information, see [Connect a
third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

---
## 2026-04-30

### Announcement

**Gemini Enterprise: Access to Gemini 3.1 Pro and 3 Flash in Limited Availability**

Gemini Enterprise users now have access to 3.1 Pro and 3 Flash in Limited Availability. This means that Gemini Enterprise app users will get the generally available Service Level Objectives (SLOs) for these models as part of the Gemini Enterprise Service while the models are in Preview. We are currently monitoring the model's performance and determining the appropriate, long-term (SLOs) and plan to offer these SLOs soon. Additionally, we currently support standard Data Location (Data Residency or "DRZ") commitments in US/EU/global multi-regions.

**Note:** There is a correction to this release note. See [May 13, 2026](#May_13_2026).

For more information, see: [Using Gemini 3.1 Pro and 3 Flash in Limited Availability](https://docs.cloud.google.com/gemini/enterprise/docs/known-limitations#using-gemini-3-preview).

---
## 2026-04-28

### Feature

**Gemini Enterprise: Custom MCP server data stores (Preview)**

You can connect your custom Model Context Protocol (MCP) server with
Gemini Enterprise to securely access your company's private data, custom
internal tools, and MCP-compliant third-party systems.

This feature is turned off by default. To enable it, an Organization Policy
Administrator must remove the organization constraint.

This feature is in Public Preview. For more information, see:

* [Set up your custom MCP server](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server)
* [Override the organization policy for Custom MCP data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-for-custom-mcp-data-stores)

---
## 2026-04-21

### Feature

**Gemini Enterprise: View agent identity (Preview)**

As a Gemini Enterprise administrator, you can view an agent's identity on the
Agent details page. This is typically the agent's SPIFFE ID.

This feature is in Public Preview. If the SPIFFE ID is not published by the
publisher, the Agent Registry resource ID is displayed as a fallback. For more
information, see
[Agent identity](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview#agent-identity).

### Feature

**Gemini Enterprise: Register agents using A2UI and A2A with Gemini Enterprise (Preview)**

Gemini Enterprise administrators can register and manage agents using [Agent to
UI (A2UI)](https://a2ui.org/introduction/what-is-a2ui/) to build custom
interfaces and the [Agent2Agent (A2A) Protocol](https://a2a-protocol.org/) for
communication with Gemini Enterprise.

This feature is in Public Preview. For more information, see:

* [Register and manage agents using A2UI and A2A](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/register-and-manage-an-a2ui-agent)
* [A2UI component gallery reference](https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference)

---
## 2026-04-20

### Feature

**Gemini Enterprise: Request access to Google Cloud Marketplace agents (Preview)**

End users can request access to Google Cloud Marketplace agents from
Agent Gallery. Admins can configure the visibility of these agents,
view purchase requests, and manage access requests.

This feature is in Public Preview. For more information, see:

* [Browse agents with Agent Gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery)
* [Add and manage A2A agents from Google Cloud Marketplace](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-marketplace-agents)

### Feature

**Gemini Enterprise: Register ADK agents hosted on Vertex AI Agent Engine**

You can register ADK agents hosted on Vertex AI Agent Engine with
Gemini Enterprise. This includes agents running within
Vertex AI Agent Engine in a different Google Cloud project. This
feature is generally available (GA).

For more information, see:

* [Register and manage ADK agents hosted on Vertex AI Agent Engine](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent)
* [Configure cross-project ADK agents](https://docs.cloud.google.com/gemini/enterprise/docs/configure-cross-project-adk-agents)

---
## 2026-04-15

### Feature

**Gemini Enterprise: Use Gemini Enterprise Admin and Gemini Enterprise User IAM roles**

Use the Gemini Enterprise Admin and Gemini Enterprise User roles.

The Gemini Enterprise Admin and Gemini Enterprise User roles still map to the
Discovery Engine admin and user roles, so existing customers do not need to make
any changes.

For more information, see [IAM roles and
permissions](https://docs.cloud.google.com/gemini/enterprise/docs/access-control).

---
## 2026-04-14

### Feature

**Gemini Enterprise: New data stores (Public Preview)**

The following data store are available in Gemini Enterprise:

* [Clinical Trials](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/clinicaltrials)
* [Crypto](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/crypto)
* [Excalidraw](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/excalidraw)
* [GoDaddy](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/godaddy)
* [Granted](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/granted)
* [Hugging Face](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/huggingface)
* [Invideo](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/invideo)
* [Kiwi](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/kiwi)
* [LastMinute](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/lastminute)
* [Microsoft Learn](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/microsoft-learn)
* [Trivago](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/trivago)

These data stores are in Public Preview. For more information, see [Connect a
third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

---
## 2026-04-13

### Feature

**Gemini Enterprise: Enhanced filtering for Google Chat data stores (Preview)**

You can configure filters for your Google Chat data stores using either the Google Cloud console or the API. These filters allow you to define exactly which Google Chat data is accessible to the Assistant by including or excluding specific content.

This feature is in Public Preview and is applicable for federated search only. For more information, see [Set up a Google Chat data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/set-up-data-store) and [Add filters to a Google Chat data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/add-filters-to-gchat-data-store).

---
## 2026-04-09

### Feature

**Gemini Enterprise: Support for new actions**

New actions are available for the following data stores:

* [Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook)
* [Salesforce](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce) (Public Preview)

For a list of actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

---
## 2026-04-07

### Feature

**Gemini Enterprise: Dropbox federated data store**

The Dropbox federated data store is generally available (GA) in Gemini Enterprise.

For more information, see [Set up a Dropbox data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox/data-store).

---
## 2026-04-03

### Feature

**Gemini Enterprise: Jira and Confluence federated data stores**

The Jira and Confluence federated data stores are generally available (GA)
in Gemini Enterprise.

For more information, see:

* [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud)
* [Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud)

---
## 2026-04-02

### Feature

**NotebookLM Enterprise: Autocomplete for email addresses and group
names when sharing notebooks**

When sharing notebooks with users and groups, autocomplete is available to help
users quickly select the correct email addresses and group names.

If your organization uses the Google Identity Provider, no action is required.
If your organization uses Third-party identity and Microsoft Entra ID, a
Gemini Enterprise administrator must provision a [System for Cross-domain
Identity Management (SCIM) tenant for
Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim)
to enable autocomplete. For more information
about identity setup, see [Set up
NotebookLM Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm).

This feature is generally available (GA). For more information, see [Share a
notebook](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/share-notebooks).

---
## 2026-04-01

### Feature

**Gemini Enterprise: Data connector request count metric**

Monitor the total number of requests to your Gemini Enterprise data connectors or
data stores using the **Gemini Enterprise DataConnector - Gemini Enterprise
DataConnector Request Count** metric in Metrics Explorer.

This feature is generally available (GA). For more information, see
[Access metrics in Metrics Explorer](https://docs.cloud.google.com/gemini/enterprise/docs/access-metrics).

---
## 2026-03-31

### Feature

**Gemini Enterprise: Support for new actions**
New actions are available for the following data stores:

* [Gmail](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail)
* [Google Drive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive)
* [GitHub](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github) (Public Preview)
* [HubSpot](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/hubspot) (Public Preview)
* [Monday](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday) (Public Preview)

For a list of actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

### Feature

**Gemini Enterprise: Connect Salesforce data using data federation (Preview)**

You can connect Salesforce data stores to Gemini Enterprise using data
federation.

This feature is in Public Preview. For more information, see
[Connect Salesforce](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce).

### Feature

**Gemini Enterprise: Federated connector error logs in Logs Explorer**

You can view detailed error logs for your federated connectors in
Logs Explorer. These logs include connection problems, data transformation
issues, or API errors.

For more information, see
[Access Gemini Enterprise connector error logs with Cloud Logging](https://docs.cloud.google.com/gemini/enterprise/docs/cloud-logging).

### Feature

**Gemini Enterprise and NotebookLM Enterprise: BSI C5:2020 compliance**

Gemini Enterprise and NotebookLM Enterprise are certified for
[BSI C5:2020](https://cloud.google.com/security/compliance/bsi-c5) compliance.

---
## 2026-03-30

### Feature

**Gemini Enterprise: Include cross-domain documents feature for Google Drive (Preview)**

When configuring a Google Drive data store, the **Include cross-domain
documents** feature lets you search and index documents outside your
organization. Enable this setting during app creation or on the **Manage web app
features** page for existing apps.

This feature is in Public Preview. For more information, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) and [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

---
## 2026-03-26

### Feature

**Gemini Enterprise: Chat with files in the Google Drive connector**

Gemini Enterprise can analyze content and generate answers from CSV, PDF, PPTX,
and XLSX files in the Google Drive connector, eliminating the need to upload
these files to the assistant.

This feature is generally available (GA). For more information, see [Chat with
files in connectors](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#chat_with_files_in_connectors).

---
## 2026-03-24

### Feature

**Gemini Enterprise: Enhanced filtering for Microsoft OneDrive data stores (Preview)**

You can configure filters for your Microsoft OneDrive data stores using either the Google Cloud console or the API. These filters allow you to define exactly which content is accessible to the Assistant by including or excluding specific OneDrive paths.

This feature is in Public Preview. For more information, see [Set up a Microsoft OneDrive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/set-up-data-store) and [Add filters to a Microsoft OneDrive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/add-filters-to-onedrive-data-store).

### Feature

**Gemini Enterprise: Get insights with the Data Insights agent (GA with allowlist)**

The Data Insights agent is a Made by Google agent that provides insights from
your BigQuery data.
This feature is available as a GA with allowlist.
Contact your Google Cloud [sales representative](https://cloud.google.com/contact) to access this
feature.

For more information, see
[Get insights with the Data Insights agent](https://docs.cloud.google.com/gemini/enterprise/docs/data-agent).

---
## 2026-03-23

### Feature

**Gemini Enterprise: Data connector for Docusign (Preview)**

You can connect Docusign data stores to Gemini Enterprise.

Support for Docusign data stores is in Public Preview. For more information,
see [Connect Docusign](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/docusign).

---
## 2026-03-17

### Feature

**Gemini Enterprise: Grace period for license deactivation**

To ensure a smooth transition and prevent service interruptions when a
subscription ends early, we've introduced a one-week (seven days) grace period.
During this time, you can continue to use the service while you transition to a
new subscription.

This feature is generally available (GA). For more information, see [Handle
early termination](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#handle-early-termination).

---
## 2026-03-13

### Feature

**Gemini Enterprise: Enhanced filtering for Microsoft SharePoint data stores (Preview)**

You can now configure filters for your Microsoft SharePoint data stores using
either the Google Cloud console or the API. These filters allow you to define
exactly which content is accessible to the Assistant by including or excluding
specific SharePoint sites.

This feature is in Public Preview. For more information, see [Connect Microsoft
SharePoint Online](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint).

### Feature

**Gemini Enterprise: Search generated images and videos**

You can search your generated images and videos in the Gemini Enterprise
assistant. You can also search for items directly in the Library.

This feature is generally available (GA). For more information, see
[Search your Gemini Enterprise content](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-organize#search-your-gemini-enterprise-content)
and
[View, download, and search generated images and videos](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze#view_download_and_search_generated_images_and_videos).

---
## 2026-03-12

### Feature

**Gemini Enterprise: Observability settings (Preview)**

Gemini Enterprise administrators can enable observability settings to view the
following data from your interactions with the assistant in your
Gemini Enterprise web app:

* View metrics in Metrics Explorer.
* View traces and spans in Trace Explorer.

This feature is in Public Preview. For more information, see
[Manage observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings).

---
## 2026-03-11

### Feature

**Gemini Enterprise: Configure retention period for assistant chats**

Gemini Enterprise administrators can configure the retention period for assistant
chat history. This feature is generally available (GA). For more information,
see [Configure the assistant](https://docs.cloud.google.com/gemini/enterprise/docs/configure-assistant).

### Feature

**Gemini Enterprise: Data connector for Google Chat (Preview)**

You can connect Google Chat data stores to Gemini Enterprise.

Support for Google Chat data stores is in Public Preview. For more information,
see [Connect Google Chat](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat).

### Feature

**Gemini Enterprise: Support for new actions (Preview)**

New actions are available for the following data stores:

* [GitHub](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github)
* [Microsoft SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint)
* [Notion](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion)
* [Shopify](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify)

For a list of actions for these data stores, see [Supported
actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

---
## 2026-03-04

### Fixed

**Gemini Enterprise: Agent Designer model configuration fix**

Fixed an issue in Agent Designer that caused agent model configurations to be
cleared or fail to appear during the transition from Gemini 3 Pro
(Preview) to Gemini 3.1 Pro (Preview).

### Feature

**Gemini Enterprise: Support for new actions (Preview)**

New actions are available for the following data stores:

* [Confluence Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc)
* [Monday](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday)
* [Shopify](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify)
* [Zendesk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk)

For a list of actions for these data stores, see [Supported
actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions). These
actions are in Public Preview.

### Feature

**Gemini Enterprise: Data connector for GitHub (Preview)**

You can connect GitHub data stores to Gemini Enterprise. For more information,
see [Connect GitHub](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github).

This feature is in Public Preview.

### Feature

**Gemini Enterprise: Chat with files in the Microsoft Outlook and Box connectors**

Gemini Enterprise can analyze content and generate answers from email
attachments in the Microsoft Outlook connector and from CSV, PDF, PPTX, and XLSX
files in the Box connector, removing the need to upload these files to the
Gemini Enterprise assistant.

This feature is generally available (GA). For more information, see [Chat with
files in connectors](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#chat_with_files_in_connectors).

---
## 2026-03-03

### Feature

**Gemini Enterprise: Use Veo 3.1 for video generation**

Use Veo 3.1 to generate videos in the Gemini Enterprise web app. Veo 3.1
is replacing Veo 3.0 for video generation. For more information, see
[Generate a video](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze#generate_a_video).

To use this feature, a Gemini Enterprise administrator must turn on **Enable
video generation** setting. For more information about feature controls, see
[Manage features on the web
app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

This feature is generally available (GA).

### Feature

**Gemini Enterprise: Export assistant responses to Google Docs and Google Sheets**

You can export chat responses from the assistant to Google Docs. You can also
export tabular and CSV data from a response to Google Sheets.

This feature is generally available (GA). For more information, see [Export to
Google Docs and
Google Sheets](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#export-responses).

---
## 2026-02-26

### Feature

**Gemini Enterprise: Support for new data stores (Preview)**

The following data stores are supported in Public Preview:

* [HubSpot](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/hubspot)
* [Monday](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/monday)
* [Shopify](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/shopify)

---
## 2026-02-23

### Feature

**Gemini Enterprise: Share agents created using Agent Designer**

The agent sharing feature in Agent Designer is generally available (GA) with the
following enhancements:

* **Direct sharing:** Agent owners can share agents directly with other users
  in their organization without prior admin approval.
* **Configurable admin review:** Admins can turn on or
  turn off the requirement for manual review of sharing requests.
* **Additional sharing controls:** Admins can share agents with
  Google Groups and Workforce Identity Federation (WIF) identity pools.

For more information, see
[Share an agent](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer/share-agent).

### Feature

**Gemini Enterprise: Sharing controls for employee-made agents**

Employee-made agents can share within an organization. Admins can manage how
these agents are shared by using the **Enable agent sharing** and **Enable agent
sharing without admin approval** toggles in the management console.

This feature is generally available (GA). For more information, see [Configure feature
controls](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features#configure_feature_controls).

### Feature

**Gemini Enterprise: Share Google-made agents, custom agents, and employee-made
agents that are registered with Gemini Enterprise**

Admins can share the following agents:

* Google-made agents such as Deep Research.
* Employee-made agents created using Agent Designer.
* Custom agents built using Agent-to-Agent (A2A) and registered with
  Gemini Enterprise.
* Agents developed using Agent Development Kit (ADK) and registered with
  Gemini Enterprise.
* Dialogflow agents that are registered with Gemini Enterprise.
* Agents added from Google Cloud Marketplace

This feature is generally available (GA). For more information, see [Share agents from Google Cloud
console](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents).

---
## 2026-02-19

### Feature

**Gemini Enterprise: Use Gemini 3.1 Pro (Preview)**

You can use Gemini 3.1 Pro in Preview with Gemini Enterprise.
This version replaces Gemini 3 Pro in Preview.

To make Gemini 3.1 Pro available to users in your Gemini Enterprise
app, a Gemini Enterprise admin must enable the
**Gemini 3.1 Pro (Preview)** toggle within the **Model availability**
feature control.

If an admin had previously enabled the **Gemini 3 Pro (Preview)**
toggle, then Gemini Enterprise enables the **Gemini 3.1 Pro (Preview)**
toggle by default too.

For more information about feature controls, see
[Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

### Feature

**Gemini Enterprise: Chat with files in the Microsoft SharePoint connector**

Gemini Enterprise can analyze content and generate answers from XLSX and
CSV files in the Microsoft SharePoint connector, eliminating the need to upload
these files to the assistant. For more information, see
[Chat with files in connectors](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#chat_with_files_in_connectors).

---
## 2026-02-12

### Feature

**Gemini Enterprise mobile app: Standard and Plus editions (Private GA)**

The Gemini Enterprise mobile app is available in Private GA. The mobile app lets
users interact with organizational data, engage with agents, and execute tasks
seamlessly using their mobile device.

To ensure that you have the latest features, security, and best experience, you
may occasionally be required to update your Gemini Enterprise mobile app, or
install a new version. Some updates may be necessary to continue using the app.

Contact your account manager to access the mobile app.

---
## 2026-02-09

### Feature

**Gemini Enterprise: Data connector for Notion (Public preview)**

You can connect Notion data stores to Gemini Enterprise. For more information,
see [Connect Notion](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion).

Support for Notion data sources is in Public preview.

---
## 2026-02-06

### Security

**Gemini Enterprise: Security update**

**CVE-ID:** [CVE-2026-1727](https://nvd.nist.gov/vuln/detail/CVE-2026-1727)

**Vulnerability:** Mitigation for Potential Cloud Storage Namespace Hijacking
("Bucket Squatting")

**Description:** We have addressed a security vulnerability
(CVE-2026-1727) in Gemini Enterprise related to the management of
Cloud Storage bucket names. The issue, commonly known as "bucket squatting," can arise
if an attacker pre-emptively registers a bucket name that Gemini Enterprise
services might be configured to use.

**Potential impact:** Exploitation of this vulnerability can let an attacker
intercept, access, or manipulate data intended for a legitimate
Gemini Enterprise-related Cloud Storage bucket.

**Status:** This vulnerability has been remediated in Gemini Enterprise. We have
enhanced our systems to ensure the integrity and proper ownership of
Cloud Storage resources used by the platform, which prevents this
potential issue.

**Action required:** No action is required from users. The
necessary fixes and safeguards have been automatically deployed to
Gemini Enterprise.

### Feature

**Gemini Enterprise: Welcome emails**

After a user signs in to Gemini Enterprise for the first time, the user receives
a welcome email with tips on how to get the most out of Gemini Enterprise.
Gemini Enterprise admins can turn this feature on or off from the admin settings.

For more information, see [Manage web app
features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

### Feature

**Gemini Enterprise: Data connector for Linear (Public preview)**

You can connect Linear data stores to Gemini Enterprise. For more information,
see [Connect Linear](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/linear).

Support for Linear data sources is in Public preview.

---
## 2026-02-04

### Feature

**Gemini Enterprise and NotebookLM Enterprise: Usage audit logs available in Cloud Logging**

Gemini Enterprise admins can access user query and response audit logs in
Cloud Logging for both Gemini Enterprise and NotebookLM Enterprise.

For more information, see:

* [Configure usage audit logging for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/set-up-usage-audit-logs)
* [Configure usage audit logging for NotebookLM Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-usage-audit-logs-for-nblme)

---
## 2026-02-02

### Feature

**Fine-grained access control for individual Gemini Enterprise apps**

Gemini Enterprise admins can control access to individual Gemini Enterprise apps
using app-level IAM policies. IAM permissions are often managed at the project
level, but app-level IAM allows for more granular control.

For more information, see [Configure access controls for apps](https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps).

---
## 2026-01-30

### Feature

**Gemini Enterprise: Support for new actions (Preview)**

New actions are available for the following data stores:

* [Jira Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc)
* [Zendesk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk)

For a list of actions for these data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

---
## 2026-01-28

### Feature

**Gemini Enterprise: Support for new data stores (Preview)**

The following data stores are supported in Gemini Enterprise:

* [Confluence Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc)
* [Jira Data Center](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc)
* [Zendesk](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk)

**Download file** action has been added to [Dropbox](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox). For a list of actions for all available data stores, see [Supported actions](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source#supported_actions).

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

The Agent Designer visual flow builder is available for all agents created
before January 12, 2026. You can manage these agents directly from the
[Agent Gallery](https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery) page, or edit their logic
using the enhanced visual flow builder from the **Agent Designer > Flow** tab.

For more information, see [Agent Designer overview](https://docs.cloud.google.com/gemini/enterprise/docs/agent-designer).

---
## 2026-01-23

### Feature

**Gemini Enterprise: New actions in the unified view (Preview)**

New actions have been added to the following data stores:

* [Box](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box)
* [Confluence Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud)
* [Dropbox](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox)
* [Jira Cloud](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud)
* [Microsoft OneDrive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive)
* [Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook)
* [Microsoft SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint)

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
