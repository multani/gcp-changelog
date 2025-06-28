# Looker Studio

## 2025-06-26

### Breaking

**Don't display data in comparison metrics when Group others is enabled**

The **Group others** option could display incorrect data when used with [comparison metrics](https://cloud.google.com/looker/docs/studio/add-comparison-metrics-and-running-totals#differences_between_running_calculations_and_calculated_fields). Comparison metric fields now display the string `no data` when the **Group others** option is enabled on a chart.

### Feature

**Looker connector enhancements**

The Looker connector can now connect to a [private IP (private services access) only](https://cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) Looker (Google Cloud core) instance or to a [private IP (Private Service Connect)](https://cloud.google.com/looker/docs/looker-core-networking-options#psc) Looker (Google Cloud core) instance [using the Looker instance ID](https://cloud.google.com/looker/docs/looker-core-connect-to-private-ip-lsp-sil).

---
## 2025-06-18

### Feature

**Updates to Assets: search API endpoint**

The Assets: search API endpoint now includes a `previousPageToken` attribute in its response. This token allows API users to paginate forwards and backwards through the result set.

---
## 2025-06-03

### Announcement

**Pro feature: Gemini in Looker is enabled by default**

For Looker Studio Pro subscriptions that are created on or after June 3, 2025, [Gemini in Looker](https://cloud.google.com/looker/docs/overview-gemini) is enabled automatically. Looker Studio users with the [appropriate permissions](https://cloud.google.com/looker/docs/studio/enable-and-disable-gemini-in-looker-for-looker-studio#before_you_begin) can manage enablement on the **Gemini in Looker** page under **User Settings**.

---
## 2025-05-29

### Feature

**Pro feature: Code Interpreter is enabled by default**

The [Code Interpreter](https://cloud.google.com/looker/docs/studio/conversational-analytics-code-interpreter) for [Conversational Analytics](https://cloud.google.com/looker/docs/studio/conversational-analytics) is now enabled by default when the Gemini in Looker and Trusted Tester features settings are enabled for the Google Cloud project that is associated with a Looker Studio Pro subscription. The Code Interpreter in Conversational Analytics is a Preview feature that translates your natural language questions into Python code and executes that code to provide advanced analysis and visualizations.

Looker Studio users with the [appropriate permissions](https://cloud.google.com/looker/docs/studio/enable-and-disable-gemini-in-looker-for-looker-studio#before_you_begin) can manage enablement on the **Gemini in Looker** page under **User Settings**.

---
