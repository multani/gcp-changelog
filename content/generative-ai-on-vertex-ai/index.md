# Generative AI on Vertex AI

## 2025-10-02

### Feature

**Google Gen AI SDK in C# Preview**

[Preview](https://cloud.google.com/products#product-launch-stages): The Google Gen AI SDK is available in C#. See [googleapis/dotnet-genai](https://github.com/googleapis/dotnet-genai).

This release includes support for `GenerateContentAsync`, `GenerateContentStreamAsync`, `GenerateImagesAsync`, and three Live APIs, which includes `SendClientContentAsync`, `SendRealtimeInputAsync`, and `SendToolResponseAsync`.

---
## 2025-09-30

### Feature

[DeepSeek-V3.2-Exp](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-v3-2) is available through Model Garden.

---
## 2025-09-25

### Announcement

New preview models for [**Gemini 2.5 Flash**](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash#2.5-flash-preview) and [**2.5 Flash-Lite**](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-lite#2.5-flash-lite-preview) are now available. These models are available at the following versioned endpoints:

* `gemini-2.5-flash-preview-09-2025`
* `gemini-2.5-flash-lite-preview-09-2025`

---
## 2025-09-24

### Deprecated

Access to Gemini's 1.5 models has been discontinued. For more information, see our [Model versions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions) page.

---
## 2025-09-23

### Announcement

**Gemini 2.5 Flash with Live API Native Audio Preview**

[**Gemini 2.5 Flash with Live API Native Audio**](cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash) (`gemini-live-2.5-flash-preview-native-audio-09-2025`) is available in [Preview](https://cloud.google.com/products#product-launch-stages). A single, unified model processes audio input and generates audio output directly, eliminating separate text-to-speech/speech-to-text conversions. This results in-low latency, high-quality, and incredibly human-like conversations. New features and capabilities include:

* **Improved Barge-in:** Interrupt Gemini more naturally and reliably, even in loud and noisy environments.
* **Robust Function Calling:** We've improved the triggering rate, allowing Gemini to successfully execute the functions you define with greater precision.
* **Accurate Transcription:** The accuracy of audio-to-text transcription has been significantly enhanced.
* **Seamless Multilingual Support:** Speak to Gemini in multiple languages, and it will effortlessly switch between them without any pre-configuration. Language is no longer a barrier!
* **Enhanced Audio Quality:** Experience a dramatically improved audio quality that truly feels like speaking with a person.
* **Proactive Audio:** Define Gemini's expertise and set conditions for when it should respond. Gemini can act as a "silent listener," only chiming in when the conversation touches upon its designated area of expertise.
* **Affective Dialog:** Gemini can adapt and adjust its generated voice to match the emotional tone of the speaker, creating more empathetic and natural interactions.

[Watch our comprehensive demo](https://youtu.be/ZsB33Tr-P3c) to see these features in action, including seamless language switching, expert mode, emotionally aware responses, memory recall, and interactive screen sharing for engineering tasks – all demonstrated directly within Vertex AI Studio without writing a single line of code!

---
## 2025-09-22

### Feature

[DeepSeek-V3.1-Terminus](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-v3-1;publisherModelVersion=deepseek-v3-1-terminus) is available through Model Garden.

---
## 2025-09-18

### Changed

**Grounding with Google Maps**

Grounding with Google Maps has implemented the following changes:

* Removed the following fields from the API response:
  + `grounding_chunk.maps.text`
  + `grounding_chunk.maps.place_answer_sources.review_snippets.author_attribution`
  + `grounding_chunk.maps.place_answer_sources.flag_content_uri`
  + `grounding_chunk.maps.place_answer_sources.review_snippets.flag_content_uri`
* The widget context token is only returned when the optional `widget_token_enable` input flag is set.

To learn more, see [Grounding with Google Maps](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/grounding-with-google-maps).

---
## 2025-09-15

### Changed

**Imagen**

We improved Imagen's virtual try-on model, `virtual-try-on-preview-08-04`, so that it is better at preserving the person's body shape and preserving the garment product's identity.

---
## 2025-09-10

### Feature

**Vertex AI Agent Engine**

Agent Engine now supports the following features:

* Agent Engine **Code Execution**, now in Preview, lets your agent run code in an isolated sandbox environment. For more information, see [Code Execution](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/code-execution/overview).
* You can now develop, deploy, and use agents that support the **Agent-to-Agent (A2A) protocol** on Agent Engine. For more information, see [Develop an Agent2Agent agent](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/develop/a2a).
* Agent Engine now supports **bidirectional streaming**. For more information, see [Bidirectional streaming](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/bidirectional-streaming).
* The [Agent Engine page](https://console.cloud.google.com/vertex-ai/agents/agent-engines) in the Cloud Console UI now has a new **Memory Bank** tab for displaying and managing memories.

### Breaking

**Vertex AI Agent Engine**

In version `v1.112.0` of the Vertex AI SDK for Python, the `agent_engines` module has been refactored to a [client-based design](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview#migration). For information about updating your existing code to the new design, see the [Migration guide](https://cloud.google.com/vertex-ai/generative-ai/docs/deprecations/agent-engine-migration).

---
## 2025-09-09

### Feature

[EmbeddingGemma](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/embeddinggemma) and [DeepSeek-V3.1](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-v3-1) models are available through Model Garden.

### Feature

[AI Singapore's SEA-LION V4 models](https://console.cloud.google.com/vertex-ai/publishers/aisingapore/model-garden/gemma-sea-lion-v4) are available through Model Garden. They are open models for Southeast Asian languages, built by leveraging Vertex Model Development Service for enhanced training efficiency and model accuracy.

---
## 2025-09-08

### Feature

**Veo video generation**

Veo 3 support for short-duration videos is [generally available](https://cloud.google.com/products#product-launch-stages). You can use Veo 3 to create 4, 6, or 8 second videos. For more information, see the following:

* [Generate videos with Veo on Vertex AI from text prompts](https://cloud.google.com/vertex-ai/generative-ai/docs/video/generate-videos-from-text)
* [Generate videos with Veo on Vertex AI from an image](https://cloud.google.com/vertex-ai/generative-ai/docs/video/generate-videos-from-an-image)
* [Veo on Vertex AI video generation API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation)

---
## 2025-09-03

### Changed

**Vertex AI RAG Engine: Managed Database (Spanner)**

Customers will be charged for the use of a Google-managed Spanner instance that's provisioned in a Google tenant project, using standard Spanner SKUs.

For more information, see [Vertex AI RAG Engine billing](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-engine-billing).

---
## 2025-08-26

### Announcement

**Gemini 2.5 Flash Image Preview**

[Gemini 2.5 Flash Image](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash#image-generation) (`gemini-2.5-flash-image-preview`) is available in [Preview](https://cloud.google.com/products#product-launch-stages). Gemini 2.5 Flash Image Preview supports additional image generation and editing features such as [image generation from multiple reference images](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/image-generation#image-generation) and [improved multi-turn image editing](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/image-editing#multi-turn-editing).

### Feature

**Vertex AI model tuning and Gen AI evaluation service**

Vertex AI model tuning now supports integration with the Gen AI evaluation service in Preview. You can automatically run evaluations on your tuned models and intermediate checkpoints. For more information, see [Create a tuning job](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-use-supervised-tuning#create_a_text_model_supervised_tuning_job).

---
## 2025-08-21

### Feature

**Vertex AI Agent Engine**

Agent Engine now supports the following enterprise security features:

* You can now deploy your agents in a private VPC environment, configuring a Private Service Connect interface, to ensure data privacy and meet security and compliance requirements. For more information, see [Configure Private Service Connect interface](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy#psc-i).
* You can now use your own [customer-managed encryption keys (CMEK)](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/manage/access#cmek) to protect data at rest.
* You can now specify [customized resource controls](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy#customized-resource-controls), such as the minimum and maximum number of application instances, resource limits for each container, and concurrency for each container.
* As a part of Vertex AI Platform, Vertex AI Agent Engine now supports [HIPAA](https://cloud.google.com/security/compliance/hipaa) workloads.

For more information, see [Agent Engine overview](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview#enterprise_security).

---
## 2025-08-14

### Announcement

**Imagen**

Imagen 4 is Generally Available.

Imagen 4 introduces the following models:

* [Imagen 4 Generate](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-001)
* [Imagen 4 Fast Generate](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-001)
* [Imagen 4 Ultra Generate](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-ultra-generate-001)

For more information, see [Generate images using text prompts](https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images) and [Image generation API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api).

### Feature

[Gemma 3 270M](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemma3;publisherModelVersion=gemma-3-270m-it), [Wan 2.2](https://console.cloud.google.com/vertex-ai/publishers/wan-ai/model-garden/wan2-2) and [Wan 2.1](https://console.cloud.google.com/vertex-ai/publishers/wan-ai/model-garden/wan2-1) models are available through Model Garden.

---
## 2025-08-13

### Feature

OpenAI's [gpt-oss-120b](https://cloud.google.com/vertex-ai/generative-ai/docs/maas/openai/gpt-oss-120b) and [gpt-oss-20b](https://cloud.google.com/vertex-ai/generative-ai/docs/maas/openai/gpt-oss-20b) are available as Model as a Service (MaaS) models in Model Garden.

### Feature

[Qwen3 Coder](https://cloud.google.com/vertex-ai/generative-ai/docs/maas/qwen/qwen3-coder) and [Qwen3 235B](https://cloud.google.com/vertex-ai/generative-ai/docs/maas/qwen/qwen3-235b) are available as Model as a Service (MaaS) models in Model Garden.

---
## 2025-08-08

### Feature

**Gemini 2.5 Flash-Lite** and **Gemini 2.5 Pro** now support supervised fine-tuning. For more information, see [About supervised fine-tuning for Gemini models](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning).

---
## 2025-08-07

### Feature

**Vertex AI prompt optimizer**

The Vertex AI prompt optimizer is now [generally available](https://cloud.google.com/products?e=13802955&hl=en#product-launch-stages). For more information, see [Optimize prompts](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-optimizer).

We now offer a [zero-shot prompt optimizer](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-optimizer).

### Feature

**Vertex AI Agent Engine**

You can use your own [custom service account](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/set-up#custom-service-account) for agent identity to manage permissions and access according to your organization's security policies.

### Feature

**Model tuning**

You can now perform supervised fine-tuning on open models such as Llama 3.1. For more information, see [Tune an open model](https://cloud.google.com/vertex-ai/generative-ai/docs/models/open-model-tuning).

---
## 2025-08-06

### Feature

[OpenAI's gpt-oss](https://console.cloud.google.com/vertex-ai/publishers/openai/model-garden/gpt-oss) models are available through Model Garden.

### Feature

**Imagen**

Virtual try-on lets you generate virtual try-on images from an image of a
person and product photos that you provide, and is available in Preview. For more information, see [Generate Virtual Try-On Images](https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-virtual-try-on-images) and [Virtual Try-On API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/virtual-try-on-api).

---
## 2025-07-29

### Announcement

**Veo video generation** Veo 3 and Veo 3 Fast are now generally available. For more information, see [Generate videos using text prompts](https://cloud.google.com/vertex-ai/generative-ai/docs/video/generate-videos-from-text).

---
## 2025-07-23

### Changed

[Grounding with Google Maps](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/grounding-with-google-maps) is available in all regions (except for the EEA) as a Preview (Pre-GA) feature.

---
## 2025-07-22

### Announcement

**Gemini 2.5 Flash-Lite** is now generally available and accessible using the API and Vertex AI Studio. This GA release includes support for explicit caching and [batch prediction](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-gemini), as well as expanded region support.

See [Gemini 2.5 Flash-Lite](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-lite) for more information.

---
## 2025-07-17

### Announcement

**Veo 3** preview models now support upscaling for 1080p resolution using the new `resolution` parameter. For more information, see [Veo on Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation#resolution).

---
## 2025-07-16

### Feature

Added [Gemma 3](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_axolotl_gemma3_finetuning.ipynb) fine-tuning notebook using Axolotl docker with support for 1b, 4b, 12b, and 27b variants.

---
## 2025-07-14

### Feature

[Multimodal MedGemma 27B IT](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/medgemma;publisherModelVersion=medgemma-27b-it), [MedSigLIP](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/medsiglip), and [T5Gemma](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/t5gemma) models are available through Model Garden.

---
## 2025-07-08

### Feature

**Vertex AI Agent Engine**

[Vertex AI Agent Engine Memory Bank](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/memory-bank/overview) is now available in Preview. Memory Bank lets you dynamically generate long-term memories based on users' conversations with your agent.

---
## 2025-07-03

### Feature

**Vertex AI Agent Garden**

[Vertex AI Agent Garden](https://console.cloud.google.com/vertex-ai/agents/agent-garden) now supports filtering by tags.

---
## 2025-06-27

### Feature

[Gemma 3n](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemma3n) models are now available through Model Garden.

### Feature

Multimodal datasets are now available in preview. For more information, see [Multimodal datasets](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/datasets).

---
## 2025-06-24

### Deprecated

Starting on June 24, 2025, Imagen versions 1 and 2, image captioning, and visual question answering are deprecated.

On September 24, 2025, the following features and models will be removed:

* image captioning
* visual question answering
* Imagen 1 model `imagegeneration@002`
* Imagen 2 models `imagegeneration@005` and `imagegeneration@006`

For more information, see [Migrate to Imagen 3](vertex-ai/generative-ai/docs/image/migrate-to-imagen-3).

---
## 2025-06-23

### Announcement

**Veo 2** support for advanced video controls is Generally Available. In addition to a providing a first frame of a video, you can specify the last frame of a video or a video to extend in length. For more information, see [Veo on Vertex AI API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation).

---
## 2025-06-17

### Announcement

**Gemini 2.5 Flash** and **Gemini 2.5 Pro** are now generally available and accessible using the API and Vertex AI Studio.

See [Gemini 2.5 Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash) and [Gemini 2.5 Pro](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro) for more information.

### Announcement

**Gemini 2.5 Flash-Lite** is now available as a preview offering in both the API and Vertex AI Studio.

See [Gemini 2.5 Flash-Lite](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-lite) for more information.

### Announcement

**Live API** is now available as a private general availability offering in the API and Vertex AI Studio. Reach out to your Google account team representative to request access.

See [Live API](https://cloud.google.com/vertex-ai/generative-ai/docs/live-api) for more information.

### Deprecated

**Preview endpoint availability and removal:** All existing Gemini 2.5 Flash and Pro preview endpoints (listed below) will continue to be available with their current preview pricing until July 15, 2025. After this date, these preview endpoints will be shut down.

* `gemini-2.5-flash-preview-04-17`
* `gemini-2.5-flash-preview-05-20`
* `gemini-2.5-pro-preview-03-25`
* `gemini-2.5-pro-preview-05-06`
* `gemini-2.5-pro-preview-06-05`

### Changed

**Updated pricing for Gemini 2.5 Flash GA:** The price for Gemini 2.5 Flash in GA will be adjusted to reflect its quality and unified output token pricing. This includes lower prices for thinking output, higher prices for non-thinking output. These pricing changes will take effect on the new GA endpoint as shared above. Preview pricing will only continue on existing preview endpoints for 30 days post-GA on **July 15, 2025**.

### Changed

**Provisioned Throughput (PT):** Once a model is GA, all new PT purchases will be for GA endpoints only. If you've purchased PT for a specific preview version, it will still work for that specific preview. However, you must [migrate the existing PT to the GA endpoint](https://cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/purchase-provisioned-throughput#change-order) or purchase new PT for the GA endpoint by **July 15, 2025**.

### Changed

**Updated preview endpoints:** Effective **June 19, 2025**, `gemini-2.5-flash-preview-04-17` endpoint will serve the Gemini 2.5 Flash model version released on 05-20, which has been promoted to GA. Similarly, the `gemini-2.5-pro-preview-05-06` and `03-25` endpoints will serve the Gemini 2.5 Pro model version released on 06-05, also promoted to GA. This update ensures continuity during your transition.

---
## 2025-06-16

### Announcement

The DeepSeek API service on Vertex AI is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see the [DeepSeek model card](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-r1-0528-maas) in Model Garden.

---
## 2025-06-11

### Changed

**Imagen 4**'s public preview models are updated to the following:

* `imagen-4.0-generate-preview-06-06`
* `imagen-4.0-fast-generate-preview-06-06`
* `imagen-4.0-ultra-generate-preview-06-06`

For more information about each model, see [Preview Imagen models](https://cloud.google.com/vertex-ai/generative-ai/docs/models#preview-imagen-models).

To avoid service interruption, migrate from `imagen-4.0-ultra-generate-exp-05-20` and `imagen-4.0-generate-preview-05-20` before 2025-07-07.

---
## 2025-06-09

### Changed

**Gemini API**

The `logprobs` and `response_logprobs` parameters for the Gemini API are now [generally available](https://cloud.google.com/products?e=13802955&hl=en#product-launch-stages). For more information, see [Generate content with Gemini API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#logprobs).

---
## 2025-06-05

### Feature

**Gemini 2.5 Pro**'s public preview version has been updated to `gemini-2.5-pro-preview-06-05` and includes expanded support for thinking. This model version is available in the API and Vertex AI Studio.

See [Gemini 2.5 Pro](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro) for model details.

---
## 2025-06-03

### Announcement

Model Garden now includes [DeepSeek-R1-0528](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-r1) variants.

### Announcement

In Model Garden, the following fine tuning features have been added:

* [Gemma 3](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemma3) UI fine-tuning using PEFT docker.
* [Qwen 2.5](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_pytorch_qwen2_5_finetuning.ipynb) fine-tuning notebook using PEFT docker.
* [Qwen 3](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_axolotl_qwen3_finetuning.ipynb) fine-tuning notebook using Axolotl docker.
* lm-evaluation-harness as an evaluation service in the [Llama 3.3](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_pytorch_llama3_3_finetuning.ipynb), [Llama 3.1](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_pytorch_llama3_1_finetuning.ipynb), [Gemma 3](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_gemma3_finetuning_on_vertex.ipynb) and [Gemma 2](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_gemma2_finetuning_on_vertex.ipynb) fine-tuning notebooks.

---
