# Looker

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

The [Query Concurrency System Activity Explore](https://cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#query_concurrency) is now available. This Explore can help you identify periods of high load and investigate performance bottlenecks that are related to database connection limits.

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
