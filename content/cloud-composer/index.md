# Cloud Composer

## 2025-09-30

### Announcement

A new Cloud Composer release has started on **September 30, 2025**. Get ready
for upcoming changes and features as we roll out the new release to all regions.
This release is in progress at the moment. Listed changes and features might
not be available in some regions yet.

### Fixed

The `GCE_METADATA_TIMEOUT` environment variable is changed to reserved. This
change addresses an issue where setting a low timeout value disrupted the
environment's operations that relied on the metadata server.

### Fixed

DAG UI now correctly generates error messages about malformed serialized DAG.

### Changed

*(Airflow 2.10.5)* The `apache-airflow-providers-google` package was upgraded
to version 17.2.0 in Cloud Composer 2 images and Cloud Composer 3 builds.

For more information about changes, see the
[apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html) from version 17.1.0 to
version 17.2.0.

### Issue

*(Airflow 2.10.5)* CloudComposerDAGRunSensor is broken in the
`apache-airflow-providers-google` package version 17.2.0. This package is used
by Cloud Composer versions and builds with Airflow 2.10.5 available in this
release. If your DAGs use this sensor, we recommend you postpone upgrading
until the issue is resolved.

### Changed

*(Airflow 2.10.5)* The `apache-airflow-providers-cncf-kubernetes` package was
[upgraded to version 10.8.0](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/changelog.html)
from version 10.7.0. For changes in other packages, see the
[preinstalled packages changelog](https://cloud.google.com/composer/docs/versions-packages).

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.15](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-15) (default)
* [composer-3-airflow-2.9.3-build.35](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-35)

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Cloud Composer 2:

* [composer-2.14.4-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-14-4-airflow-2-10-5) (default)
* [composer-2.14.4-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-14-4-airflow-2-9-3)

### Deprecated

The following Cloud Composer versions and builds have reached their
[end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):
composer-2.9.4-\*, and composer-3-airflow-2.9.1 builds from build.0 to build.7.

---
## 2025-09-11

### Fixed

Fixed Airflow logs not exporting to Cloud Logging because of a GKE version
mismatch between Airflow worker and GKE Control plane nodes.

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.14](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-14) (default)
* [composer-3-airflow-2.9.3-build.34](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-34)

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Cloud Composer 2:

* [composer-2.14.2-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-14-2-airflow-2-10-5) (default)
* [composer-2.14.2-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-14-2-airflow-2-9-3)

### Fixed

Fixed an issue where values of Airflow configuration options were evaluated
before being set. As a result, the actual value was set to the evaluated result.

---
## 2025-09-03

### Feature

*(Cloud Composer 2)* Cloud Composer's high availability infrastructure was
enhanced to provide greater resilience against zonal outages. This change rolls
out gradually over several releases to all regions supported by
Cloud Composer 2.

### Feature

