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


coverage:
	python -m pytest --cov=python_project_50 --cov-report xml --cov-report term


codeclimate:
	codeclimate-test-reporter < coverage.xml
