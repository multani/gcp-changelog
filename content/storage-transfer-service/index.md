# Storage Transfer Service

## 2026-09-21

### Feature

Storage Transfer Service now supports filtering Amazon S3 source objects by storage
class. You can specify a list of storage classes to include when creating or
updating transfer jobs using the Google Cloud console, the `gcloud` CLI, or the
REST API.

For more information, see
[Filter source objects by storage class](https://docs.cloud.google.com/storage-transfer/docs/filtering-by-storage-class).

### Feature

Storage Transfer Service now supports filtering source objects using glob patterns
with wildcard characters such as `*` and `?`. Glob filtering is supported for
transfers from Amazon S3 and Microsoft Azure Blob Storage when configuring transfer jobs using
the `gcloud` CLI or the REST API.

For more information, see
[Filter source objects using wildcards](https://docs.cloud.google.com/storage-transfer/docs/filter-by-glob-pattern).

---
## 2026-05-08

### Feature

Storage Transfer Service now supports AWS GovCloud (US) regions, including
`us-gov-east-1` and `us-gov-west-1`. You can now transfer data from Amazon S3
buckets located in GovCloud regions using both batch and event-driven
transfers.

For more information, see [Configure access to a source: Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3)
and [Event-driven transfers from AWS S3](https://docs.cloud.google.com/storage-transfer/docs/event-driven-aws).

---
## 2026-03-09

### Change

The size limit for manifest files used in agent-based transfers has been removed.

For more information, see
[Transfer specific files or objects using a manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest).

---
## 2026-02-02

### Feature

Organization Policy Service custom constraints are now available for
Storage Transfer Service. You can use custom constraints to control how
Storage Transfer Service is used in your organization. For example, you can restrict
transfers to only allow Cloud Storage to Cloud Storage transfers, or
restrict transfers to a specific list of approved source buckets.

See
[Custom organization policy constraints](https://docs.cloud.google.com/storage-transfer/docs/custom-constraints)
for details.

---
## 2026-01-14

### Feature

Storage Transfer Service event-driven transfers are now available for Azure Blob
Storage and Data Lake Storage Gen2 sources. Event-driven transfers listen
to Azure Event Grid notifications via Azure Storage Queues to automatically
transfer new or updated objects from your Azure container to
Cloud Storage.

For more information, see
[Event-driven transfers from Azure Blob Storage or Data Lake Storage Gen2](https://docs.cloud.google.com/storage-transfer/docs/event-driven-azure).

---
## 2025-12-02

### Feature

You can now transfer data from AWS S3 or Azure Blob Storage to Cloud Storage
over a private network connection, using Cross-Cloud Interconnect or
Partner Interconnect. Transferring data over a private connection can
optimize costs, provide dedicated bandwidth, and help meet compliance needs by
keeping data off the public internet.

See [Transfer from AWS or Azure over a customer-managed private
network](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/customer-managed-private-network)
for details.

---
