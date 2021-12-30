install: ## Install dependencies
	@poetry install

build: ## Check and builds a package
	@poetry build
build-reinstall:
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl
package-install:
	python3 -m pip install --user dist/*.whl
test:
	poetry run pytest
lint: ## Run linter
	poetry run flake8 page-loader
