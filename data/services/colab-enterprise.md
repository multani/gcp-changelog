# Colab Enterprise

## 2025-05-28

### Feature

Python 3.11 is now available in Colab Enterprise. Existing runtimes and runtime templates will remain using Python 3.10. For more information, see [Python versions](https://cloud.google.com/colab/docs/runtimes#python).

### Feature

When you create a runtime template, you can now configure it to use the latest Python version available to Colab Enterprise, or you can specify the Python version. Using `Latest` is a new option that means when a new version of Python is introduced to Colab Enterprise, runtimes that you create will use the latest Python version.

Existing runtime templates and runtimes remain using their current Python version (Python 3.10). This includes existing auto-generated default runtime templates. To create default runtime templates that use `Latest`, you must do one of the following:

* Delete the existing default runtime templates. Then, when a new default runtime template is created, the Python version will be set to Latest.
* [Change a runtime template's Python version](https://cloud.google.com/colab/docs/runtimes#change-python-version) by using the REST API.

---
