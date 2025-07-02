# Document AI

## 2025-06-30

### Feature

[Custom Extractor](https://cloud.google.com/document-ai/docs/ce-with-genai) model [`pretrained-foundation-model-v1.5-2025-05-05`](https://cloud.google.com/document-ai/docs/processors-list#processor_cde) is in General Availability ([GA](https://cloud.google.com/products/#product-launch-stages)) and has fine-tuning available for the US and EU.

From version v1.4 and later, we will use a new quota for online processing called [`Number of online process document pages per minute per processor type and model version`](https://cloud.google.com/document-ai/quotas#quotas_list). This quota will be enforced at a per-page and per-foundation model level. There will be no change to the batch processing quota.

These can be enabled in the console when creating labels and by using the [`DocumentSchema.EntityType`](https://cloud.google.com/document-ai/docs/reference/rpc/google.cloud.documentai.v1#entitytype).

For more information, read [Managing processor versions](https://cloud.google.com/document-ai/docs/manage-processor-versions#import).

---
## 2025-06-19

### Feature

We've increased the maximum file size for [online processing](https://cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/process) requests from 20 MB to 40 MB. This applies to all types of processors.

For more information, see the Document AI [limits](https://cloud.google.com/document-ai/limits#content_limits) page.

---
