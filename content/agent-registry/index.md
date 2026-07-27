# Agent Registry

## 2026-07-23

### Feature

Agent skill governance is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Agent Registry supports standalone skill governance, helping enable secure, enterprise-level management and governance of standalone skills for AI agents. You can register skill resources, upload and validate ZIP payload packages, track version history through immutable skill revisions, and review verified skill publishers.

This release includes the following features:

* **Lifecycle and versioning:** Register and manage standalone `Skill` resources, lifecycle states, and version snapshots (`SkillRevision`).
* **Console support:** A dedicated **Skills** tab in Google Cloud Console to register, update, download, and monitor skills and revisions.
* **Access policy enforcement:** Use policy bindings to authorize reasoning engine agents to load standalone skills.
* **Semantic search:** Query the registry to search and discover standalone skills.

For more information, see [Register skills](https://docs.cloud.google.com/agent-registry/register-skills) and [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).

---
## 2026-06-18

### Announcement

Agent Registry is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

The following are features available in Agent Registry for the GA launch stage:

* **API v1 and client libraries:** The `v1` version of the Agent Registry API is available. Cloud client libraries are available in C#, Go, Java, Node.js, PHP, Python, and Ruby.
* **A2A v1 support:** Agent Registry supports Agent-to-Agent (A2A) protocol version `1.0`, letting you explicitly declare transport endpoints and bindings inside the `supportedInterfaces` array, in addition to the existing `0.3` schema support.
* **Terraform support:** Terraform scripts for Application Default Credentials (ADC) have graduated to General Availability. You can use Terraform to configure and manage your agents, MCP servers, endpoints, and bindings.

**Known limitations:**

* **Access Transparency and Access Approval:** [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) logs, which provide visibility into when Google personnel access your content, and [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) controls aren't available for Agent Registry configurations.

---
## 2026-04-22

### Issue

The following known issues affect Agent Registry:

* **Search location filtering:** When calling the `SearchAgents` or `SearchMcpServers` APIs for the `global` location, the results might incorrectly include resources from `us` and `eu` multi-regions.
* **URN mismatch:** When searching for agents or MCP servers in the Google Cloud console, the page might display an invalid URN format in the search results list.
* **Console error:** Users who actively switch between tabs on the MCP server details page in the Google Cloud console might encounter an unexpected throttling error.

### Announcement

The Agent Registry remote Model Context Protocol (MCP) server is available in [Preview](https://cloud.google.com/products#product-launch-stages). You can connect your AI applications to the Agent Registry MCP server to dynamically discover other agents, endpoints, and MCP servers available in your environment.

For more information, see [Use the Agent Registry remote MCP server](https://docs.cloud.google.com/agent-registry/use-agentregistry-mcp).

### Announcement

Agent Registry is available in [Preview](https://cloud.google.com/products#product-launch-stages). Agent Registry is a centralized catalog for discovering and registering agents and Model Context Protocol (MCP) servers.

For more information, see the [Agent Registry overview](https://docs.cloud.google.com/agent-registry/overview).

---
