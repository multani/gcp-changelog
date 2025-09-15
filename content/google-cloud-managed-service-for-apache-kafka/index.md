# Google Cloud Managed Service for Apache Kafka

## 2025-09-09

### Feature

General availability: You can now use mutual TLS (mTLS) for certificate-based authentication with your Managed Service for Apache Kafka brokers. This feature is available for clusters created after June 24, 2025. For more information, see [Authentication types for Kafka brokers](https://cloud.google.com/managed-service-for-apache-kafka/docs/authn-types-kafka).

---
## 2025-09-04

### Feature

Integration with [VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_managed_kafka) is in [preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-09-02

### Feature

Managed Service for Apache Kafka now supports [HIPAA Compliance on Google Cloud](https://cloud.google.com/security/compliance/hipaa).

---
## 2025-07-15

### Feature

The Google Cloud Managed Service for Apache Kafka service creates new brokers automatically based on the memory and vCPU configuration of the cluster. When you update a cluster's size, the service now performs a safety check to verify that individual brokers have sufficient capacity for their portion of the traffic. For more information, see [Update the memory and vCPUs](https://cloud.google.com/managed-service-for-apache-kafka/docs/update-cluster#update-memory-vCPUs).

---
## 2025-07-09

### Feature

General availability: Metrics for all Google Cloud Managed Service for Apache Kafka resources are now available, with some exceptions. Exceptions include the `request_count` and `topic_error_count` metrics for Kafka clusters and Kafka Connect connectors. For a list of supported metrics, see [Metrics for Cloud Managed Service for Apache Kafka](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-managedkafka).

---
## 2025-05-29

### Feature

Public preview: Google Managed Service for Apache Kafka now offers schema registry support. For more information about the feature, see the [schema registry overview](https://cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-registry-overview) or [get started with an Avro producer in Java](https://cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-avro).

---
