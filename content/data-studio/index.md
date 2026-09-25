# Data Studio

## 2026-09-24

### Feature

**Bulk styling**

You can customize all series, dimensions, or metrics at once, or select an
individual item to style it separately. Styles that you set for an individual item override styles that you set for all items.

For more information, see the [Line chart and combo chart reference](https://docs.cloud.google.com/data-studio/line-chart-and-combo-chart-reference), [Time series reference](https://docs.cloud.google.com/data-studio/time-series-reference), and [Table reference](https://docs.cloud.google.com/data-studio/table-reference).

### Feature

**Connect to PostgreSQL (Private IP)**

You can connect Data Studio to PostgreSQL databases on Cloud SQL by using a private IP address. Private IP connections keep your database traffic on a private network instead of the public internet.

For more information, see [Connect to PostgreSQL](https://docs.cloud.google.com/data-studio/connect-to-postgresql).

### Deprecated

**MySQL 5.6 and 5.7 deprecation**

Support for MySQL 5.6 and 5.7 in the MySQL connector is ending:

* Creating new data sources that connect to MySQL 5.6 or 5.7 won't be possible after February 26, 2027.
* Data sources or reports that use MySQL 5.6 or 5.7 might not properly load data after February 26, 2027.

For more information, see [Connect to MySQL](https://docs.cloud.google.com/data-studio/connect-to-mysql).

### Feature

**Partner connection launch update**

The following partner connectors have been added to the Data Studio Connector Gallery:

* [Facebook Ads Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwiyh8LyfZyQ8aG5Fp39pCsIEccpSsK-w3j8y6N-ZB3-rZJX9-aUP9C0e1F5PivZ_Uv) By Langquang. Sources: Facebook Ads
* [Nextdoor](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx5xGzeuSxYpDnwhsjnEmprY9sB2h294iHRjaW4YoGxdc023iTwWfNVZQmxpIBe_CtzXA) By Windsor.ai. Sources: Nextdoor
* [Attentive](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz9s4Rb2k13vtaOIg9ZdqeEArMsmzI1ch3qfwGLP4DYgypHWJ_oHEpYKmDlJepMRV7x) By Windsor.ai. Sources: Attentive
* [Contractors Cloud](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz0G_xUNoIowgyV5SkOZrr6xknZbC-RrGQ68iyJt8Slhv4UrMB6hXx7_jkPniZuo9fxQw) By Windsor.ai. Sources: Contractors Cloud
* [AppLovin](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwa_VfDqwKV4nU-g91I3Du2yNkUjGo6IZrsS_SeU2nHWx0nnAZWWulop_gjr6se5C0l) By Windsor.ai. Sources: AppLovin
* [SEOmonitor](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwrkqEETu9VxmB6PY9qjlewyPaHdOeIVv-CmeqNMIUMB_8869OUENmB2kXa-duMY9kl) By SEOmonitor. Sources: SEOmonitor
* [SimilarWeb](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxeFsVMVREcnL3ONWeGosaa_PxhjKR7CVJYvCuE93sQEpka6Yf9oPohdv_D4LLSvEGr) By Windsor.ai. Sources: SimilarWeb
* [Salesforce](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxNSTS9Oxw51dEWq547XhMy73Sw44hFa6w2gK-dYOchos0do-ovfa9buYXSUn6q9reJzA) By Dataslayer. Sources: Salesforce
* [Facebook Ads (Meta Ads)](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwg5L8WnTzgsyCMHmKhyGoX1OadvEpaGeothozHT7ae4nNKim0hfATfgIojdpSL1xKC) By Datablaster. Sources: Meta Ads
* [Google Search Console](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw3JAdju3IIS5dA47OcoGjShqKNQ_Z9N0r24m-FPdlX1gQa_-ld2tbbIhaTh69DCM3Qqw) By Data Bloo. Sources: Google Search Console
* [CleverReach](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxljd9HY3q4bpQLfC_RdgImEcv7-ZvieLYsE53biXnKF8V5C1HVCSAqOKBoxsk4gCIO3Q) By Power My Analytics. Sources: CleverReach
* [Cin7 Core AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyunnrPcqWgRkYHecPxUfGrZTQnFuK9jynShqfP5ig3OdT0KS8A_ztUIwFup0gBHZ6kxA) By Jivrus Technologies. Sources: Cin7
* [Mangools AI Search Watcher](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwcwpBC1B5lfxYrqd_80uzzwnxWaOjKKo7ArfjglcnnreHZ-3WTwUVTMyIayLT-mmp0UQ) By Mangools.com. Sources: Mangools
* [Amazon Vendor Central](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx2W2J3Wc7U9ExmzjSBV0q2RtRR_DwLzpNP7xcP4TtxHoA5lBPQsExmLlde7qQHKy5OWw) By Power My Analytics. Sources: Amazon
* [快客-Microsoft Ads 串接](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwe2lMdXwfn76g7H0G3MnUrYmkerlw5koa5Q-69AcT0ty_fZCXjMDW8PBJrryUlYj0b) By 黑客數位. Sources: Bing Ads
* [Leadinfo](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby1g9ueAD9P0wfa-EI5h_PYZU4W4bpHxkit_X5Vt-5iuY5QXxap3_pftCvbvPtlypgOow) By Leadinfo. Sources: Leadinfo

---
## 2026-08-13

### Announcement

The following features are rolling out over the next week.

### Feature

**Fullscreen charts**

You can view individual charts in fullscreen mode. Click the fullscreen
button in the chart header to expand the chart. This feature is not available
for scorecards and gauge charts.

### Feature

**Rotate components**

You can rotate text boxes, images, and shapes in Data Studio. Report
creators can rotate these components on a non-responsive canvas and can reset
the rotation to 0 degrees.

### Feature

**Center labels on stacked bar charts**

You can position labels in the center of stacked bar charts. If
insufficient space is available to center the label within the bar, the label
is displayed outside the bar.

For more information, see the [Bar chart and column chart
reference](https://docs.cloud.google.com/data-studio/bar-chart-and-column-chart-reference).

### Feature

**Search for settings**

You can search for settings in the **Setup** and **Style** tabs of the
[properties panel](https://docs.cloud.google.com/data-studio/properties-panel).

### Feature

**Copy chart as image**

You can copy a chart as a PNG image to your clipboard.

### Feature

**Bubble chart border color**

You can modify the border color of bubbles in bubble charts.

---
## 2026-07-30

### Announcement

The following features are rolling out over the next week.

### Feature

**Conversational Analytics is generally available**

Conversational Analytics in Data Studio is now generally available. You can now filter your [data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-data-agents#start-a-conversation-with-an-agent) by the Google Cloud project to which they belong. Agents that require additional permissions are now displayed with an **Unavailable** label.

### Feature

**Email notifications when sharing Conversational Analytics data agents**

When you [share data agents](https://docs.cloud.google.com/bigquery/docs/create-data-agents#share-data-studio-users) that were created in BigQuery with Data Studio users, you can opt to send an email to notify those users of their access to the agent.

---
## 2026-06-18

### Feature

**Viewer data refresh**

Report editors can now allow report viewers to manually refresh report data. When editors enable the new **Viewer data refresh** option in [report settings](https://docs.cloud.google.com/data-studio/report-settings#viewer-data-refresh), viewers can refresh data for a component by right clicking the component, or refresh data for a report by selecting the option in the three-dot menu.

---
## 2026-06-11

### Feature

**Pro feature: Security and compliance enhancements**

The following features are now available to help you meet your organization's security and compliance needs. These features are only available for Data Studio Pro.

* **[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/data-studio/cmek)**: Use your own cryptographic keys to protect Data Studio Pro assets.
* **[Customer-managed storage](https://docs.cloud.google.com/data-studio/cms)**: Store your file uploads in your own Cloud Storage bucket and your data extracts in your own BigQuery dataset.
* **[Data residency](https://docs.cloud.google.com/data-studio/data-residency)**: Keep your data physically within a geographical area.

---
## 2026-06-01

### Feature

**Regionalization in CA in Data Studio**

Conversational Analytics in Data Studio now supports multi-region BigQuery data agents.

[Learn more about Conversational Analytics in Data Studio](https://docs.cloud.google.com/data-studio/conversational-analytics-overview).

---
