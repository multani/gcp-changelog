# Cloud Profiler

## 2026-10-29

### Security

The Cloud Profiler Java agent is updated with a new Certification Authority (CA)
certificate bundle, in response to security bulletin
[GCP-2026-071](https://docs.cloud.google.com/support/bulletins#gcp-2026-071). Google Cloud infrastructure and
the Cloud Profiler backend service are not affected.

If you use the Cloud Profiler Java agent, take one of the following
actions:

* Upgrade the Java agent to `cloud-profiler-java-agent_20261026_RC00`
  ([GitHub release v0.5.0](https://github.com/GoogleCloudPlatform/cloud-profiler-java/releases/tag/v0.5.0))
  or later, and then rebuild and redeploy your applications. Download the
  updated archive,
  <https://storage.googleapis.com/cloud-profiler/java/cloud-profiler-java-agent_20261026_RC00.tar.gz>,
  or, for `musl`-based Alpine Linux containers,
  <https://storage.googleapis.com/cloud-profiler/java/cloud-profiler-java-agent_20261026_RC00_alpine.tar.gz>.
* If you can't immediately upgrade or rebuild, update your host or container
  operating system's CA certificate store as described in
  [GCP-2026-071](https://docs.cloud.google.com/support/bulletins#gcp-2026-071), and then set the
  `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable to point to the
  updated PEM bundle.

For more information about installing the agent, see
[Profiling Java applications](https://docs.cloud.google.com/profiler/docs/profiling-java#installing-profiler).

---
