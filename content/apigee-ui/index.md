# Apigee UI

## 2025-12-19

### Announcement

On December 19, 2025, we released an updated version of Apigee Monetization.

**Note:** Rollouts of this release to production instances have begun. Rollout may
take four or more business days to complete across all Google Cloud zones. Your
instances may not have the feature available until the rollout is complete.

### Feature

Monetization now supports AppGroups. Use AppGroups to manage API product
subscriptions for all app developers in the AppGroup at the same time.

For more information, see
[Use AppGroups to manage API product subscriptions](https://cloud.google.com/apigee/docs/api-platform/monetization/overview#use-appgroups-to-manage-api-product-subscriptions).

---
## 2025-12-17

### Announcement

On December 17, 2025, we announced that Debug v1 will be shutdown on
January 15, 2026. Use
[Debug v2](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace)
instead of Debug v1.

### Announcement

On December 17, 2025 we released a new version of the Apigee integrated portal.

### Fixed

**Incorrect Cross-Origin-Opener-Policy header in developer portal**

A fix has been implemented to address an issue where the
`Cross-Origin-Opener-Policy` response header in the developer portal was
malformed with an extra colon. This change ensures the security header is
correctly formatted.

---
## 2025-11-17

### Fixed

| Bug ID | Description |
| --- | --- |
| 446973091 | **Proxy editor endpoint view is now disabled if there are over 200 flows configured in proxy endpoints.**  When opening the proxy editor endpoint view with a proxy that has over 200 flows, the proxy graph is no longer rendered, and instead you are presented with a message informing you that there are too many flows to render. This action addresses a performance issue that made the proxy editor unusable when there were over 200 flows configured. |

### Announcement

On November 17, 2025, we released an updated version of the Apigee UI.

### Announcement

On November 17, 2025 we released an updated version of Apigee Analytics.

### Feature

**Support for aggregate data in Error Code Analysis, Cache Performance, and Target Performance charts**

Announcing support for viewing aggregate data in the Error Code Analysis, Cache
Performance, and Target Performance Analytics dashboards.

For information on the Analytics dashboards, see
[Use the Analytics dashboards](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-analytics-dashboards).

---
## 2025-11-12

### Announcement

On November 12, 2025, we released an updated version of the Apigee UI.

### Fixed

| Bug ID | Description |
| --- | --- |
| 455584175 | **Fixed a performance issue with Debug session UI**  Fixed an issue where performance of the Debug session was severely degraded when loading a Debug session with a moderate number of transactions. |

---
## 2025-11-10

### Announcement

On November 10, 2025 we released an updated version of Apigee.

### Feature

**Support for new Apigee Analytics regions**

This release introduces Apigee Analytics support for these new regions:
Hong Kong (`asia-east2`) and São Paulo (`southamerica-east1`).

**NOTE:** Apigee Advanced API Security does not support these new regions at this
time.

For a list of all of the supported Analytics regions, see
[Available Apigee API Analytics regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-analytics-regions).

---
## 2025-11-02

### Announcement

On November 2, 2025, we released an updated version of the Apigee UI.

### Deprecated

The Apigee Classic UI shutdown is complete. The shutdown was finalized on
November 2, 2025, completing the migration of Apigee to the Google Cloud console.
All Apigee functionality is now available in the Apigee UI in the
Google Cloud console.

See the [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) page for more details.

---
## 2025-10-30

### Announcement

On October 30, 2025, we released an updated version of the Apigee UI.

### Fixed

| Bug ID | Description |
| --- | --- |
| 443120120 | **Fixed an issue where an incorrect target URL or cURL command was displayed in the proxy debug properties window.**  New generated debug sessions now contain information in a flow info event that describes the values used by the proxy to call the target endpoint. The debug UI displays these values and uses them to generate the target URL and curl command displayed in the debug properties window when the target request event is selected. If some of the header fields are masked in the debug session, a warning appears next to the **Copy cURL** button. If the headers are truncated due to system limitations, **Copy cURL** is disabled.  Older debug sessions that do not have the new target endpoint information no longer attempt to display the target URL or generate a cURL command as they were unreliable. A dialog is displayed warning you of this when attempting to open older debug sessions. |

---
## 2025-10-07

### Announcement

On October 7, 2025, we released an updated version of the Apigee UI.

### Feature

**Output from print statements is now displayed in the Debug session viewer**  
  
A new option has been added to the transaction navigation table header in the Debug session viewer that opens the **Transaction output** window. The **Transaction output** window displays `print()` output from either *all transactions* in the debug session, or a *specific transaction* from the session. See [Creating a debug session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace#create) for details.

---
## 2025-09-24

### Announcement

On September 24, 2025, we released an updated version of Apigee.

### Feature

**ApigeeBackendService for the Apigee Operator for Kubernetes (GA)**

The ApigeeBackendService resource for the Apigee Operator for Kubernetes is [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages).

This new resource enables the integration of the Apigee Operator for Kubernetes with the [Google Kubernetes Engine (GKE) Inference Gateway](https://cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway). The GKE Inference Gateway is an extension to the GKE Gateway that provides optimized routing and load balancing for serving generative Artificial Intelligence (AI) workloads. It simplifies the deployment, management, and observability of AI inference workloads.

With this new integration, GKE Inference Gateway users can now leverage Apigee's full suite of features to manage, govern and monetize their AI workload through APIs.

To learn more, see [Create an ApigeeBackendService](https://cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice).

---
## 2025-09-19

### Announcement

On September 19, 2025, we released an updated version of the Apigee UI.

### Fixed

| Bug ID | Description |
| --- | --- |
| 444579842 | **Fixed browser hang issue when uploading large bundles**. Fixed an issue where the browser would hang when creating a new proxy or proxy revision from a large uploaded zip bundle. |

---
## 2025-09-14

### Announcement

On September 14, 2025, we released an updated version of the Apigee UI.

### Feature

**Added icon to proxy and sharedflow editor to mark unused policies**

If a policy has yet to be [attached to any flow](https://cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui#attaching-a-policy-to-a-flow) in the configuration, an icon now displays next to that policy in the Proxy Editor side navigation to signify that the policy is currently unused in the proxy or sharedflow.

---
## 2025-08-26

### Announcement

On August 26, 2025, we released an updated version of the Apigee UI.

### Feature

**Debug view settings are now retained when switching between transactions**

When switching between transactions in the debug view the following view settings are now retained:

* The state of the expand all toggle
* The zoom level of the graph
* The positioning of the viewport in the graph (best effort). This may be modified due to discrepancies in between the transactions
* The search filter. The active match will go into an indeterminate when switching transactions.

### Feature

**Added Display name column to Apps table**

Added a column to the [Apps table](https://cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api#register) to show the App display name separate from the App name. The **App name** column will no longer show the display name if one is set. Instead the display name will appear in the new **Display name** column. You can also now filter by the **App name** and **Display name** independently.

---
## 2025-08-20

### Announcement

On August 20, 2025, we released an updated version of the Apigee UI.

### Feature

**Added Name column to API Products table**

Added a column to the [API Products table](https://cloud.google.com/apigee/docs/api-platform/publish/create-api-products#productdetails) to display the product name. You can now filter and sort by the product name. The link to the API product detail page is now in the **Name** column instead of the **Display Name** column.

---
## 2025-08-12

### Announcement

On August 12, 2025, we released an updated version of the Apigee UI.

### Feature

**Added path column to Debug transaction table**

A new column has been added to the [transactions table](https://cloud.google.com/apigee/docs/api-platform/debug/trace#create) in the Debug view that specifies the path that was used by the transaction to call the proxy.

### Fixed

| Bug ID | Description |
| --- | --- |
| **421974963** | **Adjusted tooltip positions in Debug sequence view** The tooltips for response items in the Debug sequence view now appear at the bottom of the element, so as not to block the elements above. |
| **421975987** | **You can no longer pan away from the graph in the Debug canvas** The Debug canvas is now restricted and will no longer allow you to pan away from the graph. The scroll wheel on the mouse can now also be used to zoom in and out of the graph. |
| **421975987** | **Debug canvas no longer automatically centers when event elements are clicked** When clicking an element in the Debug canvas the canvas will no longer automatically center on the selected item. |

---
## 2025-07-30

### Announcement

On July 30, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

* Develop > API Proxies
* Develop > Shared Flows
* Develop > Offline Debug

See [Apigee UI in Cloud console navigation](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

---
## 2025-07-29

### Announcement

On July 29, 2025 we removed the **Switch to Classic** option from the following Apigee UI in the Google Cloud console pages:

* API Proxy
* Shared Flow
* Offline Debug detail

This is part of the Apigee Classic UI shutdown plan.

See [Apigee UI in Cloud console navigation](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

---
## 2025-07-24

### Announcement

On July 24, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

* Publish > Portals

See [Apigee UI in Cloud console navigation](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

---
## 2025-06-25

### Announcement

On June 25, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

* Publish > API products
* Publish > Developers
* Publish > Apps
* Admin > Instances
* Admin > Data collectors
* Admin > Environments
* Admin > Endpoint attachments

See [Apigee UI in Cloud console navigation](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

---
## 2025-06-17

### Announcement

On June 17, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

* Publish > Monetization
* Analyze > API monitoring
* Analyze > API metrics
* Analyze > Developers > Developer Engagement
* Analyze > Developers > Traffic Composition
* Analyze > End Users > Devices
* Analyze > End Users > Geomap
* Analyze > Custom reports

See [Apigee UI in Cloud console navigation](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

---
## 2025-05-29

### Announcement

On May 29, 2025 we announced the shutdown schedule for the Apigee Classic UI.

### Deprecated

The Apigee Classic UI will be shutdown as of August 29, 2025.

This is the final phase of moving Apigee to the Google Cloud console. Apigee in the Google Cloud console gives you the ability to manage all of your Apigee functionality in one place.

To prepare for the shutdown of the Apigee Classic UI, familiarize yourself with the new Apigee UI in Google Cloud console by reviewing [UI overview](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview).

See [Apigee Classic UI shutdown](https://cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates and exception request.

---
