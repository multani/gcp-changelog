DOCKER_IMAGE = local/NAME

all: fmt

.PHONY: fmt
fmt:
	uv run ruff format
	uv run ruff check --fix

.PHONY: check
check:
	uv run pytest --mypy --ruff --ruff-format

.PHONY: mypy
mypy:
	uv run mypy

.PHONY: doc
doc:
	uv run mkdocs build --strict
