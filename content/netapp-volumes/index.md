# NetApp Volumes

## 2025-12-19

### Feature

Google Cloud NetApp Volumes supports Customer Managed Encryption Keys (CMEK) for
backup in allow-listed General Availability (GA). This feature is available for
Standard, Premium, and Extreme service levels. For more information, see
[Backup encryption with CMEK](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#backup_encryption_with_cmek).

### Feature

Google Cloud NetApp Volumes supports prepopulation and write-back for FlexCache.
For more information, see [Cache prepopulation](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#cache_prepopulation)
and [Write-back](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#write-back).

---
## 2025-11-21

### Announcement

Google Cloud NetApp Volumes offers volume replication between the following
region pairs for Standard, Premium, and Extreme service levels:

* `europe-west4` (Netherlands) and `europe-west6` (Zurich)

For more information, see [About volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication).

---
## 2025-11-12

### Feature

Google Cloud NetApp Volumes supports the all-squash feature for NFS exports.
This option lets you enhance security by mapping all client user IDs to a single
anonymous user ID (`UID=65534`). For more information, see [User ID
squashing](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients#user_id_squashing).

---
## 2025-11-06

### Feature

Google Cloud NetApp Volumes supports the block storage feature with iSCSI
protocol in allow-listed General Availability (GA) for the Flex service level of
the **Unified** type. For more information, see
[Block storage](https://docs.cloud.google.com/netapp/volumes/docs/discover/features#block_storage).

---
## 2025-10-01

### Feature

The manual QoS feature is now generally available for Google Cloud NetApp Volumes, supporting the Standard, Premium, and Extreme service levels. For more information, see [Manual QoS](https://docs.cloud.google.com/netapp/volumes/docs/performance/optimize-performance#manual_qos).

---
## 2025-09-26

### Feature

Selective file restore feature is now generally available for Google Cloud NetApp Volumes, supporting the Standard, Premium, and Extreme service levels. For more information, see [Selective file restore](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#selective_file_restore).

---
## 2025-09-24

### Feature

Google Cloud NetApp Volumes now supports the FlexCache feature in allow-listed General Availability (GA) for the Premium and Extreme service levels. For more information, see [FlexCache](https://cloud.google.com/netapp/volumes/docs/discover/features#flexcache).

---
## 2025-09-05

### Feature

The auto-tiering feature for the Flex service level is now generally available for custom-performance Flex zonal pools. For more information, see [Manage auto-tiering](https://cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering).

---
## 2025-08-25

### Feature

Google Cloud NetApp Volumes now supports the external replication feature in allow-listed General Availability (GA) for Standard, Premium, and Extreme service levels. This feature uses bi-directional SnapMirror to replicate data between ONTAP-based systems and NetApp Volumes. For more information, see [About external replication](https://cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview#about_external_replication).

---
## 2025-08-19

### Changed

Large capacity volumes now support a maximum capacity of 3 PiB. For more information, see [Large capacity volumes](https://cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#large-capacity-volumes).

---
## 2025-08-07

### Changed

For the Flex service level, the storage pool and volume now support a maximum capacity of 300 TiB. For more information, see [Service levels](https://cloud.google.com/netapp/volumes/docs/discover/service-levels).

---
## 2025-07-31

### Feature

Google Cloud NetApp Volumes now supports organization policy for Customer Managed Encryption Keys (CMEK). For more information, see [CMEK organization policy](https://cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/cmek-overview#cmek_organization_policy).

---
## 2025-07-29

### Feature

Google Cloud NetApp Volumes is now integrated with NetApp BlueXP Connector. For more information, see [NetApp Volumes integration with BlueXP](https://cloud.google.com/netapp/volumes/docs/discover/features#netapp-volumes-integration-with-bluexp).

---
## 2025-07-25

### Feature

Google Cloud NetApp Volumes now supports cross-project cross-region replication for Standard, Premium, and Extreme service levels. This feature is generally available for allow-listed users. For more information, see [About volume replication](https://cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication).

### Feature

Google Cloud NetApp Volumes now supports volume backups for large capacity volumes. This feature is now generally available. For more information, see [About backups](https://cloud.google.com/netapp/volumes/docs/protect-data/about-backups).

---
## 2025-07-22

### Feature

Google Cloud NetApp Volumes now supports multi-VPC peering for all service levels. For more information, see [Connect additional networks](https://cloud.google.com/netapp/volumes/docs/get-started/quickstarts/connect-additional-networks).

---
