# Apigee API hub

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

