# Bigtable

## 2026-09-01

### Feature

You can use the Google Cloud console to create and manage [aggregate column families](https://docs.cloud.google.com/bigtable/docs/aggregates)
for your Bigtable tables. You can also view and query aggregate column families in Bigtable Studio. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Create and manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables#add-column-families) and [Manage your data using Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console).

---
## 2026-08-20

### Feature

You can use the `allow_incomplete_view` query hint in SQL queries to read data
from a continuous materialized view before its initial population finishes. This
feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see [Read data during initial population](https://docs.cloud.google.com/bigtable/docs/reads#read-during-initial-population).

---
## 2026-08-12

### Feature

You can use parameterized views in Bigtable to dynamically filter data ranges
for logical views based on application context and mitigate SQL injection risks.
This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see [Parameterized views overview](https://docs.cloud.google.com/bigtable/docs/parameterized-views-overview).

### Feature

You can use the `CLUSTER_ATTRIBUTE()` filter to restrict continuous materialized
view processing to specific clusters. This function lets you isolate views
within an instance. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see [Non-deterministic SQL functions](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views#non-deterministic-functions).

---
## 2026-08-10

### Libraries

### Go

#### [1.52.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.51.0...bigtable/v1.52.0) (2026-08-03)

##### Features

* **bigtable:** Add AFE picker (Simple / LeastInFlight / LeastLatency) ([#20204](https://github.com/googleapis/google-cloud-go/issues/20204)) ([bcbf714](https://github.com/googleapis/google-cloud-go/commit/bcbf71431d1742e2e13a13d1cbe8b0fc0433aede))
* **bigtable:** Add ClientConfig.DisableSession to opt out of session backend ([#20297](https://github.com/googleapis/google-cloud-go/issues/20297)) ([7ee5e44](https://github.com/googleapis/google-cloud-go/commit/7ee5e44e0304c5509b9b77fe0760d97771657cd9))
* **bigtable:** Add getClientConfigDirectAccessChecker for session pools ([#20209](https://github.com/googleapis/google-cloud-go/issues/20209)) ([3b8d30a](https://github.com/googleapis/google-cloud-go/commit/3b8d30adeaf03c8452207b056d69922646d63bf2))
* **bigtable:** Add NoOpChannelPrimer for session channel pools ([#20208](https://github.com/googleapis/google-cloud-go/issues/20208)) ([d055a8a](https://github.com/googleapis/google-cloud-go/commit/d055a8a1b23980ad4b53c0cd690e291c9aa6248c))
* **bigtable:** Add per-AFE sessionList for the two-tier session pool ([#20224](https://github.com/googleapis/google-cloud-go/issues/20224)) ([dbf0c3f](https://github.com/googleapis/google-cloud-go/commit/dbf0c3f3ea37279a2aa00803ded8e489229b15c9))
* **bigtable:** Add protoRowToRow conversion helper for TableShim ([#20257](https://github.com/googleapis/google-cloud-go/issues/20257)) ([1297143](https://github.com/googleapis/google-cloud-go/commit/1297143a4fab4bf58cbd0bd6e44db4653a818c47))
* **bigtable:** Add Session debug surface (observability fields + methods) ([#20211](https://github.com/googleapis/google-cloud-go/issues/20211)) ([d8d3e16](https://github.com/googleapis/google-cloud-go/commit/d8d3e160c3e63150ef5d14e83a2ea0fd25a7e214))
* **bigtable:** Add Session lifecycle (Start, Close, ForceClose, readLoop, heartBeatLoop) ([#20215](https://github.com/googleapis/google-cloud-go/issues/20215)) ([b9e53c6](https://github.com/googleapis/google-cloud-go/commit/b9e53c6276efe28428adfcd4671d7ac8c7e8d330))
* **bigtable:** Add Session struct + state machine ([#20117](https://github.com/googleapis/google-cloud-go/issues/20117)) ([09acbb3](https://github.com/googleapis/google-cloud-go/commit/09acbb37a385d2c6fca465adb70a3eb03ea4a38e))
* **bigtable:** Add session.Config.EnableDebug to gate sessionz debug state ([#20247](https://github.com/googleapis/google-cloud-go/issues/20247)) ([ce74c31](https://github.com/googleapis/google-cloud-go/commit/ce74c315d41371b0ddf2c1ba7342446695a53900))
* **bigtable:** Add SessionClient + SessionTable + lazyPool ([#20228](https://github.com/googleapis/google-cloud-go/issues/20228)) ([ab2c96c](https://github.com/googleapis/google-cloud-go/commit/ab2c96c3ed62514dcf6526bb32259267fbe63e97))
* **bigtable:** Add SessionPoolImpl (two-tier pool + scaling + debug) ([#20225](https://github.com/googleapis/google-cloud-go/issues/20225)) ([683eda8](https://github.com/googleapis/google-cloud-go/commit/683eda8c690fd2b948bd3b56777039d28421ee7c))
* **bigtable:** Rename session pool display to <resource-id>-<PERM> ([#20248](https://github.com/googleapis/google-cloud-go/issues/20248)) ([35e146e](https://github.com/googleapis/google-cloud-go/commit/35e146e25d2897082f2d1b78b9273087efd855fd))
* **bigtable:** Route Client.Open()-returned \*Table through the Diverter ([#20273](https://github.com/googleapis/google-cloud-go/issues/20273)) ([2b81c7d](https://github.com/googleapis/google-cloud-go/commit/2b81c7dc2d73739f4d5f87aa43cc9a3ac031822d))
* **bigtable:** State-based classification for abnormal session close ([#20243](https://github.com/googleapis/google-cloud-go/issues/20243)) ([f2905b7](https://github.com/googleapis/google-cloud-go/commit/f2905b793d062ae597d9c39597d15a680e9e9967))
* **bigtable:** TableShim fallback to classic on session UNIMPLEMENTED ([#20269](https://github.com/googleapis/google-cloud-go/issues/20269)) ([36540af](https://github.com/googleapis/google-cloud-go/commit/36540af84ab5f7360c5c1a92bbfb5a631d4c5cc6))
* **bigtable:** TTL-on-idle cache for per-resource session.TableAPI ([#20263](https://github.com/googleapis/google-cloud-go/issues/20263)) ([00b2a49](https://github.com/googleapis/google-cloud-go/commit/00b2a49de38fe600736cf10c496f85e082ae8871))
* **bigtable:** Wire Diverter on Client and route Open\* via TableShim ([#20256](https://github.com/googleapis/google-cloud-go/issues/20256)) ([b32fbd7](https://github.com/googleapis/google-cloud-go/commit/b32fbd7d02f835e8f83b4be1926e5826c27fa8a9))

##### Bug Fixes

* **bigtable:** AFE picker latency signal — subtract poolWait and compute TransportLatency = wire − backend at source ([#20281](https://github.com/googleapis/google-cloud-go/issues/20281)) ([bb8c4d5](https://github.com/googleapis/google-cloud-go/commit/bb8c4d56bf5bb53e5e1f1d510be326821fe4ddee))
* **bigtable:** Guard NewStream OnFinish against grpc-go double-fire ([#20295](https://github.com/googleapis/google-cloud-go/issues/20295)) ([b51da29](https://github.com/googleapis/google-cloud-go/commit/b51da29536de5aa59582d2a9633a07186f8636ae))
* **bigtable:** Real per-resource pool teardown on sessionTable.Close + cache close-race gate ([#20264](https://github.com/googleapis/google-cloud-go/issues/20264)) ([599aea9](https://github.com/googleapis/google-cloud-go/commit/599aea9e67ca2526b7822eb1e873e3aaf7b5124e))
* **bigtable:** Session.durations / session.uptime — set explicit histogram bucket boundaries ([#20276](https://github.com/googleapis/google-cloud-go/issues/20276)) ([97eee22](https://github.com/googleapis/google-cloud-go/commit/97eee225c412db9288bb7813e6b9cc856e6aba44))
* **bigtable:** SessionTableHandle self-heals across cache eviction ([#20296](https://github.com/googleapis/google-cloud-go/issues/20296)) ([0dd98cd](https://github.com/googleapis/google-cloud-go/commit/0dd98cd75383bd5902f3bec936d9ae68c64e6682))
* **bigtable:** Translate ctx errors to gRPC status on session vRPC ([#20299](https://github.com/googleapis/google-cloud-go/issues/20299)) ([0f3b2a5](https://github.com/googleapis/google-cloud-go/commit/0f3b2a519e07eccdfacad1129aa0fb69bc8f06e6))
* **bigtable:** Treat PingAndWarm NotFound as a successful prime ([#20219](https://github.com/googleapis/google-cloud-go/issues/20219)) ([a1557ad](https://github.com/googleapis/google-cloud-go/commit/a1557adec2fc8a579f70cdb4de5f959ceb8d51a1))

##### Performance Improvements

* **bigtable:** Delete periodic Tick loop; sizing is event-driven ([#20285](https://github.com/googleapis/google-cloud-go/issues/20285)) ([2c096bd](https://github.com/googleapis/google-cloud-go/commit/2c096bddf6fc5353a3804d222b3683a55eda13e5))
* **bigtable:** Drop pick\_lost\_race debug tag from CheckoutSession hot path ([#20280](https://github.com/googleapis/google-cloud-go/issues/20280)) ([bd0e400](https://github.com/googleapis/google-cloud-go/commit/bd0e400948a15639546f150d5d2b1a1a7ceb5741))

---
## 2026-07-30

### Feature

You can use Bigtable as a remote storage backend for
[LMCache](https://docs.lmcache.ai/kv_cache/storage_backends/bigtable.html). By
storing the large language model (LLM) key-value (KV) cache externally in
Bigtable, multiple AI serving instances can share and reuse precomputed
attention tensors. This reduces compute overhead and significantly improves
time-to-first-token (TTFT) for repeated prompts and shared documents. This
feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-07-29

### Feature

You can use the Google Cloud console to [manage row key schemas](https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas)
for your Bigtable tables. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-07-27

### Feature

The Bigtable remote MCP server supports the Bigtable Data API, which
provides the `execute_sql` tool that you can use to query Bigtable data using
natural language prompts. This feature is
[generally available (GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see
[Use the Bigtable remote MCP server](https://docs.cloud.google.com/bigtable/docs/use-bigtable-mcp).

### Libraries

### Go

#### [1.51.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.50.0...bigtable/v1.51.0) (2026-07-23)

##### Features

* **bigtable:** Add ChainInterceptors and RetryingVRpc for vRPC pipeline ([#20185](https://github.com/googleapis/google-cloud-go/issues/20185)) ([c7a832a](https://github.com/googleapis/google-cloud-go/commit/c7a832aa13bad0896c3906f491d798482dd8c02a))
* **bigtable:** Add ClientConfigurationManager ([#19986](https://github.com/googleapis/google-cloud-go/issues/19986)) ([3a8f927](https://github.com/googleapis/google-cloud-go/commit/3a8f9270d9c2831b5d76efe89c913555577ace6a))
* **bigtable:** Add debug tag counter (recordDebugTag / assertDebugTag) ([#20114](https://github.com/googleapis/google-cloud-go/issues/20114)) ([3c97590](https://github.com/googleapis/google-cloud-go/commit/3c97590192a19306612389e9d55b93b538e8584b))
* **bigtable:** Add lazyPool helper for on-demand session pool opening ([#20182](https://github.com/googleapis/google-cloud-go/issues/20182)) ([f6ae3fb](https://github.com/googleapis/google-cloud-go/commit/f6ae3fbf65e9e41a1c2d64f281f881ebe8828439))
* **bigtable:** Add PeakEwma continuous time-decay latency tracker ([#20187](https://github.com/googleapis/google-cloud-go/issues/20187)) ([9d124ef](https://github.com/googleapis/google-cloud-go/commit/9d124ef7773dae916dfbb97657f83ae633d15220))
* **bigtable:** Add PoolSizer for server-driven session pool capacity ([#20189](https://github.com/googleapis/google-cloud-go/issues/20189)) ([57ebbeb](https://github.com/googleapis/google-cloud-go/commit/57ebbeb8e846f574034e93060682309bc1a00dc1))
* **bigtable:** Add session package with SessionClient + SessionTableAPI interfaces ([#20180](https://github.com/googleapis/google-cloud-go/issues/20180)) ([4b82fd2](https://github.com/googleapis/google-cloud-go/commit/4b82fd25cc81cdee5563d5a049b48d2694bca088))
* **bigtable:** Add Session primitives (AttemptOutcome, vRPC ctx, msgtype) ([#20116](https://github.com/googleapis/google-cloud-go/issues/20116)) ([e1011e2](https://github.com/googleapis/google-cloud-go/commit/e1011e2d2c43a838abe080ad9d3f614f8c92e55a))
* **bigtable:** Add Session state enum ([#19981](https://github.com/googleapis/google-cloud-go/issues/19981)) ([0748972](https://github.com/googleapis/google-cloud-go/commit/07489725b63174375f7faa68b7aad18cc638c27b))
* **bigtable:** Add SessionThrottler / AdaptiveSessionThrottler for OpenSession pacing ([#20184](https://github.com/googleapis/google-cloud-go/issues/20184)) ([02e3c6d](https://github.com/googleapis/google-cloud-go/commit/02e3c6d19e8ff5b6a12803bc9b0636575e070dff))
* **bigtable:** Add SessionThrottler / AdaptiveSessionThrottler for OpenSession pacing ([#20184](https://github.com/googleapis/google-cloud-go/issues/20184)) ([29be83e](https://github.com/googleapis/google-cloud-go/commit/29be83ed3b631a472e28be4d8569d34f0a071d86))
* **bigtable:** Add sessionTracer for per-Session lifecycle + vRPC metrics ([#20190](https://github.com/googleapis/google-cloud-go/issues/20190)) ([a466345](https://github.com/googleapis/google-cloud-go/commit/a4663459260ba054af918c29a94570d5ec69f399))
* **bigtable:** Enable new auth library and JWT for instance admin client ([#20013](https://github.com/googleapis/google-cloud-go/issues/20013)) ([21c4a44](https://github.com/googleapis/google-cloud-go/commit/21c4a448adf789e8acaebfaed7df5c49ac434aab))
* **bigtable:** Modularize channel priming behind a ChannelPrimer interface ([#20027](https://github.com/googleapis/google-cloud-go/issues/20027)) ([5214ab7](https://github.com/googleapis/google-cloud-go/commit/5214ab7033bd8a5aa672878ae17ce828d5d78c3c))
* **bigtable:** Modularize Direct Access compatibility check ([#19987](https://github.com/googleapis/google-cloud-go/issues/19987)) ([a25e93d](https://github.com/googleapis/google-cloud-go/commit/a25e93d25635b8fd42985edbe0290ba9a8cf2169))
* **o11y:** Regenerate clients for LRO tracing ([#20107](https://github.com/googleapis/google-cloud-go/issues/20107)) ([779074e](https://github.com/googleapis/google-cloud-go/commit/779074edd267a26520bae459307660953129eb07))

##### Bug Fixes

* **bigtable:** Default cluster/zone in toOtelMetricAttrs to avoid Monitoring reject ([#20178](https://github.com/googleapis/google-cloud-go/issues/20178)) ([14493f4](https://github.com/googleapis/google-cloud-go/commit/14493f4de7298b8fac36c1ee67f2647fbc2e6ba9))
* **bigtable:** Eliminate stats-handler MD race in internal/metrics tracer ([#20158](https://github.com/googleapis/google-cloud-go/issues/20158)) ([c387066](https://github.com/googleapis/google-cloud-go/commit/c38706633aa13da88e8c54b0b6340b9ce7209007))

---
## 2026-07-14

### Feature

AI agents can use the [`list_hot_tablets` Model Context Protocol (MCP) tool](https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/bigtable/mcp/tools_list/list_hot_tablets)
to programmatically query Bigtable cluster health to isolate resource-intensive
tablets (hot tablets) and detect overutilized node CPUs. This feature is
[generally available (GA)](https://cloud.google.com/products#product-launch-stages).

---
## 2026-07-09

### Feature

You can use the [Bigtable client library for Go](https://docs.cloud.google.com/bigtable/docs/reference/libraries)
to execute read jobs and queries using [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).

---
## 2026-07-07

### Feature

You can bind existing [tags](https://docs.cloud.google.com/bigtable/docs/tags) to Bigtable instances when you
create an instance and use policies to enforce mandatory tag assignments. This
feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance).

### Feature

The Bigtable agent skill (`bigtable-basics`) is
[generally available (GA)](https://cloud.google.com/products#product-launch-stages)
in the public [Google Agent Skills repository](https://github.com/google/skills/tree/main/skills/cloud/bigtable-basics).
This skill lets you equip AI agents with capabilities for Bigtable tasks, such as
provisioning instances and tables, designing schemas, querying data using
GoogleSQL and key-value APIs, and diagnosing performance issues or hotspots.

### Feature

You can use Organization Policy Service custom constraints to manage specific
operations on continuous materialized views. This feature is [generally available
(GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see [Use custom organization policies](https://docs.cloud.google.com/bigtable/docs/custom-constraints).

---
## 2026-07-06

### Feature

Bigtable supports direct connectivity, which bypasses the Google frontend and
optimizes performance for application traffic that meets certain criteria. For
more information, see [Direct connectivity](https://docs.cloud.google.com/bigtable/docs/performance#direct-connectivity).

---
## 2026-06-24

### Feature

You can create [hot backups](https://docs.cloud.google.com/bigtable/docs/backups#hot-backups)
and modify all backups in Bigtable Studio. For more information, see
[Manage backups](https://docs.cloud.google.com/bigtable/docs/managing-backups).

---
## 2026-06-19

### Feature

You can use the Bigtable Studio explorer to search for all resources except for
authorized views and column families. For more information, see
[Manage your data using Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console).

---
## 2026-05-28

### Feature

As part of Bigtable Enterprise Plus [edition](https://docs.cloud.google.com/bigtable/docs/editions-overview),
you can configure a retention period of up to 365 days for backups. This feature
is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see [Bigtable backups overview](https://docs.cloud.google.com/bigtable/docs/backups).

---
## 2026-05-18

### Feature

You can enable [row-affinity routing](https://docs.cloud.google.com/bigtable/docs/routing#row-affinity) for a
standard app profile in the Google Cloud console. For more information, see
[Create a standard app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#create-standard-app-profile).

---
## 2026-05-07

### Feature

You can use [Aerospike migration tools](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/tree/main/aerospike-bigtable-migration-tools) to migrate data from Aerospike to Bigtable with minimal or zero downtime. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Migrate Aerospike to Bigtable](https://docs.cloud.google.com/bigtable/docs/migrate-aerospike-to-bigtable).

---
## 2026-04-30

### Feature

You can use Bigtable [agent
skills](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem#ai-agent-skills)
to let AI agents assist with Bigtable-related tasks, such as schema design,
generating SQL queries, and infrastructure management.

---
## 2026-04-23

### Feature

You can use window functions with GoogleSQL in Bigtable to perform advanced
analytic operations over multiple table rows.
This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see [Window functions](https://docs.cloud.google.com/bigtable/docs/reference/sql/window-functions).

---
## 2026-04-22

### Feature

The Bigtable editions feature is [generally available
(GA)](https://cloud.google.com/products#product-launch-stages). Bigtable
editions introduces advanced features in performance, analytic query capability,
and resource management. You can choose between the Enterprise and Enterprise
Plus edition to select the right capabilities for your workloads. For more
information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

### Feature

Bigtable provides an in-memory tier as part of its hybrid storage
architecture. This tier provides sub-millisecond read latency and high
throughput for time-sensitive data with independent vertical scaling to handle
traffic surges. The in-memory tier is available only in the Enterprise Plus
[edition](https://docs.cloud.google.com/bigtable/docs/editions-overview) in
[Preview](https://cloud.google.com/products#product-launch-stages). For more
information, see [In-memory tier overview](https://docs.cloud.google.com/bigtable/docs/in-memory-overview).

### Feature

Bigtable [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) limit increases from
32 TB to 64 TB per node. This expansion provides higher storage
density to support retention of larger volumes of infrequently accessed data and
is available only in the Enterprise Plus [edition](https://docs.cloud.google.com/bigtable/docs/editions-overview).
Tiered storage is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

### Feature

As part of Bigtable [editions](https://docs.cloud.google.com/bigtable/docs/editions-overview), you can use
[Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) to read data from tiered
storage and HDD clusters. This feature is available only in the Enterprise Plus
edition and is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

### Feature

As part of Bigtable [editions](https://docs.cloud.google.com/bigtable/docs/editions-overview), you can use
[Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) to run GoogleSQL queries. This
feature is available only in the Enterprise Plus edition and is
[generally available (GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see [High-throughput SQL analysis with Data Boost](https://docs.cloud.google.com/bigtable/docs/googlesql-examples#data-boost-analysis).

### Feature

As part of Bigtable [editions](https://docs.cloud.google.com/bigtable/docs/editions-overview), you can
configure which cluster in a replicated instance is used for automated backups.
This feature provides greater cost control and backup resource management. This
feature is available only in the Enterprise Plus edition and is
[generally available (GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see [Bigtable backups overview](https://docs.cloud.google.com/bigtable/docs/backups).

---
## 2026-04-20

### Feature

You can use the [Database Insights remote MCP server](https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/databaseinsights/mcp)
to analyze Bigtable's performance and system metrics. This feature is
[generally available (GA)](https://cloud.google.com/products#product-launch-stages).

### Feature

Bigtable [continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views)
are [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
These views let you create precomputed tables that Bigtable automatically keeps
in sync with your source data for low-latency queries and real-time insights.

### Feature

Bigtable free trial instances are [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
These instances let you learn and explore Bigtable features for 90 days at no
cost, providing a 1-node SSD cluster and up to 500 GB of storage. For more
information, see [Free trial instances overview](https://docs.cloud.google.com/bigtable/docs/free-trial-instance).

### Feature

The [Bigtable remote MCP server](https://docs.cloud.google.com/bigtable/docs/use-bigtable-mcp) is
[generally available (GA)](https://cloud.google.com/products#product-launch-stages).
The Bigtable remote MCP server lets you interact with Bigtable instances
from LLMs, AI applications, and AI-enabled development platforms.

---
## 2026-04-16

### Feature

You can stream messages from [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/subscription-overview)
directly to a Bigtable table using
[Bigtable subscriptions](https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions). This feature lets
you write streaming messages to Bigtable without needing a separate subscriber
such as Dataflow. This feature is available in
[Preview](https://cloud.google.com/products/#product-launch-stages).

---
## 2026-04-15

### Feature

Dataplex Universal Catalog is now called Knowledge Catalog. The API, client
library, CLI, and Identity and Access Management (IAM) names remain unchanged.
For more information about how Bigtable metadata interacts with Knowledge
Catalog, see [Manage data assets using Knowledge Catalog](https://docs.cloud.google.com/bigtable/docs/manage-data-assets-using-knowledge-catalog).

---
## 2026-04-13

### Feature

You can now use GoogleSQL geography functions to work with geospatial data in Bigtable.
This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see [Work with geospatial data](https://docs.cloud.google.com/bigtable/docs/work-with-geo-data)
and [Geography functions reference](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions).

### Feature

Bigtable supports [pipe syntax](https://docs.cloud.google.com/bigtable/docs/reference/sql/pipe-syntax),
an extension to GoogleSQL that lets you build simpler and more concise queries.
This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

---
## 2026-04-09

### Feature

You can use Gemini in Bigtable Studio to help you write GoogleSQL queries. This
feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).
For more information, see [Write SQL with Gemini assistance](https://docs.cloud.google.com/bigtable/docs/write-sql-gemini).

---
## 2026-04-07

### Feature

You can connect to Bigtable from Java applications and other reporting tools
that support a generic JDBC adapter by using the [Bigtable JDBC driver](https://docs.cloud.google.com/bigtable/docs/reference/jdbc).
This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

### Feature

You can use [protocol buffer (protobuf) schemas](https://docs.cloud.google.com/bigtable/docs/create-manage-protobuf-schemas)
to query individual fields within protobuf messages stored as bytes in Bigtable.
You can query your protobuf data using GoogleSQL for Bigtable, continuous
materialized views, logical views, or BigQuery external tables. This feature is
[generally available (GA)](https://cloud.google.com/products#product-launch-stages).

---
## 2026-03-30

### Feature

You can view the [details of Bigtable continuous materialized views](https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views#view-details)
in the Google Cloud console.

---
## 2026-03-25

### Announcement

Bigtable client for Java has modernized its Admin API. For detailed migration
steps and code examples, see
[Upgrading client libraries](https://docs.cloud.google.com/bigtable/docs/upgrading-clients#java).

---
## 2026-03-24

### Feature

You can manage Bigtable [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage)
configuration in the Google Cloud console and view tiered storage metrics in
[system insights](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-monitoring-resources).
For more information, see [Create and manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables).

---
## 2026-03-06

### Feature

[Bigtable tools in the Agent Development Kit (ADK)](https://google.github.io/adk-docs/integrations/bigtable/)
are [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
With these tools, you can build AI agents that interact with Bigtable to
discover metadata about Bigtable tables and instances and execute LLM-powered
SQL queries.

---
## 2026-02-18

### Feature

You can migrate a machine learning feature management workload from Vertex AI
Feature Store (Legacy) to a Bigtable instance. For more information, see
[Migrate from Vertex AI Feature Store (Legacy) to
Bigtable](https://docs.cloud.google.com/bigtable/docs/migrate-vertex-ai-legacy-bigtable).

### Announcement

New best practices are available for securing generative AI agents using Model
Context Protocol (MCP) with Google Cloud databases. This guide covers key
security measures like least privilege, native database controls, and secure
agent design to help you build safer AI applications. For more information, see
[Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/bigtable/docs/secure-agent-interactions-mcp).

---
## 2026-02-17

### Feature

You can use the [Bigtable Admin API MCP server](https://docs.cloud.google.com/bigtable/docs/use-bigtable-mcp)
to enable agents and AI applications to perform a range of data-related tasks.
This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2026-02-13

### Feature

You can use the [Flink Bigtable connector](https://docs.cloud.google.com/bigtable/docs/flink-connector)
version 0.3.2 to connect to Bigtable from Apache Flink version 2.1.0.
Additionally, this version of the connector lets you specify the number of
mutations to include in each batch sent to Bigtable. This feature is
[generally available (GA)](https://cloud.google.com/products#product-launch-stages).

---
## 2026-02-02

### Libraries

### Java

#### [2.72.0](https://github.com/googleapis/java-bigtable/compare/v2.71.0...v2.72.0) (2026-01-30)

##### Features

* Add GcRuleBuilder for safe GC rule construction ([#2758](https://github.com/googleapis/java-bigtable/issues/2758)) ([4a99a8c](https://github.com/googleapis/java-bigtable/commit/4a99a8ccad8469933b63aa63205bc2c800a24fef))
* Handle StatusRuntimeException in CbtTestProxy, increase inbound message / metadata size ([#2763](https://github.com/googleapis/java-bigtable/issues/2763)) ([3e27d28](https://github.com/googleapis/java-bigtable/commit/3e27d2895816685743ee59d566cd8870447c02f1))
* Regenerate protos using protoc 4

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.66.0 ([ca24007](https://github.com/googleapis/java-bigtable/commit/ca240078ea4400cd071d796259ed4b8c9501a6f6))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.56.0 ([#2765](https://github.com/googleapis/java-bigtable/issues/2765)) ([d1020a1](https://github.com/googleapis/java-bigtable/commit/d1020a1ea1e296273408262a33a09427a20d8156))

---
## 2026-01-30

### Feature

Bigtable has a unified, customizable system insights dashboard. This dashboard
includes predefined metrics and other Google Cloud metrics. This
feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).
For more information, see [Customize the system insights dashboard](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#customize-system-insights).

---
## 2026-01-21

### Feature

Bigtable is available in the `asia-southeast3` (Bangkok) region. For more
information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

---
## 2026-01-19

### Libraries

### Java

#### [2.71.0](https://github.com/googleapis/java-bigtable/compare/v2.70.1...v2.71.0) (2026-01-15)

##### Features

* Add CSM for batch write flow control ([#2685](https://github.com/googleapis/java-bigtable/issues/2685)) ([62ffd1b](https://github.com/googleapis/java-bigtable/commit/62ffd1babb910bc9ef2e83482de9500e3e1a1b4f))

##### Bug Fixes

* **bigtable:** Add handling for gauge metrics ([#2719](https://github.com/googleapis/java-bigtable/issues/2719)) ([87aa4d5](https://github.com/googleapis/java-bigtable/commit/87aa4d54c047d2de1e92d75a4ff69e6d02689bdb))
* Create stub with BigtableClientContext so otels are closed ([#2747](https://github.com/googleapis/java-bigtable/issues/2747)) ([3d0a6d9](https://github.com/googleapis/java-bigtable/commit/3d0a6d9d52bd8a97adafe04ac7d6142b42139e51))
* Update BigtableChannelPool to use the background executor ([#2753](https://github.com/googleapis/java-bigtable/issues/2753)) ([8f6e2df](https://github.com/googleapis/java-bigtable/commit/8f6e2df7bba6fee4e3999dd77b8b18cd85580eff))
* Use the same background executor in otel reader and monitoring c… ([#2746](https://github.com/googleapis/java-bigtable/issues/2746)) ([3a58f9b](https://github.com/googleapis/java-bigtable/commit/3a58f9bebe416186aa8bffee8e024aef135f52c6))

##### Dependencies

* Update dependency com.google.cloud:gapic-libraries-bom to v1.76.0 ([#2754](https://github.com/googleapis/java-bigtable/issues/2754)) ([be54ef6](https://github.com/googleapis/java-bigtable/commit/be54ef69a2c2d506fc84d08a202e1eb3dafaa849))
* Update shared dependencies ([#2752](https://github.com/googleapis/java-bigtable/issues/2752)) ([fe1074c](https://github.com/googleapis/java-bigtable/commit/fe1074cb7631746b5bacee2fb4bbd37e4a96416a))

---
## 2025-12-26

### Feature

Continuous materialized views support up to five continuous materialized views
per table. This lets you create multiple asynchronous secondary indexes on a
table or have a mix of precomputed aggregate views and asynchronous secondary
indexes on the same base table. For more information, see
[Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views).

---
## 2025-12-22

### Libraries

### Python

#### [2.35.0](https://github.com/googleapis/python-bigtable/compare/v2.34.0...v2.35.0) (2025-12-16)

##### Features

* add basic interceptor to client (#1206) ([6561cfac](https://github.com/googleapis/python-bigtable/commit/6561cfac))
* Add encodings for STRUCT and the Timestamp type ([72dfdc44](https://github.com/googleapis/python-bigtable/commit/72dfdc44))
* add PeerInfo proto in Bigtable API ([72dfdc44](https://github.com/googleapis/python-bigtable/commit/72dfdc44))
* Add Type API updates needed to support structured keys in materialized views ([72dfdc44](https://github.com/googleapis/python-bigtable/commit/72dfdc44))
* support mTLS certificates when available (#1249) ([ca20219c](https://github.com/googleapis/python-bigtable/commit/ca20219c))

##### Bug Fixes

* re-export AddToCell for consistency (#1241) ([2a5baf11](https://github.com/googleapis/python-bigtable/commit/2a5baf11))
* async client uses fixed grace period (#1236) ([544db1cd](https://github.com/googleapis/python-bigtable/commit/544db1cd))
* Deprecate credentials\_file argument ([72dfdc44](https://github.com/googleapis/python-bigtable/commit/72dfdc44))
* Add ReadRows/SampleRowKeys bindings for materialized views ([72dfdc44](https://github.com/googleapis/python-bigtable/commit/72dfdc44))
* retry cancelled errors (#1235) ([e3fd5d86](https://github.com/googleapis/python-bigtable/commit/e3fd5d86))

### Java

#### [2.71.0-rc1](https://github.com/googleapis/java-bigtable/compare/v2.70.1...v2.71.0-rc1) (2025-12-19)

##### Features

* update with latest from main ([#2740](https://github.com/googleapis/java-bigtable/issues/2740)) ([90e1a02](https://github.com/googleapis/java-bigtable/commit/90e1a02c46830751a0f158b3a337eb2f926b0ee0))
* feat: Upgrade protobuf gen code to 4.33 ([#2741](https://github.com/googleapis/java-bigtable/issues/2741)) ([2b1d201](https://github.com/googleapis/java-bigtable/commit/2b1d201d56540cdb45b65b4ed2a1c786a519d3a0))

##### Dependencies

* update sdk-platform-java-config to 3.55.0-rc1 ([#2738](https://github.com/googleapis/java-bigtable/issues/2738)) ([136f164](https://github.com/googleapis/java-bigtable/commit/136f16474e7ff147c68e976894070727dfc9add8))

---
## 2025-12-15

### Libraries

### Java

#### [2.70.1](https://github.com/googleapis/java-bigtable/compare/v2.70.0...v2.70.1) (2025-12-12)

##### Dependencies

* Update shared dependencies ([#2734](https://github.com/googleapis/java-bigtable/issues/2734)) ([2823705](https://github.com/googleapis/java-bigtable/commit/28237059edaa20028ea35a1903bdee8c02885260))

---
## 2025-12-12

### Feature

In the Google Cloud console, you can import data into Bigtable using the
[Dataflow job builder](https://docs.cloud.google.com/dataflow/docs/guides/job-builder),
a web interface for building and running Dataflow pipelines. This integration
provides a pre-populated template to import data from Pub/Sub to Bigtable. You
can also create a custom job to import data from other sources. For more
information, see [Import and export data](https://docs.cloud.google.com/bigtable/docs/import-export).

---
## 2025-11-03

### Feature

You can use protocol buffer (protobuf) schemas to query individual fields within protobuf messages stored as bytes in Bigtable. First, [create and manage your protobuf schemas](https://docs.cloud.google.com/bigtable/docs/create-manage-protobuf-schemas). Then, [query your protobuf data](https://docs.cloud.google.com/bigtable/docs/query-protobuf-data) using GoogleSQL for Bigtable or BigQuery external tables. This feature is in [Preview](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages).

---
## 2025-10-28

### Feature

You can use Cloud KMS Autokey in the Google Cloud console to automate the creation and use of [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/bigtable/docs/cmek) in Bigtable clusters.

---
## 2025-10-27

### Feature

Bigtable provides vector and key-value store integrations for LangChain, an LLM orchestration framework.
For more information, see [Build LLM-powered applications using LangChain](https://docs.cloud.google.com/bigtable/docs/langchain) and [Perform Maximal Marginal Relevance search with LangChain on Bigtable](https://docs.cloud.google.com/bigtable/docs/mmr-vector-search).

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.68.0](https://github.com/googleapis/java-bigtable/compare/v2.67.1...v2.68.0) (2025-10-22)

##### Features

* Add Type API updates needed to support structured keys in materialized views ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))

##### Bug Fixes

* Add ReadRows/SampleRowKeys bindings for materialized views ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.62.3 ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))
* **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([ed6c03f](https://github.com/googleapis/java-bigtable/commit/ed6c03ff50f42a06472f5be781b68937f48228d1))
* Don't use String.format in Preconditions messages ([#2691](https://github.com/googleapis/java-bigtable/issues/2691)) ([62a1812](https://github.com/googleapis/java-bigtable/commit/62a18128d8ec65484509dde6cd0c2b0322890cc9))
* Fixed the bigtableadmin API name for snippet region tags and possibly other GAPIC attributes ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))

##### Dependencies

* Update shared dependencies ([#2697](https://github.com/googleapis/java-bigtable/issues/2697)) ([611ad20](https://github.com/googleapis/java-bigtable/commit/611ad208359e3c1f2e675d5e4e8c8ade3616b02b))

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.34.0](https://github.com/googleapis/python-bigtable/compare/v2.33.0...v2.34.0) (2025-10-16)

##### Features

* Add support for Python 3.14 ([#1217](https://github.com/googleapis/python-bigtable/issues/1217)) ([263332a](https://github.com/googleapis/python-bigtable/commit/263332af71a229cb4fa598008a708137086a6f67))

---
## 2025-10-20

### Feature

You can [save queries](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console#save-query) and then [view and manage](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console#view_and_manage_saved_queries) the saved queries in Bigtable Studio. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-13

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.67.1](https://github.com/googleapis/java-bigtable/compare/v2.67.0...v2.67.1) (2025-10-08)

##### Dependencies

* Update shared dependencies ([#2686](https://github.com/googleapis/java-bigtable/issues/2686)) ([d7eaa02](https://github.com/googleapis/java-bigtable/commit/d7eaa02d89a63d9f9197d26e430267eff200b126))

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.33.0](https://github.com/googleapis/python-bigtable/compare/v2.32.0...v2.33.0) (2025-10-06)

##### Features

* Add support for Proto and Enum types ([#1202](https://github.com/googleapis/python-bigtable/issues/1202)) ([34ceb86](https://github.com/googleapis/python-bigtable/commit/34ceb86007db08d453fa25cca4968d5b498ffcd6))
* Expose universe\_domain for tpc ([#1150](https://github.com/googleapis/python-bigtable/issues/1150)) ([451fd97](https://github.com/googleapis/python-bigtable/commit/451fd97e435218ffed47d39423680ffc4feccac4))

##### Bug Fixes

* Fix instance registration cleanup on early iterator termination ([#1216](https://github.com/googleapis/python-bigtable/issues/1216)) ([bbfd746](https://github.com/googleapis/python-bigtable/commit/bbfd746c61a6362efa42c7899ec3e34ceb541c83))
* Refactor channel refresh ([#1174](https://github.com/googleapis/python-bigtable/issues/1174)) ([6fa3008](https://github.com/googleapis/python-bigtable/commit/6fa30084058bc34d4487d1fee5c87d7795ff167a))

---
## 2025-10-07

### Feature

The [Cassandra-Bigtable proxy adapter](https://cloud.google.com/bigtable/docs/migrate-from-cassandra), which lets you connect your Apache Cassandra-based applications to Bigtable, is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

### Feature

You can connect to Bigtable from Java applications and other reporting tools that support a generic JDBC adapter by using the [Bigtable JDBC driver](https://cloud.google.com/bigtable/docs/reference/jdbc). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-10-06

### Feature

You can optimize storage with Bigtable [tiered storage](https://cloud.google.com/bigtable/docs/tiered-storage), reduce storage costs, and retain data for longer. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-29

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.67.0](https://github.com/googleapis/java-bigtable/compare/v2.66.0...v2.67.0) (2025-09-24)

##### Features

* Idle channel eviction ([#2651](https://github.com/googleapis/java-bigtable/issues/2651)) ([70c05c9](https://github.com/googleapis/java-bigtable/commit/70c05c9c09a63c53818384d2a66c622c9b95e00e))
* Load balancing options for BigtableChannelPool ([#2667](https://github.com/googleapis/java-bigtable/issues/2667)) ([5adaa84](https://github.com/googleapis/java-bigtable/commit/5adaa84d80df08779da7c36a50de4632049cfe96))

##### Bug Fixes

* Add missing break; to PROTO and ENUM value type check ([#2672](https://github.com/googleapis/java-bigtable/issues/2672)) ([337e432](https://github.com/googleapis/java-bigtable/commit/337e4325f6cb5d11309ec5f33550d47d97cbe3c3))
* Remove beta api annotation for query paginator ([#2660](https://github.com/googleapis/java-bigtable/issues/2660)) ([f68a1fa](https://github.com/googleapis/java-bigtable/commit/f68a1fae49b701d1fb9942e2af2fa84a1e5b508a))

##### Dependencies

* Update shared dependencies ([#2679](https://github.com/googleapis/java-bigtable/issues/2679)) ([a5b8260](https://github.com/googleapis/java-bigtable/commit/a5b82609c365ae4792ed822e59039c1a046ef3ff))

---
## 2025-09-15

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [6.4.1](https://github.com/googleapis/nodejs-bigtable/compare/v6.4.0...v6.4.1) (2025-09-09)

##### Bug Fixes

* Directly import JS-native impl for crc32c on non-x64 platforms to avoid segfault ([#1715](https://github.com/googleapis/nodejs-bigtable/issues/1715)) ([9848963](https://github.com/googleapis/nodejs-bigtable/commit/98489637befe779df0438f466eecb0428222a29a))

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.66.0](https://github.com/googleapis/java-bigtable/compare/v2.65.1...v2.66.0) (2025-09-10)

##### Features

* Add support for Proto and Enum types ([#2662](https://github.com/googleapis/java-bigtable/issues/2662)) ([da3065d](https://github.com/googleapis/java-bigtable/commit/da3065db331be191fdf9e06be71e45c7832574ea))

##### Dependencies

* Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#2668](https://github.com/googleapis/java-bigtable/issues/2668)) ([06ac93e](https://github.com/googleapis/java-bigtable/commit/06ac93e810830f9c04920b488d9a10af8995a6f3))

---
## 2025-09-01

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.65.1](https://github.com/googleapis/java-bigtable/compare/v2.65.0...v2.65.1) (2025-08-27)

##### Dependencies

* Update shared dependencies ([#2664](https://github.com/googleapis/java-bigtable/issues/2664)) ([841318b](https://github.com/googleapis/java-bigtable/commit/841318b2248dcda89d8482bc2e84c838bd8be8d0))

---
## 2025-08-28

### Announcement

Bigtable tools are available in [Agent Development Kit (ADK)](https://google.github.io/adk-docs/). With these tools, you can build AI agents that can interact with Bigtable data and metadata in the following ways:

* Obtain metadata about Bigtable tables and instances.
* Execute LLM-powered SQL queries.

---
## 2025-08-25

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [6.4.0](https://github.com/googleapis/nodejs-bigtable/compare/v6.3.0...v6.4.0) (2025-08-21)

##### Features

* Enable csm by default ([#1695](https://github.com/googleapis/nodejs-bigtable/issues/1695)) ([9744aa3](https://github.com/googleapis/nodejs-bigtable/commit/9744aa355e87c2170019c52b58d1045160f19e7c))
* For application latencies timed stream a few cosmetic changes are needed ([#1645](https://github.com/googleapis/nodejs-bigtable/issues/1645)) ([75d1a6f](https://github.com/googleapis/nodejs-bigtable/commit/75d1a6f5bc8d8cd74214bdf3c9db9d06786f9575))

---
## 2025-08-18

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [6.3.0](https://github.com/googleapis/nodejs-bigtable/compare/v6.2.0...v6.3.0) (2025-08-11)

##### Features

* Add client side metrics for checkAndMutateRow calls ([#1661](https://github.com/googleapis/nodejs-bigtable/issues/1661)) ([c258ea1](https://github.com/googleapis/nodejs-bigtable/commit/c258ea1b29203aad3eaaf9cfe64ddabb8c1018bf))
* Add client side metrics for readModifyWriteRow calls ([#1656](https://github.com/googleapis/nodejs-bigtable/issues/1656)) ([2129312](https://github.com/googleapis/nodejs-bigtable/commit/2129312401bf9f5b8e51b13ac576cb765de401df))
* Client side metrics support for mutateRows ([#1638](https://github.com/googleapis/nodejs-bigtable/issues/1638)) ([7601e4d](https://github.com/googleapis/nodejs-bigtable/commit/7601e4da115ff6a5da411cc857917b579c70ced7))
* Collect client side metrics for sampleRowKeys calls ([#1660](https://github.com/googleapis/nodejs-bigtable/issues/1660)) ([6ed98fa](https://github.com/googleapis/nodejs-bigtable/commit/6ed98faefe446e67f83fd5394aae30374fd3ec3a))
* For client side metrics, record metrics as MUTATE\_ROW for single row mutates ([#1650](https://github.com/googleapis/nodejs-bigtable/issues/1650)) ([f190a8c](https://github.com/googleapis/nodejs-bigtable/commit/f190a8c322498ddfbe73406759a43a268c16bdc4))
* Record ReadRows application latencies for client side metrics ([#1647](https://github.com/googleapis/nodejs-bigtable/issues/1647)) ([8af801b](https://github.com/googleapis/nodejs-bigtable/commit/8af801b3ecd7ff5e30e6c8cc67bd4123bdf34ee9))

##### Bug Fixes

* FirstResponseLatencies should only be collected for readRows calls ([#1658](https://github.com/googleapis/nodejs-bigtable/issues/1658)) ([99cf5a6](https://github.com/googleapis/nodejs-bigtable/commit/99cf5a6010249ed0eedd88f23b2d32cacb106c07))

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.65.0](https://github.com/googleapis/java-bigtable/compare/v2.64.0...v2.65.0) (2025-08-12)

##### Features

* **bigtable:** Lower the value for max rpc channels as channel resize is slow (1m, 2 channel) ([#2656](https://github.com/googleapis/java-bigtable/issues/2656)) ([d8055c1](https://github.com/googleapis/java-bigtable/commit/d8055c1fb75a616cda1503b92d7cddb9da47d42b))

---
## 2025-08-11

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.64.0](https://github.com/googleapis/java-bigtable/compare/v2.63.0...v2.64.0) (2025-08-08)

##### Features

* Add tags field to Instance proto (stable branch) ([089d527](https://github.com/googleapis/java-bigtable/commit/089d52700c225015fabfaa763163c5874b96d830))

##### Dependencies

* Update shared dependencies ([#2654](https://github.com/googleapis/java-bigtable/issues/2654)) ([4b706f4](https://github.com/googleapis/java-bigtable/commit/4b706f4f76a8152556aa99656b440adb30f37a4c))
* Update the Java code generator (gapic-generator-java) to 2.61.0 ([089d527](https://github.com/googleapis/java-bigtable/commit/089d52700c225015fabfaa763163c5874b96d830))

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.32.0](https://github.com/googleapis/python-bigtable/compare/v2.31.0...v2.32.0) (2025-08-01)

##### Features

* Add Idempotency to Cloud Bigtable MutateRowsRequest API ([#1143](https://github.com/googleapis/python-bigtable/issues/1143)) ([c3e3eb0](https://github.com/googleapis/python-bigtable/commit/c3e3eb0e4ce44ece72b150dc5822846627074fba))
* Add support for AddToCell in Data Client ([#1147](https://github.com/googleapis/python-bigtable/issues/1147)) ([1a5b4b5](https://github.com/googleapis/python-bigtable/commit/1a5b4b514cadae5c83d61296314285d3774992c5))
* Implement SQL support in test proxy ([#1106](https://github.com/googleapis/python-bigtable/issues/1106)) ([7a91bbf](https://github.com/googleapis/python-bigtable/commit/7a91bbfb9df23f7e93c40b88648840342af6f16f))
* Modernized Bigtable Admin Client featuring selective GAPIC generation ([#1177](https://github.com/googleapis/python-bigtable/issues/1177)) ([58e7d37](https://github.com/googleapis/python-bigtable/commit/58e7d3782df6b13a42af053263afc575222a6b83))

---
## 2025-08-04

### Announcement

You can add the [Cassandra to Bigtable client for Java](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/blob/main/cassandra-bigtable-migration-tools/cassandra-bigtable-java-client/cassandra-bigtable-java-client-lib/README.md) library to your Java project from the Maven Central repository.

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.63.0](https://github.com/googleapis/java-bigtable/compare/v2.62.0...v2.63.0) (2025-07-30)

##### Features

* Add Idempotency to Cloud Bigtable MutateRowsRequest API ([bc58b4f](https://github.com/googleapis/java-bigtable/commit/bc58b4f31ef457bd322f270b044735e4b62d298f))
* Add port as a parameter for the Bigtable emulator ([#2645](https://github.com/googleapis/java-bigtable/issues/2645)) ([5acd3dc](https://github.com/googleapis/java-bigtable/commit/5acd3dc01c36072bd28248d560c5d923c34b1817))
* Add type support for Proto and Enum ([bc58b4f](https://github.com/googleapis/java-bigtable/commit/bc58b4f31ef457bd322f270b044735e4b62d298f))
* Publish Proto and Enum types to CBT data API ([ace12d5](https://github.com/googleapis/java-bigtable/commit/ace12d53fe9f4d3779b2b1a2aed69ceeedd11600))
* Selective GAPIC autogeneration for Python Bigtable Admin ([e219c38](https://github.com/googleapis/java-bigtable/commit/e219c387487673869fb8bb55a5060bdc9d37bbcb))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([e219c38](https://github.com/googleapis/java-bigtable/commit/e219c387487673869fb8bb55a5060bdc9d37bbcb))
* Update routing\_parameters.path\_template ([e219c38](https://github.com/googleapis/java-bigtable/commit/e219c387487673869fb8bb55a5060bdc9d37bbcb))

##### Dependencies

* Update sdk-platorm-java-config to 3.50.2 ([#2646](https://github.com/googleapis/java-bigtable/issues/2646)) ([03e6961](https://github.com/googleapis/java-bigtable/commit/03e6961e758a9a0c39cb168c73c853328c14bfd1))

##### Documentation

* Sync generated comments from the API Protos ([bc58b4f](https://github.com/googleapis/java-bigtable/commit/bc58b4f31ef457bd322f270b044735e4b62d298f))

---
## 2025-07-31

### Feature

[Logical views](https://cloud.google.com/bigtable/docs/create-manage-logical-views) for Bigtable are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Logical views let you save a SQL query as a specific, shareable view of your data—even with a flexible schema—and then control who has permission to see the results.

---
## 2025-07-28

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [6.2.0](https://github.com/googleapis/nodejs-bigtable/compare/v6.1.0...v6.2.0) (2025-07-23)

##### Features

* Add client-side metrics collection to readRows calls ([#1571](https://github.com/googleapis/nodejs-bigtable/issues/1571)) ([71f4d78](https://github.com/googleapis/nodejs-bigtable/commit/71f4d78422137c88f1521be45004982367dbda31))
* Add plumbing to support unary calls for client side metric collection ([#1631](https://github.com/googleapis/nodejs-bigtable/issues/1631)) ([c267ede](https://github.com/googleapis/nodejs-bigtable/commit/c267ede0140aa29bc75feada93899a4945980375))
* Add support for Execute Query ([#1613](https://github.com/googleapis/nodejs-bigtable/issues/1613)) ([e3894ed](https://github.com/googleapis/nodejs-bigtable/commit/e3894edf4fc881153432f77ce976141397dc0348))
* Initial timed stream implementation for application latencies ([#1639](https://github.com/googleapis/nodejs-bigtable/issues/1639)) ([ca490e8](https://github.com/googleapis/nodejs-bigtable/commit/ca490e80f2359156475e52c5f72fe0a9fe8e9740))

##### Bug Fixes

* In client-side metrics, make sure that the right views get created for the right metrics ([#1590](https://github.com/googleapis/nodejs-bigtable/issues/1590)) ([6cb7cdd](https://github.com/googleapis/nodejs-bigtable/commit/6cb7cddf42ff1fe29b2ae4a729739bc12c3d4942))

---
## 2025-07-21

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.62.0](https://github.com/googleapis/java-bigtable/compare/v2.61.0...v2.62.0) (2025-07-15)

##### Features

* Add Idempotency to Cloud Bigtable MutateRowRequest API ([b5acca6](https://github.com/googleapis/java-bigtable/commit/b5acca6ac4f1eec420adb27bc77aa1bda0ec2dca))
* Add SchemaBundles API ([b5acca6](https://github.com/googleapis/java-bigtable/commit/b5acca6ac4f1eec420adb27bc77aa1bda0ec2dca))
* **bigtable:** Add schema bundle support ([#2619](https://github.com/googleapis/java-bigtable/issues/2619)) ([7d7b9a9](https://github.com/googleapis/java-bigtable/commit/7d7b9a966d3ef7b7a0ef3f82038ab73f4d791427))
* Next release from main branch is 2.62.0 ([#2621](https://github.com/googleapis/java-bigtable/issues/2621)) ([202b211](https://github.com/googleapis/java-bigtable/commit/202b21102e71da71ff56f19a12d8a00a59cd8107))

##### Dependencies

* Minor cleanup ([#2623](https://github.com/googleapis/java-bigtable/issues/2623)) ([7b230e8](https://github.com/googleapis/java-bigtable/commit/7b230e86902b5733c06e45fad90da76653ee1096))
* Update shared dependencies ([#2616](https://github.com/googleapis/java-bigtable/issues/2616)) ([eb7cfd5](https://github.com/googleapis/java-bigtable/commit/eb7cfd526aa999c614b7b8285d32759e2739ff9a))

---
## 2025-07-07

### Changed

When you [undelete a table](https://cloud.google.com/bigtable/docs/managing-tables#undelete-table), Bigtable automatically enables deletion protection for that table.

---
## 2025-06-30

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.61.0](https://github.com/googleapis/java-bigtable/compare/v2.60.0...v2.61.0) (2025-06-27)

##### Features

* Add getter for universe domain in JwtCredentialsWithAudience ([#2598](https://github.com/googleapis/java-bigtable/issues/2598)) ([9ad66b1](https://github.com/googleapis/java-bigtable/commit/9ad66b129923500cdeb794fc2e4570ad8b1d92fd))

##### Bug Fixes

* Add name elements for the pom.xml files ([a873719](https://github.com/googleapis/java-bigtable/commit/a873719e7e32a0cd21dc259911a193520f20797e))
* Populate table ID for materialized view ([#2610](https://github.com/googleapis/java-bigtable/issues/2610)) ([50c3fe2](https://github.com/googleapis/java-bigtable/commit/50c3fe2ffe66acaba8cb408dc3b1a4d13a4a2556))

##### Dependencies

* Update shared dependencies ([#2605](https://github.com/googleapis/java-bigtable/issues/2605)) ([4cc7246](https://github.com/googleapis/java-bigtable/commit/4cc7246ff8e2e0e26d2edc0aee8866a32ec1c8ab))

---
## 2025-06-24

### Feature

You can use [Data Boost](https://cloud.google.com/bigquery/docs/create-bigtable-external-table#compute) to analyze your Bigtable data with BigQuery without impacting the performance of the clusters that handle your application traffic. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

---
## 2025-06-09

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.60.0](https://github.com/googleapis/java-bigtable/compare/v2.59.0...v2.60.0) (2025-06-06)

##### Features

* Improve error message on malformed struct ([#2592](https://github.com/googleapis/java-bigtable/issues/2592)) ([7f5fdf0](https://github.com/googleapis/java-bigtable/commit/7f5fdf094c5fe140807ce6abcea0b891462ba809))
* Run ExecuteQuery conformance tests ([#2557](https://github.com/googleapis/java-bigtable/issues/2557)) ([0bbc083](https://github.com/googleapis/java-bigtable/commit/0bbc083b9e798e5b557f3ffe7090b45e66c9ada5))

##### Bug Fixes

* **deps:** Update the Java code generator (gapic-generator-java) to 2.59.0 ([65782aa](https://github.com/googleapis/java-bigtable/commit/65782aaf89ad78aafd7f5928e81e513c3016b471))
* Ensure that multiple instances of a client in the same process don't clobber each other ([#2590](https://github.com/googleapis/java-bigtable/issues/2590)) ([8d3dca4](https://github.com/googleapis/java-bigtable/commit/8d3dca43224179829829bcf91972610c666b130b))

##### Dependencies

* Update shared dependencies ([#2587](https://github.com/googleapis/java-bigtable/issues/2587)) ([8ec0339](https://github.com/googleapis/java-bigtable/commit/8ec033994f20b2b3aea0dfcdaffbdd1c6d19fdad))

---
## 2025-06-02

### Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [6.1.0](https://github.com/googleapis/nodejs-bigtable/compare/v6.0.0...v6.1.0) (2025-05-30)

##### Features

* Add full support for the universe domain ([#1604](https://github.com/googleapis/nodejs-bigtable/issues/1604)) ([4562e23](https://github.com/googleapis/nodejs-bigtable/commit/4562e2329e734c0c9d9f00cfa83aa2be13e9a7fe))

---
## 2025-05-29

### Changed

The [Bigtable Spark connector](https://cloud.google.com/bigtable/docs/use-bigtable-spark-connector) supports Scala versions 2.12 and 2.13 in all connector versions and has been updated as follows:

* Connector versions 0.5.0 and later support [dynamic columns](https://github.com/GoogleCloudDataproc/spark-bigtable-connector?tab=readme-ov-file#catalog-with-variable-column-definitions).
* Connector versions 0.6.0 and later support [custom authentication providers](https://github.com/GoogleCloudDataproc/spark-bigtable-connector/?tab=readme-ov-file#how-do-i-authenticate-outside-gce--dataproc) and [efficient joins with data sources](https://github.com/GoogleCloudDataproc/spark-bigtable-connector/?tab=readme-ov-file#efficient-joins-with-other-data-sources).

---
## 2025-05-27

### Announcement

You can delete logical and continuous materialized views in the Google Cloud console. For more information, see [Delete a logical view](https://cloud.google.com/bigtable/docs/create-manage-logical-views#delete) or [Delete a continuous materialized view](https://cloud.google.com/bigtable/docs/manage-continuous-materialized-views#delete).

---
