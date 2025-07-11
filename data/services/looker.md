# Looker

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
