# Cloud Deploy

## 2026-07-10

### Change

The Cloud Deploy image now uses a Google-specific fork of Skaffold. The
Skaffold version that you see if you run `gcloud deploy releases describe`, or
if you view the release in the Google Cloud Console, is now `cd-skaffold`
instead of a version number.

---
## 2026-06-15

### Change

The Cloud Deploy image now uses Kubectl Kustomize.

By default, Cloud Deploy now uses the
[Kustomize built into kubectl](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_kustomize/).
Previously, the default version of Kustomize was the version embedded in the
Cloud Deploy image. Now it's the version used by kubectl.

You can still use kustomize directly (not through kubectl) by specifying the
kustomize version when you create a release.

---
## 2026-04-14

### Change

Support for [deploying Cloud Run worker pools](https://docs.cloud.google.com/deploy/docs/run-targets) is now
generally available
([GA](https://cloud.google.com/products#product-launch-stages)).

---
## 2026-03-23

### Feature

You can now [analyze the performance of your deployed applications](https://docs.cloud.google.com/deploy/docs/analysis)
using the monitoring platform of your choice and
[automatically trigger actions](https://docs.cloud.google.com/deploy/docs/automation-rules)
such as rollbacks. This feature is
[generally available](https://cloud.google.com/products#product-launch-stages).

### Feature

You can now provide user-defined actions using [`tasks`](https://docs.cloud.google.com/deploy/docs/tasks).
This includes [deploy hooks](https://docs.cloud.google.com/deploy/docs/hooks),
[deployment verification](https://docs.cloud.google.com/deploy/docs/verify-deployment),
[analysis](https://docs.cloud.google.com/deploy/docs/analysis), and [custom target types](https://docs.cloud.google.com/deploy/docs/custom-targets).
This feature is
[generally available](https://cloud.google.com/products#product-launch-stages).

---
## 2026-03-02

### Feature

Cloud Deploy is now available in the following region: asia-southeast3 (Bangkok)

---
## 2026-02-11

### Feature

You can now
[deploy containerized workloads to Cloud Run worker pools](https://docs.cloud.google.com/deploy/docs/run-targets#create_your_worker_pool_definitions)
(in [Preview](https://cloud.google.com/products#product-launch-stages)).

---
## 2026-01-23

### Change

The limit on deployment minutes per delivery pipeline has been removed. The only
quota now enforced in Cloud Deploy is the system limit of 18,000 API
requests per minute per region. [Learn more](https://docs.cloud.google.com/deploy/quotas).

---
## 2025-12-12

### Change

We now [upgrade the tools used for deployments more frequently](https://docs.cloud.google.com/deploy/docs/select-tool-version).
This includes tools like Skaffold, Kubectl, and Helm. You can also
[select specific versions](https://docs.cloud.google.com/deploy/docs/select-tool-version#how_select) of these
tools when you create a release.

---
## 2025-09-02

### Feature

You can now use custom constraints with Organization Policy to provide more granular control over specific fields for some Cloud Deploy resources. For more information, see [Use custom organization policies](https://cloud.google.com/deploy/docs/custom-org-policy).

---
