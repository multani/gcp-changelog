# 571.0.0 (2026-06-02)

## 2026-06-02

### Google Cloud CLI

* Updated Windows PuTTY executables to version 0.83.
  + This includes a fix for the issue reported at
    <https://issuetracker.google.com/issues/515628403>.
* Fixed issue where `gcloud compute scp` file transfers were extremely slow when
  using `--tunnel-through-iap` in PY 3.14.

### AlloyDB

* Added flag `--labels` to `gcloud alloydb instances create|create-secondary` commands to assign labels to an instance.
* Added flags `--update-labels`, `--remove-labels`, and `--clear-labels` to `gcloud alloydb instances update` commands to update, remove, or clear labels for an instance.

### BigLake

* Promoted `gcloud biglake hive tables` to beta.

### Cloud Dataproc

* Added `--confidential-compute-type` flag to `gcloud dataproc clusters create` to allow specifying the Confidential Computing technology (e.g., `SEV`, `SEV_SNP`, `TDX`).
* Deprecated `--confidential-compute` flag for `gcloud dataproc clusters create`. Use `--confidential-compute-type` flag instead.

### Cloud Datastream

* Added `--sql-where-clause` flag to `gcloud datastream objects start-backfill`,
  which starts a partial backfill on the specified object.

### Cloud NetApp

* Added `gcloud netapp volumes start-split` and `get-split-status` commands to alpha and beta tracks of the volumes group.
* Added `gcloud netapp storage-pool update-backup-config` command to GA track.
* Added `--ontap-source` flag to `gcloud netapp backup-vaults backups create` GA track.
* Added `gcloud netapp storage-pools list-backup-configs` command to the GA track of the `storage-pools` group.
* Added `gcloud netapp storage-pools restore-volume` command to GA track.

### Cloud Run

* Added regional endpoint support for `gcloud beta run worker-pools` and
  `gcloud beta run jobs executions tasks` commands.
  Specify `--endpoint-mode=regional` or `--endpoint-mode=regional-preferred` to
  make API requests with regional endpoints.

### Cloud SQL

* Updated 'cloud-sql-proxy' packaged component to use 2.22.0 of the Cloud SQL
  Proxy.

### Cloud Storage

* Added `--set-object-acls-from-file` flag to `gcloud storage batch-operations jobs create`.

### Compute Engine

* Promoted `--source-machine-image` and `--source-machine-image-disk-device-name` flags for `gcloud compute disks create` in beta.

### Network Security

* Promoted project scoping for `gcloud network-security security-profiles` commands (`delete`, `describe`, `export`, `import`, `list`) to GA.
* Promoted project scoping for `gcloud network-security security-profiles custom-intercept` commands (`create`, `delete`, `describe`, `list`, `update`) to GA.
* Promoted project scoping for `gcloud network-security security-profiles custom-mirroring` commands (`create`, `delete`, `describe`, `list`, `update`) to GA.
* Promoted project scoping for
  `gcloud network-security security-profiles threat-prevention` commands
  (`add-override`, `create`, `delete`, `delete-override`, `describe`, `list`,
  `list-overrides`, `update-override`) to GA.
* Promoted project scoping for
  `gcloud network-security security-profiles url-filtering` commands
  (`create`, `delete`, `describe`, `list`) to GA.
* Promoted project scoping for
  `gcloud network-security security-profile-groups` commands
  (`create`, `delete`, `describe`, `list`, `update`) to GA.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
