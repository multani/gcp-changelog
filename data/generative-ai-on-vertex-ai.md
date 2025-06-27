# Generative AI on Vertex AI

## 2025-06-24 00:00:00-07:00

### Deprecated

Starting on June 24, 2025, Imagen versions 1 and 2, image captioning, and visual question answering are deprecated.

On September 24, 2025, the following features and models will be removed:

* image captioning
* visual question answering
* Imagen 1 model `imagegeneration@002`
* Imagen 2 models `imagegeneration@005` and `imagegeneration@006`

For more information, see [Migrate to Imagen 3](vertex-ai/generative-ai/docs/image/migrate-to-imagen-3).## 2025-06-23 00:00:00-07:00

### Announcement

**Veo 2** support for advanced video controls is Generally Available. In addition to a providing a first frame of a video, you can specify the last frame of a video or a video to extend in length. For more information, see [Veo on Vertex AI API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation).## 2025-06-17 00:00:00-07:00

### Announcement

**Gemini 2.5 Flash** and **Gemini 2.5 Pro** are now generally available and accessible using the API and Vertex AI Studio.

See [Gemini 2.5 Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash) and [Gemini 2.5 Pro](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro) for more information.### Announcement

**Gemini 2.5 Flash-Lite** is now available as a preview offering in both the API and Vertex AI Studio.

See [Gemini 2.5 Flash-Lite](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-lite) for more information.### Announcement

**Live API** is now available as a private general availability offering in the API and Vertex AI Studio. Reach out to your Google account team representative to request access.

See [Live API](https://cloud.google.com/vertex-ai/generative-ai/docs/live-api) for more information.### Deprecated

**Preview endpoint availability and removal:** All existing Gemini 2.5 Flash and Pro preview endpoints (listed below) will continue to be available with their current preview pricing until July 15, 2025. After this date, these preview endpoints will be shut down.

* `gemini-2.5-flash-preview-04-17`
* `gemini-2.5-flash-preview-05-20`
* `gemini-2.5-pro-preview-03-25`
* `gemini-2.5-pro-preview-05-06`
* `gemini-2.5-pro-preview-06-05`### Changed

**Updated pricing for Gemini 2.5 Flash GA:** The price for Gemini 2.5 Flash in GA will be adjusted to reflect its quality and unified output token pricing. This includes lower prices for thinking output, higher prices for non-thinking output. These pricing changes will take effect on the new GA endpoint as shared above. Preview pricing will only continue on existing preview endpoints for 30 days post-GA on **July 15, 2025**.### Changed

**Provisioned Throughput (PT):** Once a model is GA, all new PT purchases will be for GA endpoints only. If you've purchased PT for a specific preview version, it will still work for that specific preview. However, you must [migrate the existing PT to the GA endpoint](https://cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/purchase-provisioned-throughput#change-order) or purchase new PT for the GA endpoint by **July 15, 2025**.### Changed

**Updated preview endpoints:** Effective **June 19, 2025**, `gemini-2.5-flash-preview-04-17` endpoint will serve the Gemini 2.5 Flash model version released on 05-20, which has been promoted to GA. Similarly, the `gemini-2.5-pro-preview-05-06` and `03-25` endpoints will serve the Gemini 2.5 Pro model version released on 06-05, also promoted to GA. This update ensures continuity during your transition.## 2025-06-16 00:00:00-07:00

### Announcement

The DeepSeek API service on Vertex AI is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see the [DeepSeek model card](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-r1-0528-maas) in Model Garden.## 2025-06-11 00:00:00-07:00

### Changed

**Imagen 4**'s public preview models are updated to the following:

* `imagen-4.0-generate-preview-06-06`
* `imagen-4.0-fast-generate-preview-06-06`
* `imagen-4.0-ultra-generate-preview-06-06`

For more information about each model, see [Preview Imagen models](https://cloud.google.com/vertex-ai/generative-ai/docs/models#preview-imagen-models).

To avoid service interruption, migrate from `imagen-4.0-ultra-generate-exp-05-20` and `imagen-4.0-generate-preview-05-20` before 2025-07-07.## 2025-06-09 00:00:00-07:00

### Changed

**Gemini API**

The `logprobs` and `response_logprobs` parameters for the Gemini API are now [generally available](https://cloud.google.com/products?e=13802955&hl=en#product-launch-stages). For more information, see [Generate content with Gemini API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#logprobs).## 2025-06-05 00:00:00-07:00

### Feature

**Gemini 2.5 Pro**'s public preview version has been updated to `gemini-2.5-pro-preview-06-05` and includes expanded support for thinking. This model version is available in the API and Vertex AI Studio.

See [Gemini 2.5 Pro](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro) for model details.## 2025-06-03 00:00:00-07:00

### Announcement

Model Garden now includes [DeepSeek-R1-0528](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-r1) variants.### Announcement

In Model Garden, the following fine tuning features have been added:

* [Gemma 3](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemma3) UI fine-tuning using PEFT docker.
* [Qwen 2.5](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_pytorch_qwen2_5_finetuning.ipynb) fine-tuning notebook using PEFT docker.
* [Qwen 3](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_axolotl_qwen3_finetuning.ipynb) fine-tuning notebook using Axolotl docker.
* lm-evaluation-harness as an evaluation service in the [Llama 3.3](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_pytorch_llama3_3_finetuning.ipynb), [Llama 3.1](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_pytorch_llama3_1_finetuning.ipynb), [Gemma 3](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_gemma3_finetuning_on_vertex.ipynb) and [Gemma 2](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_gemma2_finetuning_on_vertex.ipynb) fine-tuning notebooks.