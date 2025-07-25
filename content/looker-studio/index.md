# Looker Studio

## 2025-07-24

### Feature

**New report canvas sizes**

Two new preset canvas size options are available, letting you control the width and height of your report on the screen. The new options are size A4, available in portrait or landscape orientations.

[Learn more about report and page layout options.](https://cloud.google.com/looker/docs/studio/report-and-page-layout#canvas_size)

### Feature

**New alt text field for images**

You can now [add alt text to report images](https://cloud.google.com/looker/docs/studio/add-text-images-lines-and-shapes-to-your-reports#add_images) to make them accessible to screen readers. See the [Web Content Accessibility Guidelines (WCAG) guidelines on alt text](https://www.wcag.com/blog/good-alt-text-bad-alt-text-making-your-content-perceivable/#What_is_alt_text_and_who_does_it_benefit) for more information about writing alt text.

### Feature

**Looker connector enhancements**

Additional [calculated field functions](https://cloud.google.com/looker/docs/studio/limits-of-the-looker-connector) are now available in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

**Performance improvement for BigQuery data sources**

Report viewers may notice improved performance when the report uses a BigQuery data source.

The BigQuery connector supports short query optimized mode. In this mode, when BigQuery determines it can finish a query quickly, BigQuery prioritizes returning immediate results instead of creating a BigQuery job. Short query optimized mode may apply in the following situations:

* When the data source uses Viewer's Credentials
* When the data source uses Owner's Credentials but you are not the credential owner.

There is no change in user experience or report behavior for data source credential owners.

### Feature

**Highlight charts by filter**

The [Applied Filters panel](https://cloud.google.com/looker/docs/studio/about-filter-properties#multiple_filters_on_a_component) now lets you click on a filter to highlight all charts that the filter applies to.

### Feature

**Add descriptions to reports**

You can now add text descriptions to a report. The report search now matches the report title as well as the description.

### Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://lookerstudio.google.com/data):

* [Google Ads](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbzSwavmpb_HOJ-mGTQh58_JV1lqbY8tOcvry3mi_kFOESRMIb9UDCTimctyOo9lMBL4SQ) by Detrics
* [Facebook Insights](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbxEIVPCXZyTPZtOtQPQl0nPfgtEwdKKDFGTt8GYSN2q9aKaTakYIlKf8lqYeyNGGcUm) by Master Metrics
* [Instagram Insights](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbyrOltbWEyCaf6MLjLwsX_a7ny5xyCbGY4nrm0pyukmPLA9wD63ESClQ3UtETodJSS1) by Master Metrics
* [Youtube](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbxa0z7PzIBswipUWcFWPN5LRce5Rvb0KbSuR-hN05InreICPCvyso359bGFrG7_063i) by Master Metrics
* [Google Ads](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbx8LrzHexCTkTBGu5AJntmDe-q8IYWKMxF0DfphW9s6P4YdPh9OHDUk9nGWNqffyCuoPQ) by Master Metrics
* [Google Analytics 4](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbwZ-OALYuQvZPoMf4Zs3cRFBAgfc-lll8TYKN2qF6WDSpj6PrXqb9gScu2z_k_HOQK4Rg) by Master Metrics
* [Dashbo](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbx0NZ5e2MMISr6toZCb7PoxooYfIFuDdQwCW4oWnpxjtNfwR80SkV8aAiibLnKlCRTEDA) by Dashbo
* [Odoo Sign AppiWorks](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbxCH6kb7jGrVV36u6ZBiweYnJVWWKQd7tE1mZu7GVG_Vw6dmot89sL86giHoND-rh0t8g) by Jivrus Technologies
* [快客-GSC 串接](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycby-SaBW_LVIVAyuI7q1PQhqqKbwcxp0kaCrCYi0Wj3nVlIJFENFiWOQP_MvfCgpFpY) by 黑客數位
* [IntelliKid Systems](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbznaukKHnRM-AtDjqYNKotj8BCXBZdmlcLZw4cIhy67a1NjaJWQWF7Med9GEDAgDSPG) by IntelliKid Systems LLC
* [Odoo POS AppiWorks](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbxDTDWkPSwYKH096FJ-XK-KSr23-aEVeyxGeSgSTnpF3P8Rggd3ar5GgLeY0zK8FkQL) by Jivrus Technologies
* [Google PageSpeed Insights](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbzEvtbGv2c24ZXDnJ55sjQVYfmfvyjJlK-OajreKH_OQVxWq5TGFMahS-O62t76ZBLd) by Supermetrics

---
## 2025-07-17

### Feature

**Report abuse**

Looker Studio report viewers can now [report abusive content](https://cloud.google.com/looker/docs/studio/report-abuse). Content is automatically reviewed, and content that is reported as abusive is hidden or deleted.

### Feature

**Performance improvement for BigQuery data sources**

**Note:** This feature has been delayed and is currently not available. (Release note updated on July 21, 2025.)

Report viewers may notice improved performance when the report uses a BigQuery data source.

The BigQuery connector supports short query optimized mode. In this mode, when BigQuery determines that it can finish a query quickly, BigQuery prioritizes returning immediate results instead of creating a BigQuery job. Short query optimized mode may apply in the following situations:

* When the data source uses Viewer's Credentials
* When the data source uses Owner's Credentials but you are not the credential owner

There is no change in user experience or report behavior for data source credential owners.

---
## 2025-07-10

### Feature

**New alignment option for Cartesian charts**

The new **Align with grid** setting lets you set the alignment of the chart legend with the position of the chart grid, instead of aligning with the chart title.

This setting is available for Cartesian charts in reports that [have modern charts enabled](https://cloud.google.com/looker/docs/studio/modern-charts).

---
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
