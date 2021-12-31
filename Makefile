install:
	poetry install

lint:
	poetry run flake8 page_loader tests

test:
	poetry run pytest --cov=page_loader --cov-report xml tests/

coverage:
	poetry run coverage xml

build:
	poetry build

package-install:
	pip install --user dist/*.whl
