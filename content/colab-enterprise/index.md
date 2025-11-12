# Colab Enterprise

## 2025-11-10

### Feature

The default latest Python version is now 3.12. See
[Python versions](https://docs.cloud.google.com/colab/docs/runtimes#python).

---
## 2025-10-20

### Feature

**Visualization cells**

[Preview](https://cloud.google.com/products#product-launch-stages): You can
use visualization cells to generate interactive and editable visualizations
from within a Colab Enterprise notebook. You can configure the
chart type, aggregation, colors, labels, and other aspects of the
visualization to help you explore data and discover insights. For more
information, see [Use visualization cells](https://docs.cloud.google.com/colab/docs/visualization-cells).

---
## 2025-10-14

### Feature

**SQL cells**

[Preview](https://cloud.google.com/products#product-launch-stages): You can
use SQL cells to write, edit, and run SQL queries directly from your
Colab Enterprise notebooks. For more information, see
[Use SQL cells](https://docs.cloud.google.com/colab/docs/sql-cells).

---
## 2025-10-07

### Feature

**Post-startup scripts**

[Preview](https://cloud.google.com/products#product-launch-stages): You can
use a post-startup script to perform tasks after the startup process
of your Colab Enterprise runtime. For example, you can use
a post-startup script to install specific packages or make specific
changes to your runtime's VM. For more information, see
[Use a post-startup script](https://docs.cloud.google.com/colab/docs/post-startup-script).

---
## 2025-08-05

### Feature

[Generally available](https://cloud.google.com/products#product-launch-stages): You can consume reservations with Colab Enterprise runtimes. Reservations of Compute Engine zonal resources help you gain a high level of assurance that your runtimes have the necessary resources to run. For more information, see [Use reservations with Colab Enterprise](https://cloud.google.com/colab/docs/reservations).

---
## 2025-08-04

### Feature

You can now use the new Data Science Agent to automate exploratory data analysis, perform machine learning tasks, and deliver insights from within a Colab Enterprise notebook. To get started, see [Use the Data Science Agent](https://cloud.google.com/colab/docs/use-data-science-agent). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-06-30

### Feature

[Preview](https://cloud.google.com/products#product-launch-stages): You can consume reservations with Colab Enterprise runtimes. Reservations of Compute Engine zonal resources help you gain a high level of assurance that your runtimes have the necessary resources to run. For more information, see [Use reservations with Colab Enterprise](https://cloud.google.com/colab/docs/reservations).

---
## 2025-05-28

### Feature

Python 3.11 is now available in Colab Enterprise. Existing runtimes and runtime templates will remain using Python 3.10. For more information, see [Python versions](https://cloud.google.com/colab/docs/runtimes#python).

### Feature

When you create a runtime template, you can now configure it to use the latest Python version available to Colab Enterprise, or you can specify the Python version. Using `Latest` is a new option that means when a new version of Python is introduced to Colab Enterprise, runtimes that you create will use the latest Python version.

Existing runtime templates and runtimes remain using their current Python version (Python 3.10). This includes existing auto-generated default runtime templates. To create default runtime templates that use `Latest`, you must do one of the following:

* Delete the existing default runtime templates. Then, when a new default runtime template is created, the Python version will be set to Latest.
* [Change a runtime template's Python version](https://cloud.google.com/colab/docs/runtimes#change-python-version) by using the REST API.

---
