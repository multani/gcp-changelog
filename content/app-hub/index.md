# App Hub

## 2025-12-18

### Feature

App Hub now lets you register multiple resources at once in the Google Cloud console to simplify and accelerate the application creation process.

The following are key features of this update:

* **Combined application creation and registration**: The application creation and resource registration workflows are now merged into a single process. You can register up to 10 services and workloads to an application at a time.
* **Streamlined resource registration**: You can now register multiple services and workloads to an application in a single operation, directly from the application creation page. This update reduces the time and effort required to set up your applications.
* **Copied attribute and owner information**: You now have the option to copy attributes and owner information from an application to all the resources you're registering. This feature does not apply to shared services.

For more information, see [Register existing resources to an application](https://docs.cloud.google.com/app-hub/docs/register-resources).

---
## 2025-12-16

### Feature

App Hub is now available in the `europe-north2` (Stockholm) region, letting you create applications and register resources from an expanded list of locations.

To learn more about the differences between global and regional applications, see [Global and regional applications](https://docs.cloud.google.com/app-hub/docs/global-regional-applications).
For a complete list of all available App Hub locations, see [App Hub locations](https://docs.cloud.google.com/app-hub/docs/locations).

---
## 2025-11-17

### Feature

App Hub now supports new metadata [properties](https://docs.cloud.google.com/app-hub/docs/overview#properties-and-attributes) to provide deeper context and governance for your services and workloads:

* **Functional type:** Services and workloads now include the `FunctionalType` property, which is an output-only field that identifies the known function of a resource. The initial supported value is `AGENT`, which indicates that a workload is an AI agent.
* **Extended metadata:** Services and workloads now include the `ExtendedMetadata` property to provide rich, structured, and schema-driven information about the resource, such as the `apphub.googleapis.com/AgentProperties` schema for AI agents.
* **Registration type:** Services now have the `RegistrationType` property. This output-only field indicates whether a service is exclusive (can be registered to only one application) or shared (can be registered to multiple applications). To view the registration type of your services, see [View details of services and workloads](https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources#view).
* **Identity:** Services and workloads now include the `Identity` property, which is an output-only field that contains the service account or managed workload identity name for a service or workload.

---
## 2025-11-14

### Feature

App Hub has expanded its support for Google Cloud resources. You can now register services and workloads from a wide range of products to your applications, including new resources from Access Approval, Certificate Authority Service, Cloud Run, Firebase, Gemini for Google Cloud, GKE Multi-Cloud, and more. Many of these supported resources are available in Preview. For a complete list, see [App Hub supported resources](https://docs.cloud.google.com/app-hub/docs/supported-resources).

### Feature

Management projects are now [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages) to enable application management in folders. This setup model is recommended for all new App Hub implementations and provides a centralized and scalable way to organize, deploy, and govern your applications.

Key features of this release include:

* **App-enabled folders**: You can now enable application management on a standard Google Cloud folder, which then becomes an app-enabled folder. This folder acts as the application management boundary for your App Hub applications.
* **Management projects**: A dedicated management project is automatically created within your app-enabled folder to store application metadata and configurations, and to centralize operations.
* **Simplified API management**: Required APIs for core App Hub features are automatically enabled on the management project. You can also enable recommended APIs to access the full application lifecycle experience.
* **Flexible billing**: Linking a billing account is now optional. You can use App Hub's core features for organizing and observing your applications at no cost. A billing account is required only for other application-centric features.

For more information on how to get started, see [Set up App Hub with app-enabled folders](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder).

---
## 2025-08-25

### Feature

App Hub supports resources from the following sources in [Preview](https://cloud.google.com/products#product-launch-stages):

* Vertex AI
  + Pipeline job
  + Custom job
  + Hyperparameter tuning job
  + Index
  + Index endpoint
  + NAS job
  + Model deployment monitoring job
* Compute Engine
  + Autoscaler
  + Commitment
  + Disk
  + Regional disk
  + Instance template
  + Regional instance template
  + License
  + Node group
  + Image
  + Resource policy
  + Reservation
  + Node template
  + Router
  + Snapshot
  + Route
  + Subnetwork
  + Global public delegated prefix
  + Public delegated prefix
* Dataflow
  + Job
* Datastream
  + Stream
* Cloud DNS
  + Managed zone
  + Policy

---
## 2025-07-30

### Feature

The following [Vertex AI supported resources](https://cloud.google.com/app-hub/docs/supported-resources) are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)):

* [Dataset](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.datasets) items
* [Featurestore](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores) containers
* [MetadataStore](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.metadataStores) instances
* [Model](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models) resources

---
## 2025-07-08

### Feature

[Dataproc Metastore services](https://cloud.google.com/app-hub/docs/supported-resources) are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-06-25

### Feature

App Hub supports resources from the following [sources](https://cloud.google.com/app-hub/docs/supported-resources) in [Preview](https://cloud.google.com/products#product-launch-stages):

* Dataproc Metastore Service
* Vertex AI Dataset
* Vertex AI Featurestore
* Vertex AI MetadataStore
* Vertex AI Model

---
