# Vertex AI

## 2025-08-14

### Feature

[Gemma 3 270M](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemma3;publisherModelVersion=gemma-3-270m-it), [Wan 2.2](https://console.cloud.google.com/vertex-ai/publishers/wan-ai/model-garden/wan2-2) and [Wan 2.1](https://console.cloud.google.com/vertex-ai/publishers/wan-ai/model-garden/wan2-1) models are available through Model Garden.

---
## 2025-08-06

### Feature

[OpenAI's gpt-oss](https://console.cloud.google.com/vertex-ai/publishers/openai/model-garden/gpt-oss) models are available through Model Garden.

---
## 2025-07-16

### Feature

Added [Gemma 3](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_axolotl_gemma3_finetuning.ipynb) fine-tuning notebook using Axolotl docker with support for 1b, 4b, 12b, and 27b variants.

---
## 2025-07-14

### Feature

[Multimodal MedGemma 27B IT](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/medgemma;publisherModelVersion=medgemma-27b-it), [MedSigLIP](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/medsiglip), and [T5Gemma](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/t5gemma) models are available through Model Garden.

---
## 2025-07-11

### Feature

To reduce the cost of running your inference jobs, you can now use flex-start VMs, which are powered by [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler). Flex-start VMs offer significant discounts and are well-suited for
short-duration workloads. This feature is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

For more information, see [Use DWS flex-start VMs with inference](https://cloud.google.com/vertex-ai/docs/predictions/use-flex-start-vms).

---
## 2025-07-01

### Feature

The global endpoint is generally available (GA) for Anthropic's Claude Opus 4. For details, see [Global endpoint](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#global-endpoint).

---
## 2025-06-30

### Deprecated

Mistral Nemo, which is offered as a Model as a Service (MaaS) model in Model Garden, is deprecated. For details, see [Model as a Service (MaaS) deprecations](https://cloud.google.com/vertex-ai/generative-ai/docs/deprecations/partner-models).

### Deprecated

Anthropic's Claude 3 Opus, which is offered as a Model as a Service (MaaS) model in Model Garden, is deprecated. For details, see [Model as a Service (MaaS) deprecations](https://cloud.google.com/vertex-ai/generative-ai/docs/deprecations/partner-models).

### Feature

Vertex AI online inference now offers Preview support of PSC service automation that can automatically create PSC endpoints for dedicated private endpoints. For more information, see [Create the online inference endpoint with PSC automation](https://cloud.google.com/vertex-ai/docs/predictions/private-service-connect#create-endpoint-with-automation).

### Feature

Vertex AI now offers GA support of Private Service Connect Interface and includes Private DNS Peering. For more information, see [Use Private Service Connect interface for Vertex AI Training](https://cloud.google.com/vertex-ai/docs/training/psc-i-egress).

### Feature

Private Service Connect interface (PSC-I) support for ML pipeline runs in Vertex AI Pipelines is now [generally available](https://cloud.google.com/products#product-launch-stages). PSC-I is recommended for private connectivity because it reduces the chance of IP exhaustion, allows for transitive peering, and includes Private DNS Peering.

For more information, see [Configure Private Service Connect interface for a pipeline](https://cloud.google.com/vertex-ai/docs/pipelines/configure-private-service-connect).

---
## 2025-06-27

### Feature

[Gemma 3n](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemma3n) models are now available through Model Garden.

---
## 2025-06-24

### Deprecated

The Generative AI module in the Vertex AI SDK is deprecated. For information about migrating to the Google Gen AI SDK, see the [migration guide](https://cloud.google.com/vertex-ai/generative-ai/docs/deprecations/genai-vertexai-sdk).

---
## 2025-06-10

### Feature

**Vector Search custom constraints with Organization Policy**

You can use custom constraints with the Organization Policy Service to provide more granular control over specific fields for indexes and index endpoints in Vector Search.

For more information, see [Create custom constraints for Vector Search](https://cloud.google.com/vertex-ai/docs/vector-search/custom-constraints).

---
