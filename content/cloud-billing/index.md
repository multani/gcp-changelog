# Cloud Billing

## 2026-09-04

### Change

**Introducing the Incentives page, for tracking spend-based milestone credits,
RaMP, and other conditional incentives**

If you have a custom pricing contract, you might be enrolled in conditional
incentives, where you earn credits or discounts for spending specific amounts
on Google Cloud.

The [**Incentives page**](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker)
replaces the
[*Spend-based Milestones tab*](https://docs.cloud.google.com/billing/docs/release-notes#July_22_2024)
that was located in the *Credits* page. The Incentives page provides a
consolidated and enhanced experience for tracking your progress towards
conditional incentives, including spend-based milestone credits and Rapid
Migration & Modernization Program (RaMP) credits and discounts.

Learn more about
[tracking conditional incentives](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker).

---
## 2026-08-07

### Feature

**New filter and group-by option available in Cloud Billing Reports**

In **Billing Reports**, Cloud Billing has added the
**Originating products**
[*filter*](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-orig-products) and
[*Group by*](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-orig-product)
to provide additional options that let you analyze and understand your costs.
*Originating products* are Google Cloud products that cause usage in
another product. For example, Gemini Enterprise is an
originating product when it causes usage in the Gemini Enterprise
app.

To help you **track and analyze your *AI spend***, the *Originating products*
dimension is used in the following ways:

* You can use the *Originating products* filter and group by option to
  configure your Cloud Billing report to track and analyze your
  [Gemini Enterprise subscription and consumption costs](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs).
* The *Originating products* dimension supports a new
  [*preset report*](https://docs.cloud.google.com/billing/docs/how-to/reports#preset_views)
  for quick report configuration, called
  [Gemini Enterprise costs by SKU](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs#preset-report).
* When you are viewing your costs in the Gemini Enterprise console,
  on the *Gemini Enterprise > Usage & Spending* page,
  the *Originating products* dimension supports the functionality of the costs
  displayed on the
  [Gemini Enterprise Billing tab](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs).

For more information, see the following resources:

* [Learn how to view Gemini Enterprise costs in Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs)
* [Learn more about analyzing billing data and cost trends with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports)
* [Learn how to view Gemini Enterprise costs in the Gemini Enterprise console](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs)

---
## 2026-07-27

### Feature

**Spend cap budgets are now available for a limited set of services (Preview)**

Available in [Preview](https://cloud.google.com/products#product-launch-stages)
for
[eligible services](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#eligible-services),
you can now configure a
[**spend cap budget**](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps)
to automatically pause usage when your spend exceeds the budget amount you set.

Spend caps are a cost control mechanism. A spend cap is enforced when usage
costs exceed your budget target amount. When enforced, any new request to the
eligible services, within the specified project, are paused and no further
usage costs are accrued until you manually lift the spend cap.

Spend caps typically use *estimated costs* to trigger the alerts and caps,
enforcing a cap much faster than the *actual costs* are processed and appear
on billing reports. Even though faster than reports, the enforcement of spend
caps isn't instant and any cost overages are billed as normal.

For more information about spend cap budgets, see:

* [How spend cap budgets work to help you control spend](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#how-spend-cap-budgets-work)
* [Configure a spend cap budget](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#configure-spend-cap)
* [Lift an enforced spend cap](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#lift-spend-cap)
* [Limitations of spend cap budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#limitations)

---
## 2026-07-24

### Feature

**Early signals for AI workloads**

For AI workloads (such as Gemini API and Vertex AI),
you can now view early anomalies. Early anomalies use near real-time cost
estimates to provide daily, service-level insights before finalized billing
occurs. You can view these alerts on the **By service (Early signals)** tab
on the Anomalies dashboard in the Google Cloud console. User-configured
thresholds do not apply to early anomalies.

For more information, see
[View early anomalies for AI workloads](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies#view-early-anomalies).

---
## 2026-07-10

### Feature

**Payments documents for invoiced billing accounts available on Payment
status page**

For
[Cloud Billing accounts that are paid by invoice](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types),
access to your payments documents, such as invoices and credit memos, is now
available in the Cloud Billing console in the **Payment status** page.

The **Payment status** page replaces the **Invoices** page. Self-service
(online) Cloud Billing accounts will continue to access Payments
documents on the **Invoices** page.

The **Payment status** page provides a real-time and customizable view of your
financial standing with your Cloud Billing account. The Payment status
page is based on the
[Google payments **Statement of account**](https://support.google.com/paymentscenter/answer/7520537)
page, with your payments documents filtered by the *Google payments account*
that is linked to the Cloud Billing account that you are viewing.

For more information about payments documents, see:

* [Get a Cloud Billing document such as an invoice, statement, or receipt](https://docs.cloud.google.com/billing/docs/how-to/get-invoice)
* [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)
* [Google payments Statement of account](https://support.google.com/paymentscenter/answer/7520537)

---
## 2026-06-22

### Feature

**Resource-based CUD recommendations available for Compute Engine GPUs, Local SSD disks, and OS licenses**

Resource-based committed use discount (CUD) recommendations are generally available (GA) for GPUs, Local SSD disks, and premium operating system (OS) licenses.

CUD recommendations provide insight into any additional commitments that you can
purchase to optimize the costs of the resources that you run. You can use these
recommendations and purchase commitments for resource usage that isn't covered
by commitments and is being charged at list prices. Google Cloud analyzes your
compute instance spending trends with and without a commitment and generates
CUD recommendations on a monthly basis.

For more information about how CUD recommendations are generated, what resource
types are supported, and how to use recommendations to purchase commitments, see
[Get recommendations for committed use discounts (CUDs)](https://docs.cloud.google.com/docs/cuds-recommender).

---
## 2026-06-17

### Feature

**CUD dashboard redesign available (preview)**

The redesigned CUD dashboard is available in the Billing section of the
Google Cloud console. It provides a consolidated view of all your resource-based
and spend-based CUDs in a single place. The new design improves usability and
scalability, helping you find information faster.

For more information, see [View your commitments](https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview).

---
## 2026-06-15

### Feature

**New filters and group-by options available in Cloud Billing Reports**

Cloud Billing has added two **filters** to the **Billing Reports**
page to help you analyze and understand your costs:

* **Products**: Google Cloud
  [Products](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-products)
  consist of a group of SKUs (potentially from more than one
  [Google Cloud *Service*](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-services))
  that work together and are sold as a single service, sometimes referred to as
  a *logical* product family or a subscription service. Examples include
  Gemini Enterprise and Firebase App Hosting.
* **Originating services**: An
  [Originating service](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-orig-services)
  is a Google Cloud service that causes usage in another service. For
  example, Google Kubernetes Engine (GKE) can cause usage in Compute Engine. In
  this use case, when you are viewing the Compute Engine usage and
  costs, GKE is an originating service when it causes usage
  in Compute Engine.

You can also
[**Group by**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) the new filters, to
summarize your costs by the dimension you select.

* **Product**: When you
  [group by *Product*](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-product),
  the Report shows your costs and savings summarized by Product.
* **Originating service > Service**: When you
  [group by *Originating service > Service*](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-orig-service),
  the Report shows your costs and savings summarized by Originating service.
  In the **report table**, you can expand each row for an *Originating service*
  to see your costs summarized by each *Service* that is associated with the
  *Originating service*.

Learn more about [analyzing billing data and cost trends with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports).

Learn how to [view Gemini Enterprise costs in Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs).

---
## 2026-06-10

### Feature

**Multi-project access to Cloud Billing cost views available in
Preview**

In Cloud Billing accounts, multi-project access to usage costs lets
project owners, solution owners, developers, and other non-billing admins
see cost data for all of their authorized projects in a single view in the
Cloud Billing console.

The multi-project view uses a combination of Cloud Billing account
permissions and Google Cloud project permissions that let Cloud Billing
administrators and organization administrators jointly control access to
project-level cost data.

Using project-scoped Cloud Billing account permissions,
Cloud Billing administrators can control which solution owners can
view aggregated cost data in the Cloud Billing console.

* Learn more about [cost management for project owners](https://docs.cloud.google.com/billing/docs/how-to/project-owners/overview).
* Learn how to [set up multi-project access to costs views](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access).

---
## 2026-06-08

### Feature

**FOCUS billing data export to BigQuery available in Preview**

[Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
now offers a FOCUS billing data export available in
[Preview](https://cloud.google.com/products#product-launch-stages).
The [*FinOps Open Cost and Usage Specification* (FOCUS)](https://focus.finops.org/what-is-focus/)
is an open specification that defines clear requirements for technology billing
data generators to produce consistent cost and usage datasets. The Google Cloud
billing data export using the
[FOCUS specifications](https://focus.finops.org/focus-specification/)
includes FOCUS columns up to
[FOCUS version 1.2](https://focus.finops.org/focus-specification/v1-2/).

For more information about the FOCUS billing data export to BigQuery, refer
to the following documentation:

* [Set up FOCUS Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup)
* [Structure of the FOCUS data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export)
* [FOCUS conformance report](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export#conformance-report)
* [Query examples for FOCUS use cases](https://focus.finops.org/use-cases/?version=v1-2)

---
## 2026-06-01

### Feature

**CUD Analysis is Generally Available**

CUD Analysis has reached general availability (GA). This tool supports the new
spend-based CUD model and provides a unified interface for customers to examine
both spend-based and resource-based CUDs. It offers a consolidated view of
Compute resources including the benefits of both resource-based and spend-based
CUDs.

You can use this tool to do the following:

* **Understand savings**: Understand the financial impact of your commitments.
* **Track key metrics**: Track how effectively your commitments are being
  used.
* **Download data**: Download a CSV file of your daily usage for offline
  analysis and reporting.

For more information, see [Analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).

---
## 2026-04-27

### Feature

**The AI Cost Summary Agent is now available in Preview**

You can now use the AI Cost Summary Agent to analyze your AI costs and gain
critical insights into your AI-related spend. The agent analyzes
spending related to Gemini usage, including Gemini API and
Vertex AI.

This feature is available as a widget on the **Billing Overview** page for your
Cloud Billing account.

For more information, see [Analyze your AI spend with the AI Cost Summary
Agent](https://docs.cloud.google.com/billing/docs/how-to/gemini/ai-cost-summary).

---
## 2026-04-20

### Feature

**GKE workload recommenders now available in the FinOps hub**

You can now view recommendations for right-sizing overprovisioned workloads and
optimizing underprovisioned workloads for Google Kubernetes Engine (GKE)
clusters directly in the FinOps hub.

For more information, see
[Optimize workload resource utilization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-workload-resource-utilization).

---
## 2026-03-30

### Feature

**Scenario modeling for CUD recommendations is generally available**

Scenario modeling for committed use discount (CUD) recommendations is now
generally available (GA). You can simulate scenarios for both spend-based and
resource-based CUDs, and customize recommendations to purchase a commitment that
maximizes your savings.

For more information, see
[Simulate scenarios for CUDs savings](https://docs.cloud.google.com/docs/cuds-recommender#simulate-scenarios).

---
## 2026-03-23

### Change

**Billing account permissions now streamline access to Google payments
profiles and payments accounts**

We've launched a billing IAM permissions update that simplifies
and streamlines Cloud Billing account access to the associated
[Google payments profiles and accounts](https://docs.cloud.google.com/billing/docs/concepts#billing_account), for users who have the `billing.accounts.updatePaymentInfo` permission on their
Cloud Billing account.

**Prior to this update**: *While working in the Cloud Billing console*,
to access and edit the associated Google payments profile and account
information, all Cloud Billing account users **needed *two* sets of
permissions**:

* Identity and Access Management (IAM)
  [permissions on the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  to access and manage the billing account.
* Edit or Admin
  [access permissions on the associated Google payments profile](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions)
  in order to add and edit payment methods, make a manual payment, and update
  payments profile info such as the business name, address,
  tax info, and payments account settings.

**After this permissions update**: Cloud Billing account users with
the `billing.accounts.updatePaymentInfo` permission on the billing account
can access and edit Google payments profile and account information
directly from the Cloud Billing console, without needing additional permissions on the payments profile itself.
This includes users with the
[Billing Account Administrator role](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)
(`roles/billing.admin`) and those granted this permission via a
[custom role](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information).

Note that this permissions update applies only to Cloud Billing
accounts associated with an
[Organization (or Business)](https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types)
Google payments profile type. You can verify your account type on the
[Payment settings](https://console.cloud.google.com/billing/profile)
page in the Cloud Billing console.

With the `billing.accounts.updatePaymentInfo` permission on the billing account,
users can do the following:

* [View payments history](https://docs.cloud.google.com/billing/docs/how-to/view-history) and
  [documents](https://docs.cloud.google.com/billing/docs/how-to/get-invoice) related to the associated
  Google payments profile.
* [Add and edit payment methods](https://docs.cloud.google.com/billing/docs/how-to/payment-methods) on a
  self-serve (online) billing account.
* [Make a manual payment](https://docs.cloud.google.com/billing/docs/how-to/manual-payment) to a
  self-serve (online) billing account.
* [Update payments profile info](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account)
  such as the business name, address, tax info, and payments
  account settings.

Billing account users with the `billing.accounts.updatePaymentInfo` permission
won't have the *Manage users* or *Admin with all permissions* level of access
on the Google payments profile. To *fully manage* a payments
profile and gain
[*Manage users* and *Admin* permissions](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions), billing account users still require additional
[*Google payments user permissions*](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts)
granted on the associated payments profile.

---
## 2026-01-21

### Feature

**CUD recommendations support more machine types**

Resource-based CUD recommendations for cores and RAM now support additional
machine series. For a complete list, see
[Resource-based CUDs supported by recommendations](https://docs.cloud.google.com/docs/cuds-recommender#supported-resource-types-recommendation).

You can access these recommendations using the [FinOps hub user
interface](https://console.cloud.google.com/billing/optimize), programmatically
using the [Recommender API](https://docs.cloud.google.com/recommender/docs/apis), or when you
[export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

---
## 2025-12-16

### Feature

**View granular cost data from Pub/Sub snapshot, subscription, and topic usage
in Cloud Billing exports to BigQuery**

You can now view granular Pub/Sub cost data in the Google Cloud Billing
detailed export. Use the `resource.name` or `resource.global_name` field in the
export to view and filter your detailed snapshot, subscription, and topic usage.

[Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

---
## 2025-10-30

### Feature

**Anomaly Detection is generally available**

View and manage cost spikes that deviate from your typical spend patterns using
the Anomalies dashboard, which is [generally
available](https://cloud.google.com/products#product-launch-stages). Each
anomaly includes a detailed root cause analysis that identifies the top
services, regions, and SKUs that contributed to the spike.

With this launch, we've added the following features to Anomaly Detection:

* Auto-generated anomaly thresholds that update daily based on your usage
  patterns.
* Deviation percentage as a new threshold for you to configure for your
  anomalies.
* Email alerts automatically set up for Billing administrators to help you
  proactively manage your costs.

[Learn more about using Anomaly detection to manage costs](https://cloud.google.com/billing/docs/how-to/manage-anomalies).

---
## 2025-08-08

### Feature

**Personalized saved reports are available in cost Reports.**

For customers who have enabled [Gemini Cloud Assist in Cloud Billing](https://cloud.google.com/billing/docs/how-to/gemini/overview), your custom saved reports that you open frequently now appear in the reports carousel, for quick access. Previously, the reports carousel only provided access to Google-created preset reports.

For more information, see the following topics in the **Reports** dcoumentation:

* [Save and share report views](https://cloud.google.com/billing/docs/how-to/reports#saving-views)
* [Use preset reports for quick configuration](https://cloud.google.com/billing/docs/how-to/reports#preset_views)

---
## 2025-07-16

### Feature

**Spend-based committed use discount (CUD) metadata export to BigQuery (public preview)**

You can now access spend-based CUD metadata programmatically through a BigQuery export. This data provides a comprehensive, daily snapshot of spend-based CUDs, which you can join with other billing data exports for improved CUD reporting and management.

[Learn more about the CUD metadata export](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export).

---
## 2025-07-07

### Feature

**Tags data for *regional* Secret Manager secret usage is available in both the [Standard usage cost export](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) and the [Detailed usage cost export](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).**

Tags for Global secrets have been available since [August 8, 2024](https://cloud.google.com/billing/docs/release-notes#August_08_2024). With this update, you can now tag *Regional secrets* as well.

To learn more about Tags, see [Tags overview](https://cloud.google.com/resource-manager/docs/tags/tags-overview). To learn about using Tags in your cost data exported to BigQuery, see [about tags](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and [query examples with tags](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags).

---
## 2025-06-27

### Changed

**New fields added to Cloud Billing data exports to BigQuery**

To prepare for expanding the spend-based committed use discounts (CUD)s program, we added new data fields to the schema for Cloud Billing standard and detailed data exports to BigQuery. These new fields add more information about the prices charged for your Google Cloud usage and consumption models.

To learn more, see [Billing data and SKU updates for spend-based CUDs](https://cloud.google.com/billing/docs/resources/multiprice-cuds).

---
## 2025-06-24

### Feature

**New, enhanced forecasting model for increased accuracy in cost reports**

Cloud Billing forecasts now better account for seasonality trends, data irregularities, and missing data, using an enhanced forecasting model that leverages AI to factor in various scenarios, such as the following:

* Intelligent handling of transient effects caused by known business events - for example, a new workload migration causing a usage spike.
* Deeper understanding of seasonality - for example, various recurring patterns, such as daily, weekly and monthly cycles in your cloud spend; or for retailers, increases in usage during holiday seasons.
* Adapting to trends to remain relevant in changing environments - for example, new AI spend.

These enhancements, powered by our new machine learning engine, translate to increased forecasting accuracy. By capturing complex trends, multiple seasonalities, and handling data anomalies more intelligently, you'll see a marked improvement in the precision of your cost forecasts.

For more information about the forecasted costs in reports, see
[View you forecasted costs](https://cloud.google.com/billing/docs/how-to/reports#cost-forecast).

---
