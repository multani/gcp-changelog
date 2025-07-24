# Apigee API hub

## 2025-07-22

### Changed

**API hub provisioning now enables Apigee API**

When you provision API hub, it now enables the Apigee API (`apigee.googleapis.com`) in your Google Cloud project. If Apigee isn't already provisioned, an Apigee organization is also automatically created in your project as part of the provisioning process.

API hub remains a free service. Enabling the Apigee API has no additional pricing or billing implications for your project.

For more information, see [Provision API hub in the Cloud console](https://cloud.google.com/apigee/docs/apihub/provision).

---
## 2025-07-18

### Feature

**Apigee and hybrid plugin instance management**

You can now create and delete plugin instances for Apigee and Apigee Hybrid while associating the respective Apigee runtime projects to API hub.

For more information, see [Auto-register Apigee proxies](https://cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies).

### Breaking

**Apigee and Apigee hybrid plugin creation now requires source project ID**

When creating new instances of the **Apigee X and hybrid** plugin, you must now provide a source project ID. This source project ID is the Google Cloud project from which the plugin will import data.

This is a breaking change and will affect any existing API calls that create these plugins without explicitly providing this ID.

**Action Required:** Update your API calls to include the appropriate source project ID when creating new Apigee X and hybrid plugins. Failing to do so will result in creation errors.

### Changed

**Edit plugin instances changes**

You can now change or modify the name and curation logic of your plugin instance.

For more information, see [Edit a plugin instance](https://cloud.google.com/apigee/docs/apihub/manage-plugin-instances#edit-plugin-instance).

### Changed

**Resource URI format for Apigee deployments**

To ensure optimal functionality and consistency while creating or updating **Apigee** deployments, we now recommend that the **Resource URI** conforms to the following format:
`organizations/([^/]+)/environments/([^/]+)/apis/([^/]+)$`

For more information, see [Introduction to deployments](https://cloud.google.com/apigee/docs/apihub/deployments-intro).

---
## 2025-06-03

### Announcement

On June 3, 2025, we released an updated version of Apigee.

### Feature

**Apigee API hub is enabled for new Apigee organizations in supported regions.**

With this release, we are enabling [Apigee API hub](https://cloud.google.com/apigee/docs/apihub/what-is-api-hub) for new Apigee organizations [in regions where API hub is supported](https://cloud.google.com/apigee/docs/locations#available-apigee-api-analytics-regions). All new Apigee organizations, including hybrid organizations, that select an API hub-supported region *for their Apigee Analytics region* during provisioning will have access to API hub features at no additional cost.

API hub allows you to view, organize, and manage all of the APIs in your Apigee organization in one central location. To learn more, see [What is Apigee API hub?](https://cloud.google.com/apigee/docs/apihub/what-is-api-hub)

No action on your part is required to provision API hub for your organization, with the following exceptions:

* If your Apigee organization has Data Residency or VPC Service Controls enabled, you must configure your API hub instance manually to support these services. See [VPC Service Controls for API hub](https://cloud.google.com/apigee/docs/apihub/vpc-service-control) and [API hub and data residency](https://cloud.google.com/apigee/docs/apihub/locations#drz-api-hub) for more information.
* If your Apigee organization uses Customer-Managed Encryption Keys (CMEK), you must deprovision the Apigee API hub instance provided by default and recreate it to support CMEK. See [Deprovision Apigee API hub](https://cloud.google.com/apigee/docs/apihub/deprovision) and [Provision API hub in the Cloud console](https://cloud.google.com/apigee/docs/apihub/provision) for step-by-step instructions.

Contact [Google Cloud Support](https://cloud.google.com/apigee/docs/support/getting-started-with-support) for questions or assistance.

---
