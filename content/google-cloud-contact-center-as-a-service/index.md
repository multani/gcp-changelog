# Google Cloud Contact Center as a Service

## 2025-12-06

### Feature

**Cloud Logging for Google Cloud CCaaS is Generally Available**

You can use Cloud Logging to capture logging data and events for your Google
Cloud project. The Logs Explorer displays log entries for your project. You can
use the `contactcenteraiplatform.googleapis.com/ContactCenter` resource type to
filter your results to view only the log entries for Google Cloud CCaaS. For
more information, see [View log
entries](https://docs.cloud.google.com/contact-center/ccai-platform/docs/view-log-entries).

### Announcement

**Google Cloud CCaaS 3.43**

We've released version 3.43 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule
that you have chosen. For more information, see [Deployment
schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

### Feature

**New web SDK event: exited**

We've added the `exited` event to the web SDK. This event triggers when an
end-user exits a chat session after an agent ends the session. For more
information, see
[exited](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-api-reference#exited).

### Feature

**Wait-time virtual agent for calls**

You can now configure a virtual agent to handle incoming calls requiring
escalation to a human agent. The wait-time virtual agent can place an incoming
call into a queue and then provide personalized, interactive updates based on
real-time events that your instance sends to the virtual agent. These events
include estimated wait time, queue position, and agent availability. When an
agent is available, the virtual agent transfers the call. For more information,
see [Wait-time virtual agents for
calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/wait-time-va-calls).

### Fixed

We addressed the following issues in this release:

* Fixed an issue that occurred when a call was connected directly to an agent
  using the agent's extension (either from another agent or from an end-user).
  The system didn't apply the settings of the receiving agent's queue.
* Fixed a web SDK issue where responses from virtual agents displayed markup
  code for headings, bold, italics, etc., instead of the rendered formatting.
* Fixed a web SDK issue where the timeout dialog for chat check-in didn't
  dismiss after a chat session expired.
* Fixed a web SDK issue where an error was incorrectly returned in the browser
  console log.
* Fixed a web SDK issue where the "new message" alert in the chat screen used
  a text color that didn't adequately contrast with the background.
* Fixed an issue where red boxes incorrectly appeared in the chat screen when
  an agent's message was undelivered.
* Fixed an issue where inbound calls were routed incorrectly to agents outside
  of their personal hours of operation.
* Fixed an issue that prevented users from downloading web chat transcripts
  using the **Download** button.
* Fixed an issue that occurred during overcapacity deflection. The "redirect
  to queue" action didn't route calls to the configured Dialogflow menu ID.
* Fixed an issue where virtual agents disconnected calls during after-hours
  deflection or automatic redirection instead of routing them to the
  configured location.
* Fixed an issue where virtual agents incorrectly remained in a
  session if an agent answered a call immediately after an overcapacity
  deflection announcement.
* Fixed an issue where calls didn't end after an end-user selected the
  "message" option during overcapacity deflection.
* Fixed an issue where manually adding users to multiple teams returned an
  error.
* Fixed an issue where administrators couldn't save queue reordering actions
  in the SMS channel.
* Fixed an issue where the BYOC configuration incorrectly overwrote the domain
  of target SIP URIs during outbound calls.
* Fixed an issue that incorrectly returned `Cannot read properties` console
  errors.
* Fixed an issue where a service name was misspelled, which caused errors in
  batch user creation and team assignment.
* Fixed an issue with historical data bulk import where uploading historical
  data without dates generated empty import reports instead of returning an
  error.
* Fixed an issue with historical data bulk import where the system accepted
  and processed data with future dates instead of returning an error.
* Fixed an issue where queue priority sliders for users and teams were
  active when they were configured to be inactive.
* Fixed an issue that prevented languages from being added to an instance.
* Fixed an issue where the agent directory was empty when an agent attempted
  to transfer a call to another agent.
* Addressed latency in Telnyx calls.
* Fixed a billing calculation issue where concurrent agent counts were
  inaccurate.

---
## 2025-12-02

### Fixed

We addressed the following iOS SDK issues in this release:

* Fixed an issue where the **RATE YOUR EXPERIENCE** dialog contained text that
  didn't adequately contrast with the background.
* Fixed an issue where smart action requests from an agent (for example,
  request verification or request photo) triggered push notifications to the
  end-user despite **Allow Push Notifications** being turned off in the
  end-user's app.
* Fixed an issue in the end-user's chat screen where the screen reader
  incorrectly announced that the "We are connecting you, please hold" message
  was a button.

### Feature

**Turn off push notifications at the global level**

You can configure your Android SDK or iOS SDK to turn off push notifications at
the global level. This bypasses all push notification dependencies and prevents
push notifications from reaching end-users. For more information, see the
following:

* **Android SDK**: [SDK
  configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#sdk-configuration)
* **iOS SDK**: [Turn off push notifications at the global
  level](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#turn-off-push-notifications-at-global-level)

### Announcement

**Mobile SDKs version 2.15.0**

We've released version 2.15.0 of the mobile SDKs.

---
## 2025-11-19

### Feature

**Dial pad improvements**

The dial pad in the agent adapter now includes the following:

* Country code selector
* Outbound number, Language, and Queue selectors

If you use a CRM with flexible outbound dialing turned on, the **Outbound
number** and **Language** selectors appear in the **Outbound call details**
screen.

For more information, see [Make an outbound
call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-calls#make-outbound-call).

### Feature

**Sensitive data redaction**

You can now automatically identify and redact sensitive data from chat
conversations, both in real time and in transcripts. This helps to prevent
unauthorized people from accessing sensitive information and can help you comply
with security standards. You can configure redaction for incoming messages from
end-users, outgoing messages from agents, and session notes. You can also let
agents temporarily view redacted messages during a session. This capability is
available for the web SDK.

Administrators: You can find the settings for configuring automatic redaction in
the following locations:

* To add a redaction platform: **Settings > Developer Settings
  > Redaction Platform**
* To configure automatic redaction at the global level: **Settings
  > Chat > Automatic Redaction**
* To configure automatic redaction at the queue level: **Settings >
  Queue > Web > Edit / View > SELECT\_QUEUE
  > Automatic Redaction**

For more information, see [Sensitive data
redaction](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Chat_Settings_and_Features#sensitive-data-redaction).

### Feature

**New standalone queue settings page**

Google Cloud CCaaS now includes a standalone **Queue Menu Settings** page for
each queue in your instance. These pages are separate from (but identical to)
the **Queue Menu Settings** pages at **Settings > Queue >
Edit / View > YOUR\_QUEUE**. The standalone pages load faster and you
can quickly access them in the following ways:

* From the **Queues** page (access this by clicking the **Queues** menu).
  Links to the standalone **Queue Menu Settings** pages are in the **Queue
  Name** column.
* From the **Phone Number Management** pane at **Settings > Call
  > Phone Numbers > Phone number management**. Links to
  the **Queue Menu Settings** pages are in the **Assigned Queues / Agents**
  column.
* Using a URL that identifies the queue. Example:
  `https://YOUR_CCAAS_HOST/queues/QUEUE_ID/LANGUAGE_CODE`

Links to standalone **Queue Menu Settings** pages are active only for users with
permissions to view queue settings. For more information, see [Access queue menu
settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/access-queue-menu-settings).

### Feature

**Chat check-in**

Users of the web SDK can use chat check-in to help ensure that end-users are
present and ready to engage before connecting them to a human agent. This helps
to reduce the time lost when agents wait for end-users who have abandoned a
chat.

When an end-user reaches the front of the chat queue, the system asks if they're
still available. If there's no response after the amount of time you configure,
the system removes the end-user from the queue. If the end-user rejoins the
queue, you can configure whether they rejoin at the front or the back of the
queue.

For more information, see [Chat
check-in](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Chat_Settings_and_Features#chat-check-in).

### Fixed

We addressed the following issues in this release:

* Fixed an issue where Agent Assist generated incomplete or
  inaccurate chat summaries.
* Fixed inaccurate reporting for chats escalated by a virtual agent to a
  human agent.
* Fixed incorrect labeling and routing of French voicemails to the
  English-language queue in the agent adapter.
* Fixed the missed response timer, which added an extra 30 minutes to the
  calculated time.
* Fixed a significant slowdown in background job processing.
* Fixed an issue where the global default voicemail greeting failed to save
  when applied to an individual user's settings.
* Fixed an issue that caused agents to be assigned a call and a chat at the
  same time, even when this was disabled in the settings.
* Fixed an issue that prevented users from testing Android push notifications.
* Fixed an issue where editing a phone number's settings on the **Phone Number
  Management** page removed it from queues where it was assigned for outbound
  calls.
* Fixed an issue that caused a **Custom roles permissions is invalid** error
  when attempting to save a change to the **Audit Dashboard** permission in
  a custom role.
* Fixed an issue that caused the handle time for queued chats to display an
  incorrect value, particularly after a session transfer.
* Fixed an issue where the call ID was missing in the **Activity Timeline**
  report.
* Fixed an issue where the **Auto answered** label on a chat tab in the chat
  adapter persisted even after an agent opened the chat.
* Fixed an issue where the agent directory in the call adapter appeared empty
  when an agent attempted to transfer a call.
* Fixed an issue that prevented an agent from adding another agent to a call
  using their extension number.
* Fixed an agent desktop issue where unsigned data appeared before signed data
  in the **Session Data Feed** panel. This was inconsistent with the display
  order in the agent adapter.
* Fixed an issue at **Settings > Developer Settings >
  CRM > Custom CRM > CRM lookup method >
  Custom Link**. In the **Custom link CRM lookup** section, we replaced the
  incorrect `{Custom UID}` variable name with `{CUID}` in the UI text.
* Fixed a web SDK issue where the **Select an option** channel selection
  screen appeared unnecessarily when a chat started, when the Direct Action
  Parameter was enabled.
* Improved web SDK page loading speed.
* Fixed a web SDK issue where external deflection links weren't working
  correctly.

### Feature

**Restrict the transfer of email sessions to a queue**

You can now configure queues to prevent them from receiving email session
transfers.

Administrators: A new **Allow incoming Email Transfers** toggle appears in the
settings pane at **Settings > Queue > Email >
Edit / View > YOUR\_QUEUE**.

For more information, see [Transfer email sessions to a queue](https://docs.cloud.google.com/contact-center/ccai-platform/docs/let-agents-transfer-email-sessions-to-a-queue).

### Feature

**Alvaria Advanced List Management integration with outbound dialer**

You can now integrate Alvaria Advanced List Management (ALM) with the outbound
dialer. This lets you combine Alvaria's list and campaign management
capabilities with the dialing capability of Google Cloud CCaaS. This integration
exchanges contact and result files through a shared Cloud Storage bucket.

Capabilities:

* Multi-tenancy support: helps ensure that each tenant's data remains separate
  and secure
* Flexible delimiter support: supports files using comma, pipe, tab, or
  semicolon delimiters

For more information, see [Alvaria Advanced List Management
integration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/alvaria-alm).

### Feature

**Email signatures**

You can now define standardized signatures for all outgoing emails sent from a
specific queue.

Administrators: A new **Email Signatures** section appears in the settings pane
at **Settings > Queue > Email > Edit / View
> YOUR\_QUEUE**.

For more information, see [Email signatures](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#email-signatures).

### Feature

**Virtual task assistant support in the chat platform API**

The chat platform API now provides improved support for virtual task assistants.
When an agent transfers a chat to a virtual task assistant, your application can
send and receive messages from the virtual task assistant. Enhanced webhooks
provide the virtual task assistant's message content instantly, streamlining
private, automated workflows like collecting sensitive information.

For more information, see [Use virtual task assistants with the chat API
platform](https://docs.cloud.google.com/contact-center/ccai-platform/docs/task-va-chat-api).

### Feature

**Virtual agent aliases**

You can assign a public-facing alias to each of your virtual agents. When all of
your virtual agents have the same alias, they each appear to have the same name
to end-users. This gives the impression that a single virtual agent is handling
a session even if the session is transferred between virtual agents. You can
assign virtual agent aliases to both support agents and virtual task assistants.
Virtual agent aliases are used in the web SDK, the mobile SDKs, in system
messages, and in transcripts.

Administrators: A new **Virtual Agent Alias** checkbox appears in the following
dialogs:

* The **Add a Customer Support Agent** dialog at **Settings >
  Virtual Agent > Virtual Agents > Add virtual agent
  > Customer Support**
* The **Add a Virtual Task Assistant** dialog at **Settings >
  Virtual Agent > Virtual Agents > Add virtual agent
  > Task Assistant**

For more information, see [Virtual agent
aliases](https://docs.cloud.google.com/contact-center/ccai-platform/docs/use-va-aliases).

### Feature

**New chat platform API endpoint for getting media files**

You can use the new chat platform API endpoint to get the media file that an
agent sends to an end-user during a chat session. Your custom chat application
can then make the media file available to the end-user during the session.

New endpoint: `/apps/api/v1/chats/CHAT_ID/media/MEDIA_ID`

For more information, see [Agent file attachments with the chat platform
API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-attachments-chat-api).

### Announcement

**Google Cloud CCaaS 3.42**

We've released version 3.42 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

---
## 2025-11-17

### Announcement

**Advanced reporting dashboards version 3.41**

We've released version 3.41 of the advanced reporting dashboards.

### Fixed

We addressed the following issues in this release:

* Fixed an issue where the **Chat Agent Metrics (Historical)** explore and the **Agent Metrics (Historical)** explore returned different data for chats handled. This resulted in inconsistent chat handling metrics in dashboards.
* Fixed an issue where ambiguous metrics names appeared in the **Call Queue Metrics (Historical)** explore.
* Fixed an issue where the average active concurrency metric appeared as a total instead of a percentage.
* Fixed an issue where the CSAT values on the **CSAT** and **Agent Performance** dashboards were not consistent with each other.
* Changed the **Caller ANI** table heading to **Consumer phone number** in all of the tables it appeared in.
* Fixed an issue where Call ID on the **Calls Transfer** dashboard was not correctly formatted.
* Fixed an issue where the column headings in the **Agent Productivity** table of the **Agent Performance** dashboard were ordered incorrectly.
* Fixed an issue on the **Dispositions - Chat** dashboard where the **Disposition Codes** filter wasn't working correctly.
* Fixed an issue on the **Dispositions - Chat** dashboard where the **Disposition Code** filter was unable to find existing disposition codes.
* Fixed an issue on the **Dispositions - Chat** dashboard where the **Direction** filter didn't display the available values.
* Fixed an issue on the **Dispositions - Chat** dashboard where the **Agent Name** filter wasn't working correctly.
* Fixed an issue on the **Dispositions - Chat** dashboard where the **Disposition Distribution** tile displayed the disposition codes in the wrong order.
* Fixed an issue on the **Dispositions - Calls** dashboard where the **Disposition Code** filter didn't find existing disposition lists.
* Fixed an issue on the **Dispositions - Calls** dashboard where agents didn't appear in the **Dispositions by Agent** table when filtering by Agent ID.
* Fixed an issue where dismissed chat time was being included with current chat time metrics on the **Agent Monitoring** dashboard.

### Feature

**Campaigns dashboard**

We've added a new **Campaigns** dashboard that displays real-time and historical performance metrics for call campaigns, including call outcomes, campaign volumes, and agent metrics. Managers can use this information to monitor call campaigns and make data-driven decisions to improve campaign performance. For more information, see [Campaigns dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-campaigns).

### Feature

**All Interactions dashboards: updates to tables**

On the **All Interactions - Calls** dashboard, we did the following:

* Renamed the **All Call Interactions (Historical)** table to **Call Metrics Detail**.
* Updated the formatting of the column headings in the **Virtual Agent Interactions** table.

On the **All Interactions - Chats** dashboard, we renamed the **All Chat Interactions (Historical)** table to **Chat Metric Detail**.

For more information, see [All interactions dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-all-interactions).

### Feature

**Real-time dashboard optimization**

We've optimized real-time dashboards to provide faster loading and refresh times.

---
## 2025-11-14

### Fixed

We addressed the following issues in this release:

* Fixed an issue where Agent Assist generated incomplete or
  inaccurate chat summaries.
* Fixed inaccurate reporting for chats escalated by a virtual agent to a
  human agent.
* Fixed incorrect labeling and routing of French voicemails to the
  English-language queue in the agent adapter.
* Fixed the missed response timer, which added an extra 30 minutes to the
  calculated time.
* Fixed a significant slowdown in background job processing.
* Fixed an issue where the global default voicemail greeting failed to save
  when applied to an individual user's settings.
* Fixed an issue that caused agents to be assigned a call and a chat at the
  same time, even when this was disabled in the settings.
* Fixed an issue that prevented users from testing Android push notifications.
* Fixed an issue where editing a phone number's settings on the **Phone Number
  Management** page removed it from queues where it was assigned for outbound
  calls.
* Fixed an issue that caused a **Custom roles permissions is invalid** error
  when attempting to save a change to the **Audit Dashboard** permission in
  a custom role.
* Fixed an issue that caused the handle time for queued chats to display an
  incorrect value, particularly after a session transfer.
* Fixed an issue where the call ID was missing in the **Activity Timeline**
  report.
* Fixed an issue where the **Auto answered** label on a chat tab in the chat
  adapter persisted even after an agent opened the chat.
* Fixed an issue where the agent directory in the call adapter appeared empty
  when an agent attempted to transfer a call.
* Fixed an issue that prevented an agent from adding another agent to a call
  using their extension number.
* Fixed an agent desktop issue where unsigned data appeared before signed data
  in the **Session Data Feed** panel. This was inconsistent with the display
  order in the agent adapter.
* Fixed an issue at **Settings > Developer Settings >
  CRM > Custom CRM > CRM lookup method >
  Custom Link**. In the **Custom link CRM lookup** section, we replaced the
  incorrect `{Custom UID}` variable name with `{CUID}` in the UI text.
* Fixed a web SDK issue where the **Select an option** channel selection
  screen appeared unnecessarily when a chat started, when the Direct Action
  Parameter was enabled.
* Improved web SDK page loading speed.
* Fixed a web SDK issue where external deflection links weren't working
  correctly.

### Feature

**Web SDK: chat check-in**

Users of the web SDK can use chat check-in to help ensure that end-users are
present and ready to engage before connecting them to a human agent. This helps
to reduce the time lost when agents wait for end-users who have abandoned a
chat.

When an end-user reaches the front of the chat queue, the system asks if they're
still available. If there's no response after the amount of time you configure,
the system removes the end-user from the queue. If the end-user rejoins the
queue, you can configure whether they rejoin at the front or the back of the
queue.

### Feature

**New chat platform API endpoint for getting media files**

You can use the new chat platform API endpoint to get the media file that an
agent sends to an end-user during a chat session. Your custom chat application
can then make the media file available to the end-user during the session.

New endpoint: `/apps/api/v1/chats/CHAT_ID/media/MEDIA_ID`

### Feature

**Virtual task assistant support in the chat platform API**

The chat platform API now provides improved support for virtual task assistants.
When an agent transfers a chat to a virtual task assistant, your application can
send and receive messages from the virtual task assistant. Enhanced webhooks
provide the virtual task assistant's message content instantly, streamlining
private, automated workflows like collecting sensitive information.

### Feature

**New standalone queue settings page**

Google Cloud CCaaS now includes a standalone **Queue Menu Settings** page for
each queue in your instance. These pages are separate from (but identical to)
the **Queue Menu Settings** pages at **Settings > Queue >
Edit / View > YOUR\_QUEUE**. The standalone pages load faster and you
can quickly access them in the following ways:

* From the **Queues** page (access this by clicking the **Queues** menu).
  Links to the standalone **Queue Menu Settings** pages are in the **Queue
  Name** column.
* From the **Phone Number Management** pane at **Settings > Call
  > Phone Numbers > Phone number management**. Links to
  the **Queue Menu Settings** pages are in the **Assigned Queues / Agents**
  column.
* Using a URL that identifies the queue. Example:
  `https://YOUR_CCAAS_HOST/queues/QUEUE_ID/LANGUAGE_CODE`

Links to standalone **Queue Menu Settings** pages are active only for users with
permissions to view queue settings.

### Feature

**Automatic redaction**

You can now automatically identify and redact sensitive data from chat
conversations, both in real time and in transcripts. This helps to prevent
unauthorized people from accessing sensitive information and can help you comply
with security standards. You can configure redaction for incoming messages from
end-users, outgoing messages from agents, and session notes. You can also let
agents temporarily view redacted messages during a session. This capability is
available for the web SDK.

Administrators: You can find the settings for configuring automatic redaction in
the following locations:

* To add a redaction platform: **Settings > Developer Settings
  > Redaction Platform**
* To configure automatic redaction at the global level: **Settings
  > Chat > Automatic Redaction**
* To configure automatic redaction at the queue level: **Settings >
  Queue > Web > Edit / View > SELECT\_QUEUE
  > Automatic Redaction**

### Feature

**Virtual agent alias**

You can assign a public-facing alias to each of your virtual agents. When all of
your virtual agents have the same alias, they each appear to have the same name
to end-users. This gives the impression that a single virtual agent is handling
a session even if the session is transferred between virtual agents. You can
assign virtual agent aliases to both support agents and virtual task assistants.
Virtual agent aliases are used in the web SDK, the mobile SDKs, in system
messages, and in transcripts.

Administrators: A new **Virtual Agent Alias** checkbox appears in the following
dialogs:

* The **Add a Customer Support Agent** dialog at **Settings >
  Virtual Agent > Virtual Agents > Add virtual agent
  > Customer Support**
* The **Add a Virtual Task Assistant** dialog at **Settings >
  Virtual Agent > Virtual Agents > Add virtual agent
  > Task Assistant**

### Feature

**Restrict the transfer of email sessions to a queue**

You can now configure queues to prevent them from receiving email session
transfers.

Administrators: A new **Allow incoming Email Transfers** toggle appears in the
settings pane at **Settings > Queue > Email >
Edit / View > YOUR\_QUEUE**.

### Announcement

**Google Cloud CCaaS 3.42 pre-release notes**

Here are the pre-release notes for Google Cloud CCaaS version 3.42. When we
release version 3.42, we expect the new capabilities to be as shown here.

### Feature

**Email signatures**

You can now define standardized signatures for all outgoing emails sent from a
specific queue.

Administrators: A new **Email Signatures** section appears in the settings pane
at **Settings > Queue > Email > Edit / View
> YOUR\_QUEUE**.

### Feature

**Outbound calling improvements**

We've implemented the following improvements to outbound calling:

* **Show dialpad before starting the call**: For CRM users, the **Settings
  > Operation Management > CRM Operations** section
  contains a new **Show dialpad before starting the call** checkbox. When you
  select this checkbox, agents can view the dial pad and make changes before a
  call starts, even if flexible outbound calling is turned off.
* **Dialpad improvements**: The dial pad in the agent adapter now includes the
  following:

  + Country code selector
  + Outbound number, Language, and Queue selectors

  If you use a CRM with flexible outbound dialing turned on, the **Outbound
  number** and **Language** selectors appear in the **Outbound call
  details** screen.

### Feature

**Alvaria Advanced List Management integration with outbound dialer**

You can now integrate Alvaria Advanced List Management (ALM) with the outbound
dialer. This lets you combine Alvaria's list and campaign management
capabilities with the dialing capability of Google Cloud CCaaS. This integration
exchanges contact and result files through a shared Cloud Storage bucket.

Capabilities:

* Multi-tenancy support: helps ensure that each tenant's data remains separate
  and secure
* Flexible delimiter support: supports files using comma, pipe, tab, or
  semicolon delimiters

---
## 2025-11-03

### Feature

**Google Cloud CCaaS 3.41**

We've released version 3.41 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

### Feature

**Nested disposition lists**

You can now organize your disposition lists by grouping them into nested folders, making it easier for agents to find the disposition codes they need. This is available in the agent adapter and the agent desktop.

Administrators: The **Disposition Codes** dialog at **Settings > Operation Management > Wrap-up > Manage Disposition Codes** has a new **Tree** tab.

User experience change: If you've configured nested disposition lists, the **Disposition** screen in the agent adapter displays links to the nested disposition lists.

For more information, see [Configure nested disposition lists](https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-lists-configure).

### Feature

**Virtual agent to virtual agent direct chat transfers**

You can configure Dialogflow payloads to transfer chat sessions from one virtual agent directly to another virtual agent, using the destination virtual agent's agent ID.

For more information, see [Virtual agent to virtual agent direct transfer](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-to-va-transfers#va-to-va-direct-transfer).

### Feature

**Extensions for support numbers**

You can assign a phone number extension to an agent that an end-user can use to directly call the agent. You can also set up an extension directory that end-users can use to find the extension for an agent that they want to call.

Administrators:

* The **Agent Extensions** pane on the **Call** page at **Settings > Call** contains a new **Consumer to Agent Calls** section.
* The **Add new menu** dialog at **Settings > Queue > IVR (Interactive Voice Response) > Menu Structure** contains a new **Extension Directory** toggle.

For more information, see [Turn on and configure agent extensions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#turn-on-and-configure-agent-extensions).

### Feature

**Skip language selection and IVR menu readout**

You can configure your call flow to skip language selection and the IVR menu readout. Instead, callers get the default language and are routed to the default queue. This creates a faster call connection experience for end-users.

Administrators:

* In the **Settings > Languages & Messages > Languages** pane, there's a new **Skip language selection** option.
* In the **Settings > Queue > IVR (Interactive Voice Response) > IVR Queue Menu Readout** section, there's a new **Skip IVR Menu readout** option.

For more information, see [Configure IVR messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/customizing_languages_recordings_messages#configure-ivr-messages).

### Feature

**Transfer an email session to a queue**

Agents can now transfer an email session to a queue. This resolves the problem of multiple email sessions being created when an agent forwards an email directly to an agent to transfer it.

Administrators: The **General** pane on the **Email** page at **Settings > Email** contains a new **Enable Email Transfer Between Queues** checkbox.

User experience change: In the email adapter, a new **Transfer** button appears when an agent views an assigned email.

For more information, see [Let agents transfer email sessions to a queue](https://docs.cloud.google.com/contact-center/ccai-platform/docs/let-agents-transfer-email-sessions-to-a-queue).

### Fixed

We addressed the following issues in this release:

* Fixed an issue where hyperlinks in the after-hours message of the web SDK were broken.
* Fixed an issue where the language selector mistakenly appeared in the chat UI.
* Fixed an issue where an authentication request with an invalid or expired authentication token caused an agent's browser to become unresponsive and crash.
* Fixed an issue where an end-user using the iOS mobile SDK couldn't play a video that they had sent to an agent during a web chat session.
* Fixed an issue for Android mobile SDK users where the **Send** icon in the end-user's chat input field didn't appear correctly.
* Fixed an issue where an instance using an Agent Assist profile with Conversation Summarization disabled incorrectly returned errors.
* Fixed an issue that caused inaccurate virtual agent chat analytics. Affected metrics included `response_count`, `response_time_total`, `response_time_avg`, and `response_time_max`.
* Fixed an issue for Microsoft Windows users where the scroll down button in the web chat pane wasn't working correctly.
* Fixed an issue that occurred after an administrator deactivated the chat channel or the email channel. Instead of sending a single notification email for this change, the system was sending multiple notification emails.
* Fixed a reporting discrepancy between the **Agent Metrics (Historical)** explore and the **Chat Agent Metrics (Historical)** explore in the advanced reporting dashboards.
* Fixed an issue in the **Operation Management > Virtual Agent** settings pane. After configuring the virtual agent to assign records to a specific user, subsequent changes to other settings couldn't be saved.
* Fixed an issue where the `sub_status` property was missing from the session metadata file.
* Fixed an issue for HubSpot users where the inbound phone number in the call adapter displayed as **null null**.
* Fixed an issue for Kustomer users that caused calls to be disconnected and the agent to be moved to `Unavailable` status.
* Fixed an issue where the target response time timer in the chat adapter was resetting when the end-user sent a message instead of when the agent sent a message.
* Fixed an issue that occurred when agents used the chat adapter to send email addresses containing underscores. The email addresses resolved incorrectly in the end-user's chat pane, breaking the links.
* Fixed an issue that caused inaccurate chat analytics. Affected metrics included `response_time_total`, `response_time_avg`, and `chat_duration`.
* Fixed an issue where the queue-level overcapacity callback limit was ignored, and the global setting was enforced instead.
* Fixed an issue for Kustomer users where the ticket for an outbound call incorrectly showed the recipient's number in the **From** field and left the **To** field blank.
* Fixed an issue where the agent adapter froze when an agent making an outbound call changed the outbound call number using their favorites list.
* Fixed an issue that prevented a new chat from appearing in the agent desktop. This occurred when an agent had both the agent desktop and the standard chat adapter open in separate browser tabs.
* Fixed an issue that caused a significant delay in displaying contact detail information in the call adapter for campaign calls.
* Fixed an issue where users with read-only roles were able to change settings on the developer settings page.

---
## 2025-10-31

### Announcement

**Google Cloud CCaaS 3.40**

We've released version 3.40 of Google Cloud CCaaS, including the web SDK.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

### Feature

**Web SDK: Support for hiding the Start a new conversation button**

You can now configure the web SDK to hide the **Start a new conversation** button on the end-user's chat screen after the session ends. For more information, see [Hide the button to download a transcript at the end of a session](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-getting-started#hide-start-new-conversation-button).

### Feature

**Search in email channel by email address and name**

Agents can now search for email sessions by email address and name in the email adapter.

User experience change: The search pane in the email adapter includes two new fields: **Email Address** and **Name**.

For more information, see [Search for emails](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#search-for-emails).

### Feature

**The europe-west4 and europe-west6 regions are available for Agent Assist conversation profiles**

The `europe-west4` and `europe-west6` regions are now available when you create an Agent Assist conversation profile for a Dialogflow CX virtual agent. For more information, see [Create conversation profile for Dialogflow CX virtual agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-a-dialogflow-agent#create-cp).

### Feature

**Customize the color of the Start Screen Share button**

You can now control the color of the **Start Screen Share** button to match the color palette of your brand. For more information, see [Customize the Start Screen Share button](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse#customize-start-screen-share-button).

### Feature

**New variables for custom lookup URLs**

We've added the following five variables for custom lookup URLs:

* **CUSTOMER\_PHONE\_NUMBER**: the end-user's phone number
* **SUPPORT\_PHONE\_NUMBER**: your call center's phone number that an end-user calls in on
* **OUTBOUND\_NUMBER**: the phone number an agent uses when making an outbound call
* **SESSION\_ID**: the session ID
* **CUSTOM\_AGENT\_ID**: an optional agent ID

For more information, see [Custom lookup URL configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm#custom_lookup_url_configuration).

### Feature

**Web SDK: Support for hiding the download transcript option**

You can now configure the web SDK to do the following on the end-user's chat screen:

* [Hide the command to download a transcript during a session](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-getting-started#hide-command-to-download-transcript-during-session).
* [Hide the button to download a transcript at the end of a session](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-getting-started#hide-button-to-download-transcript-at-end-of-session).

### Feature

**Agent desktop maintains state after refresh**

While you're using the agent desktop, if you refresh your browser, the agent desktop now maintains its state. This means that active conversations, finished tabs, and recently closed sessions remain as they were before the refresh.

### Fixed

The following issues were addressed in this release:

* Fixed an issue that prevented administrators from configuring virtual agents on the top level for IVR queues.
* Fixed an issue where attempting to configure automatic redirection settings for the top level of an IVR queue returned an error.
* Fixed in issue that caused incorrect agent monitoring and reporting data when a virtual agent escalated a call to a queue in a different language.
* Fixed issue for HubSpot users where the call adapter got stuck on a non-functional reconnect page after a session expired.
* Fixed an issue for HubSpot users where the **Delay call record creation until the call is connected to agent** checkbox didn't appear in the **CRM Record Creation Details** pane.
* Fixed an issue that prevented agents from ending direct SMS chat sessions.
* Fixed an issue for Microsoft Windows 11 users that prevented agents from entering Japanese characters in the chat screen during chat sessions and into the notes during wrap-up.
* Fixed an issue where SDK custom data that was passed using the web SDK didn't appear in the agent adapter.
* Fixed an issue that prevented custom links entered in the chat adapter from being converted into clickable links.
* Fixed an issue in the chat screen of the chat adapter where the **Missed target response time** message was partially obscured by the formatting toolbar.
* Fixed an issue where agents couldn't initiate a callback to a missed agent-to-agent call from the **History** tab of the agent adapter.
* Fixed an issue where predictive outbound calling campaigns stalled and incorrectly moved contacts to the **Redialed** list before retrying them. This prevented the campaigns from completing successfully.
* Fixed an issue in the **Call Details** pane where the **Recording Message Sequence** settings were incorrectly inactive when the **Play Call Recording Messages** checkboxes were cleared.

  Administrators: In the **Call Details** pane, we changed **Recording Message Sequence** to **Recording Message Sequence for Outbound Calls** for clarity.
* Fixed an issue where the customized greeting for an automatic redirection rule didn't play for calls that entered the queue using a Direct Access Phone (DAP) number.
* Fixed an issue that occurred when a call was made from the global contact list. On the **Details** tab of the call adapter, the destination name didn't display. Instead, the destination phone number displayed.
* Fixed an agent desktop issue where an agent status that was configured with a role restriction mistakenly appeared in the status list for a user assigned to that restricted role.
* Fixed an issue where searching for an inbound-only queue on the **Phone Number Management** page failed to return a result.
* Fixed an issue that caused queue duration and wait duration to be reported as `0`. This occurred when the **Call Service Level Target** on a queue settings page was set to a number that exceeded the maximum allowed limit.
* Fixed an issue where a team assigned to a preference profile added only 1 user to the profile's users count, instead of adding the total number of users on the team.
* Fixed an issue where agents were timed out for inactivity while composing an email in the email adapter.
* Fixed an issue where users with a custom role were unable to save changes in the **Chat Settings** pane, even when their role had **View** and **Edit** permissions.
* Fixed an issue that occurred after an agent configured their own hours of operation settings in the agent adapter. Those settings didn't appear for administrators in the agent's user profile on the **Settings > Users & Team > Manage Users & Teams** page. This prevented the administrator from making other edits to the agent's profile without overwriting the agent's hours of operation settings.
* Fixed an issue where CRM tickets weren't created for some calls.
* Fixed an issue where outbound SIP calls incorrectly appended data parameters, causing calls to fail.
* Fixed a Web SDK security vulnerability associated with DOMPurify.
* Fixed an issue where chat metadata wasn't saved to external storage. This occurred when an end-user ended a chat after escalating from a virtual agent but before being connected to a human agent.

---
## 2025-10-30

### Announcement

**Advanced reporting dashboards version 3.40**

We've released version 3.40 of the advanced reporting dashboards.

### Feature

**New Audit Log dashboard**

We've added a new **Audit log** dashboard to help you track changes to the configuration of your instance. The dashboard tracks changes to the settings on the **Developer Settings** page, and displays information such as the type of change, who made the change, and when. This dashboard is similar in format to the advanced reporting dashboards, but you can't save it as a new dashboard. You access the **Audit Log** dashboard from the **Settings** menu. For more information, see [Audit log dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-audit-log).

### Feature

**New Agent Preference table in the Agent Availability dashboard**

We've added a new **Agent Preference** table to the **Agent Availability** dashboard. This table can help you ensure that queues have properly skilled agents assigned to them. It can also help identify agents who improperly change their availability filters. For more information, see [Agent availability dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-agent-availability).

### Fixed

We addressed the following issues in this release:

* Fixed an issue where the queue groups dashboard failed to display data for users with a custom role assigned to a queue or queue group.
* Fixed an issue that caused the **Agent Activity Timeline** dashboard to display inaccurate or incomplete data.
* Fixed an issue on the **Virtual Agent - Calls** dashboard where the **Virtual Agent Name** and **Queue** filters didn't display available values.
* Fixed an issue on the **Dispositions - Chats** dashboard that prevented the **Agent Email**, **Agent ID**, and **Location** filters from displaying available values.
* Fixed an issue on the **Virtual Agent - Chats** dashboard that prevented the **Virtual Agent Name** filter from displaying available values.
* Fixed an issue on the **Virtual Agent - Chats** dashboard where the **Date** filter was incorrectly labeled **Time Range**.
* Fixed an issue on the **Abandons - Calls** dashboard where **Customer ANI** values weren't appearing in the **Queue Abandon Details** and **IVR Abandon Details** tables despite the customer signing the waiver.
* Fixed an issue on the **Agent Activity Timeline** dashboard where the **Agent Name** filter wasn't working properly.

---
## 2025-10-21

### Announcement

**Advanced reporting dashboards version 3.40**

We've released version 3.40 of the advanced reporting dashboards.

### Feature

**New Agent Preference table in the Agent Availability dashboard**

We've added a new **Agent Preference** table to the **Agent Availability** dashboard. This table can help you ensure that queues have properly skilled agents assigned to them. It can also help identify agents who improperly change their availability filters. For more information, see [Agent availability dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-agent-availability).

### Feature

**New Audit Log dashboard**

We've added a new **Audit log** dashboard to help you track changes to the configuration of your instance. The dashboard tracks changes to the settings on the **Developer Settings** page, and displays information such as the type of change, who made the change, and when. This dashboard is similar in format to the advanced reporting dashboards, but you can't save it as a new dashboard. You access the **Audit Log** dashboard from the **Settings** menu. For more information, see [Audit log dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-audit-log).

### Fixed

We addressed the following issues in this release:

* Fixed an issue that caused the **Agent Activity Timeline** dashboard to display inaccurate or incomplete data.
* Fixed an issue on the **Virtual Agent - Calls** dashboard where the **Virtual Agent Name** and **Queue** filters didn't display available values.
* Fixed an issue on the **Dispositions - Chats** dashboard that prevented the **Agent Email**, **Agent ID**, and **Location** filters from displaying available values.
* Fixed an issue on the **Virtual Agent - Chats** dashboard that prevented the **Virtual Agent Name** filter from displaying available values.
* Fixed an issue on the **Virtual Agent - Chats** dashboard where the **Date** filter was incorrectly labeled **Time Range**.
* Fixed an issue on the **Abandons - Calls** dashboard where **Customer ANI** values weren't appearing in the **Queue Abandon Details** and **IVR Abandon Details** tables despite the customer signing the waiver.
* Fixed an issue on the **Agent Activity Timeline** dashboard where the **Agent Name** filter wasn't working properly.

---
## 2025-10-15

### Announcement

**Mobile SDK patch 2.14.1 is released**

This patch adds the `didHandleUjetError` function to the iOS SDK. The `didHandleUjetError` function can listen for and handle the following errors:

* `networkError`
* `authenticationError`
* `authenticationJwtError`
* `voipConnectionError`
* `voipLibraryNotFound`
* `chatLibraryNotFound`

For more information, see [Fallback](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#fallback).

---
## 2025-10-14

### Announcement

**Portal version 3.40 pre-release notes**

Here are the pre-release notes for portal version 3.40. When we release version 3.40, we expect the new capabilities to be as shown here.

### Feature

**New variables for custom lookup URLs**

We've added the following five variables for custom lookup URLs:

* **CUSTOMER\_PHONE\_NUMBER**: the end-user's phone number
* **SUPPORT\_PHONE\_NUMBER**: your call center's phone number that an end-user calls in on
* **OUTBOUND\_NUMBER**: the phone number an agent uses when making an outbound call
* **SESSION\_ID**: the session ID
* **CUSTOM\_AGENT\_ID**: an optional agent ID

For more information, see [Custom lookup URL configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm#custom_lookup_url_configuration).

### Feature

**Agent desktop maintains state after refresh**

While you're using the agent desktop, if you refresh your browser, the agent desktop now maintains its state. This means that active conversations, finished tabs, and recently closed sessions remain as they were before the refresh.

### Feature

**Search in email channel by email address and name**

Agents can now search for email sessions by email address and name in the email adapter.

User experience change: The search pane in the email adapter includes two new fields: **Email Address** and **Name**.

For more information, see [Search for emails](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#search-for-emails).

### Feature

**Customize the color of the Start Screen Share button**

You can now control the color of the **Start Screen Share** button to match the color palette of your brand. For more information, see [Customize the Start Screen Share button](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse#customize-start-screen-share-button).

### Feature

**The europe-west4 and europe-west6 regions are available for Agent Assist conversation profiles**

The `europe-west4` and `europe-west6` regions are now available when you create an Agent Assist conversation profile for a Dialogflow CX virtual agent. For more information, see [Create conversation profile for Dialogflow CX virtual agents](https://cloud.google.com/contact-center/ccai-platform/docs/create-a-dialogflow-agent#create-cp).

### Feature

**Web SDK: Support for hiding the download transcript option**

You can now configure the web SDK to do the following on the end-user's chat screen:

* Hide the **Download transcript** menu option during a chat session
* Hide the **Download transcript** button after a chat session ends

### Feature

**Web SDK: Support for hiding the Start a new conversation button**

You can now configure the web SDK to hide the **Start a new conversation** button on the end-user's chat screen after the session ends.

### Fixed

The following issues were addressed in this release:

* Fixed an issue that prevented administrators from configuring virtual agents on the top level for IVR queues.
* Fixed an issue where attempting to configure automatic redirection settings for the top level of an IVR queue returned an error.
* Fixed in issue that caused incorrect agent monitoring and reporting data when a virtual agent escalated a call to a queue in a different language.
* Fixed issue for HubSpot users where the call adapter got stuck on a non-functional reconnect page after a session expired.
* Fixed an issue for HubSpot users where the **Delay call record creation until the call is connected to agent** checkbox didn't appear in the **CRM Record Creation Details** pane.
* Fixed an issue that prevented agents from ending direct SMS chat sessions.
* Fixed an issue for Microsoft Windows 11 users that prevented agents from entering Japanese characters in the chat screen during chat sessions and into the notes during wrap-up.
* Fixed an issue where SDK custom data that was passed using the web SDK didn't appear in the agent adapter.
* Fixed an issue that prevented custom links entered in the chat adapter from being converted into clickable links.
* Fixed an issue in the chat screen of the chat adapter where the **Missed target response time** message was partially obscured by the formatting toolbar.
* Fixed an issue where agents couldn't initiate a callback to a missed agent-to-agent call from the **History** tab of the agent adapter.
* Fixed an issue where predictive outbound calling campaigns stalled and incorrectly moved contacts to the **Redialed** list before retrying them. This prevented the campaigns from completing successfully.
* Fixed an issue in the **Call Details** pane where the **Recording Message Sequence** settings were incorrectly inactive when the **Play Call Recording Messages** checkboxes were cleared.

  Administrators: In the **Call Details** pane, we changed **Recording Message Sequence** to **Recording Message Sequence for Outbound Calls** for clarity.
* Fixed an issue where the customized greeting for an automatic redirection rule didn't play for calls that entered the queue using a Direct Access Phone (DAP) number.
* Fixed an issue that occurred when a call was made from the global contact list. On the **Details** tab of the call adapter, the destination name didn't display. Instead, the destination phone number displayed.
* Fixed an agent desktop issue where an agent status that was configured with a role restriction mistakenly appeared in the status list for a user assigned to that restricted role.
* Fixed an issue where searching for an inbound-only queue on the **Phone Number Management** page failed to return a result.
* Fixed an issue that caused queue duration and wait duration to be reported as `0`. This occurred when the **Call Service Level Target** on a queue settings page was set to a number that exceeded the maximum allowed limit.
* Fixed an issue where a team assigned to a preference profile added only 1 user to the profile's users count, instead of adding the total number of users on the team.
* Fixed an issue where agents were timed out for inactivity while composing an email in the email adapter.
* Fixed an issue where users with a custom role were unable to save changes in the **Chat Settings** pane, even when their role had **View** and **Edit** permissions.
* Fixed an issue that occurred after an agent configured their own hours of operation settings in the agent adapter. Those settings didn't appear for administrators in the agent's user profile on the **Settings > Users & Team > Manage Users & Teams** page. This prevented the administrator from making other edits to the agent's profile without overwriting the agent's hours of operation settings.
* Fixed an issue where CRM tickets weren't created for some calls.
* Fixed an issue where outbound SIP calls incorrectly appended data parameters, causing calls to fail.
* Fixed a Web SDK security vulnerability associated with DOMPurify.
* Fixed an issue where chat metadata wasn't saved to external storage. This occurred when an end-user ended a chat after escalating from a virtual agent but before being connected to a human agent.

---
## 2025-10-09

### Announcement

**Version 3.39 is released**

All release notes published on this date are part of version 3.39.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

### Feature

**Destination queue name and session history is available in the agent adapter**

The agent adapter now displays the destination queue during transfers and deflections for IVR calls. The agent adapter also displays transfer history in the **Call details** and **Chat details** tabs.

User experience changes:

* The **Call details** and **Chat details** tabs in the agent adapter have a new **Transfer History** section.
* The chat pane in the chat adapter has a new **Transfers** button that opens the **Transfer History** pane.

Administrators: There's a new checkbox at **Settings > Operation Management > Transfer history** for turning on transfer history in the agent adapter.

For more information, see [Transfer history and queue information in the agent adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-info-transfer-history-agent-adapter).

### Feature

**Improved controls over the ordering of key-value pairs in the agent adapter and CRM records**

Google Cloud CCaaS has improved controls over the ordering of the key-value pairs that appear in the agent adapter and in CRM records. Here's how the ordering controls work:

* **Virtual agents**: When you configure session variables, you can use the new `display_order_in_adapter` property to specify the order that the session variables appear in the agent adapter and in CRM records. For more information, see [Capture from intent response](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#capture_from_intent_response).
* **Web SDK**: Web SDK custom data is displayed in the agent adapter and CRM records in the order that the key-value pairs appear in the JSON custom data file. For more information about JSON custom data files, see [Chat unsigned custom data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk#chat-unsigned-custom-data).

### Feature

**Virtual agents for the SMS channel**

Virtual agents are now available for the SMS channel. This lets you create virtual agents and assign them to SMS queues, offering virtual agent support to end-users in SMS chat sessions. For more information, see [Virtual agents for SMS](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agents-for-sms).

### Feature

**Search in the email channel**

Agents can now search for emails in the agent adapter by keyword, session ID, or subject. For more information, see [Search for emails](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#search-for-emails).

### Feature

**Cancel scheduled calls with the callback calls API**

You can now use the callback calls API to cancel a single scheduled callback call or a list of calls. For more information, see [Callback call API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/callback-call-api).

### Feature

**Mid-session authentication is supported by all CRM types**

Mid-session authentication is supported by all CRM types, not just custom CRMs. For more information, see [Mid-Session authentication by API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/mid-session-authentication-apps-api).

### Feature

**New advanced reporting dashboards**

The following new advanced reporting dashboard is available:

* **Deflections**. Get deflection information by queue and for your entire contact center. For more information, see [Deflections dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-deflections).
* **Agent activity timeline**. See the historical activity for an agent. For more information, see [Agent activity timeline dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-agent-activity-timeline).

### Feature

**Advanced reporting dashboard updates**

We've made the following updates to the advanced reporting dashboards:

* **Queue Group Dashboards All dashboard**: The tiles and tables on this dashboard have been replaced with the following tables:

  + **Queue Group Performance Calls**: displays detailed performance information for calls by queue group.
  + **Queue Group Performance Chats**: displays detailed performance information for chats by queue group.

  For more information, see [Queue Group Dashboards All](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-group-perf#queue-group-dashboards-all).
* **Queue interval dashboards**: The **Queue Interval - Calls** and **Queue Interval - Chats** dashboards have a new **Total Queue Entries** column in the table tile. This is the sum of all inbound interactions that have entered a queue, excluding transfers.

  For more information, see [Queue interval dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-interval).
* **Virtual agent dashboards**: On both the **Virtual Agent Dashboard Calls** and **Virtual Agent Dashboard Chats** dashboards, the virtual agent metrics table contains a new **Interaction Outcome** column.

  For more information, see [Virtual agent dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-virtual-agent).
* **All Interactions - Chat dashboard**: In the **All Chat Interactions (Historical)** table, if you configure chat transcript storage for your CRM, the values in the **Chat ID** column become links to the chat transcripts.

  For more information, see [All interactions dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-all-interactions).
* **New metrics in the Call Queue Metrics (Historical) Explore**: We've added the following two metrics to the **Call Queue Metrics (Historical)** Explore:

  + **CSL %**: Custom Service Level. This is calculated as follows: The number of queued interactions within SLA / The number of queued interactions answered.
  + **Total Queued Answered**: The number of queued interactions answered by a human agent.

  For information about metrics in an Explore, see [Create a new metrics tile in a dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-add-tiles-to-dashboard#create_a_new_metrics_tile_in_a_dashboard).
* **Additional dashboards with advanced capabilities**: the following dashboards now appear on the **Advanced Reporting Landing Page**. This means you can use them to create new custom dashboards or create Looks to link to custom dashboards.

  **Performance**

  + **Dispositions / Calls**
  + **Dispositions / Chats**
  + **Deflections / Calls**
  + **Deflections / Chats**
  + **CSAT / Calls**
  + **CSAT / Chats**
  + **Co-browse / Calls**
  + **Co-browse / Chats**
  + **Failed / Calls**
  + **Failed / Chats**
  + **Missed / Calls**
  + **Missed / Chats**

  **Agent Reporting**

  + **Agent Activity Timeline**

  **Monitoring Dashboards**

  + **Calls Connected**
  + **Chats Connected**
  + **Calls Queued**
  + **Chats Queued**

  For more information, see [Advanced capabilities](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-advanced-capabilities).

### Fixed

The following issues were addressed in this release:

* Fixed an issue where incoming chats took precedence over the in-progress chat.

  **User experience change**: When a new chat appears in the agent adapter, it no longer takes focus away from the in-progress chat. The in-progress retains focus.
* Fixed a web SDK issue where sensitive data sent by an end-user was redacted for both the end-user and the agent, instead of just for the agent.
* Fixed an issue where the contact list in the agent adapter wouldn't load the full list of contacts.
* Fixed an issue where an agent clicking an email in the agent adapter returned an **Email Not Found** error.
* Fixed an issue where managers assigned to multiple teams were unable to view agent statistics for every team they were assigned to.
* Fixed an issue for ServiceNow users where `call_duration` was using the earliest `connected_at` time instead of the latest `connected_at` time, causing call durations to appear longer than they actually were.
* Fixed an issue in the **Settings > Developer Settings > External Storage** pane where language checkboxes were associated with the **Co-browse Recordings** checkbox instead of the **Session Data Feed** checkbox.

  **Administrators**: In the **Settings > Developer Settings > External Storage** pane, the languages checkboxes have moved from the **Co-browse Recordings** checkbox to the **Session Data Feed** checkbox.
* Fixed an issue where agent-initiated outbound calls were using the default number for the selected queue instead of the number chosen by the agent.
* Fixed an issue where the downloaded session chat data report contained an extra quotation mark.
* Fixed an issue where users received an email telling them to create a password after Single Sign-On (SSO) was turned on.
* Fixed an issue where SSO configuration settings in the user's instance were deleted after they turned off SSO.
* Fixed an issue where an administrator couldn't configure agent status restrictions without exposing them to agents.
* Fixed an issue where custom contact lists could only be replaced, and not removed, after they were assigned to a team.
* Fixed an issue where the inheritance indicator and **Reset to parent** button was missing from the queue level **Contact List Management** pane.
* Fixed an issue where the SMS and Web chat availability preferences in the agent adapter were the reverse of how they were configured.
* Fixed an issue where queue transfer restrictions were not saved after being configured.
* Fixed an issue that occurred when a user attempted to name a new queue. The name field abruptly lost focus after the first character, forcing the user to enter the queue name again.
* Fixed an issue where creating an instance would time out and fail.
* Fixed an issue that prevented reports from being downloaded.
* Fixed an issue where the chat history for blended SMS sessions failed to save.
* Fixed an issue where the **Transfer failed** message didn't appear. This occurred when an agent failed to pick up a transferred call before the transferred call expiration time expired.
* Fixed an issue where IVR call recordings failed to save or were corrupted. This resulted in recordings that were only one second long, were saved in the wrong format, or weren't saved at all.
* Fixed an issue where completed chat sessions appeared in the chats waiting area of agent desktop.
* Fixed an issue for CRM users with voicemails that are attached directly to tickets. An incorrect "External Storage must be configured" warning appeared when configuring voicemail options for IVR queues.
* Fixed an issue where transfer restrictions that were configured and saved for a web queue did not appear correctly the next time the **Transfer Restrictions** pane for that queue was viewed.
* Fixed an issue where the unread message count in the chat pane was inconsistent when viewing it from multiple browser tabs.
* Fixed an issue in virtual assistant reporting where the `finish_reason` property was incorrectly assigned to the `undefined` value. Now the `finish_reason` property is assigned to descriptive values that describe the reason for the conclusion of the chat session.
* Fixed an issue where PDF transcripts of chat sessions contained malformed links.
* Fixed an issue in historical reports where the fields in the **Failed Reason Description** column were blank.
* Fixed an issue where CSAT scores were missing from some advanced reporting dashboards.
* Fixed an issue for HubSpot users that caused long delays in case creation for inbound calls.
* Fixed an issue where the photo and video files that the agent provided in pre-session Smart Actions didn't appear in the CRM.
* Fixed an issue where agents in `Unavailable` status couldn't see waiting web chats.
* Fixed an issue where HTML was not rendering properly in virtual agent messages in the agent adapter
* Fixed an issue where agents were not switching into `Wrap-up Exceeded` status after a breakthrough call.
* Fixed an agent desktop issue where administrators were unable to assign announcements to some teams or agents.
* Fixed an agent desktop issue where agents couldn't copy text to the clipboard from an agent desktop custom panel.
* Fixed an agent desktop issue where the term "Anonymous User" wasn't being translated into French.
* Fixed an issue where the `UJET_ID` and `ANI` variables weren't passed correctly for SIP calls.
* Fixed an issue where the chat adapter froze when agents switched between chats.
* Fixed an issue on the **Agents** page of the Google Cloud CCaaS portal where administrators couldn't switch between session types.
* Fixed an issue where a newly added Agent Assist platform displayed as `Invalid` even though it was valid.
* Fixed an issue for Salesforce users where the call button didn't work when an agent attempted to call a number that was attached to a record for a previous call.
* Fixed an issue where audio files with accented characters in their file names failed to play back when using a storage proxy.
* Fixed an agent desktop issue where the `UJET_ID` variable in the custom URL for a custom panel wasn't being passed correctly.
* Fixed an issue where calls originating from a native campaign generated two CRM tickets for the same interaction.
* Fixed latency issues with web SDK Telnyx calls.
* Fixed an issue where outbound Bring Your Own Carrier (BYOC) calls used a number other than the one agents selected in the agent adapter.
* Fixed a Telnyx chatbot worker failure issue where background jobs related to call processing and chatbot escalations were failing and consuming excessive system resources.
* Fixed an issue where calls to the bulk user upload endpoint returned a success status even when the uploads failed.
* Fixed an issue in the chat waiting field of the agent desktop when multiple chats were in wrap-up. Instead of displaying **Wrap-up in progress** for all sessions in wrap-up, some sessions displayed **Auto answered**.
* Fixed an issue in the queue group dashboard where the **Callbacks waiting** tile incorrectly included callbacks that were completed, abandoned, or failed.
* Fixed an issue that caused inbound calls to disconnect if they were routed to an agent with a disabled microphone.
* Fixed an issue for HubSpot users where logging the "call started" event (`create_activity`) in the ticket was delayed.
* Fixed an issue that prevented transferred calls from being routed to available agents.
* Fixed an issue in the agent adapter for French (Canada) where words weren't translated or were translated incorrectly.
* Fixed an issue in call queue reporting where the Failed Reason Description for voice-scheduled mobile calls was not appearing.
* Fixed an issue that prevented external chat transcripts from being passed into new chat sessions.
* Fixed an advanced reporting issue where CSAT ratings were not appearing correctly when creating custom dashboards.
* Fixed an advanced reporting issue where callbacks waiting metrics didn't match in the following dashboards: **Queue Groups Dashboard Calls** and **Queued Calls Status Dashboard**.

---
## 2025-09-25

### Announcement

**Web SDK version 2 will be shut down on June 26, 2026**

On June 26, 2025, we announced the launch of [Web SDK version 3](https://cloud.google.com/contact-center/ccai-platform/docs/release-notes#June_26_2025). Starting on **June 26, 2026**, the web SDK v2 will no longer function. Be sure to [update your website](https://cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade) to use the web SDK v3 before that date to avoid breaking your integration with the web SDK. We are no longer adding new features to the web SDK v2.

---
## 2025-09-04

### Announcement

**Agent desktop is GA**

Agent desktop is now [generally available (GA)](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages). Agent desktop is a customizable interface that provides agents quick access to the information and tools they need to handle customer sessions. The desktop layout includes the agent adapter as well as configurable panels that display information or tools. You can configure a distinct desktop layout for each session type: inbound calls, outbound calls, or chats. You can then configure which desktop layout that an agent sees when they answer an inbound call, place an outbound call, or handle a chat. You can also configure announcements to communicate updates, alerts, and other important information directly to agents. For more information, see [Agent desktop](https://cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-overview).

The agent desktop provides the following capabilities:

* **Create desktop layouts**. With agent desktop, you can create customized desktop layouts for different use cases for your human agents. These include receiving inbound calls, placing outbound calls, and handling chat sessions. Your layouts can contain call adapters, chat adapters, and a wide variety of panels for other capabilities such as live transcripts, knowledge assist, disposition codes, and session data feeds. You can also configure custom panels to use as widgets that you can drag into panels. For more information, see [Create desktop layouts](https://cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts).
* **Configure custom panels**. A custom panel displays one or more URLs for external resources. These can be documentation, tools, or other resources. A custom panel appears as a widget in the desktop layout builder. Then, when you create desktop layouts, you can drag widgets into panels. For more information, see [Configure custom panels](https://cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-widgets).
* **Use widgets**. Widgets are containers of specific functionality that you can drag into panels in the desktop layout builder. The desktop layout builder comes with a number of pre-defined widgets, such as **Session Data Feed**, **Disposition Codes and Notes**, **Knowledge Assist**, and **Live Transcript**.
* **Configure desktop layouts for agents**. You can configure which desktop layout that agents see when they answer an inbound call, place an outbound call, or handle a chat. You can configure this globally, at the queue level, and at the team level. Queue-level layout settings take priority over global settings. Team-level settings take priority over both queue-level settings and default settings. For more information, see [Configure desktop layouts for agents](https://cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-set-desktop-layouts).
* **Configure announcements**. With announcements, you can communicate updates, alerts, and other important information directly to agents. Announcements appear in the agent desktop as notification banners that persist until the agent dismisses them. Announcements also appear in the agent's announcement list. For more information, see [Configure announcements](https://cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-announcements).

---
## 2025-09-02

### Announcement

**Mobile SDK 2.14 is released**

Mobile SDK 2.14 includes the following updates:

* Android SDK and iOS SDK:

  + Support for virtual agent to virtual agent chat transfers by queue.
  + Support for hiding the download transcript button in the options menu, the post-chat screen, or both. For the Android SDK, see [SDK configuration](https://cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#sdk-configuration). For the iOS SDK, see [Show or hide the download transcript button](https://cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#show-or-hide-download-transcript-button).
  + Improved accessibility, including better navigation and screen reader support.
* Android SDK:

  + Support for hiding the SDK using the `Ujet.hideSDK()` method. For more information, see [Hide the SDK](https://cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#hide-sdk).
  + New event types: `MessageLinkClicked` and `QuickReplyClicked`. For more information, see [Event Notifications](https://cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#UUID-b0019caa-2311-8ca3-64d7-f181ea921d77).

To support the new virtual agent chat transfer capabilities of this release, we've added a new configuration setting in the Google Cloud CCaaS portal. You can use this setting to hide transfer system messages in chat sessions with virtual agent to virtual agent transfers.

**Administrators**: In the **Settings > Chat > Web & Mobile Chat Settings** pane, there's a new **Transfers** checkbox.

For more information, see [Hide transfer messages in chat sessions](https://cloud.google.com/contact-center/ccai-platform/docs/va-to-va-transfers#hide-transfer-messages-in-chat-sessions).

---
## 2025-08-29

### Fixed

Fixed an issue where the Android SDK wouldn't minimize when an end-user clicked a deep link.

---
## 2025-08-27

### Announcement

**Portal version 3.39 pre-release notes**

Here are the pre-release notes for portal version 3.39. When we release version 3.39, we expect the new capabilities to be as shown here.

### Feature

**Destination queue name and session history is available in the agent adapter**

The agent adapter now displays the destination queue during transfers and deflections for IVR calls. The agent adapter also displays transfer history in the **Call details** and **Chat details** tabs.

User experience changes:

* The **Call details** and **Chat details** tabs in the agent adapter have a new **Transfer History** section.
* The chat pane in the chat adapter has a new **Transfers** button that opens the **Transfer History** pane.

Administrators: There's a new checkbox at **Settings > Operation Management > Transfer history** for turning on transfer history in the agent adapter.

### Feature

**Improved controls over the ordering of key-value pairs in the agent adapter and CRM records**

Google Cloud CCaaS has improved controls over the ordering of the key-value pairs that appear in the agent adapter and in CRM records. Here's how the ordering controls work:

* **Virtual agents**: When you configure session variables, you can use the new `display_order_in_adapter` property to specify the order that the session variables appear in the agent adapter and in CRM records.
* **Web SDK**: Web SDK custom data is displayed in the agent adapter and CRM records in the order that the key-value pairs appear in the JSON custom data file.

### Feature

**Virtual agents for the SMS channel**

Virtual agents are now available for the SMS channel. This lets you create virtual agents and assign them to SMS queues, offering virtual agent support to end-users in SMS chat sessions.

### Feature

**Search in the email channel**

Agents can now search for emails in the agent adapter by keyword, session ID, or subject.

### Feature

**Cancel scheduled calls with the callback calls API**

You can now use the callback calls API to cancel a single scheduled callback call or a list of calls.

### Feature

**Mid-session authentication is supported by all CRM types**

Mid-session authentication is supported by all CRM types, not just custom CRMs. For more information, see [Mid-Session authentication by API](https://cloud.google.com/contact-center/ccai-platform/docs/mid-session-authentication-apps-api).

### Feature

**New advanced reporting dashboards**

The following new advanced reporting dashboard is available:

* **Deflections**. Get deflection information by queue and for your entire contact center. For more information, see [Deflections dashboards](https://cloud.google.com/contact-center/ccai-platform/docs/dashboards-deflections).
* **Agent activity timeline**. See the historical activity for an agent.

### Feature

**Advanced reporting dashboard updates**

We've made the following updates to the advanced reporting dashboards:

* **Queue Group Dashboards All dashboard**: The tiles and tables on this dashboard have been replaced with the following tables:

  + **Queue Group Performance Calls**: displays detailed performance information for calls by queue group.
  + **Queue Group Performance Chats**: displays detailed performance information for chats by queue group.
* **Virtual agent dashboards**: On both the **Virtual Agent Dashboard Calls** and **Virtual Agent Dashboard Chats** dashboards, the virtual agent metrics table contains a new **Interaction Outcome** column.
* **All Interactions - Chat dashboard**: In the **All Chat Interactions (Historical)** table, if you configure chat transcript storage for your CRM, the values in the **Chat ID** column become links to the chat transcripts.
* **Additional dashboards with advanced capabilities**: the following dashboards now appear on the **Advanced Reporting Landing Page**. This means you can use them to create new custom dashboards or create Looks to link to custom dashboards.

  **Performance**

  + **Dispositions / Calls**
  + **Dispositions / Chats**
  + **Deflections / Calls**
  + **Deflections / Chats**
  + **CSAT / Calls**
  + **CSAT / Chats**
  + **Co-browse / Calls**
  + **Co-browse / Chats**
  + **Failed / Calls**
  + **Failed / Chats**
  + **Missed / Calls**
  + **Missed / Chats**

  **Agent Reporting**

  + **Agent Activity Timeline**

  **Monitoring Dashboards**

  + **Calls Connected**
  + **Chats Connected**
  + **Calls Queued**
  + **Chats Queued**

  For more information, see [Advanced capabilities](https://cloud.google.com/contact-center/ccai-platform/docs/dashboards-advanced-capabilities).

### Fixed

The following issues were addressed in this release:

* Fixed an issue where incoming chats took precedence over the in-progress chat.

  **User experience change**: When a new chat appears in the agent adapter, it no longer takes focus away from the in-progress chat. The in-progress retains focus.
* Fixed a web SDK issue where sensitive data sent by an end-user was redacted for both the end-user and the agent, instead of just for the agent.
* Fixed an issue where the contact list in the agent adapter wouldn't load the full list of contacts.
* Fixed an issue where an agent clicking an email in the agent adapter returned an **Email Not Found** error.
* Fixed an issue where managers assigned to multiple teams were unable to view agent statistics for every team they were assigned to.
* Fixed an issue for ServiceNow users where `call_duration` was using the earliest `connected_at` time instead of the latest `connected_at` time, causing call durations to appear longer than they actually were.
* Fixed an issue in the **Settings > Developer Settings > External Storage** pane where language checkboxes were associated with the **Co-browse Recordings** checkbox instead of the **Session Data Feed** checkbox.

  **Administrators**: In the **Settings > Developer Settings > External Storage** pane, the languages checkboxes have moved from the **Co-browse Recordings** checkbox to the **Session Data Feed** checkbox.
* Fixed an issue where agent-initiated outbound calls were using the default number for the selected queue instead of the number chosen by the agent.
* Fixed an issue where the downloaded session chat data report contained an extra quotation mark.
* Fixed an issue where users received an email telling them to create a password after Single Sign-On (SSO) was turned on.
* Fixed an issue where SSO configuration settings in the user's instance were deleted after they turned off SSO.
* Fixed an issue where an administrator couldn't configure agent status restrictions without exposing them to agents.
* Fixed an issue where custom contact lists could only be replaced, and not removed, after they were assigned to a team.
* Fixed an issue where the inheritance indicator and **Reset to parent** button was missing from the queue level **Contact List Management** pane.
* Fixed an issue where the SMS and Web chat availability preferences in the agent adapter were the reverse of how they were configured.
* Fixed an issue where queue transfer restrictions were not saved after being configured.
* Fixed an issue that occurred when a user attempted to name a new queue. The name field abruptly lost focus after the first character, forcing the user to enter the queue name again.
* Fixed an issue where creating an instance would time out and fail.
* Fixed an issue that prevented reports from being downloaded.
* Fixed an issue where the chat history for blended SMS sessions failed to save.
* Fixed an issue where the **Transfer failed** message didn't appear. This occurred when an agent failed to pick up a transferred call before the transferred call expiration time expired.
* Fixed an issue where IVR call recordings failed to save or were corrupted. This resulted in recordings that were only one second long, were saved in the wrong format, or weren't saved at all.
* Fixed an issue where completed chat sessions appeared in the chats waiting area of agent desktop.
* Fixed an issue for CRM users with voicemails that are attached directly to tickets. An incorrect "External Storage must be configured" warning appeared when configuring voicemail options for IVR queues.
* Fixed an issue where transfer restrictions that were configured and saved for a web queue did not appear correctly the next time the **Transfer Restrictions** pane for that queue was viewed.
* Fixed an issue where the unread message count in the chat pane was inconsistent when viewing it from multiple browser tabs.
* Fixed an issue in virtual assistant reporting where the `finish_reason` property was incorrectly assigned to the `undefined` value. Now the `finish_reason` property is assigned to descriptive values that describe the reason for the conclusion of the chat session.
* Fixed an issue where PDF transcripts of chat sessions contained malformed links.
* Fixed an issue in historical reports where the fields in the **Failed Reason Description** column were blank.
* Fixed an issue where CSAT scores were missing from some advanced reporting dashboards.
* Fixed an issue for HubSpot users that caused long delays in case creation for inbound calls.
* Fixed an issue where the photo and video files that the agent provided in pre-session Smart Actions didn't appear in the CRM.
* Fixed an issue where agents in `Unavailable` status couldn't see waiting web chats.
* Fixed an issue where HTML was not rendering properly in virtual agent messages in the agent adapter
* Fixed an issue where agents were not switching into `Wrap-up Exceeded` status after a breakthrough call.
* Fixed an agent desktop issue where administrators were unable to assign announcements to some teams or agents.
* Fixed an agent desktop issue where agents couldn't copy text to the clipboard from an agent desktop custom panel.
* Fixed an agent desktop issue where the term "Anonymous User" wasn't being translated into French.
* Fixed an issue where the `UJET_ID` and `ANI` variables weren't passed correctly for SIP calls.
* Fixed an issue where the chat adapter froze when agents switched between chats.
* Fixed an issue on the **Agents** page of the Google Cloud CCaaS portal where administrators couldn't switch between session types.
* Fixed an issue where a newly added Agent Assist platform displayed as `Invalid` even though it was valid.
* Fixed an issue for Salesforce users where the call button didn't work when an agent attempted to call a number that was attached to a record for a previous call.
* Fixed an issue where audio files with accented characters in their file names failed to play back when using a storage proxy.
* Fixed an agent desktop issue where the `UJET_ID` variable in the custom URL for a custom panel wasn't being passed correctly.
* Fixed an issue where calls originating from a native campaign generated two CRM tickets for the same interaction.
* Fixed latency issues with web SDK Telnyx calls.
* Fixed an issue where outbound Bring Your Own Carrier (BYOC) calls used a number other than the one agents selected in the agent adapter.
* Fixed a Telnyx chatbot worker failure issue where background jobs related to call processing and chatbot escalations were failing and consuming excessive system resources.
* Fixed an issue where calls to the bulk user upload endpoint returned a success status even when the uploads failed.
* Fixed an issue in the chat waiting field of the agent desktop when multiple chats were in wrap-up. Instead of displaying **Wrap-up in progress** for all sessions in wrap-up, some sessions displayed **Auto answered**.
* Fixed an issue in the queue group dashboard where the **Callbacks waiting** tile incorrectly included callbacks that were completed, abandoned, or failed.
* Fixed an issue that caused inbound calls to disconnect if they were routed to an agent with a disabled microphone.
* Fixed an issue for HubSpot users where logging the "call started" event (`create_activity`) in the ticket was delayed.
* Fixed an issue that prevented transferred calls from being routed to available agents.
* Fixed an issue in the agent adapter for French (Canada) where words weren't translated or were translated incorrectly.
* Fixed an issue in call queue reporting where the Failed Reason Description for voice-scheduled mobile calls was not appearing.
* Fixed an advanced reporting issue where CSAT ratings were not appearing correctly when creating custom dashboards.
* Fixed an advanced reporting issue where callbacks waiting metrics didn't match in the following dashboards: **Queue Groups Dashboard Calls** and **Queued Calls Status Dashboard**.

---
## 2025-08-20

### Announcement

**Version 3.37 is released**

All release notes published on this date are part of version 3.37.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

### Feature

**Restrict email transfers**

You can now configure your instance to prevent users with the agent role from transferring email sessions to other agents. Agents can still assign unassigned emails to themselves, and users with the manager role can still transfer email sessions from agent to agent.

Administrators: There's a new **Transfer Restrictions** pane at **Settings > Queue > Email > Edit / View > [queue] > Transfer Restrictions > Configure**.

For more information, see [Prevent email reassignment](https://cloud.google.com/contact-center/ccai-platform/docs/prevent-email-reassignment).

### Feature

**Skip the connecting message playback**

You can now configure your instance to skip playback of the connecting message when calls are connected to agents.

Administrators: The **Settings > Call > Call Details** pane contains a new **Skip the Connecting Message playback** checkbox.

For more information, see [Configure global call settings](https://cloud.google.com/contact-center/ccai-platform/docs/call-settings#configure-global-call-settings).

### Feature

**Workforce Management terminology update**

We've updated the terminology in the Workforce Management interface to align with Google Cloud CCaaS terminology. For example, we've changed "supervisor" to "manager", "employee" to "agent", and "Supervisor Portal" to "Manager Portal".

### Feature

**Generative knowledge assist is available in Agent Desktop**

Generative knowledge assist is now available in Agent Desktop as a widget that you can drag into a desktop panel.

For more information, see [Create desktop layouts](https://cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts).

### Feature

**Generative knowledge assist is available in the agent adapter**

Generative knowledge assist is now available in the agent adapter.

### Feature

**Web SDK version 3.37**

Starting with version 3.37, web SDK releases align with portal releases and share the same version number.

Web SDK version 3.37 includes the following update: we've improved the accessibily of the web SDK to be in compliance with the European Accessibility Act.

### Feature

**New advanced reporting dashboards**

The following new advanced reporting dashboards are available:

* **Missed interactions**. Get data on missed interactions to help you optimize operations. For more information, see [Missed interactions dashboards](https://cloud.google.com/contact-center/ccai-platform/docs/dashboards-missed-interactions).
* **Failed sessions**. Get insight into why your sessions are failing. For more information, see [Failed sessions dashboards](https://cloud.google.com/contact-center/ccai-platform/docs/dashboards-failed-sessions).
* **Screen share**. Get data on your agents' Screen Share interactions with end-users. For more information, see [Screen shared dashboards](https://cloud.google.com/contact-center/ccai-platform/docs/dashboards-screenshare).
* **CSAT**. Get insights into the customer satisfaction (CSAT) ratings that end-users give to their sessions with agents. For more information, see [CSAT dashboards](https://cloud.google.com/contact-center/ccai-platform/docs/dashboards-csat).
* **Dispositions**. Get disposition information to gain insights into common end-user issues and concerns. For more information, see [Dispositions dashboards](https://cloud.google.com/contact-center/ccai-platform/docs/dashboards-dispositions).

### Fixed

The following issues were addressed in this release:

* Fixed an issue where a blank error message box appeared in the agent adapter when a call connected.
* Fixed an issue where the notification icon for a new message or event in the chat adapter didn't clear after the agent viewed the message or event.
* ~~Fixed a Conversational Insights issue where conversation recordings were split into a file for the human agent segment and a file for the virtual agent segment. Now all call segments are aggregated into a single recording file, which is more useful for conversational analysis.~~
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
* Fixed an issue where the data in reports didn't match the data in the dashboards.
* Fixed an issue where virtual agent calls using Dialogflow CX failed, ending unexpectedly.
* Fixed two cross-site scripting vulnerabilites in the agent adapter.
* Fixed an issue where deltacast selected the agent with the longest time in the Available status instead of the agent with the longest time since their last customer interaction.
* Fixed an issue where escalations from a virtual agent to a human agent failed, and audio from the last agent response before human agent escalation was truncated.
* Fixed an issue where transcriptions weren't being created for IVR calls.
* Fixed an issue where agents could become stuck in wrap-up status, particularly with concurrent calls or quick callbacks.

---
## 2025-08-13

### Announcement

**Check the version number of your instance**

You can now check the version number of your instance and compare it with the version numbers of the updates and patches that Google announces in these release notes. In this way you can know which capabilities are available in your instance. For more information, see [Check the version number of your instance](https://cloud.google.com/contact-center/ccai-platform/docs/get-started#check_the_version_number_of_your_instance).

---
## 2025-08-11

### Announcement

**Availability in three additional regions**

Google Cloud CCaaS is now available in the following three additional regions:

* northamerica-northeast2 (Toronto)
* us-east4 (Virginia)
* me-west1 (Tel Aviv)

In each of these regions, Workforce Management is available and advanced reporting isn't available. For more information, see [Google Cloud regions](https://cloud.google.com/contact-center/ccai-platform/docs/localities#regions).

---
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
* Fixed an issue where the data in reports didn't match the data in the dashboards.
* Fixed an issue where virtual agent calls using Dialogflow CX failed, ending unexpectedly.
* Fixed two cross-site scripting vulnerabilites in the agent adapter.
* Fixed an issue where deltacast selected the agent with the longest time in the Available status instead of the agent with the longest time since their last customer interaction.
* Fixed an issue where escalations from a virtual agent to a human agent failed, and audio from the last agent response before human agent escalation was truncated.
* Fixed an issue where transcriptions weren't being created for IVR calls.

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
