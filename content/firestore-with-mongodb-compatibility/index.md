# Firestore with MongoDB compatibility

## 2026-04-20

### Feature

The maximum document size has been
increased to 16 MiB. To learn more, see [Behavior differences](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/behavior-differences#documents).

### Feature

Support for text and geospatial search. You
can create text indexes, perform text and geospatial search queries using
the `$text` and `$near` operators, handle language settings, and calculate
relevance scores. To learn more, see [Text search](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/text-query)
and [Geospatial search](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/geo-query).

These features are available in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

`$lookup` now supports `let` and `pipeline`.

### Feature

Support for [Change Streams](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/change-streams).
Change streams let applications access real-time changes (inserts, updates, and deletes) made to a
collection or to an entire database.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

Support for the `drop()` command to delete entire collections.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-04-09

### Feature

You can now use
Gemini Code Assist to get AI-powered assistance in Firestore
to [generate MQL queries using natural language prompts](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/write-mql-gemini).
This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-03-16

### Feature

Support for [managing TTL indexes](https://cloud.google.com/firestore/mongodb-compatibility/docs/ttl#create_ttl_index) in the MongoDB API.

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
## 2025-11-21

### Feature

Support for Object as document `_id` identifier.

---