*(Available without upgrading)* Cloud Composer 3 now supports DNS resolution
for
[regional service endpoints](https://cloud.google.com/vpc/docs/regional-service-endpoints).
You can now reach regional service endpoints from
DAGs in your environment. This change is available in Public IP environments
without additional configuration. For Private IP environments, an environment
must be
[connected to a VPC network](https://cloud.google.com/composer/docs/composer-3/connect-vpc-network)
where private endpoints are configured.

### Feature

You can now check if a Cloud Composer 2 environment's configuration
[is compatible with Cloud Composer 3](https://cloud.google.com/composer/docs/composer-2/upgrade-environments#major-version-upgrade).
We recommend doing this check before migrating to Cloud Composer 3.

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.13](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-13) (default)
* [composer-3-airflow-2.9.3-build.33](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-33)

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Cloud Composer 2:

* [composer-2.14.1-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-14-1-airflow-2-10-5) (default)
* [composer-2.14.1-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-14-1-airflow-2-9-3)

### Deprecated

The following Cloud Composer versions and builds have reached their
[end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):
composer-2.9.2-\* and composer-2.9.3-\*.

---
## 2025-08-21

### Feature

Improved the startup times of Airflow workers for environments that have a
large number of custom PyPI packages installed.

This feature was
[announced previously](https://cloud.google.com/composer/docs/release-notes#June_02_2025)
and has finished gradually rolling out to all regions supported by
Cloud Composer.

### Fixed

Airflow UI now shows the correct value of the `[core]dags_folder` Airflow
configuration option.

### Changed

*(Airflow 2.10.5)* The `apache-airflow-providers-google` package was upgraded to version 17.1.0 in Cloud Composer 2 images and Cloud Composer 3 builds.

For more information about changes, see the [apache-airflow-providers-google changelog](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/changelog.html) from version 15.1.0 to version 17.1.0.

### Changed

*(Airflow 2.10.5)* The `apache-airflow-providers-cncf-kubernetes` package was [upgraded to version 10.7.0](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/changelog.html) from version 10.6.1. For changes in other packages, see the [preinstalled packages changelog](https://cloud.google.com/composer/docs/versions-packages).

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.12](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-12) (default)
* [composer-3-airflow-2.9.3-build.32](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-32)

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Cloud Composer 2:

* [composer-2.14.0-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-14-0-airflow-2-10-5) (default)
* [composer-2.14.0-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-14-0-airflow-2-9-3)

### Deprecated

The following Cloud Composer versions and builds have reached their
[end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support):
composer-2.9.0, composer-2.9.1, and composer-3-airflow-2.7.3 builds from build.5 to build.13.

---
## 2025-08-05

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Cloud Composer 2:

* [composer-2.13.9-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-9-airflow-2-10-5) (default)
* [composer-2.13.9-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-9-airflow-2-9-3)

### Deprecated

Cloud Composer versions 2.8.7 and 2.8.8 have reached their
[end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support).

### Changed

*(Cloud Composer 2)* Moved the `update_fab_perms` option from `[webserver]` to
`[fab]` in the Airflow configuration. The corresponding deprecation warning is
no longer generated in Airflow web server logs.

### Feature

*(Airflow 2.10.5 only)* Added task-level resource consumption
[Airflow metrics](https://cloud.google.com/composer/docs/composer-3/monitor-environments)
to Cloud Composer.

* `composer.googleapis.com/workflow/task/cpu_usage`: percentage of CPU used by
  a task.
* `composer.googleapis.com/workflow/task/cpu_usage`: percentage of memory used
  by a task.

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.11](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-11) (default)
* [composer-3-airflow-2.9.3-build.31](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-31)

---
## 2025-07-28

### Fixed

Fixed an issue that caused unexpected restarts of Airflow component workloads
in the environment's cluster.

### Fixed

*(Cloud Composer 3)* The `DAGS_FOLDER` reserved environment variable now
correctly points to the local directory where DAG files are stored.

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3)
are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.10](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-10) (default)
* [composer-3-airflow-2.9.3-build.30](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-30)

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2)
are available in Cloud Composer 2:

* [composer-2.13.8-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-8-airflow-2-10-5) (default)
* [composer-2.13.8-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-8-airflow-2-9-3)

### Deprecated

Cloud Composer version 2.8.6 has reached its
[end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support).

---
## 2025-07-24

### Feature

