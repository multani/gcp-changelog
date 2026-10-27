# 591.0.0 (2026-10-27)

## 2026-10-27

### Breaking Changes

* **(Google Cloud CLI)** Fixed issue where `gcloud components update` on macOS was stuck and would exit
  immediately after printing "WARNING: Known issue encountered updating Python
  modules", preventing updates to the latest release.
  + However, because this issue is present in the 590.0.0 and 590.0.1 releases,
    existing installations currently at those versions still contain the bug,
    and affected users will need to perform a one-time workaround to become
    unstuck.
  + This can be achieved by running:
    `gcloud components --flags-file=<(echo 'update:')`
  + Users updating from version <=589.0.0 or >=591.0.0 are unaffected and can
    run `gcloud components update` as normal; the workaround is only needed for
    installations currently stuck at version 590.0.0 or 590.0.1.
  + This issue can be tracked at
    <https://issuetracker.google.com/issues/578071727>.

### Google Cloud CLI

* Updated bundled Python to 3.14.9.

### Agent Registry

* Promoted `gcloud agent-registry skills`, `gcloud agent-registry skills revisions`, `gcloud agent-registry publishers`, and `gcloud agent-registry findings` command groups to GA.

### App Engine

* Updated `gcloud beta app migrate-to-run` to mask environment variable
  values in the printed `service.yaml`. The saved `service.yaml` file keeps
  the original values.

### Audit Manager

* Added `gcloud audit-manager audit-schedules describe` command to describe an audit schedule.

### Beyondcorp

* Added `--dispatch-info-output-type` flag to
  `gcloud beyondcorp security-gateways create` and
  `gcloud beyondcorp security-gateways update`, and upstream
  `dispatchInfo` configuration to
  `gcloud beyondcorp security-gateways applications create` and
  `gcloud beyondcorp security-gateways applications update`
  to configure delegated dispatch info headers.

### BigQuery

* Updated the bundled `certifi` package to version `2026.10.19` and removed
  the distrusted `AAA Certificate Services` root certificate from bundled
  `httplib2`.

### Cloud Bigtable

* Added `--timestamp-granularity` flag to `gcloud bigtable instances tables
  create` and `gcloud bigtable tables create` to configure table timestamp
  granularity (`millis` or `micros`). Microsecond granularity is supported
  only on Enterprise Plus instances.
* Rebuild with 1.26.9 for CVE-2026-94439.

### Cloud DNS

* Updated `gcloud beta dns outbound-endpoints create` to make `--endpoint-ip` flag optional.

### Cloud Dataproc

* Promoted `--master-flexible-config`, `--worker-flexible-config`, and
  `--secondary-worker-flexible-config` flags to GA for `gcloud dataproc
  clusters create` and `gcloud dataproc workflow-templates
  set-managed-cluster`.
* Promoted `--worker-flexible-config` and `--secondary-worker-flexible-config`
  flags to GA for `gcloud dataproc clusters update`.

### Cloud IAM

* Added `--discovery-uri` flag to `gcloud iam workload-identity-pools
  providers create-oidc` and `gcloud iam workload-identity-pools providers
  update-oidc` to specify a custom OIDC discovery URI when the identity
  provider does not use the default well-known path.
* Added `--actor-providers` flag to `gcloud iam workload-identity-pools
  providers create-oidc` and `gcloud iam workload-identity-pools providers
  update-oidc` to authorize providers in the same pool to issue actor tokens
  for identity delegation.

### Cloud Memorystore

* Promote `gcloud redis clusters` basic auth feature related commands to GA track.

### Cloud Spanner Emulator

* Updated cloud spanner emulator to v1.5.59.

### Cloud Storage

* Added `--labels` and `--labels-file` flags to `gcloud storage buckets
  create`.

### Compute Engine

* Promoted `--identity-type` flag to the beta and GA tracks for `gcloud compute instances create`, `gcloud compute instances update`, and `gcloud compute instance-templates create`.
* Added circuit breakers flags (`--circuit-breakers-max-connections`,
  `--circuit-breakers-max-pending-requests`,
  `--circuit-breakers-max-requests`,
  `--circuit-breakers-max-requests-per-connection`,
  `--circuit-breakers-max-retries`) to `gcloud compute backend-services
  create` and `update` commands, and `--no-circuit-breakers` to the `update`
  command.
* Added colorization for `ACTION`, `HEALTH_STATE`, and `STATUS` columns to
  `gcloud compute instance-groups managed list-instances` in beta and GA.
* Added `--circuit-breakers-connect-timeout` flag to `gcloud compute
  backend-services create` and `update` commands in beta.
* Added `--allowed-actions` flag to `gcloud beta compute instance-groups
  managed update-instances` to specify allowed actions (including
  `restart-in-place`) when updating instances in a managed instance group.
* Added `--update-policy-allowed-actions` flag to `gcloud beta compute
  instance-groups managed create` and `gcloud beta compute instance-groups
  managed update` to specify allowed actions (including `restart-in-place`) in
  a managed instance group's update policy.

### Database Migration

* Added `--ai-processing-location` flag to
  `gcloud database-migration conversion-workspaces create|update` to set
  the location where Gemini features process conversion workspace data. Pass an
  empty value to remove a previously set location.

### GKE Hub

* Promoted `--prioritized` flag on
  `gcloud container fleet|hub rolloutsequences upgrade` command to `GA`.
* Promoted `gcloud container fleet|hub config-management update` command to
  `GA`.

### Kubernetes Engine

* Added flag `--node-config-update-mode` to
  `gcloud container node-pools update` to trigger live update on nodes.
  Supported values are `LIVE_UPDATE_WITHOUT_DRAIN`.

### Network Connectivity

* Added `--group` flag to `gcloud beta network-connectivity transports create`
  to specify the group of the Network Connectivity Center hub that the spokes
  created for this transport should be attached to.

### Network Security

* Promoted `add-override`, `update-override`, `delete-override`,
  `add-inline-ml-exception` and `delete-inline-ml-exception` commands of
  `gcloud network-security security-profiles wildfire-analysis` to GA.
* Promoted WildFire-related flags in
  `gcloud network-security firewall-endpoints create` and
  `gcloud network-security firewall-endpoints update` commands to GA.
* Promoted `gcloud network-security server-tls-policies create` to GA.
* Promoted `gcloud network-security server-tls-policies update` to GA.
* Added `--wildfire-analysis-profile-project` flag to
  `gcloud network-security security-profile-groups update` to support
  project-scoped WildFire Analysis profiles.
* Fixed an issue where
  `gcloud network-security security-profiles wildfire-analysis` modification
  commands failed when specifying a full resource URI without
  `--location=global`.
* Removed `--async` flag from `gcloud beta network-security firewall-endpoints
  wildfire-verdict-change-requests create`. The command now returns the created
  verdict change request directly because the API does not return a
  long-running operation.
* Promoted
  `gcloud network-security firewall-endpoints wildfire-verdict-change-requests`
  command group and its `create`, `get` and `list` commands to GA.

### Secure Source Manager

* Promoted the following command groups to beta:
  + `gcloud beta source-manager branch-rules`
  + `gcloud beta source-manager hooks`
  + `gcloud beta source-manager issues`
  + `gcloud beta source-manager issues comments`
  + `gcloud beta source-manager pull-requests`
  + `gcloud beta source-manager pull-requests comments`

### Workspace Key Access

* Added `gcloud beta workspace-key-access` command group to manage Workspace
  Key Access endpoints, configs, and operations.

Subscribe to these release notes at <https://groups.google.com/forum/#!forum/google-cloud-sdk-announce>.

---
