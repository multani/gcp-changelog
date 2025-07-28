# Google Cloud Contact Center as a Service

## 2025-07-24

### Announcement

**Mobile SDK patch 2.13.1 is released**

This patch fixes an issue where the Android SDK didn't support deep linking in the customizable link format.

---
## 2025-07-10

### Announcement

**Portal version 3.37 pre-release notes**

Here are the pre-release notes for portal version 3.37. When we release version 3.37, we expect the new capabilities to be as shown here.

### Feature

**Restrict email transfers**

You can now configure your instance to prevent users with the agent role from transferring email sessions to other agents. Agents can still assign unassigned emails to themselves, and users with the manager role can still transfer email sessions from agent to agent.

Administrators: There's a new **Transfer Restrictions** pane at **Settings > Queue > Email > Edit / View > [queue] > Transfer Restrictions > Configure**.

### Feature

**Skip the connecting message playback**

You can now configure your instance to skip playback of the connecting message when calls are connected to agents.

Administrators: The **Settings > Call > Call Details** pane contains a new **Skip the Connecting Message playback** checkbox.

### Feature

**Workforce Management terminology update**

We've updated the terminology in the Workforce Management interface to align with Google Cloud CCaaS terminology. For example, we've changed "supervisor" to "manager", "employee" to "agent", and "Supervisor Portal" to "Manager Portal".

### Feature

**Generative knowledge assist is available in Agent Desktop**

Generative knowledge assist is now available in Agent Desktop as a widget that you can drag into a desktop panel.

