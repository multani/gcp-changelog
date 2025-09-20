# Cortex Framework

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
