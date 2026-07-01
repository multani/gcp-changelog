# Managed Service for Apache Airflow

## 2026-06-26

### Announcement

A new Managed Service for Apache Airflow release has started on **June 26, 2026**. Get ready
for upcoming changes and features as we roll out the new release to all regions.
This release is in progress at the moment. Listed changes and features might
not be available in some regions yet.

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
