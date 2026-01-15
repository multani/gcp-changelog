# Storage Transfer Service

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
