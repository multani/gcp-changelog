# Cloud Storage

## 2025-12-16

### Feature

You can now use Anywhere Cache to serve data for object read requests issued
by BigQuery to accelerate data reads for your applications. For more
information, see [Using Anywhere Cache to accelerate reads for BigQuery](https://docs.cloud.google.com/storage/docs/anywhere-cache#integrations).

### Feature

You can now generate [Storage Insights
datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) for activity data to receive insights
about object mutations, errors, and activity trends across projects, buckets,
and regions. For more information, see [Dataset schema for activity data
tables](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#activity-data-schema).

---
## 2025-12-15

### Libraries

### Python

#### [3.7.0](https://github.com/googleapis/python-storage/compare/v3.6.0...v3.7.0) (2025-12-09)

##### Features

* Auto enable mTLS when supported certificates are detected ([#1637](https://github.com/googleapis/python-storage/issues/1637)) ([4e91c54](https://github.com/googleapis/python-storage/commit/4e91c541363f0e583bf9dd1b81a95ff2cb618bac))
* Send entire object checksum in the final api call of resumable upload ([#1654](https://github.com/googleapis/python-storage/issues/1654)) ([ddce7e5](https://github.com/googleapis/python-storage/commit/ddce7e53a13e6c0487221bb14e88161da7ed9e08))
* Support urllib3 >= 2.6.0 ([#1658](https://github.com/googleapis/python-storage/issues/1658)) ([57405e9](https://github.com/googleapis/python-storage/commit/57405e956a7ca579b20582bf6435cec42743c478))

##### Bug Fixes

* **bucket:** Move blob fails when the new blob name contains characters that need to be url encoded ([#1605](https://github.com/googleapis/python-storage/issues/1605)) ([ec470a2](https://github.com/googleapis/python-storage/commit/ec470a270e189e137c7229cc359367d5a897cdb9))

---
## 2025-11-14

### Feature

You can now use the Google Cloud console to [relocate
buckets](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview). Using bucket relocation, you
can move an existing bucket from one location to another without changing the
bucket's name or requiring manual transfer of data within the bucket.

---
## 2025-11-11

### Feature

You can now enable [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for buckets with
[hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled.

---
## 2025-10-27

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.59.0](https://github.com/googleapis/java-storage/compare/v2.58.1...v2.59.0) (2025-10-21)

##### Features

* Add per-message checksum validation for gRPC ReadObject operations ([#3336](https://github.com/googleapis/java-storage/issues/3336)) ([6eef1b0](https://github.com/googleapis/java-storage/commit/6eef1b0f587b9f32041ac4bcef1a16b1b0bc4bb3))

##### Bug Fixes

* Add case insensitive check for X-Goog-Content-SHA256 in SignatureInfo ([#3337](https://github.com/googleapis/java-storage/issues/3337)) ([54bc2c1](https://github.com/googleapis/java-storage/commit/54bc2c12f2d0e8c164e4ddcaa1a61d2de3911131))
* Migrate away from GoogleCredentials.fromStream() usages ([#3339](https://github.com/googleapis/java-storage/issues/3339)) ([7e42c2f](https://github.com/googleapis/java-storage/commit/7e42c2fbca53ca6b1266f784e58cee00cfed7d62))
* Update BlobReadSession channels to not implicitly close once EOF is observed ([#3344](https://github.com/googleapis/java-storage/issues/3344)) ([9f0a93e](https://github.com/googleapis/java-storage/commit/9f0a93eb4c6bb8aab13915ca1cb40ba9e229a2f9))
* Update grpc single-shot uploads to attach the callers stracktrace as suppressed exception if an error happens in the background ([#3330](https://github.com/googleapis/java-storage/issues/3330)) ([64e2b2e](https://github.com/googleapis/java-storage/commit/64e2b2ef839e69da0605b9e53989c1f5a2b09e66))
* Update retry logic for grpc start resumable upload to properly handle client side deadline\_exceeded ([#3354](https://github.com/googleapis/java-storage/issues/3354)) ([6eb3331](https://github.com/googleapis/java-storage/commit/6eb33311d8dd7344e30ddcb92334fd52c7c63b4d))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#3351](https://github.com/googleapis/java-storage/issues/3351)) ([e64565a](https://github.com/googleapis/java-storage/commit/e64565ab674f586ea4850408a3f30544997f4b1b))

---
## 2025-10-23

### Feature

You can now use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) to create and manage [retention configurations](https://docs.cloud.google.com/storage/docs/metadata#retention-config) for objects in bulk using the `PutMetadata` transformation.

---
## 2025-10-13

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.17.2](https://github.com/googleapis/nodejs-storage/compare/v7.17.1...v7.17.2) (2025-10-06)

##### Bug Fixes

* Common Service: should retry a request failed ([#2652](https://github.com/googleapis/nodejs-storage/issues/2652)) ([b38b5d2](https://github.com/googleapis/nodejs-storage/commit/b38b5d221f2cb72658c1eb4a726315ab395a542c))
* Implement path containment to prevent traversal attacks ([#2654](https://github.com/googleapis/nodejs-storage/issues/2654)) ([08d7abf](https://github.com/googleapis/nodejs-storage/commit/08d7abf32dd365b24ce34c66174be06c30bfce8f))

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.58.1](https://github.com/googleapis/java-storage/compare/v2.58.0...v2.58.1) (2025-10-06)

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.62.3 ([ba84793](https://github.com/googleapis/java-storage/commit/ba847937e553f6a47aa459f634f63ed42310762d))
* Update BlobReadSession ScatteringByteChannel projection to use less CPU ([#3324](https://github.com/googleapis/java-storage/issues/3324)) ([678fecc](https://github.com/googleapis/java-storage/commit/678feccc972e557380e9ba5fcd52be099440197d))
* Update DefaultRetryContext to trap and forward RejectedExceptionException to onFailure ([#3327](https://github.com/googleapis/java-storage/issues/3327)) ([1be31bd](https://github.com/googleapis/java-storage/commit/1be31bdfbc0283733e86b049d3be1911db50fb96))
* Update PCU request building logic to properly clear crc32c and md5 ([#3323](https://github.com/googleapis/java-storage/issues/3323)) ([4da9f31](https://github.com/googleapis/java-storage/commit/4da9f3108d27f5c2ed3cc39eec161651f421e4db))

##### Dependencies

* Update dependency com.google.apis:google-api-services-storage to v1-rev20250925-2.0.0 ([#3313](https://github.com/googleapis/java-storage/issues/3313)) ([ab310eb](https://github.com/googleapis/java-storage/commit/ab310eb5af51ed332329abd6c3441d18f9965571))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 ([#3325](https://github.com/googleapis/java-storage/issues/3325)) ([4d3e3be](https://github.com/googleapis/java-storage/commit/4d3e3be27811ad92becc93321048c4268cec2fcf))
* Update googleapis/sdk-platform-java action to v2.62.3 ([#3322](https://github.com/googleapis/java-storage/issues/3322)) ([a5808ea](https://github.com/googleapis/java-storage/commit/a5808ea168a81f07040276c1a05da67108fda37f))

### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [3.4.1](https://github.com/googleapis/python-storage/compare/v3.4.0...v3.4.1) (2025-10-08)

##### Bug Fixes

* Fixes [#1561](https://github.com/googleapis/python-storage/issues/1561) by adding an option to specify the entire object checksum for resumable uploads via the `upload_from_string`, `upload_from_file`, and `upload_from_filename` methods ([acb918e](https://github.com/googleapis/python-storage/commit/acb918e20f7092e13d72fc63fe4ae2560bfecd40))

---
## 2025-09-30

### Feature

[Object contexts](https://cloud.google.com/storage/docs/object-contexts) are now available in [Preview](https://cloud.google.com/products#product-launch-stages). Object contexts let you attach contextual
information to your objects to help you manage and discover data.

---
## 2025-09-29

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.57.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.56.1...storage/v1.57.0) (2025-09-23)

##### Features

* **storage/control:** Add new GetIamPolicy, SetIamPolicy, and TestIamPermissions RPCs ([d73f912](https://github.com/googleapis/google-cloud-go/commit/d73f9123be77bb3278f48d510cd0fb22feb605bc))
* **storage:** Post support dynamic key name ([#12677](https://github.com/googleapis/google-cloud-go/issues/12677)) ([9e761f9](https://github.com/googleapis/google-cloud-go/commit/9e761f961a2c4351b3e0793ed655314ac5853903))
* **storage:** WithMeterProvider allows custom meter provider configuration ([#12668](https://github.com/googleapis/google-cloud-go/issues/12668)) ([7f574b0](https://github.com/googleapis/google-cloud-go/commit/7f574b01e0b454c1ef5c13e6a58075e394ee990d))

##### Bug Fixes

* **storage:** Free buffers in Bidi Reader ([#12839](https://github.com/googleapis/google-cloud-go/issues/12839)) ([bc247fd](https://github.com/googleapis/google-cloud-go/commit/bc247fdc3f5234a8bd6934e58d5b0b578f1335cb))
* **storage:** Make Writer thread-safe. ([#12753](https://github.com/googleapis/google-cloud-go/issues/12753)) ([9ea380b](https://github.com/googleapis/google-cloud-go/commit/9ea380bea5b980a9054d201be4f315a195da2182))
* **storage:** No progress report for oneshot write ([#12746](https://github.com/googleapis/google-cloud-go/issues/12746)) ([b97c286](https://github.com/googleapis/google-cloud-go/commit/b97c286ec369a10a81b1a8a3a1aae18b46d2dfbc))

##### Performance Improvements

* **storage:** Pipeline gRPC writes ([#12422](https://github.com/googleapis/google-cloud-go/issues/12422)) ([1f2c5fe](https://github.com/googleapis/google-cloud-go/commit/1f2c5fe2843724302086fe04cb8dab8b515969c5))

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.58.0](https://github.com/googleapis/java-storage/compare/v2.57.0...v2.58.0) (2025-09-23)

##### Features

* **storagecontrol:** Add GetIamPolicy, SetIamPolicy, and TestIamPermissions RPCs ([c884551](https://github.com/googleapis/java-storage/commit/c884551048a323f2a3fd7aaf4fce469d4d4f543e))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.62.2 ([984f8ca](https://github.com/googleapis/java-storage/commit/984f8ca23a38c7a892a2256a694b72431e44aa27))
* Fix appendable upload finalization race condition ([#3295](https://github.com/googleapis/java-storage/issues/3295)) ([485be18](https://github.com/googleapis/java-storage/commit/485be184c08c7b857d8c9a9443f32903df879b23))
* Fix IllegalMonitorStateException thrown from BlobAppendableUpload.isOpen() ([#3302](https://github.com/googleapis/java-storage/issues/3302)) ([aa90468](https://github.com/googleapis/java-storage/commit/aa904688b784d7427454318196ef88628e415246))
* Update object context diff logic to be shallow rather than deep ([#3287](https://github.com/googleapis/java-storage/issues/3287)) ([2fd15f6](https://github.com/googleapis/java-storage/commit/2fd15f69e93a3df2b8dbbd4f08edd07c087e957c))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.2 ([#3298](https://github.com/googleapis/java-storage/issues/3298)) ([1489f3a](https://github.com/googleapis/java-storage/commit/1489f3a74c8a27f0888c40600c83adedcfd9a9ec))
* Update googleapis/sdk-platform-java action to v2.62.2 ([#3299](https://github.com/googleapis/java-storage/issues/3299)) ([c3b05ac](https://github.com/googleapis/java-storage/commit/c3b05ac8798140f9ddcab098948a3a2f3638dc6b))

---
## 2025-09-22

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.56.2](https://github.com/googleapis/google-cloud-go/compare/storage/v1.56.1...storage/v1.56.2) (2025-09-15)

##### Bug Fixes

* **storage:** Free buffers in Bidi Reader ([#12839](https://github.com/googleapis/google-cloud-go/issues/12839)) ([10c8fac](https://github.com/googleapis/google-cloud-go/commit/10c8faccc2dae2a8177ff30ab16d67413df9f536))

### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [3.4.0](https://github.com/googleapis/python-storage/compare/v3.3.1...v3.4.0) (2025-09-15)

##### Features

* **experimental:** Add async grpc client ([#1537](https://github.com/googleapis/python-storage/issues/1537)) ([ac57b8d](https://github.com/googleapis/python-storage/commit/ac57b8d819a49aef0ed0cb5bb630bf11012f43e3))
* **experimental:** Add grpc client ([#1533](https://github.com/googleapis/python-storage/issues/1533)) ([5674587](https://github.com/googleapis/python-storage/commit/5674587f2aa347ec2787f2bc1e847eaa294bc1ca))

##### Bug Fixes

* GAPIC generation failed with 'Directory not empty' ([#1542](https://github.com/googleapis/python-storage/issues/1542)) ([c80d820](https://github.com/googleapis/python-storage/commit/c80d8207a8661b84c56cd66bb34de7b5704675b8))

---
## 2025-09-17

### Feature

The `bucket_attributes_view` and `bucket_attributes_latest_snapshot_view` tables in [Storage Insights datasets](https://cloud.google.com/storage/docs/insights/datasets) are updated with two new fields: `objectCount` and `totalSize`. `objectCount` reflects the total number of objects in the bucket and `totalSize` reflects the total size of the bucket in bytes. The tables are automatically updated with the new fields in all existing datasets and are included in all new dataset configurations.

---
## 2025-09-15

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.17.1](https://github.com/googleapis/nodejs-storage/compare/v7.17.0...v7.17.1) (2025-08-27)

##### Bug Fixes

* Respect useAuthWithCustomEndpoint flag for resumable uploads ([#2637](https://github.com/googleapis/nodejs-storage/issues/2637)) ([707b4f2](https://github.com/googleapis/nodejs-storage/commit/707b4f2fe1d67878bcd8f1434e4cbb57c951994e))

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.57.0](https://github.com/googleapis/java-storage/compare/v2.56.0...v2.57.0) (2025-09-09)

##### Features

* Add BlobInfo.ObjectContexts ([#3259](https://github.com/googleapis/java-storage/issues/3259)) ([485aefd](https://github.com/googleapis/java-storage/commit/485aefd3047c52c98d8bd913033c8aee1473e988))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 ([0e348db](https://github.com/googleapis/java-storage/commit/0e348dbee247e1e65713d0155e1aa29ae5c5e0e4))
* Update BlobAppendableUpload implementation to periodically flush for large writes ([#3278](https://github.com/googleapis/java-storage/issues/3278)) ([d0ffe18](https://github.com/googleapis/java-storage/commit/d0ffe18084b32936c889bb280005294c7ae7064d))
* Update otel integration to properly activate span context for lazy RPCs such as reads & writes pt.2 ([#3277](https://github.com/googleapis/java-storage/issues/3277)) ([3240f67](https://github.com/googleapis/java-storage/commit/3240f67c192a855c92256526aeb2fa689ea15445))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#3280](https://github.com/googleapis/java-storage/issues/3280)) ([d046ea3](https://github.com/googleapis/java-storage/commit/d046ea3da19288b64c48300bdd4f94a0ebf35458))
* Update googleapis/sdk-platform-java action to v2.62.1 ([#3281](https://github.com/googleapis/java-storage/issues/3281)) ([c9078bb](https://github.com/googleapis/java-storage/commit/c9078bb98e3999234f95ab2e4c842c9dd7191c3d))

---
## 2025-09-10

### Feature

Cloud Storage FUSE now supports buffered reads, which can improve sequential read performance for large files by two to five times. When enabled, Cloud Storage FUSE asynchronously prefetches parts of a file into an in-memory buffer, allowing subsequent reads to be served from the buffer instead of requiring network calls.

To learn more about buffered reads, see [Enable buffered reads](https://cloud.google.com/storage/docs/cloud-storage-fuse/performance#enable-buffered-reads).

---
## 2025-09-01

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.56.0](https://github.com/googleapis/java-storage/compare/v2.55.0...v2.56.0) (2025-08-25)

##### Features

* *breaking behavior* rewrite Storage.blobAppendableUpload to be non-blocking and have improved throughput ([#3231](https://github.com/googleapis/java-storage/issues/3231)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
* Add AppendableUploadWriteableByteChannel#flush() ([#3261](https://github.com/googleapis/java-storage/issues/3261)) ([950c56f](https://github.com/googleapis/java-storage/commit/950c56f0e622d75faff51257d5cbc9f3ddc7e1ce))
* Add MinFlushSizeFlushPolicy#withMaxPendingBytes(long) ([#3231](https://github.com/googleapis/java-storage/issues/3231)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
* Add StorageChannelUtils to provide helper methods to perform blocking read/write to/from non-blocking channels ([#3231](https://github.com/googleapis/java-storage/issues/3231)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))

##### Bug Fixes

* Make FlushPolicy${Min,Max}FlushSizeFlushPolicy constructors private ([#3217](https://github.com/googleapis/java-storage/issues/3217)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
* Update BlobAppendableUploadConfig and FlushPolicy.MinFlushSizeFlushPolicy to default to 4MiB minFlushSize and 16MiB maxPendingBytes ([#3249](https://github.com/googleapis/java-storage/issues/3249)) ([7bd73d3](https://github.com/googleapis/java-storage/commit/7bd73d3104f5c47299f5a9c8d68dec82933eeda5))
* Update otel integration to properly activate span context for lazy RPCs such as reads & writes ([#3255](https://github.com/googleapis/java-storage/issues/3255)) ([d6587f4](https://github.com/googleapis/java-storage/commit/d6587f42b65a586a2e3f30e0559975801726a812))

##### Dependencies

* Update actions/checkout action to v5 ([#3239](https://github.com/googleapis/java-storage/issues/3239)) ([33f024b](https://github.com/googleapis/java-storage/commit/33f024b1ae094bf3e3605e1a835cb55eb5c9e750))
* Update dependency com.google.apis:google-api-services-storage to v1-rev20250815-2.0.0 ([#3245](https://github.com/googleapis/java-storage/issues/3245)) ([87afe1a](https://github.com/googleapis/java-storage/commit/87afe1ac5f500053e4c0639d5b824304d03796f4))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#3250](https://github.com/googleapis/java-storage/issues/3250)) ([0782e62](https://github.com/googleapis/java-storage/commit/0782e62fc9534e3cecfaaa4d78b58904ecf699d6))

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [3.3.1](https://github.com/googleapis/python-storage/compare/v3.3.0...v3.3.1) (2025-08-25)

##### Bug Fixes

* Provide option to user to set entire object checksum at "initiate a resumable upload session" and send the same.([#1525](https://github.com/googleapis/python-storage/issues/1525)) ([a8109e0](https://github.com/googleapis/python-storage/commit/a8109e0d02c62542f1bea20373b53864fb776caa))
* Send part's checksum for XML MPU part upload ([#1529](https://github.com/googleapis/python-storage/issues/1529)) ([2ad77c7](https://github.com/googleapis/python-storage/commit/2ad77c7d949e84c515c051a0fd4b37b822788dd8))

---
## 2025-08-28

### Changed

Beginning October 31, 2025, if you set an object's `age` condition to a value of `0` when setting Object Lifecycle Management rules, the condition is satisfied at midnight UTC after the object is created, which helps reduce unintended data loss. To learn more about the `age` condition, see [Lifecycle conditions](https://cloud.google.com/storage/docs/lifecycle#conditions).

---
## 2025-08-25

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/storage](https://github.com/googleapis/nodejs-storage)

#### [7.17.0](https://github.com/googleapis/nodejs-storage/compare/v7.16.0...v7.17.0) (2025-08-18)

##### Features

* Add CSEK to download ([#2604](https://github.com/googleapis/nodejs-storage/issues/2604)) ([cacc0be](https://github.com/googleapis/nodejs-storage/commit/cacc0be49a4fe81c384180bdfd77820b6b3f3001))

##### Bug Fixes

* Propagate errors when using pipelines ([#2560](https://github.com/googleapis/nodejs-storage/issues/2560)) ([#2624](https://github.com/googleapis/nodejs-storage/issues/2624)) ([a43b490](https://github.com/googleapis/nodejs-storage/commit/a43b4904ecf2ebacde22bc6efbdcf97ac886e28d))
* Typo correction ([#2610](https://github.com/googleapis/nodejs-storage/issues/2610)) ([9cae69c](https://github.com/googleapis/nodejs-storage/commit/9cae69cc280227737b5a1a1476eae1b2612b162b))

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.56.1](https://github.com/googleapis/google-cloud-go/compare/storage/v1.56.0...storage/v1.56.1) (2025-08-19)

##### Bug Fixes

* **storage:** Fix redirect logic in MRD ([#12733](https://github.com/googleapis/google-cloud-go/issues/12733)) ([9f369f9](https://github.com/googleapis/google-cloud-go/commit/9f369f931853220550cabb3d67a5a5d3d9e137ba))
* **storage:** Pass all user options to NewService ([#12615](https://github.com/googleapis/google-cloud-go/issues/12615)) ([77cdb83](https://github.com/googleapis/google-cloud-go/commit/77cdb832a374eba29e4de7699324a87f1d20eea3))
* **storage:** ZB Reader redirect support ([#12703](https://github.com/googleapis/google-cloud-go/issues/12703)) ([3c7ea5c](https://github.com/googleapis/google-cloud-go/commit/3c7ea5ceb199d5787d36bf8f415f028bea66e3b5))

---
## 2025-08-18

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [3.3.0](https://github.com/googleapis/python-storage/compare/v3.2.0...v3.3.0) (2025-08-05)

##### Features

* Add support for bucket IP filter ([#1516](https://github.com/googleapis/python-storage/issues/1516)) ([a29073c](https://github.com/googleapis/python-storage/commit/a29073cf58df9c5667305e05c6378284057cda23))

##### Bug Fixes

* Add logs on AssertionError for issue [#1512](https://github.com/googleapis/python-storage/issues/1512) ([#1518](https://github.com/googleapis/python-storage/issues/1518)) ([6a9923e](https://github.com/googleapis/python-storage/commit/6a9923e4fc944f7a7c3906eb7800d23677bd2481))

##### Documentation

* Update the documentation of move\_blob function ([#1507](https://github.com/googleapis/python-storage/issues/1507)) ([72252e9](https://github.com/googleapis/python-storage/commit/72252e940909ce2e3da9cfd80f5b7b43a026f45c))

---
## 2025-08-12

### Feature

You can now use Anywhere Cache in the `asia-south1-b` and `asia-south1-c` zones. For more information, see [Anywhere Cache supported locations](https://cloud.google.com/storage/docs/anywhere-cache#supported-locations).

---
## 2025-08-11

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.55.0](https://github.com/googleapis/java-storage/compare/v2.54.0...v2.55.0) (2025-08-05)

##### Features

* Add new preview Bucket encryption policy configuration ([#3204](https://github.com/googleapis/java-storage/issues/3204)) ([7b250dd](https://github.com/googleapis/java-storage/commit/7b250dd53cfa29bbb6a0a4cb4a345aeb2dab5c86))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 ([f98b686](https://github.com/googleapis/java-storage/commit/f98b686ef940879458acb1e56339adf869400b94))
* Enable ALTS bound token (for DirectPath) in the grpc channel provider ([#2919](https://github.com/googleapis/java-storage/issues/2919)) ([38d248d](https://github.com/googleapis/java-storage/commit/38d248d9511e808e88c1bac0b6bb2ba54897830d))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#3213](https://github.com/googleapis/java-storage/issues/3213)) ([86ff697](https://github.com/googleapis/java-storage/commit/86ff69788b30d8f82b6b95d010df507093852889))

### Feature

You can now use Anywhere Cache in the `asia-south1-a` zone. For more information, see [Anywhere Cache supported locations](https://cloud.google.com/storage/docs/anywhere-cache#supported-locations).

---
## 2025-08-04

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.54.0](https://github.com/googleapis/java-storage/compare/v2.53.3...v2.54.0) (2025-07-24)

##### Features

* Add BucketInfo.IpFilter ([#3177](https://github.com/googleapis/java-storage/issues/3177)) ([14a91ec](https://github.com/googleapis/java-storage/commit/14a91ec208067e6afc55923cffda5f69aa33d8b4))
* Add default end-to-end checksumming for JournalingBlobWriteSessionConfig [#3180](https://github.com/googleapis/java-storage/issues/3180) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))
* Add default end-to-end crc32c checksumming for several upload methods via grpc transport [#3176](https://github.com/googleapis/java-storage/issues/3176) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([bd1f199](https://github.com/googleapis/java-storage/commit/bd1f199cf57c2b8039c303586d5beac64aeca0ba))
* Give user provided checksum precondition priority for Storage#create methods that accept byte[] [#3182](https://github.com/googleapis/java-storage/issues/3182) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))
* Move crc32c computation before writing to disk for BufferToDiskThenUpload BlobWriteSession config [#3187](https://github.com/googleapis/java-storage/issues/3187) ([fa0f6a0](https://github.com/googleapis/java-storage/commit/fa0f6a03380af78e239bd0079267649ba4138f38))

##### Dependencies

* Update dependency com.google.apis:google-api-services-storage to v1-rev20250718-2.0.0 ([#3203](https://github.com/googleapis/java-storage/issues/3203)) ([18978e4](https://github.com/googleapis/java-storage/commit/18978e4ec54790df2939490ef76fc19b9f72eb04))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#3201](https://github.com/googleapis/java-storage/issues/3201)) ([782c3c4](https://github.com/googleapis/java-storage/commit/782c3c416583704a196b17f23e9c12c33659f67d))
* Update googleapis/sdk-platform-java action to v2.60.1 ([#3196](https://github.com/googleapis/java-storage/issues/3196)) ([6ba56e5](https://github.com/googleapis/java-storage/commit/6ba56e5a4b86a75a9f48beccf79ff6d5fdd3e19f))

---
## 2025-07-28

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.56.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.55.0...storage/v1.56.0) (2025-07-24)

##### Features

* **storage/control:** Update BUILD configs to support rest transportation for all client ([116a33a](https://github.com/googleapis/google-cloud-go/commit/116a33ab13c9fac6f6830dded55c24d38504707b))

##### Bug Fixes

* **storage:** Avoid integration test segfaults. ([#12419](https://github.com/googleapis/google-cloud-go/issues/12419)) ([a9dec07](https://github.com/googleapis/google-cloud-go/commit/a9dec0763f85f083cc1da451249caae7ad97d904))
* **storage:** Current object generation takeover. ([#12383](https://github.com/googleapis/google-cloud-go/issues/12383)) ([9ca8e01](https://github.com/googleapis/google-cloud-go/commit/9ca8e015405a523bbe68cbff2defbdff3dac0a61))
* **storage:** Fix MultiRangeDownloader deadlock ([#12548](https://github.com/googleapis/google-cloud-go/issues/12548)) ([2eb23bb](https://github.com/googleapis/google-cloud-go/commit/2eb23bb01ffe92c967e772ef66c846357fbf5419))
* **storage:** Remove object length limit for unfinalized reads ([#12489](https://github.com/googleapis/google-cloud-go/issues/12489)) ([5566d7d](https://github.com/googleapis/google-cloud-go/commit/5566d7dd5cc83afce38821961c447f5945e48456))

##### Performance Improvements

* **storage:** Zero copy for MultiRangeDownloader ([#12542](https://github.com/googleapis/google-cloud-go/issues/12542)) ([a5e6a68](https://github.com/googleapis/google-cloud-go/commit/a5e6a681164d5be62270cde16891685a9f03bb12))

##### Documentation

* **storage/internal:** Fix broken link for message `CustomPlacementConfig` ([9614487](https://github.com/googleapis/google-cloud-go/commit/96144875e01bfc8a59c2671c6eae87233710cef7))
* **storage:** Fix typo in storage/doc.go ([#12391](https://github.com/googleapis/google-cloud-go/issues/12391)) ([bf74408](https://github.com/googleapis/google-cloud-go/commit/bf744088f0ed23ea510b914c994e1754ca1fc7c4))
* **storage:** Improve error inspection documentation ([#12301](https://github.com/googleapis/google-cloud-go/issues/12301)) ([420da1a](https://github.com/googleapis/google-cloud-go/commit/420da1a64ac4040c8b2e6d6f0d66e7633426ac25))

---
## 2025-07-14

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.53.3](https://github.com/googleapis/java-storage/compare/v2.53.2...v2.53.3) (2025-07-09)

##### Bug Fixes

* Fix DefaultBlobWriteSessionConfig init to work when grpc classes are excluded ([#3147](https://github.com/googleapis/java-storage/issues/3147)) ([8571ba8](https://github.com/googleapis/java-storage/commit/8571ba8eee82d055cdeb5f0b6970d5b814eaa24e))

##### Dependencies

* Update dependency com.google.apis:google-api-services-storage to v1-rev20250629-2.0.0 ([#3185](https://github.com/googleapis/java-storage/issues/3185)) ([4ce8281](https://github.com/googleapis/java-storage/commit/4ce8281246cbe84ed068205532cac4a03853c331))
* Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#3189](https://github.com/googleapis/java-storage/issues/3189)) ([7fbfb01](https://github.com/googleapis/java-storage/commit/7fbfb013a8cfb72d49e3d752ad25e73b6ccaab4f))

---
## 2025-07-08

### Feature

You can now create caches with Anywhere Cache in the `us-west3-a`, `us-west3-b`, and `us-west3-c` zones. For more information about supported locations for Anywhere Cache, see [Supported locations](https://cloud.google.com/storage/docs/anywhere-cache#supported-locations).

---
## 2025-07-07

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [3.2.0](https://github.com/googleapis/python-storage/compare/v3.1.1...v3.2.0) (2025-07-04)

##### Features

* Adding support of single shot download ([#1493](https://github.com/googleapis/python-storage/issues/1493)) ([61c5d5f](https://github.com/googleapis/python-storage/commit/61c5d5f62c88506f200bc6d86b399a2c28715bc4))

---
## 2025-07-02

### Feature

[Bucket IP filtering](https://cloud.google.com/storage/docs/ip-filtering-overview) for Cloud Storage is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Bucket IP filtering provides enhanced control over access to your data, allowing you to restrict incoming requests to your Cloud Storage buckets based on their source IP addresses or their Google Cloud Virtual Private Cloud.

---
## 2025-06-30

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.53.2](https://github.com/googleapis/java-storage/compare/v2.53.1...v2.53.2) (2025-06-25)

##### Bug Fixes

* Fix Journaling BlobWriteSessionConfig to properly handle multiple consecutive retries ([#3166](https://github.com/googleapis/java-storage/issues/3166)) ([895bfbd](https://github.com/googleapis/java-storage/commit/895bfbda902a77d16a33fe5238349a6b3d397c10))

##### Dependencies

* Update dependency com.google.cloud.opentelemetry:exporter-trace to v0.36.0 ([#3162](https://github.com/googleapis/java-storage/issues/3162)) ([41a1030](https://github.com/googleapis/java-storage/commit/41a1030a2e77036cf961a16d472068b07e624192))
* Update sdk-platform-java dependencies ([#3164](https://github.com/googleapis/java-storage/issues/3164)) ([c22a131](https://github.com/googleapis/java-storage/commit/c22a1319d8e2d92beeb03abac6bf2af8d09d49ee))

---
## 2025-06-23

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.53.1](https://github.com/googleapis/java-storage/compare/v2.53.0...v2.53.1) (2025-06-18)

##### Bug Fixes

* Cancel the future in RemoteStorageHelper#forceDelete when TimeoutException happens ([#3136](https://github.com/googleapis/java-storage/issues/3136)) ([e6007d5](https://github.com/googleapis/java-storage/commit/e6007d56e8801be65209cb5761f62749369425c9))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.59.0 ([7dba9f0](https://github.com/googleapis/java-storage/commit/7dba9f09f100062cc8c04e5a2735a4349d8e7ed1))

##### Dependencies

* Update dependency com.google.apis:google-api-services-storage to v1-rev20250605-2.0.0 ([#3143](https://github.com/googleapis/java-storage/issues/3143)) ([17a80d8](https://github.com/googleapis/java-storage/commit/17a80d8b49fef65557215b310895b0f08ee25235))
* Update sdk-platform-java dependencies ([#3152](https://github.com/googleapis/java-storage/issues/3152)) ([2f78192](https://github.com/googleapis/java-storage/commit/2f78192d97e9d3ca29c97a52a66a074777dce196))

### Python

### Changes for [google-cloud-storage](https://github.com/googleapis/python-storage)

#### [3.1.1](https://github.com/googleapis/python-storage/compare/v3.1.0...v3.1.1) (2025-06-13)

##### Bug Fixes

* Add a check for partial response data ([#1487](https://github.com/googleapis/python-storage/issues/1487)) ([7e0412a](https://github.com/googleapis/python-storage/commit/7e0412a4fdfedcaa4683d5ef7d9155d5d58efa11))
* Add trove classifier for Python 3.13 ([0100916](https://github.com/googleapis/python-storage/commit/01009164beaab8931a1e1684966e3060edcf77b7))
* **deps:** Require google-crc32c >= 1.1.3 ([0100916](https://github.com/googleapis/python-storage/commit/01009164beaab8931a1e1684966e3060edcf77b7))
* **deps:** Require protobuf >= 3.20.2, < 7.0.0 ([0100916](https://github.com/googleapis/python-storage/commit/01009164beaab8931a1e1684966e3060edcf77b7))
* **deps:** Require requests >= 2.22.0 ([0100916](https://github.com/googleapis/python-storage/commit/01009164beaab8931a1e1684966e3060edcf77b7))
* Remove setup.cfg configuration for creating universal wheels ([#1448](https://github.com/googleapis/python-storage/issues/1448)) ([d3b6b3f](https://github.com/googleapis/python-storage/commit/d3b6b3f96a6f94aa7c371902f48d1363ae6bfb5c))
* Resolve issue where pre-release versions of dependencies are installed ([0100916](https://github.com/googleapis/python-storage/commit/01009164beaab8931a1e1684966e3060edcf77b7))
* Segmentation fault in tink while writing data ([#1490](https://github.com/googleapis/python-storage/issues/1490)) ([2a46c0b](https://github.com/googleapis/python-storage/commit/2a46c0b9e6ec561ae3151d2a9a80c7452634487e))

##### Documentation

* Move quickstart to top of readme ([#1451](https://github.com/googleapis/python-storage/issues/1451)) ([53257cf](https://github.com/googleapis/python-storage/commit/53257cf20a4de3810156ae9576a7092f5527df98))
* Update README to break infinite redirect loop ([#1450](https://github.com/googleapis/python-storage/issues/1450)) ([03f1594](https://github.com/googleapis/python-storage/commit/03f1594eb90ea1298a3a23927537c86ac35d33d5))

### Feature

The Cloud Storage Cloud Audit Logs have expanded support to include error scenario coverage and produce a more comprehensive error message with code, error messages, and details, in an easy to understand format. The Gemini Cloud Assist (GCA) service can then easily analyze the log and provide tailored recommendations on how to mitigate issues as they arise. Before this enhancement, error logs were generated for only a specific set of scenarios, and the status field solely contained the gRPC error code without any additional information. To learn more about Cloud Audit Logs, see [Cloud Audit Logs overview](https://cloud.google.com/logging/docs/audit).

---
## 2025-06-16

### Feature

Cloud Storage FUSE version 3.0 is now available with new features and enhancements designed to improve performance and simplify configuration. Improvements include [automated configurations for high-performance machines](https://cloud.google.com/storage/docs/cloud-storage-fuse/automated-configurations), a comprehensive [performance tuning guide](https://cloud.google.com/storage/docs/cloud-storage-fuse/performance) to help optimize performance, and the new [`global-max-blocks` configuration option](https://cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#write-global-max-blocks), which gives you granular control over streaming write operations.

---
## 2025-06-09

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-storage](https://github.com/googleapis/java-storage)

#### [2.53.0](https://github.com/googleapis/java-storage/compare/v2.52.3...v2.53.0) (2025-06-04)

##### Features

* Expose BucketInfo.getProject as a BigInteger ([#3119](https://github.com/googleapis/java-storage/issues/3119)) ([64bbb60](https://github.com/googleapis/java-storage/commit/64bbb608033f757cb6e31e75a78740d8ed1dccab)), closes [#3023](https://github.com/googleapis/java-storage/issues/3023)
* **storagecontrol:** Add Anywhere cache control APIs ([06572b7](https://github.com/googleapis/java-storage/commit/06572b7ced2829cdc00bf648521c024a52d93b3a))
* **storagecontrol:** Add Client Libraries Storage IntelligenceConfig ([06572b7](https://github.com/googleapis/java-storage/commit/06572b7ced2829cdc00bf648521c024a52d93b3a))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.58.0 ([06572b7](https://github.com/googleapis/java-storage/commit/06572b7ced2829cdc00bf648521c024a52d93b3a))

##### Dependencies

* Update dependency com.google.apis:google-api-services-storage to v1-rev20250521-2.0.0 ([#3118](https://github.com/googleapis/java-storage/issues/3118)) ([e1be49e](https://github.com/googleapis/java-storage/commit/e1be49e6c987daccf9542c15c6ba418c007d2fb7))
* Update dependency com.google.apis:google-api-services-storage to v1-rev20250524-2.0.0 ([#3127](https://github.com/googleapis/java-storage/issues/3127)) ([2a4499d](https://github.com/googleapis/java-storage/commit/2a4499d1686e93e8495f29b5198488d166caaa06))
* Update sdk-platform-java dependencies ([#3129](https://github.com/googleapis/java-storage/issues/3129)) ([31cd058](https://github.com/googleapis/java-storage/commit/31cd058dcaf5a891ecb7a955602b09634d912560))

##### Documentation

* Add explicit Optional annotations to fields that have always been treated as optional ([53b6927](https://github.com/googleapis/java-storage/commit/53b6927de9e5b948e1192e6cf716b88cc872c632))
* Add note that Bucket.project output format is always project number format ([53b6927](https://github.com/googleapis/java-storage/commit/53b6927de9e5b948e1192e6cf716b88cc872c632))
* Add note that managedFolders are supported for GetIamPolicy and SetIamPolicy ([53b6927](https://github.com/googleapis/java-storage/commit/53b6927de9e5b948e1192e6cf716b88cc872c632))

---
## 2025-06-05

### Changed

The limit for the maximum number of prefixes and suffixes when using [matchesPrefix and matchesSuffix lifecycle conditions](https://cloud.google.com/storage/docs/lifecycle#matchesprefix-suffix) across all rules on a bucket is increased from 50 to 1,000. For more information, see [Quotas and limits](https://cloud.google.com/storage/quotas#buckets).

---
## 2025-06-02

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Go

### Changes for [storage/internal/apiv2](https://github.com/googleapis/google-cloud-go/tree/main/storage/internal/apiv2)

#### [1.55.0](https://github.com/googleapis/google-cloud-go/compare/storage/v1.54.0...storage/v1.55.0) (2025-05-29)

##### Features

* **storage/control:** Add Client Libraries Storage IntelligenceConfig ([2aaada3](https://github.com/googleapis/google-cloud-go/commit/2aaada3fb7a9d3eaacec3351019e225c4038646b))
* **storage/internal:** Add IpFilter to Bucket ([#12309](https://github.com/googleapis/google-cloud-go/issues/12309)) ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))
* **storage/internal:** Add Object.Retention message ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))

##### Bug Fixes

* **storage:** Add EnableNewAuthLibrary internalOption to HTTP newClient ([#12320](https://github.com/googleapis/google-cloud-go/issues/12320)) ([0036073](https://github.com/googleapis/google-cloud-go/commit/0036073affee5451894654a983fba6b2638433cb))
* **storage:** Migrate oauth2/google usages to cloud.google.com/go/auth ([#11191](https://github.com/googleapis/google-cloud-go/issues/11191)) ([3a22349](https://github.com/googleapis/google-cloud-go/commit/3a22349c1ba6a192d70269f77e5804a9957aa572))
* **storage:** Omit check on MultiRangeDownloader ([#12342](https://github.com/googleapis/google-cloud-go/issues/12342)) ([774621c](https://github.com/googleapis/google-cloud-go/commit/774621c5baa5110f57fe79d817143416bd671d1e))
* **storage:** Retry url.Error and net.OpErrors when they wrap an io.EOF ([#12289](https://github.com/googleapis/google-cloud-go/issues/12289)) ([080f6b0](https://github.com/googleapis/google-cloud-go/commit/080f6b05c5e8bd5baaef71ed47f8d54c695f63d3))

##### Documentation

* **storage/internal:** Add explicit Optional annotations to fields that have always been treated as optional ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))
* **storage/internal:** Add note that Bucket.project output format is always project number format ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))
* **storage/internal:** Add note that managedFolders are supported for GetIamPolicy and SetIamPolicy ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))

---
