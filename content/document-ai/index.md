# Document AI

## 2025-10-06

### Feature

[Custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) model
`pretrained-foundation-model-v1.5.1-2025-08-07` with improved adaptive few-shot
learning is available as Release Candidate
([Preview](https://cloud.google.com/products/#product-launch-stages)).

---
## 2025-09-26

### Announcement

Capacity reservation is available for Document AI in
[preview](https://cloud.google.com/products/#product-launch-stages). This lets you
grant capacity to selected processors and maintain a steady real-time, high-volume
processing flow for document processing requests.

For the necessary steps, read [make a capacity reservation
request](https://cloud.google.com/document-ai/quotas#capacity-reservation).

---
## 2025-09-23

### Feature

[Custom classifier](https://cloud.google.com/document-ai/docs/custom-classifier)
model [`pretrained-classifier-v1.5-2025-08-05`](https://cloud.google.com/document-ai/docs/custom-classifier#models)
powered by Gemini 2.5 Flash is in [Preview](https://cloud.google.com/products/#product-launch-stages). It has ML processing available for US and EU regions, a
maximum page limit of [30](https://cloud.google.com/document-ai/limits#classification_processors) pages,
and processing requests of [120](https://cloud.google.com/document-ai/quotas#service_tiers) pages per minute.

Unlike the prior custom classifier, which used classical
machine learning, this version features a new platform. It accommodates:

* High accuracy immediately, based on the document classes you define.
* Few-shot learning to further improve accuracy.
* Use of descriptions when labeling for more context and insight for document classes.
* More accurate results with the same training dataset on the fine-tuned generative AI model, compared to the trained version.
* Autolabeling documents for fine-tuning and evaluation.
* Generative AI to fine-tune and heighten accuracy.

For more information on processor versions, see [Managing processor
versions](https://cloud.google.com/document-ai/docs/manage-processor-versions).

---
## 2025-09-10

### Deprecated

Custom Extractor version [`pretrained-foundation-model-v1.4-2025-02-05`](https://cloud.google.com/document-ai/docs/processors-list#processor_cde) will no longer be accessible on **February 5, 2026**.

To avoid service disruptions, migrate to a later version such as
`pretrained-foundation-model-v1.5-2025-05-05` or `pretrained-foundation-model-v1.5-pro-2025-06-20`.
To learn more about the migration process, refer to our [Manage processor
versions](https://cloud.google.com/document-ai/docs/manage-processor-versions) documentation.

---
## 2025-09-09

### Announcement

Document AI supports [two service tiers](https://cloud.google.com/document-ai/quotas#service_tiers)
and associated quotas: provisioned and best effort tiers.

The base is **provisioned tier** quota, which provides 120 pages per minute for
Gemini 2.0 and 2.5 Flash LLM and 30 pages per minute for Gemini
2.5 Pro LLM.

If you require more volume, **best effort tier** quota provides 120 pages per
minute for Gemini 2.0 2.5 Flash and 60 pages per minute for
Gemini 2.5 Pro, and is only used once the provisioned quota has been
exhausted. This applies to quotas `BestEffortOnlineProcessDocumentPagesPerMinutePerProjectUS`,
and `EU`, and `best_effort_online_process_document_pages_us` and `eu` in the console.

Best effort can get up to 240 pages per minute for [custom data extractor
models](https://cloud.google.com/document-ai/docs/ce-with-genai)
v1.4 and v1.5 with a quota increase request (QIR). You can make a QIR by
contacting your sales team representative.

There is no service level agreement [(SLA)](https://cloud.google.com/document-ai/sla)
for best effort tier.

---
## 2025-09-03

### Feature

Custom extractor model `pretrained-foundation-model-v1.5-pro-2025-06-20` is
available as General Availability ([GA](https://cloud.google.com/products/#product-launch-stages)).

For more information about available models, see the [custom
extractor](https://cloud.google.com/document-ai/docs/ce-with-genai) page.

---
## 2025-08-29

### Feature

Derived entity and signature detection are now supported in [Custom
Extractor](https://cloud.google.com/document-ai/docs/ce-with-genai) models `pretrained-foundation-model-v1.4-2025-02-05`
as General Availability [(GA)](https://cloud.google.com/products/#product-launch-stages)
and `pretrained-foundation-model-v1.5-2025-05-05`, as well as `pretrained-foundation-model-v1.5-pro-2025-06-20`
as Preview.

Signature detection lets you identify handwritten signatures by using visual
cues in the document. Derived entity detection lets you deduce entities by
inference without requiring the value to be explicitly present in the text. You
can use this feature to deduce the country in an address, counting items in a
table, or detecting if an ID is fake.

These can be enabled in the console when creating labels or by using the
[`DocumentSchema.EntityType`](https://cloud.google.com/document-ai/docs/reference/rpc/google.cloud.documentai.v1#entitytype)
resource in the API.

For more information, read [Custom extractor with derived
fields](https://cloud.google.com/document-ai/docs/ce-derived-signature) and [choose label
attributes](https://cloud.google.com/document-ai/docs/create-dataset#choose_label_attributes).

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
