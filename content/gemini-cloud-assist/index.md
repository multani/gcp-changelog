# Gemini Cloud Assist

## 2026-04-16

### geminicloudassist API automatically enabled for Gemini Cloud Assist chat users

As of April 16th, 2026, the `geminicloudassist.googleapis.com` API has been
automatically enabled on projects that meet **all** of the following criteria:

* Had used [Gemini Cloud Assist chat](https://docs.cloud.google.com/cloud-assist/chat-panel) in the prior
  60 days.
* Had the `cloudaicompanion.googleapis.com` API enabled on April 16, 2026.
* Did not have the `geminicloudassist.googleapis.com` API enabled on
  April 16, 2026.

The Gemini Cloud Assist chat functionality that was previously served by
`cloudaicompanion.googleapis.com` is now served by
`geminicloudassist.googleapis.com`, and both APIs are dependencies to use
Gemini Cloud Assist. This automatic API enablement ensures that users have
access to the same functionality without any loss of service.

---
## 2026-04-10

### Update for Gemini Cloud Assist investigations

From April 10, 2026, creating, running, and editing Gemini Cloud Assist
[investigations](https://docs.cloud.google.com/cloud-assist/investigations) will only be available to users
with a Premium Support contract or who have requested access through their
account team. If you ran an investigation prior to April 10, 2026, the results
of the investigation continue to be available to you in the Google Cloud console.

---
## 2026-04-09

### Model Context Protocol support

MCP support is available in Private Preview. To request access, contact your
Google Cloud account team. You can interact with Gemini Cloud Assist agents from
various surfaces, including third-party client agents and IDEs, using the Model
Context Protocol (MCP). For more information, see
[Integrating with MCP](https://docs.cloud.google.com/cloud-assist/docs/mcp-integration).

### Proactive agents for issue investigation

Proactive agents are available in Private Preview to Premium Support customers.
Enable Gemini Cloud Assist to autonomously investigate issues triggered by Cloud
Alerting policies or cost anomalies in the background. These investigations
don't modify or make any changes to your environment. Results and insights, such
as root cause analysis for alerts or cost spike drivers, are delivered via
Eventarc. You can view these results in the Google Cloud console. This feature requires
administrator enablement and configuration of an agent identity. For more
information, see [Configure proactive agents](https://docs.cloud.google.com/cloud-assist/docs/proactive-agents-setup).

### Page context awareness

Page context awareness is available in Public Preview. Gemini Cloud Assist
automatically uses the context of the content currently visible on your
Google Cloud console page to provide more relevant and accurate responses to your
prompts. For more information, see
[Manage page context sharing](https://docs.cloud.google.com/cloud-assist/chat-panel#page-context-sharing)

### Enhanced agent administration controls

[Enhanced agent administration controls](https://docs.cloud.google.com/cloud-assist/admin-settings) are available in Public Preview.
Administrators have the following options in the Cloud Assist settings panel:

* **Web grounding settings:** Choose how Gemini Cloud Assist uses Google Search to
  ground its responses, with options for either the most comprehensive results
  or stricter data residency compliance. For more information, see
  [Configure web grounding](https://docs.cloud.google.com/cloud-assist/docs/admin/web-grounding).
* **Custom instructions:** Define persistent system instructions to customize the
  agent's persona, response formatting, and awareness of organizational
  standards or business context for all users within the project. For more
  information, see [Set custom instructions](https://docs.cloud.google.com/cloud-assist/docs/admin/custom-instructions).

---
## 2026-04-08

### Custom IAM roles permission update for Gemini Cloud Assist

Gemini Cloud Assist has replaced the `cloudaicompanion.instances.completeTask`
IAM permission with `geminicloudassist.agents.invoke`. If you
have access to Gemini Cloud Assist through a custom IAM role,
you must update the role to continue having access. For more information, see the
[deprecated IAM permissions](https://docs.cloud.google.com/cloud-assist/deprecations/permissions)
document.

---
## 2026-04-06

### Custom IAM roles permission update for Gemini Cloud Assist

On April 8, 2026, Gemini Cloud Assist is replacing the
`cloudaicompanion.instances.completeTask` IAM permission with
`geminicloudassist.agents.invoke`. Updates to standard IAM roles
will be done automatically, but if you have access to Gemini Cloud Assist
through a custom IAM role, you must update the role before
April 8, 2026 to ensure continued access. For more information, see the
[deprecated IAM permissions](https://docs.cloud.google.com/cloud-assist/deprecations/permissions)
document.

---
## 2026-01-01

### Gemini Cloud Assist documentation migration

Gemini Cloud Assist release notes are now published here. If you are
looking for Gemini Cloud Assist release notes prior to January 2026,
see the [Gemini for Google Cloud release notes](https://docs.cloud.google.com/gemini/docs/release-notes).

---
