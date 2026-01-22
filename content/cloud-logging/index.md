# Cloud Logging

## 2026-01-20

### Announcement

Cloud Logging adds support for the `asia-southeast3` region. For a complete
list of supported regions, see
[Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).

---
## 2025-12-12

### Change

The default setting for the time-range selector for the
Logs Explorer is now five minutes. The previous default was one hour.

---
## 2025-12-08

### Feature

You can now install and manage the Ops Agent on virtual machines in
a specified zone by using VM Extension Manager extension policies.
You can use extension policies to keep the installed version of the agent
current, keep a specified version of the agent installed, and other tasks.
For more information, see [Install and manage the Ops Agent by using
VM Extension Manager policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies).

---
## 2025-10-09

### Feature

The query builder in the Log Analytics page is
[generally available](https://docs.cloud.google.com/products#product-launch-stages) (GA). For more
information, see [Build, edit, and run a query](https://docs.cloud.google.com/logging/docs/analyze/query-and-view#query-builder).

---
## 2025-09-22

### Announcement

Cloud Logging has removed the quota for write requests per minute, which has been replaced by volume-based regional quotas. We've also removed the references to August dates for the removal of the old quota from the public documentation. For more information, see [Logging API quotas and limits](https://cloud.google.com/logging/quotas#api-limits).

---
## 2025-09-15

### Libraries

### Java

#### [3.23.4](https://github.com/googleapis/java-logging/compare/v3.23.3...v3.23.4) (2025-09-11)

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 ([1438bff](https://github.com/googleapis/java-logging/commit/1438bff5bc7028fbf125895f0bdd2bb50490effa))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#1853](https://github.com/googleapis/java-logging/issues/1853)) ([c21a635](https://github.com/googleapis/java-logging/commit/c21a635f054b1cd8a6e5aea7450017af85ba03c7))
* Update googleapis/sdk-platform-java action to v2.62.1 ([#1855](https://github.com/googleapis/java-logging/issues/1855)) ([b6ce498](https://github.com/googleapis/java-logging/commit/b6ce4988391dba73e019aa9f597ce6cc23f81a8c))

---
## 2025-09-08

### Libraries

### Node.js

#### [11.2.1](https://github.com/googleapis/nodejs-logging/compare/v11.2.0...v11.2.1) (2025-09-03)

##### Bug Fixes

* **logging:** Specifying resourceNames should fetch logs only from those resources ([#1597](https://github.com/googleapis/nodejs-logging/issues/1597)) ([ff7899f](https://github.com/googleapis/nodejs-logging/commit/ff7899f5e91da6540d3f68476b2d9acd58ff0993))

---
## 2025-08-25

### Libraries

### Java

#### [3.23.3](https://github.com/googleapis/java-logging/compare/v3.23.2...v3.23.3) (2025-08-20)

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#1848](https://github.com/googleapis/java-logging/issues/1848)) ([162ef56](https://github.com/googleapis/java-logging/commit/162ef563793270c236ecf7ca2524ad3b560d7a12))

---
## 2025-08-11

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-logging](https://github.com/googleapis/java-logging)

#### [3.23.2](https://github.com/googleapis/java-logging/compare/v3.23.1...v3.23.2) (2025-08-05)

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 ([0a21b83](https://github.com/googleapis/java-logging/commit/0a21b83377e6e6a2f4cf98149424a47dcd490c1c))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#1843](https://github.com/googleapis/java-logging/issues/1843)) ([975d8ae](https://github.com/googleapis/java-logging/commit/975d8aeca38ff2f2f8317df93a661910969c5fc1))

---
## 2025-08-04

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-logging](https://github.com/googleapis/java-logging)

#### [3.23.1](https://github.com/googleapis/java-logging/compare/v3.23.0...v3.23.1) (2025-07-28)

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([6a268f8](https://github.com/googleapis/java-logging/commit/6a268f8dbb33b38fa5e4d35d8dfcd196f8fcf9db))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#1834](https://github.com/googleapis/java-logging/issues/1834)) ([2e46f6e](https://github.com/googleapis/java-logging/commit/2e46f6ef44278af5031167106c216dcdb0a16357))

### Feature

You can now build queries without manually writing SQL in the Log Analytics page by using the query builder. This feature is in Public Preview. For more information, see [Build and run a SQL query](https://cloud.google.com/logging/docs/analyze/query-and-view#query-builder).

---
## 2025-07-14

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-logging](https://github.com/googleapis/java-logging)

#### [3.23.0](https://github.com/googleapis/java-logging/compare/v3.22.6...v3.23.0) (2025-07-11)

##### Features

* Next release from main branch is 3.23.0 ([#1826](https://github.com/googleapis/java-logging/issues/1826)) ([f0ef15f](https://github.com/googleapis/java-logging/commit/f0ef15f609a3400460bd8074bdd05014cc388743))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#1828](https://github.com/googleapis/java-logging/issues/1828)) ([44c3094](https://github.com/googleapis/java-logging/commit/44c3094e23450f1a8e6bb397f209b17cf37a4345))

---
## 2025-06-30

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-logging](https://github.com/googleapis/java-logging)

#### [3.22.6](https://github.com/googleapis/java-logging/compare/v3.22.5...v3.22.6) (2025-06-25)

##### Bug Fixes

* Regenerate gapic yaml and service yaml for logging by augmentation configs ([9023895](https://github.com/googleapis/java-logging/commit/9023895fd56381c1f4309843a269975763a89d40))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.50.0 ([#1821](https://github.com/googleapis/java-logging/issues/1821)) ([af4edc5](https://github.com/googleapis/java-logging/commit/af4edc5b1399b3563d9cf07e171c4281fde2bb79))
* Update googleapis/sdk-platform-java action to v2.60.0 ([#1822](https://github.com/googleapis/java-logging/issues/1822)) ([0a96dd5](https://github.com/googleapis/java-logging/commit/0a96dd52dc1594767b7dd60da99a17bac8ac14ba))

---
## 2025-06-09

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-logging](https://github.com/googleapis/java-logging)

#### [3.22.5](https://github.com/googleapis/java-logging/compare/v3.22.4...v3.22.5) (2025-06-05)

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.59.0 ([f2362fb](https://github.com/googleapis/java-logging/commit/f2362fb4c05d34fda4a1c9788ea87822ac887d9e))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#1813](https://github.com/googleapis/java-logging/issues/1813)) ([c15da84](https://github.com/googleapis/java-logging/commit/c15da84716d6d554ae26919412e8d4313fd980bc))

---
## 2025-06-06

### Announcement

Cloud Logging begins enforcement of the new volume-based regional quotas. For more information, see [Logging API quotas and limits](https://cloud.google.com/logging/quotas#api-limits).

---
## 2025-06-04

### Feature

You can now cancel a running query in the Logs Explorer by clicking the **Stop query** button.

---
## 2025-05-29

### Feature

You can now configure the observability scope or set the default log scope by using the Google Cloud CLI. You must use version 254.0 or higher. For more information, see [Configure observability scopes](https://cloud.google.com/stackdriver/docs/scopes/configure) and [Set the default log scope](https://cloud.google.com/logging/docs/log-scope/create-and-manage#set-default).

---
