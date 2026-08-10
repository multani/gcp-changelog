# Managed Service for Apache Airflow

## 2026-08-05

### Change

*(Airflow 3.2.2, 3.1.8, and 2.11.1)*
The `apache-airflow-providers-google` package was upgraded to version 22.2.2.
For more information about changes, see the
[apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html).

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Managed Airflow (Gen 3):

* [composer-3-airflow-3.2.2-build.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-2-2-build-1)
* [composer-3-airflow-3.1.8-build.3](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-8-build-3)
* [composer-3-airflow-2.11.1-build.14](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-14) (default)
* [composer-3-airflow-2.10.5-build.47](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-47)

These builds are versions with an extended upgrade timeline.

### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Managed Airflow (Gen 2):

* [composer-2.17.9-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-9-airflow-2-11-1) (default)
* [composer-2.17.9-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-9-airflow-2-10-5)

These images are versions with an extended upgrade timeline.

### Deprecated

The following Managed Airflow versions and builds have reached their
[end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):
composer-3-airflow-2.10.5-build.11, composer-3-airflow-2.9.3-build.31, composer-2.13.9-airflow-2.9.3, and composer-2.13.9-airflow-2.10.5.

---
## 2026-07-29

### Feature

**Airflow 3.2.2** is available in Managed Airflow (Gen 3).

### Change

*(Airflow 3.2.2)* The
[Multi-Team](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/multi-team.html)
Airflow feature isn't available. The `[core]multi_team` Airflow configuration
option is set to `False` and it isn't possible to override it.

### Fixed

