# AI Applications

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