For more information, see [Create desktop panels](https://cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts).

### Feature

**Generative knowledge assist is available in the agent adapter**

Generative knowledge assist is now available in the agent adapter.

### Feature

**Web SDK version 3.37**

Starting with version 3.37, web SDK releases align with portal releases and share the same version number.

Web SDK version 3.37 includes the following update: we've improved the accessibily of the web SDK to be in compliance with the European Accessibility Act.

### Fixed

The following issues were addressed in this release:

* Fixed an issue where a blank error message box appeared in the agent adapter when a call connected.
* Fixed an issue where the notification icon for a new message or event in the chat adapter didn't clear after the agent viewed the message or event.
* Fixed a Conversational Insights issue where conversation recordings were split into a file for the human agent segment and a file for the virtual agent segment. Now all call segments are aggregated into a single recording file, which is more useful for conversational analysis.
* Fixed an issue where a single call was being reported as two separate calls after the following occurred: (1) A call was escalated from a virtual agent to a queue, (2) An agent clicked **Answer** in the agent adapter, and (3) The end-user hung up before the countdown was complete.
* Fixed an issue where agents were unsure whether their action of declining a call was taking effect. Now, after an agent declines a call, the **Decline** button changes to **Declining...**, the **Answer** button is deactivated, and a message displays indicating that the call was declined.
* Fixed the message that appeared in the agent adapter when an agent left a multi-party session. Instead of saying that the session will be tranferred to the remaining agents(s), the message now says that the session will be transferred to the remaining participant(s). This is because the remaining participants might not be agents.
* Fixed an issue where administators were unable to monitor or barge into calls.
* Fixed an issue where the **Decline** button didn't display or didn't work correctly in the agent adapter when the following occurred: (1) An agent was in an active call, and (2) The agent received a second call on their direct number.
* Fixed an issue where clearing the **Play Call Recording Message** checkbox in **Settings > Call > Call Details** pane didn't work if the queue was configured for human agents and virtual agents or virtual agents only.
* Fixed an issue where the **Transfer failed** error message failed to appear in the call adapter after the following occured: a transferred call wasn't answered before the unanswered call expiration time expired.
* Fixed an issue where an agent on a team that was assigned to a queue wasn't able to select their desired queue to make an outbound call. We also improved the text at **Settings > Call > Call Details > Queue Selection for Outbound Call** to better describe the call adapter behavior.
* Fixed an issue where the missed chat message didn't appear after the missed chat threshold expired.
* Fixed an issue where end-users were unable to download chat transcripts containing special characters, emoji, or redacted content.
* Fixed an issue with the web SDK where configuring custom system messages with empty quotes or NULL values didn't fully suppress the messages.
* Fixed an issue with the web SDK where some non-English characters in downloaded chat transcripts were appearing as question marks.
* Fixed an issue in Hubspot where recordings of transferred calls were failing to save.
* Fixed an issue in Salesforce where the **Call** button in the call adapter wasn't working for outbound calls to a phone number that was associated with a previous record.

---
## 2025-07-08

### Announcement

**Mobile SDK 2.13 is released**

Mobile SDK 2.13 includes the following updates:

* End-users can download chat transcripts to their devices during a session or after a session ends. For more information, see [Download chat transcripts using the web SDK and mobile SDKs](https://cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts#download_chat_transcripts_using_the_web_sdk_and_mobile_sdks).
* The user experience with post-session virtual assistants is improved in the following ways:

  + You can configure an opt-in banner to appear for the post-session virtual assistant experience.
  + The user interface makes it easier for an end-user to know whether they are speaking to a human agent or a post-session virtual agent.
* End-users can navigate the user interface using keyboard shortcuts in conformance with the W3C Web Content Accessibility Guidelines.
* You can configure your instance to let end-users skip customer satisfaction surveys.

### Fixed

The following issues were addressed in this release:

* Android SDK:

  + Fixed an issue where system messages containing an empty space were being sent, even though the message strings were set to NULL.
* iOS SDK:

  + Fixed an issue where the "Skip the human agent" button was displayed after an end-user was transferred to a virtual agent.
  + Fixed an issue where a notification sound played for new chat messages despite the end-user disabling notifications.

---
## 2025-07-07

### Announcement

**Session metadata in Conversational Insights conversations is GA**

The Google Cloud CCaaS capability of including session metadata when creating conversations in Conversational Insights is now [generally available (GA)](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages). Metadata values are available for each conversation. For more information, see [Conversational Insights and Quality AI](https://cloud.google.com/contact-center/ccai-platform/docs/conversational-insights).

---
## 2025-07-02

### Announcement

**Version 3.36 is released**

All release notes published on this date are part of version 3.36.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

### Feature

**Configure storage of Screen Share recordings**

You can now configure how long to store Screen Share recordings in your external storage settings. You can also now store Screen Share recordings that originated from the Screen Share adapter.

Administrators: The **CRM Comments Creation Details** pane at **Settings > Operation Management** has new **Post Cobrowse recording link to CRM record** settings. You need to contact Google support to enable Screen Share recordings.

For more information, see [Set up external storage for CRMs](https://cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage).

### Feature

**Restrict auto-assignment for email queues**

You can now configure email queues so that incoming emails are auto-assigned only during queue operating hours or to agents who are signed in.

Administrators: The **Auto assignment** dialog at **Settings > Queue > Email Edit/View > [queue name] > Automatic assignment > Configure** has two new checkboxes.

For more information, see [Email auto assignment](https://cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#email-auto-assignment).

### Feature

**Salesforce: New closed record options for scheduled calls**

If you've integrated Google Cloud CCaaS with the Salesforce CRM, you can configure how your instance handles scheduled calls for closed records. Here are the configuration options that are available with Salesforce integrations:

* **Don't look up record status**. Your instance doesn't look up record status and makes the scheduled call regardless of whether the record is open or closed.
* **Look up record status and reopen closed records**. Your instance looks up record status before making a scheduled call and reopens records that are closed.
* **Look up record status and cancel scheduled calls for closed records**. Your instance looks up record status before making a scheduled call and cancels scheduled calls for records that are closed.

Administrators: The **CRM Record Creation Details** pane at **Settings > Operation Management** has new settings at **Closed record options when initiating an API-scheduled call**.

For more information, see [Schedule calls with Salesforce](https://cloud.google.com/contact-center/ccai-platform/docs/schedule-calls-salesforce).

### Fixed

The following issues were addressed in this release:

* Fixed an issue where calls weren't being assigned to the correct agent in Google Cloud CCaaS reporting.
* Fixed an issue where calls weren't being assigned to the correct agent in the CRM.
* Fixed an issue where the communication between a virtual task assistant and an end-user was not included in the Agent Assist live transcript in the agent adapter.
* Fixed an issue where agent outbound calls generated incorrect URLs in reporting. URLs contained `ticket` instead of `tickets`.
* Fixed an issue where newly created global contact list destinations were not available in the **Overcapacity Deflection** settings for IVR queues.
* Fixed an issue where the `on_email_thread_created` event listener was mistakenly logging customer names and email addresses.
* Fixed an issue where uploading a new overcapacity deflection message didn't replace the existing message.
* Fixed an issue where agents were not being assigned chat sessions while routing was configured for deltacast.
* Fixed an issue where attachments were lost when: (1) A chat session was transfered to another agent, or (2) After a chat auto-dismissed, an end-user restarted the chat with the same agent in the same queue.
* Fixed an issue where chats didn't time out after being inactive for longer than the chat timeout setting for the queue.
* Fixed an issue where agents who were removed from a chat session using the **Connected Chats** page were not fully disconnected from the session. These agents remained in the conversation tile, couldn't remove themselves from the session, and couldn't receive new chats.
* Fixed an issue where chats initiated outside of working hours generated incorrect chat transcripts. Instead of indicating that the support center was closed, the transcipts indicated that customer support was experiencing high volume.
* Fixed an issue where an external agent and an end-user couldn't communicate after an internal agent did the following: (1) Answered the call, (2) Put the end-user on hold, (3) tranferred the call to a queue with auto redirect to an external number, and (4) failed to release the hold before leaving the call.
* Fixed an issue where end-users with a blocked phone number were able to contact support using chat.
* Fixed an issue where the global disposition list appeared in the chat adapter during wrap-up instead of the disposition list for the agent's queue.
* Fixed an issue where a barge-in event interrupted an agent's audio.
* Fixed an issue where call session recordings were either not being sent to external storage or they were sent in the wrong file format.
* Fixed an issue in advanced reporting dashboards where chats appeared in the chat waiting menu even after the chat sessions ended.
* Fixed an issue where the agent desktop translations in French (Canada) and Japanese were not complete.
* Fixed an issue where the system was generating duplicate After Call Work records for a single wrap-up.
* Fixed an issue where bulk upload containing new users assigned to teams failed.
* Fixed an issue where the chat adapter failed to appear after Nexmo VOIP initialization failed.
* Fixed an issue where saving chat transcripts to a CRM failed.

---
## 2025-06-26

### Announcement

**Web SDK version 3**

We're pleased to announce that the web SDK v3 is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). The web SDK v3 is built on the [headless web SDK](https://cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide), so all of the methods that are available on a headless SDK client are also available with the web SDK v3 widget.

**Deprecation notice**

Starting on **December 31, 2025**, the web SDK v2 will no longer function. Be sure to [update your website](https://cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade) to use the web SDK v3 before that date to avoid breaking your integration with the web SDK. We are no longer adding new features to the web SDK v2.

**Capabilities**

The web SDK v3 provides the following new capabilities:

* **View previous chats and download chat transcripts**. End-users can view previous chats and download chat transcripts from the web SDK widget. For more information, see [View previous chats and download chat transcripts](https://cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts).
* **Web forms**. You can set up HTML web forms to collect data from end-users. For more information, see [Use data collection forms](https://cloud.google.com/contact-center/ccai-platform/docs/use-data-collection-forms).
* **Include conditional operators with proactive chat triggers**. When configuring proactive chat triggers, you can include OR operators with keywords and AND operators with multiple conditions. For more information, see [Proactive Web SDK Triggers](https://cloud.google.com/contact-center/ccai-platform/docs/Chat_Settings_and_Features#UUID-ff948643-7f0c-2db5-ff46-a3e121b180d4).
* **Agents can attach files during chats**. An agent can attach a wide variety of file types using the web SDK widget during a chat session. For more information, see [Configure rich messaging and file attachments](https://cloud.google.com/contact-center/ccai-platform/docs/Chat_Settings_and_Features#rich-messaging).
* **Disable chat audio**. An end-user can disable chat audio using the web SDK widget.
* **System message categorization**. System messages are categorized as standard, confirmation, or error types.
* **Post-session transfers when the end-user ends a session**. Post-session transfers can be triggered when an end-user ends a call or chat session. For more information, see [Post-session transfers](https://cloud.google.com/contact-center/ccai-platform/docs/post-session-transfer).

**Documentation**

Here's the web SDK v3 documentation:

* [Web SDK v3 guide](https://cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-getting-started)
* [Web SDK v3 strings guide](https://cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-strings)
* [Upgrade from web SDK version 2 to web SDK version 3](https://cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade)

**Upgrade**

For help upgrading to web SDK v3, see [Upgrade from web SDK version 2 to web SDK version 3](https://cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade). If you've been using the Private Preview version of web SDK v3, be sure to update your implementations to access `widget.js` from your Google Cloud CCaaS instance.

---
## 2025-06-23

### Announcement

**Version 3.36 pre-release notes**

Here are the pre-release notes for version 3.36. When we release version 3.36, we expect the new capabilities to be as shown here.

### Feature

**Configure storage of Screen Share recordings**

You can now configure how long to store Screen Share recordings in your external storage settings. You can also now store Screen Share recordings that originated from the Screen Share adapter.

Administrators: The **CRM Comments Creation Details** pane at **Settings > Operation Management** has new **Post Cobrowse recording link to CRM record** settings. You need to contact Google support to enable Screen Share recordings.

### Feature

**Restrict auto-assignment for email queues**

You can now configure email queues so that incoming emails are auto-assigned only during queue operating hours or to agents who are signed in.

Administrators: The **Auto assignment** dialog at **Settings > Queue > Email Edit/View > [queue name] > Automatic assignment > Configure** has two new checkboxes.

### Feature

**Salesforce: New closed record options for scheduled calls**

If you've integrated Google Cloud CCaaS with the Salesforce CRM, you can configure how your instance handles scheduled calls for closed records. Here are the configuration options that are available with Salesforce integrations:

* **Don't look up record status**. Your instance doesn't look up record status and makes the scheduled call regardless of whether the record is open or closed.
* **Look up record status and reopen closed records**. Your instance looks up record status before making a scheduled call and reopens records that are closed.
* **Look up record status and cancel scheduled calls for closed records**. Your instance looks up record status before making a scheduled call and cancels scheduled calls for records that are closed.

Administrators: The **CRM Record Creation Details** pane at **Settings > Operation Management** has new settings at **Closed record options when initiating an API-scheduled call**.

### Fixed

The following issues were addressed in this release:

* Fixed an issue where calls weren't being assigned to the correct agent in Google Cloud CCaaS reporting.
* Fixed an issue where calls weren't being assigned to the correct agent in the CRM.
* Fixed an issue where the communication between a virtual task assistant and an end-user was not included in the Agent Assist live transcript in the agent adapter.
* Fixed an issue where agent outbound calls generated incorrect URLs in reporting. URLs contained `ticket` instead of `tickets`.
* Fixed an issue where newly created global contact list destinations were not available in the **Overcapacity Deflection** settings for IVR queues.
* Fixed an issue where the `on_email_thread_created` event listener was mistakenly logging customer names and email addresses.
* Fixed an issue where uploading a new overcapacity deflection message didn't replace the existing message.
* Fixed an issue where agents were not being assigned chat sessions while routing was configured for deltacast.
* Fixed an issue where attachments were lost when: (1) A chat session was transfered to another agent, or (2) After a chat auto-dismissed, an end-user restarted the chat with the same agent in the same queue.
* Fixed an issue where chats didn't time out after being inactive for longer than the chat timeout setting for the queue.
* Fixed an issue where agents who were removed from a chat session using the **Connected Chats** page were not fully disconnected from the session. These agents remained in the conversation tile, couldn't remove themselves from the session, and couldn't receive new chats.
* Fixed an issue where chats initiated outside of working hours generated incorrect chat transcripts. Instead of indicating that the support center was closed, the transcipts indicated that customer support was experiencing high volume.
* Fixed an issue where an external agent and an end-user couldn't communicate after an internal agent did the following: (1) Answered the call, (2) Put the end-user on hold, (3) tranferred the call to a queue with auto redirect to an external number, and (4) failed to release the hold before leaving the call.
* Fixed an issue where end-users with a blocked phone number were able to contact support using chat.
* Fixed an issue where the global disposition list appeared in the chat adapter during wrap-up instead of the disposition list for the agent's queue.
* Fixed an issue where a barge-in event interrupted an agent's audio.
* Fixed an issue where call session recordings were either not being sent to external storage or they were sent in the wrong file format.
* Fixed an issue in advanced reporting dashboards where chats appeared in the chat waiting menu even after the chat sessions ended.
* Fixed an issue where the agent desktop translations in French (Canada) and Japanese were not complete.
* Fixed an issue where the system was generating duplicate After Call Work records for a single wrap-up.
* Fixed an issue where bulk upload containing new users assigned to teams failed.

---
## 2025-06-09

### Announcement

**Salesforce ICU Update**

This is for Google Contact Center as a Service (CCaaS) customers that use Salesforce integration with CCaaS.

On **June 15th, 2025**, Salesforce is rolling out an automatic upgrade to its International Components for Unicode (ICU) locale data. This affects how date, time, number, and currency formatting are handled across Apex, Visualforce, and Lightning components.

This change affects Salesforce integrations that are using Apex API versions earlier than 45.0. These integrations use the legacy Java locale behavior, which could cause formatting discrepancies, incorrect parsing, or runtime errors.

**Solution**

Google has reviewed the CCaaS managed package and has updated the impacted classes to use safe, ICU-compatible parsing and formatting methods. This includes cleaning up legacy code that uses older API versions, which might affect this transition.

The following table shows the affected classes:

**Affected classes**

| Name | API version |
| --- | --- |
| `UJETUtilsController` | 35.0 |
| `UJETUtilsControllerTests` | 35.0 |
| `UJETJWT` | 43.0 |
| `UJETJWTTests` | 43.0 |
| `UJETPageController` | 43.0 |

**Required action**

To ensure compatibility with the Salesforce ICU update and prevent any operational impact, you must complete the following action before **June 15th, 2025**:

* Install the [v1.40 update](https://login.salesforce.com/?ec=302&startURL=%2Fpackaging%2FinstallPackage.apexp%3Fp0%3D04tKk0000011MNw%26InstHostname%3Dlogin.salesforce.com).

This installation updates the affected classes. No further action is required.

**What happens if you don't upgrade?**

If any part of your integration or Apex code uses versions earlier than 45.0 after June 15th, Salesforce will not apply the ICU formatting to those sections. This could potentially lead to issues, including the following:

* Incorrect date and time parsing
* Unexpected errors in workflows or automations
* Mismatch between Lightning and Classic behavior
* Breakage in integrations expecting consistent locale handling

Google considers the affected classes in CC\_AGENT\_APP v1.38 to be safe. While some of the affected classes have legacy methods that are affected by this update, they are not being actively used and will be deprecated in version 1.40. Regardless, Google still recommends installing the v1.40 update. Not upgrading can potentially impact other solutions that are installed on the environment, as described in this communication.

**Defer the update**

As described in [Enable the ICU Locale Formats](https://help.salesforce.com/s/articleView?id=xcloud.icu_migration_enable.htm&type=5), you can defer the automatic rollout of this update.

To defer this update, follow these steps:

1. From the Quick Find search box in **Setup**, enter **User Interface**.
2. On the User Interface page, deselect the **Enable ICU locale formats as part of the scheduled rollout** checkbox.

**Important**: This will only be effective if completed before **June 15th 2025**.

---
## 2025-06-05

### Announcement

**Patch 3.35.15 is released**

This patch does the following:

* Fixes an issue in agent desktop. When an agent had active chat sessions with two end-users simultaneously, the chat history was missing for one of the chats.
* ~~Fixes an issue where bulk user upload jobs on the **Bulk User Management** page got stuck and didn't complete.~~
* Fixes an issue in agent desktop where the chat adapter was unavailable when a chat was received.

---
## 2025-05-28

### Announcement

**Headless web SDK 3.6.5 is released**

This release does the following:

* Fixes an issue where duplicate messages from the virtual assistant appeared in the end-user's chat pane.
* Fixes an issue where end-users were able to reactivate inactive chats outside of operating hours.
* Fixes an issue with data collection forms, where the SDK timed out during the form server's first load attempt, causing a delay in the appearance of the form in the end-user's chat pane.

---
## 2025-05-27

### Announcement

**Version 3.35 is released**

All release notes published on this date are part of version 3.35.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

### Feature

**QM integration now includes chat session events**

You can now export chat session events to an external quality management (QM) system. After you configure the endpoint of your QM system in Google Cloud CCaaS, your chat session events can be streamed to the endpoint in real time.

User experience change:

* The **QM Integration** dialog at **Settings > Developer Settings > Session Data Export > QM Integration** has a new **QM Chat Events - send chat sessions events** checkbox.

For more information, see [QM, SIPREC, and WFM integration](https://cloud.google.com/contact-center/ccai-platform/docs/qm-siprec-integration).

### Feature

**Remove email subject lines from interaction data**

We now support removing email subject lines when you delete interaction data from your instance for specified end-users. The email subjects are removed when you delete data for an end-user in the **Consumer Privacy** dialog at **Settings > Consumer Management > Consumer Privacy**. To completely remove an end-user's data, you must also delete their emails from your mail server. You must also delete chat transcripts, call recordings, and other session-related files from your CRM or external storage, depending on your configuration.

For more information, see [Remove subject lines from end-user email interactions](https://cloud.google.com/contact-center/ccai-platform/docs/remove-end-user-data#remove-subject-lines-from-email-interactions).

### Feature

**New sender email with auto-response emails**

You can now configure an outbound-only email address and use it as the sender address for auto-response emails. The outbound-only address is a "no-reply" email address that prevents the receiver from responding.

User experience changes:

* The **Auto-response** dialog at **Settings > Queue > Email > [your-email-queue] > Auto-response** has a new **Sender email** field.
* The **Add an email** dialog at **Settings > Developer Settings > Email Account Management > Email account list > Add email account** has a new **This is an outbound only email account** checkbox.

For more information, see [Configure an outbound-only email account](https://cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#configure-outbound-only-email-account) and [Configure an auto-response email](https://cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#configure-auto-response-email).

### Feature

**Include images in outbound emails**

You can now include images in outbound emails. This includes emails from an agent in an email session and outbound auto-response emails.

User experience change:

* The **Auto-response** dialog at **Settings > Queue > Email > [your-email-queue] > Auto-response** has a new **Insert Image** button.
* The email adapter has a new **Insert Image** button.

For more information, see [Agent email adapter](https://cloud.google.com/contact-center/ccai-platform/docs/email-adapter) and [Configure an auto-response email](https://cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#configure-auto-response-email).

### Fixed

The following issues were addressed in this release:

* Fixed an issue where calls were were being logged as **Call with unknown contact** in HubSpot instead of under the correct contact name.
* Fixed an issue where the client secret couldn't be saved when a user attempted to set up authentication (using either basic authentication or OAuth) for a custom CRM with the **Generic API** CRM lookup method.
* Fixed an issue where the setup dialog for **Find an account by query endpoint** could not be reached due to an authentication error when configuring OAuth for a custom CRM.
* Fixed an issue where calls were being passed to a custom CRM with the incorrect phone number format.
* Fixed an issue for ServiceNow users where records were created for outbound calls despite the agent selecting **Do not create a record** in the call adapter.
* Fixed an issue where a queue did not have access to the global contact list even though it was configured to have access to it.
* Fixed an issue where the **Directory** tab didn't appear when an agent was transferring a call.
* Fixed an issue where the **Voice Campaign** checkbox didn't appear for **Select Call Types** in the **Create Reports** pane, despite the user having the appropriate report access permissions.
* Fixed an issue where agent extension deflection recordings didn't upload after appearing to be successfully uploaded.
* Fixed an issue that occurred when the `@{NEXT_REOPEN_HOUR}` dynamic variable was put in the **Message** field for **After Hour Messaging** in the **Web & Mobile Messages** pane. The variable always resolved as the next time the chat queue opened on the *following* day. This happened even when the next time the chat queue opened was on the *current* day.
* Fixed an issue that occurred when an end-user on the global contact list placed an inbound call to a queue with access to the global contact list turned off. The agent adapter displayed the destination name of the caller, despite access to the global contact list being turned off.
* Extended the search conditions for the **Directory** tab in the agent adapter to include search by an extension number.
* Fixed an issue where the "next open hours" message was incorrect when a chat ended after midnight.
* Fixed an issue where the call transcript failed to continue after an agent returned from hold.
* Fixed an issue where the default disposition list appeared in the agent adapter instead of the custom disposition list, which was configured to appear.
* Fixed an issue where a user with a manager role received a "Not Authorized" error when attempting to use the **Operation Management** and **Disposition Codes** pages.
* Fixed an issue where the `failReason` and `afterHours` fields in the session metadata file were incorrect for chats that failed because they were attempted after hours.
* Fixed an issue where the **Assign agents** button wasn't working for custom after hours deflection and automatic redirection.
* Fixed an issue where the client secret was not saved when configuring OAuth for a custom CRM.
* Fixed an issue where calling the current queue status endpoint of the Manager API intermittently returned a 404 error.
* Fixed an issue where the wrong disposition code list appeared for an agent after transferring a chat to an agent in a different queue.
* Fixed an issue where chat shortcuts were not working in the agent adapter for mobile chats.
* Fixed issues where agents were unable to successfully move beyond the wrap-up state to handle the next call.

---
