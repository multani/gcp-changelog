# Vertex AI Search

## 2026-02-05

### Feature

**Vertex AI Search: MCP server (Public Preview)**

Vertex AI Search has a Model Context Protocol (MCP) server hosted at the
following endpoint: `https://discoveryengine.googleapis.com/mcp`

This feature is in Public Preview. For more information, see [MCP Reference:
discoveryengine.googleapis.com](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/mcp).

---
## 2026-01-26

### Feature

**Vertex AI Search: Change the pricing model for apps and data stores**

There are two pricing models for apps and data stores: the general model
(pay-as-you-go consumption-based) and the configurable subscription model (a
monthly subscription).

If you have enabled configurable pricing for your project, you can change the
pricing model for apps and data stores from configurable to general, as well as
from general to configurable. See [Disable configurable
pricing](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing#disable-configurable-pricing).

---
## 2025-12-16

### Feature

**Vertex AI Search: Filter searches by document-level relevance (Public Preview)**

When searching in your Vertex AI Search app, you can specify
document-level relevance filters so that only the documents that meet the
filter threshold are returned as results.

You can specify either the relevance threshold or semantic-relevance threshold to
filter documents by relevance based on keyword and semantic search similarity.

This feature is in Public Preview. For more information, see
[Filter searches by document-level relevance](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance).

---
## 2025-12-09

### Feature

**Vertex AI Search: Configurable pricing for custom search (GA)**

Configurable pricing is available for custom search apps and data stores.

Configurable pricing offers a flexible alternative to the default pay-as-you-go
model. Configurable pricing lets you to choose a subscription that fits your
needs. There are two subscriptions, one for storage and one for search queries,
plus add-ons that let you add more features according to your needs.

For storage, the minimum subscription is 50 GiB/month and the available
add-on is semantic embedding. For search queries, the minimum subscription is
1000 queries per minute per project, and the available add-ons are semantic
query, KPI & personalization, and AI overview.

After you set up configurable pricing for a project, apply configurable pricing
to apps and data stores as needed. In a project, you can have some apps and
data store using the general pricing and others using configurable pricing.

Configurable pricing is generally available (GA). For more information, see
[Enable configurable pricing for custom
search](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing) and [Vertex
AI Search pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing).

---
## 2025-11-24

### Feature

**Vertex AI Search: Natural language query filters (GA)**

For queries on structured data stores, the natural language queries can be
reformulated as filters and a residual query. For example, "Find a coffee shop
serving banana bread" becomes `"query": "banana bread", "filter": "type":
ANY("cafe")`.

The natural-language query understanding feature only applies to custom search
apps attached to a single, structured, data store.

By default, a hard restriction filter is applied, but a softer, boost-like
filter can be used instead.

This feature is generally available (GA). For more information, see [Filter with
natural language
understanding](https://docs.cloud.google.com/generative-ai-app-builder/docs/natural-language-queries).

---
## 2025-11-21

### Feature

**Vertex AI Search: Allowlist fields for natural language query understanding**

You can specify an allowlist of fields to be used for filter extraction. If you
have some fields, perhaps for internal use, that you don't want to be used in
filters, then specify an allowlist to restrict the fields that can be used.

For more information, see [Specify fields for natural-language
queries](https://docs.cloud.google.com/generative-ai-app-builder/docs/natural-language-queries#search-nl-allowlist).

---
## 2025-11-20

### Feature

**Vertex AI Search: Updated file size restrictions for unstructured data**

The file size restrictions for unstructured data import have been unified. For
unstructured data, you can import files up to 200 MB regardless of the
parser type.

For more information, see [Unstructured
data](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#unstructured).

---
## 2025-11-14

### Feature

**Vertex AI Search: Gemini layout parser (Public Preview)**

For data stores with unstructured documents, you can use Gemini to
get layout analysis and content extraction on PDF files. Layout parsing
with Gemini provides high quality table recognition, improved reading order and
more accurate text recognition.

This feature is in Public Preview. For more information, see [Parse and chunk
documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents).

---
## 2025-11-05

### Feature

**Vertex AI Search: Layout parser support for DOCX, PPTX, and XLSX (GA)**

With the layout parser, support for parsing DOCX, PPTX, and XLSX file formats is
Generally Available (GA). Both the layout and digital parsers can parse PDF,
HTML, DOCX, PPTX, and XLSX files.
For more information about the parsers, see [Parse and chunk
documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents).

**Important:** If you have been using the layout parser for these file formats,
you will now be billed when parsing new documents. For
information about layout parser pricing, see [Document AI feature
pricing](https://cloud.google.com/document-ai/pricing).

---
## 2025-10-02

### Changed

**Vertex AI Search: Renamed from AI Applications**

The AI Applications product has been renamed as Vertex AI Search in the following contexts:

* The documentation set. See [What is Vertex AI Search?](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction)
* The marketing collateral. See [Vertex AI Search](https://docs.cloud.google.com/enterprise-search).

What has not changed:

* The user interface in the Google Cloud console is still referred to as AI Applications. See [AI Applications](https://console.cloud.google.com/gen-app-builder).
* The APIs still use the DiscoveryEngine API endpoints. See [APIs and reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis).

Despite the rebrand, the product functionality remains the same.

---
