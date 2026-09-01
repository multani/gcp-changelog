# Cortex Framework

## 2026-09-01

### Release 7.0.5



### Fixed

* Removed obsolete review items checklist from tests.

---
## 2026-08-26

### Release 7.0.4



### Fixed

* Removed unused dependencies (pandas, pytest-bigquery-mock) and lockfile cleanup.

---
## 2026-08-14

### Release 7.0.3



### Fixed

* Resolved an issue where `SapBdcProductBuilder` incorrectly enforced SAP-versioned sections (ecc, s4, common) in `table_settings`.

---
## 2026-08-11

### Release 7.0.2



### Fixed

* Resolved security vulnerabilities in transitive dependencies by updating the following corresponding direct dependencies: `google-auth`, `google-cloud-bigquery`, `google-cloud-dataform`, `google-cloud-resource-manager`, `google-cloud-service-usage` and `google-cloud-storage`.

---
## 2026-08-07

### Release 7.0.1



### Fixed

* Resolved an issue where running the [`uv run cortex-build`](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-build) command in Windows PowerShell or Windows Command Prompt resulted in a `Could not auto-import local builder` warning and an `Invalid builder type NoneType for category ...` error.
* Improved Dataform quota management in [`uv run cortex-deploy`](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-deploy) script.

---
## 2026-07-30

### Release 7.0.0-GA (General Availability)

**Note: Important upgrade considerations for Version 7**

