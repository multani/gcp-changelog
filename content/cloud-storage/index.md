# Cloud Storage

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
