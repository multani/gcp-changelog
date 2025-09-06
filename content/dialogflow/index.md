# Dialogflow

## 2025-09-04

### Announcement

**Dialogflow CX (Conversational Agents)**: *This is a correction of the release note posted on [August 7, 2025](https://cloud.google.com/dialogflow/docs/release-notes#August_07_2025)*. All deactivated models are now automatically upgraded to model `gemini- 2.5-flash` with the exception of **generative fallback**, which is automatically upgraded to `gemini-2.5-flash-lite`.

### Feature

**Dialogflow CX (Conversational Agents)**: The following regions are now available:

* `asia-southeast2`
* `europe-west4`
* `europe-west6`

### Feature

**Dalogflow CX (Conversational Agents)**: New prompt security controls are available in **agent settings**. See the [agent settings documentation](https://docs.google.com/document/d/1JsI5akdrE0jeut-dTS1niBWCycpa3JbnzzwELtAicxA/edit?resourcekey=0-fW6C0xA5t-bEBypItPV3XA&tab=t.0) for details.

### Feature

**Dialogflow CX (Conversational Agents)** The [model](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions) `gemini-2.5-flash-lite` is now available in all regions, and `gemini-2.5-flash` is now GA. These changes apply to the following features:

* Generators
* Playbooks
* Data store tools

---
## 2025-08-07

### Deprecated

**Dialogflow CX and Vertex AI**: The `gemini-1.0-pro`, `gemini-1.5-pro` and `gemini-1.5-flash` models will be deprecated on **September 1, 2025** and automatically upgraded to the `gemini-2.0-flash-001` model. This change applies to Vertex AI agents and the following Conversational Agents generative features:

* Playbooks
* Data stores
* Generators
* Generative Fallback

After the upgrade on September 1, 2024, `gemini-2.0-flash-001` will be automatically selected in the console. We recommend that you upgrade to the new model early to allow enough time for testing and to ensure that your solution works as intended.

---
## 2025-07-31

### Feature

**Conversational Agents**: [Routine playbooks](https://cloud.google.com/dialogflow/cx/docs/concept/playbook#routine) are now generally available.

### Feature

**Conversational Agents**: [Parameter passing](https://cloud.google.com/dialogflow/cx/docs/concept/playbook/parameter#passing-parameters) is now available and documented between routine playbooks, task playbooks, and flows.

---
## 2025-07-24

### Feature

**Conversational Agents**: 21 new [Chirp 3 HD voices](https://cloud.google.com/text-to-speech/docs/chirp3-hd) are now available across 34 locales.

### Feature

**Conversational Agents data stores**: Conversational Agents now supports AlloyDB AI, Bigtable, Firestore, Spanner and Cloud SQL data store source as public GA features; Microsoft Entra ID source has now private GA support. See the [data store documentation](https://cloud.google.com/dialogflow/cx/docs/concept/data-store) for a complete list.

---
## 2025-07-17

### Feature

**Conversational Agents**: CMEK is now available in EU regions.

### Feature

**Conversational Agents**: The [conversational history flow analysis feature](https://cloud.google.com/dialogflow/cx/docs/concept/conversation-history#flow-analysis-table) is now available.

### Feature

**Conversational Agents**: The [model](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions) `gemini-2.5-flash` is now available in all regions. This change applies to the following features:

* Generators
* Playbooks (Public Preview)
* Data stores tools (Public Preview)

---
## 2025-06-26

### Feature

**Conversational Agents data stores**: Conversational Agents now supports AlloyDB, Bigtable, Firestore, Spanner and Cloud SQL [data store sources](https://cloud.google.com/dialogflow/cx/docs/concept/data-store#sources) as public GA features. Microsoft Entra ID source has now private GA support.

### Feature

**Conversational Agents data stores**: You can now create some data store types directly within the Conversational Agents console rather than needing to use AI Applications. See the [data store creation documentation](https://cloud.google.com/dialogflow/cx/docs/concept/data-store/handler#data-store-console) for details.

---
## 2025-06-12

### Feature

**Conversational Agents**: New [Chirp 3 HD](https://cloud.google.com/text-to-speech/docs/chirp3-hd) Cloud Text-to-Speech voice **Autonoe** is now available.

### Feature

**Conversational Agents**: Conversational Agents console now supports [test cases](https://cloud.google.com/dialogflow/cx/docs/concept/test-case).

### Announcement

**Conversational Agents**: Service agent access tokens used for authentication by both webhooks and tools are now discontinued as mentioned in notification emails to customers earlier this year. Most customers can use service accounts instead.

### Changed

**Data store handlers**: Data store handler use tracking for billing purposes has been corrected.

---
