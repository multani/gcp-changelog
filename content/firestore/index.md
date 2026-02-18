# Firestore

## 2026-02-17

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
