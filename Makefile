install:
	poetry install


publish:
	poetry publish --dry-run


build:
	poetry build


gendiff:
	poetry run gendiff


package-install:
	python3 -m pip install --force-reinstall dist/*.whl


lint:
	flake8


test:
	poetry run pytest


test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests

codeclimate:
	codeclimate-test-reporter < coverage.xml