* **Upgrading from v6:** Because v7 is a new major version it implies breaking changes with no automatic migration path. For v6 customers looking to adopt v7, we provide [v6 compatibility content for SAP reporting.](https://docs.cloud.google.com/cortex/docs/v6-compatibility)
* **Upgrading from a v7 Preview:** Due to configuration model improvements, you must recreate your configuration files and re-deploy

### Feature

Google Cloud Cortex Framework version 7 is now generally available. Version 7 introduces a modular deployment architecture, simplified data orchestration via [Dataform](https://cloud.google.com/dataform/docs), and AI-ready data products with [BigQuery](https://cloud.google.com/bigquery/docs) and [Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog) integration. This enables enterprises to build, extend, and deploy data assets and pipelines for advanced analytics and agentic use cases with less risk, complexity, and cost.

**New features and enhancements**

*additional to those released in preview*

AI, discovery, and governance:

* **[New agentic data product builder skills](https://docs.cloud.google.com/cortex/docs/agentic-skills-for-data-product-building)**: Automate the creation and customization of data products using natural language.
* **[New Knowledge Catalog integration](https://docs.cloud.google.com/cortex/docs/knowledge-catalog)**: Automatically synchronize deployed Cortex Framework data products and enriched metadata directly into Knowledge Catalog for discovery and governance.

Expanded data product content and integrations:

* **[New data products available for SAP ERP](https://docs.cloud.google.com/cortex/docs/data-product#available_data_products)**: Access an expanded number of Cortex Framework delivered data products for SAP ECC and SAP S/4HANA.
* **[New support for SAP Business Data Cloud data products](https://docs.cloud.google.com/cortex/docs/source-system-integration/sap-bdc)**: Register your SAP BDC data products with Cortex Framework for expanded use case opportunities on top.
* **[New solution samples features](https://docs.cloud.google.com/cortex/docs/solution-samples/overview)**: Consumption data product samples for SAP ERP and SAP BDC can now be easily deployed on top of Cortex Framework managed data products.
* **[New v6 compatibility for SAP reporting](https://docs.cloud.google.com/cortex/docs/v6-compatibility)**: Provides an option to use Cortex Framework version 6 delivered SAP BigQuery data models within the version 7 architecture to support customers looking to migrate while continuing to use v6 delivered Looker reports.

Supportability and operations:

* **[New observability features](https://docs.cloud.google.com/cortex/docs/observability)**: Enhanced error reporting and pipeline monitoring.
* **[New environment management and operations features](https://docs.cloud.google.com/cortex/docs/deployment)**: Gain deeper control over deployments with the option to provide compilation overrides that integrate cleanly with Dataform release configurations.

### Change

Google Cloud Cortex Framework version 7 includes [telemetry](https://docs.cloud.google.com/cortex/docs/telemetry)
to capture anonymized deployment statistics. This data helps the solution build
team focus on improving modules with high adoption. Telemetry is enabled by
default, but you can opt out at any time.

---
## 2026-06-25

### Release 7.0.0-preview.2.1 (Public Preview)



### Fixed

* **Configuration**: Fix for `tableSettings` path resolution issue.

---
## 2026-06-24

### Release 7.0.0-preview.2 (Public Preview)



### Feature

* **[Data products for SAP ERP](https://docs.cloud.google.com/cortex/docs/data-product)**: Additional data product accelerators including: accounting documents, accounts payable, accounts receivable, addresses, agency business settlement documents, billing documents, business partners, condition contracts, controlling areas and cost elements, cost and profit centers, currency conversion, financial statement structure & versions, fiscal year variants, fixed assets, general ledger accounts, global settings, plants and storage, project structure, units of measurement, universal journal, and vendor invoices.
* **[Extensibility guide](https://docs.cloud.google.com/cortex/docs/extensibility-guide)**: Documentation explaining how to customize and extend Cortex Framework, organized by three steps: [Custom namespace setup](https://docs.cloud.google.com/cortex/docs/extensibility-guide-namespaces), [Data foundation module creation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-foundation), and [Data product module creation](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-product).

---
## 2026-04-30

### Release 7



### Feature

Cortex Framework **version 7** introduces a highly modular deployment architecture, simplified data orchestration via [Dataform](https://docs.cloud.google.com/dataform/docs), and enhanced support for the next generation of AI-ready data products with [BigQuery](https://docs.cloud.google.com/bigquery/docs) - enabling enterprises to build, extend, and deploy robust data models and pipelines for advanced analytics and AI/agentic use cases. To request access to the GitHub repository, see [Request access](https://docs.cloud.google.com/cortex/docs/request-access).

* **Key architecture features**

  + **Modular deployment and smart dependency resolution**: Deploy exactly what you need. Simply select the desired data products, and the framework will automatically identify, retrieve, and transform the necessary tables to the data foundation layer, ensuring no unnecessary data is processed. Easily add custom fields or logic without breaking standard models.
  + **Native dependency graph generation**: Automatically handle the order of operations for complex data models, ensuring prerequisite tables are ready before deploying data foundations and data products.
  + **Bring your own CDC (External data foundation)**: A flexible architecture allows you to bypass built-in Change Data Capture processing and connect your own existing CDC pipelines directly to the foundation layer.
  + **Serverless BigQuery-native execution**: Orchestration relies entirely on Google Cloud Dataform, enabling easy data transformation and processing using version-controlled SQL. No standing compute clusters or Airflow VMs are required, minimizing infrastructure overhead.
  + **Incremental loading**: Native, incremental loading configurations ensure highly efficient processing of large enterprise datasets. Significantly reduce BigQuery processing time and costs by processing only new or changed data since the last execution.
  + **High data fidelity & semantics**: Features dynamic discovery and ingestion of custom fields, robust semantic mapping (e.g. translating cryptic table names to business-friendly terms), AI-ready metadata, and advanced logic handling (e.g. integrating the SAP TCURX table for exact currency decimal shifts).
  + **Multi-system SAP support**: Built-in dynamic dependency resolution and logic differentiation allows seamless compilation and parallel deployment for both SAP ECC and SAP S/4HANA source systems. Seamlessly bring in data from multiple SAP ERP systems.
  + **Extensibility framework**: Maintain a clean separation between your custom data products and Cortex Data Products using namespaces. This ensures you can benefit from the latest Cortex updates without impacting your custom work.
* **Data product accelerators**

  BigQuery based [data product accelerators for SAP ERP](https://docs.cloud.google.com/cortex/docs/data-product#data_source_specific_data_products_for_sap_erp)
  (SAP ECC and S/4HANA), purpose-built for
  AI-readiness with agent-friendly metadata included for all data model and
  field-level descriptions.
* **Solution samples for SAP ERP or SAP BDC**

  Solution reference architectures and code snippets for demonstrating
  how to build use cases on top of Cortex Framework data
  products to address particular business needs.

  + **[Sales Performance Insights](https://docs.cloud.google.com/cortex/docs/sales-performance-insights)**: How to accelerate
    insights into sales performance health using SAP ERP or SAP BDC sourced data.
  + **[Supplier Spend Analysis](https://docs.cloud.google.com/cortex/docs/supplier-spend-analysis)**: How to accelerate insights
    into supplier spend position using SAP ERP or SAP BDC sourced data.

---
## 2026-02-27

### Release 6.3.4



### Fixed

* **Airflow v3 support**:
  + All Composer DAGs generated by new deployments are now compatible
    with Airflow v3.
  + Airflow v2 is still supported. However, consider
    [planning for migration](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html)
    as [it will soon reach end-of-life](https://www.astronomer.io/airflow-2-eol/).
* **SAP:**
  + SAP CDC scripts now support custom tables containing forward slashes
    (`/`) in their names. Existing deployments are not affected.
  + Added optional `adrt` table to SAP CDC table list.
* **Cortex for Marketing:**
  + Meta API is now upgraded from v21 to v25. For field name changes, see
    [changelog](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog/).
* **Minor fixes:**
  + Migrated Cloud SDK to `gcloud storage` CLI.
  + Fixed for line breaks in DAG packages import.
  + Improved error handling for target bucket access verification.

---
## 2025-12-17

### Fixed

* **SAP**: Added support for future dates to `currency_conversion`.
* **Cloud Build Image**: Updated gcloud SDK to v541 and Python library
  dependencies used during Cloud Build deployment.
* **Composer DAG**: Corrected propagation of location parameterization.
* **Cortex for Marketing**: Updated references to Google Ads API v22.

### Change

* **SAP**: The column `DUMMY_SDDOCPARTNER_INCL_EEW_PS` has been removed from
  *SalesOrderPartnerFunction* (ECC and S/4) as it is a non-standard column not
  used for reporting.

### Deprecated

* **SAP**: Cortex's Data Mesh functionality has been deprecated. This change
  is prompted by the evolution of Google Cloud data management services. The Data
  Mesh solution was built using Data Catalog for metadata management, which is
  now being replaced by the more advanced
  [Dataplex Universal Catalog](https://docs.cloud.google.com/dataplex/docs/introduction).
  Dataplex Universal Catalog provides a unified API, enhanced metadata capabilities, and
  new features for a more comprehensive data governance experience. For existing
  Cortex Framework users who have implemented the Data Mesh feature, we recommend
  transitioning to Dataplex Universal Catalog to ensure continued support and access to the
  latest features. For a detailed migration guide, see
  [Transition to Dataplex Universal Catalog](https://cloud.google.com/dataplex/docs/transition-to-dataplex-catalog).

### Release 6.3.3



---
## 2025-09-19

### Changed

* **1-Click Deployer**: 1-Click deployer now deploys the
  [Sustainability](https://cloud.google.com/cortex/docs/dun-and-bradstreet) module when SAP ECC or S/4 is selected.
* **SAP**:
  + The CDC script now considers the `L` flag alongside `I` and `U` when
    determining which records are updated in the raw dataset. This is to account
    for situations where the pipeline is somehow re-configured after data load,
    but the CDC dataset can still be reused to avoid re-processing existing data.
  + Column names in `StockInHand` views (ECC and S/4) for `MATNR` and
    `WERKS` have been aligned with other views to be `MaterialNumber_MATNR`
    and `Plant_WERKS`. Previous column names `ArticleNumber_MATNR` and
    `Site_WERKS` still exist for compatibility reasons, but will be removed in
    a future release. Customers are advised to change their upstream consumption assets accordingly.
  + Column names in `SalesOrders_V2` views (ECC and S/4) for `ERDAT` and
    `ERZET` have been aligned to new names `SalesDocumentCreationDate_ERDAT`,
    `SalesOrderItemCreationDate_ERDAT`, `SalesOrderCreationTime_ERZET` and
    `SalesDocumentItemCreationTime_ERZET` to account for the correct
    granularity of their source table (either `VBAP` or `VBAK`) . Previous
    column names `CreationDate_ERDAT` and `CreationTime_ERZET` still exist for
    compatibility reasons, but will eventually be removed in a future release.
    Customers are advised to change their upstream consumption assets
    accordingly. Also, Sales Order Item level calendar dimensions are now added
    by default.
  + Column names in `Deliveries` view for `VGBEL`, `VGPOS`, and `XBLNR` are
    updated to `InternalReferenceDocumentNumber_VGBEL`,
    `InternalReferenceDocumentItem_VGPOS` `ExternalReferenceDocumentNumber_XBLNR`
    for more clarity. Previous column names `SalesOrderNumber_VGBEL`,
    `SalesOrderItem_VGPOS`, and `ReferenceDocumentNumber_XBLNR` still exist for
    compatibility reasons, but will eventually be removed in a future release.
    Customers are advised to change their upstream consumption assets
    accordingly.
  + Sales Order Item level calendar dimensions are now added by default.
  + In `AccountingDocuments` view as well as the downstream
    `AccountingDocumentsReceivables` views, `DoubtfulReceivables`, and
    `DaysInArrear` metrics are now positive instead of negative to align with
    [official SAP guidelines](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/3cb1182b4a184bdd93f8d62e3f1f0741/39a73b581aee2160e10000000a44147b.html).
  + `SalesFulfillment` and `SalesFulfillment_PerOrder` views are updated
    to use `SalesOrders_V2` instead of `SalesOrders` view as their upstream
    source for both ECC and S/4. The view signatures are unchanged.
  + ERD for both [ECC](https://cloud.google.com/cortex/docs/operational-sap#sap-ecc) and
    [S/4](https://cloud.google.com/cortex/docs/operational-sap#sap-s4-hana) have been cleaned up and
    updated based on the latest changes.
* **Marketing**: Cortex for Meridian reporting views adapted to TikTok, Meta,
  and YouTube (DV360) to focus on top of the funnel marketing campaigns. Search
  Ads data is skipped from aggregates as higher quality data is now available from
  Marketing Mix Modeling (MMM) Data Platform.

### Fixed

* **SAP**:
  + `Qty` field data type in `StockInHand` views (ECC and S/4) has been
    changed from `STRING` to `NUMERIC`.
  + Currency conversion and currency decimal shift in `PurchaseDocuments_Flow`
    views (ECC and S/4) now align with the logic implemented in all other SAP
    reporting views.
  + Fixed incorrect GR quantity caused by an incorrect `JOIN` condition.
  + Removed an excessive `LEFT JOIN` in the Unit of Measure Function and View
    Utility code to avoid possible duplicate rows.
  + Cleaned up unnecessary date casting and `ORDER BY` clauses in some views
    to improve performance.
* **Salesforce (SFDC):**
  + Currency conversion logic is now updated to account for possible source
    currency fields that are not corporate currency in the objects
    (for example, `Opportunities`).
  + Updated ERD to include proper linkage to calendar dimension.

### Deprecated

* **SAP**: The views `GLDocumentsHdr` and `RegionsMD` are now removed as
  they are no longer relevant.

### Issue

* **Oracle** builds may time out when using a private worker pool created
  with default parameters.

### Release 6.3.2



---
