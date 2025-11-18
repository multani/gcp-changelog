# Buildpacks

## 2025-11-14

### Feature

Cloud Run and Cloud Run functions source deployments support `pyproject.toml`
file for managing dependencies. If you use a `pyproject.toml` file, source deployments
use one of the following to find and install dependencies:

* `pip`
* `uv`
* `poetry`

For more information, see [Deploy Python applications with a `pyproject.toml`
file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml) (Preview).

---
## 2025-09-18

### Feature

Ubuntu 24 builder with the `google-24` stack is available for Google Cloud's Buildpacks. For more information, see [Builders](https://cloud.google.com/docs/buildpacks/builders) and [Use a specific builder](https://cloud.google.com/docs/buildpacks/use-a-specific-builder).

---
## 2025-08-14

### Feature

The Python buildpack supports Cloud Run source deployments for modern web frameworks such as [FastAPI](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-fastapi-service.md), [Gradio](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-gradio-service), and [Streamlit](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-streamlit-service).

For Python version 3.13 and later, the Python buildpack sets the default entrypoint for [Cloud Run source deployments](https://cloud.google.com/run/docs/deploying-source-code) based on the web server or framework configuration in your `requirements.txt` file. For more information, see [Build a Python application](https://cloud.google.com/docs/buildpacks/python#entrypoint).

---
