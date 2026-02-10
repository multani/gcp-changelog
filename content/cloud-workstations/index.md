# Cloud Workstations

## 2026-02-06

### Feature

You can provide [custom metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) for a
workstation's host VM.

Use the `--instance-metadata` flag with the
[`gcloud workstations configs create`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/create)
and [`gcloud workstations configs update`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/update)
commands. Format the metadata as a comma-separated list of key-value pairs—for
example, `--instance-metadata=key1=value1,key2=value2`.

Note that updating metadata replaces all existing custom metadata for the
workstation instance.

### Feature

Cloud Workstations supports specifying a custom startup script to be executed on
the workstation's host VM during boot.

Provide the custom startup script as a Google Cloud Storage URL, such as
`gs://BUCKET/FILE`, using the `--startup-script-uri` flag with the
[`gcloud workstations configs create`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/create) and [`gcloud workstations configs update`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/update)
commands.

---
## 2026-01-31

### Feature

Cloud Workstations supports [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) (`hyperdisk-balanced-ha`) for persistent directories on configurations using A3, C3, C4, G4, M3, N4, N4D, and Z3 machine series. You can specify the disk type using the `--disk-type` flag with the [`gcloud workstations configs create`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/create) and [`gcloud workstations configs update`](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/configs/update) commands.

Cloud Workstations supports A3 machine types with Hyperdisk only. For more details, see [Available machine types](https://docs.cloud.google.com/workstations/docs/available-machine-types) and [Available GPUs](https://docs.cloud.google.com/workstations/docs/available-gpus).

---
## 2025-12-05

### Change

Cloud Workstations predefined images include
[Node.js](https://nodejs.org/) 24 (LTS). The previous version, 20.19.6, is no
longer pre-installed. To continue using a previous version, you can
[customize your container images](https://docs.cloud.google.com/workstations/docs/customize-container-images)
to include it or add a version manager like [NVM](https://www.nvmnode.com/).

### Change

Cloud Workstations predefined images include
[Eclipse Temurin](https://adoptium.net/temurin) JDK 21 and 25. JDK 11 is no longer
pre-installed. To continue using JDK 11,
[customize your container images](https://docs.cloud.google.com/workstations/docs/customize-container-images).

---
## 2025-07-07

### Feature

Cloud Workstations is available in the `europe-central2` region (Warsaw). For more information, see [Locations](https://cloud.google.com/workstations/docs/locations).

---
## 2025-06-09

### Feature

The JetBrains [readiness server](https://cloud.google.com/workstations/docs/develop-code-using-local-jetbrains-ides#add_a_server_readiness_check) lets you configure the port it listens on and the timeout when you specify the `JETBRAINS_READY_SERVER_PORT` and `JETBRAINS_READY_SERVER_TIMEOUT` environment variables in your workstation environment. For more information about setting environment variables, see [Customizing your environment](https://cloud.google.com/workstations/docs/create-configuration#customize_environment).

---
## 2025-06-03

### Changed

The [JetBrains CLion preconfigured base image](https://cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [CLion 2025.1.1](https://youtrack.jetbrains.com/articles/CPP-A-230654398/CLion-2025.1.1-251.25410.104-build-Release-Notes)

### Changed

The [JetBrains GoLand preconfigured base image](https://cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [GoLand 2025.1.1](https://youtrack.jetbrains.com/articles/GO-A-231735963/GoLand-2025.1.1-251.25410.140-build-Release-Notes)

### Changed

The [JetBrains IntelliJ Ultimate preconfigured base image](https://cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [IntelliJ-IDEA 2025.1.1](https://youtrack.jetbrains.com/articles/IDEA-A-2100662430/IntelliJ-IDEA-2025.1.1.1-251.25410.129-build-Release-Notes)

### Changed

The [JetBrains PhpStorm preconfigured base image](https://cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [PhpStorm 2025.1.1](https://youtrack.jetbrains.com/articles/WI-A-231736231/PhpStorm-2025.1.1-251.25410.148-build-Release-Notes)

### Changed

The [JetBrains WebStorm preconfigured base image](https://cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [WebStorm 2025.1.1](https://youtrack.jetbrains.com/articles/WEB-A-233538594/WebStorm-2025.1.1-251.25410.117-build-Release-Notes)

### Changed

The [JetBrains RubyMine preconfigured base image](https://cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [RubyMine 2025.1.1](https://youtrack.jetbrains.com/articles/RUBY-A-220365264/RubyMine-2025.1.1-251.25410.120-build-Release-Notes)

### Changed

The [JetBrains PyCharm preconfigured base image](https://cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [PyCharm 2025.1.1.1](https://youtrack.jetbrains.com/articles/PY-A-233538403/PyCharm-2025.1.1.1-251.25410.159-build-Release-Notes)

### Changed

The [JetBrains Rider preconfigured base image](https://cloud.google.com/workstations/docs/preconfigured-base-images#list_of_preconfigured_base_images) uses [Rider 2025.1.2](https://youtrack.jetbrains.com/issues?q=project:%20Rider%20%7Bavailable%20in%7D:%20%7B2025.1.2%20(251.25410.119)%7D)

---