[Web server restarting](https://cloud.google.com/composer/docs/composer-3/access-airflow-web-interface#restarting)
is is now generally available (GA) in Cloud Composer 2 and Cloud Composer 3.

---
## 2025-07-23

### Announcement

If your environment uses `dag-factory` package version 0.22, then you might
experience DAG failures in Cloud Composer versions that have
`apache-airflow-providers-cncf-kubernetes` package version 10.4.2 or later. At
the same time, upgrading the `dag-factory` package to version 0.23 might require
you to update your DAG code to make it compatible.

If your environment uses `dag-factory` version 0.22, we recommend to do the
following:

* Temporarily postpone upgrading your environment until you're ready to switch
  to `dag-factory` version 0.23. Last versions of Cloud Composer that support
  version 0.22 are composer-3-airflow-2.10.5-build.3,
  composer-3-airflow-2.9.3-build.23, composer-2.13.1-airflow-2.10.5, and
  composer-2.13.1-airflow-2.9.3 released on May 14, 2025.
* When you are ready to upgrade, update your DAGs for compatibility with 0.23.
  We recommend to do this in a development environment first.
  [Install](https://cloud.google.com/composer/docs/composer-3/install-python-dependencies)
  `dag-factory` version 0.23, then check that your DAGs are parsed and are
  working correctly, and update them if needed. After your DAGs are
  compatible, install `dag-factory` version 0.23 in your production
  environment and transfer the updated DAGs. Your environment can now be
  upgraded to a later version of Cloud Composer or Airflow.
* If your environment is already upgraded to a later version of Cloud Composer
  and you experience problems, then update `dag-factory` to version 0.23 and
  update your DAGs for compatibility with 0.23.

---
## 2025-07-17

### Feature

[Highly resilient environments](https://cloud.google.com/composer/docs/composer-3/set-up-highly-resilient-environments) are now generally available (GA) in Cloud Composer 3.

---
## 2025-07-14

### Changed

We're changing the way we provide support dates for Airflow builds in Cloud Composer 3. Before this change, some Airflow builds had their end of support date listed as "To be announced" until a later Airflow version became available. We're deprecating this approach for all builds that are released after July 01, 2025.

We are now providing support dates that depend on a date when a particular Airflow build was released:

* We are introducing the [standard support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support) of 12 months after the release date.
* All Airflow builds that didn't have an end of support date when this change was introduced are supported until July 1, 2026. Because of this change, some Airflow builds released before July 1, 2025 are supported for longer than the standard support period.
* All Airflow builds that had their support date shorter than 12 months are now supported for 12 months since the date of their initial release.
* All builds released after July 1, 2025 will use the standard support period.

---
## 2025-07-09

### Announcement

A new Cloud Composer release has started on **July 9, 2025**. Get ready for upcoming changes and features as we roll out the new release to all regions. This release is in progress at the moment. Listed changes and features might not be available in some regions yet.

### Changed

We are gradually rolling out a change that **switches the default version** from Cloud Composer 2 to Cloud Composer 3 in the Cloud Composer API.

In regions where the change is rolled out, a Cloud Composer 3 environment is created by default when a version is not specified in Google Cloud CLI, Cloud Composer API, or Terraform. If you use automation scripts to provision Cloud Composer 2 environments, make sure that you explicitly specify a Cloud Composer 2 version.

In this release, the change is rolling out in the following regions: africa-south1, asia-northeast2, asia-south2, asia-southeast2, europe-southwest1, europe-west10, europe-west12, europe-west8, me-central1, me-central2, me-west1, southamerica-west1, and us-south1.

### Changed

*(Available without upgrading)* During Cloud Composer 2 environment operations, a more informative error message is returned when an environment's web server has connectivity issues.

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.9](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-9) (default)
* [composer-3-airflow-2.9.3-build.29](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-29)

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

* [composer-2.13.7-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-5-airflow-2-10-5) (default)
* [composer-2.13.7-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-5-airflow-2-9-3)

### Deprecated

Cloud Composer versions 2.8.4 and 2.8.5 have reached their [end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support).

---
## 2025-07-02

### Changed

Cloud Composer 1 and Cloud Composer 2 environments with version 2.0.x are **approaching their end of life**. We're planning to deprecate them in the following way:

* Starting **September 15, 2025**, you will no longer be able to create new Cloud Composer 1 environments.
* On **September 15, 2026**, all Cloud Composer 1 and Cloud Composer 2 version 2.0.x environments will reach their planned end of life, and you **won't be able to use them**.

Cloud Composer 2 environments with versions later than 2.1.0 and all Cloud Composer 3 environments are not affected by this deprecation.

We recommend planning
[migration to Cloud Composer 3](https://cloud.google.com/composer/docs/latest/migrate-composer-1-to-3)
or upgrading your Cloud Composer 2 environments to a later version.

---
## 2025-07-01

### Announcement

A new Cloud Composer release has started on **July 1, 2025**. This release is in progress at the moment. Listed changes might not be available in some regions yet.

### Changed

This release includes internal infrastructure improvements to Cloud Composer. There are no user-visible changes.

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.8](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-8) (default)
* [composer-3-airflow-2.9.3-build.28](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-28)

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

* [composer-2.13.6-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-5-airflow-2-10-5) (default)
* [composer-2.13.6-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-5-airflow-2-9-3)

---
## 2025-06-23

### Feature

Improved the startup times of Airflow workers for environments that have a large number of custom PyPI packages installed.

This feature [was announced previously](https://cloud.google.com/composer/docs/release-notes#June_02_2025) and is gradually rolling out over several releases. In this release, it's available in asia-east2, asia-northeast3, europe-central2, europe-west9, me-central1, me-west1, northamerica-northeast1, northamerica-northeast2, northamerica-south1, and us-west1 re

### Fixed

*(Available without upgrading)* Fixed an issue where deleting a Cloud Composer 2 environment could fail when the environment's cluster was in the process of creating a node pool.

### Changed

*(Airflow 2.10.5)* The `apache-airflow-providers-cncf-kubernetes` package was [upgraded to version 10.5.0](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/changelog.html) from version 10.4.2. For changes in other packages, see the [preinstalled packages changelog](https://cloud.google.com/composer/docs/versions-packages).

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.7](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-7) (default)
* [composer-3-airflow-2.9.3-build.27](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-27)

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

* [composer-2.13.5-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-5-airflow-2-10-5) (default)
* [composer-2.13.5-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-5-airflow-2-9-3)

### Deprecated

Cloud Composer version 2.8.3 has reached its [end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support).

---
## 2025-06-16

### Announcement

We're planning to phase out the APIs that aren't required by Cloud Composer 3.

* Starting **February 27, 2026**, the following APIs will **become fully detachable**. Deactivating these APIs won't cause the deactivation of the Cloud Composer API:

  + artifactregistry.googleapis.com
  + cloudbuild.googleapis.com
  + container.googleapis.com
  + pubsub.googleapis.com
  + sqladmin.googleapis.com
* Starting **May 27, 2026**, these APIs **will no longer be enabled automatically** when you enable the Cloud Composer API. To create Cloud Composer 2 environments in new projects, the group of detached APIs must be enabled manually.

Existing Cloud Composer 3 and Cloud Composer 2 environments in projects where the Cloud Composer API is already enabled will not be impacted. You can do the following:

* After **February 27, 2026**, if your project has only Cloud Composer 3 environments, then you can manually disable the detached APIs.
* After **February 27, 2026**, if your project has Cloud Composer 2 environments, then we recommend keeping these APIs enabled because disabling them might lead to environment's malfunction.
* After **May 27, 2026**, if you use automation scripts to provision Cloud Composer 2 environments, then make sure that the listed APIs are enabled in addition to the Cloud Composer API.

---
## 2025-06-13

### Feature

Cloud Composer pages in the Cloud Console now support the dark color theme. You can switch to the dark theme on the [Appearance page](https://console.cloud.google.com/user-preferences/appearance) in the Cloud Console.

---
## 2025-06-10

### Announcement

A new Cloud Composer release has started on **June 10, 2025**. Get ready for upcoming changes and features as we roll out the new release to all regions. This release is in progress at the moment. Listed changes and features might not be available in some regions yet.

### Fixed

Fixed an issue that caused Airflow worker and scheduler Pods to be evicted when a large number of tasks was executed.

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.6](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-6) (default)
* [composer-3-airflow-2.9.3-build.26](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-26)

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

* [composer-2.13.4-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-4-airflow-2-10-5) (default)
* [composer-2.13.4-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-4-airflow-2-9-3)

### Deprecated

Cloud Composer version 2.8.2 has reached its [end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support).

---
## 2025-06-02

### Feature

Improved the startup times of Airflow workers for environments that have a large number of custom PyPI packages installed.

This change rolls out gradually. In this release, it's available in asia-east1, asia-northeast2, asia-south1, europe-north1, europe-west3, us-east1, us-south1, and us-west2 regions.

### Changed

*(Cloud Composer 3)* If a VPC network is attached to an environment, then all DNS addresses accessed by the Airflow components of the environment are resolved using the Cloud DNS configuration of the VPC network. In particular, Airflow workers that execute DAGs will resolve DNS addresses in this way.

### Changed

*(Cloud Composer 3)* All newly created private DNS zones are immediately visible to a Cloud Composer environment. Previously, re-attaching a VPC network was required.

### Fixed

*(Cloud Composer 3)* It's now possible to use [zones with cross-project binding](http://cloud.google.com/dns/docs/zones/cross-project-binding). Before this change, cross-project bound zones weren't supported in Cloud Composer 3.

### Changed

*(Cloud Composer 2)* In Cloud Composer versions 2.11.5 and later, log processing is switching to using OpenTelemetry instead of Fluentd.

This change was [announced previously](https://cloud.google.com/composer/docs/release-notes#May_14_2025) and is gradually rolling out over several releases. In this release, it's available in the following regions: asia-east1, asia-east2, asia-northeast2, asia-northeast3, asia-south2, asia-southeast2, australia-southeast1, australia-southeast2, europe-central2, europe-north1, europe-north2, europe-southwest1, europe-west, europe-west10, europe-west12, europe-west6, europe-west8, europe-west9, me-central1, me-central2, me-west1, northamerica-northeast2, northamerica-south1, southamerica-east1, southamerica-west1, us-east5, us-south1, us-west, and us-west3.

### Changed

New [Airflow builds](https://cloud.google.com/composer/docs/composer-versions#images-composer-3) are available in Cloud Composer 3:

* [composer-3-airflow-2.10.5-build.5](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-10-5-build-5) (default)
* [composer-3-airflow-2.9.3-build.25](https://cloud.google.com/composer/docs/versions-packages#composer-3-airflow-2-9-3-build-25)

### Changed

New [images](https://cloud.google.com/composer/docs/composer-versions#images-composer-2) are available in Cloud Composer 2:

* [composer-2.13.3-airflow-2.10.5](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-3-airflow-2-10-5) (default)
* [composer-2.13.3-airflow-2.9.3](https://cloud.google.com/composer/docs/versions-packages#composer-2-13-3-airflow-2-9-3)

### Deprecated

Cloud Composer version 2.8.1 has reached its [end of support period](https://cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support).

---
## 2025-05-29

### Feature

The [Composer Local Development CLI tool](https://cloud.google.com/composer/docs/composer-3/run-local-airflow-environments) is now available in Cloud Composer 3. This tool helps to streamline testing and developing by providing local Airflow environments based on Airflow builds used by Cloud Composer 3.

---