*(Airflow 3.2.2)* Backported
[#69877](https://github.com/apache/airflow/pull/69877) to restore the ability
to deliver failure and retry alerts through a pluggable email backend
(configured through the `[email]email_backend` Airflow configuration option).

### Change

*(Managed Airflow Gen 3 with Airflow 2)* Default triggerer resources are
changing to 1 vCPU and 2 GB memory to match Airflow 3 defaults. This change is
available in the Google Cloud CLI, Terraform, and Cloud Composer API and is
gradually rolling out in the Google Cloud console.

### Fixed

A correct error message is now generated when an environment creation request
fails because of malformed network and subnetwork identifiers.

### Fixed

*(Available without upgrading)* The correct default task priority weight of `1`
is now shown for tasks in the Google Cloud console.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Managed Airflow (Gen 3):

* [composer-3-airflow-3.2.2-build.0](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-2-2-build-0)
* [composer-3-airflow-3.1.8-build.2](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-8-build-2)
* [composer-3-airflow-2.11.1-build.13](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-13) (default)
* [composer-3-airflow-2.10.5-build.46](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-46)

### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Managed Airflow (Gen 2):

* [composer-2.17.8-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-8-airflow-2-11-1) (default)
* [composer-2.17.8-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-8-airflow-2-10-5)

### Deprecated

The following Managed Airflow versions and builds have reached their
[end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):
composer-3-airflow-2.10.5-build.10, composer-3-airflow-2.9.3-build.30,
composer-2.13.8-airflow-2.9.3, and composer-2.13.8-airflow-2.10.5.

---
## 2026-07-24

### Announcement

Starting in September, 2026, **Airflow 2.10.5 will no longer be included** in
new Managed Airflow images and builds. This change will not affect existing
images and builds.

### Announcement

Starting in September 2026, we are changing the version support policy for
Managed Airflow (Gen 2) to align it with the Managed Airflow (Gen 3) policy.
The changes will **affect Airflow 2 versions that we release**:

* In Managed Airflow (Gen 2), we will
  **release only new images with Airflow 2.11**. New Airflow 2.10.5 images
  will no longer be released.
* In Managed Airflow (Gen 3) we will keep releasing new builds of Airflow 3
  (no changes) and will release only new Airflow 2.11 builds. New
  Airflow 2.10.5 builds will no longer be released.

---
## 2026-07-16

### Feature

**Airflow 3.1.8** is available in Managed Airflow (Gen 3).

### Change

Airflow 3.1.7 is no longer included in Managed Airflow images and builds.

### Fixed

*(Airflow 3.1.8)* Backported
[#64031](https://github.com/apache/airflow/pull/64031) to fix an issue in
the Airflow UI when viewing tasks in non-terminal states (scheduled, running)
with "Show Gantt" enabled.

### Change

*(Airflow 3.1.8)* The `apache-airflow-providers-google` package was upgraded to version 22.2.0.
For more information about changes, see the
[apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html).

### Change

*(Airflow 2.11.1)* The `apache-airflow-providers-google` package was upgraded to version 22.2.1.
For more information about changes, see the
[apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html).

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Managed Airflow (Gen 3):

* [composer-3-airflow-3.1.8-build.0](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-8-build-0)
* [composer-3-airflow-2.11.1-build.11](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-11) (default)
* [composer-3-airflow-2.10.5-build.44](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-44)

### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Managed Airflow (Gen 2):

* [composer-2.17.7-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-7-airflow-2-11-1) (default)
* [composer-2.17.7-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-7-airflow-2-10-5)

### Deprecated

The following Managed Airflow versions and builds have reached their
[end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):
composer-3-airflow-2.10.5-build.9, composer-3-airflow-2.9.3-build.29,
composer-2.13.7-airflow-2.9.3, composer-2.13.7-airflow-2.10.5.

---
## 2026-07-13

### Issue

In Managed Airflow (Gen 3) builds with Airflow 2.11.1 starting from
[composer-3-airflow-2.11.1-build.7](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-7),
the Airflow web server requires at least 3 GB of memory (the default amount of
memory for a Small environment preset is 4 GB).

If the Airflow web server has less than 3 GB of memory, it might experience
intermittent out-of-memory (OOM) issues. To resolve these issues,
[increase the web server memory](https://docs.cloud.google.com/composer/docs/composer-3/scale-environments#web-server-parameters)
to at least 3 GB.

---
## 2026-07-07

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Managed Airflow (Gen 3):

* [composer-3-airflow-3.1.7-build.13](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-13)
* [composer-3-airflow-2.11.1-build.9](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-9) (default)
* [composer-3-airflow-2.10.5-build.42](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-42)

### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Managed Airflow (Gen 2):

* [composer-2.17.6-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-6-airflow-2-11-1) (default)
* [composer-2.17.6-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-6-airflow-2-10-5)

### Deprecated

The following Managed Airflow versions and builds have reached their
[end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):
composer-3-airflow-2.9.3-build.28, composer-3-airflow-2.10.5-build.0,
composer-3-airflow-2.10.5-build.2, composer-3-airflow-2.10.5-build.3,
composer-3-airflow-2.10.5-build.4, composer-3-airflow-2.10.5-build.5,
composer-3-airflow-2.10.5-build.6, composer-3-airflow-2.10.5-build.7,
composer-3-airflow-2.10.5-build.8, composer-2.13.6-airflow-2.9.3,
and composer-2.13.6-airflow-2.10.5.

---
## 2026-06-29

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Managed Airflow (Gen 3):

* [composer-3-airflow-3.1.7-build.12](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-12)
* [composer-3-airflow-2.11.1-build.8](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-8) (default)
* [composer-3-airflow-2.10.5-build.41](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-41)

### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Managed Airflow (Gen 2):

* [composer-2.17.5-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-5-airflow-2-11-1) (default)
* [composer-2.17.5-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-5-airflow-2-10-5)

---
## 2026-06-26

### Change

The `apache-airflow-providers-google` package was upgraded to version 22.1.0.
For more information about changes, see the
[apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html).

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Managed Airflow (Gen 3):

* [composer-3-airflow-3.1.7-build.11](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-11)
* [composer-3-airflow-2.11.1-build.7](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-7) (default)
* [composer-3-airflow-2.10.5-build.40](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-40)

### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Managed Airflow (Gen 2):

* [composer-2.17.4-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-4-airflow-2-11-1) (default)
* [composer-2.17.4-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-4-airflow-2-10-5)

### Deprecated

The following Managed Airflow versions and builds have reached their
[end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):
composer-3-airflow-2.9.3-build.25, composer-3-airflow-2.9.3-build.26,
composer-3-airflow-2.9.3-build.27, composer-2.13.3-airflow-2.9.3,
composer-2.13.4-airflow-2.9.3, composer-2.13.5-airflow-2.9.3,
composer-2.13.3-airflow-2.10.5, composer-2.13.4-airflow-2.10.5,
composer-2.13.5-airflow-2.10.5.

---
## 2026-06-12

### Feature

New Managed Airflow (Gen 2) environments created while the Restrict Endpoint
Usage organization policy is active now use regional endpoints for services
like Cloud Storage, Cloud Logging, Pub/Sub, and Data Lineage. For more
information, see
[Configure environments with Restrict Endpoint Usage policy](https://docs.cloud.google.com/composer/docs/composer-2/configure-restrict-endpoint-usage-environments).

---
## 2026-06-08

### Change

Several API dependencies that aren't required by Managed Airflow (Gen 3) are
now phased out and must be enabled separately if you want to create
Managed Airflow (Gen 2) environments in a new project. This change was
[announced previously](https://docs.cloud.google.com/composer/docs/release-notes#June_16_2025).

The following API dependencies were phased out:

* artifactregistry.googleapis.com
* cloudbuild.googleapis.com
* container.googleapis.com
* pubsub.googleapis.com

The following API dependencies aren't phased out yet and are scheduled to be
detached from the Cloud Composer API in the future:

* sqladmin.googleapis.com

Existing Managed Airflow (Gen 3) and Managed Airflow (Gen 2) environments in
projects where the Cloud Composer API is already enabled aren't impacted.

You can do the following:

* If your project has only Managed Airflow (Gen 3) environments, then you can
  manually disable the listed APIs that were phased out.
* If your project has Managed Airflow (Gen 2) environments, then we recommend
  to keep these APIs enabled because disabling them might lead to environment's malfunction.
* If you want to create Managed Airflow (Gen 2) environments in a new project,
  you can enable the listed APIs manually or using a Google Cloud CLI
  command. For more information, see
  [Enable Managed Airflow (Gen 2) dependencies](https://docs.cloud.google.com/composer/docs/composer-2/enable-composer-service#enable-gen-2-dependencies).
* If you use automation scripts to provision Managed Airflow (Gen 2)
  environments, then make sure that the listed APIs are enabled in addition
  to the Cloud Composer API.

---
## 2026-06-02

### Feature

*(Managed Airflow Gen 3)* You can now
[access Cloud Run endpoints restricted to internal ingress traffic](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network#cloud-run-traffic)
through your environment's network attachment. This feature is available
through gcloud CLI beta commands and beta Cloud Composer API in all Managed
Airflow (Gen 3) versions.

---
## 2026-05-27

### Feature

Managed Service for Apache Airflow now
[supports Google Cloud tags](https://docs.cloud.google.com/composer/docs/composer-3/create-and-manage-tags)
for environments.

[Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview)
provide a way to create annotations for resources, and conditionally allow or
deny policies based on whether a resource has a specific tag.

### Feature

In Managed Airflow (Gen 3), it is now possible to
create Kubernetes Secrets with the `kubernetes.io/dockerconfigjson`
[secret type](https://kubernetes.io/docs/concepts/configuration/secret/#secret-types)
through the beta Cloud Composer API, in addition to the default
`Opaque` secret type. For more information, see [Manage Kubernetes Secrets](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator#api).

### Fixed

(Airflow 3) The INFO log level filter in Airflow UI now correctly displays log
messages with this logging level.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Managed Airflow (Gen 3):

* [composer-3-airflow-3.1.7-build.10](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-10)
* [composer-3-airflow-2.11.1-build.6](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-6) (default)
* [composer-3-airflow-2.10.5-build.39](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-39)

### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Managed Airflow (Gen 2):

* [composer-2.17.3-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-3-airflow-2-11-1) (default)
* [composer-2.17.3-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-3-airflow-2-10-5)

### Deprecated

The following Managed Airflow versions and builds have reached their
[end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):
composer-3-airflow-2.9.3-build.24, composer-2.13.2-airflow-2.9.3,
composer-2.13.2-airflow-2.10.5.

---
## 2026-05-14

### Change

The `[scheduler]print_stats_interval` Airflow configuration option can now be
overridden in environments with Airflow 2.10.5 and later. This option
previously was blocked.

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Managed Airflow (Gen 3):

* [composer-3-airflow-3.1.7-build.9](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-9)
* [composer-3-airflow-2.11.1-build.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-5) (default)
* [composer-3-airflow-2.10.5-build.38](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-38)

### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Managed Airflow (Gen 2):

* [composer-2.17.2-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-2-airflow-2-11-1) (default)
* [composer-2.17.2-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-2-airflow-2-10-5)

### Deprecated

The following Managed Airflow versions and builds have reached their
[end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):
composer-3-airflow-2.9.3-build.23, composer-3-airflow-2.10.5-build.3, and composer-2.13.1-airflow-\*.

### Issue

The `google-api-core` preinstalled package versions from 2.28.0 to 2.30.2 might
cause degraded environment performance, which can result in longer times to
execute a task and longer times to move a task from the queued to the executing
state.

Affected Managed Airflow (Gen 3) builds:

* composer-3-airflow-3.1.7-build.0 to composer-3-airflow-3.1.7-build.5
* composer-3-airflow-3.1.0-build.5 to composer-3-airflow-3.1.0-build.10
* composer-3-airflow-2.11.1-build.0
* composer-3-airflow-2.10.5-build.22 to composer-3-airflow-2.10.5-build.33
* composer-3-airflow-2.9.3-build.42 to composer-3-airflow-2.9.3-build.53

Affected Managed Airflow (Gen 2) builds:

* composer-2.16.10-airflow-2.11.1
* composer-2.16.0-airflow-2.10.5 to composer-2.16.10-airflow-2.10.5
* composer-2.16.0-airflow-2.9.3 to composer-2.16.10-airflow-2.9.3

We recommend to upgrade your environment to the following versions, which
contain a version of the package where the problem is fixed or isn't present:

* composer-3-airflow-3.1.7-build.7 and later
* composer-3-airflow-2.11.1-build.3 and later
* composer-3-airflow-2.10.5-build.36 and later
* composer-3-airflow-2.9.3-build.54 (contains 2.27.0)
* composer-2.17.0-airflow-2.11.1 and later
* composer-2.17.0-airflow-2.10.5 and later
* composer-2.16.11-airflow-2.11.1 (contains 2.27.0)
* composer-2.16.11-airflow-2.10.5 (contains 2.27.0)
* composer-2.16.11-airflow-2.9.3 (contains 2.27.0)

As a workaround, you can manually install a later version of the
`google-api-core` package to an affected environment by specifying `>=2.30.3`
as the required version.

---
## 2026-05-11

### Change

New [Airflow builds](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Managed Airflow (Gen 3):

* [composer-3-airflow-3.1.7-build.8](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-3-1-7-build-8)
* [composer-3-airflow-2.11.1-build.4](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-11-1-build-4) (default)
* [composer-3-airflow-2.10.5-build.37](https://docs.cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-37)

### Change

New [images](https://docs.cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Managed Airflow (Gen 2):

* [composer-2.17.1-airflow-2.11.1](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-1-airflow-2-11-1) (default)
* [composer-2.17.1-airflow-2.10.5](https://docs.cloud.google.com/composer/docs/versions-packages#composer-2-17-1-airflow-2-10-5)

### Deprecated

The following Managed Airflow versions and builds have reached their
[end of support period](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):
composer-3-airflow-2.9.3-build.22 and composer-2.13.0-airflow-\*.

---
