# Looker

## 2026-02-17

### Feature

Rolling out in preview starting February 17, 2026, LookML developers can unlock their Git branch in cases where their Git branch is locked as a result of another Git operation in progress or a previous Git operation failing. When the Git repository is locked, Looker displays the **Unlock Branch** option in the [**Git Actions** panel](https://docs.cloud.google.com/looker/docs/git-command-reference#git_actions_panel) of the Looker IDE. In addition, if a LookML developer tries to commit a change on a locked Git branch, Looker displays a warning in the **Commit** dialog, along with an option to delete the Git lock. See the [Using version control and deploying](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#unlock-branch) documentation page for details.

**Note:** This item was added on February 18, 2026.

### Feature

Rolling out in preview starting February 17, 2026, the **Self-service Explores** feature supports updating the data for a self-service Explore. The owner of a self-service Explore can update it with data from the latest version of the file that was used to create the self-service Explore. See the [Creating self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service#update-data) documentation page for more information.

### Feature

Rolling out in preview starting February 17, 2026, the **Self-service Explores** feature supports [uploading data from Google Sheets](https://docs.cloud.google.com/looker/docs/exploring-self-service#from-sheets). To support uploading data from Google Sheets, your Looker admin must [enable the required APIs](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore#enable-apis) in the Google Cloud project that houses your BigQuery database.

### Feature

Rolling out in preview starting February 17, 2026, the **In-database merge queries** feature is supported for [merging results](https://docs.cloud.google.com/looker/docs/merged-results) of two queries that are on the same BigQuery connection. Previously, the join for merging results was always performed in Looker memory, which limited each query to 5,000 rows that could be calculated in the join. If your Looker admin has enabled the [**In-database merge queries** Looker Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#in-database-merge-queries), the join between two queries that are on the same BigQuery connection is performed in the BigQuery database itself. Performing the join in the database is more performant and allows for unlimited rows that can be joined.

### Feature

The [System Activity User Activity dashboard](https://docs.cloud.google.com/looker/docs/system-activity-dashboards#user_activity_dashboard) has been updated to improve authentication troubleshooting. New information includes: recent login failures, the authentication method that was used, the error message that was returned, and the time of the attempt.

### Feature

Rolling out in preview starting February 17, 2026, the [content certification](https://docs.cloud.google.com/looker/docs/content-certification) feature includes several new updates:

* The [Settings](admin-panel-general-settings) page in the General section of the Admin panel now includes options that let admins enable or disable content certification, set a custom URL for the certification process, and control whether certification is revoked when content is edited.
* LookML dashboards can now be certified.
* Looks and dashboards that are based on uncertified self-service Explores now display the "ungoverned" badge.
* Searching for content now includes the ability to sort content based on its certification status.

### Feature

Now rolling out in preview starting February 17, 2026, Looker admins can grant the new [`schedule_without_limit` permission](https://docs.cloud.google.com/looker/docs/admin-users-roles#schedule_without_limit) to restrict a user's ability to [deliver all data results from a Look or an Explore](https://docs.cloud.google.com/looker/docs/delivering-looks-explores). This permission must be combined with another Looker permission that permits delivering data.

This permission will be automatically granted to any existing roles that already contain a data delivery permission. Looker admins must remove this permission from any users whom they wish to prevent from delivering all results from a Look or an Explore.

### Feature

Now rolling out in preview starting February 7, 2026, dashboard editors can [set default options for how the download of a dashboard tile includes query results](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#download-limit). They can set the download to include by default all query results or the current result table that is displayed in the visualization, or set a custom number of rows and columns. To enable this feature, a Looker admin must turn on the [**Tile Download Default Options** Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#dashboard-tile-download-limits).

### Feature

Now rolling out in preview starting February 17, 2026, dashboard editors can change the size and layout of dashboard tiles with more granularity. To enable this feature, a Looker admin must turn on the [**Granular Dashboard Sizing** Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#granular-dashboard-sizing).

### Feature

Rolling out in preview starting February 17, 2026, the [Embed Conversational Analytics Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#embed_conversational_analytics) is now available. When enabled, the Embed Conversational Analytics Labs feature lets you [embed Conversational Analytics conversations and agents in an iframe](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-embedding) like other Looker content types.

---
## 2026-02-09

### Feature

The Looker Action Hub has been updated to support newer API versions for Google Ads (from v19 to v22) and Facebook Custom Audiences (from v22 to v24).

### Breaking

When you use [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity), all System Activity fields of the `longtext` type that have a size greater than 2 MB will be truncated. If a table has only one column with a `longtext` type, that column will be set to a maximum of 1.9 MB in size. If a table has multiple columns of the `longtext` type, the total maximum size across all such columns is 2 MB, and this limit is distributed uniformly among those columns. For example, if a table has `x` `longtext` columns, each column will have a maximum length of 2 MB divided by `x`.

### Fixed

An issue has been fixed where some drill links could fail to work when cookieless embed was enabled. This feature now performs as expected.

### Feature

When you use [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity), the `merge_query` table now refreshes every 10 minutes.

### Feature

When you are [delivering content to an SFTP server](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_sftp_servers), additional key exchange algorithms and host key algorithms are now supported.

### Fixed

An issue has been fixed where the pagination option was not being displayed in the LookML Dashboards folder for some users.
This feature now performs as expected.

### Fixed

An issue has been fixed where custom dimensions that were based on numeric fields could be converted to strings, which caused incorrect sorting. This feature now performs as expected.

### Fixed

An issue has been fixed where choosing a non-default color collection and then choosing a custom color in a conditional formatting rule could cause the rule to revert to the default color collection. This feature now performs as expected.

### Announcement

**Looker 26.2** is expected to include the following changes, features, and fixes:

* Expected Looker (original) deployment start: **Monday, February 9, 2026**
* Expected Looker (original) final deployment and download available: **Monday, February 16, 2026**
* Expected Looker (Google Cloud core) deployment start: **Monday, February 9, 2026**
* Expected Looker (Google Cloud core) final deployment: **Friday, February 27, 2026**

### Fixed

An issue has been fixed where a modification to the color palette for the "Along a scale..." conditional formatting feature could fail to be saved. This feature now performs as expected.

### Feature

Now available in preview, Looker has full support for connections with [AlloyDB for PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-alloydb). When you [create a connection](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) in Looker, you can now select "Google Cloud AlloyDB for PostgreSQL" from the Dialect drop-down menu. This update does not affect existing AlloyDB connections that were created using the PostgreSQL 9.5+ option in the Dialect menu.

### Fixed

An issue has been fixed where non-admin users could not favorite
LookML dashboards. This feature now performs as expected.

### Feature

The user attribute pairing user interface for [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml), [LDAP](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-ldap), and [OpenID Connect](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect) authentication has been updated. A new "Manage Pairings" side panel provides a robust interface for adding, removing, and viewing attribute pairings. This new interface also includes filtering and pagination and allows for a single claim to be associated with multiple Looker user attributes.

### Fixed

An issue has been fixed where Looker could return a 500 error if a user with one or more single quotes in their name attempted to commit LookML. This feature now performs as expected.

### Fixed

An issue has been fixed where switching a visualization type from Table to Single Value could carry over unwanted conditional formatting. This feature now performs as expected.

### Fixed

An issue has been fixed where conditional formatting no longer appeared on certain dashboard tiles. This feature now performs as expected.

### Fixed

An issue has been fixed where changing the collection in a conditional formatting rule could reset styles for the rule. This feature now performs as expected.

### Fixed

An issue has been fixed where the filter bar would automatically expand on dashboard load when the filter location was set to "Right". This feature now performs as expected.

### Fixed

An issue has been fixed where switching filter types from `Matches (Advanced)` to another filter type could populate that filter with an incorrect filter configuration. This feature now performs as expected.

### Fixed

An issue has been fixed where adding a new field to a conditionally formatted result set could fail to apply the conditional formatting to the new field. This feature now performs as expected.

### Fixed

An issue has been fixed where dashboard tiles with titles that included the % symbol could not be downloaded in the Safari 26.0 browser. This feature now performs as expected.

### Feature

Looker admins can now [grant essential Google Cloud services](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist), such as [Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview), access to a Looker instance, even when an IP allowlist is active.

### Feature

Looker admins can now enforce a [password expiration policy](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-password#setting_password_expiration), enhancing security for users who authenticate with an email and a password. This new feature lets admins set a password expiration window between 30 and 365 days. Fourteen days before password expiration, a banner will notify the user, and, once their password has expired, the user must reset it at the next login.

### Feature

The [Customer Engineer Advanced Editor](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#customer_engineer_advanced_editor) default role now includes the `gemini_in_looker`, `chat_with_agent`, `chat_with_explore`, and `save_agents` permissions, which grant access to Gemini features and Conversational Analytics functionality.

---
## 2026-02-06

### Deprecated

The DataRobot [action](https://docs.cloud.google.com/looker/docs/actions-overview) is now deprecated. This action is no longer available in the Looker Action Hub.

---
## 2026-02-02

### Feature

Conversational Analytics now displays its reasoning for how it analyzes queries. After you enter your query, click [**Show reasoning**](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#show-reasoning) to see a plain text explanation of the steps that Conversational Analytics took to interpret your query.

---
## 2026-01-28

### Feature

You can now view the public [egress IP addresses](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) for Looker (Google Cloud core) instances that use Private Service Connect and controlled native egress. These IP addresses may be used when setting up [outbound connections](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#configure-outbound).

---
## 2026-01-26

### Feature

**Available January 29, 2026:** Conversational Analytics includes a **Show reasoning** toggle that provides step-by-step insight into how the agent reaches its answers. This update also includes improvements to overall answer accuracy. See the [Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview) documentation for details.

### Feature

Updates to the [Continuous Integration (CI)](https://docs.cloud.google.com/looker/docs/continuous-integration) feature will be available in February, 2026.

**Note:** This item was added on January 28, 2026 and updated on January 30, 2026.

### Feature

Gemini in Looker can now [generate a summary and an analysis of an Explore](https://docs.cloud.google.com/looker/docs/explore-summary-gemini).

### Feature

Now available in preview, the [**Configuration** tab of the **Projects Settings** page](https://docs.cloud.google.com/looker/docs/git-options#configuration) in the Looker IDE contains a **Delete Developer Copy** button that lets LookML developers delete their local developer copy of the project's Git repository. See the [Using version control and deploying](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#delete-dev-copy) documentation page for details.

### Announcement

**Looker 26.0** includes the following feature updates, which will start rolling out on January 26, 2026:

### Feature

The [**Self-service Explores** admin page](https://docs.cloud.google.com/looker/docs/admin-panel-self-service-explore) now supports a connection test button so that Looker admins can verify that the BigQuery connection is able to support self-service Explores.

### Feature

The [Tabbed Dashboards Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#tabbed-dashboards) is now available. The Tabbed Dashboards Labs feature lets dashboard editors organize dashboard content across multiple tabs within a single dashboard. Adding tabs to dashboards lets you do the following:

* Better organize content: Group related visualizations and tiles into separate tabs.
* Improve data storytelling: Guide viewers through different aspects of your data in a structured way.
* Enhance performance: Load only the tiles on an active tab, potentially speeding up initial dashboard load times.
* Reduce clutter: Consolidate multiple related analyses into a single dashboard.

This feature is only for Looker (original) instances and is enabled by default.

### Feature

The [Dashboard Filter Enhancements Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#dashboard-filter-enhancements) is now available. The Dashboard Filter Enhancements Labs feature includes the following improvements:

* Persistent filter suggestion drop-down: Filter suggestion drop-downs remain open for easier multi-selection for [tag list](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#tag-list) and [advanced filter type](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#advanced_filters) filters.
* Select or deselect all filter values: Lets users select or deselect all values in tag list and advanced filter type filters.
* Limit condition controls for advanced filters: Lets dashboard creators limit the condition options that are available to users for advanced filters.
* Enable [Include custom filter values](https://docs.cloud.google.com/looker/docs/presenting-content#adding_dashboards_to_boards_with_custom_filter_values_applied) by default for boards: Admins can choose to enable Include custom filter values for boards by default instance-wide.

This feature is only for Looker (original) instances and is enabled by default.

### Feature

The [Custom Tooltips Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#custom-tooltips) is now available. The Custom Tooltips Labs feature lets you configure tooltips within the Explore [visualization editor](https://docs.cloud.google.com/looker/docs/creating-visualizations#quick_guide) using a combination of UI settings and an HTML editor that supports Liquid templating.

This feature is only for Looker (original) instances and is enabled by default.

---
## 2026-01-14

### Feature

Looker (Google Cloud core) is now available in the asia-southeast3 (Bangkok) region. For more information, see the [Looker (Google Cloud core) locations](https://docs.cloud.google.com/looker/docs/looker-core-locations#asia-pacific) documentation.

---
## 2026-01-08

### Fixed

An issue has been fixed where Looker would generate inefficient SQL for some Databricks queries that included date manipulation for weekly data. Looker now uses Databricks functions like `date_trunc` when generating SQL.

### Fixed

For the Spanish (`es_ES`) locale, the weekday initials for Sunday and Tuesday in the schedule dashboard dialog have been set to the correct values (`D` and `M`).

### Feature

The JDBC driver for [Apache Spark 3+](https://docs.cloud.google.com/looker/docs/db-config-apache-spark) connections has been updated to version 2.7.6.

### Fixed

An issue has been fixed where applying filters to a Google Map visualization would require a refresh before the filters would take effect. This feature now performs as expected.

### Feature

[Custom mail settings that are configured for SMTP servers](https://docs.cloud.google.com/looker/docs/admin-panel-platform-smtp) now support OAuth 2.0 authentication.

### Fixed

An issue has been fixed where some columns in the Query Concurrency System Activity Explore were displaying null values. This feature now performs as expected.

### Feature

For [creating self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) from Excel files that contain multiple worksheets, the **Data upload** dialog now lets you specify which Excel worksheet to upload. Previously, the self-service Explore was always based on the first worksheet in the Excel file. **Note:** This item was added on January 15, 2026.

### Fixed

An issue has been fixed where a join wouldn't be added to the query, even if one was required by a measure of type `count_distinct`, `sum_distinct`, or `avg_distinct`.

### Fixed

An issue has been fixed where Looker would prevent users from uploading data if they lacked the `explore` permission. This feature now performs as expected.

### Fixed

An issue has been fixed where testing a connection could fail to return an error message in cases where the user had insufficient permissions or if the connection no longer existed. This feature now performs as expected.

### Feature

The LookML dashboards folder is now paginated, showing 30 dashboards per page.

### Fixed

When you use the Field Picker to clear all fields, the chart type no longer changes to Table (Legacy).

### Fixed

An issue has been fixed where strings with accented characters were not being displayed properly in the Y-Axis of a visualization. This feature now performs as expected.

### Fixed

An issue has been fixed where the Get LookML Model Explore API endpoint could time out without returning results. This feature now performs as expected.

### Fixed

An issue has been fixed where manually resetting column widths from a dashboard grid tile header had no effect. This feature now performs as expected.

### Fixed

An issue has been fixed where long content in tooltips could not be scrolled. This feature now performs as expected.

### Fixed

A retry limit has been added for scheduled jobs. If a scheduled job fails five times in a row, then it's skipped until the next time the schedule is triggered.

### Breaking

HTML characters are now displayed in plaintext in table visualizations to match other visualization types. For example, `&quot;` is no longer rendered as `"`.

### Announcement

**Looker 26.0** is expected to include the following changes, features, and fixes:

* Expected Looker (original) deployment start: **Monday, January 12, 2026**
* Expected Looker (original) final deployment and download available: **Monday, January 19, 2026**
* Expected Looker (Google Cloud core) deployment start: **Monday, January 12, 2026**
* Expected Looker (Google Cloud core) final deployment: **Friday, January 23, 2026**

### Fixed

An issue has been fixed where, after you uploaded data, Looker would not redirect you to the uploaded file. This feature now performs as expected.

### Feature

Looker now supports encrypted files for [key-pair authentication for Snowflake connections](https://docs.cloud.google.com/looker/docs/db-config-snowflake#key-pair).

### Fixed

The **Skip to Main Content** accessibility link for dashboards has been removed for embedded dashboards.

### Feature

When you [view folders on embedded content](https://docs.cloud.google.com/looker/docs/viewing-embedded-items#viewing_folders_on_embedded_looks_explores_and_dashboards), LookML dashboards are now visible. The LookML dashboards folder, however, will not be visible.

### Fixed

An issue has been fixed where a SQL Runner query against a model would fail if the user had not yet opened the model in Development Mode. This feature now performs as expected.

### Fixed

An issue has been fixed where merged queries could disappear if a user edited one of the settings in the Values tab for a field. This feature now performs as expected.

### Fixed

An issue has been identified and fixed in search where the latency in fetching search results spiked, causing search to be slow in returning results. A layer of caching has been added, causing search results to be more performant. **Note:** This item was added on January 13, 2026.

### Fixed

An issue has been fixed where the custom tooltip editor was unable to scroll to edit long tooltip templates. This feature now performs as expected.

### Fixed

An issue has been fixed where tooltip background colors were not being correctly rendered. This feature now performs as expected.

### Fixed

An issue has been fixed where certain fields in dialogs, such as the Format field in the Download dialog, were incorrectly labeled as read-only to screen readers. This feature now performs as expected.

### Fixed

An issue has been fixed where the dialog to select a folder would attempt to load a second page of results without being prompted by the user. This feature now performs as expected.

### Fixed

An issue has been fixed where `value_format` was not respected in table visualizations for numeric values larger than 16 digits. This feature now performs as expected.

### Fixed

An issue has been fixed where selecting the filter option "is before N hours ago" incorrectly displayed "is before N hours" in the filter.

### Fixed

An issue has been fixed where Looker extensions could not access webpack development servers. This feature now performs as expected.

### Fixed

An issue has been fixed where filters with commas were not including all filter conditions on Safari browsers. This feature now performs as expected.

### Fixed

An issue has been fixed where a table visualization could become unresponsive if a fixed column width was specified for multiple columns. This feature now performs as expected.

### Fixed

An issue has been fixed where downloading pivoted queries with table calculations while using an Exasol database could return an error. This feature now performs as expected.

### Fixed

An issue has been fixed where any Liquid usage in a derived table SQL resulted in full suggestions behavior. This feature now performs as expected.

### Fixed

An issue has been fixed where clicking **Status details** in the connection setup page without first selecting a dialect caused the page to crash. This feature now performs as expected.

### Fixed

An issue has been fixed where modifying conditional formatting rules other than the first one incorrectly affected the first rule. This fix has been backported to Looker versions 25.18.41 and 25.20.17.

### Fixed

An issue has been fixed where the **Show More** button wouldn't appear for large lists when a user was managing folder access. This feature now performs as expected.

### Fixed

An issue has been fixed where custom measures with invalid field references could cause queries to fail, even if those measures weren't selected in the query. This feature now performs as expected.

### Fixed

An issue has been fixed where the LookML Validator was not surfacing errors if an invalid field name was referenced in a `suggest_dimension` field. This feature now performs as expected.

### Fixed

An issue has been fixed where very long dashboard names were not properly truncated. This feature now performs as expected.

### Fixed

An issue has been fixed where an empty `sorts:` property in a LookML `explore` file definition could cause Looker to return a 500 error. This feature now performs as expected.

### Breaking

When you use [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity), the System Activity field `scheduled_plan.filters_string` is limited to a length of 1.9 MB. Any data beyond the 1.9 MB limit is truncated.

### Fixed

An issue has been fixed where tooltips incorrectly displayed the text `[object Object]`. This feature now performs as expected.

### Fixed

An issue has been fixed where the **Explore from SQL Runner query** feature could return an error if it found Liquid syntax in the query. The feature now exports the query as plaintext.

### Feature

The new LookML parameter [`autogenerate_primary_keys`](https://docs.cloud.google.com/looker/docs/reference/param-explore-autogenerate-primary-keys) parameter is now supported. When a view or Explore is defined with `autogenerate_primary_keys: yes`, Looker generates a temporary, distinct key for a view, allowing symmetric aggregates and one-to-many counts to be calculated correctly without any changes to your underlying database table. The primary key is generated at query runtime; it does not persist across queries. **Note:** This item was added on January 12, 2026.

### Feature

The JDBC driver for [Databricks](https://docs.cloud.google.com/looker/docs/db-config-databricks) connections has been updated to version 3.0.5.

### Fixed

An issue has been fixed where filtered custom measures could fail to load if they referenced a dimension that used the `alias` parameter in their filter. This feature now performs as expected.

### Fixed

An issue has been fixed where the **Show Totals** option in the Plot menu was not correctly hiding totals when a user downloaded results. This feature now performs as expected.

### Feature

The user interface for configuring group mappings for LDAP, SAML, and OpenID Connect has been updated for improved management. The new interface allows administrators to more easily add, edit, remove, and search for group mappings.

### Feature

Looker now supports conditional formatting rules for string types in single value and table visualizations.

### Feature

Looker now supports key-pair authentication in the [PDT overrides for Snowflake connections](https://docs.cloud.google.com/looker/docs/db-config-snowflake#pdt-overrides).

### Fixed

An issue has been fixed where downloaded reports with pivoted tables could contain extra whitespace. This feature now performs as expected.

### Fixed

An issue has been fixed where creating a custom dimension with a single letter name could cause the query to fail. This feature now performs as expected.

### Feature

The [**Tabbed Dashboards** Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#tabbed-dashboards) lets dashboard editors organize dashboard content across multiple tabs within a single dashboard. Adding tabs to dashboards lets you do the following:

* **Better organize content:** Group related visualizations and tiles into separate tabs.
* **Improve data storytelling:** Guide viewers through different aspects of your data in a structured way.
* **Enhance performance:** Load only the tiles on an active tab, potentially speeding up initial dashboard load times.
* **Reduce clutter:** Consolidate multiple related analyses into a single dashboard.

This feature will be available beginning January 26, for Looker (Original) instances, and will be disabled by default.

**Note:** This item was updated on January 20, 2026.

### Feature

Looker admins can now create dedicated [service accounts for API-only access](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#service-account). Additionally, eligible standard user accounts that are being used for API access can be [migrated](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#migrating) to the new service account type from the Users page in the Admin panel.

### Feature

The **Favoriting LookML Dashboards** Labs feature, which enables LookML dashboards to be [marked as favorites](https://docs.cloud.google.com/looker/docs/finding-content#navigating_to_content_in_folders) and displays them on the Looker Favorites tab, is now out of Labs and generally available.

### Feature

The [**Custom Tooltips** Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#custom-tooltips) lets you configure tooltips within the [Explore visualization editor](https://docs.cloud.google.com/looker/docs/creating-visualizations#quick_guide) using a combination of UI settings and an HTML editor that supports Liquid templating.

This feature will be available beginning January 26, for Looker (Original) instances, and will be enabled by default.

**Note:** This item was updated on January 20, 2026.

### Feature

The API endpoint `search_lookml_dashboards` is out of Labs and now generally available.

### Feature

The [**Dashboard Filter Enhancements** Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#dashboard-filter-enhancements) includes the following improvements:

* Persistent filter suggestion drop-down: Filter suggestion drop-downs remain open for easier multi-selection for [tag list](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#tag-list) and [advanced filter](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#advanced_filters) type filters.
* Select or deselect all filter values: Lets users select or deselect all values in tag list and advanced filter type filters.
* Limit condition controls for advanced filters: Lets dashboard creators limit the condition options that are available to users for advanced filters.
* Enable [**Include custom filter values**](https://docs.cloud.google.com/looker/docs/presenting-content#adding_dashboards_to_boards_with_custom_filter_values_applied) by default for boards: Admins can choose to enable **Include custom filter values for boards** by default instance-wide.

This feature will be available beginning January 26, for Looker (Original) instances, and will be enabled by default.

**Note:** This item was updated on January 20, 2026.

### Feature

LookML dashboards can now be [marked as favorites](https://docs.cloud.google.com/looker/docs/finding-content#navigating_to_content_in_folders), allowing the LookML dashboards to appear on the Looker Favorites tab.

### Feature

Looker (Google Cloud core) instances that use Private Service Connect can now connect to Google APIs through [controlled native egress](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#controlled-native-egress).

### Feature

The API endpoint `search_lookml_dashboards` is now generally available.

---
## 2025-12-23

### Feature

Historical data cannot be accessed with the API Usage System Activity Explore for Looker instances that are running Looker 25.16 or later. Looker instances that are running Looker 25.16 or later must use the [API Usage Hourly System Activity Explore](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#api_usage_hourly).

---
## 2025-12-03

### Feature

For Looker instances that are running Looker 25.20 or later, admins can now [test the connection](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions) between their instance and the Looker Action Hub. This option is available only for the Looker Action Hub. It is not available for [custom action hubs](https://docs.cloud.google.com/looker/docs/action-hub#setting_up_a_local_action_hub_server).

### Feature

Now available in preview, the [**Self-service Explore**](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature lets Looker users upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control. In addition, [content certification](https://docs.cloud.google.com/looker/docs/content-certification) is supported for self-service Explores.

---
## 2025-12-02

### Feature

Now available in preview, Looker can display a new [**Connected Sheets**](https://docs.cloud.google.com/looker/docs/connected-sheets-quicklink) option in the **Explore actions** menu. The **Connected Sheets** option opens Google Sheets and initiates a connection from Google Sheets to the Looker Explore. You can then build reports, pivot tables, or charts within the newly created Google Sheets using the fields available from the selected Looker Explore. The **Connected Sheets** quick link feature must be configured in the Google Cloud console and on your Looker instance. See the [Connected Sheets quick link](https://docs.cloud.google.com/looker/docs/connected-sheets-quicklink#admin-config) documentation page for details.

---
## 2025-12-01

### Feature

You can now use [Google-managed certificates](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-google-managed-certs) for Looker (Google Cloud core) instances that use Private Service Connect connections. This feature simplifies custom domain configuration by using a `*.private.looker.app` domain, eliminating the need to manage your own SSL certificates. Instances may need to [migrate](https://docs.cloud.google.com/looker/docs/looker-core-psc-migration) to the updated service attachment URI.

### Feature

You can now use [global access](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview#using_global_access) with Looker (Google Cloud core) instances that use Private Service Connect connections. Instances may need to [migrate](https://docs.cloud.google.com/looker/docs/looker-core-psc-migration) to the updated service attachment URI.

### Feature

The Looker–Tableau BI Connector is now available on [Tableau Exchange](https://exchange.tableau.com/products/1097). This means that for [Tableau Desktop](https://docs.cloud.google.com/looker/docs/tableau-connector#desktop) and [Tableau Server](https://docs.cloud.google.com/looker/docs/tableau-admin#server), you no longer need to manually download and install the Tableau connector (TACO) file. **Note:** This item was added on December 12, 2025.

### Feature

The Looker–Tableau BI Connector is now supported for Tableau Cloud, so that you can use a Looker Explore as a data source in Tableau Cloud. See the [Looker–Tableau BI Connector](https://docs.cloud.google.com/looker/docs/tableau-connector#cloud) documentation page for more information.

To use the Looker–Tableau BI Connector with Tableau Cloud, your admin must configure your Looker instance and your Tableau Cloud instance as described on the [Administering Tableau to Looker connections](https://docs.cloud.google.com/looker/docs/tableau-admin#cloud) documentation page.

---
## 2025-11-26

### Deprecated

The DataRobot [action](https://docs.cloud.google.com/looker/docs/actions-overview) will be deprecated on February 1, 2026. After that date, this action won't be available in the Looker Action Hub.

---
## 2025-11-19

### Feature

Now available in preview, the [**Self-service Explore**](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature lets Looker users upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

---
## 2025-11-17

### Feature

The [content certification](https://docs.cloud.google.com/looker/docs/content-certification) feature, when enabled, lets trusted users certify Looker dashboards and Looks to indicate that the content has gone through a manual review and is certified as reliable and trustworthy. This lets other users identify reliable content and confidently use that data for decision-making. **Note:** This item was updated on November 20, 2025.

---
## 2025-11-12

### Feature

[Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) is now generally available for Looker instances that are on Looker 25.18 or later. Use of Conversational Analytics in your Looker instance is now available without a Looker admin having to enable the **Trusted Testers** settings. Enablement of the **Gemini in Looker** setting is still required. Enablement of the **Trusted Tester Features** setting is still required when using the [Code Interpreter](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-code-interpreter) with Conversational Analytics in Looker.

For Looker (Google Cloud core) instances, this launch includes support for Conversational Analytics in instances that are within a VPC perimeter.

See the [Looker pricing](https://cloud.google.com/looker/pricing) page for pricing information.

(This release note was updated on November 13, 2025 to add pricing information.)

---
## 2025-11-11

### Feature

You can now schedule a daily, zero-downtime export for Looker (Google Cloud core) instances. For more information, see the [Create a scheduled export job for a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-scheduled-export) documentation page. This feature is being rolled out and will appear in all instances within a few weeks.

---
## 2025-11-05

### Feature

Looker 25.20 contains the following accessibility improvements:

* The character count for the custom message field of a schedule is now accessible to screen readers.
* The text for errors on custom filters is now accessible to screen readers.
* The list of visualization types in the Visualization section of an Explore is now accessible to screen readers.
* The reload button and corresponding "last refreshed" timestamp on a dashboard are now accessible to screen readers.
* The timezone selector on an Explore is now accessible to screen readers.
* The sort indicators in an Explore are now accessible to screen readers.
* The text formatting options in the Series tab of an Explore are now accessible to screen readers.
* Contrast is improved for elements that are selected when you set up dashboard filters.
* Contrast is improved for fields that are selected when Looker suggests a field name in the table calculations editor.
* Contrast is improved for tabs that are selected on the Schedule Delivery dialog.
* Contrast is improved for radio buttons that are selected on dialogs such as the download dialog.
* Dashboard filter options are no longer incorrectly classified as dialogs.
* The drill links in a single value visualization are now classified as buttons and can be accessed using the keyboard.
* The destination of an alert is now a required field.

### Breaking

Looker now recognizes results from the `YEAR` function as a number and not a date in MySQL 8.4. This change replicates the behavior of MySQL 8.0 and earlier.

To undo this change for a MySQL connection, add the following parameter to the Additional JDBC parameters section: `yearIsDateType=true`

### Feature

The [Max Number of PDT Builder Connections](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_number_of_pdt_builder_connections) limit has been increased from 10 to 100.

### Breaking

When you use [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity), the System Activity fields `sql_query.sql` and `sql_text.text` are limited to a length of 1.9 MB. Any data beyond the 1.9 MB limit will be truncated. (This release note was updated on November 10, 2025 to specify Elite System Activity.)

### Other

**Looker 25.20** is expected to include the following changes, features, and fixes:

* Expected Looker (original) deployment start: **Thursday, November 6, 2025**
* Expected Looker (original) final deployment and download available: **Thursday, November 13, 2025**
* Expected Looker (Google Cloud core) deployment start: **Thursday, November 6, 2025**
* Expected Looker (Google Cloud core) final deployment: **Tuesday, November 18, 2025**

### Fixed

An issue has been fixed where SQL Runner could return a `NoMethodError` when trying to query a LookML model that doesn't exist in the user's development mode. This feature now performs as expected.

### Fixed

An issue has been fixed where a measure of `type: period_over_period` could be referenced in the `sql` parameter for a measure of `type: number`. Attempting to do so now correctly displays an error in the LookML validator. This feature now performs as expected.

### Fixed

An issue has been fixed where the **Clear field keep filter** button on an Explore could incorrectly become disabled when a user used the field search bar in the field picker. This feature now performs as expected.

### Feature

The Visual Drilling feature is now out of Labs and generally available on the Admin > General Settings page.

### Feature

A new Labs feature, Internal Dashboard Theming, lets users apply predefined themes to a Looker dashboard. These themes, which are distinct from the themes that are used for embedded dashboards, can be managed by users with the `manage_internal_themes` permission.

### Fixed

An issue has been fixed where disabling the Favoriting LookML Dashboards Labs feature prevented users from moving LookML dashboards in folders. This feature now performs as expected.

### Feature

The Visual Drilling feature is now generally available on the Admin > General Settings page.

---
## 2025-10-31

### Feature

Looker (Google Cloud core) instances that use Private Service Connect now offer a simplified method for configuring outbound connections to external domains or the Looker Marketplace. For more information, see the [Configure outbound connections](https://cloud.google.com/looker/docs/looker-core-create-psc#configure-outbound) documentation.

---
## 2025-10-23

### Feature

**Conversational Analytics in Looker**

The following features are available in [Preview](https://cloud.google.com/products#product-launch-stages) for use with [Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) instances that are running Looker 25.18 or later:

* [Event and event attribute information](https://docs.cloud.google.com/looker/docs/events) is now available in [System Activity Explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#system_activity_explores).
* A [Conversational Analytics System Activity dashboard](https://docs.cloud.google.com/looker/docs/system-activity-dashboards#conversational_analytics) is now available to surface usage data for Conversational Analytics features in Looker, including the most popular data agents, the most popular Explores that are used in conversations, and the most active users.

### Feature

Looker now supports [cloning a public Git repository using an `https://` URL](https://docs.cloud.google.com/looker/docs/create-projects#cloning_a_public_git_repository_from_the_new_project_page). Looker does not support cloning Git repositories using `git://` URLs.

---
## 2025-10-21

### Feature

The new [Looker Status Dashboard](https://status.cloud.google.com/looker) provides real-time updates about service availability or disruptions for [Looker-hosted instances](https://cloud.google.com/looker/docs/choosing-hosting-option#looker-hosted-pros-cons). For more information, see the [Monitor Looker status](https://docs.cloud.google.com/looker/docs/status-dashboard-help) documentation page.

---
## 2025-10-10

### Feature

**Conversational Analytics in Looker**

The following features are available in [Preview](https://cloud.google.com/products#product-launch-stages) for use with [Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/studio/conversational-analytics-looker) instances that are running Looker 25.18.9 or later:

* New model-specific Looker permissions are available to manage and use the [Conversational Analytics data agents](https://docs.cloud.google.com/looker/docs/studio/conversational-data-agents-looker#before-you-begin) that are created to chat with Looker Explores. You can grant these permissions to users as part of a [custom role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create-custom-roles), or use one of two new [default roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), **Conversational Analytics Agent Manager** and **Conversational Analytics User**, to manage and use agents, respectively.
* You can now select up to five Looker Explores as data sources for a data agent in Looker.
* Users with the `admin_agents` permission can now [share data agents](https://docs.cloud.google.com/looker/docs/studio/conversational-data-agents-looker#share-data-agents) to let other users chat with your agent and its Explores. Starting in Looker 25.18.10, users with either the `save_agents` or the `admin_agents` permission can share data agents with other users.

(This release note was updated on October 10, 2025 to correct the Looker version for this release. This release note was updated on October 23, 2025 to correct the Looker version for data agent sharing permissions.)

---
## 2025-10-08

### Feature

**Conversational Analytics in Looker**

The following features are now available in [Preview](https://cloud.google.com/products#product-launch-stages) for use with [Conversational Analytics in Looker](https://cloud.google.com/looker/docs/studio/conversational-analytics-looker) instances that are running Looker 25.18 or later:

* New model-specific Looker permissions are available to manage and use the [Conversational Analytics data agents](https://cloud.google.com/looker/docs/studio/conversational-data-agents-looker#before-you-begin) that are created to chat with Looker Explores. You can grant these permissions to users as part of a [custom role](https://cloud.google.com/looker/docs/admin-panel-users-roles#create-custom-roles), or use one of two new [default roles](https://cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), **Conversational Analytics Agent Manager** and **Conversational Analytics User**, to manage and use agents, respectively.
* You can now select up to five Looker Explores as data sources for a data agent in Looker.
* You can now [share data agents](https://cloud.google.com/looker/docs/studio/conversational-data-agents-looker#share-data-agents) to let other users chat with your agent and its Explores.

(This release note was updated on October 9, 2025 to correct the Looker version for this release.)

---
## 2025-10-06

### Announcement

**Looker 25.18** is expected to include the following changes, features, and fixes:

* Expected Looker (original) deployment start: **Tuesday, October 7, 2025**
* Expected Looker (original) final deployment and download available: **Thursday, October 16, 2025**
* Expected Looker (Google Cloud core) deployment start: **Tuesday, October 7, 2025**
* Expected Looker (Google Cloud core) final deployment: **Monday, October 20, 2025**

### Feature

You can now set the Auto Resize Value setting on single value visualizations. This setting has no effect if the Smart Single Value Text Size setting is enabled on the Admin > General Settings page.

### Feature

The Athena JDBC driver version has been upgraded from 2.1.5 to 2.2.2. The Athena JDBC driver is used for connections to [Amazon Athena](https://docs.cloud.google.com/looker/docs/db-config-amazon-athena).

### Changed

Conversational Analytics users with the `save_agents` permission can now [share data agents](https://docs.cloud.google.com/looker/docs/studio/conversational-data-agents-looker), which lets other users chat with the data agent and its Explores. (This release note was added on October 9, 2025.)

### Fixed

Looker 25.18 contains the following accessibility improvements:

* You can navigate drill menus by using a keyboard.
* When you select a button toggle with a keyboard, the focus ring uses more contrasting colors.
* You can switch button toggles on or off by using the Enter key.
* When you use a keyboard to select a Look, dashboard, or folder that's inside a folder, a focus ring will appear around the selected item.
* You can now use a keyboard to edit boards.
* You can now use the keyboard to access LookML field definitions in the field picker.
* The Alerts dialog is now compatible with screen readers.
* The Series tab of the visualization editor is now compatible with screen readers.
* Tile notes are now added to ARIA descriptions.
* Actions for pivot columns are now accessible with a keyboard.
* The color contrast has been improved on large text boxes such as the custom filter editor.
* The options in the visualization settings panel now have names that can be read by screen readers.
* The state of expanded dialogs on the Explore page, such as the field picker and visualization settings panel, can now be read by screen readers.

### Fixed

An issue has been fixed where, when dashboard filters were updated, column widths could resize on table visualizations that included pivoted values. This feature now performs as expected.

### Fixed

An issue has been fixed where non-string values that were entered in the expression element of the `dynamic_fields` section of a LookML dashboard could cause the LookML validator to crash. This feature now performs as expected.

### Fixed

An issue has been fixed where subtotal values could display incorrect values after a filter was added or updated. This feature now performs as expected.

### Fixed

An issue has been fixed where, when dashboard filters were updated, table visualizations could get incorrectly cropped to exclude the Total row and scroll bar. This feature now performs as expected.

### Fixed

An issue has been fixed where the Collapse Subtotal toggle wasn't collapsing subtotals on table visualizations. This feature now performs as expected.

### Fixed

An issue has been fixed where the maximum column limit warning could obscure the contents of a visualization. This feature now performs as expected.

### Fixed

An issue has been fixed where users couldn't sort tables that included pivoted values. This feature now performs as expected.

### Fixed

LookML dashboards that aren't deployed to production can no longer be moved into folders other than the LookML Dashboards folder.

### Fixed

LookML project parse errors now include the LookML file path as well as the line number of the error.

### Fixed

An issue has been fixed where Databricks connections that used OAuth could not be saved if the password field was blank. You can now use OAuth without entering a password on the connections page.

### Fixed

An issue has been fixed where users were sometimes unable to add line breaks to table calculations. This feature now performs as expected.

### Fixed

An issue has been fixed where certain countries would not be displayed when a custom TopoJSON file was used. The following country names are now supported:

* Czechia for Czech Republic
* Eswatini for Swaziland
* Brunei Darussalam for Brunei
* North Macedonia for Macedonia
* Timor-Leste for East Timor

### Feature

The Prerender iframes for custom visualizations feature is now generally available on the Admin > Content Guardrails page.

### Feature

The Smart single value text size feature is now generally available on the Admin > General Settings page.

### Feature

The API endpoint `search_lookml_dashboards` is now generally available. This endpoint is similar to the `search_dashboards` endpoint except that it searches LookML dashboards instead of user-defined dashboards.

### Feature

The Data History Playback feature is now generally available on the Admin > Settings page.

### Feature

The Reduce Filter Queries feature is now generally available on the Admin > Settings page.

### Breaking

Looker admins can no longer create or edit individual users' API keys. Instead, from the Admin > Users page, admins can enable users to manage their own API keys. Once a user has API key management enabled, they can create, view, edit, and delete their API keys from their Looker account page. **Note:** This item was changed on October 9, 2025 to specify that it supports Looker (Google Cloud core) only, and it was changed again on October 22, 2025 to indicate that it's a breaking change.

### Feature

The Prerender iframes for custom visualizations feature is now out of Labs and generally available on the Admin > Content Guardrails page.

### Feature

The Smart single value text size feature is now out of Labs and generally available on the Admin > General Settings page.

### Feature

The API endpoint `search_lookml_dashboards` is now out of Labs and generally available. This endpoint is similar to the `search_dashboards` endpoint except that it searches LookML dashboards instead of user-defined dashboards.

### Feature

The Data History Playback Labs feature is is now out of Labs and generally available on the Admin > Settings page.

### Feature

The Reduce Filter Queries Labs feature is now is now out of Labs and generally available on the Admin > Settings page.

---
## 2025-10-02

### Feature

The `sql_preamble` parameter now [supports Liquid statements](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-preamble#using_liquid_in_sql_preamble). This update is supported on Looker 25.12 and later versions.

---
## 2025-09-30

### Feature

The following features are coming soon for use with Conversational Analytics:

* New model-specific Looker permissions are available to [manage](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_ca_agent_manager) and [use](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_ca_agent_user) the [Conversational Analytics data agents](https://docs.cloud.google.com/looker/docs/studio/conversational-data-agents-looker) that are created to chat with Looker Explores. You can grant these to users as part of a custom role, or use one of two new default roles, [Conversational Analytics Agent Manager](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#conversational_analytics_agent_manager) and [Conversational Analytics User](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#conversational_analytics_user), to manage and use agents, respectively.
* You can now select up to five Looker Explores as data sources for a data agent.
* You can now [share data agents](https://docs.cloud.google.com/looker/docs/studio/conversational-data-agents-looker#share-data-agents) to let other users chat with your agent and its Explores.

**Note:** This release note was published prematurely. It was amended on October 8, 2025 to reflect that these features are coming soon and amended on October 14, 2025 to indicate that the features [have been launched](https://docs.cloud.google.com/looker/docs/release-notes#October_10_2025).

---
## 2025-09-23

### Feature

You can now [connect to your Looker instance with the Gemini CLI](https://cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox) using a dedicated [Gemini extension](https://github.com/gemini-cli-extensions/looker). The Gemini extension can run queries, create Looks and dashboards, and retrieve elements of your LookML models.

---
## 2025-09-10

### Announcement

**Looker 25.16** is expected to include the following changes, features, and fixes:

* Expected Looker (original) deployment start: **Monday, September 15, 2025**
* Expected Looker (original) final deployment and download available: **Thursday, September 25, 2025**
* Expected Looker (Google Cloud core) deployment start: **Monday, September 15, 2025**
* Expected Looker (Google Cloud core) final deployment: **Monday, September 29, 2025**

### Breaking

Looker no longer supports connections to Firebolt.

### Feature

Suggest queries now respect the concurrency limit in the connection configuration.

### Feature

The Spanner JDBC Driver has been updated to version 2.32.1. This driver is used for connections to [Google Spanner](https://cloud.google.com/looker/docs/db-config-cloud-spanner).

### Feature

The [Looker-Excel Connector](https://cloud.google.com/looker/docs/excel-connector) is now generally available. When your Looker admin enables the Looker-Excel Connector on the BI Connections admin page, Looker Explores display the Open in Excel option in the Explore gear menu. This option downloads the Explore results to a Windows PC in a format that Microsoft Excel recognizes.

### Feature

The [Looker–Power BI Connector](https://cloud.google.com/looker/docs/powerbi-connector) is now supported for [customer-hosted Looker instances](https://cloud.google.com/looker/docs/customer-hosted-installation-steps) and for Looker (Google Cloud core) instances that use [private connections](https://cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections). **Note:** This item was added on September 19, 2025.

### Feature

The [Looker–Tableau BI Connector](https://cloud.google.com/looker/docs/tableau-connector) is now supported for [customer-hosted Looker instances](https://cloud.google.com/looker/docs/customer-hosted-installation-steps) and for Looker (Google Cloud core) instances that use [private connections](https://cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections). **Note:** This item was added on September 19, 2025.

### Fixed

Looker 25.16 contains the following accessibility improvements:

* Improved keyboard navigation for embed folders.
* Added ARIA labels to filter drop-down menu items.
* Added ARIA labels to schedule options.
* Added focus rings to navigation links.
* Improved VoiceOver support for filter navigation.
* Added the ability for users to close modals by using the Esc key. Users will be prevented from closing modals this way if there are unsaved changes in the modal.

### Fixed

When you upload a p12 file to a database connection, Looker now checks that it is a valid file before completing the upload.

### Fixed

An issue has been fixed where adding multiple filters to the same field could cause filter conditions to overwrite each other. This feature now performs as expected.

### Fixed

An issue has been fixed where changing the size of a visualization could cause the visualization to flicker. This feature now performs as expected.

### Fixed

An issue has been fixed where users could enter color codes that were longer than six characters when they were updating custom color collections. This feature now performs as expected.

### Fixed

An issue has been fixed where Explore drill links would not open correctly if cookieless embed was enabled. This feature now performs as expected.

### Fixed

An issue has been fixed where generating a view inside a folder could fail if the folder's name contained special characters. This feature now performs as expected.

### Fixed

An issue has been fixed where generating an embed URL from a LookML dashboard could fail with the following error: `'models' param cannot be converted to an array of String`. This feature now performs as expected.

### Fixed

An issue has been fixed where loading JavaScript files for custom visualizations could take more than one second. This feature now performs as expected.

### Fixed

An issue has been fixed where non-admin users were unable to select a project when they added a connection. This feature now performs as expected.

### Fixed

An issue has been fixed where scheduled deliveries could fail with the following error message: `Async delivery failed due to errors Internal server error. [Google Cloud Storage] undefined`. This feature now performs as expected.

### Fixed

An issue has been fixed where subtotal rows could fail to appear in downloaded result sets. This feature now performs as expected.

### Fixed

An issue has been fixed where the OAuth client secret could not be updated in the Connections page. This feature now performs as expected.

### Fixed

An issue has been fixed where total references and row total references in table calculations could return the following error if there was no data: `Field either does not exist in the current query or is a measure.` This feature now performs as expected.

### Fixed

An issue has been fixed where updating a Spanner connection could fail to save changes. This feature now performs as expected.

### Fixed

An issue has been fixed where users with only the `embed_browse_spaces` permission could be incorrectly classified as Standard users instead of Viewer users. This feature now performs as expected.

### Fixed

An issue has been fixed where using the `matches_filter` function in custom filters could return an error. This feature now performs as expected.

### Fixed

An issue has been fixed where visualizations could render twice when they were first loaded on an Explore or a dashboard. This feature now performs as expected.

### Fixed

The Athena JDBC driver version has been downgraded from 2.2.1 to 2.1.5 to fix an issue with result set streaming. This feature now performs as expected. The Athena JDBC driver is used for connections to [Amazon Athena](https://cloud.google.com/looker/docs/db-config-amazon-athena).

### Fixed

Dashboards that are not configured to run on load no longer show past query results when you revisit the dashboard in the same browser session. You must click the Load button to run the queries again.

### Fixed

An issue has been fixed where the Collapse subtotal toggle on table visualizations was unresponsive. This feature now performs as expected.

### Fixed

An issue has been fixed where updating a customer-hosted instance could fail with the following error message: `Data import is in progress and some features will not be available`. This feature now performs as expected.

### Fixed

An issue has been fixed where SQL Runner could fail to return new results after running a second query. This feature now performs as expected.

### Feature

A new Labs feature, Favoriting LookML Dashboards, enables LookML dashboards to be [marked as favorites](https://cloud.google.com/looker/docs/finding-content#navigating_to_content_in_folders) causing the LookML dashboards to appear on the Looker Favorites tab.

### Feature

The Full Screen Visualizations Labs feature is now generally available. You can turn it on and off on the Admin - General page.

### Fixed

An issue has been fixed where updating the Host URL in the Admin - Settings page could fail to be saved. This feature now performs as expected.

### Fixed

An issue has been fixed where visualization templates could be edited by API users without the need for the `explore` permission.

### Feature

Looker (Google Cloud core) 90-day trial instances are now available.

### Feature

The Full Screen Visualizations feature is now generally available. You can turn it on and off on the Admin - General page.

---
## 2025-08-13

### Announcement

**Looker 25.14** is expected to include the following changes, features, and fixes:

* Expected Looker (original) deployment start: **Monday, August 18, 2025**
* Expected Looker (original) final deployment and download available: **Thursday, August 28, 2025**
* Expected Looker (Google Cloud core) deployment start: **Monday, August 18, 2025**
* Expected Looker (Google Cloud core) final deployment: **Monday, September 1, 2025**

### Feature

For projects that are enabled for the [New LookML Runtime](https://cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime), the [`synonyms` parameter](https://cloud.google.com/looker/docs/reference/param-field) is now supported. The `synonyms` parameter lets LookML developers provide additional context about their data that will help [Conversational Analytics](https://cloud.google.com/looker/docs/studio/conversational-analytics) and other features to answer questions more accurately.

### Feature

The [API Usage Hourly System Activity Explore](https://cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#api_usage_hourly) is now available. This Explore provides a detailed, hourly summary of the volume and performance of API calls that are made to your Looker instance.

### Feature

Denodo 9 databases are now supported.

### Feature

The Maria JDBC Driver has been updated to version 3.5.3. This driver is used for connections to [MySQL, MySQL 8.0.12+, MariaDB, SingleStore, SingleStore 7+](https://cloud.google.com/looker/docs/db-config-mysql-mariadb-singlestore), [Amazon Aurora MySQL](https://cloud.google.com/looker/docs/db-config-amazon-aurora-mysql), [Google Cloud SQL](https://cloud.google.com/looker/docs/db-config-google-cloud-sql), and HyperSQL. **NOTE:** This item was updated on September 10, 2025.

### Feature

The Athena driver has been updated to version 2.2.1. This driver is used for connections to [Amazon Athena](https://cloud.google.com/looker/docs/db-config-amazon-athena). **Note**: This change was made in Looker 25.10. This item was updated on August 18, 2025. **NOTE:** This item was updated on September 10, 2025.

### Feature

The Databricks JDBC driver has been upgraded to version 2.7.3. This driver is used for connections to [Databricks](https://cloud.google.com/looker/docs/db-config-databricks).
**Note**: This change was made in Looker 25.10. This item was updated on August 18, 2025 and September 10, 2025.

### Feature

A new JavaScript event, [`dashboard:tile:merge`](https://cloud.google.com/looker/docs/embedded-javascript-events#dashboardtilemerge), has been added.

### Feature

Looker now displays a notice to instance admins if the instance license has been revoked. Admins will have 14 days to correct any problems before the instance will be shut down.

### Feature

The following [Looker events](https://cloud.google.com/looker/docs/events) are now visible in the [System Activity Events Explore](https://cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#event):

* `create_project`
* `delete_project`
* `update_project`
* `create_git_deploy_key`
* `delete_repository_credential`
* `update_repository_credential`

### Feature

A new Customer Engineer Advanced Editor [default role](https://cloud.google.com/looker/docs/admin-panel-users-roles#customer_engineer_advanced_editor) has been added and can be used to [grant support access](https://cloud.google.com/looker/docs/admin-panel-general-support-access) to Google Cloud customer engineers.

### Feature

The [Query Concurrency System Activity Explore](https://cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#query_concurrency) is now available. This Explore can help you identify periods of high load and investigate performance bottlenecks that are related to database connection limits. **Note:** This feature was included in the Looker 25.12 release notes but its launch was delayed.

### Feature

New visualizations have been added to the [Database Performance dashboard](https://cloud.google.com/looker/docs/system-activity-dashboards#database_performance) and the [Instance Performance dashboard](https://cloud.google.com/looker/docs/system-activity-dashboards#instance_performance) in System Activity.

### Feature

The following updates have been made for [Period-over-period (PoP) measures](https://cloud.google.com/looker/docs/period-over-period):

* The PoP measure feature is out of Preview and is now generally available. **Note:** This item was added on August 21, 2025.
* PoP measures are now supported for MySQL 8.0.12+ connections to Looker. **Note:** This item was added on August 18, 2025.
* You can now specify the following types of measures in the PoP measure's [`based_on`](https://cloud.google.com/looker/docs/period-over-period#based_on) parameter: [`list`](https://cloud.google.com/looker/docs/reference/param-measure-types#list), [`median`](https://cloud.google.com/looker/docs/reference/param-measure-types#median), [`median_distinct`](https://cloud.google.com/looker/docs/reference/param-measure-types#median_distinct), [`number`](https://cloud.google.com/looker/docs/reference/param-measure-types#number), [`percentile`](https://cloud.google.com/looker/docs/reference/param-measure-types#percentile), [`percentile_distinct`](https://cloud.google.com/looker/docs/reference/param-measure-types#percentile_distinct). **Note:** This item was added on August 21, 2025.
* For queries with PoP measures and time-based filters, in order to calculate data for the PoP measure Looker now automatically retrieves an extra time period of the coarsest time granularity in the query. (Previously, the user was required to adjust the granularity of time-based filters in order to account for the PoP measure calculations.) **Note:** This item was added on August 21, 2025.
* For queries with PoP measures, if no time-based dimensions are included in the query from the Explore's field picker, Looker can now infer the time period from time-based dimensions in the Explore's filters. (Previously, for queries with PoP measures, the user was required to specify a time-based dimension from the Explore's field picker.) See [Requirements for Explore queries with PoP measures](https://cloud.google.com/looker/docs/period-over-period#explore-requirements) for more information. **Note:** This item was added on August 21, 2025.
* PoP measures are now supported with [Connected Sheets](https://cloud.google.com/looker/docs/connected-sheets). **Note:** This item was added on August 21, 2025.

### Fixed

Looker 25.14 contains the following accessibility improvements:

* ARIA labels have been added to iframes that contain custom visualizations.
* ARIA labels have been added to legends on visualizations.
* ARIA labels have been added to modals.
* ARIA labels have been added to the Looker page header and logo.
* ARIA labels have been added to untitled dashboard tiles.
* Keyboard focus has been improved on modals.
* Text contrast has been increased on banners.
* Dashboard filters stay in focus while users are typing.
* Users can use the Explore from here link in a drill menu by using the keyboard.
* Users can interact with Single Value visualizations by using the keyboard.
* PDF rendering progress messages have been updated to better integrate with screen readers.

### Fixed

The LookML validation spinner now correctly stops if there is an error with the server's validation process.

### Fixed

An issue has been fixed where a route that wasn't intended for embedding was allowed to be embedded. This feature now performs as expected.

### Fixed

An issue has been fixed where "Create view from table" would fail if it was initiated from a LookML subfolder. This feature now performs as expected.

### Fixed

An issue has been fixed where color palettes with Japanese labels could not be added or removed. This feature now performs as expected.

### Fixed

An issue has been fixed where getting LookML for dashboards wouldn't preserve all query filters even if they overlapped with dashboard-level filters. This feature now performs as expected.

### Fixed

An issue has been fixed where `include` statements for empty folders that used single-slash syntax returned an unrecognized project reference error. This feature now performs as expected.

### Fixed

An issue has been fixed where multiple tooltips could be displayed at once. This feature now performs as expected.

### Fixed

An issue has been fixed where project names weren't fully sanitized. This feature now performs as expected.

### Fixed

An issue has been fixed where projects that have not been deployed to production wouldn't appear in a user's list of available projects. This feature now performs as expected.

### Fixed

An issue has been fixed where removing fields from embedded dashboard tiles could become impossible. This feature now performs as expected.

### Fixed

An issue has been fixed where resetting a project's git connection and attempting to use a bare repo would fail. This feature now performs as expected.

### Fixed

An issue has been fixed where sorting a pivoted column in the drill modal could sort all pivoted columns instead of just the selected one. This feature now performs as expected.

### Fixed

An issue has been fixed where special characters such as slashes, ampersands, and question marks were allowed in BigQuery and Spanner connection names. This feature now performs as expected.

### Fixed

An issue has been fixed where the HTTP error codes for moving and copying dashboards and Looks could return 422 when they should return 404. This feature now performs as expected.

### Fixed

An issue has been fixed where the last accessed time for Looks that were saved to a dashboard as Looks wasn't updated when the dashboard was accessed. This feature now performs as expected.

### Fixed

An issue has been fixed where the MoreVert button would not be disabled when no options were available in the menu. This feature now performs as expected.

### Fixed

An issue has been fixed where the new dashboard name wasn't preserved when a LookML dashboard was copied to a folder. This feature now performs as expected.

### Fixed

An issue has been fixed where unfavoriting a dashboard or Look on a board would not persist. This feature now performs as expected.

### Feature

**Note:** This item was removed on August 27, 2025.

---
## 2025-07-25

### Announcement

The [Code Interpreter in Conversational Analytics](https://cloud.google.com/looker/docs/studio/conversational-analytics-code-interpreter) is available in [Preview](https://cloud.google.com/products#product-launch-stages) for Looker (original) and Looker (Google Cloud core) instances. The Code Interpreter translates your natural language questions into Python code and executes that code to provide advanced analysis and visualizations. The Code Interpreter is disabled by default.

* Looker (original) instances must be on Looker 25.8 or later. Looker admins can manage enablement for the Code Interpreter on the [**Gemini in Looker** admin page](https://cloud.google.com/looker/docs/admin-panel-platform-gil#enable-and-disable-gil-original) of the Looker (original) instance.
* Looker (Google Cloud core) instances must be on Looker 25.10 or later. Looker admins can manage enablement for the Code Interpreter on the [**Gemini in Looker** admin page](https://cloud.google.com/looker/docs/looker-core-admin-gemini#enable-ci-core) of the Looker (Google Cloud core) instance.

---
## 2025-07-24

### Announcement

**Looker 25.12** is expected to include the following changes, features, and fixes:

* Expected Looker (original) deployment start: **Monday, July 28, 2025**
* Expected Looker (original) final deployment and download available: **Thursday, August 7, 2025**
* Expected Looker (Google Cloud core) deployment start: **Monday, July 28, 2025**
* Expected Looker (Google Cloud core) final deployment: **Wednesday, July 30, 2025**

### Breaking

Because of security concerns, text tiles no longer support the `form` and `input` Markdown elements.

### Feature

The Oracle JDBC driver has been updated to version 19.25.

### Feature

For faster response time for queries in BigQuery, Looker will execute BigQuery queries by using [`jobCreationMode=JOB_CREATION_OPTIONAL`](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query#jobcreationmode). If BigQuery can return immediate results, it will run the query without creating a job, so the record in the Looker query history will have a BigQuery query ID instead of a BigQuery job ID. See the [Understanding query performance metrics](https://cloud.google.com/looker/docs/query-performance-metrics#bigquery_bi_engine_metrics) documentation page for more information about the BigQuery BI Engine metrics.

### Feature

The [Query Concurrency System Activity Explore](https://cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#query_concurrency) is now available. This Explore can help you identify periods of high load and investigate performance bottlenecks that are related to database connection limits. **Note:** This feature launch was delayed and is now available in Looker 25.14. This item was updated on August 13, 2025.

### Fixed

An issue has been fixed where certain API calls would fail to time out and would instead run indefinitely. **Note:** This item was added August 18, 2025.

### Fixed

Looker 25.12 contains the following accessibility improvements:

* Improved contrast for exit buttons on dialogs
* Improved contrast for checkbox borders

### Fixed

An issue has been fixed where pull requests could display a different user than the pull request's owner. This feature now performs as expected.

### Fixed

An issue has been fixed where the System Activity Query Metrics Explore was not reliably populating with data. This feature now performs as expected.

### Fixed

An issue has been fixed where API users could view a list of users on a Looker instance, even if they didn't have the `see_users` permission. This feature now performs as expected.

### Fixed

An issue has been fixed where the response headers from some API calls were not set by Looker. This feature now performs as expected.

### Fixed

An issue has been fixed where exploring from a dashboard tile while editing a dashboard could result in a permissions error, even if the user had permission to view the Explore. This feature now performs as expected.

### Fixed

An issue has been fixed where the row limit in an Explore could display a blank field when the row limit was set to 5,000. This feature now performs as expected.

### Fixed

An issue has been fixed where some users were unable to create or edit BigQuery OAuth connections. This feature now performs as expected.

### Fixed

An issue has been fixed where SQL Runner would display a blank page if a user changed the visualization type after pivoting on a dimension. This feature now performs as expected.

### Fixed

An issue has been fixed where some queries to the internal database were unoptimized, affecting instance performance. This feature now performs as expected.

### Fixed

An issue has been fixed where a visualization template could fail to be displayed in the list of templates if the name contained certain unicode characters. This feature now performs as expected.

### Fixed

An issue has been fixed where invalid query killing statements could cause unnecessarily verbose log outputs. This feature now performs as expected.

### Fixed

An issue has been fixed where API users without the `explore` permission could access visualization templates. This feature now performs as expected.

### Fixed

An issue has been fixed where Looker could return a 500 error while retrieving dashboard details if the details contained non-UTF-8 characters. This feature now performs as expected.

### Fixed

An issue has been fixed where forecasting didn't work properly on fields that were based on JSON data. This feature now performs as expected.

### Fixed

An issue has been fixed where Looker didn't properly sanitize slash characters in git references that were used for remote dependencies. This feature now performs as expected.

### Fixed

An issue has been fixed where fields could be sorted differently when a visualization was downloaded or scheduled as a PNG. This feature now performs as expected.

### Fixed

An issue has been fixed where the `all_connections` API call could ignore the `fields` parameter. This feature now performs as expected.

### Fixed

An issue has been fixed where a map visualization would display drill links for fields that were hidden from the visualization. This feature now performs as expected.

### Fixed

An issue has been fixed where some System Activity tables were missing the `element_id` field. This feature now performs as expected.

### Fixed

An issue has been fixed where subtotals could be incorrectly formatted in PDF downloads when an HTML parameter was defined on the field and the "Expand tables to show all rows" option was enabled. This feature now performs as expected.

### Fixed

The Looker IDE now checks for subparameters in local and remote dependencies and displays a more informative error if the subparameters are missing. Local dependencies must be defined with a project subparameter, while remote dependencies require both a `url` subparameter and a `ref` subparameter.

### Fixed

An issue has been fixed where editing a merged query in an embedded session would open in a new tab. This feature now performs as expected.

### Fixed

An issue has been fixed where Looker could generate duplicate SQL table references if a PDT referenced a table directly as well as through a join. This feature now performs as expected.

### Fixed

An issue has been fixed where some PDT regeneration events were not tracked in System Activity. This feature now performs as expected.

### Fixed

When an Explore is saved as a new dashboard, Looker will create advanced filter type dashboard filters, rather than drop-down type dashboard filters, for number type parameters.

### Fixed

An issue has been fixed where SAML authentication could fail for a Looker (Google Cloud core) instance. This feature now performs as expected.

### Fixed

An issue has been fixed where the Looker Marketplace toggle was not being displayed in Looker core instances for users who were granted Admin permissions with an IAM role. This feature now performs as expected.

### Fixed

An issue has been fixed where installing multiple drivers for the same database type on a customer-hosted instance could cause Looker to display an error. This feature now performs as expected.

---
## 2025-06-30

### Feature

The Fast Dev Mode Transition feature is out of Labs and is now generally available. The Fast Dev Mode Transition feature improves the performance of [Development Mode](https://cloud.google.com/looker/docs/dev-mode-prod-mode#development_mode) on your instance by loading LookML projects in read-only mode until a developer clicks the [Create Developer Copy](https://cloud.google.com/looker/docs/git-command-reference#create-developer-copy) button for the project. **Note:** This item was added on July 8, 2025.

### Feature

The Fast Dev Mode Transition feature is now available for Looker (Google Cloud core). The Fast Dev Mode Transition feature improves the performance of [Development Mode](https://cloud.google.com/looker/docs/dev-mode-prod-mode#development_mode) on your instance by loading LookML projects in read-only mode until a developer clicks the [Create Developer Copy](https://cloud.google.com/looker/docs/git-command-reference#create-developer-copy) button for the project. **Note:** This item was added on July 8, 2025.

---
## 2025-06-24

### Feature

The following feature is generally available for Looker reports:

* The Looker connector can now connect to a [private IP (private services access) only](https://cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) Looker (Google Cloud core) instance or to a [private IP (Private Service Connect)](https://cloud.google.com/looker/docs/looker-core-networking-options#psc) Looker (Google Cloud core) instance [using the Looker instance ID](https://cloud.google.com/looker/docs/looker-core-connect-to-private-ip-lsp-sil).

---
## 2025-06-11

### Announcement

**Looker 25.10** is expected to include the following changes, features, and fixes:

* Expected Looker (original) deployment start: **Tuesday, June 17, 2025**
* Expected Looker (original) final deployment and download available: **Thursday, June 26, 2025**
* Expected Looker (Google Cloud core) deployment start: **Monday, June 16, 2025**
* Expected Looker (Google Cloud core) final deployment: **Monday, June 30, 2025**

### Breaking

The [Embed SDK](https://cloud.google.com/looker/docs/embed-sdk-intro) has been upgraded to release 2.0.0. While the 2.0.0 API is backwards-compatible with Embed SDK 1.8.x, the underlying implementation has changed for some functionality. SDK 1.8.x exported a number of classes. SDK 2.0.0 replaces these classes with interfaces that are marked as deprecated (alternative interfaces are identified). We recommend that applications use the interfaces that have an 'I' prefix (the interfaces that have prefixes are identical to the interfaces that don't have them). Applications that are upgraded to SDK 2.0.0 should continue to work and behave as they did previously. To take advantage of the API improvements, some refactoring will be required. The following major changes are included in Embed SDK 2.0.0:

* Navigating between dashboards, Explores, and Looks no longer requires that an iframe be recreated. Instead, the `loadDashboard`, `loadLook`, `loadExplore`, and `loadUrl` methods can be used to navigate within the Looker iframe.
* `connect` now returns a unified connection rather than a connection that is related only to a dashboard, a Look, or an Explore. The unified connection allows embedding applications to detect a user navigating inside the iframe.
* Support for additional Looker embedded content has been added for Looker reports and query visualizations.

**Note:** This item was added on June 13, 2025.

### Feature

For period-over-period (PoP) measures, a new subparameter, [`value_to_date`](https://cloud.google.com/looker/docs/period-over-period#value_to_date), is available. When a PoP measure is defined with `value_to_date:yes`, Looker will calculate the amount of time in the current timeframe at the time that the query is run and apply that amount of time when it calculates the values for previous periods.

### Feature

The Firebolt JDBC driver has been updated to version 3.5.0.

### Feature

The Hive JDBC driver has been updated to version 4.0.1.

### Feature

The MS SQL JDBC driver has been updated to version 12.10.0.

### Feature

The Teradata JDBC driver has been updated to version 20.00.00.45.

### Feature

The Vertica JDBC driver has been updated to version 24.2.0-1.

### Feature

The new Content Guardrails admin panel lets Looker admins limit both the ability for users to add or execute merged results queries on dashboards and the use of the dashboard auto-refresh option. Limiting merged results queries and dashboard auto-refreshes can reduce the number of queries that are sent to the database and improve dashboard performance. **Note:** This item was added on June 12, 2025.

### Feature

The Looker [Continuous Integration (CI)](https://cloud.google.com/looker/docs/continuous-integration) features let you run tests on your LookML project to deliver more reliable, efficient, and user-friendly data experiences. You can use the CI validators to catch issues with SQL, data test, content, and LookML before they hit production to verify your LookML and prevent query errors for your users. You can also configure the CI validators to run automatically when a pull request is submitted to your LookML repository. **Note:** This item was added on June 23, 2025.

### Fixed

This release contains the following accessibility improvements:

* Increased contrast ratio for graphic elements, including icon bullets
* Improved contrast for download links and unemphasized text to comply with Web Content Accessibility Guidelines (WCAG) Level AA

### Fixed

The Tile Actions kebab menu now includes the name of the dashboard tile in its `aria-label` value.

### Fixed

An issue has been fixed where SDK API calls could return a 500 error if optional headers were not specified. The API calls now work as expected even if optional headers are not included.

### Fixed

An issue has been fixed where the PDT Override Service Account field was not available for connections that use OAuth credentials. This feature now performs as expected.

### Fixed

An issue has been fixed where the Manage Access dialog on a folder could load slowly if the Looker instance has a large number of groups. This feature now performs as expected.

### Fixed

An issue has been fixed where, previously, testing a new OAuth connection before saving would run connection tests on an empty connection. OAuth settings must now be saved before running connection tests. This feature now performs as expected.

### Fixed

The OAuth Tenant ID field will no longer appear in connections for which it is not relevant. The only connection type that supports this field is Trino.

### Fixed

An issue has been fixed where the API calls to run git connection tests would fail unless the user was in dev mode. These calls now work as expected whether the user is in production or development mode.

### Fixed

An issue has been fixed where drill downs wouldn't be displayed for a field if the first field value had null values. This feature now performs as expected.

### Fixed

An issue has been fixed where assigning the user attribute
`looker_internal_email_domain_allowlist` on the SAML config page would return a 500 error. This user attribute is not designed to be assigned at the user level, so the option to assign it has been removed from the SAML config page.

### Fixed

An issue has been fixed where restarting the Looker instance during a folder sync could cause the instance to fail to start.

### Fixed

An issue has been fixed where selecting fields from the Session view in the System Activity User Explore could cause fanout. This feature now performs as expected.

### Fixed

An issue has been fixed where the `count` table calculation function could return incorrect values if its inputs included a list with null values. This feature now performs as expected.

### Fixed

An issue has been fixed where the drill menu did not properly translate some entries when the locale was set to Swedish (sv\_SE). This feature now performs as expected.

### Fixed

An issue has been fixed where drilling on a query with subtotals could display incorrect values. This feature now performs as expected.

### Fixed

An issue has been fixed where filtering on a custom dimension that references a `datetime` type field could return the following error message: `No matching signature`. This feature now performs as expected.

### Fixed

An issue has been fixed where the LookML validator would return a 500 error if a LookML file contained a `sum_distinct` measure for a database that doesn't support `sum_distinct` measures. The LookML validator now returns a more descriptive error message.

### Fixed

An issue has been fixed where entering the value `12:00` in the Time field of an alert schedule dialog would input `00:00` instead.

### Fixed

An issue has been fixed where changes to PDT override settings would not be saved. This feature now performs as expected.

### Fixed

An issue has been fixed where PDTs could fail to rebuild with the following error message: `undefined method trace_id_hex`. This feature now performs as expected.

### Feature

You can now [embed Looker reports](https://cloud.google.com/looker/docs/embed-reports) on Looker (original) instances when Looker reports and the Embed Looker reports Labs features are enabled for your instance. Looker reports are available in preview.

### Fixed

An issue has been fixed where LDAP authentication could fail with the following error message: `no implicit conversion of Hash into String`. This feature now performs as expected.

### Feature

The [Code Interpreter in Conversational Analytics](https://cloud.google.com/looker/docs/studio/conversational-analytics-code-interpreter) is now available in [Preview](https://cloud.google.com/products#product-launch-stages). The Code Interpreter translates your natural language questions into Python code and executes that code to provide advanced analysis and visualizations. The Code Interpreter is disabled by default. Admins of Looker (Google Cloud core) instances can manage enablement for the Code Interpreter on the [Gemini in Looker admin page](https://cloud.google.com/looker/docs/looker-core-admin-gemini#enable-ci-core). **Note:** This item was added on June 23, 2025.

---
## 2025-06-09

### Announcement

Gemini in Looker will be enabled by default for Looker (original) instances that meet at least one of the following criteria:

* The Automated Gemini in Looker enablement and user management setting on the Settings page in the Looker Admin panel was previously enabled.
* The instance is updated to Looker 25.6 or later after June 9, 2025.

Instances that are hosted in the [EMEA region](https://cloud.google.com/looker/docs/looker-original-locations) and those that are enrolled in Looker's [Extended Support Release (ESR) program](https://cloud.google.com/looker/docs/standard-extended-support-release-program-overview) are exempt from automatic enablement.

Looker admins can still manage Gemini in Looker enablement manually on the [Gemini in Looker](https://cloud.google.com/looker/docs/admin-panel-platform-gil) page in the Admin panel.

### Feature

When the [Automated Gemini in Looker enablement and user management](https://cloud.google.com/looker/docs/admin-panel-general-settings#gemini_default_enablement) setting is enabled, the Gemini Default Users group
is created automatically for instances that use an [open system configuration](https://cloud.google.com/looker/docs/access-levels#open_and_closed_systems_of_access_to_folders). The Gemini Default Users group is populated automatically with all existing users and any new users who are added to the instance.

---
