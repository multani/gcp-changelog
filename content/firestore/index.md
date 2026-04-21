# Firestore

## 2026-04-20

### Feature

The Firestore emulator now supports Enterprise edition.
See [Start emulator in specific edition](https://docs.cloud.google.com/firestore/native/docs/emulator#starting_emulator_in_specific_edition).

### Feature

Firestore Enterprise edition in Native mode and the Pipeline
operations interface are now supported at the General Availability ([GA](https://cloud.google.com/products#product-launch-stages)) level.

### Feature

Firestore Enterprise edition now supports
[Text search](https://docs.cloud.google.com/firestore/native/docs/text-search) and [Geospatial search](https://docs.cloud.google.com/firestore/native/docs/geospatial-search).

These features are in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

The [Firestore remote MCP server](https://docs.cloud.google.com/firestore/native/docs/use-firestore-mcp)
is now supported at the General Availability
([GA](https://cloud.google.com/products#product-launch-stages)) level.

### Feature

You can now use pipeline operations to perform joins with subqueries.
To learn more, see
[Perform joins with subqueries](https://docs.cloud.google.com/firestore/native/docs/pipeline/perform-joins-with-sub-pipelines).

### Feature

Firestore Enterprise edition now supports the
`update(...)` and `delete()` pipeline operation stages.
Use these stages to [Modify data with Pipeline operations](https://docs.cloud.google.com/firestore/native/docs/pipeline/dml).

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2026-04-13

### Feature

You can now use the **Usage Insights** dashboard in the
Google Cloud console to monitor and analyze your billable usage for specific
Firestore databases. Usage insights help you track granular usage
data, optimize costs, and monitor historical trends.

To learn more, see the guide to analyze usage insights for [Native mode](https://docs.cloud.google.com/firestore/native/docs/usage-insights) and [MongoDB compatibility mode](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/usage-insights).

---
## 2026-03-23

### Feature

Regional and Multi-Regional endpoints for the Firestore API
are now Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)).
You can use a Regional or a Multi-Regional endpoint to ensure that your
application's requests are transmitted, stored and processed in the same region
or multi-region as your database's location.

To learn more, see the
[Firestore regional endpoints](https://docs.cloud.google.com/firestore/native/docs/regional-endpoints)
guide.

You can also use
[Private Service Connect regional endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints)
and [Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends)
to connect to the regional and the multi-regional endpoints of the
Firestore API.

---
## 2026-03-05

### Feature

Firestore Enterprise edition now supports Native mode in
all supported regions. For a list of supported regions, see
[Locations](https://docs.cloud.google.com/firestore/native/docs/locations).

---
## 2026-02-17

### Change

After March 17, 2026, when you enable Firestore, the Firestore
MCP server is automatically enabled.

### Deprecated

Control of MCP use with organization policies is deprecated. After March 17,
2026, organization policies that use the `gcp.managed.allowedMCPServices`
constraint won't work, and you can control MCP use with IAM deny policies. For
more information about controlling MCP use, see
[Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

### Announcement

New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see [Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/firestore/native/docs/secure-agent-interactions-mcp).

---
## 2026-02-10

### Feature

You can now use the [Firestore remote MCP server](https://docs.cloud.google.com/firestore/native/docs/use-firestore-mcp).
The Firestore remote MCP server lets you interact with documents stored
in a Firestore database from your AI application.

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2026-02-02

### Feature

The Firestore databases page in the Google Cloud console now includes
a status column. Possible statuses include:

* Ready
* Cloning is in progress
* Restoring from backup is in progress
* Deleted
* Failed

For the cloning and restore statuses, the status column updates upon completion.

---
## 2026-01-15

### Feature

Firestore Enterprise edition now supports Native mode and the Pipeline operations interface.

Pipeline operations are a new query interface for Firestore.
This interface provides advanced query functionality that includes complex
expressions. It also adds support for many new functions like `min`, `max`,
`substring`, `regex_match` and `array_contains_all`.

With Firestore Enterprise edition in Native mode,
index creation is also completely optional, streamlining the process of developing new queries.

To learn more about Pipeline operations,
see the [query interfaces overview](https://docs.cloud.google.com/firestore/native/docs/query-data/understanding-core-pipelines).

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-11-21

### Feature

Support for Object as document `_id` identifier.

---
## 2025-10-27

### Feature

The [database clone feature](https://docs.cloud.google.com/firestore/native/docs/manage-databases#clone-database) is now
supported at the General Availability ([GA](https://cloud.google.com/products#product-launch-stages)) level.

---
## 2025-09-23

### Feature

You can now query your databases and update data using the [dedicated Gemini CLI extension for Firestore](https://cloud.google.com/firestore/native/docs/connect-ide-using-mcp-toolbox#about-gemini-cli-extension). This feature is available in beta.

---
## 2025-09-02

### Feature

Use [Query insights](https://cloud.google.com/firestore/native/docs/query-insights) to view query performance metrics for your database. This feature is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-08-01

### Feature

You can [clone an existing database](https://cloud.google.com/firestore/native/docs/manage-databases#clone-database) at a selected timestamp into a new database. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
