# Gemini Enterprise

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
