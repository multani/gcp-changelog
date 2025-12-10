# Spanner

## 2025-12-10

### Feature

Spanner now supports the following new columns in the `SPANNER_SYS`
[oldest active queries](https://docs.cloud.google.com/spanner/docs/introspection/oldest-active-queries)
table:

* `CLIENT_IP_ADDRESS`
* `API_CLIENT_HEADER`
* `USER_AGENT_HEADER`
* `SERVER_REGION`
* `PRIORITY`
* `TRANSACTION_TYPE`

You can also view these columns in the Spanner **query insights** page
on the Google Cloud console. For more information, see
[Monitor active queries](https://docs.cloud.google.com/spanner/docs/monitor-active-queries#view-longest-running-queries).

---
## 2025-12-03

### Changed

String values in
[Spanner Studio query results](https://docs.cloud.google.com/spanner/docs/manage-data-using-console#create-modify-query-data)
are now enclosed in double quotes, providing a clear visual cue to differentiate
string values from other data types. This enhancement is for display purposes
only and does not affect how data is exported or accessed.

---
## 2025-11-20

### Feature

Query optimizer version 8 is now the [default version](https://docs.cloud.google.com/spanner/docs/query-optimizer/versions) for Spanner.

---
## 2025-11-11

### Feature

[Spanner Studio](https://docs.cloud.google.com/spanner/docs/manage-data-using-console)
now supports several new export options for your query results. You can export
to a CSV or JSON file, Google Sheets, or copy the results to a clipboard. For
more information, see
[Create, modify, and query your data](https://docs.cloud.google.com/spanner/docs/manage-data-using-console#create-modify-query-data).

---
## 2025-11-10

### Feature

Spanner now automatically provides recommendations to apply
[schema design best practices](https://docs.cloud.google.com/spanner/docs/schema-design)
to your databases. You can view these schema issue recommendations on the
Spanner Studio page for your database. For more information, see
[View schema design best practice recommendations](https://docs.cloud.google.com/spanner/docs/manage-data-using-console#recommend-schema-best).
This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages%22%3E).

---
## 2025-10-31

### Libraries

A monthly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)

#### [6.102.1](https://github.com/googleapis/java-spanner/compare/v6.102.0...v6.102.1) (2025-10-23)

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([c1a8238](https://github.com/googleapis/java-spanner/commit/c1a8238af33a083411f63cf6276eb683ee67ac6a))
* Do a quick check if the application runs on Google Cloud ([#4163](https://github.com/googleapis/java-spanner/issues/4163)) ([b9d7daf](https://github.com/googleapis/java-spanner/commit/b9d7daf000c0fb8b67142c6161bb578cadf49b18))
* Migrate away from GoogleCredentials.fromStream() usages ([#4151](https://github.com/googleapis/java-spanner/issues/4151)) ([94d0474](https://github.com/googleapis/java-spanner/commit/94d0474ace62ea1059e5b69243f0b6eef31ddd06))

##### Dependencies

* Update actions/checkout action to v5 ([#4158](https://github.com/googleapis/java-spanner/issues/4158)) ([b32ebcf](https://github.com/googleapis/java-spanner/commit/b32ebcf96bbf696b1eb84204622463fac59be017))
* Update actions/checkout action to v5 ([#4161](https://github.com/googleapis/java-spanner/issues/4161)) ([02a17c6](https://github.com/googleapis/java-spanner/commit/02a17c6e6253e026cb3c6360eb925a322143b518))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#4178](https://github.com/googleapis/java-spanner/issues/4178)) ([24fe194](https://github.com/googleapis/java-spanner/commit/24fe194fa3595b2ab817b9fc4cd57840250fef1f))
* Update dependency net.bytebuddy:byte-buddy to v1.17.8 ([#4154](https://github.com/googleapis/java-spanner/issues/4154)) ([c911381](https://github.com/googleapis/java-spanner/commit/c911381c2ca9cd46fbeb831c659aaf55f21437f2))
* Update dependency net.bytebuddy:byte-buddy-agent to v1.17.8 ([#4155](https://github.com/googleapis/java-spanner/issues/4155)) ([3075df7](https://github.com/googleapis/java-spanner/commit/3075df714b1787512174b3f18cbc802359d442dc))
* Update googleapis/sdk-platform-java action to v2.63.0 ([#4179](https://github.com/googleapis/java-spanner/issues/4179)) ([5f48191](https://github.com/googleapis/java-spanner/commit/5f481913d60372fccf399c5c0e168b7d0c553ba0))

##### Documentation

* Add warning for encoded credential ([#4182](https://github.com/googleapis/java-spanner/issues/4182)) ([92620f9](https://github.com/googleapis/java-spanner/commit/92620f969908a8ba7fcf92d0b350a8c4d05398f8))

#### [6.102.0](https://github.com/googleapis/java-spanner/compare/v6.101.1...v6.102.0) (2025-10-08)

##### Features

* Add connection property for gRPC interceptor provider ([#4149](https://github.com/googleapis/java-spanner/issues/4149)) ([deb8dff](https://github.com/googleapis/java-spanner/commit/deb8dff6c01c37a3158e8f4a28ef5e821d10092a))
* Support statement\_timeout in connection url ([#4103](https://github.com/googleapis/java-spanner/issues/4103)) ([542c6aa](https://github.com/googleapis/java-spanner/commit/542c6aa63bfdd526070f14cb76921dd34527c1f9))

##### Bug Fixes

* Automatically set default\_sequence\_kind for CREATE SEQUENCE ([#4105](https://github.com/googleapis/java-spanner/issues/4105)) ([3beea6a](https://github.com/googleapis/java-spanner/commit/3beea6ac4eb53b70db34e0a2d2e33e56f450c88b))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.62.3 ([7047a3a](https://github.com/googleapis/java-spanner/commit/7047a3ae31aae51e9e23758fe004b93855a0ee4b))

##### Dependencies

* Update actions/checkout action to v5 ([#4069](https://github.com/googleapis/java-spanner/issues/4069)) ([4c88eb9](https://github.com/googleapis/java-spanner/commit/4c88eb91a321aa718f957296012f9e7501c7caec))
* Update actions/checkout action to v5 ([#4106](https://github.com/googleapis/java-spanner/issues/4106)) ([14ebdb3](https://github.com/googleapis/java-spanner/commit/14ebdb35c33442c4e0f70d63dce3425edb730525))
* Update actions/setup-java action to v5 ([#4071](https://github.com/googleapis/java-spanner/issues/4071)) ([e23134a](https://github.com/googleapis/java-spanner/commit/e23134a2f864e8abd2890ac3a81ff6b668afbe63))
* Update all dependencies ([#4099](https://github.com/googleapis/java-spanner/issues/4099)) ([b262edc](https://github.com/googleapis/java-spanner/commit/b262edcfc4713bb64986bc4acd3f02b69d3367f8))
* Update dependency com.google.api.grpc:grpc-google-cloud-monitoring-v3 to v3.77.0 ([#4117](https://github.com/googleapis/java-spanner/issues/4117)) ([2451ca2](https://github.com/googleapis/java-spanner/commit/2451ca2abe1dd2de3907b88e8d18beab1a15a634))
* Update dependency com.google.api.grpc:proto-google-cloud-monitoring-v3 to v3.77.0 ([#4143](https://github.com/googleapis/java-spanner/issues/4143)) ([6c9dc26](https://github.com/googleapis/java-spanner/commit/6c9dc26330cf66f196adc2203323a482e08f0325))
* Update dependency com.google.api.grpc:proto-google-cloud-trace-v1 to v2.76.0 ([#4144](https://github.com/googleapis/java-spanner/issues/4144)) ([d566a42](https://github.com/googleapis/java-spanner/commit/d566a4295be018070169ba082a018394a2e60b45))
* Update dependency com.google.cloud:google-cloud-monitoring to v3.77.0 ([#4145](https://github.com/googleapis/java-spanner/issues/4145)) ([8917c05](https://github.com/googleapis/java-spanner/commit/8917c054410e4035d6d4e201e43599d5ddc1fadd))
* Update dependency com.google.cloud:google-cloud-monitoring to v3.77.0 ([#4146](https://github.com/googleapis/java-spanner/issues/4146)) ([4ebea1a](https://github.com/googleapis/java-spanner/commit/4ebea1adf726069084087ce46900f3174658055c))
* Update dependency com.google.cloud:google-cloud-trace to v2.76.0 ([#4147](https://github.com/googleapis/java-spanner/issues/4147)) ([4b1d4af](https://github.com/googleapis/java-spanner/commit/4b1d4af19336e493af38a1e58c95786da3892d34))
* Update dependency com.google.cloud:google-cloud-trace to v2.76.0 ([#4148](https://github.com/googleapis/java-spanner/issues/4148)) ([8f91a89](https://github.com/googleapis/java-spanner/commit/8f91a894771653213b6fcded5795349ad7ea6724))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 ([#4107](https://github.com/googleapis/java-spanner/issues/4107)) ([8a8a042](https://github.com/googleapis/java-spanner/commit/8a8a042494b092b3dddd0c9606a63197d8a23555))
* Update dependency org.json:json to v20250517 ([#3881](https://github.com/googleapis/java-spanner/issues/3881)) ([5658c83](https://github.com/googleapis/java-spanner/commit/5658c8378aa2e8028d4ef7dfaf94b647f33cd812))
* Update googleapis/sdk-platform-java action to v2.62.3 ([#4108](https://github.com/googleapis/java-spanner/issues/4108)) ([65913ec](https://github.com/googleapis/java-spanner/commit/65913ec0638fec4ea536cf42f8fe25460133f68e))

### Node.js

### Changes for [@google-cloud/spanner](https://github.com/googleapis/nodejs-spanner)

#### [8.2.2](https://github.com/googleapis/nodejs-spanner/compare/v8.2.1...v8.2.2) (2025-10-07)

##### Bug Fixes

* Correctly determine project ID for metrics export ([#2427](https://github.com/googleapis/nodejs-spanner/issues/2427)) ([0d63312](https://github.com/googleapis/nodejs-spanner/commit/0d633126a87c1274abfd59550cb94052a819fcaa))
* Metrics Export Error log ([#2425](https://github.com/googleapis/nodejs-spanner/issues/2425)) ([110923e](https://github.com/googleapis/nodejs-spanner/commit/110923ea1dc6f6c891e0f70406b3839224a25b9e))

### Python

### Changes for [google-cloud-spanner](https://github.com/googleapis/python-spanner)

#### [3.59.0](https://github.com/googleapis/python-spanner/compare/v3.58.0...v3.59.0) (2025-10-18)

##### Features

* **spanner:** Add lazy decode to partitioned query ([#1411](https://github.com/googleapis/python-spanner/issues/1411)) ([a09961b](https://github.com/googleapis/python-spanner/commit/a09961b381314e3f06f1ff4be7b672cd9da9c64b))

##### Bug Fixes

* **spanner:** Resolve TypeError in metrics resource detection ([#1446](https://github.com/googleapis/python-spanner/issues/1446)) ([7266686](https://github.com/googleapis/python-spanner/commit/7266686d6773f39a30603061ae881e258421d927))

##### Documentation

* Add snippet for Repeatable Read configuration at client and transaction ([#1326](https://github.com/googleapis/python-spanner/issues/1326)) ([58e2406](https://github.com/googleapis/python-spanner/commit/58e2406af3c8918e37e0daadefaf537073aed1a4))

---
## 2025-10-29

### Feature

[Named schemas](https://docs.cloud.google.com/spanner/docs/named-schemas) are supported in Spanner Graph. For more information, see [Spanner Graph schema overview](https://docs.cloud.google.com/spanner/docs/graph/schema-overview).

---
## 2025-10-21

### Feature

[Schema object drop protection](https://docs.cloud.google.com/spanner/docs/schema-drop-protection) is now generally available. This feature protects schema objects such as tables, indexes, and columns from accidental deletion.

---
## 2025-10-20

### Feature

You can now use the GoogleSQL [`ML.PREDICT` function](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/ml-functions#mlpredict) to convert your natural language query text into an embedding and perform approximate nearest neighbors (ANN) vector search.

---
## 2025-10-02

### Feature

You can now use repeatable read isolation (in [Preview](https://cloud.google.com/products#product-launch-stages0)) to reduce latency and transaction abort rates for workloads that have many reads contending with fewer writes. For more information, see [Repeatable read isolation](https://cloud.google.com/spanner/docs/isolation-levels#repeatable-read).

---
## 2025-10-01

### Feature

The [Spanner CLI](https://cloud.google.com/spanner/docs/spanner-cli) is generally available. Bundled with gcloud, you can use the Spanner command-line interface to open an interactive session or automate SQL executions from the shell or an input file.

---
## 2025-09-30

### Libraries

A monthly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [spanner/admin/database/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/spanner/admin/database/apiv1)

#### [1.86.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.85.1...spanner/v1.86.0) (2025-09-26)

##### Features

* **spanner:** Support "readOnly" column tag parsing for Go struct operations ([#12895](https://github.com/googleapis/google-cloud-go/issues/12895)) ([003abca](https://github.com/googleapis/google-cloud-go/commit/003abca9172082ad1f2fbcc9b37639f389ade8ee))

##### Bug Fixes

* **spanner:** Use fresh context for rollback ([#12897](https://github.com/googleapis/google-cloud-go/issues/12897)) ([99c7eeb](https://github.com/googleapis/google-cloud-go/commit/99c7eeb6ff95af9c967c78764069f752d3c26d34))

#### [1.85.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.84.1...spanner/v1.85.0) (2025-08-28)

##### Features

* **spanner:** Enable multiplex sessions by default for all operations ([#12734](https://github.com/googleapis/google-cloud-go/issues/12734)) ([0491ba6](https://github.com/googleapis/google-cloud-go/commit/0491ba6f258600cc518a5a2c274caa0fb6105c8a))

##### Performance Improvements

* **spanner:** Improve mutationProto allocations and performance ([#12740](https://github.com/googleapis/google-cloud-go/issues/12740)) ([2a4add5](https://github.com/googleapis/google-cloud-go/commit/2a4add5405205fea315b17e4f70096d4be78b506))

#### [1.85.1](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.85.0...spanner/v1.85.1) (2025-09-12)

##### Bug Fixes

* **spanner:** Disable afe\_connectivity\_error\_count metric ([#12866](https://github.com/googleapis/google-cloud-go/issues/12866)) ([baab714](https://github.com/googleapis/google-cloud-go/commit/baab714b87311822a7c8c5202430a0cd7e11cc7d))

##### Documentation

* **spanner:** A comment for enum Kind is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for enum Priority is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for enum value LOCK\_HINT\_EXCLUSIVE in enum LockHint is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for enum value LOCK\_HINT\_UNSPECIFIED in enum LockHint is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for enum value ORDER\_BY\_PRIMARY\_KEY in enum OrderBy is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for enum value ORDER\_BY\_UNSPECIFIED in enum OrderBy is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for enum value PROFILE in enum QueryMode is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for enum value SERIALIZABLE in enum IsolationLevel is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field approximate\_last\_use\_time in message .google.spanner.v1.Session is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field auto\_failover\_disabled in message .google.spanner.v1.DirectedReadOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field columns in message .google.spanner.v1.Mutation is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field data\_boost\_enabled in message .google.spanner.v1.ExecuteSqlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field data\_boost\_enabled in message .google.spanner.v1.ReadRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field exclude\_replicas in message .google.spanner.v1.DirectedReadOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field exclude\_txn\_from\_change\_streams in message .google.spanner.v1.BatchWriteRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field include\_replicas in message .google.spanner.v1.DirectedReadOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field index in message .google.spanner.v1.PlanNode is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field insert\_or\_update in message .google.spanner.v1.Mutation is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field key\_set in message .google.spanner.v1.Mutation is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field key\_set in message .google.spanner.v1.PartitionReadRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field key\_set in message .google.spanner.v1.ReadRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field kind in message .google.spanner.v1.PlanNode is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field last\_statement in message .google.spanner.v1.ExecuteSqlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field last\_statements in message .google.spanner.v1.ExecuteBatchDmlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field limit in message .google.spanner.v1.ReadRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field location in message .google.spanner.v1.DirectedReadOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field max\_commit\_delay in message .google.spanner.v1.CommitRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field max\_partitions in message .google.spanner.v1.PartitionOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field multiplexed in message .google.spanner.v1.Session is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field mutation\_key in message .google.spanner.v1.BeginTransactionRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field optimizer\_statistics\_package in message .google.spanner.v1.ExecuteSqlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field optimizer\_version in message .google.spanner.v1.ExecuteSqlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field order\_by in message .google.spanner.v1.ReadRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field param\_types in message .google.spanner.v1.ExecuteBatchDmlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field param\_types in message .google.spanner.v1.ExecuteSqlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field param\_types in message .google.spanner.v1.PartitionQueryRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field params in message .google.spanner.v1.ExecuteBatchDmlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field params in message .google.spanner.v1.ExecuteSqlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field params in message .google.spanner.v1.PartitionQueryRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field partition\_size\_bytes in message .google.spanner.v1.PartitionOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field partition\_token in message .google.spanner.v1.ExecuteSqlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field partition\_token in message .google.spanner.v1.Partition is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field partition\_token in message .google.spanner.v1.ReadRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field plan\_nodes in message .google.spanner.v1.QueryPlan is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field precommit\_token in message .google.spanner.v1.CommitRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field precommit\_token in message .google.spanner.v1.ExecuteBatchDmlResponse is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field ranges in message .google.spanner.v1.KeySet is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field replace in message .google.spanner.v1.Mutation is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field request\_options in message .google.spanner.v1.BeginTransactionRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field request\_tag in message .google.spanner.v1.RequestOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field return\_commit\_stats in message .google.spanner.v1.CommitRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field seqno in message .google.spanner.v1.ExecuteBatchDmlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field seqno in message .google.spanner.v1.ExecuteSqlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field session\_count in message .google.spanner.v1.BatchCreateSessionsRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field session\_template in message .google.spanner.v1.BatchCreateSessionsRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field short\_representation in message .google.spanner.v1.PlanNode is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field single\_use\_transaction in message .google.spanner.v1.CommitRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field sql in message .google.spanner.v1.PartitionQueryRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field transaction in message .google.spanner.v1.ExecuteSqlRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field transaction in message .google.spanner.v1.PartitionQueryRequest is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field transaction\_tag in message .google.spanner.v1.RequestOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field values in message .google.spanner.v1.Mutation is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for field variable in message .google.spanner.v1.PlanNode is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for message DirectedReadOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for message DirectedReadOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for message DirectedReadOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for message Mutation is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for message PartitionOptions is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for message PlanNode is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for method BatchWrite in service Spanner is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for method Commit in service Spanner is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for method CreateSession in service Spanner is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for method DeleteSession in service Spanner is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for method ExecuteSql in service Spanner is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for method ExecuteStreamingSql in service Spanner is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for method GetSession in service Spanner is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for method PartitionQuery in service Spanner is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for method PartitionRead in service Spanner is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for method Read in service Spanner is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))
* **spanner:** A comment for method Rollback in service Spanner is changed ([51583bd](https://github.com/googleapis/google-cloud-go/commit/51583bd5c9b886d22b45da092dc8311422b8b5ac))

### Java

### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)

#### [6.99.0](https://github.com/googleapis/java-spanner/compare/v6.98.1...v6.99.0) (2025-08-26)

##### Features

* Support read lock mode for R/W transactions ([#4010](https://github.com/googleapis/java-spanner/issues/4010)) ([7d752d6](https://github.com/googleapis/java-spanner/commit/7d752d686e638b6266aab3a5188c01641d2f9adc))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.62.0 ([52c68db](https://github.com/googleapis/java-spanner/commit/52c68db5c75f24a066c2e828ed79917c824f699b))
* GetCommitResponse() should return error if tx has not committed ([#4021](https://github.com/googleapis/java-spanner/issues/4021)) ([a2c179f](https://github.com/googleapis/java-spanner/commit/a2c179f2e7c19d295bdbf9cf1bbd1c5562dd9e21))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#4024](https://github.com/googleapis/java-spanner/issues/4024)) ([7e3294f](https://github.com/googleapis/java-spanner/commit/7e3294f6d42bddb4cfff67334118f615c90c3bb7))

#### [6.100.0](https://github.com/googleapis/java-spanner/compare/v6.99.0...v6.100.0) (2025-09-11)

##### Features

* Read\_lock\_mode support for connections ([#4031](https://github.com/googleapis/java-spanner/issues/4031)) ([261abb4](https://github.com/googleapis/java-spanner/commit/261abb4b9c5ff00fac2d816a31926b23264657c4))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 ([e9773a7](https://github.com/googleapis/java-spanner/commit/e9773a7aa27a414d56093b4e09e0f197a07b5980))
* Disable afe\_connectivity\_error\_count metric ([#4041](https://github.com/googleapis/java-spanner/issues/4041)) ([f89c1c0](https://github.com/googleapis/java-spanner/commit/f89c1c0517ba6b895f405b0085b8df41aac952be))
* Skip session delete in case of multiplexed sessions ([#4029](https://github.com/googleapis/java-spanner/issues/4029)) ([8bcb09d](https://github.com/googleapis/java-spanner/commit/8bcb09d141fe986c92ccacbaa9a45302c5c8e79d))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#4034](https://github.com/googleapis/java-spanner/issues/4034)) ([13bfa7c](https://github.com/googleapis/java-spanner/commit/13bfa7c68c7ea887e679fb5504dceb85cbb43cb9))

##### Documentation

* A comment for field `ranges` in message `.google.spanner.v1.KeySet` is changed ([e9773a7](https://github.com/googleapis/java-spanner/commit/e9773a7aa27a414d56093b4e09e0f197a07b5980))

#### [6.101.1](https://github.com/googleapis/java-spanner/compare/v6.101.0...v6.101.1) (2025-09-26)

##### Bug Fixes

* Potential NullPointerException in LocalConnectionChecker ([#4092](https://github.com/googleapis/java-spanner/issues/4092)) ([3b9f597](https://github.com/googleapis/java-spanner/commit/3b9f597ba60199a16556824568b24908ce938a69))

#### [6.101.0](https://github.com/googleapis/java-spanner/compare/v6.100.0...v6.101.0) (2025-09-26)

##### Features

* Add transaction\_timeout connection property ([#4056](https://github.com/googleapis/java-spanner/issues/4056)) ([cdc52d4](https://github.com/googleapis/java-spanner/commit/cdc52d49b39c57e7255f4e09fb33a41f4810397d))
* TPC support ([#4055](https://github.com/googleapis/java-spanner/issues/4055)) ([7625cce](https://github.com/googleapis/java-spanner/commit/7625cce9ad48b14a1cff9c2ede86a066ea292bef))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.62.2 ([8d6cbf6](https://github.com/googleapis/java-spanner/commit/8d6cbf6bea9cbd823b8f0070516e34b4d8428e87))
* Potential NullPointerException in Value#hashCode ([#4046](https://github.com/googleapis/java-spanner/issues/4046)) ([74abb34](https://github.com/googleapis/java-spanner/commit/74abb341e2ea42bbf0a2de4ec3e3555335b5fd9f))
* Recalculate remaining statement timeout after retry ([#4053](https://github.com/googleapis/java-spanner/issues/4053)) ([5e26596](https://github.com/googleapis/java-spanner/commit/5e26596f4f9c924260da0908920854d8ddfc626b))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.2 ([#4057](https://github.com/googleapis/java-spanner/issues/4057)) ([d782aff](https://github.com/googleapis/java-spanner/commit/d782aff63ff81e1b760690d4dee3e566028d522e))

### Node.js

### Changes for [@google-cloud/spanner](https://github.com/googleapis/nodejs-spanner)

#### [8.2.0](https://github.com/googleapis/nodejs-spanner/compare/v8.1.0...v8.2.0) (2025-08-26)

##### Features

* **spanner:** Add support for multiplexed session for r/w transactions ([#2351](https://github.com/googleapis/nodejs-spanner/issues/2351)) ([6a9f1a2](https://github.com/googleapis/nodejs-spanner/commit/6a9f1a2b2c0dad955593571c71e9d4b6c9e7eeee))
* **spanner:** Support setting read lock mode ([#2388](https://github.com/googleapis/nodejs-spanner/issues/2388)) ([bd66f61](https://github.com/googleapis/nodejs-spanner/commit/bd66f61f3ecac65678d31cbc841c11cd0fb7c3da))

##### Bug Fixes

* **deps:** Add uuid to dependencies ([#2376](https://github.com/googleapis/nodejs-spanner/issues/2376)) ([0b2060b](https://github.com/googleapis/nodejs-spanner/commit/0b2060b4ad7302ab23ac757e79fe760e34e81083))
* **deps:** Update dependency @grpc/proto-loader to ^0.8.0 ([#2354](https://github.com/googleapis/nodejs-spanner/issues/2354)) ([75dc4da](https://github.com/googleapis/nodejs-spanner/commit/75dc4daf114cbc4eb4669ed6cb042af051cdce63))
* **deps:** Update dependency google-gax to v5.0.1 ([#2362](https://github.com/googleapis/nodejs-spanner/issues/2362)) ([9223470](https://github.com/googleapis/nodejs-spanner/commit/922347014ac3966ec4a48116b61ba4850edf0b50))
* Provide option to disable built in metrics ([#2380](https://github.com/googleapis/nodejs-spanner/issues/2380)) ([b378e2e](https://github.com/googleapis/nodejs-spanner/commit/b378e2ed6739acf76f3f3f27090311129dd83473))
* Race condition among transactions when running parallely ([#2369](https://github.com/googleapis/nodejs-spanner/issues/2369)) ([f8b6f63](https://github.com/googleapis/nodejs-spanner/commit/f8b6f6340f4f04e04213fdf0a9665d643f474eeb))

#### [8.2.1](https://github.com/googleapis/nodejs-spanner/compare/v8.2.0...v8.2.1) (2025-09-12)

##### Bug Fixes

* **deps:** Update dependency google-gax to v5.0.3 ([#2371](https://github.com/googleapis/nodejs-spanner/issues/2371)) ([8a175e2](https://github.com/googleapis/nodejs-spanner/commit/8a175e2e5cc8d0ed81faee7b24b59b5026758a59))
* Disable afe\_connectivity\_error\_count metric ([af72d70](https://github.com/googleapis/nodejs-spanner/commit/af72d707c8857d5596bd2b93830e52c8e152967f))

### Python

### Changes for [google-cloud-spanner](https://github.com/googleapis/python-spanner)

#### [3.58.0](https://github.com/googleapis/python-spanner/compare/v3.57.0...v3.58.0) (2025-09-10)

##### Features

* **spanner:** Support setting read lock mode ([#1404](https://github.com/googleapis/python-spanner/issues/1404)) ([ee24c6e](https://github.com/googleapis/python-spanner/commit/ee24c6ee2643bc74d52e9f0a924b80a830fa2697))

##### Dependencies

* Remove Python 3.7 and 3.8 as supported runtimes ([#1395](https://github.com/googleapis/python-spanner/issues/1395)) ([fc93792](https://github.com/googleapis/python-spanner/commit/fc9379232224f56d29d2e36559a756c05a5478ff))

---
## 2025-09-29

### Feature

You can now create BigQuery [non-incremental materialized views over Spanner data](https://cloud.google.com/bigquery/docs/materialized-views-create#spanner) to improve query performance by periodically caching results. This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2025-09-25

### Feature

The Cassandra interface for Spanner is now generally available. The Cassandra interface lets you take advantage of Spanner's fully managed, scalable, and highly available infrastructure using familiar Cassandra tools and syntax. For more information, see [Cassandra interface](https://cloud.google.com/spanner/docs/non-relational/cassandra-overview), [Migrate from Cassandra to Spanner](https://cloud.google.com/spanner/docs/non-relational/migrate-from-cassandra-to-spanner), and [Connect to Spanner using the Cassandra interface](https://cloud.google.com/spanner/docs/non-relational/connect-cassandra-adapter).

---
## 2025-09-23

### Feature

You can now use [read lease](https://cloud.google.com/spanner/docs/read-lease) regions to reduce latency for strong reads in multi-region or dual-region instances. Read leases use designated non-leader, read-write or read-only regions to serve strong reads locally, eliminating the network round trip to the leader region that is typically required. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

### Feature

You can now use the dedicated [Gemini CLI extension for Spanner](https://cloud.google.com/spanner/docs/pre-built-tools-with-mcp-toolbox) to execute SQL statements and query your Spanner instance using natural language controls.

---
## 2025-09-22

### Feature

You can now run federated queries against [PostgreSQL dialect databases in Spanner](https://cloud.google.com/spanner/docs/reference/postgresql/overview) using [BigQuery external datasets](https://cloud.google.com/bigquery/docs/spanner-external-datasets) using GoogleSQL; this includes [cross-region federated queries](https://cloud.google.com/bigquery/docs/spanner-federated-queries#cross_region_queries). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Python

### Changes for [google-cloud-spanner](https://github.com/googleapis/python-spanner)

#### [3.58.0](https://github.com/googleapis/python-spanner/compare/v3.57.0...v3.58.0) (2025-09-10)

##### Features

* **spanner:** Support setting read lock mode ([#1404](https://github.com/googleapis/python-spanner/issues/1404)) ([ee24c6e](https://github.com/googleapis/python-spanner/commit/ee24c6ee2643bc74d52e9f0a924b80a830fa2697))

##### Dependencies

* Remove Python 3.7 and 3.8 as supported runtimes ([#1395](https://github.com/googleapis/python-spanner/issues/1395)) ([fc93792](https://github.com/googleapis/python-spanner/commit/fc9379232224f56d29d2e36559a756c05a5478ff))

---
## 2025-09-17

### Feature

Spanner Graph support of schemaless schemas is [generally available](https://cloud.google.com/products#product-launch-stages) (GA). For more information, see [Manage schemaless data with Spanner Graph](https://cloud.google.com/spanner/docs/graph/manage-schemaless-data).

---
## 2025-09-15

### Feature

The Cassandra interface for Spanner is now generally available. The Cassandra interface lets you take advantage of Spanner's fully managed, scalable, and highly available infrastructure using familiar Cassandra tools and syntax. For more information, see [Cassandra interface](https://cloud.google.com/spanner/docs/non-relational/cassandra-overview), [Migrate from Cassandra to Spanner](https://cloud.google.com/spanner/docs/non-relational/migrate-from-cassandra-to-spanner), and [Connect to Spanner using the Cassandra interface](https://cloud.google.com/spanner/docs/non-relational/connect-cassandra-adapter).

---
## 2025-09-03

### Feature

You can import your own data into a Spanner database by using a CSV file, a MySQL dump file, or a PostgreSQL dump file.

Additionally, you can populate new databases in an existing Spanner instance from sample datasets that
help you explore Spanner capabilities such as its relational model, full-text search, vector search, or Spanner Graph.

For more information, see [Create and manage databases](https://cloud.google.com/spanner/docs/create-manage-databases).

---
## 2025-08-29

### Libraries

A monthly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [spanner/admin/database/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/spanner/admin/database/apiv1)

#### [1.84.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.83.0...spanner/v1.84.0) (2025-08-05)

##### Features

* **spanner/adapter:** Add last field in AdaptMessageResponse for internal optimization usage ([c574e28](https://github.com/googleapis/google-cloud-go/commit/c574e287f49cc1c3b069b35d95b98da2bc9b948f))
* **spanner/admin/database:** Proto changes for an internal api ([eeb4b1f](https://github.com/googleapis/google-cloud-go/commit/eeb4b1fe8eb83b73ec31b0bd46e3704bdc0212c3))
* **spanner:** A new field `snapshot_timestamp` is added to message `.google.spanner.v1.CommitResponse` ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))
* **spanner:** Add Google Cloud standard otel attributes ([#11652](https://github.com/googleapis/google-cloud-go/issues/11652)) ([f59fcff](https://github.com/googleapis/google-cloud-go/commit/f59fcfffdfcd01ef5b436b76fa83351e2b695920))

##### Bug Fixes

* **spanner:** Context cancel in traces in case of skipping trailers ([#12635](https://github.com/googleapis/google-cloud-go/issues/12635)) ([509dc90](https://github.com/googleapis/google-cloud-go/commit/509dc90cd13061f8302d20451af1d9f7e186641f))
* **spanner:** Enforce only one resource header ([#12618](https://github.com/googleapis/google-cloud-go/issues/12618)) ([4e04b7e](https://github.com/googleapis/google-cloud-go/commit/4e04b7efd68a979837f78d94ac1dbc930c2e5efb))
* **spanner:** Fix blind retry for ResourceExhausted ([#12523](https://github.com/googleapis/google-cloud-go/issues/12523)) ([f9b6e88](https://github.com/googleapis/google-cloud-go/commit/f9b6e88bd3fce735ea58f70e3a7634837886d393))
* **spanner:** Remove stream wrapper for direct path check ([#12622](https://github.com/googleapis/google-cloud-go/issues/12622)) ([88a36cd](https://github.com/googleapis/google-cloud-go/commit/88a36cdfb7f7d1d265f45ed8795b6c08915fe183))

##### Documentation

* **spanner:** A comment for enum value `OPTIMISTIC` in enum `ReadLockMode` is changed ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))
* **spanner:** A comment for enum value `PESSIMISTIC` in enum `ReadLockMode` is changed ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))
* **spanner:** A comment for enum value `READ_LOCK_MODE_UNSPECIFIED` in enum `ReadLockMode` is changed ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))
* **spanner:** A comment for field `commit_stats` in message `.google.spanner.v1.CommitResponse` is changed ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))
* **spanner:** A comment for field `exclude_txn_from_change_streams` in message `.google.spanner.v1.TransactionOptions` is changed ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))
* **spanner:** A comment for field `multiplexed_session_previous_transaction_id` in message `.google.spanner.v1.TransactionOptions` is changed ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))
* **spanner:** A comment for field `precommit_token` in message `.google.spanner.v1.CommitResponse` is changed ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))
* **spanner:** A comment for message `.google.spanner.v1.MultiplexedSessionPrecommitToken` is changed ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))
* **spanner:** A comment for message `.google.spanner.v1.TransactionOptions` is changed ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))

#### [1.84.1](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.84.0...spanner/v1.84.1) (2025-08-06)

##### Features

* **spanner:** Release 1.84.1 ([#12663](https://github.com/googleapis/google-cloud-go/issues/12663)) ([8b410ec](https://github.com/googleapis/google-cloud-go/commit/8b410ec689591a591aecb46831f2f50706cb973f))

##### Miscellaneous Chores

* **spanner:** Release 1.84.1 ([#12665](https://github.com/googleapis/google-cloud-go/issues/12665)) ([a1ce8c2](https://github.com/googleapis/google-cloud-go/commit/a1ce8c26651e7a0ba4f1b20aba4c0fefbab0b972))

**DO NOT USE**
This version is retracted due to https://github.com/googleapis/google-cloud-go/issues/12659, use version >=v1.84.1

### Java

### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)

#### [6.98.0](https://github.com/googleapis/java-spanner/compare/v6.97.1...v6.98.0) (2025-07-31)

##### Features

* Proto changes for an internal api ([675e90b](https://github.com/googleapis/java-spanner/commit/675e90b4582b4fc968118121e6c23ec98ee178e9))
* **spanner:** A new field `snapshot_timestamp` is added to message `.google.spanner.v1.CommitResponse` ([675e90b](https://github.com/googleapis/java-spanner/commit/675e90b4582b4fc968118121e6c23ec98ee178e9))
* Support Exemplar ([#3997](https://github.com/googleapis/java-spanner/issues/3997)) ([fcf0a01](https://github.com/googleapis/java-spanner/commit/fcf0a0182a33f229e865e4593635efaed34d6dac))
* Use multiplex sessions for RW and Partition Ops ([#3996](https://github.com/googleapis/java-spanner/issues/3996)) ([a882204](https://github.com/googleapis/java-spanner/commit/a882204e07a2084b228c14fb37ac53e4e33d0f59))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([675e90b](https://github.com/googleapis/java-spanner/commit/675e90b4582b4fc968118121e6c23ec98ee178e9))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#4004](https://github.com/googleapis/java-spanner/issues/4004)) ([986c0e0](https://github.com/googleapis/java-spanner/commit/986c0e07fddecd51cd310a9759ce1d41c1f5c657))

#### [6.98.1](https://github.com/googleapis/java-spanner/compare/v6.98.0...v6.98.1) (2025-08-11)

##### Bug Fixes

* Add missing span.end calls for AsyncTransactionManager ([#4012](https://github.com/googleapis/java-spanner/issues/4012)) ([1a4adb4](https://github.com/googleapis/java-spanner/commit/1a4adb4d70c3a3822fa6bda93d689f2dae1835fa))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 ([8156ef3](https://github.com/googleapis/java-spanner/commit/8156ef31d93932c14f9fdd13c8c5e5b7ce370ba5))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#4013](https://github.com/googleapis/java-spanner/issues/4013)) ([4e90c29](https://github.com/googleapis/java-spanner/commit/4e90c29ce3447d14411368e45a39c7b0965cb40a))

### Node.js

### Changes for [@google-cloud/spanner](https://github.com/googleapis/nodejs-spanner)

#### [8.1.0](https://github.com/googleapis/nodejs-spanner/compare/v8.0.0...v8.1.0) (2025-07-28)

##### Features

* Add Custom OpenTelemetry Exporter in for Service Metrics ([#2272](https://github.com/googleapis/nodejs-spanner/issues/2272)) ([610d1b9](https://github.com/googleapis/nodejs-spanner/commit/610d1b989ba186c0758791343deaa7f683c4bd26))
* Add methods from gax to cache proto root and process custom error details ([#2330](https://github.com/googleapis/nodejs-spanner/issues/2330)) ([1b3931a](https://github.com/googleapis/nodejs-spanner/commit/1b3931a799bdd052adc91703e59e1d0c83270065))
* Add metrics tracers ([#2319](https://github.com/googleapis/nodejs-spanner/issues/2319)) ([192bf2b](https://github.com/googleapis/nodejs-spanner/commit/192bf2bb603bca4ac481fcfd1f04974173adc6a1))
* Add support for AFE latency metrics ([#2348](https://github.com/googleapis/nodejs-spanner/issues/2348)) ([0666f05](https://github.com/googleapis/nodejs-spanner/commit/0666f05d589e2f229b44dffae8e9649220bccf8b))
* Add throughput\_mode to UpdateDatabaseDdlRequest to be used by Spanner Migration Tool. See https://github.com/GoogleCloudPlatform/spanner-migration-tool ([#2304](https://github.com/googleapis/nodejs-spanner/issues/2304)) ([a29af56](https://github.com/googleapis/nodejs-spanner/commit/a29af56ae3c31f07115cb938bcf3f0f77241b725))
* Operation, Attempt, and GFE metrics ([#2328](https://github.com/googleapis/nodejs-spanner/issues/2328)) ([646e6ea](https://github.com/googleapis/nodejs-spanner/commit/646e6ea6f1dc5fa1937e512ae9e81ae4d2637ed0))
* Proto changes for an internal api ([#2356](https://github.com/googleapis/nodejs-spanner/issues/2356)) ([380e770](https://github.com/googleapis/nodejs-spanner/commit/380e7705a23a692168db386ba5426c91bf1587b6))
* **spanner:** A new field `snapshot_timestamp` is added to message `.google.spanner.v1.CommitResponse` ([#2350](https://github.com/googleapis/nodejs-spanner/issues/2350)) ([0875cd8](https://github.com/googleapis/nodejs-spanner/commit/0875cd82e99fa6c95ab38807e09c5921303775f8))
* **spanner:** Add new change\_stream.proto ([#2315](https://github.com/googleapis/nodejs-spanner/issues/2315)) ([57d67be](https://github.com/googleapis/nodejs-spanner/commit/57d67be2e3b6d6ac2a8a903acf8613b27a049c3b))
* **spanner:** Add tpc support ([#2333](https://github.com/googleapis/nodejs-spanner/issues/2333)) ([a381cab](https://github.com/googleapis/nodejs-spanner/commit/a381cab92c31373a6a10edca0f8a8bdfc4415e4b))
* Track precommit token in r/w apis(multiplexed session) ([#2312](https://github.com/googleapis/nodejs-spanner/issues/2312)) ([3676bfa](https://github.com/googleapis/nodejs-spanner/commit/3676bfa60725c43f85a04ead87943be92e4a99f0))

##### Bug Fixes

* Docs-test ([#2297](https://github.com/googleapis/nodejs-spanner/issues/2297)) ([61c571c](https://github.com/googleapis/nodejs-spanner/commit/61c571c729c2a065df6ff166db784a6e6eaef74d))
* Ensure context propagation works in Node.js 22 with async/await ([#2326](https://github.com/googleapis/nodejs-spanner/issues/2326)) ([e8cdbed](https://github.com/googleapis/nodejs-spanner/commit/e8cdbedd55f049b8c7766e97388ed045fedd1b4e))
* Pass the Span correctly ([#2332](https://github.com/googleapis/nodejs-spanner/issues/2332)) ([edaee77](https://github.com/googleapis/nodejs-spanner/commit/edaee7791b2d814f749ed35119dd705924984a78))
* System test against emulator ([#2339](https://github.com/googleapis/nodejs-spanner/issues/2339)) ([2a6af4c](https://github.com/googleapis/nodejs-spanner/commit/2a6af4c36484f44929a2fac80d8f225dad5d702c))
* Unhandled exceptions from gax ([#2338](https://github.com/googleapis/nodejs-spanner/issues/2338)) ([6428bcd](https://github.com/googleapis/nodejs-spanner/commit/6428bcd2980852c1bdbc4c3d0ab210a139e5f193))

##### Performance Improvements

* Skip gRPC trailers for StreamingRead & ExecuteStreamingSql ([#2313](https://github.com/googleapis/nodejs-spanner/issues/2313)) ([8bd0781](https://github.com/googleapis/nodejs-spanner/commit/8bd0781e8b434a421f0e0f3395439a5a86c7847c))

### Python

### Changes for [google-cloud-spanner](https://github.com/googleapis/python-spanner)

#### [3.57.0](https://github.com/googleapis/python-spanner/compare/v3.56.0...v3.57.0) (2025-08-14)

##### Features

* Support configuring logger in dbapi kwargs ([#1400](https://github.com/googleapis/python-spanner/issues/1400)) ([ffa5c9e](https://github.com/googleapis/python-spanner/commit/ffa5c9e627583ab0635dcaa5512b6e034d811d86))

---
## 2025-08-25

### Feature

You can now terminate multiple active queries in your Spanner instance. Active queries are long-running queries that might affect the performance of your instance. Monitoring these queries can help you identify causes of instance latency and high CPU usage. Terminating queries might help free up resources and reduce the load on your instance.

For more information, see [Monitor active queries](https://cloud.google.com/spanner/docs/monitor-active-queries#terminate-query).

---
## 2025-08-14

### Feature

You can now use [cross region federated queries](https://cloud.google.com/bigquery/docs/spanner-federated-queries#cross_region_queries) to query Spanner tables from regions other than the source BigQuery region. These cross region queries incur additional [Spanner network egress charges](https://cloud.google.com/spanner/pricing#network). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

---
## 2025-08-13

### Feature

Spanner offers a predefined library of over [80 MySQL functions](https://cloud.google.com/spanner/docs/reference/mysql/user_defined_functions_all) that you can install in a database. These functions let you perform operations that are common in the MySQL environments directly with Spanner. They can help reduce the changes required when migrating workloads from MySQL to Spanner.

These functions are packaged as user-defined functions that can be installed from an open-source DDL script hosted on GitHub. For more information, see [Install MySQL functions in Spanner](https://cloud.google.com/spanner/docs/install-mysql-functions).

---
## 2025-08-05

### Feature

Columnar engine for Spanner is now in Preview. Columnar engine is a storage technique used with analytics queries to speed up scans. Spanner columnar engine accelerates analytical query performance on live operational data by up to 200 times without affecting transaction workloads. This eliminates the need for ETL into separate data warehouses while maintaining strong consistency. For more information, see the [Columnar engine for Spanner overview](https://cloud.google.com/spanner/docs/columnar-engine).

---
## 2025-08-01

### Feature

When you create the free trial instance using the Google Cloud console, Spanner creates and preloads it with a sample database for an ecommerce store. You can use the free trial instance to explore the dataset and learn about Spanner capabilities with pre-loaded queries.

For more information, see [Spanner free trial instances](https://cloud.google.com/spanner/docs/free-trial-instance).

---
## 2025-07-31

### Feature

You can use [continuous queries](https://cloud.google.com/bigquery/docs/continuous-queries-introduction) to [export BigQuery data into Spanner in real time](https://cloud.google.com/bigquery/docs/export-to-spanner). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

### Libraries

A monthly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)

#### [6.96.1](https://github.com/googleapis/java-spanner/compare/v6.96.0...v6.96.1) (2025-06-30)

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.59.0 ([2836042](https://github.com/googleapis/java-spanner/commit/2836042217fe29bb967fe892bd6b492391ded95c))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.50.0 ([#3925](https://github.com/googleapis/java-spanner/issues/3925)) ([1372bbd](https://github.com/googleapis/java-spanner/commit/1372bbd82b7828629cbc407b78878469bc477977))

#### [6.97.0](https://github.com/googleapis/java-spanner/compare/v6.96.1...v6.97.0) (2025-07-10)

##### Features

* Next release from main branch is 6.97.0 ([#3984](https://github.com/googleapis/java-spanner/issues/3984)) ([5651f61](https://github.com/googleapis/java-spanner/commit/5651f6160e1e655f118aa2e7f0203a47cd6914c0))

##### Bug Fixes

* Drop max message size ([#3987](https://github.com/googleapis/java-spanner/issues/3987)) ([3eee899](https://github.com/googleapis/java-spanner/commit/3eee89965547dfa49b4282b470f625d43c92f4fd))
* Return non-empty metadata for DataBoost queries ([#3936](https://github.com/googleapis/java-spanner/issues/3936)) ([79c0684](https://github.com/googleapis/java-spanner/commit/79c06848c0ac4eff8410dd3bd63db8675c202d94))

#### [6.97.1](https://github.com/googleapis/java-spanner/compare/v6.97.0...v6.97.1) (2025-07-15)

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#3992](https://github.com/googleapis/java-spanner/issues/3992)) ([69ffd72](https://github.com/googleapis/java-spanner/commit/69ffd7282220b8b12c6b9b64d8856ff88068ffa2))
* Update googleapis/sdk-platform-java action to v2.60.1 ([#3926](https://github.com/googleapis/java-spanner/issues/3926)) ([7001b7f](https://github.com/googleapis/java-spanner/commit/7001b7faaff581e26ec81c4db2c99a1e8726d5eb))

### Python

### Changes for [google-cloud-spanner](https://github.com/googleapis/python-spanner)

#### [3.56.0](https://github.com/googleapis/python-spanner/compare/v3.55.0...v3.56.0) (2025-07-24)

##### Features

* Add support for multiplexed sessions - read/write ([#1389](https://github.com/googleapis/python-spanner/issues/1389)) ([ce3f230](https://github.com/googleapis/python-spanner/commit/ce3f2305cd5589e904daa18142fbfeb180f3656a))
* Add support for multiplexed sessions ([#1383](https://github.com/googleapis/python-spanner/issues/1383)) ([21f5028](https://github.com/googleapis/python-spanner/commit/21f5028c3fdf8b8632c1564efbd973b96711d03b))
* Default enable multiplex session for all operations unless explicitly set to false ([#1394](https://github.com/googleapis/python-spanner/issues/1394)) ([651ca9c](https://github.com/googleapis/python-spanner/commit/651ca9cd65c713ac59a7d8f55b52b9df5b4b6923))
* **spanner:** Add new change\_stream.proto ([#1382](https://github.com/googleapis/python-spanner/issues/1382)) ([ca6255e](https://github.com/googleapis/python-spanner/commit/ca6255e075944d863ab4be31a681fc7c27817e34))

##### Performance Improvements

* Skip gRPC trailers for StreamingRead & ExecuteStreamingSql ([#1385](https://github.com/googleapis/python-spanner/issues/1385)) ([cb25de4](https://github.com/googleapis/python-spanner/commit/cb25de40b86baf83d0fb1b8ca015f798671319ee))

---
## 2025-07-14

### Feature

[Spanner Data Boost](https://cloud.google.com/spanner/docs/databoost/databoost-overview) supports data stored on hard disk drives (HDD). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

---
## 2025-07-01

### Changed

The performance of the `ANY` and the [`ANY SHORTEST`](https://cloud.google.com/spanner/docs/graph/work-with-paths#any-shortest) algorithms have been improved. These algorithms are used to find Spanner Graph paths. For more information, see [`ANY` and `ANY SHORTEST` paths](https://cloud.google.com/spanner/docs/graph/queries-overview#any-and-any-shortest-paths).

---
## 2025-06-30

### Feature

Spanner supports the following new client-side metrics to the Spanner API frontend (AFE) and Google frontend (GFE) for Java and Go applications:

* AFE connectivity error count
* AFE latencies
* GFE connectivity error count
* GFE latencies

These metrics can be used with server-side metrics to enable faster troubleshooting of performance and latency issues. For more information, see
[Client-side metrics descriptions](https://cloud.google.com/spanner/docs/client-side-metrics-descriptions).

### Feature

To troubleshoot or understand your Spanner queries better, you can download and save your [query execution plan](https://cloud.google.com/spanner/docs/query-execution-plans) as a JSON file. You can now use the content of this file to see a visualization of the query execution plan in Spanner Studio. For more information, see [Take a tour of the query plan visualizer](https://cloud.google.com/spanner/docs/tune-query-with-visualizer#visual-plan-tour).

### Libraries

A monthly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [spanner/admin/database/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/spanner/admin/database/apiv1)

#### [1.83.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.82.0...spanner/v1.83.0) (2025-06-27)

##### Features

* **spanner/spansql:** Add support for TOKENIZE\_JSON. ([#12338](https://github.com/googleapis/google-cloud-go/issues/12338)) ([72225a5](https://github.com/googleapis/google-cloud-go/commit/72225a52c0f6bc6eac6d4e450dad0b566e79553f))
* **spanner/spansql:** Support EXISTS in query parsing ([#12439](https://github.com/googleapis/google-cloud-go/issues/12439)) ([f5cb67b](https://github.com/googleapis/google-cloud-go/commit/f5cb67b104e4d99196064fb4474e0644e90c9a00))
* **spanner:** Add new change\_stream.proto ([40b60a4](https://github.com/googleapis/google-cloud-go/commit/40b60a4b268040ca3debd71ebcbcd126b5d58eaa))
* **spanner:** Add option for how to call BeginTransaction ([#12436](https://github.com/googleapis/google-cloud-go/issues/12436)) ([2cba13b](https://github.com/googleapis/google-cloud-go/commit/2cba13b8fef80b6cb5980e3b5b2bfc6dc796a03e))
* **spanner:** Wrap proto mutation ([#12497](https://github.com/googleapis/google-cloud-go/issues/12497)) ([e655889](https://github.com/googleapis/google-cloud-go/commit/e655889e2fd6a55f901d1d8b146e7aa5efdca705))

##### Bug Fixes

* **spanner:** Pointer type custom struct decoder ([#12496](https://github.com/googleapis/google-cloud-go/issues/12496)) ([ac3cafb](https://github.com/googleapis/google-cloud-go/commit/ac3cafbac435a3ac98fd4693bac84a3f4a260c5b))

### Java

### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)

#### [6.95.0](https://github.com/googleapis/java-spanner/compare/v6.94.0...v6.95.0) (2025-06-05)

##### Features

* Enable ALTS hard bound token in DirectPath ([#3904](https://github.com/googleapis/java-spanner/issues/3904)) ([2b0f2ff](https://github.com/googleapis/java-spanner/commit/2b0f2ff214f4b68dd5957bc4280edb713b77a763))
* Enable grpc and afe metrics ([#3896](https://github.com/googleapis/java-spanner/issues/3896)) ([706f794](https://github.com/googleapis/java-spanner/commit/706f794f044c2cb1112cfdae6f379e5f2bc3f26f))
* Last statement sample ([#3830](https://github.com/googleapis/java-spanner/issues/3830)) ([2f62816](https://github.com/googleapis/java-spanner/commit/2f62816b0af9aced1b73e25525f60f8e3e923454))
* **spanner:** Add new change\_stream.proto ([f385698](https://github.com/googleapis/java-spanner/commit/f38569865de7465ae9a37b844a9dd983571d3688))

##### Bug Fixes

* Directpath\_enabled attribute ([#3897](https://github.com/googleapis/java-spanner/issues/3897)) ([53bc510](https://github.com/googleapis/java-spanner/commit/53bc510145921d00bc3df04aa4cf407179ed8d8e))

##### Dependencies

* Update dependency io.opentelemetry:opentelemetry-bom to v1.50.0 ([#3887](https://github.com/googleapis/java-spanner/issues/3887)) ([94b879c](https://github.com/googleapis/java-spanner/commit/94b879c8c1848fa0b14dbe8cda8390cfe9e8fce6))

#### [6.95.1](https://github.com/googleapis/java-spanner/compare/v6.95.0...v6.95.1) (2025-06-06)

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#3909](https://github.com/googleapis/java-spanner/issues/3909)) ([3de8502](https://github.com/googleapis/java-spanner/commit/3de8502b98ebb90526fc2339e279f9b710816b3b))
* Update googleapis/sdk-platform-java action to v2.59.0 ([#3910](https://github.com/googleapis/java-spanner/issues/3910)) ([aed8bd6](https://github.com/googleapis/java-spanner/commit/aed8bd6d5a0b1e0dfab345e0de68f285e8b8aedb))

#### [6.96.0](https://github.com/googleapis/java-spanner/compare/v6.95.1...v6.96.0) (2025-06-27)

##### Features

* Allow JDBC to configure directpath for connection ([#3929](https://github.com/googleapis/java-spanner/issues/3929)) ([d754f1f](https://github.com/googleapis/java-spanner/commit/d754f1f99294d86ec881583f217fa09f291a3d7a))
* Support getOrNull and getOrDefault in Struct ([#3914](https://github.com/googleapis/java-spanner/issues/3914)) ([1dc5a3e](https://github.com/googleapis/java-spanner/commit/1dc5a3ec0ca9ea530e8691df5c2734c0a1ece559))
* Use multiplexed sessions for read-only transactions ([#3917](https://github.com/googleapis/java-spanner/issues/3917)) ([37fdc27](https://github.com/googleapis/java-spanner/commit/37fdc27aab4e71ac141c2a2c979f864e97395a97))

##### Bug Fixes

* Allow zero durations to be set for connections ([#3916](https://github.com/googleapis/java-spanner/issues/3916)) ([43ea4fa](https://github.com/googleapis/java-spanner/commit/43ea4fa68eac00801beb8e58c1eb09e9f32e5ce5))

##### Documentation

* Add snippet for Repeatable Read configuration at client and transaction ([#3908](https://github.com/googleapis/java-spanner/issues/3908)) ([ff3d212](https://github.com/googleapis/java-spanner/commit/ff3d212c98276c4084f44619916d0444c9652803))
* Update SpannerSample.java to align with best practices ([#3625](https://github.com/googleapis/java-spanner/issues/3625)) ([7bfc62d](https://github.com/googleapis/java-spanner/commit/7bfc62d3d9e57242e0dfddea090208f8c65f0f8e))

---
## 2025-06-24

### Feature

You can directly connect and interact with your Spanner database using the Spanner CLI, an interactive shell for Spanner that is built into the Google Cloud CLI. You can use the Spanner CLI to start an interactive session and automate SQL executions from the shell or an input file. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Spanner CLI quickstart](https://cloud.google.com/spanner/docs/spanner-cli).

---
## 2025-06-20

### Feature

A new free trial creation work flow makes it easier to start your Spanner free trial. With a free trial instance, you can learn and explore Spanner for 90 days at no cost. You can create relational (GoogleSQL and PostgreSQL) databases and deploy NoSQL models (Spanner Graph, Vector search, and Full-text search) in a single, fully managed database. For more information, see [Spanner free trial instances overview](https://cloud.google.com/spanner/docs/free-trial-instance).

---
## 2025-06-11

### Feature

Column operations statistics are [generally available](https://cloud.google.com/products#product-launch-stages). They help you get insights into and monitor the usage of columns in your database. For more information, see [Column operations statistics](https://cloud.google.com/spanner/docs/introspection/column-operations-statistics).

---
## 2025-06-02

### Feature

BigQuery now supports using [Spanner external datasets](https://cloud.google.com/bigquery/docs/spanner-external-datasets) with [authorized views](https://cloud.google.com/bigquery/docs/authorized-views), [authorized routines](https://cloud.google.com/bigquery/docs/authorized-routines), and [Cloud resource connections](https://cloud.google.com/bigquery/docs/create-cloud-resource-connection). This feature is [generally available](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages) (GA).

### Libraries

A monthly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [spanner/admin/database/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/spanner/admin/database/apiv1)

#### [1.81.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.80.0...spanner/v1.81.0) (2025-05-09)

##### Features

* **spanner/spansql:** Add support for DROP SEARCH INDEX and ALTER SEARCH INDEX ([#11961](https://github.com/googleapis/google-cloud-go/issues/11961)) ([952cd7f](https://github.com/googleapis/google-cloud-go/commit/952cd7fd419af9eb74f5d30a111ae936094b0645))

##### Bug Fixes

* **spanner:** Row mismatch in SelectAll using custom type ([#12222](https://github.com/googleapis/google-cloud-go/issues/12222)) ([ce6a23a](https://github.com/googleapis/google-cloud-go/commit/ce6a23a45fe66cc12e1b5014d2d45f1968ddc067))

#### [1.81.1](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.81.0...spanner/v1.81.1) (2025-05-15)

##### Features

* **spanner:** Add support of AFE and GRPC metrics in client-side metrics ([#12067](https://github.com/googleapis/google-cloud-go/issues/12067)) ([7b77038](https://github.com/googleapis/google-cloud-go/commit/7b77038eb4afe31b1a0d42f7c35aeabce0f48810))

#### [1.82.0](https://github.com/googleapis/google-cloud-go/compare/spanner/v1.81.1...spanner/v1.82.0) (2025-05-20)

##### Features

* **spanner/admin/database:** Add throughput\_mode to UpdateDatabaseDdlRequest to be used by Spanner Migration Tool. See https ([#12287](https://github.com/googleapis/google-cloud-go/issues/12287)) ([2a9d8ee](https://github.com/googleapis/google-cloud-go/commit/2a9d8eec71a7e6803eb534287c8d2f64903dcddd))

### Java

### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)

#### [6.92.0](https://github.com/googleapis/java-spanner/compare/v6.91.1...v6.92.0) (2025-04-29)

* **spanner:** Do not export metrics during shutdown if prev export was less than 30 seconds ago ([#12266](https://github.com/googleapis/google-cloud-go/issues/12266)) ([8ad7511](https://github.com/googleapis/google-cloud-go/commit/8ad75111433be5424f9fff8aafd73463cb467734))
* **spanner:** Fix invalid trace in case of skipping trailers ([#12235](https://github.com/googleapis/google-cloud-go/issues/12235)) ([e54c439](https://github.com/googleapis/google-cloud-go/commit/e54c4398831b5a1c2998f9e8d159f0118aee1d0b))
  ### Changes for [google-cloud-spanner](https://github.com/googleapis/java-spanner)
  #### [6.94.0](https://github.com/googleapis/java-spanner/compare/v6.93.0...v6.94.0) (2025-05-21)

##### Features

* [Internal] client-side metrics for afe latency and connectivity error ([#3819](https://github.com/googleapis/java-spanner/issues/3819)) ([a8dba0a](https://github.com/googleapis/java-spanner/commit/a8dba0a83939fdbbc324f0a7aa6c44180462fa3a))
* Support begin with AbortedException for manager interface ([#3835](https://github.com/googleapis/java-spanner/issues/3835)) ([5783116](https://github.com/googleapis/java-spanner/commit/578311693bed836c8916f4b4ffa0782a468c1af3))
* Add throughput\_mode to UpdateDatabaseDdlRequest to be used by Spanner Migration Tool. See https://github.com/GoogleCloudPlatform/spanner-migration-tool ([3070f1d](https://github.com/googleapis/java-spanner/commit/3070f1db97788c2a55c553ab8a4de3419d1ccf5c))
* Enable AFE and gRPC metrics for DP ([#3852](https://github.com/googleapis/java-spanner/issues/3852)) ([203baae](https://github.com/googleapis/java-spanner/commit/203baae3996378435095cb90e3b2c7ee71a643cd))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.56.2 ([11bfd90](https://github.com/googleapis/java-spanner/commit/11bfd90daa244dbd31a76bc5a1d2e694e43fa292))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.58.0 ([3070f1d](https://github.com/googleapis/java-spanner/commit/3070f1db97788c2a55c553ab8a4de3419d1ccf5c))
* Remove trailing semicolons in DDL ([#3879](https://github.com/googleapis/java-spanner/issues/3879)) ([ca3a67d](https://github.com/googleapis/java-spanner/commit/ca3a67db715f398943382df1f8a9979905811ff8))
* Change server timing duration attribute to float as per w3c ([#3851](https://github.com/googleapis/java-spanner/issues/3851)) ([da8dd8d](https://github.com/googleapis/java-spanner/commit/da8dd8da3171a073d7b450d4413936351a4c1060))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.57.0 ([23b985c](https://github.com/googleapis/java-spanner/commit/23b985c9a04837b0b38f2cfc5d96469e1d664d67))
* Non-ASCII Unicode characters in code ([#3844](https://github.com/googleapis/java-spanner/issues/3844)) ([85a0820](https://github.com/googleapis/java-spanner/commit/85a0820505889ae6482a9e4f845cd53430dd6b44))
* Only close and return sessions once ([#3846](https://github.com/googleapis/java-spanner/issues/3846)) ([32b2373](https://github.com/googleapis/java-spanner/commit/32b2373d62cac3047d9686c56af278c706d7c488))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#3836](https://github.com/googleapis/java-spanner/issues/3836)) ([2ee7f97](https://github.com/googleapis/java-spanner/commit/2ee7f971f3374b01d22e5a7f8f2483cf60c3363d))

#### [6.93.0](https://github.com/googleapis/java-spanner/compare/v6.92.0...v6.93.0) (2025-05-09)

* Update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#3869](https://github.com/googleapis/java-spanner/issues/3869)) ([afa17f7](https://github.com/googleapis/java-spanner/commit/afa17f73beab80639467916bc73b5c96305093aa))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#3880](https://github.com/googleapis/java-spanner/issues/3880)) ([f3b00b6](https://github.com/googleapis/java-spanner/commit/f3b00b663aa897fda1bc21222d29726e6be630cb))
* Update dependency com.google.cloud.opentelemetry:exporter-metrics to v0.34.0 ([#3861](https://github.com/googleapis/java-spanner/issues/3861)) ([676b14f](https://github.com/googleapis/java-spanner/commit/676b14f916dea783b40ddec4061bd7af157b5d98))
* Update dependency commons-io:commons-io to v2.19.0 ([#3863](https://github.com/googleapis/java-spanner/issues/3863)) ([80a6af8](https://github.com/googleapis/java-spanner/commit/80a6af836ca29ec196a2f509831e1d36c557168f))
* Update dependency io.opentelemetry:opentelemetry-bom to v1.50.0 ([#3865](https://github.com/googleapis/java-spanner/issues/3865)) ([ae63050](https://github.com/googleapis/java-spanner/commit/ae6305089b394be0c1eaf8ff7e188711288d87ad))
* Update googleapis/sdk-platform-java action to v2.58.0 ([#3870](https://github.com/googleapis/java-spanner/issues/3870)) ([d1e45fa](https://github.com/googleapis/java-spanner/commit/d1e45fa88bb005529bcfb2a6ff2df44065be0fd2))
* Update opentelemetry.version to v1.50.0 ([#3866](https://github.com/googleapis/java-spanner/issues/3866)) ([f7e09b8](https://github.com/googleapis/java-spanner/commit/f7e09b8148c0e51503255694bd3347c637724b34))

##### Documentation

* Add samples for unnamed (positional) parameters ([#3849](https://github.com/googleapis/java-spanner/issues/3849)) ([035cadd](https://github.com/googleapis/java-spanner/commit/035cadd5bb77a8f9f6fb25ac8c8e5a3e186d9a22))

### Node.js

### Changes for [@google-cloud/spanner](https://github.com/googleapis/nodejs-spanner)

#### [8.0.0](https://github.com/googleapis/nodejs-spanner/compare/v7.21.0...v8.0.0) (2025-05-12)

##### ⚠ BREAKING CHANGES

* remove the arrify package ([#2292](https://github.com/googleapis/nodejs-spanner/issues/2292))
* migrate to Node 18 ([#2271](https://github.com/googleapis/nodejs-spanner/issues/2271))

##### Features

* Add promise based signatures for createQueryPartitions ([#2284](https://github.com/googleapis/nodejs-spanner/issues/2284)) ([255d8a6](https://github.com/googleapis/nodejs-spanner/commit/255d8a6a5749b6a05cd87dd7444cab7dd75d3e42))
* Add promise based signatures on createReadPartitions ([#2300](https://github.com/googleapis/nodejs-spanner/issues/2300)) ([7b8a1f7](https://github.com/googleapis/nodejs-spanner/commit/7b8a1f70f0de3aa5886a2cde9325c9a36222a311))
* Support promise based signatures for execute method ([#2301](https://github.com/googleapis/nodejs-spanner/issues/2301)) ([bb857e1](https://github.com/googleapis/nodejs-spanner/commit/bb857e18459f717d67b9b3d144c2b022178363cb))

##### Bug Fixes

* **deps:** Update dependency @google-cloud/kms to v5 ([#2289](https://github.com/googleapis/nodejs-spanner/issues/2289)) ([1ccb505](https://github.com/googleapis/nodejs-spanner/commit/1ccb505935e70b6f576f06e566325146ee68f3ff))
* **deps:** Update dependency @google-cloud/precise-date to v5 ([#2290](https://github.com/googleapis/nodejs-spanner/issues/2290)) ([44f7575](https://github.com/googleapis/nodejs-spanner/commit/44f7575efd3751d0595beef2ec4eb9f39bc426d7))
* **deps:** Update dependency big.js to v7 ([#2286](https://github.com/googleapis/nodejs-spanner/issues/2286)) ([0911297](https://github.com/googleapis/nodejs-spanner/commit/0911297cc33aec93c09ef2be42413f20c75fc2bf))

##### Miscellaneous Chores

* Migrate to Node 18 ([#2271](https://github.com/googleapis/nodejs-spanner/issues/2271)) ([cab3f22](https://github.com/googleapis/nodejs-spanner/commit/cab3f229ccb2189bd5af0c25a3006b553f8a5453))
* Remove the arrify package ([#2292](https://github.com/googleapis/nodejs-spanner/issues/2292)) ([e8f5ca1](https://github.com/googleapis/nodejs-spanner/commit/e8f5ca15125d570949769e6e66f0d911cb21f58d))

### Python

### Changes for [google-cloud-spanner](https://github.com/googleapis/python-spanner)

#### [3.54.0](https://github.com/googleapis/python-spanner/compare/v3.53.0...v3.54.0) (2025-04-28)

##### Features

* Add interval type support ([#1340](https://github.com/googleapis/python-spanner/issues/1340)) ([6ca9b43](https://github.com/googleapis/python-spanner/commit/6ca9b43c3038eca1317c7c9b7e3543b5f1bc68ad))
* Add sample for pre-split feature ([#1333](https://github.com/googleapis/python-spanner/issues/1333)) ([ca76108](https://github.com/googleapis/python-spanner/commit/ca76108809174e4f3eea38d7ac2463d9b4c73304))
* Add SQL statement for begin transaction isolation level ([#1331](https://github.com/googleapis/python-spanner/issues/1331)) ([3ac0f91](https://github.com/googleapis/python-spanner/commit/3ac0f9131b38e5cfb2b574d3d73b03736b871712))
* Support transaction isolation level in dbapi ([#1327](https://github.com/googleapis/python-spanner/issues/1327)) ([03400c4](https://github.com/googleapis/python-spanner/commit/03400c40f1c1cc73e51733f2a28910a8dd78e7d9))

##### Bug Fixes

* Improve client-side regex statement parser ([#1328](https://github.com/googleapis/python-spanner/issues/1328)) ([b3c259d](https://github.com/googleapis/python-spanner/commit/b3c259deec817812fd8e4940faacf4a927d0d69c))

#### [3.55.0](https://github.com/googleapis/python-spanner/compare/v3.54.0...v3.55.0) (2025-05-28)

##### Features

* Add a `last` field in the `PartialResultSet` ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* Add support for multiplexed sessions ([#1381](https://github.com/googleapis/python-spanner/issues/1381)) ([97d7268](https://github.com/googleapis/python-spanner/commit/97d7268ac12a57d9d116ee3d9475580e1e7e07ae))
* Add throughput\_mode to UpdateDatabaseDdlRequest to be used by Spanner Migration Tool. See https://github.com/GoogleCloudPlatform/spanner-migration-tool ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* Support fine-grained permissions database roles in connect ([#1338](https://github.com/googleapis/python-spanner/issues/1338)) ([064d9dc](https://github.com/googleapis/python-spanner/commit/064d9dc3441a617cbc80af6e16493bc42c89b3c9))

##### Bug Fixes

* E2E tracing metadata append issue ([#1357](https://github.com/googleapis/python-spanner/issues/1357)) ([3943885](https://github.com/googleapis/python-spanner/commit/394388595a312f60b423dfbfd7aaf2724cc4454f))
* Pass through kwargs in dbapi connect ([#1368](https://github.com/googleapis/python-spanner/issues/1368)) ([aae8d61](https://github.com/googleapis/python-spanner/commit/aae8d6161580c88354d813fe75a297c318f1c2c7))
* Remove setup.cfg configuration for creating universal wheels ([#1324](https://github.com/googleapis/python-spanner/issues/1324)) ([e064474](https://github.com/googleapis/python-spanner/commit/e0644744d7f3fcea42b461996fc0ee22d4218599))

##### Documentation

* A comment for field `chunked_value` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `precommit_token` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `precommit_token` in message `.google.spanner.v1.ResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `query_plan` in message `.google.spanner.v1.ResultSetStats` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `row_count_lower_bound` in message `.google.spanner.v1.ResultSetStats` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `row_type` in message `.google.spanner.v1.ResultSetMetadata` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `rows` in message `.google.spanner.v1.ResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `stats` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `stats` in message `.google.spanner.v1.ResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for field `values` in message `.google.spanner.v1.PartialResultSet` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for message `ResultSetMetadata` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* A comment for message `ResultSetStats` is changed ([d532d57](https://github.com/googleapis/python-spanner/commit/d532d57fd5908ecd7bc9dfff73695715cc4b1ebe))
* Fix markdown formatting in transactions page ([#1377](https://github.com/googleapis/python-spanner/issues/1377)) ([de322f8](https://github.com/googleapis/python-spanner/commit/de322f89642a3c13b6b1d4b9b1a2cdf4c8f550fb))

---
## 2025-05-27

### Feature

Spanner now supports [cross regional federated queries](https://cloud.google.com/bigquery/docs/spanner-federated-queries#cross_region_queries) from BigQuery, which allows BigQuery users to query Spanner tables from regions other than their BigQuery region. Users will not incur any Spanner [network egress charges](https://cloud.google.com/spanner/pricing#network) during the preview period. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
