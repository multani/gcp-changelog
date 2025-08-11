# AI Applications

## 2025-08-06

### Feature

**Vertex AI Search: Advanced autocomplete (GA)**

Use advanced autocomplete to enable autocomplete on blended search apps.

For more information, see [Configure advanced autocomplete](https://cloud.google.com/generative-ai-app-builder/docs/configure-advanced-autocomplete). This feature is in generally available (GA).

---
## 2025-08-04

### Changed

**Vertex AI Search: gemini-2.5-flash/answer\_gen/v1 model is the default model**

Model version gemini-2.5-flash/answer\_gen/v1 is the default model for generating answers in Vertex AI Search.

For more information, see [Answer generation model versions and lifecycle](https://cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

---
## 2025-07-09

### Announcement

**AI Applications: Quotas**

AI Applications offers the following allocation quotas in the global region (`global`), the US multi-region (`us`), and the EU multi-region (`eu`) under the Discovery Engine API:

* Number of data stores per project
* Number of documents per project
* Number of engines per project
* Number of user events

The number of data stores, documents, user events, and engines across all locations can't exceed the total per-project quota for that resource.

For more information, see [Quotas](https://cloud.google.com/generative-ai-app-builder/quotas).

---
## 2025-07-02

### Feature

**Vertex AI Search: Search for an exact match (GA)**

To search for an exact match, you can enclose your search query in double quotes (`"`). For example, when you search for `"Mary had a little lamb"`, Vertex AI Search looks for the phrase exactly as it is. It doesn't return search results that contain `Mary had lamb`, which has missing words; or `a little lamb had Mary`, which has the words in a different order.

This feature is Generally available when you use the [`engines.servingConfigs.search`](https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method to get search results for [custom data](https://cloud.google.com/generative-ai-app-builder/docs/preview-search-results), [media data](https://cloud.google.com/generative-ai-app-builder/docs/get-media-search-results), and [healthcare data](https://cloud.google.com/generative-ai-app-builder/docs/search-hc-data).

---
## 2025-06-26

### Feature

**Vertex AI Search: gemini-2.5-flash/answer\_gen/v1 model**

You can generate answers with the Gemini 2.5 Flash (`gemini-2.5-flash`) model. This model is tuned to address context-based question and answering tasks.

For more information, see [Answer generation model versions and lifecycle](https://cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

---
## 2025-06-16

### Changed

**AI Applications: Custom search and recommendations**

The vertical-agnostic apps, formerly known as *generic* search and recommendations, are renamed to *custom* search and recommendations. You'll see this new name in the product console and the documentation set. The functionality and the endpoints remain the same.

---
## 2025-06-06

### Feature

**Vertex AI Search: Skip layout parsing for types of HTML content (GA)**

The [layout parser](https://cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#layout-parsing) can skip parsing specific types of HTML content. By excluding less relevant content such as boilerplate, you can improve data quality. The layout parser can exclude based on HTML tags and IDs and on CSS classes.

This feature is generally available (GA) and accessible only through the API. For more information, see [Exclude HTML content](https://cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#exclude-html-content).

---
## 2025-05-29

### Feature

**Vertex AI Search: Adjust autocomplete settings to reduce risk of PII leaks (Public preview)**

If you use either the search history or user events model for autocomplete suggestions and you have concerns about your users entering their personally identifiable information (PII) as search queries, then see [Reduce the risk of returning suggestions that contain PII](https://cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete#update-thresholds).

This feature is in Public preview.

---
