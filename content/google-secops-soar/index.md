# Google SecOps SOAR

## 2025-09-28

### Announcement

Release 6.3.63 is being rolled out to the first phase of regions, as outlined in our [Google SecOps release plan](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains the following changes:

### Feature

**Podman support for Remote Agents**

You can now install a Remote Agent using Podman. This new functionality provides a streamlined deployment workflow—a lightweight alternative to existing installation methods.

For more information, see [Deploy an agent with Podman](https://cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-podman).

### Feature

**Deploy an agent with Debian**

You can now install a Remote Agent using Debian. This new functionality provides a streamlined deployment workflow—an alternative to existing installation methods.

For more information, see [Deploy an agent with Debian](https://cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-on-debian).

### Announcement

Remote Agent, Release 2.5.0 contains the following changes:

### Changed

**Increased Alert Trimming limit for Remote Agent**

The default setting for Alert Trimming has been increased to 25 MB.

### Changed

**Publisher Connector package size limit enforced**

The maximum allowed size for a Publisher's Connector Package is now limited to 25 MB.

---
## 2025-09-27

### Announcement

[Release 6.3.62](https://cloud.google.com/chronicle/docs/soar/release-notes#September_16_2025) is now available for all regions.

---
## 2025-09-17

### Feature

**SentinelOneV2**: Version 41.0

* The following new action has been added:

  + **Update Alert**
* The following new connector has been added:

  + **SentinelOne - Alert Connector**
* A new predefined widget has been added to the following action:

  + **Update Alert**

### Feature

**Google Threat Intelligence**: Version 4.0

* The following new action has been added:

  + **Set DTM Alert Analysis**

### Feature

**Palo Alto Cortex XDR**: Version 18.0

* The following new actions have been added:

  + **Add Comment To Incident**
  + **Execute XQL Search**
  + **Get Incident Details**

### Changed

**Google Threat Intelligence**: Version 4.0

* Updated the processing of the threat actor entity in the following action:

  + **Enrich Entities**
* Updated the predefined widget in the following actions:

  (REGRESSIVE) The widget now works with GTI information. To see the changes, the widget must be re-added to the existing views in playbooks.

  + **Enrich Entities**
  + **Enrich IOCs**
* Added JSON samples to the following action:

  + **Enrich Entities**

### Changed

**Trend Vision One**: Version 6.0

* Added support for Agent UUID in the following actions:

  + **Enrich Entities**
  + **Execute Custom Script**
  + **Isolate Endpoint**
  + **Unisolate Endpoint**

### Changed

**Splunk**: Version 58.0

* Updated the alert processing logic in the following connector:

  + **Splunk ES - Notable Events Connector**

### Changed

**Jira**: Version 48.0

* **Integration**: Updated the SDK version.

### Changed

Added the ability to modify the `API Root` and `Login API Root` in the following integrations:

* **Azure Active Directory**: Version 18.0
* **Azure AD Identity Protection**: Version 7.0
* **Microsoft Teams**: Version 28.0

### Changed

**Vertex AI**: Version 4.0

* **Integration**: Increased the default timeout for API requests.

### Changed

**Microsoft Azure Sentinel**: Version 56.0

* Updated mapping for the `ScheduledAlert` event types in the following connector:

  + **Microsoft Azure Sentinel Incident Connector v2**

---
## 2025-09-16

### Announcement

**Migrate SOAR to Google Cloud**

All customers and partners are being migrated from SOAR to Google Cloud. For more information, see [SOAR migration overview](https://cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp) and [FAQ](https://cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-faq).

### Announcement

Release 6.3.62 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains internal and customer bug fixes.

---
## 2025-09-15

### Announcement

[Release 6.3.61](https://cloud.google.com/chronicle/docs/soar/release-notes?hl=en#September_07_2025) is now available for all regions.

---
## 2025-09-07

### Announcement

Release 6.3.61 is being rolled out to the first phase of regions, as outlined in our [Google SecOps release plan](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains the following features:

### Feature

**Advanced job scheduling**

The job scheduling functionality has been enhanced with advanced options. This functionality provides more precise control and flexible, calendar-like scheduling for your scripts.

For more information, see [Configure a new job with advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling).

### Feature

**Use custom fields in the Close Case dialog**

Administrators can now add custom fields to the **Close Case** dialog. This new functionality provides a more streamlined workflow and replaces the **Dynamic Fields** feature.

For more information, see [Use custom fields in the Close Case dialog](https://cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/custom-fields-in-case-closure).

---
## 2025-09-06

### Announcement

[Release 6.3.60](https://cloud.google.com/chronicle/docs/soar/release-notes#August_31_2025) is now available for all regions.

---
## 2025-09-03

### Changed

**Google Threat Intelligence**: Version 3.0

* Extended supported filters in the following connector:

  + **Google Threat Intelligence - ASM Issues Connector**

---
## 2025-08-31

### Announcement

Release 6.3.60 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains internal and customer bug fixes.

---
## 2025-08-30

### Announcement

[Release 6.3.59](https://cloud.google.com/chronicle/docs/soar/release-notes#August_23_2025) is now available for all regions.

---
## 2025-08-27

### Feature

**Google Workspace**: Version 20.0

* The following new actions have been added:

  + **Block Extension**
  + **Delete Extension**
  + **Get Extension Details**
  + **Get Host Browser Details**
  + **Search User Activity Events**

### Changed

**Google Threat Intelligence**: Version 3.0

* **Integration:** Updated authentication flow.

---
## 2025-08-23

### Announcement

Release 6.3.59 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains internal and customer bug fixes.

---
## 2025-08-22

### Announcement

[Release 6.3.58](https://cloud.google.com/chronicle/docs/soar/release-notes#August_17_2025) is now available for all regions.

---
## 2025-08-17

### Announcement

Release 6.3.58 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains internal and customer bug fixes.

---
## 2025-08-16

### Announcement

[Release 6.3.57](https://cloud.google.com/chronicle/docs/soar/release-notes#August_10_2025) is now available for all regions.

---
## 2025-08-10

### Announcement

Release 6.3.57 is being rolled out to the first phase of regions, as outlined in our [Google SecOps release plan](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains the following features:

### Feature

**Expression Builder enhancements**

The **Expression Builder** has been enhanced with a new set of pre-built filters to help streamline query creation.

We've improved the information within the platform for all filters, both new and existing. The supporting documentation provides clearer descriptions and practical examples for each transformer, making it easier to understand their purpose and syntax.

For details, see [Use the Expression Builder](https://cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder).

### Feature

**Remote agent notifications**

Agent notifications will alert you to new remote agent version releases and agent downtime based on your permissions and associated environments. Agent notifications are now enabled by default. You can opt out of these notifications at any time from your user preferences.

For details, see [Agent notifications](https://cloud.google.com/chronicle/docs/soar/working-with-remote-agents/what-is-a-remote-agent#agent-notifications).

---
## 2025-08-09

### Announcement

[Release 6.3.56](https://cloud.google.com/chronicle/docs/soar/release-notes#August_3_2025) is now available for all regions.

---
## 2025-08-03

### Announcement

Release 6.3.56 is rolling out to the first phase of regions, as outlined in our [Google SecOps release plan](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release includes the following features:

### Feature

**Automated retries for failed playbook actions**

This feature is in Preview.

Playbook functionality now supports automatic retries for individual actions that encounter temporary issues, such as network outages, API rate limits, or service unavailability. You can define the number of retry attempts and the intervals between retries directly at the step level within playbooks.

For more information on configuring and using action retries, see [Configure action retries in playbooks](https://cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/retry-actions).

### Feature

**Custom Fields Form widget is now supported in Playbook View**

The **Custom Fields Form** widget is now supported in Playbook View.

---
## 2025-08-02

### Announcement

[Release 6.3.55](https://cloud.google.com/chronicle/docs/soar/release-notes#July_27_2025) is now available for all regions.

---
## 2025-07-27

### Announcement

Release 6.3.55 is being rolled out to the first phase of regions, as outlined in our [Google SecOps release plan](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains the following features:

### Feature

**Automate tasks with Playbook Loops**

This feature is in Preview.

Playbook functionality has been enhanced to include **Playbook Loops**. This feature update lets playbooks iterate over lists or entities, performing one or more actions for each item. It streamlines automation by eliminating the need for duplicated steps or custom actions when processing multiple items. You can configure Playbook Loops directly within a playbook or inside a playbook block.

For setup instructions and use case examples , see [Automate tasks with Playbook Loops](https://cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-loops).

### Feature

**Playbook Simulator enhancements for loops**

The Playbook Simulator now supports visualization and debugging of playbooks that contain loops. This lets you clearly see and navigate through each loop iteration within the simulator viewer.

Additionally, the step display order has been updated to show actions from top to bottom (oldest at the top, newest at the bottom), with automatic scrolling to the most recent activity.

For more details, see [Loops in the Playbook Simulator](https://cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-loops#loops-in-the-playbook-simulator).

---
## 2025-07-26

### Announcement

[Release 6.3.54](https://cloud.google.com/chronicle/docs/soar/release-notes#July_20_2025) is now available for all regions.

---
## 2025-07-20

### Announcement

Release 6.3.54 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains internal and customer bug fixes.

---
## 2025-07-19

### Announcement

[Release 6.3.53](https://cloud.google.com/chronicle/docs/soar/release-notes#July_13_2025) is now available for all regions.

---
## 2025-07-13

### Announcement

Release 6.3.53 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains internal and customer bug fixes.

---
## 2025-07-12

### Announcement

[Release 6.3.52](https://cloud.google.com/chronicle/docs/soar/release-notes#July_06_2025) is now available for all regions.

---
## 2025-07-06

### Announcement

Release 6.3.52 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains the following feature:

### Feature

**Share Case Queue Filters**

You can now share case queue filters with other users. These filters can be saved with specific criteria, such as assignee roles, and shared with individual users, SOC roles, or all users in your organization for quick access.

For more information, see [Apply and save filters](https://cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/apply-and-save-filters).

---
## 2025-07-05

### Announcement

[Release 6.3.51](https://cloud.google.com/chronicle/docs/soar/release-notes#June_29_2025) is now available for all regions.

---
## 2025-06-29

### Announcement

Release 6.3.51 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains the following change.

### Changed

**Bulk Playbook Duplication Behavior Updated**

When duplicating playbooks in bulk, the original selection is now preserved. Newly created copies are no longer automatically selected in the platform.

---
## 2025-06-28

### Announcement

[Release 6.3.50](https://cloud.google.com/chronicle/docs/soar/release-notes#June_22_2025) is now available for all regions.

---
## 2025-06-22

### Announcement

Release 6.3.50 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains internal and customer bug fixes.

---
## 2025-06-21

### Announcement

[Release 6.3.49](https://cloud.google.com/chronicle/docs/soar/release-notes#June_14_2025) is now available for all regions.

---
## 2025-06-14

### Announcement

Release 6.3.49 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/release-notes#March_03_2025).

This release contains internal and customer bug fixes.

---
## 2025-06-13

### Announcement

[Release 6.3.48](https://cloud.google.com/chronicle/docs/soar/release-notes#June_07_2025) is now available for all regions.

---
## 2025-06-08

### Announcement

[Release 6.3.47](https://cloud.google.com/chronicle/docs/soar/release-notes#May_24_2025) is now available for all regions.

---
## 2025-06-07

### Announcement

Release 6.3.48 is being rolled out to the first phase of regions.

### Feature

**Playbook Permissions: Support for API Key Roles**

The platform has been updated to extend playbook permissions to also support the SOC Roles associated with API keys, in addition to the user SOC Roles.

This enhancement affects how integrations using API keys interact with playbooks that have specific permission configurations. For example, GitSync now uses this capability to synchronize playbooks with restricted permissions.

For more information on how playbook permissions work with users and API keys, see [Playbook permissions](http://cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-permissions).

For specific instructions on configuring GitSync with restricted playbooks, see [GitSync - Work with playbook permissions](https://cloud.google.com/chronicle/docs/soar/marketplace/power-ups/gitsync#work-with-playbook-permissions).

### Feature

**Advanced Reports: Case Custom Fields**

Advanced Reports (Looker) has been enhanced to include support for custom fields created for Cases.

This enhancement allows users to leverage organization-specific data captured in custom fields to gain deeper insights and create tailored visualizations within Looker reports. Specific LookML formulas and filtering guidance are now available.

For more information on how to use custom fields in Advanced Reports, see [Use Custom Fields in Advanced Reports](https://cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/adding-custom-fields#use-custom-fields-in-advanced-reports).

---
