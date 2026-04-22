# Agent Registry

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
