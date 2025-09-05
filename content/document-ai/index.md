# Document AI

## 2025-08-29

### Feature

Derived entity and signature detection are now supported in [Custom Extractor](https://cloud.google.com/document-ai/docs/ce-with-genai) models `pretrained-foundation-model-v1.4-2025-02-05` as General Availability [(GA)](https://cloud.google.com/products/#product-launch-stages), and `pretrained-foundation-model-v1.5-2025-05-05` and `pretrained-foundation-model-v1.5-pro-2025-06-20` as Preview.

Signature detection lets you identify hand-written signatures by using visual cues in the document. Derived entity detection lets you deduce entities by inference without requiring the value to be explicitly present in the text. You can use this feature to deduce the country in an address, counting items in a table, or detecting if an ID is fake.

These can be enabled in the console when creating new labels or by using the [`DocumentSchema.EntityType`](https://cloud.google.com/document-ai/docs/reference/rpc/google.cloud.documentai.v1#entitytype) resource in the API.

For more information, read [Custom extractor with derived fields](https://cloud.google.com/document-ai/docs/ce-derived-signature), and [choose label attributes](https://cloud.google.com/document-ai/docs/create-dataset#choose_label_attributes).

---
## 2025-07-22

### Feature

[Custom extractor](https://cloud.google.com/document-ai/docs/ce-with-genai) model [`pretrained-foundation-model-v1.5-pro-2025-06-20`](https://cloud.google.com/document-ai/docs/processors-list#processor_cde) powered by Gemini 2.5 Pro is in [Public Preview](https://cloud.google.com/products/#product-launch-stages). It has ML processing available for US and EU regions, and 30 page per minute processing requests.

For more information, see [Managing processor versions](https://cloud.google.com/document-ai/docs/manage-processor-versions#import).

---
## 2025-07-04

### Feature

Document AI now supports [Identity and Access Management](https://cloud.google.com/iam/docs/overview) (IAM) deny policies. These policies allow you to define deny rules that prevent certain principals from using certain permissions to access Google Cloud resources, regardless of the roles they're granted.

For more information, read [Deny policy](https://cloud.google.com/iam/docs/deny-overview) overview and [Document AI security and compliance](https://cloud.google.com/document-ai/docs/security).

### Feature

Document AI [VPC service controls](https://cloud.google.com/vpc-service-controls/docs/overview) (VPC-SC) integration now supports identity groups.

For more information on setting up VPC-SC identity groups, read [Configure identity groups and third-party identities in ingress and egress rules](https://cloud.google.com/vpc-service-controls/docs/configure-identity-groups).

---
## 2025-07-03

### Feature

The Document AI CDE processor now supports merging the child entities of nested entities that extend across several pages. This is supported in custom extractor model [`pretrained-foundation-model-v1.5-2025-05-05`](https://cloud.google.com/document-ai/docs/processors-list#processor_cde).

This change is automatically present in existing and newly created processors.

For customers with existing v1.5 processors to make use of this feature, you must relabel the nested entities in different pages.

To learn more about the labeling process, refer to our [Label documents](https://cloud.google.com/document-ai/docs/label-documents) documentation.

---
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
